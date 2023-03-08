import json
import re
from collections import Counter


def frequencia_processos_por_ano(ficheiro):

    frequencias = {}
    ano_regex = re.compile(r'^\d+::(?P<ano>\d{4})-')

    with open(ficheiro, 'r') as f:
        for registro in f:
            match = ano_regex.match(registro)
            if match:
                ano = match.group('ano')
                if ano in frequencias:
                    frequencias[ano] += 1
                else:
                    frequencias[ano] = 1

    for ano, freq_processos in frequencias.items():

        print(f"Ano {ano}: {freq_processos} processos")


def frequencia_nomes_e_apelidos_por_seculo(ficheiro):

    nome_regex = re.compile(r'^\d+::(?P<ano>\d{4})-\d{2}-\d{2}::(?P<nome>.+?) (?P<apelido>\S+)(::.*)?$')
    nomes_por_seculo = {'XIX': Counter(), 'XX': Counter(), 'XXI': Counter()}

    with open(ficheiro, 'r') as f:
        for linha in f:
            match = nome_regex.match(linha)
            if match:
                nome = match.group('nome')
                apelido = match.group('apelido')
                ano = int(match.group('ano'))
                seculo = 'XIX' if ano < 1900 else ('XXI' if ano >= 2000 else 'XX')
                nomes_por_seculo[seculo][f'{nome} {apelido}'] += 1

    for seculo, nomes in nomes_por_seculo.items():
        print(f"--- Século {seculo} ---")
        nomes_mais_frequentes = nomes.most_common(5)
        for nome, frequencia in nomes_mais_frequentes:
            print(f"{nome}: {frequencia} ocorrências")
        print()


def frequencia_relacoes(ficheiro):

    relacao_regex = re.compile(r'Tio Paterno|Tio Materno|Tia Materna|Tia Paterna|Primo|Filho|Filha|Pai|Mãe|Avô Materna|Avó Paterna|Avô Materno|Avó Paterno|Neto|Neta|Genro|Nora|Cunhado|Cunhada|Enteado|Amigo|Sobrinho|Sobrinha')
    relacoes = []

    with open(ficheiro, 'r') as f:
        for linha in f:
            relacao_match = relacao_regex.search(linha)
            if relacao_match:
                relacao = relacao_match.group()
                relacoes.append(relacao)

    print(Counter(relacoes))


def registos_to_json(ficheiro, output_file):

    registro_regex = re.compile(r'^(?P<Processo>\d+)::(?P<data_nascimento>\d{4}-\d{2}-\d{2})::(?P<Nome>\w+\s*\w*\s*\w*)::(?P<Pai>\w+\s*\w*\s*\w*)::(?P<Mae>\w+\s*\w*\s*\w*)(::(?P<Observacoes>.+))?')
    processados = []
    contador = 0

    with open(ficheiro, 'r') as f:
        for registro in f:
            match = registro_regex.match(registro)
            if match:
                contador += 1
                dicionario = {
                    'Processo': int(match.group('Processo')),
                    'data_nascimento': match.group('data_nascimento'),
                    'Nome': match.group('Nome').strip(),
                    'Pai': match.group('Pai').strip(),
                    'Mae': match.group('Mae').strip(),
                    'Observações': match.group('Observacoes').strip() if match.group('Observacoes') else None
                }
                processados.append(dicionario)
            if contador == 20:
                break

    #print(processados)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processados, f, indent=2, ensure_ascii=False)



if __name__ == '__main__':

    frequencia_processos_por_ano('processos.txt')

    #frequencia_nomes_e_apelidos_por_seculo('processos.txt')

    #frequencia_relacoes('processos.txt')

    #registos_to_json('processos.txt','test.json')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
