package pr7;
import java.util.*;

public class DiffieHellman {
    static int power(int a , int b, int n){
        int r = 1;
        while(b-- > 0) r = r*a%n;
        return r;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter q : "); int q=sc.nextInt();
        System.out.println("Enter Alpha : "); int a=sc.nextInt();
        System.out.println("public key XA : "); int xa=sc.nextInt();
        System.out.println("public key XB : "); int xb=sc.nextInt();

        int ya = power(a,xa,q);
        int yb = power(a,xb,q);
        int keya = power(yb,xa,q);
        int keyb = power(ya,xb,q);

        System.out.println("Public key of a : "+ ya);
        System.out.println("Public key of b : "+ yb);
        System.out.println("Secret key of a : "+ keya);
        System.out.println("Secret key of b : "+ keyb);        
    }
}