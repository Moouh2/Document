# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# ___Programme en mode console___
# nom = "tata" # variable qu'on affecte une valeur
# print(nom) # fonction qui affiche une valeur de sortie
# print("Hello World! " + nom) # concatenation
# print("Hello " + nom)
# print()

# __Demande des données à l'utilisateur__
# input est une fonction d'entrée
# nom2 = input("quel est ton nom?")
# print("je m'appelle" + nom2)

# Exercice
# nom3 = input("quel est votre nom ? ")
# ages = input("quel est votre age ? ")
# print("vous vous appelez " + nom3 + ", vous avez " + ages +" ans")

# ___Variable numérique___
# on a changé le type numérique en chaine de caractère str(ages)
#nom = "Tata"
#ages = 27
#print(type(nom))
#print(type(ages))
#print("Vous vous appelez " + nom + ", vous avez " + str(ages) + " ans.")

#__Convertir une chaine en entier
#nom = input("quel est votre nom ? ")
#age = input("quel est votre age ? ")
# str->int
#age_prochain = int(age) + 1
#print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
#print("l'an prochain vous aurez " + str(age_prochain) + " ans.")

# ___Erreurs et gestion des exceptions___
#nom = input("quel est votre nom ? ")
#age = input("quel est votre age ? ")

# try: c'est essayer
#try:
 #   age_prochain = int(age) + 1
#except:
   # print("ERREUR: Vous devez rentrer un nombre pour l'age ")
#else:
    #print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    #print("l'an prochain vous aurez " + str(age_prochain) + " ans.")

#La boucle while
nom = input("quel est votre nom ? ")
age = input("quel est votre age ? ")

try:
    age_prochain = int(age) + 1
except:
    print("ERREUR: Vous devez rentrer un nombre pour l'age ")
else:
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    print("l'an prochain vous aurez " + str(age_prochain) + " ans.")

