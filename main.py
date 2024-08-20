import discrete_univarie_file as DU
import continue_univarie_file as CU
import discrete_bivarie_file as DB
import continue_bivarie_file as CB
import global_file as glo
import sys

   
def menu_principal():

    choice = -1
    
    while choice:

        glo.clear()
        print(f"\n{'*'*120}\n")
        print('BIENVENUE DANS "EASY-STATISTICS" VOTRE LOGICIEL. AVEC "EASY-STATISTICS"  C\'EST LA STAT FACILE POUR TOUS.')
        print(f"\n{'*'*120}\n")

        print("\nMENU PRINCIPAL\n")
        print('0 : Quitter "EASY-STATISTICS".\n')
        print("1 : Variables discrètes univariées.\n")
        print("2 : Variables continues univariées.\n")
        print("3 : Variables discrètes bivariées.\n")
        print("4 : Variables continues bivariées.\n")

        while choice<0 or choice>4:
            choice = input("\nSaisir le numéro de votre choix:  ")
            choice = glo.new_entry_int2(choice)
            if 0<=choice<=4:
                break
            else:
                print("\nOPTION: 0, 1, 2, 3 ou 4. Tout autre numéro est invalide.")
        match choice:
            case 0: 
                print('\n"EASY-STATISTICS" VOUS DIT AUREVOIR.\n')
                sys.exit()
            case 1: 
                glo.clear()
                case1()  
            case 2: 
                glo.clear()
                case2()
            case 3: 
                glo.clear()
                case3()
            case 4: 
                glo.clear()
                case4()
        choice = -1

def case1():
    matrix = []

    while True:
        choice = -1
        print(f"\n{'*'*80}\n")
        print('BIENVENUE dans le MENU 2: "Variables Discrètes Univariées".')
        print(f"\n{'*'*80}\n")

        print("\nOPTIONS\n")
        print("1 : Afficher le tableau statistique.\n")
        print("2 : Afficher les valeurs centrales.\n")
        print("3 : Afficher les valeurs de dispersion.\n")
        print("4 : Entrer une nouvelle série statistique.\n")
        print("5 : Revenir au Menu Principal.\n")

        while choice<1 or choice>5:
            choice = input("\nSaisir le numéro de votre choix:  ")
            choice = glo.new_entry_int2(choice)
            if 1<=choice<=5:
                break
            else:
                print("\nOPTION: 1, 2, 3, 4 ou 5. Tout autre numéro est invalide.")
        match choice:
            case 1: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DU.enter_matrix()
                DU.print_statistical_table(matrix)  

            case 2: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DU.enter_matrix()
                DU.print_central_values(matrix)  
            case 3: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DU.enter_matrix()
                DU.print_dispersion_values(matrix)  
            case 4: 
                glo.clear()
                matrix = []
                print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                matrix = DU.enter_matrix()
            case 5:
                break
                matrix = []
                glo.clear()
                menu_principal()


def case2():
    matrix = []

    while True:
        choice = -1
        print(f"\n{'*'*80}\n")
        print('BIENVENUE dans le MENU 3: "Variables Continues Univariées".')
        print(f"\n{'*'*80}\n")

        print("\nOPTIONS\n")
        print("1 : Afficher le tableau statistique.\n")
        print("2 : Afficher les valeurs centrales.\n")
        print("3 : Afficher les valeurs de dispersion.\n")
        print("4 : Entrer une nouvelle série statistique.\n")
        print("5 : Revenir au Menu Principal.\n")

        while choice<1 or choice>5:
            choice = input("\nSaisir le numéro de votre choix:  ")
            choice = glo.new_entry_int2(choice)
            if 1<=choice<=5:
                break
            else:
                print("\nOPTION: 1, 2, 3, 4, ou 5. Tout autre numéro est invalide.")
        match choice:
            case 1: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CU.enter_matrix()
                CU.print_statistical_table(matrix)  
            case 2: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CU.enter_matrix()
                CU.print_central_values(matrix)  
            case 3: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CU.enter_matrix()
                CU.print_dispersion_values(matrix)  
            case 4: 
                glo.clear()
                matrix = []
                print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                matrix = CU.enter_matrix()
            case 5:
                break
                matrix = []
                glo.clear()
                menu_principal()
        choice = -1

def case3():
    matrix = []

    while True:
        choice = -1
        print(f"\n{'*'*80}\n")
        print('BIENVENUE dans le MENU 4: "Variables Discrètes Bivariées".')
        print(f"\n{'*'*80}\n")

        print("\nOPTIONS\n")
        print("1 : Afficher les Moyennes des variables.\n")
        print("2 : Afficher la Variance et l'Ecart-type.\n")
        print("3 : Afficher la Covariance.\n")
        print("4 : Afficher la Droite de Correlation.\n")
        print("5 : Afficher le Coefficient de correlation et conclure.\n")
        print("6 : Entrer une nouvelle série statistique.\n")
        print("7 : Revenir au Menu Principal.\n")


        while choice<1 or choice>7:
            choice = input("\nSaisir le numéro de votre choix:  ")
            choice = glo.new_entry_int2(choice)
            if 1<=choice<=7:
                break
            else:
                print("\nOPTION: 1, 2, 3, 4, 5, 6 ou 7. Tout autre numéro est invalide.")
        match choice: 
            case 1: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DB.enter_matrix()
                DB.print_mean(matrix)
            case 2: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DB.enter_matrix()
                DB.print_variance_ecart(matrix) 
            case 3:
                glo.clear() 
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DB.enter_matrix()
                DB.print_covariance(matrix)  
            case 4: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DB.enter_matrix()
                DB.print_droite(matrix)  
            case 5: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = DB.enter_matrix()
                DB.print_coefficient(matrix)  
            case 6: 
                glo.clear()
                matrix = []
                print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                matrix = DB.enter_matrix()
            case 7:
                break
                matrix = []
                glo.clear()
                menu_principal()

def case4():
    matrix = []

    while True:
        choice = -1
        print(f"\n{'*'*80}\n")
        print('BIENVENUE dans le MENU 5: "Variables Continues Bivariées".')
        print(f"\n{'*'*80}\n")

        print("\nOPTIONS\n")
        print("1 : Afficher les Distributions Marginales.\n")
        print("2 : Afficher les Moyennes Marginales.\n")
        print("3 : Afficher la Covariance.\n")
        print("4 : Afficher la Droite de Regression.\n")
        print("5 : Entrer une nouvelle série statistique.\n")
        print("6 : Revenir au Menu Principal.\n")


        while choice<1 or choice>6:
            choice = input("\nSaisir le numéro de votre choix:  ")
            choice = glo.new_entry_int2(choice)
            if 1<=choice<=6:
                break
            else:
                print("\nOPTION: 1, 2, 3, 4, 5, 6. Tout autre numéro est invalide.")
        match choice:
            case 1: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CB.enter_matrix()
                CB.print_distributions_marginales(matrix)  
            case 2: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CB.enter_matrix()
                CB.print_mean(matrix)  
            case 3: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CB.enter_matrix()
                CB.print_covariance(matrix)  
            case 4: 
                glo.clear()
                if matrix == []:
                    print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                    matrix = CB.enter_matrix()
                CB.print_droite(matrix)  
            case 5: 
                glo.clear()
                matrix = []
                print("\nENREGISTREMENT DE LA SÉRIE STATISTIQUE\n")
                matrix = CB.enter_matrix()
            case 6:
                break
                matrix = []
                glo.clear()
                menu_principal()


if __name__ == '__main__':
    menu_principal()