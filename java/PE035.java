public class PE035 {
    public static void main(String[] args) {
        int count = 0;
        for(int i = 2; i < 1000000; i++) {
            if(isPrime(i)) {
                if(isCircularPrime(i))
                    count++;
            }
        }
        System.out.println(count);
    }
    private static boolean isCircularPrime(int n) {
        int m = rotate(n);
        while(m != n) {
            if(isPrime(m))
                ;
            else
                return false;
            m = rotate(m);
        }
        return true;
    }
    private static int rotate(int n) {
        int a = n % 10;
        n /= 10;
        int i;
        for(i = 1; i <= n; i *= 10) {;}
        n += i*a;
        return n;
    }   
    private static boolean isPrime(int n) {
        int k = (int)Math.sqrt(n);
        for(int i = 2; i <= k; i++) {
            if(n%i == 0)
                return false;
        }
        return true;
    }
}
