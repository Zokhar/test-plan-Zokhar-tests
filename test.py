import unittest
import Checker

class TestF(unittest.TestCase):

    def test_f1(self):
        self.assertEqual(Checker.check_date("08.12.2001"), True)
        
    def test_f2(self):
        self.assertEqual(Checker.check_date("Первое февраля 2001 года"), False)
        
    def test_f3(self):
        self.assertEqual(Checker.check_date("08.00.2001"), False)

    def test_f4(self):
        self.assertEqual(Checker.check_date("08.13.2001"), False)

    def test_f5(self):
        self.assertEqual(Checker.check_date("08.12.1955"), False)

    def test_f6(self):
        self.assertEqual(Checker.check_date("08.12.2025"), False)

    def test_f7(self):
        self.assertEqual(Checker.check_date("00.12.2001"), False)

    def test_f8(self):
        self.assertEqual(Checker.check_date("31.04.2001"), False)

    def test_f9(self):
        self.assertEqual(Checker.check_date("29.02.2001"), False)

    def test_f10(self):
        self.assertEqual(Checker.check_date("30.02.2024"), False)

    def test_f11(self):
        self.assertEqual(Checker.check_date("32.12.2023"), False)

    def test_f12(self):
        self.assertEqual(Checker.check_date("00.01.2000"), False)

    def test_f13(self):
        self.assertEqual(Checker.check_date("01.01.2000"), True)

    def test_f14(self):
        self.assertEqual(Checker.check_date("31.01.2000"), True)

    def test_f15(self):
        self.assertEqual(Checker.check_date("32.01.2000"), False)

    def test_f16(self):
        self.assertEqual(Checker.check_date("01.01.1956"), False)

    def test_f17(self):
        self.assertEqual(Checker.check_date("01.01.1957"), True)

    def test_f18(self):
        self.assertEqual(Checker.check_date("19.02.2024"), True)

    def test_f19(self):
        self.assertEqual(Checker.check_date("00.01.2025"), False)

    def test_f20(self):
        self.assertEqual(Checker.check_date("01.00.2000"), False)

    def test_f21(self):
        self.assertEqual(Checker.check_date("01.01.2000"), True)

    def test_f22(self):
        self.assertEqual(Checker.check_date("01.12.2000"), True)

    def test_f23(self):
        self.assertEqual(Checker.check_date("01.13.2000"), False)

    def test_f24(self):
        self.assertEqual(Checker.check_date("30.04.2001"), True)

    def test_f25(self):
        self.assertEqual(Checker.check_date("31.04.2001"), False)

    def test_f26(self):
        self.assertEqual(Checker.check_date("28.02.2001"), True)

    def test_f27(self):
        self.assertEqual(Checker.check_date("29.02.2001"), False)

    def test_f28(self):
        self.assertEqual(Checker.check_date("29.02.2024"), True)

    def test_f29(self):
        self.assertEqual(Checker.check_date("30.02.2024"), False)
