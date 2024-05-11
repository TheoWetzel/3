print("""
          __________     __      __      ______      ___________
         |____  ____|   |  |    |  |    |   ___|    |  _______  |
             |  |       |  |____|  |    |  |___     | |       | | 
             |  |       |   ____   |    |   ___|    | |       | |
             |  |       |  |    |  |    |  |___     | |_______| |
             |__|       |__|    |__|    |______|    |___________|
                                                                   """)

print("Souhaiter vous vous connecter a notre systeme")

print("1. Se connecter")
print("2. S'inscrire")
print("3. Deconnecter")

choix = int(input("Que souhaiter vous faire : "))

user_list = []
mdp_list = []

def connection():
    Username_verification = input("Mettez votre nom d'utilisateur : ")
    Password_verification = input("Mettez votre mots de passe : ")

def inscription():
    Username_inscription = str(input("Mettez votre nom d'utilisateur : "))
    Password_inscription = input("Mettez votre mots de passe : ")
    Password_inscription2 = input("Re-mettez votre mots de passe : ")

    if Password_inscription != Password_inscription2:
        print("Le mots de passe ne correspondent pas")
    else:
        print("Le mots de passe correspondent bien")

def menu_non_connecter():
    while True:
        if choix == 1:
            connection()

        elif choix == 2:
            inscription()
    
        elif choix == 3:
            print("Vous êtes déconnecter")

menu_non_connecter()