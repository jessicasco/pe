import java.io.*;

public class PE008
{
    public static void main(String[] args)
    throws IOException {
        BufferedReader in = new BufferedReader(
                new FileReader("PE008.txt"));
        StringBuilder sb = new StringBuilder();
        String s;
        while ((s = in.readLine()) != null) {
            sb.append(s);
        }
        in.close();
        s = sb.toString();
        int max = 0;
        int i = 0;
        for(; i <= s.length() - 5; i++) {
            int temp = 1;
            for (int j = 0; j < 5; j++) {
                temp *= s.charAt(i+j) - '0';
            }
            if(temp > max)
                max = temp;
        }
        System.out.println(max);
    }
}
