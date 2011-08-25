public class PE012
{
    public static void main(String[] args)
    {
        for(int i = 1; ; i++) {
            long n = i*(i+1)/2;
            if(numOfDivisor(n) > 500) {
                System.out.println(n);
                break;
            }
        }
    }
    private static int numOfDivisor(long n) {
        int num = 1;
        int count = 1;
        while (n%2 == 0) {
            n /= 2;
            count += 1;
        }
        num *= count;
        for(int i = 3; i*i <= n; i+=2) {
            count = 1;
            while (n%i == 0) {
                n /= i;
                count ++;
            }
            num *= count;
        }
        if (n > 1)
            num *= 2;
        return num;
    }
}
