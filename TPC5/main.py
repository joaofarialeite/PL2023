
import sys
import re

MOEDAS = ["10c","20c","50c","1e","2e"]
#saldo = 0.0

def converter_em_str(valor):
    valor_euros = int(valor)
    valor_centimos = int((valor - valor_euros) * 100)
    return f"{valor_euros}e{valor_centimos:02d}c"

def converter_em_valor(saldo):
    saldo = saldo.replace("e", ".").replace("c", "")
    return float(saldo)

def define_saldo(euros, centimos):

    total_cents = sum(euros)*100 + sum(centimos)

    saldo_euros = total_cents // 100
    saldo_cents = total_cents % 100

    return f"{saldo_euros}.{saldo_cents:02d}"

def converteremdinheiro(euros, centimos, valor_a_adicionar=0):
    total_cents = round(sum(euros)*100 + sum(centimos) + valor_a_adicionar*100)

    saldo_euros = total_cents // 100
    saldo_cents = total_cents % 100

    #saldo = float(f"{saldo_euros}e.{saldo_cents:02d}c")
    return (f"{saldo_euros}e{saldo_cents:02d}c")

def converter_em_dinheiro_valido(valor):
    valor_cents = int(valor * 100)
    saldo_euros = valor_cents // 100
    saldo_cents = valor_cents % 100
    return f"{saldo_euros}e{saldo_cents:02d}c"

def parsing():

    chamada = False

    while True:

        texto = input()

        if re.search(r'^LEVANTAR$',texto):
            chamada = True
            saldo = 0.0

        elif chamada:
            re_moeda = re.search(r'^MOEDA', texto)
            re_telefone = re.search(r'^T=(?P<numero>\d{9})$',texto)
            re_pousar = re.search(r'^POUSAR$',texto)


            if re_moeda:
                re_valores = re.findall(r'\d{1,2}\w{1}',texto)
                #re_valores = re.search(r'(?P<moedas>(\d{1,2}\w{1}))',texto)


                if all(elem in MOEDAS for elem in re_valores):
                    a = 5
                else:
                    print("Moeda invalida")
                    break

                valores_comuns = [valor for valor in re_valores if valor in MOEDAS]

                valores_nao_comuns = [valor for valor in re_valores if valor not in MOEDAS]

                valores_eur = [valor for valor in valores_comuns if re.match(r'.*e\b',valor)]

                valores_centimos = [valor for valor in valores_comuns if re.match(r'.*c\b', valor)]

                l_soma_valores_eur = [int(re.search(r'\d*(?=e)', valor).group(0)) for valor in valores_eur if valor.endswith('e')]

                l_soma_valores_centimos = [int(re.search(r'\d*(?=c)', valor).group(0)) for valor in valores_centimos if valor.endswith('c')]

                soma_valores_centimos = sum(int(valor) for valor in l_soma_valores_centimos)

                soma_valores_eur = sum(int(valor) for valor in l_soma_valores_centimos)

                #print(l_soma_valores_eur,l_soma_valores_centimos)

                saldo = float(define_saldo(l_soma_valores_eur,l_soma_valores_centimos))

                print(f"maq: saldo = {converteremdinheiro(l_soma_valores_eur,l_soma_valores_centimos)}")

            if re_telefone and saldo > 0.0:

                numero = re_telefone.group('numero')

                if numero.startswith('00'):
                    if saldo < 1.5:
                        print("maq: Saldo insuficiente para chamada internacional")
                    else:
                        saldo -= 1.5
                        saldo = converteremdinheiro(l_soma_valores_eur, l_soma_valores_centimos, -1.5)
                        print(f'maq: "saldo = {saldo}"')

                elif numero.startswith('601') or numero.startswith('641'):
                    print("maq: Chamada bloqueada")
                elif numero.startswith('800'):
                    print("maq: Chamada verde realizada")
                elif numero.startswith('808'):
                    if saldo < 0.1:
                        print("maq: Saldo insuficiente para chamada azul")
                    else:
                        saldo -= 0.1
                        saldo = converteremdinheiro(l_soma_valores_eur, l_soma_valores_centimos, -0.1)
                        print(f'maq: "saldo = {saldo}"')
                elif numero.startswith('2'):
                    if saldo < 0.25:
                        print(f"maq: Saldo insuficiente para chamada naciona : l{saldo}")
                    else:
                        saldo -= 0.25
                        saldo = converteremdinheiro(l_soma_valores_eur, l_soma_valores_centimos, -0.25)
                        print(f'maq: "saldo = {saldo}"')

                elif numero.startswith('800'):
                    print("maq: Chamada gratuita")

                elif numero.startswith('810'):
                    if saldo < 0.10:
                        print(f"maq: Saldo insuficiente para chamada azul : l{saldo}")
                    else:
                        saldo -= 0.10
                        saldo = converteremdinheiro(l_soma_valores_eur, l_soma_valores_centimos, -0.10)
                        print(f'maq: "saldo = {saldo}"')

                #print(saldo)
                saldo = converter_em_valor(saldo)

            if re_pousar:
                print(f'maq: troco={converter_em_str(saldo)}; Volte sempre!')

        else:
            print("maq: Comando invalido")
            break

if __name__=="__main__":

    parsing()
