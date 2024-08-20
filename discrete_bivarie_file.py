import global_file as glo

def not_double_func(matrix, value1, value2):
    for i in range(len(matrix)):
        if matrix[i][0] == value1 and matrix[i][1] == value2:
            return 0
            break
    return 1

def enter_matrix():
    numb_of_entries = input("\nNombre de couples de modalités:  ")
    numb_of_entries = glo.new_entry_int(numb_of_entries)
    matrix1 = []
   
    for j in range(numb_of_entries):
        print(f"\n\nCOUPLE {j+1}:")
        matrix2 = []
        not_double = 0

        while not_double == 0:
            entry1 = input(f"\nEntrer la variable X:  ")
            entry1 = glo.new_entry_float(entry1)
        
            entry2 = input(f"\nEntrer la variable Y:  ")
            entry2 = glo.new_entry_float(entry2)

            not_double = not_double_func(matrix1, entry1, entry2)
            if not_double == 1:
                break
            else:
                print("\nModalités X et Y déja présentes: MAUVAISES ENTREES\n")

        matrix2.append(entry1)
        matrix2.append(entry2)
        matrix1.append(matrix2)   

    matrix1 = total_effectif(matrix1)
    return matrix1

def total_effectif(matrix: list):
    total_dict = {"total":(len(matrix))}
    matrix.append(total_dict)
    return matrix

def mean(matrix: list):
    mean_x,  mean_y = 0, 0
    for j in range(len(matrix)-1):
        mean_x += matrix[j][0]
        mean_y += matrix[j][1]
    mean_x /= matrix[len(matrix)-1]['total']
    mean_y /= matrix[len(matrix)-1]['total']
    matrix[len(matrix)-1]['moyenne'] = mean_x, mean_y
    return mean_x, mean_y

def print_mean(matrix: list):
    mean_x, mean_y = 0, 0
    print(f"\n{'*'*36}MOYENNES{'*'*36}\n")
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean_x, mean_y = mean(matrix)
    print(f"Moyenne de X: {round(matrix[len(matrix)-1]['moyenne'][0], 3)}\n")
    print(f"Moyenne de Y: {round(matrix[len(matrix)-1]['moyenne'][1], 3)}\n")
    print(f"\n{'*'*80}\n")

def variance(matrix: list):
    mean_x, mean_y = 0, 0
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean_x, mean_y = mean(matrix)
    variance_x, variance_y = 0, 0
    for j in range(len(matrix)-1):
        variance_x += (matrix[j][0] ** 2)
        variance_y += (matrix[j][1] ** 2)
    variance_x /= matrix[len(matrix)-1]['total']
    variance_y /= matrix[len(matrix)-1]['total']
    variance_x -= (matrix[len(matrix)-1]['moyenne'][0] ** 2)
    variance_y -= (matrix[len(matrix)-1]['moyenne'][1] ** 2)
    matrix[len(matrix)-1]['variance'] = variance_x, variance_y
    return variance_x, variance_y

def ecart_type(matrix: list):
    var_x, var_y = 0, 0
    if (matrix[len(matrix)-1]).get('variance') == None:
        var_x, var_y = variance(matrix)
    ecart_x = (matrix[len(matrix)-1]['variance'][0]) ** (1/2)
    ecart_y = (matrix[len(matrix)-1]['variance'][1]) ** (1/2)
    matrix[len(matrix)-1]['ecart'] = ecart_x, ecart_y
    return ecart_x, ecart_y

def print_variance_ecart(matrix: list):
    print(f"\n{'*'*28}VARIANCES ET ECART-TYPE{'*'*29}\n")

    variance_x, variance_y, ecart_x, ecart_y = 0, 0, 0, 0
    if (matrix[len(matrix)-1]).get('variance') == None:
        variance_x, variance_y = variance(matrix)
    if (matrix[len(matrix)-1]).get('ecart') == None:
        ecart_x, ecart_y = ecart_type(matrix)

    ecart_x = (matrix[len(matrix)-1]['ecart'][0]) 
    ecart_y = (matrix[len(matrix)-1]['ecart'][1])
    variance_x = (matrix[len(matrix)-1]['variance'][0]) 
    variance_y = (matrix[len(matrix)-1]['variance'][1])
    
    print(f"Variance de X:   {round(variance_x, 3)}\n")
    print(f"Ecart-type de X:   {round(ecart_x, 3)}\n")
    print(f"Variance de Y:   {round(variance_y, 3)}\n")
    print(f"Ecart-type de Y:   {round(ecart_y, 3)}\n")
    print(f"\n{'*'*80}\n")

def covariance(matrix: list):
    cov, mean_x, mean_y = 0, 0, 0
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean_x, mean_y = mean(matrix)
    for j in range(len(matrix)-1):
        cov += (matrix[j][0] * matrix[j][1])
    cov /= matrix[len(matrix)-1]['total']
    cov -= (matrix[len(matrix)-1]['moyenne'][0] * matrix[len(matrix)-1]['moyenne'][1])
    matrix[len(matrix)-1]['covariance'] = cov
    return cov

def print_covariance(matrix: list):
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

def print_coefficient(matrix: list):
    print(f"\n{'*'*27}COEFFICIENT DE CORRELATION{'*'*27}\n")
    coef = 0
    if (matrix[len(matrix)-1]).get('coefficient') == None:
        coef = coefficient_correlation(matrix)
    coef = matrix[len(matrix)-1]['coefficient']
    print(f"Coefficient de correlation de X et Y: {round(coef, 3)}\n")
    if coef > 0:
        print(f"CONCLUSION: Plus la variable X augmente, plus la variable Y augmente aussi.\n")
    elif coef < 0:
        print(f"CONCLUSION: Plus la variable X est grande, moins la variable Y est grande..\n")
    else:
        print(f"CONCLUSION: Aucune dépendance linéaire entre X et Y.\n")
    print(f"\n{'*'*80}\n")















