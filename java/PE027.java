public class PE027 {
    public static void main(String[] args) {
        int longest = 0;
        int product = 0;
        for(int a = -999; a <= 999; a++) {
            for(int b = 2; b <= 999; b++) {
                int length = max(a, b);
                if(length > longest) {
                    longest = length;
                    product = a*b;
                }
            }
        }
        System.out.println(product);
    }
    private static int max(int a, int b) {
        int i;
        for(i = 0; ; i++) {
            if(i*i + a*i + b <= 1)
                break;
            if(!isPrime(i*i + a*i + b)) {
                break;
            }
        }
        return i;
    }
    private static boolean isPrime(int n)
    {
        int k = (int)Math.sqrt(n);
        for(int i = 2; i <= k; i++) {
            if(n%i == 0) {
                return false;
            }
        }
        return true;
    }
}
