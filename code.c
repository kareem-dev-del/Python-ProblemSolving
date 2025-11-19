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


float avr(int x, int y , int z){
  return (x+ y +z )/ 3.0;
}
int main() {
 
  // int array[]={1,2,3,4,5};
  // int sizee= sizeof(array) / sizeof(array[0]);
  // printf("tne max:%d",maxArray(array,sizee));

  float x=5,y=4,z=1;
  printf("The avrege:%.2f",avr(x,y,z));

  
return 0; }

 
