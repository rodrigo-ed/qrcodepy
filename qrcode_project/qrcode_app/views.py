from django.shortcuts import render

import qrcode
from io import BytesIO
import base64
from django.shortcuts import render
from django.http import HttpResponse

# This function generates a QR code based on the data provided in the POST request.
def gerar_qrcode(request):
    if request.method == 'POST':
        dados = request.POST.get('dados')
        if dados:
            qr = qrcode.make(dados)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            imagem_qrcode = base64.b64encode(buffer.getvalue()).decode()
            return render(request, 'qrcode_app/index.html', {
                'imagem_qrcode': imagem_qrcode,
                'dados': dados,
            })
    # Em requisições GET (ex: refresh), mostra apenas a tela limpa
    return render(request, 'qrcode_app/index.html')


# This function allows the user to download the generated QR code as a PNG file.
def download_qrcode(request):
    dados = request.GET.get('dados')
    if not dados:
        return HttpResponse("Dados não fornecidos.", status=400)
    qr = qrcode.make(dados)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
    return response