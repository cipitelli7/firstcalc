import math

# Funções para as operações
def somar(*args):
    return sum(args)

def subtrair(*args):
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def dividir(*args):
    resultado = args[0]
    try:
        for num in args[1:]:
            resultado /= num
        return resultado
    except ZeroDivisionError:
        return "Erro: divisão por zero."

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não é possível calcular a raiz quadrada de um número negativo. O resultado da raiz quadrada de números negativos é um número complexo."
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
                # Solicitar ao usuário os números
                numeros = []
                print("\nDigite os números (digite 'fim' para encerrar):")
                while True:
                    entrada = input("Digite um número: ")
                    if entrada.lower() == 'fim':
                        if len(numeros) < 2 and opcao in [1, 3, 4]:  # Soma, Multiplicação e Divisão precisam de pelo menos 2 números
                            print("É necessário inserir pelo menos dois números para realizar essa operação.")
                            continue
                        break
                    try:
                        numero = float(entrada)
                        numeros.append(numero)
                    except ValueError:
                        print("Por favor, digite um número válido.")
                
                # Realizar a operação escolhida
                if opcao == 1:
                    resultado = somar(*numeros)
                    print(f"O resultado da soma é: {resultado}")
                elif opcao == 2:
                    resultado = subtrair(*numeros)
                    print(f"O resultado da subtração é: {resultado}")
                elif opcao == 3:
                    resultado = multiplicar(*numeros)
                    print(f"O resultado da multiplicação é: {resultado}")
                elif opcao == 4:
                    resultado = dividir(*numeros)
                    print(f"O resultado da divisão é: {resultado}")
                else:
                    print("Opção inválida. Por favor, digite uma opção válida de 1 a 6.")

        except ValueError:
            print("Por favor, digite apenas números válidos.")

# Chamando a função principal
if __name__ == "__main__":
    main()
