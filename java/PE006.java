public class PE006
{
    public static void main(String[] args)
    {
        long n = 100;
        System.out.println(getSquareOfSum(n) - getSumOfSquare(n));
    }
    
    private static long getSumOfSquare(long n)
    {
        return n*(n+1)*(2*n+1)/6;
    }
    
    private static long getSquareOfSum(long n)
    {
        long a = n*(n+1)/2;
        return a*a;
    }
}
