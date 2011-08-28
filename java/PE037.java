public class PE037 {
    public static void main(String[] args) {
        int sum = 0;
        int count = 0;
        for(int i = 11; count < 11; i++) {
            if(isPrime(i)) {
                if(isLeft(i) && isRight(i)) {
                    count++;
                    sum += i;
                }
            }
        }
        System.out.println(sum);
    }

    private static boolean isLeft(int n)
    {
        while(n > 0) {
            int i;
            for(i = 1; i <= n; i *= 10) ;
            i /= 10;
            n = n - (n/i)*i;
            if(!isPrime(n))
                return false;
        }
        return true;
    }

    private static boolean isRight(int n)
    {
        while(n != 0) {
            n /= 10;
            if(!isPrime(n))
                return false;
        }
        return true;
    }
    private static boolean isPrime(int n)
    {
        if(n == 1)
            return false;
        int k = (int)Math.sqrt(n);
        for(int i = 2; i <= k; i++) {
            if(n%i == 0)
                return false;
        }
        return true;
    }
}
