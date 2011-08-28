public class PE049 {
    public static void main(String[] args)
    {
        for(int i = 1001; i <= 9999; i += 2)
            for(int j = 1; i+2*j <= 9999 ; j++)
                if(isPrime(i) && isPrime(i+j) && isPrime(i+2*j))
                    if(isPer(i, j)) {
                        if (i == 1487 && j == 3330) {
                            continue;
                        }
                        System.out.println(i+""+(i+j)+""+(i+2*j));
                    }
    }

    private static boolean isPrime(int n)
    {
        int k = (int)Math.sqrt(n);
        for(int i = 2; i <= k; i++)
            if(n%i == 0)
                return false;
        return true;
    }
    
    private static boolean isPer(int s, int t) {
        int[] a = new int[10];
        int[] b = new int[10];
        int[] c = new int[10];
        int i;
        for(i = 0; i < 10; i++) {
            a[i] = 0;
            b[i] = 0;
            c[i] = 0;
        }
        int k = s;
        while(k != 0) {
            a[k%10] ++;
            k /= 10;
        }
        k = s + t;  
        while(k != 0) {
            b[k%10] ++;
            k /= 10;
        }
        k = s + 2*t;
        while(k != 0) {
            c[k%10] ++;
            k /= 10;
        }
        for(i = 0; i < 10; i++) {
            if(a[i] == b[i] && b[i] == c[i])
                continue;
            break;
        }
        if(i == 10)
            return true;
        return false;
    }
}
