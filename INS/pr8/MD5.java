package pr8;
import java.security.MessageDigest;
import java.util.HexFormat;

public class MD5 {
    public static String getHash(byte[] input , String algo) throws Exception{
        MessageDigest md = MessageDigest.getInstance(algo);
        md.update(input);
        return HexFormat.of().formatHex(md.digest());
    }
        public static void main(String[] args) throws Exception {
        String input = "Akash";
        System.out.println("Input: " + input);
        System.out.println("MD5 Hash: " + getHash(input.getBytes(), "MD5"));
    }
}