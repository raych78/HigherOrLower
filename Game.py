from propositions_dictionary import propositions
import random 
import pyfiglet



end_game = True
score = 0

#Continuer tant que c’est pas faux
#Avec une while boucle
while end_game == True : 
    #Assigner pour chaque phrase la variable A et B 
    #Utilisation du dictionnaire python dans le fichier "propositions_dictionary"
    A, value_A = random.choice(list(propositions.items()))
    B, value_B = random.choice(list(propositions.items()))

    if A == B :
        B, value_B = random.choice(list(propositions.items()))

   
    #Mettre deux propositions aléatoire
    #Avec random faire apparaître deux propositions 
    ascii_banner = pyfiglet.figlet_format("Higer or Lower")
    print(ascii_banner)


    print(" Who's animal has killed most humans in 2022? \n \n")
    print(f"Compare A: {A} \n ")

    #VS in asci
    ascii_vs = pyfiglet.figlet_format("VS")
    print(ascii_vs)

    print(f"Against B: {B}\n")

    #Pouvoir choisir la proposition qui a le plus de follower
    #Utiliser Input pour choisir A ou B 
    choice = input("Enter A or B:  ")

    #Vérifier si c’est vrai ou faux
    #si A < ou > B alors ajouter un point ou affichage du score et fin du jeu 
    if choice.upper() == "A" or choice.upper() == "B":
        if choice == "A" :
            if value_A > value_B:
                print("Exact")
                score += 1
            else : 
                print("Wrong answer")
                end_game = False
                 #Print score in ascci text 
                ascii_score = pyfiglet.figlet_format(f"Final score : {score}")
                print(ascii_score)

        if choice == "B" : 
            if value_B > value_A:
                print("Exact")
                score += 1 
            else : 
                print("Wrong answer")
                end_game = False
                #Print score in ascci text 
                ascii_score = pyfiglet.figlet_format(f"Final score : {score}")
                print(ascii_score)
            
        print("Invalid input. Please try again.")


    

