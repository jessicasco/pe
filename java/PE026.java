public class PE026 {
    public static void main(String[] args) {
        int longest = 0;
        int d = 0;
        for(int i = 2; i < 1000; i++) {
            int length = recurringLength(i);
            if (length > longest) {
                longest = length;
                d = i;
            }
        }
        System.out.println(d);
    }

    private static int recurringLength(int n) {
        int[] a = new int[1000];
        int[] b = new int[1000];
        int remain = 10;
        int length = 0;
        for(int i = 0; ; i++) {
            a[i] = remain/n;
            b[i] = remain%n;
            for(int j = 0; j < i; j++) {
                if(a[j] == a[i] && b[j] == b[i]) {
                    length = i -j;
                    return length;
                }
            }
            remain = b[i]*10;
            if(remain == 0)
                return 0;
        }
    }
}
