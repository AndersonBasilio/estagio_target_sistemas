"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

"""

def verificar_lampadas(interruptor1, interruptor2):
    l1 = "acesa" if interruptor1 else "apagada"
    l2 = "acesa" if interruptor2 else "apagada"
    return l1, l2

interruptor1 = True
interruptor2 = False

estado_inicial = verificar_lampadas(interruptor1, interruptor2)

interruptor1 = False
interruptor2 = True

estado_final = verificar_lampadas(interruptor1, interruptor2)

for i in range(2):
    if estado_inicial[i] == "acesa" and estado_final[i] == "apagada":
        print(f"O interruptor {i + 1} controla a lâmpada acesa.")
    elif estado_inicial[i] == "apagada" and estado_final[i] == "apagada":
        print(f"O interruptor {i + 1} controla a lâmpada apagada.")
    elif estado_inicial[i] == "apagada" and estado_final[i] == "acesa":
        print(f"O interruptor {i + 1} nunca foi ligado.")