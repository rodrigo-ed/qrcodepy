import qrcode
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk

def gerar_qrcode_e_mostrar(data):
    """
    Gera um QR Code para os dados fornecidos e o exibe em uma janela Tkinter.

    Args:
        data (str): Os dados a serem codificados no QR Code.
    """
    try:
        # Cria o objeto QRCode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Cria a imagem do QR Code
        img = qr.make_image(fill_color="black", back_color="white")

        # Converte a imagem para o formato Tkinter
        img_tk = ImageTk.PhotoImage(img)

        # Cria a janela Tkinter
        janela = tk.Tk()
        janela.title("QR Code Gerado")

        # Cria um label para exibir a imagem
        label_qrcode = tk.Label(janela, image=img_tk)
        label_qrcode.pack(padx=10, pady=10)

        # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        label_qrcode.image = img_tk

        # Inicia o loop principal da Tkinter
        janela.mainloop()

    except Exception as e:
        print(f"Ocorreu um erro ao gerar e exibir o QR Code: {e}")

if __name__ == "__main__":
    dados = input("Digite os dados para o QR Code: ")
    gerar_qrcode_e_mostrar(dados)