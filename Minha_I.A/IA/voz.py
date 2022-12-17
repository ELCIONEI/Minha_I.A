

import speech_recognition as sr

import os
#funcao para ouvir e reconhecer a fala

def ouvir_microfone():
    #Habilita o microfone
    microfone = sr.Recognizer()

    #usuando o microfone
    with sr.Microfone() as source:

        #Algoritimo para redução de ruidos, pegara o som mais proximo
        microfone.adjust_for_ambiente_noise(source)

        #Frase para iniciar a fala desejada
        print("Diga o que deseja!")

        #armazena a fala
        audio = microfone.listen(source)
    try:
        #passa a variavel para o algoritimo reconhecedor de padroes
        frase = ouvir_microfone.recognize_google(audio, language='pt-BR')
        
        if "navegador" in frase:
            os.system("start Chrome.exe")
        elif "Exel" in frase:
            os.system("start Exel.ex")
        #retorna a frase pronunciada
        print("Frase pronunciaada: " + frase)

        #caso não reconheça a pronuncia retornara
    except sr.UnknownValueError:
            print("Comando não recocnhecido")
        
    return frase
    ouvir_microfone()