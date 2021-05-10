import unittest
from MyFraction import MyFraction

class TestMyFractionMethods(unittest.TestCase):

  def test_new_fraction_int(self):
      self.assertEqual(str(MyFraction(1, 1)), "1")

  def test_new_rational(self):
      self.assertEqual(str(MyFraction(1, 2)), "1/2")

  def test_new_rational_minus_1(self):
      self.assertEqual(str(MyFraction(-1, 2)), "-1/2")

  def test_new_rational_minus_2(self):
      self.assertEqual(str(MyFraction(1, -2)), "-1/2")

  def test_new_rational_from_string(self):
      self.assertEqual(str(MyFraction("1/2")), "1/2")

  def test_new_rational_from_simple_string_1(self):
      self.assertEqual(str(MyFraction("+1/2")), "1/2")

  def test_new_rational_from_simple_string_2(self):
      self.assertEqual(str(MyFraction("-1/2")), "-1/2")

  def test_new_rational_from_simple_string_3(self):
      self.assertEqual(str(MyFraction("1.5")), "3/2")

  def test_new_rational_from_simple_string_4(self):
      self.assertEqual(str(MyFraction("-1.5")), "-3/2")

  def test_new_rational_from_simple_string_5(self):
      self.assertEqual(str(MyFraction("+1.5")), "3/2")

  def test_new_rational_from_simple_string_6(self):
      self.assertEqual(str(MyFraction("+1.(6)")), "15/9")

  def test_new_rational_from_simple_string_7(self):
      self.assertEqual(str(MyFraction("-1.(6)")), "-15/9")

  def test_new_rational_from_string_1(self):
      self.assertEqual(str(MyFraction("-13.4(8)")), "-1214/90")

  def test_new_rational_from_string_2(self):
      self.assertEqual(str(MyFraction("10.5")), "21/2")

  def test_new_rational_from_string_error_1(self):
      with self.assertRaises(ValueError):
          MyFraction("123123dasd")

  def test_new_rational_from_string_error_2(self):
      with self.assertRaises(ValueError):
          MyFraction("123123.(f)")

  def test_plus_1(self):
      self.assertEqual(MyFraction(1, 2) + MyFraction(1, 2), MyFraction(1))

  def test_plus_2(self):
      self.assertEqual(MyFraction(1, 4) + MyFraction(2, 4), MyFraction(3, 4))

  def test_plus_3(self):
      self.assertEqual(MyFraction(-1, 4) + MyFraction(2, 4), MyFraction(1, 4))

  def test_minus_1(self):
      self.assertEqual(MyFraction(-1, 4) - MyFraction(2, 4), MyFraction(-3, 4))

  def test_minus_2(self):
      self.assertEqual(MyFraction(10) - MyFraction(2, 3), MyFraction(28, 3))

  def test_minus_3(self):
      self.assertEqual(MyFraction(10) - MyFraction(-2), MyFraction(12))

  def test_multiply_1(self):
      self.assertEqual(MyFraction(10) * MyFraction(1, 2), MyFraction(5))

  def test_multiply_2(self):
      self.assertEqual(MyFraction(1, 3) * MyFraction(1, 2), MyFraction(1, 6))

  def test_multiply_3(self):
      self.assertEqual(MyFraction(-3, 2) * MyFraction(4, 2), MyFraction(-3))

  def test_divide_1(self):
      self.assertEqual(MyFraction(8) / MyFraction(-7), MyFraction(-8, 7))

  def test_divide_2(self):
      self.assertEqual(MyFraction(4, 7) / MyFraction(1/2), MyFraction(8, 7))

  def test_divide_3(self):
      self.assertEqual(MyFraction(4, -7) / MyFraction(1/2), MyFraction(-8, 7))

  def test_pow_1(self):
      self.assertEqual(MyFraction(1, 2) ** 2, MyFraction(1, 4))

  def test_pow_2(self):
      self.assertEqual(4 ** MyFraction(1, 2), 2)

  def test_pow_3(self):
      self.assertEqual(MyFraction(1, 16) ** MyFraction(1, 2), MyFraction(1, 4))

  def test_pow_imagine(self):
      self.assertEqual(MyFraction(1, -16) ** MyFraction(1, 2), 1.5308084989341915e-17+0.25j)

  def test_mod_1(self):
      self.assertEqual(MyFraction(2) % 2, 0)

  def test_mod_2(self):
      self.assertEqual(MyFraction(1, 4) % MyFraction(1, 2), MyFraction(1, 4))

  def test_mod_3(self):
      self.assertEqual(MyFraction(-1, 4) % MyFraction(1, 2), MyFraction(1, 4))

  def test_decimal_string_1(self):
      self.assertEqual(str(MyFraction(-1, 4).get_decimal_string()), "-0.25")

  def test_decimal_string_2(self):
      self.assertEqual(str(MyFraction(1, 6).get_decimal_string()), "0.1(6)")

  def test_bool_1(self):
      self.assertEqual(MyFraction(-1, 4) == MyFraction(1, 2), False)

  def test_bool_2(self):
      self.assertEqual(MyFraction(1, 2) == MyFraction(1, 2), True)

  def test_bool_3(self):
      self.assertEqual(MyFraction(1, 4) < MyFraction(1, 2), True)

  def test_bool_4(self):
      self.assertEqual(MyFraction(-1, 4) > MyFraction(1, -2), True)

  def test_bool_5(self):
      self.assertEqual(MyFraction(-1, 4) != MyFraction(1, -2), True)

  def test_bool_6(self):
      self.assertEqual(MyFraction(-1, 4) >= MyFraction(1, -2), True)

  def test_bool_7(self):
      self.assertEqual(MyFraction(-1, 4) <= MyFraction(1, -2), False)

  def test_round(self):
      self.assertEqual(MyFraction(1, 6).__round__(3), MyFraction(167, 1000))

if __name__ == '__main__':
    unittest.main()