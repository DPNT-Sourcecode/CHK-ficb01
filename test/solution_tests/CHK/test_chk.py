from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
    def test_checkout_deal(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_checkout_multideal(self):
        assert checkout_solution.checkout("AAAAAA") == 260
    def test_checkout_multideal_different(self):
        assert checkout_solution.checkout("AAABB") == 175
    def test_checkout_multideal_with_extra(self):
        assert checkout_solution.checkout("AAABBD") == 190





