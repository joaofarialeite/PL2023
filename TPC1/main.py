from Catalogo import Catalogo

def main():

    ctg =  Catalogo("myheart.csv")
    # ctg.mostrar_pacientes()
    # ctg.mostrar_doencas_por_sexo()
    # ctg.mostrar_doencas_por_idade()
    # ctg.mostrar_doencas_por_colesterol()
    ctg.mostrar_doencas_por_sexo_tabela()
    ctg.mostrar_doencas_por_idade_tabela()
    ctg.mostrar_doencas_por_colesterol_tabela()
    # ctg.mostrar_doencas_por_sexo_grafico()
    # ctg.mostrar_doencas_por_idade_grafico()
    # ctg.mostrar_doencas_por_colesterol_grafico()

if __name__ == "__main__":
    main()

