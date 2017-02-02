#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, compute_cycle_length, interval_eval

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    def test_read2(self):
        s = "143 1430\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  143)
        self.assertEqual(j, 1430)
    def test_read3(self):
        s = "1765 1111\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1765)
        self.assertEqual(j, 1111)        
    # ----
    # eval 
    # ----

    def test_eval_1(self):
        v = collatz_eval(351737, 610734)
        self.assertEqual(v, 470)

    def test_eval_2(self):
        v = collatz_eval(97024, 731998 )
        self.assertEqual(v, 509)

    def test_eval_3(self):
        v = collatz_eval(999, 1999 )
        self.assertEqual(v, 182)

    def test_eval_4(self):
        v = collatz_eval(1, 1000000 )
        self.assertEqual(v, 525)
    # ----
    # eval Helper
    # ----

    def test_interval_eval_1(self):
        v = interval_eval(1, 10)
        self.assertEqual(v, 20)

    def test_interval_eval_2(self):
        v = interval_eval(100, 200)
        self.assertEqual(v, 125)

    def test_interval_eval_3(self):
        v = interval_eval(201, 210)
        self.assertEqual(v, 89)

    def test_interval_eval_4(self):
        v = interval_eval(900, 1000)
        self.assertEqual(v, 174)
    # -----
    # Compute Cycle Length
    # -----

    def test_compute_cycle_length_1(self):
        x = compute_cycle_length(9)
        self.assertEqual(x, 20)

    def test_compute_cycle_length_2(self):
        x = compute_cycle_length(500)
        self.assertEqual(x, 111)

    def test_compute_cycle_length_3(self):
        x = compute_cycle_length(51)
        self.assertEqual(x, 25)


    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print2(self):
        w = StringIO()
        collatz_print(w, 5, 500, 2500)
        self.assertEqual(w.getvalue(), "5 500 2500\n")
    def test_print3(self):
        w = StringIO()
        collatz_print(w, 4331, 120, 2980)
        self.assertEqual(w.getvalue(), "4331 120 2980\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve2(self):
        r = StringIO("834663 44619 \n963494 396050 \n295483 534708 \n355772 491736 \n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "834663 44619 509\n963494 396050 525\n295483 534708 470\n355772 491736 449\n")
    def test_solve3(self):
        r = StringIO("128622 32188 \n980118 887243 \n646873 585341 \n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "128622 32188 354\n980118 887243 507\n646873 585341 509\n")
# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
