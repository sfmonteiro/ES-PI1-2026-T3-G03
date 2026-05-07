from funcoes import cor, mod_vot
from funcoes.bd import cadastrar_eleitor

import time
import sys

def loading(msg, duracao):
    frames = [
    "◜",
    "◝",
    "◞",
    "◟"
    ]

    fim = time.time() + duracao

    while time.time() < fim:
        for frame in frames:
            sys.stdout.write(
                f"\r{cor.amarelo(frame)}  {cor.amarelo(msg)}"
            )
            sys.stdout.flush()
            time.sleep(0.07)

    # limpa a linha no final
    sys.stdout.write("\r" + " " * (len(msg) + 5) + "\r")
    sys.stdout.flush()


if __name__ == "__main__":
    mod_vot.mostrar_protocolo("VCP261191294")
    loading("Carregando protocolo...",5)