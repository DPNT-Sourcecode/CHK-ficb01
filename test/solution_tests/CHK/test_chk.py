from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
    def test_checkout_deal(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_checkout_multideal(self):
        assert checkout_solution.checkout("AAAAA") == 200
    def test_checkout_multideal_different(self):
        assert checkout_solution.checkout("AAABB") == 175
    def test_checkout_multideal_with_extra(self):
        assert checkout_solution.checkout("AAABBD") == 190
    def test_checkout_lower(self):
        assert checkout_solution.checkout("AAaBbD") == -1
    def test_checkout_invalid(self):
        assert checkout_solution.checkout("-") == -1
    def test_checkout_e(self):
        assert checkout_solution.checkout("E") == 40
    def test_checkout_e_freeB(self):
        assert checkout_solution.checkout("EEB") == 80
    def test_checkout_double_e_no_b(self):
        assert checkout_solution.checkout("EE") == 80
    def test_checkout_double_b(self):
        assert checkout_solution.checkout("EEEEBB") == 160
    def test_checkout_double(self):
        assert checkout_solution.checkout("ABCDEABCDE") == 280
    def test_checkout_free_f(self):
        assert checkout_solution.checkout("FFF") == 20
    def test_checkout_free_f_double(self):
        assert checkout_solution.checkout("FFFF") == 30




