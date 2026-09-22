#include<stdio.h>
int main(){
    int x;
    int i=1;
    int factorial =1;
printf("enter your number:");
scanf("%d",&x);

while(i<=x);{
factorial=factorial*i;
i++;
}
printf("the value of %d factorial is %d\n",x,factorial);

return 0;
}