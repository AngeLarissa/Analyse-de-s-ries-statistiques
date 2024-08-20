import global_file as glo

def not_double_func(matrix, value1, value2):
    for i in range(len(matrix)):
        if matrix[i][0] == value1 and matrix[i][1] == value2:
            return 0
            break
    return 1
    

def order(matrix: list):
    a = []
    for j in range(len(matrix) - 1):
        for i in range(j+1, len(matrix)):
            if matrix[i][0] < matrix[j][0]:
                a = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = a
    return matrix

def enter_matrix():
    numb_of_entries = input("\nNombre de Classes:  ")
    numb_of_entries = glo.new_entry_int(numb_of_entries)
    matrix1 = []
   
    for j in range(numb_of_entries):
        entry1, entry2, entry = 10, 0, 0
        matrix2 = []
        not_double = 0
        while  entry1 >= entry2 or not_double == 0:
            print(f"\n\nCLASSE {j+1}:")
            entry1 = input(f"\nBorne inférieure:  ")
            entry1 = glo.new_entry_float(entry1)

            entry2 = input(f"\nBorne supérieure:  ")
            entry2 = glo.new_entry_float(entry2)

            if entry1<entry2 :
                not_double = not_double_func(matrix1, entry1, entry2)
                if not_double == 1:
                    break
                else:
                    print("\nClasse déja présente: MAUVAISES ENTREES\n")
                    
            else:
                print("\nBorne inf >= Borne sup: MAUVAISES ENTREES")

        matrix2.append(entry1)
        matrix2.append(entry2)
        entry = input(f"\nEffectif:  ")
        entry = glo.new_entry_int(entry)
        matrix2.append(entry)

        matrix1.append(matrix2)   

    matrix1 = order(matrix1)

    return matrix1

def test_amplitude(matrix):
    test = [matrix[j][1] - matrix[j][0] for j in range(len(matrix))]
    return all(element == test[0] for element in test)

def total_effectif(matrix: list):
    total = 0
    for j in range(len(matrix)):
        total += matrix[j][2]
    return total

def statistical_table(matrix: list):
    ecc, frequence, fcc, densité, centre = 0, 0, 0, 0, 0
    total = total_effectif(matrix)
    val = test_amplitude(matrix)
    for j in range(len(matrix)):
        #calculate centre
        centre =  (matrix[j][0] +  matrix[j][1]) / 2
        matrix[j].append(centre)
        # calculate ecc
        ecc += matrix[j][2]
        matrix[j].append(ecc)
        # calculate frequence
        frequence = matrix[j][2]/total
        matrix[j].append(frequence)
        # calculate fcc
        fcc += matrix[j][5]
        matrix[j].append(fcc)
        if val == False:
            densité = matrix[j][2] / (matrix[j][1] - matrix[j][0])
            matrix[j].append(densité)
    total_dict = {"total":total}
    matrix.append(total_dict)

    return matrix

def print_statistical_table(matrix: list):
    if type(matrix[(len(matrix)) - 1]) != dict:
        matrix = statistical_table(matrix)
    if len(matrix[1]) ==7 or len(matrix) ==2:
        print(f"\n{'*'*30}TABLEAU STATISTIQUE{'*'*31}\n")
        print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
        print(f"|{'Classes'.center(15)}|{'Effectifs'.center(15)}|{'Centres'.center(15)}|{'ECC'.center(15)}|{'Fréquences'.center(15)}|{'FCC'.center(15)}|")
        for j in range(len(matrix)-1):
            print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
            print(f"|{f'[{matrix[j][0]},{matrix[j][1]}['.center(15)}|{matrix[j][2]:^15}|{matrix[j][3]:^15}|{matrix[j][4]:^15}|{round(matrix[j][5], 3):^15}|{round(matrix[j][6], 3):^15}|")
        print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
        print(f"|{'Total'.center(15)}|{matrix[len(matrix)-1]['total']:^15}|               |               |{1:^15}|               |")
        print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
        print(f"\n{'*'*80}\n")
    else:
        print(f"\n{'*'*30}TABLEAU STATISTIQUE{'*'*31}\n")
        print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
        print(f"|{'Classes'.center(15)}|{'Effectifs'.center(15)}|{'Centres'.center(15)}|{'ECC'.center(15)}|{'Fréquences'.center(15)}|{'FCC'.center(15)}|{'Densités'.center(15)}|")
        for j in range(len(matrix)-1):
            print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
            print(f"|{f'[{matrix[j][0]},{matrix[j][1]}['.center(15)}|{matrix[j][2]:^15}|{matrix[j][3]:^15}|{matrix[j][4]:^15}|{round(matrix[j][5], 3):^15}|{round(matrix[j][6], 3):^15}|{matrix[j][7]:^15}|")
        print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
        print(f"|{'Total'.center(15)}|{matrix[len(matrix)-1]['total']:^15}|               |               |{1:^15}|               |               |")
        print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
        print(f"\n{'*'*80}\n")

