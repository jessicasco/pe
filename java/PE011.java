import java.util.Scanner;
import java.io.*;

public class PE011 {
    public static void main(String[] args) throws FileNotFoundException
    {
        int[][] m = new int[20][20];
        Scanner sc = new Scanner(new File("PE011.txt"));
        for(int i = 0; i < 20; i++) {
            for(int j = 0; j < 20; j++) {
                m[i][j] = sc.nextInt();
            }
        }
        int max = 0;
        int temp;
        for(int i = 0; i < 20; i++) {
            for(int j = 0; j < 20; j++) {
                if(isIn(i+3, j-3)) {
                    temp = m[i][j]*m[i+1][j-1]*m[i+2][j-2]*m[i+3][j-3];
                    if(temp > max)
                        max = temp;
                }
                if(isIn(i+3, j)) {
                    temp = m[i][j]*m[i+1][j]*m[i+2][j]*m[i+3][j];
                    if(temp > max)
                        max = temp;
                }
                if(isIn(i+3, j+3)) {
                    temp = m[i][j]*m[i+1][j+1]*m[i+2][j+2]*m[i+3][j+3];
                    if(temp > max)
                        max = temp;
                }
                if(isIn(i, j+3)) {
                    temp = m[i][j]*m[i][j+1]*m[i][j+2]*m[i][j+3];
                    if(temp > max)
                        max = temp;
                }
            }
        }
        System.out.println(max);
    }
    private static boolean isIn(int a, int b)
    {
        if((a >= 0 && a < 20) && (b >= 0 && b < 20))
            return true;
        return false;
    }
}
