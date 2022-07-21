#-------------------------------------------------------------------------------
# Name:        Delivery de Supermercado
# Purpose:     Programa para simular uma app de delivery de supermercado
#
# Author:      GUSTAVO EVANGELISTA
#
# Copyright:   (c) GUSTAVO 2022
#-------------------------------------------------------------------------------

# -*- coding: UTF-8 -*-
import time
from datetime import datetime
import os
import produtos
import math

os.system("color F2") #letra com cor verde e fundo branco

lista_de_compras = []
quant_produtos = 0
valor_total = 0


def Produtos_disponiveis():  #imprime a lista de produtos disponíveis
    print("Lista de produtos disponíveis: \n")
    produtos.lista_de_produtos()


def comprar():   #funçao que cria a sua lista de compras
    Produtos_disponiveis()

    continuar = "sim"
    global quant_produtos

    while (continuar == "sim"):
        lista_de_compras.append(input("\nO que deseja inserir na sua lista de compras? "))
        quant_produtos = quant_produtos + 1    #conta a quantidade de produtos

        continuar = input("Deseja comprar mais algum produto? (sim | nao) ")


        if continuar == "sim":
            continue
        else:
            break

    print("\nSua lista de compras ficou assim: ")
    for i in range(0,len(lista_de_compras)):
        print("\t",lista_de_compras[i])


def alterar_pedido(): #funçao para adicionar ou remover produtos da sua lista de compras

    if (lista_de_compras == []):
        print ("Seu cesto ainda está vazio. Por favor, vá às compras :)")

    else:
        print("Esta é sua lista de compras no momento: ")
        for i in range(0,len(lista_de_compras)):
            print("\t",lista_de_compras[i])

        selecao = int(input("Deseja adicionar (insira o numero 1) ou remover (insira o numero 2) um produto? "))

        global quant_produtos


        if selecao == 1:
            Produtos_disponiveis()

            continuar = "sim"

            while (continuar == "sim"):
                lista_de_compras.append(input("\nO que deseja inserir na sua lista de compras? "))

                quant_produtos = quant_produtos + 1

                continuar = input("Deseja adicionar mais um produto? ")

                if continuar == "sim":
                    continue
                else:
                    break

            print("Sua lista de compras ficou assim: ")
            for i in range(0,len(lista_de_compras)):
                print("\t",lista_de_compras[i])

        elif (selecao == 2):
            print("Esta é sua lista de compras no momento: ")
            for i in range(0,len(lista_de_compras)):
                print("\t",lista_de_compras[i])

            continuar = "sim"
            while (continuar == "sim"):
                lista_de_compras.remove(input("\nO que deseja remover da sua lista de compras? "))
                quant_produtos = quant_produtos - 1

                continuar = input("Deseja remover mais um produto? ")

                if continuar == "sim":
                    continue
                else:
                    break

            print("Sua lista de compras ficou assim: ")
            for i in range(0,len(lista_de_compras)):
                print("\t",lista_de_compras[i])


def checkout(): #funçao para apresentar um resumo da sua compra
    global valor_total

    if (lista_de_compras == []):
        print("Ainda não fez nenhuma compra...")

    else:

        print("\nResumo da compra:")
        for i in range(0,len(lista_de_compras)):
            print("\t",lista_de_compras[i])

            if produtos.preco_limpeza[lista_de_compras[i]] != False: #associa cada item da lista de compra ao dicionario de precos da biblioteca produtos
                valor_total = valor_total + produtos.preco_limpeza[lista_de_compras[i]]

            if produtos.preco_congelados[lista_de_compras[i]] != False: #associa cada item da lista de compra ao dicionario de precos da biblioteca produtos
                valor_total = valor_total + produtos.preco_congelados[lista_de_compras[i]]

            if produtos.preco_chacurtaria[lista_de_compras[i]] != False: #associa cada item da lista de compra ao dicionario de precos da biblioteca produtos
                valor_total = valor_total + produtos.preco_chacurtaria[lista_de_compras[i]]

            if produtos.preco_talho[lista_de_compras[i]] != False: #associa cada item da lista de compra ao dicionario de precos da biblioteca produtos
                valor_total = valor_total + produtos.preco_talho[lista_de_compras[i]]

        print("\nE este é o nosso preçário:")
        produtos.precario()

        print ("\nQuantidade de produtos na lista de compras: ",quant_produtos)
        print("Valor total da compra: ", valor_total, "€")
        print("Horário da compra: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def contactos(): # funçao par apresentar os contactos do supermercado
    print("Telefone: 282 000 00")
    print("E-mail: superlagos@gmail.com")
    print("Morada: Estrada de Lagos, nº2000, 8600 ,Lagos, Faro, Portugal")


def menu(): # menu de opçoes
    print("1- Comprar")
    print("2- Alterar pedido")
    print("3- Checkout")
    print("4- Contactos")
    print("5- Sair")
    global opcao
    global quant_produtos
    opcao = int(input("Introduza a sua opção: "))


print("-----SUPER LAGOS-----\n") #inicio do programa
print("Bem-vindo :) ")
print("Já iremos apresentar o menu de opções...")
time.sleep(1)

while True: #fica em ciclo até o utilizador inserir a opçao de sair
    print("\n------Menu de opções------")

    menu()

    if opcao == 1:
        print("")
        comprar()


    elif opcao == 2:
        print("")
        alterar_pedido()


    elif opcao == 3:
        print("")
        checkout()
        morada = str(input("\nInsira a morada de entrega: "))
        print("\nSua compra será enviada para a morada inserida. Obrigado pela preferência! Adeus!")
        break


    elif opcao == 4:
        print("")
        contactos()

    elif opcao == 5:
        print("")
        print("O programa vai encerrar... Adeus!")
        break

    else:
        print("Opcao invalida, volte a tentar...")

    print("")
