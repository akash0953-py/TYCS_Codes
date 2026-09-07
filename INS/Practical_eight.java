import java.security.MessageDigest; 
import java.util.HexFormat; 

// MDS 

public class Practical_eight { 
public static String getHash(byte[] inputBytes, 
String algorithm) { 
String hashvalue = ""; 
try { 
MessageDigest messageDigest = 
MessageDigest.getInstance(algorithm); 
messageDigest.update(inputBytes); 
byte[] digestedBytes = messageDigest.digest(); 
// Convert bytes to lowercase hexadecimal 
hashvalue = 
HexFormat.of().formatHex(digestedBytes); 
} catch (Exception e) { 
e.printStackTrace(); 
} 
return hashvalue; 
} 
public static void main(String[] args) { 
String somestring = "this is some string"; 
System.out.println( 
getHash(somestring.getBytes(), "SHA-256") 
);}} 