package pr1;

import java.util.*;

public class Mono {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String key = "QWERTYUIOPLKJHGFDSAZXCVBNM";
        System.out.println("Enter string : ");
        String pt = sc.next().toUpperCase();
        String enc = "", dec = "";

        for (int i = 0; i < pt.length(); i++) {
            enc += key.charAt(pt.charAt(i) - 'A');
        }
        for (int i = 0; i < enc.length(); i++) {
            dec += (char) (key.indexOf(enc.charAt(i)) + 'A');
        }

        System.out.println("Encrypted: " + enc);
        System.out.println("Decrypted: " + dec);
    }
}
