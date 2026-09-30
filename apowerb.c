#include<stdio.h>
int power(int a ,int b){
    if(b==0){
        return 1;
    }
    else{
        return a* power(a,b-1);
    }

}
int main(){
    int a=2,b=10,result;
     result =power(a,b);
    printf("%d raised to power %d is %d\n",a,b,result);
    return 0;
}