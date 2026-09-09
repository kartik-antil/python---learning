#include<stdio.h>
int main()
{
    int marks;
    printf("enter marks (1-100)=");
    scanf("%d",&marks);

    if(marks>=0 &&  marks<=33){
    printf("fail hogya ");}

    else if(marks>33 &&marks<100)
    printf("pass hogya  ");

    else if(marks==100){
    printf("top kr diya");}

    else  {
        printf("wrong marks");
    }
    return 0;
}
