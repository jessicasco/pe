public class PE004 {
    public static void main (String [] args)
    {
        int max = 0;
        for (int a=999; a>=100; a-=1) {
            int step;
            int b;
            if (a%11 == 0) {
                step = 1;
                b = a;
            }
            else {
                step = 11;
                b = a / 11 * 11;
            }
            if (max != 0 && a*b <= max) {
                break;
            }
            while (b >= 100) {
                int s = a * b;
                if (max != 0 && s <= max) {
                    break;
                }
                int s1 = s;
                String S = "";
                while (s1 != 0) {
                    S += s1 % 10;
                    s1 /= 10;
                }
                int i, j;
                for (i=0,j=S.length()-1; i<j; i++, j-- ) {
                    if (S.charAt(i) != S.charAt(j)) {
                        break;
                    }
                }
                if (i >= j) {
                    max = s;
                }
                b -= step;
            }
        }
        System.out.println(max);
    }
}
