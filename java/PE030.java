public class PE030 {
    public static void main(String[] args) {
        int sum = 0;
        for(int i = 2; i <= 999999; i++) {
            if(isFifth(i)) {
                sum += i;
            }
        }
        System.out.println(sum);
    }
    private static boolean isFifth(int i) {
        int j = i;
        int sum = 0;
        while(j != 0) {
            sum += (int)Math.pow(j%10, 5);
            j /= 10;
        }
        if(sum == i) {
            return true;
        }
        else {
            return false;
        }
    }
}
