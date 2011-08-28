public class PE047
{
    public static void main(String[] args)
    {
        for(int i = 1; ; i++) {
            int j;
            for(j = 0; j < 4; j++) {
                if(isFour(i+j))
                    continue;
                break;
            }
            if(j == 4) {
                System.out.println(i);
                break;
            }
        }
    }

    private static boolean isFour(int n)
    {
        int count = 0;
        for(int i = 2; n != 1; i++) {
            if(n%i == 0) {
                count++;
            }
            while(n%i == 0)
                n /= i;
        }
        if(count == 4)
            return true;
        return false;
    }
}
