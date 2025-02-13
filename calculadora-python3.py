import tkinter as tk
from tkinter import messagebox
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
        return "Erro: não é possível calcular a raiz quadrada de um número negativo."
    return math.sqrt(a)

def raiz_cubica(a):
    return a ** (1/3)

def calcular_percentual(valor, percentual):
    return (valor * percentual) / 100

# Função para exibir o resultado
def exibir_resultado(resultado):
    label_resultado.config(text=f"Resultado: {resultado}")

# Função para pegar os valores dos campos e realizar a operação
def realizar_operacao(opcao):
    try:
        # Pegando os números inseridos
        entrada = entry_numeros.get()
        numeros = [float(num) for num in entrada.split()]  # Convertendo os números separados por espaço
        
        if opcao == 1:  # Soma
            resultado = somar(*numeros)
        elif opcao == 2:  # Subtração
            resultado = subtrair(*numeros)
        elif opcao == 3:  # Multiplicação
            resultado = multiplicar(*numeros)
        elif opcao == 4:  # Divisão
            resultado = dividir(*numeros)
        elif opcao == 5:  # Raiz Quadrada (apenas um número)
            if len(numeros) != 1:
                resultado = "Por favor, insira apenas um número para a raiz quadrada."
            else:
                resultado = raiz_quadrada(numeros[0])
        elif opcao == 6:  # Raiz Cúbica (apenas um número)
            if len(numeros) != 1:
                resultado = "Por favor, insira apenas um número para a raiz cúbica."
            else:
                resultado = raiz_cubica(numeros[0])
        elif opcao == 7:  # Cálculo de Porcentagem (do primeiro número)
            if len(numeros) != 2:
                resultado = "Por favor, insira dois números para calcular a porcentagem."
            else:
                resultado = calcular_percentual(numeros[0], numeros[1])
        else:
            resultado = "Operação inválida."

        exibir_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos separados por espaço.")

# Função para limpar os campos
def limpar():
    entry_numeros.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Avançada")
janela.geometry("400x400")

# Labels e entradas
label_numeros = tk.Label(janela, text="Digite os números (separados por espaço):")
label_numeros.pack()

entry_numeros = tk.Entry(janela)
entry_numeros.pack()

# Botões de operação
botao_somar = tk.Button(janela, text="Soma", command=lambda: realizar_operacao(1))
botao_somar.pack()

botao_subtrair = tk.Button(janela, text="Subtração", command=lambda: realizar_operacao(2))
botao_subtrair.pack()

botao_multiplicar = tk.Button(janela, text="Multiplicação", command=lambda: realizar_operacao(3))
botao_multiplicar.pack()

botao_dividir = tk.Button(janela, text="Divisão", command=lambda: realizar_operacao(4))
botao_dividir.pack()

botao_raiz_quadrada = tk.Button(janela, text="Raiz Quadrada", command=lambda: realizar_operacao(5))
botao_raiz_quadrada.pack()

botao_raiz_cubica = tk.Button(janela, text="Raiz Cúbica", command=lambda: realizar_operacao(6))
botao_raiz_cubica.pack()

botao_percentual = tk.Button(janela, text="Cálculo de Porcentagem", command=lambda: realizar_operacao(7))
botao_percentual.pack()

# Botão de limpar
botao_limpar = tk.Button(janela, text="Limpar", command=limpar)
botao_limpar.pack()

# Label pa
