import qrcode
from PIL import Image

# Caminho da imagem de fundo (ex: sua logo)
background_path = "logo.png"  # Certifique-se de que esse arquivo esteja na mesma pasta

# Link desejado
link = "https://dnagenetica.klingo.app/#/novocadastro/27?s=1"

# Nome do arquivo de saída
output_file = "qrcode_dna_final.png"

# Gera o QR Code com fundo branco
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(link)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Torna o fundo branco do QR Code transparente
datas = qr_img.getdata()
newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0))  # Transparente
    else:
        newData.append(item)
qr_img.putdata(newData)

# Abre a imagem de fundo
background = Image.open(background_path).convert("RGBA")

# Redimensiona o QR Code
qr_img = qr_img.resize((300, 300))

# Centraliza o QR Code no fundo
bg_width, bg_height = background.size
qr_width, qr_height = qr_img.size
position = ((bg_width - qr_width) // 2, (bg_height - qr_height) // 2)

# Cola o QR sobre o fundo
background.paste(qr_img, position, qr_img)

# Salva a imagem final
background.save(output_file)
print(f"QR Code com fundo salvo como: {output_file}")


#167446