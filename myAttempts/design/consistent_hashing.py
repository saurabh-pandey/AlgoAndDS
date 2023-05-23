import bisect
import hashlib

from typing import List

class ConsistentHash:
    def __init__(self, servers: List[str]) -> None:
        self._servers = {self._hash(s) : s for s in servers}
        self._sorted_servers = []
        for hash in self._servers.keys():
            bisect.insort(self._sorted_servers, hash)
    
    def get_server(self, object: str) -> str:
        obj_hash = self._hash(object)
        index = bisect.bisect(self._sorted_servers, obj_hash)
        server_hash = (self._sorted_servers[index]
                       if index < len(self._sorted_servers)
                       else self._sorted_servers[0])
        return self._servers[server_hash]

    def _hash(self, val: str) -> str:
        return hashlib.sha256(val.encode()).hexdigest()


