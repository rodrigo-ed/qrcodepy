# 📱 Gerador de QR Code com Django + Tailwind

Um gerador de QR Code fullstack desenvolvido com **Django** no backend e **Tailwind CSS** no frontend. A aplicação permite ao usuário digitar qualquer texto ou link, gerar um QR Code automaticamente, visualizar e fazer o download da imagem.

---

## 🚀 Funcionalidades

- ✅ Geração de QR Code a partir de texto, link ou qualquer dado.
- 🎨 Interface moderna, responsiva e interativa com Tailwind CSS via CDN.
- 📥 Download do QR Code gerado em formato PNG.
- 🔄 Reset automático da imagem ao atualizar a página (limpeza da sessão).
- 🔐 Proteção contra CSRF via Django Forms.

---

## 📸 Demonstração

![Demo do App](https://via.placeholder.com/800x400?text=Inserir+captura+de+tela+aqui)

---

## 🧰 Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- Tailwind CSS (via CDN)
- qrcode (biblioteca Python)
- Pillow (para manipulação de imagem)
- HTML5 & CSS3

---

## 🛠️ Instalação e Execução

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/gerador-qrcode-django.git
cd gerador-qrcode-django

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o servidor
python manage.py runserver

Acesse em: http://127.0.0.1:8000
