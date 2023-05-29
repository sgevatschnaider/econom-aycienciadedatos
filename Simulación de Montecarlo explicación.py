#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import random

def roll_dice():
    # Genera dos números aleatorios entre 1 y 6 para simular el lanzamiento de dos dados
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    # Verifica si los números de los dados son iguales
    if die_1 == die_2:
        same_num = True
    else:
        same_num = False

    # Devuelve un valor booleano que indica si los números de los dados son iguales
    return same_num

# Número de simulaciones para ejecutar
num_simulations = 10000

# Número máximo de tiradas permitidas por simulación
max_num_rolls = 1000

# Cantidad apostada en cada tirada
bet = 1

# Lista para almacenar la probabilidad de ganar en cada simulación
win_probability = []

# Lista para almacenar el saldo final alcanzado en cada simulación
end_balance = []

# Bucle que realiza las simulaciones
for i in range(num_simulations):
    # Lista para almacenar el saldo en cada tirada de una simulación
    balance = [1000]

    # Lista para almacenar el número de tiradas realizadas en una simulación
    num_rolls = [0]

    # Contador para llevar el registro de las veces que se obtuvo un resultado igual en los dados
    num_wins = 0

    # Bucle que simula las tiradas hasta alcanzar el número máximo de tiradas permitidas
    while num_rolls[-1] < max_num_rolls:
        # Llama a la función roll_dice() para determinar si los números de los dados son iguales
        same = roll_dice()

        # Actualiza el saldo y el número de tiradas según el resultado obtenido
        if same:
            balance.append(balance[-1] + 2 * bet)  # Si los números de los dados son iguales, se incrementa el saldo en 2 veces la apuesta
            num_wins += 1  # Se incrementa el contador de victorias
        else:
            balance.append(balance[-1] - bet)  # Si los números de los dados no son iguales, se reduce el saldo en la apuesta

        num_rolls.append(num_rolls[-1] + 1)  # Se incrementa el contador de tiradas

    # Calcula la probabilidad de ganar en la simulación actual y la agrega a la lista de probabilidades de ganar
    win_probability.append(num_wins / num_rolls[-1])

    # Agrega el saldo final alcanzado en la simulación actual a la lista de saldos finales
    end_balance.append(balance[-1])

    # Grafica el saldo en función del número de tiradas para la simulación actual
    plt.plot(num_rolls, balance)

# Muestra la gráfica generada
plt.show()


# In[2]:


import random
import matplotlib.pyplot as plt

def roll_dice():
    # Función que simula el lanzamiento de dos dados
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    # Verifica si los números de los dados son iguales
    if die_1 == die_2:
        same_num = True
    else:
        same_num = False

    # Devuelve un valor booleano que indica si los números de los dados son iguales
    return same_num

# Número de simulaciones a realizar
num_simulations = 10000

# Número máximo de tiradas permitidas por simulación
max_num_rolls = 1000

# Lista de valores de apuesta a probar
bet_values = [0.1, 0.5, 1.0, 2.0, 2.5, 3.0]

# Lista para almacenar las ganancias promedio correspondientes a cada valor de apuesta
average_balances = []

# Bucle que itera sobre cada valor de apuesta
for bet in bet_values:
    total_balance = 0

    # Bucle que realiza las simulaciones
    for i in range(num_simulations):
        balance = 1000  # Saldo inicial de 1000 dólares
        num_rolls = 0  # Contador para llevar el registro del número de tiradas

        # Bucle que simula las tiradas hasta alcanzar el número máximo de tiradas permitidas
        while num_rolls < max_num_rolls:
            same = roll_dice()  # Llama a la función roll_dice() para determinar si los números de los dados son iguales

            if same:
                balance += 2 * bet  # Si los números de los dados son iguales, se incrementa el saldo en 2 veces la apuesta
            else:
                balance -= bet  # Si los números de los dados no son iguales, se reduce el saldo en la apuesta

            num_rolls += 1

        total_balance += balance

    average_balance = total_balance / num_simulations  # Calcula la ganancia promedio para el valor de apuesta actual
    average_balances.append(average_balance)  # Agrega la ganancia promedio a la lista de ganancias promedio
    print(f"Para bet={bet}: Ganancia promedio = {average_balance}")

# Graficar los resultados
plt.plot(bet_values, average_balances, marker='o')  # Grafica los valores de apuesta en el eje x y las ganancias promedio en el eje y
plt.title("Ganancia promedio según el valor de apuesta")
plt.xlabel("Valor de apuesta")
plt.ylabel("Ganancia promedio")
plt.show()


# In[ ]:





# In[ ]:




