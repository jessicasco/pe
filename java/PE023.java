public class PE023 {
    public static void main(String[] args)
    {
        int sum = 0;
        int j = 0;
        boolean[] a = new boolean[28123+1];
        int[] b = new int[28123+1];
        for(int i = 1; i <= 28123; i++) {
            a[i] = false;
            if(isAbundant(i)){
                b[j++] = i;
            }
        }
        for(int i = 0; i < j; i++) {
            for(int k = 0; k <= i; k++) {
                if(b[k] + b[i] <= 28123)
                    a[b[k]+b[i]] = true;
            }
        }
        for(int i = 0; i < 28123; i++) {
            if(a[i] == false)
                sum += i;
        }
        System.out.println(sum);
    }
    private static boolean isAbundant(int a)
    {
        int sum = 0;
        for(int i = 1; i < a; i++) {
            if(a%i == 0)
                sum += i;
        }
        if(sum > a)
            return true;
        else
            return false;
    }
}
