 #include <stdio.h>
 int main() {
 int x = 10;
 int *p = &x;
 printf("&pValue of x: %d\n", x);
 printf("*pAddress of x: %p\n", &x);
 printf("Value stored at pointer p: %p\n", p);
 printf("the Value that pointer p points to is: %d\n", *p);
 printf("Address of pointer: %p\n", &p);
int x[5]={10,20,30,40,50};
int *p=x;
printf("%d\n",*(p + 2));
printf("%d",strlen(x));
 return 0;
 }