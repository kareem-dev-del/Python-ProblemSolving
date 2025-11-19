#include <stdio.h>
#include <math.h>
int main() {
 double number, power, result;
 printf("Enter a number: ");
 scanf("%f", &number);
 printf("Enter the power: ");
 scanf("%lf", &power);
 result = pow(number, power);
 printf("%.2lf raised to %.2lf = %.2lf\n", number, power, result);
 printf("Square root of %.2lf = %.2lf\n", number, sqrt(number));
 return 0; }