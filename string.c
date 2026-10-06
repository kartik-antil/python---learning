#include <stdio.h>
#include<string.h>
char*slice(char str[],int m, int n)
{

    int i = 0, count;
    char*ptr1=&str[m];
    char*ptr2=&str[n];
    
    str[n]='\0';
    return ptr1;
}
int main()
{
    char str[] = "kartik bhai";
    printf("%s", slice(str,1,8));

    return 0;
}