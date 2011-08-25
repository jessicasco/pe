public class PE015
{
    public static void main(String[] args)
    {
        System.out.println(c(20+20, 20));
    }

    private static long c(long a, long b)
    {
        double result = 1;
        if(a-b < b) {
            b = a - b;
        }
        for(int i = 1; i <= b; i++) {
            result *= (a-i+1)*1.0/i;
        }
        return (long)result;
    }
}
