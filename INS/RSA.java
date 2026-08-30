import java.math.BigInteger;
import java.util.Scanner;

public class RSA{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.System.err.println("Enter p: ");
        int p = sc.nextInt();

        System.out.print("Enter q : ");
        int q = sc.nextInt();

        int n = p*q;
        int phi = (p-1) * (q-1);

        //Calculate e
        
    }
}