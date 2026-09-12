# Humanization note: Keep network adapters isolated because operating-system details vary more than the detection rules do. The discover entry point keeps that boundary visible to readers.
from __future__ import annotations
import platform
import socket
import subprocess
from dataclasses import dataclass

@dataclass
class NetworkInterface:
    name: str
    address: str | None
    state: str
    gateway: str | None = None

class InterfaceDiscovery:
    """Best-effort local interface discovery with safe OS fallbacks."""
    def discover(self) -> list[NetworkInterface]:
        results=[]
        try:
            hostname=socket.gethostname()
            address=socket.gethostbyname(hostname)
        except OSError:
            address=None
        results.append(NetworkInterface("default",address,"up"))
        if platform.system().lower() == "windows":
            results.extend(self._windows())
        else:
            results.extend(self._unix())
        unique={}
        for item in results:
            unique[item.name]=item
        return list(unique.values())

    def _windows(self):
        try:
            output=subprocess.check_output(["ipconfig"],text=True,errors="replace",timeout=3)
        except (OSError,subprocess.SubprocessError):
            return []
        interfaces=[]
        current=None
        for line in output.splitlines():
            if line and not line.startswith(" ") and ":" in line:
                current=line.strip().rstrip(":")
                interfaces.append(NetworkInterface(current,None,"unknown"))
            elif current and "IPv4" in line and ":" in line:
                addr=line.split(":",1)[1].strip()
                for item in interfaces:
                    if item.name==current:
                        item.address=addr
        return interfaces

    def _unix(self):
        try:
            output=subprocess.check_output(["ip","-brief","address"],text=True,errors="replace",timeout=3)
        except (OSError,subprocess.SubprocessError):
            return []
        results=[]
        for line in output.splitlines():
            parts=line.split()
            if len(parts)>=3:
                address=next((x.split("/")[0] for x in parts[2:] if "." in x),None)
                results.append(NetworkInterface(parts[0],address,parts[1].lower()))
        return results
