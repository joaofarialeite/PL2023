from Paciente import Paciente
from tabulate import tabulate
from prettytable import PrettyTable
import matplotlib.pyplot as plt
#plt.switch_backend('agg')


class Catalogo:
    def __init__(self,csv):
        self.pacientes = []
        self.parsing(csv)
        self.doenca_por_sexo = {"M": 0, "F": 0}
        self.calcula_doenca_por_sexo()
        self.doenca_por_idade = {}
        self.calcula_doenca_idade()
        self.doenca_por_colestrol = {}
        self.calcula_doenca_por_colesterol()

    def parsing(self, csv):
        with open(csv, 'r', encoding='utf8') as registos:
            next(registos)
            for linha in registos:
                campos = linha.strip().split(',')
                paciente = Paciente(*campos) # para desempacotar os campos
                self.pacientes.append(paciente) # adicionar o paciente a lista

    def calcula_doenca_por_sexo(self):
        for paciente in self.pacientes:
            if paciente.sexo == 'M' and paciente.tem_doenca == 1:
                self.doenca_por_sexo[paciente.sexo] += 1
            elif paciente.sexo == 'F' and paciente.tem_doenca == 1:
                self.doenca_por_sexo[paciente.sexo] += 1

    def max_idade(self):
        max_idade = 0
        for paciente in self.pacientes:
            if paciente.idade > max_idade:
                max_idade = paciente.idade
        return max_idade

    def calcula_doenca_idade(self):

        max_idade = self.max_idade()

        for idade in range(30, max_idade+1, 5): # mais 1 para incluir o max_idade, 5 porque é onde começa o proximo

            self.doenca_por_idade[f"{idade}-{idade+4}"] = 0


        for paciente in self.pacientes:
            if paciente.tem_doenca and paciente.idade >= 30:
                for faixa_etaria in self.doenca_por_idade:
                    faixa_etaria_inferior, faixa_etaria_superior = map(int, faixa_etaria.split('-'))
                    if faixa_etaria_inferior <= paciente.idade <= faixa_etaria_superior:
                        self.doenca_por_idade[faixa_etaria] += 1
                        break

    def calcula_doenca_por_colesterol(self):

        limites_colesterol = [paciente.colesterol for paciente in self.pacientes]

        min_colesterol = min(limites_colesterol)
        max_colesterol = max(limites_colesterol)


        for i in range(min_colesterol, max_colesterol+10, 10): # +10 para contar com o ultimo
            self.doenca_por_colestrol[f"{i}-{i+9}"] = 0

        for paciente in self.pacientes:
            for nivel_colesterol, value in self.doenca_por_colestrol.items():
                colesterol_inferior, colesterol_superior = map(int, nivel_colesterol.split('-'))
                if colesterol_inferior <= paciente.colesterol <= colesterol_superior and paciente.tem_doenca:
                    self.doenca_por_colestrol[nivel_colesterol] += 1
                    break

    #PROMPT

    def mostrar_pacientes(self):
        for paciente in self.pacientes:
            print(f"Idade: {paciente.idade}, Sexo: {paciente.sexo}, Tensão: {paciente.tensao}, Colesterol: {paciente.colesterol}, Batimento: {paciente.batimento}, Tem doença: {'Sim' if paciente.tem_doenca else 'Não'}")

    def mostrar_doencas_por_sexo(self):
        for sexo, doencas in self.doenca_por_sexo.items():
            print(f"Sexo {sexo}: {doencas} com doença")

    def mostrar_doencas_por_idade(self):

        for faixa_etaria, num_pacientes in self.doenca_por_idade.items():
            print(f"Faixa etária {faixa_etaria}: {num_pacientes} com doença")

    def mostrar_doencas_por_colesterol(self):

        for nivel_de_colesterol, num_pacientes in self.doenca_por_colestrol.items():
            print(f"Nivel de colesterol {nivel_de_colesterol}: {num_pacientes} com doenca")

    #TABELAS

    def mostrar_doencas_por_sexo_tabela(self):
        table = PrettyTable()
        table.field_names = ["Sexo", "Doenças"]

        for sexo, doencas in self.doenca_por_sexo.items():
            table.add_row([sexo, doencas])

        print(table)

    def mostrar_doencas_por_idade_tabela(self):
        headers = ["Faixa Etária", "Número de Doenças"]
        table = []

        for faixa_etaria, num_pacientes in self.doenca_por_idade.items():
            table.append([faixa_etaria, num_pacientes])

        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        #print(tabulate(tabela, headers=["Faixa Etária", "Número de Pacientes com Doença"], tablefmt="fancy_grid"))

    def mostrar_doencas_por_colesterol_tabela(self):
        
        tabela = PrettyTable()
        tabela.field_names = ["Nível de Colesterol", "Número de Pacientes"]

        for nivel_de_colesterol, num_pacientes in self.doenca_por_colestrol.items():
            tabela.add_row([nivel_de_colesterol, num_pacientes])

        print(tabela)

    # GRAFICOS

    def mostrar_doencas_por_sexo_grafico(self):
        
        sexos = list(self.doenca_por_sexo.keys())
        num_doencas_por_sexo = list(self.doenca_por_sexo.values())

        plt.bar(sexos, num_doencas_por_sexo)
        plt.title("Distribuição de Doenças por Sexo")
        plt.xlabel("Sexo")
        plt.ylabel("Número de Pacientes com Doença")

        plt.show()
        
    def mostrar_doencas_por_idade_grafico(self):
            
        grupo_etario = list(self.doenca_por_idade.keys())
        num_pacientes_por_grupo_etario = list(self.doenca_por_idade.values())

        plt.bar(grupo_etario, num_pacientes_por_grupo_etario)
        plt.title("Distribuição de Doenças por Grupo Etário")
        plt.xlabel("Grupo Etário")
        plt.ylabel("Número de Pacientes com Doença")

        plt.show()
        
    def mostrar_doencas_por_colesterol_grafico(self):

        niveis_colesterol = list(self.doenca_por_colestrol.keys())
        num_pacientes_por_nivel = list(self.doenca_por_colestrol.values())

        plt.bar(niveis_colesterol, num_pacientes_por_nivel)
        plt.title("Distribuição de Pacientes por Nível de Colesterol")
        plt.xlabel("Nível de Colesterol")
        plt.ylabel("Número de Pacientes com Doença")

        plt.show()

