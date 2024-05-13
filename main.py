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

choix = int(input("Que souhaiter vous faire : "))

def folder_data():
    data_user = open("data.txt", "a+")


def connection():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    if username not in folder_data.data_user:
        print("Votre nom d'utilisateur ou votre mot de passe est incorrect")
    elif password not in folder_data.data_user:
        print("Votre nom d'utilisateur ou votre mot de passe est incorrect")
    else:
        print("Vous êtes connecté")

def inscription():
    username = str(input("Mettez votre nom d'utilisateur : "))
    password = input("Mettez votre mots de passe : ")
    password2 = input("Re-mettez votre mots de passe : ")

    if password != password2:
        print("Les mots de passe ne correspondent pas")

    elif username in folder_data.data_user:
        try:
            retry_username = str(username)
        except ValueError:
            print("Nom d'utilisateur deja pris !")
        print(retry_username)


    else:
        print("Les mots de passe correspondent bien")
        folder_data.data_user.write(username)
        folder_data.data_user.write(password)
        for line in folder_data.data_user:
            line.split.str(folder_data.data_user.write('\n' + password))


def menu_connecter():
    if choix == 1:
        print("Pas encore disponible !")
    elif choix == 2:
        print("Pas encore disponible !")
    elif choix == 3:
        print("Pas encore disponible !")
        
def menu_non_connecter():
        if choix == 1:
            connection()
            menu_connecter()
            folder_data.data_user.close()

        elif choix == 2:
            inscription()
            folder_data.data_user.close()

        elif choix == 3:
            print("Vous êtes déconnecté !")
            folder_data.data_user.close()

menu_non_connecter()