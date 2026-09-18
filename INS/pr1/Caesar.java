package pr1;

import java.util.*;

public class Caesar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter string: ");
        String s = sc.next();

        System.out.print("Enter key: ");
        int k = sc.nextInt();

        String enc = "", dec = "";

        // Encryption
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isUpperCase(c))
                enc += (char) ((c - 'A' + k) % 26 + 'A');
            else
                enc += (char) ((c - 'a' + k) % 26 + 'a');
        }

        // Decryption of encrypted string
        for (int i = 0; i < enc.length(); i++) {
            char c = enc.charAt(i);

            if (Character.isUpperCase(c))
                dec += (char) ((c - 'A' - k + 26) % 26 + 'A');
            else
                dec += (char) ((c - 'a' - k + 26) % 26 + 'a');
        }

        System.out.println("Cipher Text: " + enc);
        System.out.println("Plain Text: " + dec);
    }
}