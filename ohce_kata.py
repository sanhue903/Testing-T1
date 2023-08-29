from datetime import datetime

def ohce(string):
    return string[::-1]

def palindrome(string, inverted_string):
    if string == inverted_string:
        return "¡Bonita palabra!"
    
    return 

def salute(name, time):
    if time.hour >= 6 and time.hour < 12:
        return f"Buenos días {name}!"
    
    if time.hour >= 12 and time.hour < 20:
        return f"Buenas tardes {name}!"
    
    return

if __name__ == "__main__":
    name = "Seba"
    
    print(salute(name,datetime.now().time()))
    
    while (True):
        string = input()
        inversed_string = ohce(string)
        print(inversed_string)
        
        is_palindrome = palindrome(string, inversed_string)
        if is_palindrome is not None:
            print(is_palindrome)
        
        
            
        