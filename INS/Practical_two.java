// Monoalphabetic Substitution
import java.util.Scanner;

public class Practical_two {
    public static void main(String[] args) {
        String key = "ZXCVBNMASDFGHJKLQWERTYUIOP";
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter plain text: ");
        String pt = sc.next().toUpperCase();
        String ct = encrypt(pt,key);
        String pt1 = decrypt(ct,key);
        System.out.println("Encrypted text: "+ ct);
        System.out.println("Decrypted text: "+ pt1);
        sc.close();
    }

    // Encryption Function
    public static String encrypt(String s , String k){
        StringBuffer sb = new StringBuffer(s);
        for ( int i=0; i<sb.length() ; i++){
            sb.setCharAt(i,k.charAt(sb.charAt(i) - 'A'));
            // char c = sb.charAt(i);
            // int idx = c - 65;
            // c = k.charAt(idx);
            // sb.setCharAt(i, c);
        }
        return sb.toString();
    }

    public static String decrypt(String s,String k){
        // int idx;
        // char c;
        StringBuffer sb = new StringBuffer(s);
        for (int i=0; i< sb.length() ; i++){
            sb.setCharAt(i,(char) (k.indexOf(sb.charAt(i)) + 'A'));
            // c = sb.charAt(i);
            // idx = k.indexOf(c);
            // c = (char) (idx + 65);
            // sb.setCharAt(i,c);
        }
        String decryptedText = new String(sb);
        return decryptedText;
    }
    // public static int getIndex(char c, String k){
    //     int idx = 0;
    //     for(int i=0; i< k.length() ; i++){
    //         if (k.charAt(i) == c){
    //             idx = i;
    //         }
    //     }
    //     return idx;
    // }
}
