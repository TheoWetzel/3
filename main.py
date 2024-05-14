print("""
          __________     __      __      ______      ___________
         |____  ____|   |  |    |  |    |   ___|    |  _______  |
             |  |       |  |____|  |    |  |___     | |       | | 
             |  |       |   ____   |    |   ___|    | |       | |
             |  |       |  |    |  |    |  |___     | |_______| |
             |__|       |__|    |__|    |______|    |___________|
                                                                   """)

print("Souhaitez-vous vous connecter à notre systême ?")

print("1. Se connecter")
print("2. S'inscrire")
print("3. Déconnecté")

data_user = open("data.txt", "a+")

def choix():
    choix = int(input("Que souhaiter vous faire : "))
    if choix is 'str()':
        print("Veulliez mettre un nombre !")
        choix = input("Que souhaiter vous faire : ")

choix()

class ConnectionData:

    def connection_input():
        username = str(input("Nom d'utilisateur : "))
        password = input("Mot de passe : ")

    def username_check():
        if ConnectionData.connection_input.username not in data_user:
            print("Votre nom d'utilisateur ou votre mot de passe est incorrect !")

    def password_check():
        if ConnectionData.connection_input.password not in data_user:
            print("Votre nom d'utilisateur ou votre mot de passe est incorrect !")

    def connection():        
        if ConnectionData.username_check == True + ConnectionData.password_check == True:
            print("Vous êtes connecté !")

class InscriptionData:

    def inscription_input():
        username = str(input("Mettez votre nom d'utilisateur : "))
        password = input("Mettez votre mots de passe : ")
        password2 = input("Re-mettez votre mots de passe : ")
    
    def password_check():
        if InscriptionData.inscription_input.password != InscriptionData.inscription_input.password2: # Password check
            wrong_password = print("Les mots de passe ne correspondent pas !")
        else:
            print("Les mots de passe correspondent bien !")

    def username_check():
        if InscriptionData.inscription_input.username in data_user:
            username_unavailable = print("Nom d'utilisateur indisponible !")
        else:
            print("Nom d'urilisateur disponible !")

    def inscription():
        InscriptionData.inscription_input()
        if InscriptionData.username_check == False:
            print(InscriptionData.username_check.username_unavailable)
        elif InscriptionData.password_check == False:
            print(InscriptionData.password_check.wrong_password)
        else:
            print("compte crée")
            data_user.write(InscriptionData.inscription_input.username)
            data_user.write('\n' + InscriptionData.inscription_input.password)

class Menu:

    def menu_connecter():
        if choix == 1:
            print("Pas encore disponible !")
        elif choix == 2:
            print("Pas encore disponible !")
        elif choix == 3:
            print("Pas encore disponible !")
        
    def menu_non_connecter():
            if choix == 1:
                ConnectionData.connection()

            elif choix == 2:
                InscriptionData.inscription()

            elif choix == 3:
                print("Vous êtes déconnecté !")
                data_user.close()
                
    menu_non_connecter()