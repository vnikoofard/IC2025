import tkinter as tk

def inverter_frase():
    frase = entrada.get()
    frase_inversa = frase[::-1]
    resultado.config(text=frase_inversa)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Inversor de Frases")

# Entrada de texto
tk.Label(janela, text="Digite uma frase:").pack()
entrada = tk.Entry(janela, width=50)
entrada.pack()

# Botão para inverter a frase
botao = tk.Button(janela, text="Inverter", command=inverter_frase)
botao.pack()

# Label para exibir o resultado
resultado = tk.Label(janela, text="")
resultado.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()