def upper_lower(matrix: list):
    upper_value = 0
    for j in range(len(matrix)-1):
        if matrix[j][1]>upper_value:
            upper_value = matrix[j][1]
    lower_value = upper_value
    for j in range(len(matrix)-1):
        if matrix[j][0]<lower_value:
            lower_value = matrix[j][0]
    matrix[len(matrix)-1]['upper'] = upper_value
    matrix[len(matrix)-1]['lower'] = lower_value
    return upper_value, lower_value


def mean(matrix: list):
    mean = 0
    for j in range(len(matrix)-1):
        mean += matrix[j][2] * matrix[j][3]
    mean /= matrix[len(matrix)-1]['total']
    matrix[len(matrix)-1]['moyenne'] = mean
    return mean

def mode(matrix: list):
    if len(matrix[1]) ==7 or len(matrix) == 2:
        upper_effectif, index = 0, 0
        for j in range(len(matrix)-1):
            if matrix[j][2] > upper_effectif:
                upper_effectif = matrix[j][2]
                index = j

        mode0 = (matrix[index][0], matrix[index][1], matrix[j][3])
    else:
        upper_effectif, index = 0, 0
        for j in range(len(matrix)-1):
            if matrix[j][7] > upper_effectif:
                upper_effectif = matrix[j][7]
                index = j
        if index == 0:
            m = matrix[index][0] + ((matrix[index][7])/(matrix[index][7] + matrix[index][7] - matrix[index+1][7])*(matrix[index][1] - matrix[index][0]))
        else:
            m = matrix[index][0] + ((matrix[index][7] - matrix[index-1][7])/(matrix[index][7] - matrix[index-1][7] + matrix[index][7] - matrix[index+1][7])*(matrix[index][1] - matrix[index][0]))
        mode0 = (matrix[index][0], matrix[index][1], m)
    matrix[len(matrix)-1]['mode'] = mode0
    return mode0

def mediane(matrix: list):
    mediane0 = 0 
    for j in range(len(matrix)-1):
        if matrix[j][6] >= 0.5:
            if j==0:
                mediane0 = matrix[j][0] + (0.5/(matrix[j][6])*(matrix[j][1] - matrix[j][0]))
            else:
                mediane0 = matrix[j][0] + ((0.5 - matrix[j-1][6])/(matrix[j][6] - matrix[j-1][6])*(matrix[j][1] - matrix[j][0]))
            break
    matrix[len(matrix)-1]['mediane'] = mediane0
    return mediane0

def first_quartile(matrix: list):
    q1_quartile = 0
    for j in range(len(matrix)-1):
        if matrix[j][6] >= 0.25:
            if j==0:
                q1_quartile = matrix[j][0] + (0.25/(matrix[j][6])*(matrix[j][1] - matrix[j][0]))
            else:
                q1_quartile = matrix[j][0] + ((0.25 - matrix[j-1][6])/(matrix[j][6] - matrix[j-1][6])*(matrix[j][1] - matrix[j][0]))
            break
    matrix[len(matrix)-1]["q1"] = q1_quartile
    return q1_quartile

def third_quartile(matrix: list):
    q3_quartile = 0
    for j in range(len(matrix)-1):
        if matrix[j][6] >= 0.75:
            if j==0:
                q3_quartile = matrix[j][0] + (0.75/(matrix[j][6])*(matrix[j][1] - matrix[j][0]))
            else:
                q3_quartile = matrix[j][0] + ((0.75 - matrix[j-1][6])/(matrix[j][6] - matrix[j-1][6])*(matrix[j][1] - matrix[j][0]))
            break
    matrix[len(matrix)-1]["q3"] = q3_quartile
    return q3_quartile
        
def central_values(matrix: list):
    mean1, mode1, mediane1, q1_quartile, q3_quartile = 0, 0, 0, 0, 0
    matrix = matrix
    if type(matrix[(len(matrix)) - 1]) != dict:
        matrix = statistical_table(matrix)
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean1 = mean(matrix)
    if (matrix[len(matrix)-1]).get('mode') == None:    
        mode1 = mode(matrix)
    if (matrix[len(matrix)-1]).get('mediane') == None:
        mediane1 = mediane(matrix)
    if (matrix[len(matrix)-1]).get('q1') == None:
        q1_quartile = first_quartile(matrix)
    if (matrix[len(matrix)-1]).get('q3') == None:
        q3_quartile = third_quartile(matrix)
    return matrix[len(matrix)-1]['moyenne'], matrix[len(matrix)-1]['mode'], matrix[len(matrix)-1]['mediane'], matrix[len(matrix)-1]['q1'], matrix[len(matrix)-1]['q3']

