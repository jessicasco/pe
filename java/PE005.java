public class PE005 {
    public static void main(String[] args) {
        int[] primeList = {2, 3, 5, 7, 11, 13, 17, 19};
        int result = 1;
        for (int prime: primeList) {
            int maxPower = (int)Math.floor(Math.log(20)/Math.log(prime));
            result *= (int)Math.pow(prime, maxPower);
        }
        System.out.println(result);
    }
}
