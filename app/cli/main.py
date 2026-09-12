# Humanization note: Keep command-line behavior thin and scriptable so operators can automate safe diagnostics without bypassing services. The main entry point keeps that boundary visible to readers.
import argparse, asyncio, json
from app.db.database import Database
from app.config import DB_PATH
from app.simulation.scenarios import SCENARIOS

def main():
    parser=argparse.ArgumentParser(prog="netshield",description="NetShield ARP Guardian CLI")
    sub=parser.add_subparsers(dest="command",required=True)
    sub.add_parser("status")
    sim=sub.add_parser("simulate"); sim.add_argument("scenario",choices=sorted(SCENARIOS)); sim.add_argument("--repeat",type=int,default=1)
    args=parser.parse_args()
    db=Database(DB_PATH); db.initialize()
    if args.command=="status":
        with db.connect() as c:
            print(json.dumps({
                "devices":c.execute("SELECT COUNT(*) FROM devices").fetchone()[0],
                "events":c.execute("SELECT COUNT(*) FROM arp_events").fetchone()[0],
                "alerts":c.execute("SELECT COUNT(*) FROM alerts").fetchone()[0],
            },indent=2))
    elif args.command=="simulate":
        for event in __import__("app.simulation.scenarios",fromlist=["generate"]).generate(args.scenario,args.repeat):
            print(json.dumps(event.__dict__))

if __name__=="__main__": main()
