import java.math.BigInteger;

public class PE020 {
    public static void main(String[] args) {
        BigInteger a = BigInteger.ONE;
        for(int i = 1; i <= 100; i++) {
            a = a.multiply(new BigInteger("" + i + ""));
        }
        String b = a.toString();
        int sum = 0;
        for(int i = 0; i < b.length(); i++) {
            sum += b.charAt(i) - '0';
        }
        System.out.println(sum);
    }
}
