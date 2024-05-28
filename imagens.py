from PIL import Image
from PIL import ImageDraw

# Funcao de somar imagens


def somar():
    img1 = Image.open("imagens/foto1.jpg")
    img2 = Image.open("imagens/foto2.jpg")
    img3 = Image.new(img1.mode, img1.size, "white")  # vai ser alterada

    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):

            pixel1 = img1.getpixel((i, j))
            pixel2 = img2.getpixel((i, j))

            # Soma os pixeis
            novopixelR = (pixel1[0] + pixel2[0],
                          255)[pixel1[0] + pixel2[0] > 255]

            novopixelG = (pixel1[1] + pixel2[1],
                          255)[pixel1[1] + pixel2[1] > 255]

            novopixelB = (pixel1[2] + pixel2[2],
                          255)[pixel1[2] + pixel2[2] > 255]

            img3.putpixel((i, j), (novopixelR, novopixelG, novopixelB))

    img3.save("imagens/somar.jpg")

# Funcao de subtrair imagens


def subtrair():
    img1 = Image.open("imagens/foto1.jpg")
    img2 = Image.open("imagens/foto2.jpg")
    img3 = Image.new(img1.mode, img1.size, "white")  # vai ser alterada
    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):

            pixel1 = img1.getpixel((i, j))
            pixel2 = img2.getpixel((i, j))

            novopixelR = (pixel1[0] - pixel2[0], 0)[pixel1[0] - pixel2[0] < 0]

            novopixelG = (pixel1[1] - pixel2[1], 0)[pixel1[1] - pixel2[1] < 0]

            novopixelB = (pixel1[2] - pixel2[2], 0)[pixel1[2] - pixel2[2] < 0]

            img3.putpixel((i, j), (novopixelR, novopixelG, novopixelB))

    img3.save("imagens/subtrair.jpg")

# Funcao de aplicar operaçao logica em imagem - OR


def ou():
    img1 = Image.open("imagens/foto1.jpg")
    img2 = Image.open("imagens/foto2.jpg")
    img3 = Image.new(img1.mode, img1.size, "white")  # vai ser alterada
    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):

            pixel1 = img1.getpixel((i, j))
            pixel2 = img2.getpixel((i, j))

            novopixelR = pixel1[0] | pixel2[0]

            novopixelG = pixel1[1] | pixel2[1]

            novopixelB = pixel1[2] | pixel2[2]

            img3.putpixel((i, j), (novopixelR, novopixelG, novopixelB))

    img3.save("imagens/or.jpg")

# Funcao de aplicar operaçao logica em imagem - AND


def e():
    img1 = Image.open("imagens/foto1.jpg")
    img2 = Image.open("imagens/foto2.jpg")
    img3 = Image.new(img1.mode, img1.size, "white")  # vai ser alterada
    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):

            pixel1 = img1.getpixel((i, j))
            pixel2 = img2.getpixel((i, j))

            novopixelR = pixel1[0] & pixel2[0]

            novopixelG = pixel1[1] & pixel2[1]

            novopixelB = pixel1[2] & pixel2[2]

            img3.putpixel((i, j), (novopixelR, novopixelG, novopixelB))

    img3.save("imagens/and.jpg")

# Aplica um filtro verde na imagem toda, isto é mete o r, b a 0


def filtroverde():
    img1 = Image.open("imagens/foto2.jpg")
    img2 = Image.new(img1.mode, img1.size, "white")  # vai ser alterada

    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):

            pixel1 = img1.getpixel((i, j))
            # Soma os pixeis
            novopixelR = 0

            novopixelG = pixel1[1]

            novopixelB = 0

            img2.putpixel((i, j), (novopixelR, novopixelG, novopixelB))

    img2.save("imagens/verde.jpg")

# Aplica o filtro do negativo na imagem


def negativo():
    image = Image.open("imagens/foto1.jpg")

    # criar a nova imagem

    negativo = Image.new(image.mode, image.size, "white")

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):

            pixel = image.getpixel((i, j))

            # Inverter a cor

            r = 255 - pixel[0]
            g = 255 - pixel[1]
            b = 255 - pixel[2]

            negativo.putpixel((i, j), (r, g, b))

    negativo.save("imagens/negativo.jpg")

# Coloca a imagem no filtro cinzento (como as fotos antigas)


def cinzentaImagem():
    img = Image.open('imagens/foto1.jpg')
    cinzenta = Image.new(img.mode, img.size, "white")

    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):

            pixel = img.getpixel((i, j))

            # mete a cinzenta

            corCizenta = int((pixel[0]*0.2125+pixel[1]*0.7174+pixel[2]*0.0721))

            cinzenta.putpixel((i, j), (corCizenta, corCizenta, corCizenta))

    cinzenta.save("imagens/cinzenta.jpg")
