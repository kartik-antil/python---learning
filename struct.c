#include<stdio.h>
#include<stdlib.h>

    struct node {
        int data;
        struct node *next;
    };
    int main(){
        struct node *p;
        p=(struct node*)malloc(sizeof(struct node));
    p->data = 10;
    p->next = NULL;
printf("%d",p->data);
free(p);
return 0;

}