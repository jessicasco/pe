public class PE032 {
    public static void main(String[] args) {
        int sum = 0;
        int[] a = new int[10];
        for(int i = 1000; i <= 9999; i++) {
            int j = (int)Math.sqrt(i);
            for(int k = 2; k <= j; k++) {
                if(i%k == 0) {
                    int m;
                    for(int s = 0; s < 10; s++) {
                        a[s] = 0;
                    }
                    int n = 0;
                    m = i;
                    while(m != 0) {
                        a[m%10] ++;
                        n++;
                        m /= 10;
                    }
                    m = k;
                    while(m != 0) {
                        a[m%10]++;
                        n++;
                        m /= 10;
                    }
                    m = i / k;      
                    while(m != 0) {
                        a[m%10] ++;
                        n++;
                        m /= 10;
                    }
                    m = 0;
                    for(int s = 1; s < 10; s++)
                           if(a[s] == 1)
                                m++;
                    if(n == 9 && m == 9 && a[0] == 0) {
                        sum += i;
                        break;
                    }
                }
            }
        }
        System.out.println(sum);
    }
}
