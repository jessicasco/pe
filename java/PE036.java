public class PE036 {
    public static void main(String[] args) {
        int sum = 0;
        for(int i = 1; i < 1000000; i++) {
            if(isPalindromicTwo(i) && isPalindromicTen(i))
                sum += i;
        }
        System.out.println(sum);
    }
    private static boolean isPalindromicTwo(int n) {
        String b = Integer.toBinaryString(n);
        int k = b.length();
        for(int i = 0; i < k; i++) {
            if(b.charAt(i) == b.charAt(k-1-i))
                continue;
            return false;
        }
        return true;
    }
    private static boolean isPalindromicTen(int n) {
        String a = ""+n+"";
        int k = a.length();
        for(int i = 0; i < k; i++) {
            if(a.charAt(i) == a.charAt(k-i-1))
                continue;
            return false;
        }
        return true;
    }
}
