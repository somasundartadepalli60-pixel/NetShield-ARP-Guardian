let csrfToken=null;
let currentUser=null;
const loginScreen=document.querySelector('#login-screen');
const passwordChange=document.querySelector('#password-change');
const userChip=document.querySelector('#user-chip');
const authFetch=async(path,options={})=>{
    const headers=new Headers(options.headers||{});
    headers.set('Accept','application/json');
    if(csrfToken && ['POST','PUT','PATCH','DELETE'].includes((options.method||'GET').toUpperCase())) headers.set('X-CSRF-Token',csrfToken);
    const r=await fetch('/api/'+path,{...options,headers});
    const body=await r.text(), type=r.headers.get('content-type')||'';
    let data={};
    if(body && type.includes('json')){try{data=JSON.parse(body)}catch{}}
    if(r.status===401) throw new Error('AUTH_REQUIRED');
    if(!r.ok) throw new Error(data.error||body||`HTTP ${r.status}`);
    return data;
};
function showLogin(message=''){
    document.body.classList.add('login-mode'); loginScreen.classList.add('visible');
    document.querySelector('.sidebar').style.display='none'; document.querySelector('main').style.display='none';
    document.querySelector('#login-error').textContent=message;
}
function showApp(){
    document.body.classList.remove('login-mode'); loginScreen.classList.remove('visible');
    document.querySelector('.sidebar').style.display='flex'; document.querySelector('main').style.display='block';
}
async function establishSession(){
    try{
        const d=await fetch('/api/auth/status',{headers:{Accept:'application/json'}}).then(r=>r.json());
        if(!d.authenticated){showLogin();return false}
        currentUser=d; csrfToken=d.csrf_token||null;
        const loginData=await authFetch('auth/me');
        currentUser=loginData;
        userChip.innerHTML=`<span class="avatar">${esc((loginData.display_name||loginData.username).slice(0,1).toUpperCase())}</span><span>${esc(loginData.display_name||loginData.username)}</span>`;
        showApp();
        if(loginData.must_change_password) passwordChange.classList.add('visible');
        return true;
    }catch(e){showLogin();return false}
}
document.querySelector('#login-form').onsubmit=async e=>{
    e.preventDefault();
    const b=document.querySelector('#login-error'); b.textContent='Authenticating…';
    try{
        const d=await fetch('/api/auth/login',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},
            body:JSON.stringify({username:document.querySelector('#login-user').value,password:document.querySelector('#login-pass').value})});
        const data=await d.json();
        if(!d.ok) throw new Error(data.error||'Sign in failed');
        csrfToken=data.csrf_token; currentUser=data;
        userChip.innerHTML=`<span class="avatar">${esc((data.display_name||data.username).slice(0,1).toUpperCase())}</span><span>${esc(data.display_name||data.username)}</span>`;
        showApp(); render('overview');
        if(data.must_change_password) passwordChange.classList.add('visible');
    }catch(err){b.textContent=err.message}
};
document.querySelector('#logout').onclick=async()=>{
    try{await authFetch('auth/logout',{method:'POST'})}catch{}
    csrfToken=null; currentUser=null; location.reload();
};
document.querySelector('#password-form').onsubmit=async e=>{
    e.preventDefault(); const msg=document.querySelector('#password-error');
    const n=document.querySelector('#new-password').value, n2=document.querySelector('#new-password-2').value;
    if(n!==n2){msg.textContent='New passwords do not match.';return}
    try{await authFetch('auth/change-password',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({current_password:document.querySelector('#old-password').value,new_password:n})});
        passwordChange.classList.remove('visible'); msg.textContent='';
    }catch(err){msg.textContent=err.message}
};

