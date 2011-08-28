import java.util.Arrays;

public class PE043 {
    public static void main(String[] args) {
        long sum = 0;
        int[] c = {2, 3, 5, 7, 11, 13, 17};
        int[] a = {0, 9, 8, 7, 6, 5, 4, 3, 2, 1};
        for(int i = 0; i < 3265920; i++){
            lexicographical_sort(a, 10);
            int[] b = new int[7];
            for(int j = 0; j < 7; j++) {
                b[j] = a[j+1]*100+a[j+2]*10+a[j+3];
            }
            int j;
            for(j = 0; j < 7; j++) {
                if(!(b[j]%c[j] == 0))
                    break;
            }
            if(j == 7) {
                long m = 0;
                for(int k = 0; k < 10; k++){
                    m = m*10 + a[k];
                }
                sum += m;
            }
        }
        System.out.println(sum);
    }

    private static void lexicographical_sort(int[] a, int n)
    {
        for(int i = n-1; i > 0; i--) {
            if(a[i] > a[i-1]) {
                for(int j = n-1;; j--) {
                    if(a[j] > a[i-1]) {
                        int t = a[j];
                        a[j] = a[i-1];
                        a[i-1] = t;
                        break;
                    }
                }
                Arrays.sort(a, i, n);
                break;
            }
        }
    }
}
