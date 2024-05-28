import cv2 

# pega numa imagem e mete em preto e branco e devolve
def gray(img, w, h):

    for i in range(w):
        for j in range(h):
            #BGR
            pixel = int((img[j,i][2]*0.2125+img[j,i][1]*0.7174+img[j,i][0]*0.0721))
            img[j,i] =[pixel, pixel, pixel]
    return img

# Funcao do video
def video():
    # le o video
    original = cv2.VideoCapture('imagens/video.mp4')
    

    # Resolução do video - converter de float para int
    frame_width = int(original.get(3))
    frame_height = int(original.get(4))

    size = (frame_width, frame_height)
    result = cv2.VideoWriter('imagens/Preto_E_Branco.mp4',
                            cv2.VideoWriter_fourcc(*'m','p','4','v'),
                            30, size)  # o numero são os frames por segundo

    ret = bool(True)
    # corre o loop
    while ret:
        
        # extrariar o frame
        ret, img = original.read()
        if ret == True:
            h, w, canais = img.shape
            gray1 = gray(img, w, h)
            # guardar no ficheiro em preto e branco
            result.write(gray1)
    
    original.release()
    result.release()