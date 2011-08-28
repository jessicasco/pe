public class PE041
{
    public static void main(String[] args)
    {
        int max = 0;
        for(int i = 2143; i < 9876543; i += 2) {
            if(isPrime(i) && isPandigital(i)) {
                //System.out.println(i);
                max = i;
            }
        }
        System.out.println(max);
    }
    
    private static boolean isPrime(int n) 
    {
        int k = (int)Math.sqrt(n);
        for(int i = 2; i <= k; i++) {
            if(n%i == 0)
                return false;
        }
        return true;
    }

    private static boolean isPandigital(int n) {
        int[] a = new int[10];
        for(int i = 0; i < 10; i++) 
            a[i] = 0;
        int s = 0;
        while(n != 0) {
            a[n%10]++;
            n /= 10;
            s++;
        }
        int i;
        for(i = 1; i < 10; i++) {
            if(a[i] != 1)
                break;
        }
        if(i-1 == s)
            return true;
        else
            return false;
    }
}
