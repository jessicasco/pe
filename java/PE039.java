public class PE039
{
    public static void main(String[] args)
    {
        int count = 0;
        int maxcount = 0;
        int k = 0;
        for(int p = 12; p <= 1000; p++) {
            count = 0;
            for(int a = 3; a <= (p-3)/3; a++)
                for(int b = a+1; b <= (p-1-a)/2; b++) {
                    if(a*a+b*b == (p-a-b)*(p-a-b))
                        count++;
                }
            if(count > maxcount) {
                k = p;
                maxcount = count;
            }
        }
        System.out.println(k);
    }
}