def print_central_values(matrix: list):
    mean0, mode0, mediane0, q1_quartile, q3_quartile = central_values(matrix)
    print(f"\n{'*'*31}VALEURS CENTRALES{'*'*32}\n")
    print(f"Moyenne: {round(mean0, 3)}\n")
    print(f"Classe modale: [{mode0[0]}, {mode0[1]}[\n")
    print(f"Mode: {round(mode0[2], 3 )}\n")
    print(f"Mediane: {round(mediane0, 3)}\n")
    print(f"Premier quartile: {round(q1_quartile, 3)}\n")
    print(f"Troisieme quartile: {round(q3_quartile, 3)}\n")

    print(f"\n{'*'*80}\n")

def etendue(matrix: list):
    upper, lower = 0, 0
    if (matrix[len(matrix)-1]).get('upper') == None:
        upper, lower = upper_lower(matrix)
    upper_value = matrix[len(matrix)-1]['upper']
    lower_value = matrix[len(matrix)-1]['lower']
    etendue = upper_value - lower_value
    matrix[len(matrix)-1]['etendue'] = etendue
    return etendue

def variance(matrix: list):
    variance, mean0 = 0, 0
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean0 = mean(matrix)
    for j in range(len(matrix)-1):
        variance += (matrix[j][3] ** 2) * (matrix[j][5])
    variance -= ((matrix[len(matrix)-1]['moyenne']) ** 2)
    matrix[len(matrix)-1]['variance'] = variance
    return variance

def ecart_type(matrix:list):
    var = 0
    if (matrix[len(matrix)-1]).get('variance') == None:
        var = variance(matrix)
    ecart = (matrix[len(matrix)-1]['variance']) ** (1/2)
    matrix[len(matrix)-1]['ecart'] = ecart
    return ecart

def distance_interquartile(matrix:list):
    q1, q3 = 0, 0
    if (matrix[len(matrix)-1]).get('q1') == None:
        q1 = first_quartile(matrix)
    if (matrix[len(matrix)-1]).get('q3') == None:
        q3 = third_quartile(matrix)
    iq_distance = matrix[len(matrix)-1]['q3'] - matrix[len(matrix)-1]['q1']
    matrix[len(matrix)-1]['iq'] = iq_distance
    return iq_distance

def coefficient_variation(matrix:list):
    ecart, moyenne = 0, 0
    if (matrix[len(matrix)-1]).get('ecart') == None:
        ecart = ecart_type(matrix)
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        moyenne = mean(matrix)
    coefficient = matrix[len(matrix)-1]['ecart'] / matrix[len(matrix)-1]['moyenne']
    matrix[len(matrix)-1]['coefficient'] = coefficient
    return coefficient

def dispersion_values(matrix: list):
    etendue0, variance0, ecart, distance, coefficient = 0, 0, 0, 0, 0
    mean1, q1, q3 = 0, 0, 0

    if type(matrix[(len(matrix)) - 1]) != dict:
        matrix = statistical_table(matrix)
    if (matrix[len(matrix)-1]).get('upper') == None:
        upper, lower = upper_lower(matrix)
    if (matrix[len(matrix)-1]).get('moyenne') == None:
        mean1 = mean(matrix)
    if (matrix[len(matrix)-1]).get('q1') == None:
        q1 = first_quartile(matrix)
    if (matrix[len(matrix)-1]).get('q3') == None:
        q3 = third_quartile(matrix)

    if (matrix[len(matrix)-1]).get('etendue') == None:
        etendue0 = etendue(matrix)
    if (matrix[len(matrix)-1]).get('variance') == None:
        variance0 = variance(matrix)
    if (matrix[len(matrix)-1]).get('ecart') == None:
        ecart = ecart_type(matrix)
    if (matrix[len(matrix)-1]).get('iq') == None:
        distance = distance_interquartile(matrix)
    if (matrix[len(matrix)-1]).get('coefficient') == None:  
        coefficient = coefficient_variation(matrix)
    return matrix[len(matrix)-1]['etendue'], matrix[len(matrix)-1]['variance'], matrix[len(matrix)-1]['ecart'], matrix[len(matrix)-1]['iq'], matrix[len(matrix)-1]['coefficient']

def print_dispersion_values(matrix: list):
    etendue0, variance0, ecart, distance, coefficient = dispersion_values(matrix)
    print(f"\n{'*'*29}VALEURS DE DISPERSION{'*'*30}\n")
    print(f"Etendue: {etendue0}\n")
    print(f"Variance: {round(variance0, 3)}\n")
    print(f"Ecart-type: {round(ecart, 3)}\n")
    print(f"Distance interquartile: {round(distance, 3)}\n")
    print(f"Coefficient de variation: {round(coefficient, 3)}\n")

    print(f"\n{'*'*80}\n")



