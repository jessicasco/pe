import java.math.BigInteger;

public class PE025
{
    public static void main(String[] args)
    {
        BigInteger a = BigInteger.ONE;
        BigInteger b = BigInteger.ONE;
        BigInteger c;
        int index = 2;
        String d;
        for(d = b.toString(); d.length() < 1000; ) {
            c = b.add(a);
            a = b;
            b = c;
            d = b.toString();
            index++;
        }
        System.out.println(index);
    }
}
