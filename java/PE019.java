public class PE019
{
    public static void main(String[] args)
    {
        int[][] days = {{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}, {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}};
        int count= 0;
        int dayOfWeek = 1;
        for(int i = 1900; i <= 2000; i++) {
            int leap = 0;
            if((i%4 == 0 && i%100 != 0) || i%400 == 0) 
                leap = 1;
            for(int j = 1; j <= 12; j++) {
                if(i == 2000 && j == 12)
                    break;
                dayOfWeek += days[leap][j-1];
                dayOfWeek %= 7;
                if(dayOfWeek == 0){
                    if(i == 1900)
                        continue;
                    count ++;
                }
            }
        }
        System.out.println(count);
    }
}
