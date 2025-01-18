
import math

# Funções para as operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não é possível calcular a raiz quadrada de um número negativo."
    return math.sqrt(a)

# Função principal que solicita ao usuário as operações
def main():
    print("Calculadora Avançada")

    while True:
        print("\nEscolha a operação desejada:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Sair")

        try:
            opcao = int(input("\nDigite o número da operação: "))

            if opcao == 6:
                print("Saindo da calculadora. Até logo!")
                break

            if opcao == 5:
                num1 = float(input("\nDigite o número para calcular a raiz quadrada: "))
                print(f"A raiz quadrada de {num1} é: {raiz_quadrada(num1)}")
            else:
                num1 = float(input("\nDigite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == 1:
                    resultado = somar(num1, num2)
                    print(f"O resultado da soma de {num1} + {num2} é: {resultado}")
                elif opcao == 2:
                    resultado = subtrair(num1, num2)
                    print(f"O resultado da subtração de {num1} - {num2} é: {resultado}")
                elif opcao == 3:
                    resultado = multiplicar(num1, num2)
                    print(f"O resultado da multiplicação de {num1} * {num2} é: {resultado}")
                elif opcao == 4:
                    resultado = dividir(num1, num2)
                    print(f"O resultado da divisão de {num1} / {num2} é: {resultado}")
                else:
                    print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Por favor, digite apenas números válidos.")

# Chamando a função principal
if __name__ == "__main__":
    main()
