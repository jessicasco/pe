public class PE002 {
    public static void main (String [] args)
    {
        int a = 2;
        int b = 8;
        int sum = a + b;
        int c = 4*b + a;
        while(c <= 4000000) {
            sum += c;
            a = b;
            b = c;
            c = 4*b + a;
        }
        System.out.println(sum);
    }
}
