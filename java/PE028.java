public class PE028 {
    public static void main(String[] args) {
        int sum = 1;
        int a = 1;
        int b = 2;
        for(int i = 1; i <= 500; i++) {
            for(int j = 1; j <= 4; j++) {
                a += b;
                sum += a;
            }
            b += 2;
        }
        System.out.println(sum);
    }
}

