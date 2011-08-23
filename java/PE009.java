public class PE009 {
    public static void main (String [] args) {
        int[] triple = new int[3];
        triple = getPythagoreanTriplet(1000);
        System.out.println(triple[0] * triple[1] * triple[2]);
    }
    private static int[] getPythagoreanTriplet(int s) {
        int[] triple = new int[3];
        int s2 = s / 2;
        int mlimit = (int)Math.ceil(Math.sqrt(s2));
        for (int m = 2; m < mlimit; m++) {
            int k, n, d;
            if (s2 % m != 0)
                continue;
            int sm = s2 / m;
            while (sm % 2 == 0)
                sm /= 2;
            if (m % 2 == 1)
                k = m + 2;
            else
                k = m + 1;
            while (k < 2*m && k <= sm) {
                if (sm % k == 0 && gcd(k, m) == 1){
                    d = s2 / (k*m);
                    n = k - m;
                    triple[0] = d * (m*m - n*n);
                    triple[1] = 2 * d * m * n;
                    triple[2] = d * (m*m + n*n);
                    return triple;
                }
                k += 2;
            }
        }
        return null;
    }
    private static int gcd(int a, int b) {
        int r;
        if (a < b) {
            r = b;
            b = a;
            a = r;
        }
        while (a % b != 0) {
            r = a % b;
            a = b;
            b = r;
        }
        return b;
    }
}
