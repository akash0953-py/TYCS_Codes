package pr4;
import java.util.*;

public class Columnar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Plain Text: ");
        String text = sc.next();

        System.out.print("Enter Number of Columns: ");
        int col = sc.nextInt();

        int row = (text.length() + col -1 )/col;
        char[][] m = new char[row][col];
        int k = 0 ;
        for(int i =0; i< row; i++){
            for(int j=0 ; j< col ; j++){
                if ( k< text.length()){
                    m[i][j] = text.charAt(k++);
                }else{
                    m[i][j] = 'X';
                }
            }
        }
        for(int i =0; i< row; i++){
            for(int j=0 ; j< col ; j++){
                System.out.print(m[i][j] + " ");
                }
            System.out.println();
            }
        }
    }
