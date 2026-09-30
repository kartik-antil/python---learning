#include<stdio.h>
int main(){
    int num1,num2;
    char op;
    printf("enter num1:");
    scanf("%d",&num1);
printf("enter any operator +,*,/,-,%:");

scanf(" %c",&op);
printf("enter num2:");
scanf("%d",&num2); 
switch(op){
    case '+': printf("Result =%d",num1+num2);
    break;
    case '*':
    printf("Result=%d",num1*num2);
    break;
    case '/':
    if(num2==0){
        printf("division not possible");
    }
    else{
    printf("Result=%d",num1/num2);
    }
    break;
    case '-':
    printf("Result=%d",num1-num2);
    break;
    case '%':
    printf("Result=%d",num1%num2);
    break;   
    default:
    printf("error:not possible");
    break;
}
}