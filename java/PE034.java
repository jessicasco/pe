public class PE034 {
    public static void main(String[] args) {
        int sum = 0;
        for(int i = 3; i < 10000000; i++) {
            if(isCurious(i)) {
                sum += i;
            }
        }
        System.out.println(sum);
    }
    private static boolean isCurious(int i) {
        int k = i;
        int sum = 0;
        while(k != 0) {
            sum += factor(k%10);
            k /= 10;
        }
        if(sum == i) {
            return true;
        }
        else
            return false;
    }
    private static int factor(int n) {
        int result = 1;
        if(n == 0)
            return result;
        for(int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
