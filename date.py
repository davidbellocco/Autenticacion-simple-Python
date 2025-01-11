import random
import time
name =input("Ingresa tu nombre:")
credenciales =input("Ingresa tu contraseña:")
password = 232343

def times():
    time.sleep(2)
    
def Verificar(digit):
    
    try:
        if not digit.isdigit():
            print("Debes ingresar solo números.")
        elif len(digit) > 6:
            print("No puedes ingresar más de seis dígitos.")
        elif name !="" and int(digit) == password:
            times()
            print(f"Bienvenido {name}")
            randoms()
        else:
            print("Contraseña incorrecta.")
    except ValueError:
        print("Ocurrió un error con la entrada.")


def randoms():
    aleatorio = random.randint(1,10)
    print(f"Tu ticket es {aleatorio} ")

Verificar(credenciales)

