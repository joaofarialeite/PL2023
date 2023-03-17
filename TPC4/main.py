import json
import re


def pergunta0(ficheiro):

    er_cabecalho = re.compile(r'(?P<numero>\w*),(?P<nome>\w*),(?P<curso>\w*)')
    er1 = re.compile(r'^(?P<numero>\d*),(?P<nome>(\w|\s)*),(?P<curso>(\w|\s)*)$')


    with open(ficheiro, 'r', encoding='utf-8') as f:
        for registo in f:

            if er_cabecalho.search(registo):
                print(er_cabecalho.search(registo).group())

            if er1.search(registo):
                print(er1.search(registo).group().strip())


def pergunta1(ficheiro):

    #er_cabecalho = re.compile(r'(?P<numero>\w*),(?P<nome>\w*),(?P<curso>\w*),((?P<notas_simples>\w*)|(?P<notas_simples1>\w*{(?P<quantidade>\d*)}))')
    er_cabecalho = re.compile(
        r'^(?P<numero>(Número)),(?P<nome>\w*),(?P<curso>\w*)(,(?P<notas_simples>\w*)({(?P<quantidade>(\d*|(\d*,\d*)))})?)?')
    er1 = re.compile(r'^(?P<numero>\d+),(?P<nome>(\w|\s)*),(?P<curso>(\w|\s)*)(,(?P<quantidade>(\d|,)*))?$')

    lista_dic=[]

    quantidade_registos = 0

    with open(ficheiro, 'r', encoding='utf-8') as f:
        for registo in f:

            registo = registo.strip()
            res =  er1.search(registo)

            if er_cabecalho.search(registo):
                quantidade_registos = er_cabecalho.search(registo).group('quantidade')
                print(quantidade_registos)

            if res:

                if er1.search(registo).group('quantidade'):
                    resultado = er1.search(registo).group('quantidade').split(',')
                    print(resultado,len(list(filter(bool,resultado))))


                    if len(list(filter(bool,resultado))) == int(quantidade_registos):
                        res_dic = {key: value for key, value in er1.search(registo).groupdict().items() if value is not None}
                        res_dic['quantidade'] = str([int(x) for x in list(filter(bool,resultado))]).replace(' ','')
                        lista_dic.append(res_dic)

    with open('pergunta1.json', 'w', encoding='utf-8') as f:
        json.dump(lista_dic, f, indent=2, ensure_ascii=False)


def pergunta2(ficheiro):

    #er_cabecalho = re.compile(r'(?P<numero>\w*),(?P<nome>\w*),(?P<curso>\w*),((?P<notas_simples>\w*)|(?P<notas_simples1>\w*{(?P<quantidade>\d*)}))')
    er_cabecalho = re.compile(
        r'^(?P<numero>(Número)),(?P<nome>\w*),(?P<curso>\w*)(,(?P<notas_simples>\w*)({(?P<quantidade>(\d*|(\d*,\d*)))})?)?')
    er1 = re.compile(r'^(?P<numero>\d+),(?P<nome>(\w|\s)*),(?P<curso>(\w|\s)*)(,(?P<quantidade>(\d|,)*))?$')

    lista_dic=[]

    quantidade_registos = 0

    with open(ficheiro, 'r', encoding='utf-8') as f:
        for registo in f:

            registo = registo.strip()
            res =  er1.search(registo)

            if er_cabecalho.search(registo):
                quantidade_registos = er_cabecalho.search(registo).group('quantidade')
                nr_quantidade_registos = len(quantidade_registos.split(','))

                if nr_quantidade_registos == 2:
                    lista_nr_quantidade_registos = quantidade_registos.split(',')
                    min = lista_nr_quantidade_registos[0]
                    max = lista_nr_quantidade_registos[1]

            if res:
                if er1.search(registo).group('quantidade'):
                    resultado = er1.search(registo).group('quantidade').split(',')
                    #print(resultado,len(list(filter(bool,resultado))))

                    #print(len(list(filter(bool,resultado))), int(max),int(min))

                    if nr_quantidade_registos == 1 and len(list(filter(bool,resultado))) == int(quantidade_registos):
                        res_dic = {key: value for key, value in er1.search(registo).groupdict().items() if value is not None}
                        res_dic['quantidade'] = str([int(x) for x in list(filter(bool,resultado))]).replace(' ','')
                        lista_dic.append(res_dic)

                    if (len(list(filter(bool,resultado))) <= int(max)) and (int(min) <= len(list(filter(bool,resultado)))) and nr_quantidade_registos == 2:

                        res_dic = {key: value for key, value in er1.search(registo).groupdict().items() if value is not None}
                        res_dic['quantidade'] = str([int(x) for x in list(filter(bool,resultado))]).replace(' ','')
                        lista_dic.append(res_dic)

    with open('pergunta2.json', 'w', encoding='utf-8') as f:
        json.dump(lista_dic, f, indent=2, ensure_ascii=False)


