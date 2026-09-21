package pr5;
import java.util.*;
import java.util.Base64;
import javax.crypto.*;
import javax.crypto.spec.*;

public class DES_AES {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        // Choose algorithm
        System.out.println("1. DES");
        System.out.println("2. AES");
        System.out.print("Choose Algorithm: ");
        int choice = sc.nextInt();
        sc.nextLine(); // consume newline

        String algo = (choice == 1) ? "DES" : "AES";

        // Generate key
        KeyGenerator kg = KeyGenerator.getInstance(algo);
        SecretKey key = kg.generateKey();

        // Input
        System.out.print("Enter Plain Text: ");
        String text = sc.nextLine();

        // Encrypt
        Cipher c1 = Cipher.getInstance(algo);
        c1.init(Cipher.ENCRYPT_MODE, key);
        String enc = Base64.getEncoder().encodeToString(c1.doFinal(text.getBytes()));

        // Decrypt
        Cipher c2 = Cipher.getInstance(algo);
        c2.init(Cipher.DECRYPT_MODE, key);
        String dec = new String(c2.doFinal(Base64.getDecoder().decode(enc)));

        System.out.println("\nAlgorithm: " + algo);
        System.out.println("Encryption: " + enc);
        System.out.println("Decryption: " + dec);
    }
}