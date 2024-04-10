# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 01:09:06 2023

@author: bogaa
"""

import pickle
import os
import pathlib
from tkinter import messagebox
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    #fonction de la creation de compte
    def createAccount(self):
        self.accNo= int(input(" Entrez le numéro de compte: "))
        self.name = input(" Entrez le nom du titulaire du compte: ")
        self.type = input("Ente le type de compte [C/S] : ")
        self.deposit = int(input("Entrez le montant initial (>=500 pour l’épargne et >=1000 pour l’épargne actuelle"))
        messagebox.showinfo("Account Created")
    
    # fonction pour visualiser les detailles du compte
    def showAccount(self):
        print("Numéro de compte : ",self.accNo)
        print(" Nom du titulaire du compte: ", self.name)
        print("Type de compte",self.type)
        print("Balance: ",self.deposit)
    
    # fonction pour modifier les information du compte
    def modifyAccount(self):
        print("Numéro de compte : ",self.accNo)
        self.name = input(" Modifier le nom du titulaire du compte:")
        self.type = input("Modifier le type de compte :")
        self.deposit = int(input("Modifier l’équilibre :"))
        
         # fonction pour faire un depot
    def depositAmount(self,amount):
        self.deposit += amount
    
    # fonction pour faire un retrait
    def withdrawAmount(self,amount):
        self.deposit -= amount
     
         #fonction pour afficher les ellements du compte
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        messagebox.showinfo("Aucun enregistrement à afficher")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Le solde de votre compte est = ",item.deposit)
                found = True
    else :
        print("Aucun enregistrement à rechercher")
    if not found :
        messagebox.showinfo('Aucun enregistrement existant avec ce numéro')

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input(" Entrez le montant à déposer: "))
                    item.deposit += amount
                    print("Votre compte est mis à jour")
                elif num2 == 2 :
                    amount = int(input("Entrez le montant à retirer : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        messagebox.showinfo('Vous ne pouvez pas retirer un montant plus important')
                
    else :
        messagebox.showinfo('Aucun enregistrement à rechercher')
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Entrez le nom du titulaire du compte : ")
                item.type = input("Entrez le type de compte: ")
                item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# commencement du programme
ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("\tMENU PRINCIPAL")
    print("\t1. NOUVEAU COMPTE")
    print("\t2.MONTANT DU DÉPÔT ")
    print("\t3.MONTANT DU RETRAIT")
    print("\t4.DEMANDE DE SOLDE ")
    print("\t5. LISTE DE TOUS LES TITULAIRES DE COMPTES")
    print("\t6.FERMER UN COMPTE ")
    print("\t7.MODIFIER UN COMPTE ")
    print("\t8.SORTIE ")
    print("\tSélectionnez votre option (1-8) ")
    ch = input()
    #system("cls");
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEntrez le numéro de compte. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEntrez le numéro de compte. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEntrez le numéro de compte. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEntrez le numéro de compte. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEntrez le numéro de compte. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tMerci d'utiliser le système de gestion bancaire")
        break
    else :
        print("Choix invalide")
    
    ch = input("Entrez votre choix : ")
    


    
    
    
    
    
    
    
    
    
    