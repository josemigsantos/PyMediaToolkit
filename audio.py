from pydub import AudioSegment

# Corta o audio1 em duas partes iguais


def cortar():
    audio1 = AudioSegment.from_wav("audio/audio1.wav")
    duracao_audio1 = len(audio1)
    metade = duracao_audio1/2
    primeira_parte = audio1[:metade]
    ultima_parte = audio1[-metade:]

    primeira_parte.export("audio/audio1_1m.wav", format="wav")
    ultima_parte.export("audio/audio1_2m.wav", format="wav")
# junta o audio 1 com o audcio 2


def juntar():
    audio1 = AudioSegment.from_wav("audio/audio1.wav")
    audio2 = AudioSegment.from_wav("audio/audio2.wav")

    audio3 = audio1 + audio2

    audio3.export("audio/juncao.wav", format="wav")
# mete um eco de fundo no audio 1


def eco():
    um_segundo_silencio = AudioSegment.silent(duration=1000)
    audio1 = AudioSegment.from_wav("audio/audio1.wav")
    musica_por_cima = audio1 + um_segundo_silencio
    musica_de_fundo = um_segundo_silencio + audio1
    musica_de_fundo -= 4
    eco = musica_por_cima * musica_de_fundo
    eco.export("audio/eco.wav", format="wav")
# normaliza o audio1


def normaliza():
    audio1 = AudioSegment.from_wav("audio/audio1.wav")
    normalizado = audio1 - 10  # REDUZIR 10 decibéis

    normalizado.export("audio/norma.wav", format="wav")
