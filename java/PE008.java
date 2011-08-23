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
        int temp;
        for(; i <= s.length() - 5; i++) {
            temp = (s.charAt(i)-'0') * (s.charAt(i+1)-'0') * (s.charAt(i+2)-'0') * (s.charAt(i+3)-'0') * (s.charAt(i+4)-'0');
            if(temp > max)
                max = temp;
        }
        System.out.println(max);
    }
}
