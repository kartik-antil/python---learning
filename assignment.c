#include <stdio.h>

struct Student {
    int rollNumber;
    float marks;
};

int main() {

    struct Student s1;
    s1.rollNumber = 101;
    s1.marks = 85.5;


    printf("Roll numbe: %d\n", s1.rollNumber);
    printf("Marks: %.1f\n", s1.marks);

    return 0;
}