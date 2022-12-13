import pyttsx3
from time import sleep

eng = pyttsx3.init()
eng.setProperty("voice", "brazil")
eng.setProperty("volume", 1.)


def responder(userMsg):
    msg = userMsg.lower()
    if msg == 'como você está?':
        return 'Estou bem! Obrigado por perguntar.'
    elif msg == "tudo bem?":
        return 'Estou bem! Obrigado por perguntar.'
    elif msg == 'stop' or msg == 'parar':
        quit()
    else:
        return 'Não entendi, pode tentar novamente?'

def main():
    print('Assistent: Bem vindo!')
    print('Assistent: Como posso ajudar?')
    eng.say(['Bem vindo!', 'Como posso ajudar?'])
    eng.runAndWait()
    rodando = True

    while True:
        userMsg = input('You: ')
        response = responder(userMsg)
        eng.say(response)
        eng.runAndWait()
        print(response)


if __name__ == "__main__":
    main()
