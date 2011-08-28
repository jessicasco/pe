public class PE040
{
    public static void main(String[] args)
    {
        int[] a = new int[1000000+100];
        int[] b = new int[100];
        int i = 0;
        int j = 1;
        while(i < 1000000) {
            int k = j;
            j ++;
            int m = 0;
            while(k != 0) {
                b[m] = k%10;
                k /= 10;
                m ++;
            }
            m --;
            while(m >= 0) {
                a[i] = b[m];
                i++;
                m--;
            }
        }
        int res = a[0]*a[10-1]*a[100-1]*a[1000-1]*a[10000-1]*a[100000-1]*a[1000000-1];
        System.out.println(res);
    }
}
