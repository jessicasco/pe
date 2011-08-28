public class PE046
{
    public static void main(String[] args)
    {
        for(int i = 35; ; i += 2) {
            if(isPrime(i)) {
                continue;
            }
            int j;
            for(j = 1; i-2*j*j >= 2; j++) {
                if(isPrime(i-2*j*j))
                    break;
            }
            if(i-2*j*j < 2) {
                System.out.println(i);
                break;
            }
        }
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
}
