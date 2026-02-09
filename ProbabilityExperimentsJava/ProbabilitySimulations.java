import java.util.Random;

public class ProbabilitySimulations {

    public static void main(String[] args) {
        simulateCoinTosses(100);
        simulateDieRolls(60);
        simulateCardDraws(20);
        simulateTwoCoinFlips(50);
    }

    // Task 1: Coin Toss
    public static void simulateCoinTosses(int n) {
        int heads = 0, tails = 0;
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            if (rand.nextBoolean()) heads++;
            else tails++;
        }
        System.out.println("Coin Tosses (" + n + " trials): Heads=" + heads + ", Tails=" + tails);
        System.out.println("Theoretical probability: Heads=0.5, Tails=0.5\n");
    }

    // Task 2: Die Roll
    public static void simulateDieRolls(int n) {
        int[] counts = new int[6];
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            int roll = rand.nextInt(6); // 0-5
            counts[roll]++;
        }
        System.out.print("Die Rolls (" + n + " trials): ");
        for (int i = 0; i < 6; i++) System.out.print((i+1) + "=" + counts[i] + " ");
        System.out.println("\nTheoretical probability: Each face=1/6 ≈ 0.1667\n");
    }

    // Task 3: Card Draw
    public static void simulateCardDraws(int n) {
        int red = 0, black = 0;
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            if (rand.nextBoolean()) red++;
            else black++;
        }
        System.out.println("Card Draws (" + n + " draws): Red=" + red + ", Black=" + black);
        System.out.println("Theoretical probability: Red=0.5, Black=0.5\n");
    }

    // Task 4: Two Coin Flips
    public static void simulateTwoCoinFlips(int n) {
        int bothHeads = 0, atLeastOneHead = 0;
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            boolean coin1 = rand.nextBoolean();
            boolean coin2 = rand.nextBoolean();
            if (coin1 && coin2) bothHeads++;
            if (coin1 || coin2) atLeastOneHead++;
        }
        System.out.println("Two Coin Flips (" + n + " trials): Both Heads=" + bothHeads + ", At least one Head=" + atLeastOneHead);
        System.out.println("Theoretical probability: Both Heads=0.25, At least one Head=0.75\n");
    }
}
