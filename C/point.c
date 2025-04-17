#include <stdio.h>

void exchangeValues(int *a, int *b){
int temp =*a;
  *a = *b;
  *b=temp;
}

int main(){
int x, y;
  x =10; y = 20;
printf("x: %d, y: %d",x,y);
exchangeValues(&x,&y);
printf("\n");  
printf("x: %d, y: %d", x, y);
  return 0;

}
