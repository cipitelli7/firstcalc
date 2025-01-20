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
        return "Erro: não é possível calcular a raiz quadrada de um número negativo. O resultado da raiz quadrada de números negativos é um número complexo."
    return math.sqrt(a)

def raiz_cubica(a):
    return a ** (1/3)

def calcular_percentual(valor, percentual):
    return (valor * percentual) / 100

# Função para atualizar o resultado
def atualizar_resultado(resultado):
    resultado_label.config(text=f"Resultado: {resultado}")

# Função de soma
def soma():
    try:
        numeros = [float(entry.get()) for entry in entradas]
        resultado = somar(*numeros)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função de subtração
def subtracao():
    try:
        numeros = [float(entry.get()) for entry in entradas]
        resultado = subtrair(*numeros)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função de multiplicação
def multiplicacao():
    try:
        numeros = [float(entry.get()) for entry in entradas]
        resultado = multiplicar(*numeros)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função de divisão
def divisao():
    try:
        numeros = [float(entry.get()) for entry in entradas]
        resultado = dividir(*numeros)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função de raiz quadrada
def raiz_quadrada_func():
    try:
        num = float(entry.get())
        resultado = raiz_quadrada(num)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Função de raiz cúbica
def raiz_cubica_func():
    try:
        num = float(entry.get())
        resultado = raiz_cubica(num)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Função de cálculo de porcentagem
def percentual_func():
    try:
        valor = float(entry.get())
        percentual = float(entry_percentual.get())
        resultado = calcular_percentual(valor, percentual)
        atualizar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função principal para criar a janela
def criar_interface():
    global entradas, entry, entry_percentual, resultado_label
    root = tk.Tk()
    root.title("Calculadora Avançada")

    # Tela de entrada
    entradas = []
    for i in range(3):  # 3 campos de entrada
        entry = tk.Entry(root)
        entry.grid(row=0, column=i)
        entradas.append(entry)

    # Label para exibir o resultado
    resultado_label = tk.Label(root, text="Resultado: ", font=("Arial", 14))
    resultado_label.grid(row=4, column=0, columnspan=3)

    # Botões de operação
    btn_soma = tk.Button(root, text="Soma", command=soma)
    btn_soma.grid(row=1, column=0)

    btn_subtracao = tk.Button(root, text="Subtração", command=subtracao)
    btn_subtracao.grid(row=1, column=1)

    btn_multiplicacao = tk.Button(root, text="Multiplicação", command=multiplicacao)
    btn_multiplicacao.grid(row=1, column=2)

    btn_divisao = tk.Button(root, text="Divisão", command=divisao)
    btn_divisao.grid(row=2, column=0)

    btn_raiz_quadrada = tk.Button(root, text="Raiz Quadrada", command=raiz_quadrada_func)
    btn_raiz_quadrada.grid(row=2, column=1)

    btn_raiz_cubica = tk.Button(root, text="Raiz Cúbica", command=raiz_cubica_func)
    btn_raiz_cubica.grid(row=2, column=2)

    entry_percentual = tk.Entry(root)
    entry_percentual.grid(row=3, column=0)
    
    btn_percentual = tk.Button(root, text="Percentual", command=percentual_func)
    btn_percentual.grid(row=3, column=1)

    # Rodar a interface
    root.mainloop()

# Chamar a função para criar a interface
if __name__ == "__main__":
    criar_interface()
