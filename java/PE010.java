import java.util.*;

public class PE010 {
    public static void main(String[] args)
    {
        long sum = 0;
        for(int i: getPrimeList(2000000)) {
            sum += i;
        }
        System.out.println(sum);
    }

    private static List<Integer> getPrimeList(int limit) {
        int sievebound = (limit - 1) / 2;
        List<Boolean> sieve = new ArrayList<Boolean>();
        List<Integer> Sieve = new ArrayList<Integer>();
        for (int i = 0; i <= sievebound; i++) 
            sieve.add(false);
        int crosslimit = ((int)Math.sqrt(limit) - 1) / 2;
        for (int i = 1; i <= crosslimit; i++) {
            if (!sieve.get(i)) {
                for (int j = 2*i*(i+1); j <= sievebound; j += 2*i+1) {
                    sieve.set(j, true);
                }
            }
        }
        Sieve.add(2);
        for (int i=1; i <= sievebound; i+=1) {
            if (!sieve.get(i)) {
                Sieve.add(2*i+1);
            }
        }
        return Sieve;
    }
}
