#include<stdio.h>

int main() {

    int n1, n2, n3;
    int soma, subtracao, multiplicacao;
    float divisao;

    //Solicita os números ao usuário
    printf("Digite o primeiro número: ");
    scanf("%d", &n1);
    printf("Digite o segundo número: ");
    scanf("%d", &n2);
    printf("Digite o terceiro número: ");
    scanf("%d", &n3);
    
    //Cálculo da soma, subtração, multiplicação e divisão
    soma = n1 + n2 + n3;
    subtracao = n1 - n2 - n3;
    multiplicacao = n1 * n2 * n3;
    
    //Verificar se a divisão é possível
    if (n2 != 0 && n3 != 0) {
        divisao = (float)n1 / n2 / n3;
        printf("divisao: %.2f\n", divisao);
    } else {
        printf("A divisão por zero não é possível.\n");
    }

    //Exibir o resultado das operações
    printf("Soma: %d\n", soma);
    printf("Subtração: %d\n, subtracao");
    printf("Multiplicação: %d\n, multiplicacao");

    //Verificar os operadores relacionais
    if (n1 > n2) {
        printf("O primeiro número é maior que o segundo.\n");
    } else {
        printf("O primeiro número não é maior que o segundo.\n");
    }
    if (n2 < n3) {
        printf("O segundo número é menor que o terceiro.\n");
    } else {
        printf("O segundo número não é menor que o terceiro.\n");
    }
    
    //Operadores lógicos para verificar se o primeiro número é positivo e o segundo é par
    if (n1 < 0 && n2 % 2 == 0) {
        printf("O primeiro número é positivo E o segundo é par.");
    } else {
        printf("O primeiro número não é positivo OU o segundo não é par.");
    }

    return 0;

}

