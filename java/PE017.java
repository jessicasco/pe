public class PE017
{
    public static void main(String[] args)
    {
        int[] a = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8};
        int[] b = {0, 0, 6, 6, 5, 5, 5, 7, 6, 6};

        int sum = 0;
        for(int i = 1; i < 1000; i++) {
            if(i < 20) {
                   sum += a[i];
            }
            else if(i < 100) {
                sum += b[i/10] + a[i%10];
            }
            else {
                if(i%100 < 20) {
                    sum += a[i/100] + a[i%100];
                }
                else {
                    sum += a[i/100] + b[(i%100)/10] + a[i%10];
                }
                if(i%100 != 0) {
                    sum += 3;
                }
                sum += 7;
            }
        }
        sum += 3 + 8;
        System.out.println(sum);
    }
}
