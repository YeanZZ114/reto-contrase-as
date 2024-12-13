import random
import string

def generate_password(long, use_mayus, use_minus, use_numbers, use_symbols):
    characters = ''  
    if use_mayus:
        characters += string.ascii_uppercase  
    if use_minus:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits 
    if use_symbols:
        characters += string.punctuation  
    if not characters:
        return "Error: Debes seleccionar al menos un tipo de carácter."
    password = ''.join(random.choice(characters) for _ in range(long))
    return password
def main():
    print("Bienvenido al generador de contraseñas seguras.")
    while True:
        long = int(input("Introduce la longitud de la contraseña (mínimo 4): "))
        if long < 4:
            print("La longitud mínima es 4. Inténtalo de nuevo.")
            continue
        use_mayus = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
        use_minus = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
        use_numbers = input("¿Incluir números? (si/no): ").lower() == 'si'
        use_symbols = input("¿Incluir símbolos? (si/no): ").lower() == 'si'
        password = generate_password(long, use_mayus, use_minus, use_numbers, use_symbols)
        print(f"Contraseña generada: {password}")        
        another = input("¿Deseas generar otra contraseña? (si/no): ").lower()
        if another != 'si':
            print("Gracias por usar el generador de contraseñas. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()