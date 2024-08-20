import os

def is_int(data):
	try:
		int(data)
		return True
	except ValueError:
		return False

def is_float(data):
	try:
		float(data)
		return True
	except ValueError:
		return False

def new_entry_int(entry):
    while True:
        if is_int(entry):
            if int(entry) > 0:
                entry = int(entry)
                return entry
            else:
                print("\nAttention!!! \n")
                entry = input("Nouvelle valeur non nulle et positive:  ")
        else:
            print("\nAttention!!! Entrée invalide\n")
            entry = input("Nouvelle valeur entière:  ")

def new_entry_int2(entry):
    while True:
        if is_int(entry):
            entry = int(entry)
            return entry
        else:
            print("\nAttention!!! Entrée invalide\n")
            entry = input("Nouvelle valeur entière:  ")

def new_entry_float(entry):
    while True:
        if is_int(entry):
            entry = int(entry)
            return entry
        elif is_float(entry):
            entry = float(entry)
            return entry
        else:
            print("Attention!!! Entrée invalide\n")
            entry = input("Nouvelle valeur réelle:  ")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')