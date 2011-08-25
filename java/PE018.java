import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class PE018
{
    public static void main(String[] args) throws FileNotFoundException
    {
        int[][] a = new int[15][15];
        Scanner sc = new Scanner(new File("PE018.txt"));
        for(int i = 0; i < 15; i++) {
            for(int j = 0; j <= i; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        int max = 0;
        int t = (int) Math.pow(2, 14);
        for(int b = 0; b < t; b++) {
            int s = b;
            int temp = a[0][0];
            int j = 0;
            for(int i = 1; i < 15; i++) {
                if(s%2 == 1) {
                    j++;
                }
                s /= 2;
                temp += a[i][j];
            }
            if(temp > max) {
                max = temp;
            }
        }
        System.out.println(max);
    }
}

