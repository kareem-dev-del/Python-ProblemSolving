#include <stdio.h>

// int maxArray(int arr[],int size){
//   int max=arr[0];
//   for(int i=0;i<size;i++){
//     if (arr[i] > max){
//       max=arr[i];
//     }
//   }
//   return max;
// }


// float avr(int x, int y , int z){
//   return (x+ y +z )/ 3.0;
// }

// int Fib (int n){
//   if (n == 0 || n == 1) return n;
//    return  Fib(n-1) + Fib(n-2) ;

// }



float L(int km){
  return km * 0.621371;
}



int main() {
 
  // int array[]={1,2,3,4,5};
  // int sizee= sizeof(array) / sizeof(array[0]);
  // printf("tne max:%d",maxArray(array,sizee));

  // float x=5,y=4,z=1;
  // printf("The avrege:%.2f",avr(x,y,z));
// int x=5;
// int *p=&x;
// printf("value:%d\n",x);
// printf("adress of integers:%p\n",&x);
// printf("valve store poin: %d\n",*p);
// printf("adress of poin:%p",&p);
  // int num=5;
  // printf("the Fibonacci:%d",Fib(num));
 int arr[]={1,5,10};
 for(int i=0;i<3;i++){
  printf("%d:km converts %.3f miles: \n",arr[i],L(arr[i]));
 }
return 0; }

 
