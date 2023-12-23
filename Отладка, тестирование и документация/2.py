class TestMultiply(TestCase):
    def test_both_positive(self):
        a, b = 4, 2
        answer = 8
        self.assertEqual(multiply(a, b), answer)

    def test_first_positive_second_negative(self):
        a, b = -4, 2
        answer = -8
        self.assertEqual(multiply(a, b), answer)

    def test_first_negative_second_positive(self):
        a, b = 4, -2
        answer = -8
        self.assertEqual(multiply(a, b), answer)

    def test_both_negative(self):
        a, b = -4, -2
        answer = 8
        self.assertEqual(multiply(a, b), answer)

    def test_both_zero(self):
        a, b = 0, 0
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_first_zero_second_positive(self):
        a, b = 0, 2
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_first_zero_second_negative(self):
        a, b = 0, -2
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_first_positive_second_zero(self):
        a, b = 2, 0
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_first_negative_second_zero(self):
        a, b = -2, 0
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_both_float(self):
        a, b = 1.1, 5.2
        answer = 5.72
        self.assertEqual(multiply(a, b), answer)


    def test_first_float_second_positive(self):
        a, b = 1.1, 2
        answer = 2.2
        self.assertEqual(multiply(a, b), answer)

    def test_first_negative_second_float(self):
        a, b = -5, 1.1
        answer = -5.5
        self.assertEqual(multiply(a, b), answer)

    def test_both_float_negative(self):
        a, b = -1.1, -5.2
        answer = 5.72
        self.assertEqual(multiply(a, b), answer)

    def test_both_big(self):
        a, b = 10 ** 12, 10 ** 13
        answer = 10 ** 25
        self.assertEqual(multiply(a, b), answer)

    def test_first_big_second_zero(self):
        a, b = 10 ** 12, 0
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_first_zero_second_big(self):
        a, b = 0, 10 ** 12
        answer = 0
        self.assertEqual(multiply(a, b), answer)