package pr3;

import java.util.*;

public class Rail_fence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string :");
        String pt = sc.nextLine().toLowerCase();
        System.out.println("Enter key : ");
        int key = sc.nextInt();
        String r1 = "", r2 = "";
        for (int i = 0; i < pt.length(); i++) {
            if (i % 2 == 0) {
                r1 += pt.charAt(i);
            } else {
                r2 += pt.charAt(i);
            }
        }
        System.out.println("cipher text : " + r1 + r2);
    }
}
