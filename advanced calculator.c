#include<stdio.h>
#include<math.h>
int main(){
    int choice;
    
        printf("---Calculator Menu---\n");
        printf("1.Integer Calculator\n");
        printf("2.float/double Calculator\n");
        printf("choose your choice (1 or 2):\n");

        scanf("%d", &choice);
        if(choice==1){
    int num1,num2;

    char op;

    printf("enter num1:");
    scanf("%d",&num1);

printf("enter any operator +,*,/,-,%:");
scanf(" %c",&op);

printf("enter num2:");
scanf("%d",&num2); 

switch(op){
    case '+': 
    printf("Result =%d\n",num1+num2);
    break;

    case '*':
    printf("Result=%d\n",num1*num2);
    break;

    case '/':
    if(num2==0){
        printf("division not possible");
    }
    else{
    printf("Result=%d\n",num1/num2);
    }
    break;

    case '-':
    printf("Result=%d\n",num1-num2);
    break;

    case '%':if(num2==0){
        printf("erorr: not possible");
    }
    else{
    printf("Result=%d\n",num1%num2);
    }
    break;

    default:
    printf("error:not possible");
    break;
}
}
else if(choice==2){
    double num1, num2;

    char op;

    printf("enter num1: ");
    scanf("%lf", &num1);

    printf("enter the op +,*,/,-,%");
    scanf(" %c", &op);

    printf("enter num2: ");
    scanf("%lf", &num2);
    
    switch(op){
        case '+':
        printf("Result=%.5lf\n",num1+num2);
        break;

        case '*':
        printf("Result=%.5lf\n",num1*num2);
        break;

        case '/':if(num2==0){
            printf("Division not possible");
        }
        else{
        printf("Result=%.5lf\n",num1/num2);
        }
        break;

        case '-':
        printf("Result=%.5lf\n",num1-num2);
        break;

        case '%':if(num2=0){
            printf("error: not possible");
        }
        else{
        printf("Result=%.5lf\n",num1,num2);
        }
        break;

        default:
        printf("error not possible");
        break;
    }
}
    else{
        printf("error:invalid choice please restart and press 1 and 2\n");
    }
    return 0;
}