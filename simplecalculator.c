#include<stdio.h>

int main(int argc,char *argv[])
{
  int a,b,res;
  char op;
  if(argc!=4)
  {
    printf("enter the correct number of operators\n");
  }
  a=atoi(argv[1]);
  b=atoi(argv[3]);
  op=*argv[2];
  switch(op)
  {
    case '+':res=(a+b);
             printf("%i\n",res);
             break;
    case '-':res=(a-b);
             printf("%i\n",res);
             break;
    case '*':res=(a*b);
             printf("%i\n",res);
             break;
    case '/':res=(a/b);
             printf("%i\n",res);
             break;
    default:printf("invalid operator\n");
   }
   return 0;
}
