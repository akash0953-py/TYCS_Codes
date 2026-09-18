package pr2;

import java.util.*;

public class Vernam {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string :");
        String pt = sc.next().toUpperCase();

        System.out.println("Enetr key ");
        String key = sc.next().toUpperCase();

        if (pt.length() != key.length()) {
            System.err.println("String and key must be same length");
        }

        String enc = "", dec = "";
        for (int i = 0; i < pt.length(); i++) {
            enc += (char) ((pt.charAt(i) ^ key.charAt(i)) + 97);
        }

        for (int i = 0; i < enc.length(); i++) {
            dec += (char) ((enc.charAt(i) - 97) ^ key.charAt(i));
        }
        System.out.println("cipher :" + enc);
        System.out.println("Decrypt : " + dec);
    }
}
