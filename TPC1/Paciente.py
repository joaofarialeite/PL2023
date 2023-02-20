class Paciente:
    def __init__(self, idade, sexo, tensao, colesterol, batimento, tem_doenca):
        self.idade = int(idade)
        self.sexo = sexo[0]
        self.tensao = int(tensao)
        self.colesterol = int(colesterol)
        self.batimento = int(batimento)
        self.tem_doenca = bool(tem_doenca)



