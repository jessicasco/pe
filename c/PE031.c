#include <stdio.h>
 
int coins[8] = {200, 100, 50, 20, 10, 5, 2, 1};
 
int findposs(int money, int maxcoin)
{
    int sum = 0;
    if(maxcoin == 7) return 1; //maybe this code not needed
    for(int i = maxcoin; i<8;i++)
    {
        if (money-coins[i] == 0) sum+=1;
        else if (money-coins[i] > 0) sum+=findposs(money-coins[i], i);
    }
    return sum;     
}
 
int main()
{
    printf("%d\n", findposs(200, 0));
}
