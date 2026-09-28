#include<stdio.h>
int main()
{
    int n,i=1,factorial=1;
    printf("enter n:");
    scanf("%d",&n);

    for (i=1;i<=n;i++)
    {
       factorial=factorial*i;
    
    }
    printf("the value of %d factorial is %d",n,factorial);
    return 0;
}