import java.math.BigInteger;

public class PE048
{
    public static void main(String[] args)
    {
        BigInteger sum = BigInteger.ZERO;
        for(int i = 1; i <= 1000; i++) {
            BigInteger a = new BigInteger(i+"");
            a = a.pow(i);
            sum = sum.add(a);
        }
        String s = sum.toString();
        int t = s.length();
        System.out.println(s.substring(t-10, t));
    }
}
