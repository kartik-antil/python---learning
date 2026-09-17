#include <stdio.h>

int main() {
    int a, b, c;

    // User se teen numbers input lena
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    // && (AND) operator dono conditions true hone par hi run karega
    if (a >= b && a >= c) {
        printf("%d is the greatest number.\n", a);
    } 
    else if (b >= a && b >= c) {
        printf("%d is the greatest number.\n", b);
    } 
    else {
        printf("%d is the greatest number.\n", c);
    }

    return 0;
}

