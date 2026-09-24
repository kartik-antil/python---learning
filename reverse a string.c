#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    
    printf("Enter a string: ");
    scanf("%[^\n]s", str); // Reads string with spaces

    int len = strlen(str);
    char *start = str;
    char *end = str + len - 1;

    // Swap characters from both ends moving inward
    while (start < end) {
        char temp = *start;
        *start = *end;
        *end = temp;
        
        start++;
        end--;
    }

    printf("Reversed string: %s\n", str);
    return 0;
}
