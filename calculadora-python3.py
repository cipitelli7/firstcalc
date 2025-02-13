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

# Função para pegar o valor dos campos e realizar a operação
def realizar_operacao(opcao):
    try:
        valor1 = float(entry_num1.get())
        if opcao != 5:  # Operações de raiz não precisam de dois valores
            valor2 = float(entry_num2.get())
        else:
            valor2 = None

        if opcao == 1:  # Soma
            resultado = somar(valor1, valor2)
        elif opcao == 2:  # Subtração
            resultado = subtrair(valor1, valor2)
        elif opcao == 3:  # Multiplicação
            resultado = multiplicar(valor1, valor2)
        elif opcao == 4:  # Divisão
            resultado = dividir(valor1, valor2)
        elif opcao == 5:  # Raiz Quadrada
            resultado = raiz_quadrada(valor1)
        elif opcao == 6:  # Raiz Cúbica
            resultado = raiz_cubica(valor1)
        elif opcao == 7:  # Cálculo de Porcentagem
            percentual = float(entry_num2.get())
            resultado = calcular_percentual(valor1, percentual)
        else:
            resultado = "Operação inválida."

        exibir_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função para limpar os campos
def limpar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Avançada")
janela.geometry("400x400")

# Labels e entradas
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(janela)
entry_num1.pack()

label_num2 = tk.Label(janela, text="Número 2 (se aplicável):")
label_num2.pack()

entry_num2 = tk.Entry(janela)
entry_num2.pack()

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

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
