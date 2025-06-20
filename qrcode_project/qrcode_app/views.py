from django.shortcuts import render

import qrcode
from io import BytesIO
import base64
from django.shortcuts import render

def gerar_qrcode(request):
    imagem_qrcode = None
    if request.method == 'POST':
        dados = request.POST.get('dados')
        if dados:
            qr = qrcode.make(dados)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            imagem_qrcode = base64.b64encode(buffer.getvalue()).decode()
    return render(request, 'qrcode_app/index.html', {'imagem_qrcode': imagem_qrcode})

