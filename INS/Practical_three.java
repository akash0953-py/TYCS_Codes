import java.util.*;

// Rail Fence  KEY = 2
// public class Practical_three {
//     public static StringBuffer encryption(String PT, int Key) {
//         StringBuffer result1 = new StringBuffer();
//         StringBuffer result2 = new StringBuffer();
//         StringBuffer result = new StringBuffer();
//         for (int i = 0; i < PT.length(); i++) {
//             if (i % 2 == 0) {
//                 result1.append(PT.charAt(i));
//             } else {
//                 result2.append(PT.charAt(i));
//             }
//         }
//         result.append(result1);
//         result.append(result2);
//         return result;
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter Plain Text : ");
//         String PT = sc.nextLine().toLowerCase();
//         System.out.print("Enter Key/Rail/Depth : ");
//         int Key = sc.nextInt();

//         if (Key == 2) {
//             String a = encryption(PT, Key).toString();
//             System.out.println("Encrypted Text : " + a);
//         } else {
//             System.out.println("Key Should Be 2");
//         }

//     }
// }

// Rail Fence KEY = Custom

import java.util.*;

public class Practical_three {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter plain text: ");
        String pt = sc.nextLine();
        System.out.println("Enter key : ");
        pt = pt.replaceAll("\\s+", "");
        int key = sc.nextInt();

        char[][] rail = new char[key][pt.length()];

        for (int i = 0; i < key; i++) {
            for (int j = 0; j < pt.length(); j++) {
                rail[i][j] = '\n';
            }
        }
        int row = 0;
        boolean down = true;

        for (int i = 0; i < pt.length(); i++) {
            rail[row][i] = pt.charAt(i);
            if (row == 0)
                down = true;
            else if (row == key - 1)
                down = false;

            if (down)
                row++;
            else
                row--;
        }
        String cipher = "";
        for (int i = 0; i < key; i++) {
            for (int j = 0; j < pt.length(); j++) {
                if (rail[i][j] != '\n')
                    cipher += rail[i][j];
            }
        }
        System.out.println("Encryption text: " + cipher);

        sc.close();
    }
}