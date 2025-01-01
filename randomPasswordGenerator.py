import random

def generate_letter():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter = random.choice(letters)
    return letter
   

def generate_number():
    random_int = random.randint(0,9)
    return random_int

def generate_symbol():
    symbols = ["!","@","#","$","%","^","&","*"]
    symbol = random.choice(symbols)
    return symbol

def random_placement(n_symbol, len_password):
    return random.sample(range(len_password), n_symbol)


def password_check(password, len_password, n_symbol):
    symbols = ["!","@","#","$","%","^","&","*"]
    counter = 0
    if len(password) == len_password:
        length_check = True
    else: 
        length_check = False
    
    for i in password:
        if i in symbols:
            counter += 1
    if counter == n_symbol:
        symbol_check = True
    else:
        symbol_check = False

    if length_check and symbol_check:
        return "Password passed the check"
    else:
        return "Password did not pass the check"
    

def generate_password(n_symbol: int, len_password: int):
    password = ""
    symbol_placement = random_placement(n_symbol, len_password)

    for i in range(len_password):
        selection = random.randint(1,2)
        if i in symbol_placement:
            symbol = generate_symbol()
            password += symbol
        elif selection == 1:
            letter = generate_letter()
            password += letter
        elif selection == 2:
            number = generate_number()
            password += str(number)
    return password

password_symbols = int(input("How many symbols should be in your password: "))
password_length = int(input("How long should your password be: "))
user_password = generate_password(password_symbols, password_length)
print(f"User generated password: {user_password}\t{password_check(user_password, password_length, password_symbols)}")







