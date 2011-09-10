public class PE053 {
    public static void main(String[] args) {
        int count = 0;
        for (int i = 23; i <= 100; i++) {
            int j = i / 2;
            while (comb(i, j) > 1000000) {
                if (2 * j != i) {
                    count++;
                }
                count++;
                j -= 1;
            }
        }
        System.out.println(count);
    }

    private static double comb(int n, int r) {
        double res = 1.0;
        for (int i = 0; i < r; i++) {
            res *= (n - i) * 1.0 / (i + 1);
        }
        return res;
    }
}
