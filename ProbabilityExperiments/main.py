import random
import matplotlib.pyplot as plt
from collections import Counter


# ----- Functions -----
def simulate_coin_tosses(n=100):
    tosses = [random.choice(["Heads", "Tails"]) for _ in range(n)]
    counts = Counter(tosses)
    print(f"Coin Tosses ({n} trials): {counts}")
    plt.bar(counts.keys(), counts.values())
    plt.title(f"Coin Toss Results ({n} Tosses)")
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    plt.show()
    # Theoretical probability
    print("Theoretical probability: Heads = 0.5, Tails = 0.5\n")
    return counts


def simulate_die_rolls(n=60):
    rolls = [random.randint(1, 6) for _ in range(n)]
    counts = Counter(rolls)
    print(f"Die Rolls ({n} trials): {counts}")
    plt.bar(counts.keys(), counts.values())
    plt.title(f"Die Roll Distribution ({n} Rolls)")
    plt.xlabel("Die Face")
    plt.ylabel("Frequency")
    plt.show()
    # Theoretical probability
    print("Theoretical probability: Each face = 1/6 ≈ 0.1667\n")
    return counts


def simulate_card_draws(n=20):
    deck = ["Red"] * 26 + ["Black"] * 26
    draws = [random.choice(deck) for _ in range(n)]
    counts = Counter(draws)
    print(f"Card Draws ({n} draws): {counts}")
    plt.bar(counts.keys(), counts.values())
    plt.title(f"Red vs Black Cards ({n} Draws)")
    plt.xlabel("Card Color")
    plt.ylabel("Count")
    plt.show()
    # Theoretical probability
    print("Theoretical probability: Red = 0.5, Black = 0.5\n")
    return counts


def simulate_two_coin_flips(n=50):
    flips = [(random.choice(["H", "T"]), random.choice(["H", "T"])) for _ in range(n)]
    both_heads = sum(1 for a, b in flips if a == "H" and b == "H")
    at_least_one_head = sum(1 for a, b in flips if a == "H" or b == "H")

    print(f"Two Coin Flips ({n} trials): Both Heads = {both_heads}, At least one Head = {at_least_one_head}")
    plt.bar(["Both Heads", "At Least One Head"], [both_heads, at_least_one_head])
    plt.title(f"Two Coin Flips ({n} Trials)")
    plt.ylabel("Count")
    plt.show()

    # Theoretical probability
    print("Theoretical probability: Both Heads = 0.25, At least one Head = 0.75\n")
    return both_heads, at_least_one_head


# ----- Main Execution -----
if __name__ == "__main__":
    simulate_coin_tosses(100)
    simulate_die_rolls(60)
    simulate_card_draws(20)
    simulate_two_coin_flips(50)
