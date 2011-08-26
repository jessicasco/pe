import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.File;
import java.io.FileNotFoundException;

public class PE022
{
    public static void main(String[] args) throws FileNotFoundException
    {
        Scanner sc = new Scanner(new File("PE022.txt"));
        ArrayList<String> names = new ArrayList<String>();
        sc.useDelimiter(",");
        while(sc.hasNext()) {
            String name = sc.next();
            names.add(name);
        }
        Object[] s = names.toArray();
        Arrays.sort(s);
        long index = 1;
        long totalScore = 0;
        for(int j = 0; j < s.length; j++) {
            String name = (String)s[j];
            int score = 0;
            for(int i = 0; i < name.length(); i++) {
                if(name.charAt(i) >= 'A' && name.charAt(i) <= 'Z') {
                    score += name.charAt(i) - 'A' + 1;
                }
            }
            totalScore += score*index;
            index ++;
        }
        System.out.println(totalScore);
    }
}

