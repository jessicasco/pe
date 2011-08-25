public class PE014
{
    public static void main(String[] args)
    {
        int max = 0;
        int start = 0;
        int length = 0;
        for(int i = 1; i < 1000000; i++) {
            long a = i;
            length = 1;
            while(a != 1) {
                a = next(a);
                length++;
            }
            if(length > max) {
                max = length;
                start = i;
            }
        }
        System.out.println(start);
    }
    private static long next(long a)
    {
        if(a%2 == 0) {
            return a/2;
        }
        return 3*a+1;
    }
}