const root=document.querySelector('#app'), title=document.querySelector('#page-title');
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
const fmt=v=>v?new Date(v).toLocaleString():'—';
const badge=v=>`<span class="badge ${esc(v)}">${esc(v).toUpperCase()}</span>`;
async function get(path){
    try{return await authFetch(path)}
    catch(e){if(e.message==='AUTH_REQUIRED'){showLogin('Your session expired. Please sign in again.');}throw e}
}
function metric(label,value,note=''){return `<div class="metric"><span>${label}</span><strong>${value}</strong><small>${note}</small></div>`}
async function overview(){const d=await get('dashboard');return `<div class="metrics">
${metric('DEVICES',d.devices,'Known network identities')}${metric('ARP EVENTS',d.events,'Normalized observations')}
${metric('OPEN ALERTS',d.alerts,'Needs investigation')}${metric('CRITICAL',d.critical,'Highest severity')}
</div><div class="grid"><section class="panel"><div class="panel-head"><h2>Recent ARP activity</h2><div class="panel-actions"><span>${d.suspicious_events} suspicious</span><button type="button" class="button small" id="activity-refresh">Refresh</button></div></div>
<table><thead><tr><th>TIME</th><th>SOURCE</th><th>MAC</th><th>RISK</th><th>RESULT</th></tr></thead><tbody>
${d.recent_events.map(e=>`<tr><td>${fmt(e.timestamp)}</td><td class="mono">${esc(e.source_ip)}</td><td class="mono">${esc(e.source_mac)}</td><td>${e.risk_score}</td><td>${badge(e.detection_result)}</td></tr>`).join('')||'<tr><td colspan="5" class="empty">No events yet.</td></tr>'}</tbody></table></section>
<section class="panel"><div class="panel-head"><h2>Alert queue</h2></div>${d.recent_alerts.map(a=>`<article class="alert"><div><b>${esc(a.alert_type)}</b>${badge(a.severity)}</div><p>${esc(a.message)}</p><small>${esc(a.source_ip)} · risk ${a.risk_score} · ${fmt(a.created_at)}</small></article>`).join('')||'<div class="empty">No alerts.</div>'}</section></div>`}
async function devices(){const rows=await get('devices');return `<div class="page-head"><p>Observed IP/MAC identities and their current trust state.</p></div><section class="panel"><table><thead><tr><th>IP</th><th>MAC</th><th>STATUS</th><th>RISK</th><th>LAST SEEN</th><th>TRUST</th></tr></thead><tbody>${rows.map(d=>`<tr><td class="mono">${esc(d.ip_address)}</td><td class="mono">${esc(d.mac_address)}</td><td>${badge(d.status)}</td><td>${d.risk_score}</td><td>${fmt(d.last_seen)}</td><td><button class="button small trust" data-id="${d.id}">${d.trusted?'Trusted':'Trust'}</button></td></tr>`).join('')||'<tr><td colspan="6" class="empty">No devices discovered.</td></tr>'}</tbody></table></section>`}
async function alerts(){const rows=await get('alerts');return `<div class="page-head"><p>Signals generated by the local detection engine.</p></div><section class="panel">${rows.map(a=>`<article class="alert"><div><b>${esc(a.alert_type)} · ${esc(a.source_ip)}</b>${badge(a.severity)}</div><p>${esc(a.message)}</p><small>Expected ${esc(a.expected_mac||'unknown')} · observed ${esc(a.observed_mac)} · confidence ${Math.round((a.confidence||0)*100)}%</small>${!['resolved','closed','false_positive'].includes(a.status)?`<button class="button small ack" data-id="${a.id}">Acknowledge</button>`:''}</article>`).join('')||'<div class="empty">No alerts recorded.</div>'}</section>`}
async function incidents(){const rows=await get('incidents');return `<div class="page-head"><p>Correlated security incidents and investigation context.</p></div><section class="panel"><table><thead><tr><th>ID</th><th>TITLE</th><th>SEVERITY</th><th>STATUS</th><th>AFFECTED IP</th><th>CREATED</th></tr></thead><tbody>${rows.map(i=>`<tr><td>${i.id}</td><td>${esc(i.title)}</td><td>${badge(i.severity)}</td><td>${badge(i.status)}</td><td class="mono">${esc(i.affected_ip)}</td><td>${fmt(i.created_at)}</td></tr>`).join('')||'<tr><td colspan="6" class="empty">No incidents yet.</td></tr>'}</tbody></table></section>`}
async function arp(){const rows=await get('packets?limit=200');return `<div class="page-head"><p>Normalized ARP observations with detector evidence.</p></div><section class="panel"><table><thead><tr><th>TIME</th><th>SOURCE</th><th>TARGET</th><th>OP</th><th>RISK</th><th>DETECTORS</th></tr></thead><tbody>${rows.map(e=>`<tr><td>${fmt(e.timestamp)}</td><td class="mono">${esc(e.source_ip)}<br>${esc(e.source_mac)}</td><td class="mono">${esc(e.target_ip)}</td><td>${esc(e.operation)}</td><td>${e.risk_score}</td><td>${esc(e.detector_ids||'none')}</td></tr>`).join('')||'<tr><td colspan="6" class="empty">No ARP observations.</td></tr>'}</tbody></table></section>`}
async function rules(){const rows=await get('rules');return `<div class="cards">${rows.map(r=>`<article class="rule"><span class="rule-id">${esc(r.rule_id)}</span><h3>${esc(r.name)}</h3><p>${esc(r.description)}</p><div>${badge(r.severity)} <span class="tag">threshold ${r.threshold}</span><span class="tag">${r.window_seconds}s</span></div></article>`).join('')}</div>`}
async function baselines(){const rows=await get('baselines');return `<div class="page-head"><p>Learned local IP/MAC identities used as historical context.</p></div><section class="panel"><table><thead><tr><th>NETWORK</th><th>IP</th><th>MAC</th><th>OBSERVATIONS</th><th>CONFIDENCE</th><th>LAST SEEN</th></tr></thead><tbody>${rows.map(b=>`<tr><td>${esc(b.network_key)}</td><td class="mono">${esc(b.ip_address)}</td><td class="mono">${esc(b.mac_address)}</td><td>${b.observations}</td><td>${Math.round(b.confidence*100)}%</td><td>${fmt(b.last_seen)}</td></tr>`).join('')||'<tr><td colspan="6" class="empty">Baseline is empty until observations are learned.</td></tr>'}</tbody></table></section>`}
async function interfaces(){const rows=await get('interfaces');return `<div class="cards">${rows.map(x=>`<article class="rule"><span class="rule-id">INTERFACE</span><h3>${esc(x.name)}</h3><p>Address: <span class="mono">${esc(x.address||'unknown')}</span></p>${badge(x.state)}</article>`).join('')}</div>`}
async function reports(){const r=await get('reports/summary');return `<div class="metrics">${metric('DEVICES',r.devices)}${metric('EVENTS',r.events)}${metric('ALERTS',r.alerts)}${metric('SUSPICIOUS',r.suspicious_events)}${metric('HIGH',r.high_alerts)}${metric('CRITICAL',r.critical_alerts)}</div><section class="panel report"><h2>Exports</h2><p>All reporting stays local.</p><a class="button accent" href="/api/reports/events.csv" target="_blank">Export ARP events CSV</a></section>`}
async function audit(){
    const rows=await get('audit');
    const actionCount={}; let actors=new Set(), sensitive=0;
    rows.forEach(a=>{actors.add(a.actor);actionCount[a.action]=(actionCount[a.action]||0)+1;
        if(/auth|trust|acknowledge|password|delete|policy/i.test(a.action)) sensitive++;});
    const topAction=Object.entries(actionCount).sort((a,b)=>b[1]-a[1])[0];
    return `<div class="page-head"><p>Security audit trail — who performed an administrative action, what changed, which resource was affected, and when it happened. Click a row to inspect the recorded details.</p></div>
    <div class="audit-summary">
      <div class="audit-kpi"><b>${rows.length}</b><span>RECENT EVENTS</span></div>
      <div class="audit-kpi"><b>${actors.size}</b><span>UNIQUE ACTORS</span></div>
      <div class="audit-kpi"><b>${sensitive}</b><span>SECURITY-SENSITIVE ACTIONS</span></div>
      <div class="audit-kpi"><b>${topAction?topAction[1]:0}</b><span>MOST COMMON ACTION</span></div>
    </div>
    <section class="panel">
      <div class="panel-head"><h2>Administrative security trail</h2><span>Local-only evidence</span></div>
      <div class="audit-toolbar"><input id="audit-filter" placeholder="Filter actor, action, resource…"><select id="audit-action"><option value="">All actions</option>${Object.keys(actionCount).sort().map(x=>`<option>${esc(x)}</option>`).join('')}</select><button class="button small" id="audit-refresh">Refresh</button></div>
      <table><thead><tr><th>TIME</th><th>ACTOR</th><th>ACTION</th><th>RESOURCE</th><th>DETAILS</th></tr></thead><tbody id="audit-body">
      ${rows.map((a,i)=>`<tr class="audit-row" data-search="${esc([a.actor,a.action,a.resource_type,a.resource_id,a.details].join(' ').toLowerCase())}" data-action="${esc(a.action)}" data-index="${i}">
        <td>${fmt(a.created_at)}</td><td><b>${esc(a.actor)}</b></td><td>${esc(a.action)}</td><td>${esc(a.resource_type)} ${esc(a.resource_id||'')}</td><td class="mono">${esc(a.details)}</td>
      </tr><tr class="audit-detail" id="audit-detail-${i}"><td colspan="5"><div class="detail-grid">
        <div class="detail-cell"><small>Actor</small><code>${esc(a.actor)}</code></div>
        <div class="detail-cell"><small>Action</small><code>${esc(a.action)}</code></div>
        <div class="detail-cell"><small>Resource</small><code>${esc(a.resource_type)} ${esc(a.resource_id||'')}</code></div>
        <div class="detail-cell" style="grid-column:1/-1"><small>Recorded details</small><code>${esc(a.details)}</code></div>
      </div></td></tr>`).join('')||'<tr><td colspan="5" class="empty">No administrative actions have been recorded yet.</td></tr>'}</tbody></table>
    </section>`;
}

