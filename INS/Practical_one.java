// // import java.util.*;

// // class Practical_one{
// //   public static StringBuffer encryption(String text,int k){
// //   StringBuffer result=new StringBuffer();
// //   for(int i=0;i<text.length();i++){
// //     if(Character.isUpperCase(text.charAt(i))){
// //     char ch=(char)(((int)text.charAt(i)+k-65)%26+65);
// //     result.append(ch);
// //   }
// //     else{
// //     char ch=(char)(((int)text.charAt(i)+k-97)%26+97);
// //     result.append(ch);
// //   }
// //   }
// //   return result;
// //   }
// //   public static StringBuffer decryption(String text, int k){
// //     StringBuffer result1 = new StringBuffer();

// //     for(int i = 0; i < text.length(); i++){
// //         if(Character.isUpperCase(text.charAt(i))){
// //             char ch = (char)(((text.charAt(i) - 65 - k + 26) % 26) + 65);
// //             result1.append(ch);
// //         }
// //         else{
// //             char ch = (char)(((text.charAt(i) - 97 - k + 26) % 26) + 97);
// //             result1.append(ch);
// //         }
// //     }
// //     return result1;
// // }
// //   public static void main(String args[]){
// //   String s,str;
// //   StringBuffer s1;
// //   int k;

// //   System.out.println("Enter string");
// //   Scanner sc=new Scanner(System.in);
// //   s=sc.nextLine();
// //   System.out.println("Enter key");
// //   k=sc.nextInt ();


// //   s1=new StringBuffer(encryption(s,k));
// //   str=s1.toString();

// //   System.out.println("cipher: "+encryption(s,k));
// //   System.out.println("plain Text: "+decryption(str,k));
// //   sc.close();
// //   }
// // }



// // Caesar Cipher 

// // import java.util.*; 
// // class JavaApplication9{ 
// //   public static StringBuffer encryption(String text,int k){ 
// //   StringBuffer result=new StringBuffer(); 
// //   for(int i=0;i<text.length();i++){ 
// //     if(Character.isUpperCase(text.charAt(i))){ 
// //     char ch=(char)(((int)text.charAt(i)+k-65)%26+65); 
// //     result.append(ch); 
// //   } 
  
// //     else{ 
// //     char ch=(char)(((int)text.charAt(i)+k-97)%26+97); 
// //     result.append(ch); 
// //   } 
// //   } 
// //   return result; 
// //   } 
// //   public static StringBuffer decryption(String text, int 
// // k){ 
// //     StringBuffer result1 = new StringBuffer(); 
 
// //     for(int i = 0; i < text.length(); i++){ 
// //         if(Character.isUpperCase(text.charAt(i))){ 
// //             char ch = (char)(((text.charAt(i) - 65 - k + 26) 
// // % 26) + 65); 
// //             result1.append(ch); 
// //         } 
// //         else{ 
// //             char ch = (char)(((text.charAt(i) - 97 - k + 26) 
// // % 26) + 97); 
// //             result1.append(ch); 
// //         } 
// //     } 
// //     return result1; 
// // } 
// // public static void main(String args[]) { 
 
// //     Scanner sc = new Scanner(System.in); 
 
// //     System.out.print("Enter string: "); 
// //     String s = sc.next();
// //     System.out.print("Enter key: "); 
// //     int k = sc.nextInt(); 
 
// //     k = k % 26; 
 
// //     String str = encryption(s, k).toString(); 
 
// //     System.out.println("Cipher Text: " + str); 
// //     System.out.println("Plain Text: " + decryption(str, 
// // k)); 
// // } 
// // } 


// //  Monoalphabetic Cipher

// // MY METHOD 
// // Monoalphabetic Substitution
// import java.util.Scanner;

// public class Practical_one {
//     public static void main(String[] args) {
//         String key = "ZXCVBNMASDFGHJKLQWERTYUIOP";
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter plain text: ");
//         String pt = sc.next().toUpperCase();
//         String ct = encrypt(pt,key);
//         String pt1 = decrypt(ct,key);
//         System.out.println("Encrypted text: "+ ct);
//         System.out.println("Decrypted text: "+ pt1);
//         sc.close();
//     }

//     // Encryption Function
//     public static String encrypt(String s , String k){
//         StringBuffer sb = new StringBuffer(s);
//         for ( int i=0; i<sb.length() ; i++){
//             sb.setCharAt(i,k.charAt(sb.charAt(i) - 'A'));
//             // char c = sb.charAt(i);
//             // int idx = c - 65;
//             // c = k.charAt(idx);
//             // sb.setCharAt(i, c);
//         }
//         return sb.toString();
//     }

//     public static String decrypt(String s,String k){
//         // int idx;
//         // char c;
//         StringBuffer sb = new StringBuffer(s);
//         for (int i=0; i< sb.length() ; i++){
//             sb.setCharAt(i,(char) (k.indexOf(sb.charAt(i)) + 'A'));
//             // c = sb.charAt(i);
//             // idx = k.indexOf(c);
//             // c = (char) (idx + 65);
//             // sb.setCharAt(i,c);
//         }
//         String decryptedText = new String(sb);
//         return decryptedText;
//     }
//     // public static int getIndex(char c, String k){
//     //     int idx = 0;
//     //     for(int i=0; i< k.length() ; i++){
//     //         if (k.charAt(i) == c){
//     //             idx = i;
//     //         }
//     //     }
//     //     return idx;
//     // }
// }


// // DOST KA CODE 
// import java.util.*; 
// import java.io.*; 
// public class  Practical_one { 
     
//     public static void main(String[]args){ 
//         String key="ZXCBMNASDFGHJKLQWERTYUIOPV"; 
//         Scanner sc=new Scanner(System.in); 
//         System.out.println("Enter Plain Text"); 
//         String pt=sc.next().toUpperCase(); 
//         String ct = encrypt(pt, key); 
//         String pt1=decrypt(ct,key); 
//         System.out.println("Encrypted "+ct);   
//         System.out.println("Decrypted "+pt1); 
         
//     } 
 
//     public static String encrypt(String s, 
// String k){ 
//         StringBuffer sb =new StringBuffer(s); 
//         for(int i=0;i<sb.length();i++){ 
//             int idx; 
//             char c; 
//             idx=sb.charAt(i)-65; 
//             c=k.charAt(idx); 
//             sb.setCharAt(i, c); 
//         } 
//         String ecryptedText = sb.toString(); 
//         return ecryptedText; 
         
//     } 
//     public static String decrypt(String s,String 
// key){ 
//         StringBuffer sb =new StringBuffer(s); 
//         for (int i=0;i<sb.length();i++){ 
//         int idx; 
//         char c; 
//         c=sb.charAt (i ); 
//         idx=key.indexOf(c); 
 
//         sb.setCharAt(i,(char)(idx+65)); 
//         } 
//         return sb.toString(); 
         
//     } 
// } 