import pytest

import binary_search.first_bad_version as prob

class TestFirstBadVersion:
  def test_example1(self):
    n = 5
    bad = 4
    bad_ver = prob.BadVersion(n, bad)
    assert prob.firstBadVersion(n, bad_ver) == bad_ver.bad_version()
  
  def test_example2(self):
    n = 1
    bad = 1
    bad_ver = prob.BadVersion(n, bad)
    assert prob.firstBadVersion(n, bad_ver) == bad_ver.bad_version()
  
  def test_my_example1(self):
    n = 20
    bad_ver = prob.BadVersion(n)
    assert prob.firstBadVersion(n, bad_ver) == bad_ver.bad_version()