const views={overview,devices,alerts,incidents,arp,rules,baselines,interfaces,reports,audit};
async function render(view){document.querySelectorAll('.nav').forEach(x=>x.classList.toggle('active',x.dataset.view===view));title.textContent={overview:'Network overview',devices:'Known devices',alerts:'Alert queue',incidents:'Incident management',arp:'ARP activity',rules:'Detection rules',baselines:'Network baselines',interfaces:'Interfaces',reports:'Reports',audit:'Audit log'}[view];root.innerHTML='<div class="empty">Loading…</div>';try{root.innerHTML=await views[view]();bind()}catch(e){root.innerHTML=`<div class="panel error">Unable to load this view: ${esc(e.message)}</div>`}}
function bind(){
    document.querySelectorAll('.audit-row').forEach(row=>row.onclick=()=>{
        const d=document.querySelector('#audit-detail-'+row.dataset.index);
        row.classList.toggle('open'); d.classList.toggle('open');
    });
    const filter=document.querySelector('#audit-filter'), action=document.querySelector('#audit-action');
    if(filter&&action){
        const apply=()=>document.querySelectorAll('.audit-row').forEach(row=>{
            const q=(filter.value||'').toLowerCase(), a=action.value;
            row.style.display=(!q||row.dataset.search.includes(q))&&(!a||row.dataset.action===a)?'':'none';
            const d=document.querySelector('#audit-detail-'+row.dataset.index); if(row.style.display==='none') d.style.display='none';
        });
        filter.oninput=apply; action.onchange=apply;
        document.querySelector('#audit-refresh').onclick=()=>render('audit');
    }
    const activityRefresh=document.querySelector('#activity-refresh');
    if(activityRefresh) activityRefresh.onclick=()=>render('overview');
    document.querySelectorAll('.trust').forEach(b=>b.onclick=async()=>{await authFetch('devices/'+b.dataset.id+'/trust',{method:'PATCH'});render('devices')});document.querySelectorAll('.ack').forEach(b=>b.onclick=async()=>{await authFetch('alerts/'+b.dataset.id+'/acknowledge',{method:'POST'});render('alerts')})}
