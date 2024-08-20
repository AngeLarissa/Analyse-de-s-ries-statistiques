import global_file as glo

def not_double_func(matrix, value1, value2, value3, value4):
    for i in range(len(matrix)):
        if matrix[i][0] == value1 and matrix[i][1] == value2 and matrix[i][2] == value3 and matrix[i][3] == value4:
            return 0
            break
    return 1

def total_func(matrix: list):
    total = 0
    for j in range(len(matrix)):
        total += matrix[j][4]
    return total 

def enter_matrix():
    numb_of_entries1 = input("\nNombre de Classes de la variable X:  ")
    numb_of_entries1 = glo.new_entry_int(numb_of_entries1)
    numb_of_entries2 = input("\nNombre de Classes de la variable Y:  ")
    numb_of_entries2 = glo.new_entry_int(numb_of_entries2)
    matrix1 = []
    k = 1
    entry = 0
    for i in range(numb_of_entries1):
        for j in range(numb_of_entries2):
            matrix2 = []
            not_double = 0

            while not_double == 0:
                entry1, entry2 = 10, 0
                while  entry1 >= entry2:
                    print(f"\n\n***Entree {k} =>  X: Classe {i+1}  et  Y: Classe {j+1}\n")
                    print(f"\nX: Classe {i+1}")
                    entry1 = input(f"\nBorne inférieure de X{i+1}:  ")
                    entry1 = glo.new_entry_float(entry1)

                    entry2 = input(f"\nBorne supérieure de X{i+1}:  ")
                    entry2 = glo.new_entry_float(entry2)

                    if entry1<entry2:
                        break
                    else:
                        print("\nBorne inf >= Borne sup: MAUVAISES ENTREES")

            

                entry3, entry4 = 10, 0
                while  entry3 >= entry4:
                    print(f"\nY: Classe {j+1}")
                    entry3 = input(f"\nBorne inférieure de Y{j+1}:  ")
                    entry3 = glo.new_entry_float(entry3)

                    entry4 = input(f"\nBorne supérieure de X{j+1}:  ")
                    entry4 = glo.new_entry_float(entry4)

                    if entry3<entry4:
                        break
                    else:
                        print("\nBorne inf >= Borne sup: MAUVAISES ENTREES")

                not_double = not_double_func(matrix1, entry1, entry2, entry3, entry4)
                if not_double == 1:
                    break
                else:
                    print("\nClasses déja présentes: MAUVAISES ENTREES\n")

            matrix2.append(entry1)
            matrix2.append(entry2)
            matrix2.append(entry3)
            matrix2.append(entry4)

            entry = input(f"\nEffectif: de X:[{entry1};{entry2}[ et Y:[{entry3};{entry4}[:     ")
            entry = glo.new_entry_int(entry)
            matrix2.append(entry)
            k += 1
            matrix1.append(matrix2)  

    total_dict = {"total":total_func(matrix1)}
    matrix1.append(total_dict) 

    return matrix1

def distributions_marginales(matrix: list):
    distribution_x = set()
    distribution_y = set()
    for j in range(len(matrix) -1):
        number1, number2 = 0, 0
        for i in range(len(matrix) - 1):
            if (matrix[j][0] == matrix[i][0]) and (matrix[j][1] == matrix[i][1]):
                number1 += matrix[i][4]
            if (matrix[j][2] == matrix[i][2]) and (matrix[j][3] == matrix[i][3]):
                number2 += matrix[i][4]

        distribution_x.add((matrix[j][0], matrix[j][1], number1, (matrix[j][0] + matrix[j][1]) / 2))
        distribution_y.add((matrix[j][2], matrix[j][3], number2, (matrix[j][2] + matrix[j][3]) / 2))

    distribution_x = list(distribution_x)
    distribution_y = list(distribution_y)


    (matrix[len(matrix)-1]['distribution_x']) = distribution_x
    (matrix[len(matrix)-1]['distribution_y']) = distribution_y

    return distribution_x, distribution_y

def print_distributions_marginales(matrix: list):
    distribution_x, distribution_y = [], []
    if (matrix[len(matrix)-1]).get('distribution_x') == None:
        distribution_x, distribution_y = distributions_marginales(matrix)
    distribution_x =  matrix[len(matrix)-1]['distribution_x']
    distribution_y =  matrix[len(matrix)-1]['distribution_y']

    print(f"\n{'*'*26}DISTRIBUTION MARGINALE DE X{'*'*27}\n")
    print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
    print(f"|{'Classes'.center(30)}|{'Effectif marginal de X'.center(30)}|{'Centres'.center(30)}|")
    for j in range(len(distribution_x)):
        print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
        print(f"|{f'[{distribution_x[j][0]},{distribution_x[j][1]}['.center(30)}|{distribution_x[j][2]:^30}|{distribution_x[j][3]:^30}|")
    print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
    print(f"|{'Total'.center(30)}|{matrix[len(matrix)-1]['total']:^30}|                              |")
    print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
    print(f"\n{'*'*80}\n")

    print(f"\n\n{'*'*26}DISTRIBUTION MARGINALE DE Y{'*'*27}\n")
    print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
    print(f"|{'Classes'.center(30)}|{'Effectif marginal de Y'.center(30)}|{'Centres'.center(30)}|")
    for j in range(len(distribution_y)):
        print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
        print(f"|{f'[{distribution_y[j][0]},{distribution_y[j][1]}['.center(30)}|{distribution_y[j][2]:^30}|{distribution_y[j][3]:^30}|")
    print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
    print(f"|{'Total'.center(30)}|{matrix[len(matrix)-1]['total']:^30}|                              |")
    print(f"|{'-' * 30}|{'-' * 30}|{'-' * 30}|")
    print(f"\n{'*'*80}\n")


