public class PE007
{
    public static void main(String[] args)
    {
        int count = 1;
        int i;
        for(i = 3; count != 10001; i += 2) {
            if(isPrime(i))
                count++;
        }
        System.out.println(i-2);
    }
    private static boolean isPrime(int n)
    {
        int i = 2;
        int k = (int)Math.sqrt(n); 
        for(; i <= k; i++) {
            if(n%i == 0)
                return false;
        }
        return true;
    }
}
