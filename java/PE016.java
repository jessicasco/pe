import java.math.BigInteger;

public class PE016
{
    public static void main(String[] args)
    {
        BigInteger a = BigInteger.ONE;
        BigInteger b = new BigInteger("2");
        for(int i = 1; i <= 1000; i++) {
            a = a.multiply(b);
        }
        String c = a.toString();
        int sum = 0;
        for(int i = 0; i < c.length(); i++) {
            sum += c.charAt(i) - '0';
        }
        System.out.println(sum);
    }
}
