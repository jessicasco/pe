import java.util.*;

public class PE051 {
    public static void main (String [] args)
    {
        int n = 1000000;
        while (true) {
            boolean res = f(n);
            if (res) 
                return;
            n *= 10;
        }
    }

    private static boolean f(int n) {
        List<Integer> primeList = getPrimeList(n);
        List<List<Integer>> subPrimeList = new ArrayList<List<Integer>>();
        int length = 1;
        List<Integer> tmpList = new ArrayList<Integer>();
        for (Integer i: primeList) {
            if(i.toString().length() == length) {
                tmpList.add(i);
            }
            else {
                length ++;
                subPrimeList.add(tmpList);
                tmpList = new ArrayList<Integer>();
                tmpList.add(i);
            }
        }
        subPrimeList.add(tmpList);
        for (int subIndex = 0; subIndex < subPrimeList.size(); subIndex++) {
            tmpList = subPrimeList.get(subIndex);
            while(tmpList.size() >= 8) {
                Integer i = tmpList.get(0);
                tmpList.remove(0);
                String strNum = i.toString();
                for (int j = 0; j < 3; j++) {
                    String stro = (new Integer(j)).toString();
                    String[] tmplist = strNum.split(stro);
                    length = tmplist.length;
                    if (length == 1)
                        continue;
                    for(int ii = 0; ii < ((int)Math.pow(2, length-1) -1); ii++) {
                        int count = 1;
                        int count2 = 0;
                        for(int k = j+1; k < 10; k++) {
                            String strr = (new Integer(k)).toString();
                            String rstr = "";
                            for(int jj = 0; jj < length-1; jj++) {
                                if(((ii>>jj)&1) == 1)
                                    rstr += tmplist[jj] + stro;
                                else
                                    rstr += tmplist[jj] + strr;
                            }
                            Integer rnum = new Integer(rstr + tmplist[length-1]);
                            if (primeList.contains(rnum) == false) {
                                count2 += 1;
                            }
                            else {
                                count += 1;
                            }
                            if (10-8-j < count2)
                                break;
                        }
                        if (count == 8) {
                            System.out.println(i);
                            return true;
                        }
                    }
                }
            }
        }
        return false;
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
