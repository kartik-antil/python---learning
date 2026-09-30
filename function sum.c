#include<stdio.h>
int sum(int n){
    if(n<=9&&n>=0){
        return n;
    }
    else{
        return n%10+ sum(n/10);
    }
}
int main(){
    int n=345629992;
   printf("the sum of digits is %dis %d",n,sum(n));
   return 0;
}