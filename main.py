print("""
          __________     __      __      ______      ___________
         |____  ____|   |  |    |  |    |   ___|    |  _______  |
             |  |       |  |____|  |    |  |___     | |       | | 
             |  |       |   ____   |    |   ___|    | |       | |
             |  |       |  |    |  |    |  |___     | |_______| |
             |__|       |__|    |__|    |______|    |___________|
                                                                   """)

print("Souhaitez-vous vous connecter à notre systême")

print("1. Se connecter")
print("2. S'inscrire")
print("3. Déconnecté")

user_list = []
mdp_list = []

choix = int(input("Que souhaiter vous faire : "))

def connection():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    if username not in user_list:
        print("Votre nom d'utilisateur ou votre mot de passe est incorrect")
    elif password not in mdp_list:
        print("Votre nom d'utilisateur ou votre mot de passe est incorrect")
    else:
        print("Vous êtes connecté")

def inscription():
    username = str(input("Mettez votre nom d'utilisateur : "))
    password = input("Mettez votre mots de passe : ")
    password2 = input("Re-mettez votre mots de passe : ")

    if password != password2:
        print("Les mots de passe ne correspondent pas")

    else:
        print("Les mots de passe correspondent bien")
        user_list.append("ffg")
        mdp_list.append("1234")
        
def menu_non_connecter():
        if choix == 1:
            connection()

        elif choix == 2:
            inscription()

        elif choix == 3:
            print("Vous êtes déconnecté !")

menu_non_connecter()