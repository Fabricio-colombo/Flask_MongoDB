

def brutal_force():
    import itertools
    import string
    import time
    def ataque_forca_bruta(senha_correta):
        caracteres_possiveis = string.ascii_letters + string.digits + string.punctuation
        print("Caracteres possíveis:", caracteres_possiveis)
        tentativas = 0
        while True:
            for tentativa in itertools.product(caracteres_possiveis, repeat=4):
                senha_tentativa = ''.join(tentativa)
                tentativas += 1
                if senha_tentativa == senha_correta:
                    return senha_tentativa, tentativas

    senha_correta = '1234ab'

    print("Iniciando ataque de força bruta...")
    inicio = time.time()

    senha_quebrada, tentativas = ataque_forca_bruta(senha_correta)

    fim = time.time()
    tempo_total = fim - inicio

    if senha_quebrada:
        print("Senha quebrada:", senha_quebrada)
        print("Número de tentativas:", tentativas)
        print("Tempo total:", tempo_total, "segundos")
        
if __name__ == "__main__":
    brutal_force()
