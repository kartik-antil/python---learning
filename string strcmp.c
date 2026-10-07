#include <stdio.h>
#include<string.h>
int main() {
    char st[]="kartik";
    char s1[56]="kartik";
    char s2[56]="bhai";
    //printf("%d",strlen(st));

    //char source[]="kartik";
    char target[30];
    strcpy(target, st);
    //printf("%s %s",st,target);
    strcat(s1,s2);
    //printf("%s ", s1);

    int a=strcmp(" deep far","a joke");//DJ IS NEGATIVE            
    printf("%d",a);

    return 0;
}