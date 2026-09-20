package pr6;
import java.util.*;
import java.math.BigInteger;

// MEthod 1
public class RSA {
    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
    static int pow(int a , int b , int n){
        int r=1;
        while (b-- > 0) r = r * a % n;
        return r;
    }
    public static void main(String[] args) {
        int p = 3 , q = 11 , n = p*q;
        int phi = (p-1) * (q-1);
        int e=2 , d=1;
        while (gcd(e,phi) != 1)e++;
        while ((e*d) % phi != 1)d++;

        int msg =32;
        int enc = pow(msg , e , n);
        int dec = pow(enc , d , n);

        System.out.println("Encrypt : " + enc);
        System.out.println("Decrypt : " + dec);
    }
}

// Method 2
// public class RSA{
// public static void main(String[] args) { 
//     Random r = new Random(); 

//     BigInteger p = BigInteger.probablePrime(256, r); 
//     BigInteger q = BigInteger.probablePrime(256, r); 
//     BigInteger n = p.multiply(q); 
//     BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)); 

//     BigInteger e = BigInteger.valueOf(65537); 
//     BigInteger d = e.modInverse(phi); 

//     BigInteger m = new BigInteger("1128"); 
//     BigInteger c = m.modPow(e, n); 
//     BigInteger dec = c.modPow(d, n); 

//     System.out.println("Encrypted: " + c); 
//     System.out.println("Decrypted: " + dec); 
// } 
// }