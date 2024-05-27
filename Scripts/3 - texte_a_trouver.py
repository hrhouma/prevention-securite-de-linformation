# coding:utf-8
import string
import random
import time

caracteresPossibles = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' &é(-è_çà)=~#{[|\^@]}$*ù!:;,?./%\''

texteATrouver = input("Entrez le texte à découvrir : ")
tentativeCourante = ''.join(random.choice(caracteresPossibles) for c in range(len(texteATrouver)))
tentativeSuivante = ''

termine = False
generation = 0

while termine == False: #tant qu'on n'a pas trouvé le texte, on boucle
    print(tentativeCourante) #affiche la tentative actuelle
    tentativeSuivante = ''   #prépare une variable pour la prochaine tentative
    termine = True #indique par défaut
    for i in range(len(texteATrouver)): 
	#pour chaque caractère du texte à trouver on le compare avec la tentative courante
        if tentativeCourante[i] != texteATrouver[i]: 
            termine = False #s'il ne correspond pas, on passe à la tentative suivante
            tentativeSuivante += random.choice(caracteresPossibles) #choix aléatoire
        else:
            tentativeSuivante += texteATrouver[i] #si on trouve, on garde en mémoire
    generation += 1 #on compte le nombre de générations
    tentativeCourante = tentativeSuivante #on met à jour la tentative courante
    time.sleep(0.1) #on laisse un peu de temps à programme à chaque tour de boucle

print("Texte trouvé ! Cela a demandé " + str(generation) + " génération(s)")
