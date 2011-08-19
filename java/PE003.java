public class PE003 {
    public static void main (String [] args)
    {
        long n = 600851475143L;
        int m = 1;
        for (int i = 3; i*i <= n; i += 2) {
            while(n%i == 0) {
                n /= i;
                m = i;
            }
        }
        if (n != 1) {
            System.out.println(n);
        }
        else {
            System.out.println(m);
        } 
    }
}
