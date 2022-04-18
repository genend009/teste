#include <stdio.h>

int calc_a(int d){
  int e = d *3;
  return e ;
}

int main()
{
    int a =0;
    int b =0;
    int c =0;
    int i =0;


    a = 2;
    b = 4;
    c = a+b;
for ( i = 0; i < 100; i++)
{
    c = calc_a(c) ;
    printf("%d\n",c);

    if (c >= 10000)
    {
        c = 1;
        break;
    }
    
}

 int f = 0;
 f = calc_a(c);
 
 printf("%d\n",f);


}