"""
These tests are not complete yet - I will be writing them in the next couple of days. I'll push the changes to GitLab as soon
as I write all the tests.

"""
import py_cw


def test_q1a():
	s = py_cw.cadd((1, 0), (0, 1))
	p = py_cw.cmult((3,2), (9,6))
	assert s == (1, 1) and p == (27, 12), "test failed"



