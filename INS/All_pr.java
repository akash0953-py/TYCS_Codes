import java.util.*;

public class All_pr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String ");
        String s = sc.next();

        System.out.println("KEY ");
        int k = sc.nextInt() % 26;

        String enc = "", dec = "";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                enc += (char) ((c - 'A' + k) % 26 + 'A');
            } else {
                enc += (char) ((c - 'a' + k) % 26 + 'a');
            }
        }
        for (int i = 0; i < enc.length(); i++) {
            char c = enc.charAt(i);
            if (Character.isUpperCase(c)) {
                dec += (char) ((c - 'A' - k + 26) % 26 + 'A');
            } else {
                dec += (char) ((c - 'a' - k + 26) % 26 + 'a');
            }
        }
        System.out.println("Cipher :" + enc);
        System.out.println("decrypt :" + dec);

    }
}