#include<stdio.h>
void func(int n){
    if(n==1){
    printf("*");
    }
else{
    printf("*");
    func(n-1);
}
}
int main(){
   int  n=5;
   func(n);
   func(n);
return 0;
}
