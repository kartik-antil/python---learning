#include<stdio.h>
int main (){
    int income ;
    printf("enter income:");
    scanf("%d",&income);

    if (income<=250000){
    printf("tax=%f",0*income);}

    else if (income>250000 &&income<=500000){
    printf("tax=%f",0.02*(income-250000));}

    else if(income>500000 &&income<=1000000){
    printf("tax=%f",0.02*(500000-250000)+ 0.5*(income-500000));}

    else if (income>1000000){
    printf("tax=%f",0.02*(500000-250000)+0.5*(1000000-500000)+0.7*(income-1000000));}

    return 0;

}