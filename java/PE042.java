import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class PE042
{
    public static void main(String[] args) throws FileNotFoundException
    {
        int count = 0;
        Scanner sc = new Scanner(new File("PE042.txt"));
        sc.useDelimiter(",");
        while(sc.hasNext()) {
            String a = sc.next();
            int value = 0;
            for(int i = 1; i < a.length()-1; i++) {
                value += a.charAt(i) - 'A' + 1;
            }
            int t = (int)Math.sqrt(1+8*value);
            t = (t-1)/2;
            if(t*(t+1)/2 == value)
                count++;
        }
        System.out.println(count);
    }
}
