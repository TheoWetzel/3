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

user_list = ["theo",]
mdp_list = ["ok",]

if nbr == 1:
    Username_verification = input("Mettez votre nom d'utilisateur : ")
    Password_verification = input("Mettez votre mots de passe : ")
    if Username_verification != user_list:
        print("votre nom d'utilisateur ou votre mots de passe est incorrecte")
    elif Password_verification != mdp_list:
        print("votre nom d'utilisateur ou votre mots de passe est incorrecte")
    else:
        print("vous etes connecter")
elif nbr == 2:
    Username_inscription = str(input("mettez votre nom d'utilisateur : "))
    Password_inscription = input("mettez votre mots de passe : ")
    Password_inscription2 = input("re mettez votre mots de passe : ")
    if Password_inscription : # mettre une retestriction pour eviter qu'il y a rien
        pass
    elif Username_inscription : # mettre une restriction pour eviter qu'il y a rien
        pass
    elif Password_inscription != Password_inscription2:
        print("Les mots de passe ne correspondent pas")
    else:
        print("Les mots de passe correspondent bien")
        user_list.append(Username_inscription)
        mdp_list.append(Password_inscription2)
elif nbr == 3:
    print("vous vous deconnecter de nos services")
    exit