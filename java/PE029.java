import java.util.HashSet;
import java.math.BigInteger;

public class PE029 {
    public static void main(String[] args) {
        HashSet<BigInteger> set = new HashSet<BigInteger>();
        for(int a = 2; a <= 100; a++) {
            for(int b = 2; b <= 100; b++) {
                BigInteger big = new BigInteger("" + a + "");
                big = big.pow(b);
                set.add(big);
            }
        }
        System.out.println(set.size());
    }
}
