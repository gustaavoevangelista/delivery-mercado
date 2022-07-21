def lista_de_produtos():
    limpeza = ["Detergente", "Lixívia", "Sabão em Pó", "Vanish"] #vetor
    congelados = ["Batata Frita", "Nuggets", "Pizza", "Lasanha de Espinafre"] #lista
    chacurtaria = "Queijo Terra Nostra", "Fiambre", "Bacon" #tupla
    talho = ["Bife da Vazia", "Peito de Frango","Cachaço"] #lista


    print("Secção de limpeza: ")
    for i in range(0,len(limpeza)):
        print("\t",limpeza[i])

    print("\nSecção de congelados: ")
    for i in range(0,len(congelados)):
        print("\t",congelados[i])

    print("\nSecção de chacurtaria: ")
    for i in range(0,len(chacurtaria)):
        print("\t",chacurtaria[i])

    print("\nSecção do talho: ")
    for i in range(0,len(talho)):
        print("\t",talho[i])


#dicionario
preco_limpeza = {"Detergente": 1, "Lixívia": 2.5, "Sabão em Pó": 10, "Vanish": 7.99}
preco_congelados = {"Batata Frita": 2.99, "Nuggets": 3.49, "Pizza": 1.99, "Lasanha de Espinafre": 3.99}
preco_chacurtaria = {"Queijo Terra Nostra": 7.99, "Fiambre": 12, "Bacon":3.99}
preco_talho = {"Bife da Vazia": 14, "Peito de Frango": 5,"Cachaço": 6}


def precario():
    for i in preco_limpeza:
        print("\t",i , "->",preco_limpeza[i],"€")


    for i in preco_congelados:
        print("\t",i , "->",preco_congelados[i],"€")


    for i in preco_chacurtaria:
        print("\t",i , "->",preco_chacurtaria[i],"€")


    for i in preco_talho:
        print("\t",i , "->",preco_talho[i],"€")

