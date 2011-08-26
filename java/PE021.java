public class PE021
{
    public static void main(String[] args)
    {
        int sum = 0;
        for(int i = 2; i < 10000; i++) {
            int n = d(i);
            if(n > i && d(n) == i) {
                sum += n + i;
            }
        }
        System.out.println(sum);
    }
    private static int d(int a)
    {
        int result= 0;
        for(int i = 1; i < a; i++) {
            if(a%i == 0)
                result += i;
        }
        return result;
    }
}
