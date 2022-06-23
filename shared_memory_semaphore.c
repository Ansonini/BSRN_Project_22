#include <stdio.h>
#include <stdlib.h>

void conv(num[]);

void log(num[]);

void stat(num[]);

void report();

int main() {
    int num[10];
    conv(num);
 //   log(num);
    return 0;
}

void conv(num[]) {

    for (int i = 1; i <= 10; i++) {
        num = rand() % 1000 + 1;
        printf("%d\n", num);
    }
}

void log(num[]) {
   /* FILE *fp = NULL;

    fp = fopen("log_C.txt", "w");

    if (fp != NULL) {
        for (int i = 0; i <= 10; i++) {
            fprintf("%d \n", num[i]);
        }
    } */
}

void stat(num[]) {
int sum, med;
    for (int i = 0; i < num; i++) {
        sum += num[i];
    }
    med = sum / 10;
}

void report() {

}
