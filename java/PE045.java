public class PE045 {
    public static void main(String[] args)
    {
        for(long i = 286; ; i++) {
            long m = T(i);
            if(isPentagonal(m) && isHexagonal(m)) {
                System.out.println(m);
                break;
            }
        }
    }

    private static long T(long n)
    {
        return n*(n+1)/2;
    }

    private static boolean isPentagonal(long n)
    {
        long t = (1+(long)Math.sqrt(1+24*n))/6;
        if(t*(3*t-1)/2 == n)
            return true;
        return false;
    }

    private static boolean isHexagonal(long n)
    {
        long t = (1+(long)Math.sqrt(1+8*n))/4;
        if(t*(2*t-1) == n)
            return true;
        return false;
    }
}
