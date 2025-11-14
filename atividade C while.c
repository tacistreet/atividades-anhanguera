/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
int main() {
    int num;
    int soma = 0;
   
    while (num != 0) {
    printf("Digite um número ou 0 para encerrar: \n");
    scanf("%d" ,&num);
    if (num == 0) {
        break;
    }
    soma += num;
    }
   printf("A soma total dos números é: %d\n", soma);
   
    return 0;
}













