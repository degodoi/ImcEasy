import tkinter as tk

class IMCEasy:
    def __init__(self, root):
        self.root = root
        self.root.title('ImcEasy@degodoi.felipe')
        self.root.geometry('300x280')  # Tamanho da janela
        self.root.resizable(False, False)  # Impedir redimensionamento
        self.root.configure(bg='#f0f0f0')  # Cor de fundo suave

        # Centralizar janela na tela
        window_width = 300
        window_height = 280
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        # Labels e Entrada de dados
        self.label_altura = tk.Label(self.root, text='Altura (m):', bg='#f0f0f0', font=('Arial', 12))
        self.label_altura.pack(padx=10, pady=(10, 5))  # Padding ajustado
        self.entry_altura = tk.Entry(self.root, justify='center')
        self.entry_altura.pack(padx=10, pady=5)

        self.label_peso = tk.Label(self.root, text='Peso (kg):', bg='#f0f0f0', font=('Arial', 12))
        self.label_peso.pack(padx=10, pady=5)
        self.entry_peso = tk.Entry(self.root, justify='center')
        self.entry_peso.pack(padx=10, pady=5)

        # Botão para calcular IMC
        self.button_calcular = tk.Button(self.root, text='Calcular IMC', command=self.calcular_imc, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'), width=15, height=1)
        self.button_calcular.pack(padx=10, pady=10, fill=tk.X)

        # Label para exibir resultado
        self.label_resultado = tk.Label(self.root, text='', fg='#333333', font=('Arial', 12, 'bold'))
        self.label_resultado.pack(padx=10, pady=5)

    def calcular_imc(self):
        try:
            altura = float(self.entry_altura.get())
            peso = float(self.entry_peso.get())

            if altura <= 0 or peso <= 0:
                self.label_resultado.config(text='Altura e peso devem ser maiores que zero.', fg='red')
            else:
                imc = peso / (altura ** 2)
                categoria = self.get_categoria_imc(imc)
                mensagem = f'Seu IMC é {imc:.2f} - {categoria}'
                self.label_resultado.config(text=mensagem, fg='#333333')
        except ValueError:
            self.label_resultado.config(text='Por favor, insira valores numéricos.', fg='red')

    def get_categoria_imc(self, imc):
        if imc < 18.5:
            return 'Abaixo do peso'
        elif 18.5 <= imc < 24.9:
            return 'Peso normal'
        elif 24.9 <= imc < 29.9:
            return 'Sobrepeso'
        elif 29.9 <= imc < 34.9:
            return 'Obesidade grau I'
        elif 34.9 <= imc < 39.9:
            return 'Obesidade grau II'
        else:
            return 'Obesidade grau III'

# Criar a janela principal
root = tk.Tk()
app = IMCEasy(root)
root.mainloop()
