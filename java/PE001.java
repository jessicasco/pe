class PE001 {
    public static void main(String[] ars) {
        System.out.println(f(3, 1000) + f(5, 1000) - f(3 * 5, 1000));
    }
    
    private static int f(int a, int b) {
        int n = (b - 1) / a;
        return a * (n * (n + 1) / 2);
    }
}
