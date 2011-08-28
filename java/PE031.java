public class PE031
{
    public static void main(String[] args)
    {
        int num = 1;
        for(int a = 0; a <= 2; a++)
        for(int b = 0; b <= 4; b++)
        for(int c = 0; c <= 10; c++)
        for(int d = 0; d <= 20; d++)
        for(int e = 0; e <= 40; e++)
        for(int f = 0; f <= 100; f++){
            if(200-a*100-b*50-c*20-d*10-e*5-f*2 >= 0)
                num++;
        }
        System.out.println(num);
    }
}
