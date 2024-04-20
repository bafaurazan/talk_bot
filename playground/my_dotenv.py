from dotenv import load_dotenv, dotenv_values

load_dotenv()

# Pobranie wszystkich zmiennych z pliku .env
env_variables = dotenv_values()

# Wyświetlenie wszystkich zmiennych i ich wartości
for key, value in env_variables.items():
    print(key, "=", value)
