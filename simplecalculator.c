#include<stdio.h>
#include<conio.h>

int main(int argc, char* argv[])
{
  float n1,n2,result;
  char choice;
  if(argc==4)
  {
    sscanf(argv[1],"%f",&n1);
    sscanf(argv[2],"%c",&choice);
    sscanf(argv[3],"%f",&n2);
  }
  else if(argc==2)
  {
    sscanf(argv[1],"%f",&n2);
    scanf("%c", &choice);
    scanf("%f", &n1);
  }
  else
  {
    printf("input error\n");
  }
  switch(choice)
  {
    case '+': result=(n1+n2);
              break;
    case '-': result=(n1-n2);
              break;
    case '*': result=(n1*n2);
              break;
    case '/': if(n2==0)
                printf("divide by zero error\n");
              else
                result=n1/n2;
              break;
    default: printf("input error\n");
  }
  printf("%f\n", result);
}