def mean(matrix: list):
    distribution_x, distribution_y = [], []
    if (matrix[len(matrix)-1]).get('distribution_x') == None:
        distribution_x, distribution_y = distributions_marginales(matrix)
    distribution_x =  matrix[len(matrix)-1]['distribution_x']
    distribution_y =  matrix[len(matrix)-1]['distribution_y']

    mean_x,  mean_y = 0, 0
    for j in range(len(distribution_x)):
        mean_x += distribution_x[j][2] * distribution_x[j][3]
    for j in range(len(distribution_y)):
        mean_y += distribution_y[j][2] * distribution_y[j][3]

    mean_x /= matrix[len(matrix)-1]['total']
    mean_y /= matrix[len(matrix)-1]['total']

    matrix[len(matrix)-1]['moyenne'] = mean_x, mean_y
    return mean_x, mean_y

def print_mean(matrix: list):
    print(f"\n{'*'*30}MOYENNES MARGINALES{'*'*31}\n")
    mean_x, mean_y = 0, 0
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean_x, mean_y = mean(matrix)
    print(f"Moyenne marginale de X: {round(matrix[len(matrix)-1]['moyenne'][0], 3)}\n")
    print(f"Moyenne marginale de Y: {round(matrix[len(matrix)-1]['moyenne'][1], 3)}\n")
    print(f"\n{'*'*80}\n")

def variance(matrix: list):
    distribution_x, distribution_y = [], []
    if (matrix[len(matrix)-1]).get('distribution_x') == None:
        distribution_x, distribution_y = distributions_marginales(matrix)
    distribution_x =  matrix[len(matrix)-1]['distribution_x']
    distribution_y =  matrix[len(matrix)-1]['distribution_y']

    mean_x, mean_y = 0, 0
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean_x, mean_y = mean(matrix)

    variance_x, variance_y = 0, 0
    for j in range(len(distribution_x)):
        variance_x += (((distribution_x[j][3] - matrix[len(matrix)-1]['moyenne'][0]) ** 2) * distribution_x[j][2] )

    for j in range(len(distribution_y)):
        variance_y += (((distribution_y[j][3] - matrix[len(matrix)-1]['moyenne'][1]) ** 2) * distribution_y[j][2] )

    variance_x /= matrix[len(matrix)-1]['total']
    variance_y /= matrix[len(matrix)-1]['total']
  
    matrix[len(matrix)-1]['variance'] = variance_x, variance_y
    return variance_x, variance_y

def ecart_type(matrix:list):
    var_x, var_y = 0, 0
    if (matrix[len(matrix)-1]).get('variance') == None:
        var_x, var_y = variance(matrix)
    ecart_x = (matrix[len(matrix)-1]['variance'][0]) ** (1/2)
    ecart_y = (matrix[len(matrix)-1]['variance'][1]) ** (1/2)
    matrix[len(matrix)-1]['ecart'] = ecart_x, ecart_y
    return ecart_x, ecart_y

def covariance(matrix: list):
    cov, mean_x, mean_y = 0, 0, 0
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean_x, mean_y = mean(matrix)
    for j in range(len(matrix)-1):
        cov += (matrix[j][4]) * ((matrix[j][0] + matrix[j][1])/2) * ((matrix[j][2] + matrix[j][3])/2)
    cov /= matrix[len(matrix)-1]['total']
    cov -= (matrix[len(matrix)-1]['moyenne'][0] * matrix[len(matrix)-1]['moyenne'][1])
    matrix[len(matrix)-1]['covariance'] = cov
    return cov

def print_covariance(matrix:list):
    print(f"\n{'*'*35}COVARIANCE{'*'*35}\n")
    cov = 0
    if (matrix[len(matrix)-1]).get('covariance') == None:
        cov = covariance(matrix)
    print(f"Covariance de X et Y: {round(matrix[len(matrix)-1]['covariance'], 3)}\n")
    print(f"\n{'*'*80}\n")

def droite_correlation(matrix: list):
    cov, var_x, var_y = 0, 0, 0
    if (matrix[len(matrix)-1]).get('covariance') == None:
        cov = covariance(matrix)
    if (matrix[len(matrix)-1]).get('variance') == None:
        var_x, var_y = variance(matrix)
    a = (matrix[len(matrix)-1]['covariance']) / (matrix[len(matrix)-1]['variance'][0])
    b = matrix[len(matrix)-1]['moyenne'][1] - (a * (matrix[len(matrix)-1]['moyenne'][0]))
    matrix[len(matrix)-1]['droite'] = a, b
    return a, b

def print_droite(matrix: list):
    print(f"\n{'*'*29}DROITE DE CORRELATION{'*'*30}\n")
    a, b = 0, 0
    if (matrix[len(matrix)-1]).get('droite') == None:
        a, b = droite_correlation(matrix)
    print(f"La droite de regression est: Y = {round(matrix[len(matrix)-1]['droite'][0], 3)}X + {round(matrix[len(matrix)-1]['droite'][1], 3)}\n")
    print(f"\n{'*'*80}\n")

def coefficient_correlation(matrix: list):
    cov, ecart_x, ecart_y = 0, 0 , 0
    if (matrix[len(matrix)-1]).get('ecart') == None:
        ecart_x, ecart_y = ecart_type(matrix)
    if (matrix[len(matrix)-1]).get('covariance') == None:
        cov = covariance(matrix)
    coef = (matrix[len(matrix)-1]['covariance']) / (matrix[len(matrix)-1]['ecart'][0] * matrix[len(matrix)-1]['ecart'][1])
    matrix[len(matrix)-1]['coefficient'] = coef
    return coef
















