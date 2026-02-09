import unittest
from collections import Counter
import random


# For testing, we modify the functions to **return counts without plotting**.

def coin_toss_counts(n):
    tosses = [random.choice(["Heads", "Tails"]) for _ in range(n)]
    return Counter(tosses)

def die_roll_counts(n):
    rolls = [random.randint(1, 6) for _ in range(n)]
    return Counter(rolls)

def card_draw_counts(n):
    deck = ["Red"]*26 + ["Black"]*26
    draws = [random.choice(deck) for _ in range(n)]
    return Counter(draws)

def two_coin_flips_counts(n):
    flips = [(random.choice(["H","T"]), random.choice(["H","T"])) for _ in range(n)]
    both_heads = sum(1 for a,b in flips if a=="H" and b=="H")
    at_least_one_head = sum(1 for a,b in flips if a=="H" or b=="H")
    return both_heads, at_least_one_head

# --------------------- TEST CASES ---------------------

class TestSimulations(unittest.TestCase):

    # ----- Normal Test Cases -----

    # Testing to see that total is equal to 100 because there are 100 tosses
    def test_normal_coin_toss(self):
        counts = coin_toss_counts(100)
        self.assertEqual(sum(counts.values()), 100)
        self.assertTrue("Heads" in counts and "Tails" in counts)

    # Testing to see that toal is 60
    def test_normal_die_roll(self):
        counts = die_roll_counts(60)
        self.assertEqual(sum(counts.values()), 60)
        for i in range(1,7):
            self.assertIn(i, counts)

    # Testing that the counts make sense
    def test_normal_two_coin_flips(self):
        both, at_least = two_coin_flips_counts(50)
        self.assertTrue(0 <= both <= 50)
        self.assertTrue(both <= at_least <= 50)

    # ----- Edge Test Cases -----

    # Setting n to 0
    def test_edge_zero_trials(self):
        counts = coin_toss_counts(0)
        self.assertEqual(sum(counts.values()), 0)

    # 1 dice roll, so face must be between 1-6
    def test_edge_one_trial_die(self):
        counts = die_roll_counts(1)
        self.assertEqual(sum(counts.values()), 1)
        self.assertTrue(all(1 <= k <= 6 for k in counts.keys()))

    # Force all heads and check counts of "both heads" and "at least 1 head"
    def test_edge_all_heads_two_coins(self):
        # Force all heads by patching random.choice temporarily
        original_choice = random.choice
        random.choice = lambda x: "H"
        both, at_least = two_coin_flips_counts(10)
        self.assertEqual(both, 10)
        self.assertEqual(at_least, 10)
        random.choice = original_choice

if __name__ == "__main__":
    unittest.main()
