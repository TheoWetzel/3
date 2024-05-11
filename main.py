print("""
          __________     __      __      ______      ___________
         |____  ____|   |  |    |  |    |   ___|    |  _______  |
             |  |       |  |____|  |    |  |___     | |       | | 
             |  |       |   ____   |    |   ___|    | |       | |
             |  |       |  |    |  |    |  |___     | |_______| |
             |__|       |__|    |__|    |______|    |___________|
                                                                   """)

print("souhaiter vous vous connecter a notre systeme")

print("1. se connecter")
print("2. s'inscrire")
print("3. deconnecter")

nbr = int(input("que souhaiter vous faire : "))

user_list = []
mdp_list = []

def connection():
    Username_verification = input("Mettez votre nom d'utilisateur : ")
    Password_verification = input("Mettez votre mots de passe : ")
def inscription():
    Username_inscription = str(input("mettez votre nom d'utilisateur : "))
    Password_inscription = input("mettez votre mots de passe : ")
    Password_inscription2 = input("re-mettez votre mots de passe : ")

    if Password_inscription != Password_inscription2:
        print("Le mots de passe ne correspondent pas")
    else:
        print("Le mots de passe correspondent bien")

if nbr == 1:
    connection()
elif nbr == 2:
    inscription()
elif nbr == 3:
    print("vous êtes déconnecter")