document.querySelectorAll('.nav').forEach(n=>n.onclick=()=>render(n.dataset.view));
const dialog=document.querySelector('#simulator');document.querySelector('#simulate').onclick=()=>dialog.showModal();document.querySelector('#close-dialog').onclick=()=>dialog.close();
document.querySelector('#sim-form').onsubmit=async e=>{
    e.preventDefault();
    const result=document.querySelector('#sim-result'), submit=e.target.querySelector('button[type="submit"]');
    const d=Object.fromEntries(new FormData(e.target));
    submit.disabled=true; result.textContent='Processing…';
    try{
        const r=await authFetch('observations',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
        result.textContent='Processed.';
        if(r) setTimeout(()=>{dialog.close();render('overview')},500);
    }catch(err){
        result.textContent=err.message==='AUTH_REQUIRED'?'Session expired. Sign in again.':`Could not process: ${err.message}`;
    }finally{submit.disabled=false}
};
const ws=new WebSocket(`${location.protocol==='https:'?'wss':'ws'}://${location.host}/ws`);
ws.onopen=()=>document.querySelector('#connection').innerHTML='<i></i> CONNECTED';ws.onclose=()=>document.querySelector('#connection').innerHTML='<i></i> OFFLINE';ws.onmessage=()=>render('overview');
establishSession();
