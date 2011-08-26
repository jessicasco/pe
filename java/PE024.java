import java.util.Arrays;

public class PE024 {
    public static void main(String[] args) {
        int[] a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        for(int i = 1; i < 1000000; i++)
            lexicographic_sort(a, 10);
        for(int i = 0; i < a.length; i++)
            System.out.print(a[i]);
        System.out.println();
    }
    private static void lexicographic_sort(int[] a, int n) {
        for(int i = n-1; i > 0; i--) {
            if(a[i] > a[i-1]) {
                int temp = 0;
                int j;
                for(j = n-1; j >= i-1; j--) {
                    if(a[j] > a[i-1]) {
                        temp = a[j];
                        break;
                    }
                }
                a[j] = a[i-1];
                a[i-1] = temp;
                Arrays.sort(a, i, n);
                break;
            }
        }
    }
}
