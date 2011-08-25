import java.math.BigInteger;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class PE013
{
    public static void main(String[] args) throws FileNotFoundException
    {
        Scanner sc = new Scanner(new File("PE013.txt"));
        BigInteger bi = BigInteger.ZERO;
        while(sc.hasNextBigInteger())
            bi = bi.add(sc.nextBigInteger());
        System.out.println(bi.toString().substring(0, 10));
    }
}