def pergunta3(ficheiro):

    #er_cabecalho = re.compile(r'(?P<numero>\w*),(?P<nome>\w*),(?P<curso>\w*),((?P<notas_simples>\w*)|(?P<notas_simples1>\w*{(?P<quantidade>\d*)}))')
    er_cabecalho = re.compile(
        r'^(?P<numero>(Número)),(?P<nome>\w*),(?P<curso>\w*)(,(?P<notas_simples>\w*)({(?P<quantidade>(\d*|(\d*,\d*)))})?)?(::((?P<Notas_media>(media))|(?P<Notas_somadas>(sum))))?')
    er1 = re.compile(r'^(?P<numero>\d+),(?P<nome>(\w|\s)*),(?P<curso>(\w|\s)*)(,(?P<quantidade>(\d|,)*))?$')

    lista_dic=[]


    quantidade_registos = 0

    with open(ficheiro, 'r', encoding='utf-8') as f:
        for registo in f:

            registo = registo.strip()
            res =  er1.search(registo)

            if er_cabecalho.search(registo):
                quantidade_registos = er_cabecalho.search(registo).group('quantidade')
                tem_media = False
                tem_soma = False
                tem_algo = False  # inicializa a variável com o valor False

                if er_cabecalho.search(registo).group('Notas_media'):
                    tem_media = True
                    tem_algo = True  # apenas altera o valor de tem_algo se a condição if for satisfeita

                if er_cabecalho.search(registo).group('Notas_somadas'):
                    tem_soma = True
                    tem_algo = True

                nr_quantidade_registos = len(quantidade_registos.split(','))

                if nr_quantidade_registos == 2:
                    lista_nr_quantidade_registos = quantidade_registos.split(',')
                    min = lista_nr_quantidade_registos[0]
                    max = lista_nr_quantidade_registos[1]

            if res:
                if er1.search(registo).group('quantidade'):
                    resultado = er1.search(registo).group('quantidade').split(',')
                    #print(resultado,len(list(filter(bool,resultado))))

                    if tem_algo == False:

                        if nr_quantidade_registos == 1 and len(list(filter(bool,resultado))) == int(quantidade_registos):
                            res_dic = {key: value for key, value in er1.search(registo).groupdict().items() if value is not None}
                            res_dic['quantidade'] = str([int(x) for x in list(filter(bool,resultado))]).replace(' ','')
                            lista_dic.append(res_dic)
                        #o list(filter(bool) elimina os  vazios ou seja que so tem virgula e aparece noa array ''
                        if (len(list(filter(bool,resultado))) <= int(max)) and (int(min) <= len(list(filter(bool,resultado)))) and nr_quantidade_registos == 2:

                            res_dic = {key: value for key, value in er1.search(registo).groupdict().items() if value is not None}
                            res_dic['quantidade'] = str([int(x) for x in list(filter(bool,resultado))]).replace(' ','')
                            lista_dic.append(res_dic)
                    else:
                        res_dic = {key: value for key, value in er1.search(registo).groupdict().items() if
                                   value is not None}

                        if "quantidade" in res_dic and tem_media:

                            res_dic.pop('quantidade')
                            resultado = [int(x) for x in list(filter(bool,resultado))]
                            res_dic['Notas_media'] = sum(resultado) / len(list(filter(bool,resultado)))
                            lista_dic.append(res_dic)

                        if "quantidade" in res_dic and tem_soma:

                            res_dic.pop('quantidade')
                            resultado = [int(x) for x in list(filter(bool, resultado))]
                            res_dic['Notas_somadas'] = sum(resultado)
                            lista_dic.append(res_dic)



    with open('pergunta3.json', 'w', encoding='utf-8') as f:
        json.dump(lista_dic, f, indent=2, ensure_ascii=False)


pergunta3("alunos.csv")