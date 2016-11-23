import unittest
from new_eleusis import *

class TestNewEleusis(unittest.TestCase):

    def test_is_suit(self):
        for c in "CDHS":
            self.assertTrue(is_suit(c))
        self.assertFalse(is_suit("B"))

    def test_is_color(self):
        for c in "BR":
            self.assertTrue(is_color(c))
        self.assertFalse(is_color("H"))

    def test_is_value(self):
        for c in "A234JQK":
            self.assertTrue(is_value(c))
        self.assertFalse(is_value("D"))
        self.assertFalse(is_value("KD"))

    def test_is_card(self):
        for c in ["2C", "10D", "JH", "AS"]:
            self.assertTrue(is_card(c))
        self.assertFalse(is_card("H"))
        self.assertFalse(is_card("10"))

##    def test_split_card(self):
##        self.assertEqual(("A", "S"), split_card("AS"))
##        self.assertEqual(("2", "C"), split_card("2C"))
##        self.assertEqual(("10", "D"), split_card("10D"))

    def test_value_to_number(self):
        self.assertEqual(1, value_to_number("A"))
        self.assertEqual(5, value_to_number("5"))
        self.assertEqual(10, value_to_number("10"))
        self.assertEqual(11, value_to_number("J"))
        self.assertEqual(12, value_to_number("Q"))
        self.assertEqual(13, value_to_number("K"))

    def test_number_to_value(self):
        self.assertEqual("A", number_to_value(1))
        self.assertEqual("5", number_to_value(5))
        self.assertEqual("10", number_to_value(10))
        self.assertEqual("J", number_to_value(11))
        self.assertEqual("Q", number_to_value(12))
        self.assertEqual("K", number_to_value(13))
        
    def test_suit(self):
        self.assertEqual('S', suit("AS"))
        self.assertEqual('D', suit("10D"))  

    def test_color(self):
        self.assertEqual('B', color("2C")) 
        self.assertEqual('R', color("6D")) 
        self.assertEqual('R', color("10H")) 
        self.assertEqual('B', color("AS"))

    def test_value(self):
        self.assertEqual(1, value("AS"))
        self.assertEqual(2, value("2C"))
        self.assertEqual(10, value("10D"))
        self.assertEqual(11, value("JH"))
        self.assertEqual(12, value("QD"))
        self.assertEqual(13, value("KC"))

    def test_suit(self):
        self.assertEqual('C', suit("2C")) 
        self.assertEqual('D', suit("6D")) 
        self.assertEqual('H', suit("10H")) 
        self.assertEqual('S', suit("AS"))               

    def test_is_royal(self):
        for c in ["QC", "JD", "KH"]:
            self.assertTrue(is_royal(c))
        self.assertFalse(is_royal("AS"))
        self.assertFalse(is_royal("10C"))

    def test_equal(self):
        self.assertEqual("R", "R")
        self.assertEqual(13, value("KD"))

    def test_less(self):
        self.assertTrue(less("3C", "10C"))
        self.assertTrue(less("10C", "2D"))
        self.assertFalse(less("3C", "AC"))

        self.assertTrue(less("C", "D"))
        self.assertFalse(less("C", "C"))

        self.assertTrue(less("B", "R"))
        self.assertFalse(less("R", "B"))

        self.assertTrue(less("A", "2"))
        self.assertFalse(less("2", "A"))
        self.assertTrue(less("A", "J"))
        self.assertTrue(less("J", "Q"))
        self.assertTrue(less("Q", "K"))

    def test_plus1(self):
        self.assertEqual("2", plus1("A"))
        self.assertEqual("J", plus1("10"))
        self.assertEqual("S", plus1("H"))
        self.assertEqual("KC", plus1("QC"))
        self.assertEqual("B", plus1("R"))
        self.assertEqual("R", plus1("B"))

    def test_minus1(self):
        self.assertEqual("A", minus1("2"))
        self.assertEqual("10", minus1("J"))
        self.assertEqual("H", minus1("S"))
        self.assertEqual("QC", minus1("KC"))
        self.assertEqual("B", minus1("R"))
        self.assertEqual("R", minus1("B"))

    def test_even(self):
        self.assertFalse(even("AS"))
        self.assertTrue(even("2D"))
        self.assertFalse(even("JC"))
        self.assertTrue(even("QH"))
        self.assertFalse(even("KD"))

    def test_odd(self):
        self.assertTrue(odd("AS"))
        self.assertFalse(odd("2D"))
        self.assertTrue(odd("JC"))
        self.assertFalse(odd("QH"))
        self.assertTrue(odd("KD"))

    def eval_tree(self, root, left=None, right=None,
                  cards=("3H", "5D", "AS")):
        """Shortcut for creating and evaluating a Tree"""
        return Tree(root, left, right).evaluate(cards)
        
    def test_simple_evaluate(self):
        self.assertEqual("AS", self.eval_tree("current"))
        self.assertEqual("5D", self.eval_tree("previous"))
        self.assertEqual("3H", self.eval_tree("previous2"))
        self.assertEqual("9C", self.eval_tree("9C"))
        self.assertEqual(True, self.eval_tree(True))
        self.assertEqual(False, self.eval_tree(False))

    def test_unary_evaluate(self):
        self.assertEqual("S", self.eval_tree(suit, "AS"))
        self.assertEqual("B", self.eval_tree(color, "AS"))
        self.assertEqual(1, self.eval_tree(value, "AS"))
        self.assertEqual(12, self.eval_tree(value, "QS"))
        self.assertTrue(self.eval_tree(is_royal, "JD"))
        self.assertFalse(self.eval_tree(is_royal, "3D"))
        self.assertFalse(self.eval_tree(is_royal, "AD"))
        self.assertEqual("10D", self.eval_tree(minus1, "JD"))
        self.assertEqual("QD", self.eval_tree(plus1, "JD"))
        self.assertTrue(self.eval_tree(even, "QH"))
        self.assertFalse(self.eval_tree(even, "3H"))
        self.assertTrue(self.eval_tree(odd, "AC"))
        self.assertFalse(self.eval_tree(odd, "8C"))

    def test_binary_evaluate(self):
        self.assertTrue(self.eval_tree(equal, "AC", "AC"))
        self.assertFalse(self.eval_tree(equal, "8C", "8H"))

        self.assertTrue(self.eval_tree(less, "AD", "KD"))
        self.assertFalse(self.eval_tree(less, "8C", "8C"))
        self.assertFalse(self.eval_tree(less, "2D", "KC"))

        self.assertTrue(self.eval_tree(greater, "AH", "KD"))
        self.assertFalse(self.eval_tree(greater, "8C", "8C"))
        self.assertFalse(self.eval_tree(greater, "3C", "KC"))

    def test_logic_evaluate(self):
        self.assertTrue(self.eval_tree(andf, True, True))
        self.assertFalse(self.eval_tree(andf, True, False))

        self.assertTrue(self.eval_tree(orf, True, True))
        self.assertTrue(self.eval_tree(orf, True, False))
        self.assertTrue(self.eval_tree(orf, False, True))
        self.assertFalse(self.eval_tree(orf, False, False))

        self.assertTrue(self.eval_tree(notf, False))
        self.assertFalse(self.eval_tree(notf, True))

        cards = ("3H", "5D", "AS")
        self.assertEquals("5H", self.evalTree(Tree(iff, "5H", "AS", True), cards))
        self.assertEquals("AS", self.evalTree(iff, "5H", "AS", False), cards)
unittest.main()
