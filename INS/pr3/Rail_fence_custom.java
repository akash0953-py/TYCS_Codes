package pr3;
import java.util.*;

public class Rail_fence_custom {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter string : ");
        String pt = sc.nextLine().replaceAll("\\s+", "");
        System.out.println("enter key ");
        int key = sc.nextInt();

        char[][] rail = new char[key][pt.length()];
        for (char[] row : rail) Arrays.fill(row, '\n');

        int r =0 ;
        boolean down = true;
        for (int i=0 ; i<pt.length() ; i++){
            rail[r][i] = pt.charAt(i);

            if (r==0)down = true;
            else if (r == key-1) down = false ;

            r += down ? 1:-1;
        }
        String cipher ="";
        for(char[] row : rail){
            for(char c : row){
                if ( c != '\n') cipher += c;
            }
        }

        System.out.println("Cipher text " + cipher);
    }
    
}
