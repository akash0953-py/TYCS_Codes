
// DiffieHellman
import java.util.Scanner;

public class Practical_seven {

    // Calculate (base ^ power) % q
    static int power(int base, int power, int q) {
        int result = 1;
        for (int i = 1; i <= power; i++) {
            result = (result * base) % q;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Public values
        System.out.print("Enter q: ");
        int q = sc.nextInt();

        System.out.print("Enter alpha: ");
        int alpha = sc.nextInt();

        // Private keys
        System.out.print("Enter private key XA: ");
        int xa = sc.nextInt();

        System.out.print("Enter private key XB: ");
        int xb = sc.nextInt();

        // Public keys
        int ya = power(alpha, xa, q);
        int yb = power(alpha, xb, q);

        // Secret keys
        int keyA = power(yb, xa, q);
        int keyB = power(ya, xb, q);

        System.out.println("\nPublic Key of A = " + ya);
        System.out.println("Public Key of B = " + yb);

        System.out.println("Secret Key of A = " + keyA);
        System.out.println("Secret Key of B = " + keyB);

        sc.close();
    }
}