public class PE033
{
    public static void main(String[] args)
    {
        int result = 1;
        int num = 1;
        int den = 1;
        for(int a = 10; a < 99; a++) {
            for(int b = a+1; b <= 99; b++) {
                if(b%10 != 0 && a%10 == b/10 && a*1.0/b == (a/10)*1.0/(b%10)){
                    if(a*1.0/b == (a/10)*1.0/(b/10))
                        continue;
                    num *= a;
                    den *= b;
                }
            }
        }
        result = den/gcd(num, den);
        System.out.println(result);
    }
    private static int gcd(int a, int b) {
        if(a < b) {
            int temp = a;
            a = b;
            b = temp;
        }
        int c = a%b;
        while(c != 0) {
            a = b;
            b = c;
            c = a % b;
        }
        return b;
    }
}
