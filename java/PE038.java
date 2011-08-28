public class PE038 {
    public static void main(String[] args)
    {
        int[] a = new int[10];
        int max = 0;
        for(int i = 2; i <= 9999; i++) {
            for(int j = 0; j < 10; j++) {
                a[j] = 0;
            }
            int n = 0;
            for(int j = 1; j <= 6; j++) {
                int k = i * j;
                while(k != 0) {
                    a[k%10]++;
                    n++;
                    k /= 10;
                }
                if(n == 9) {
                    n = 0;
                    for(int m = 1; m < 10; m++) {
                        if(a[m] == 1)
                            n++;
                    }
                    if(n == 9) {
                        int t = 0;
                        String b = "";
                        for(int r = 1; r <= j; r++)
                            b += i*r;
                        Integer l = new Integer(b);
                        t = l.intValue();
                        if(t > max)
                            max = t;
                    }
                    break;
                }
                else if(n > 9) {
                    break;
                }
            }
        }
        System.out.println(max);
    }
}
