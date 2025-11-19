#include <stdio.h>

int maxArray(int arr[],int size){
  int max=arr[0];
  for(int i=0;i<size;i++){
    if (arr[i] > max){
      max=arr[i];
    }
  }
  return max;
}
int main() {
 
  int array[]={1,2,3,4,5};
  int sizee= sizeof(array) / sizeof(array[0]);
  printf("tne max:%d",maxArray(array,sizee));

  
return 0; }

 
