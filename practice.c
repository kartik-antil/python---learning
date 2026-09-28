#include<stdio.h>
int main()
{
    int n,i=1,sum=0;
    printf("enter n:");
    scanf("%d",&n);

    for ( i = 1; i <=n; i++)
    {
        printf("%d\n",i);
        sum=sum+i;

    }
    printf("the sum of first %d natural no. is %d",i,sum);
    return 0;
}