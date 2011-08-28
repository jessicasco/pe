public class PE044 {
    public static void main(String[] args) {
        long min = 0;
        long  m, n, i, j;
        for(i = 1; ; i++) {
            m = (i*(3*i-1))/2 - ((i-1)*(3*(i-1)-1))/2;
            if(m >= min && min != 0)
                break;
            for(j = i-1; j > 0; j--) {
                m = (i*(3*i-1))/2 - (j*(3*j-1))/2;
                if(m >= min && min != 0)
                    break;
                n = (i*(3*i-1))/2 + (j*(3*j-1))/2;
                if(isPentagonal(m) && isPentagonal(n)) {
                    min = m;
                }
            }
        }
        System.out.println(min);
    }
    
    private static boolean isPentagonal(long n)
    {
        long t = (1 + (long)Math.sqrt(1+24*n))/6;
        if((t*(3*t-1))/2 == n)
            return true;
        return false;
    }
}

