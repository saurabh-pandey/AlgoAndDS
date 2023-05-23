import pytest

from design.consistent_hashing import ConsistentHash


class TestConsistentHash:
    def test_example1(self):
        servers = ["localhost_0", "localhost_1", "localhost_2"]
        ch = ConsistentHash(servers)
        print()
        print(ch.get_server("ABC"))
        print(ch.get_server("DEF"))
        print(ch.get_server("GHI"))
        print(ch.get_server("JKL"))
        print(ch.get_server("ABC"))
        print(ch.get_server("DEF"))
        print(ch.get_server("GHI"))
        print(ch.get_server("JKL"))
