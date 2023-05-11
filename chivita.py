import random
animales = ['perro', 'gato', 'león', "lobo", "tigre", "raton", "oso"]
animal_actual = random.choice(animales)
texto_1_y_final = "Sal de ahí chivita chivita, sal de ahí de ese lugar"  # Se imprime 1 sola y unica ves al principio y cada ves finalizado el ciclo for
texto_2 = f"Hay que llamar a el {animal_actual} para que saque a la chiva"  # los animales van cambiando
texto_3 = f"el {animal_actual} no quiere sacar a la chiva"  # los animales cambian
texto_4 = "La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar"  # Se imprime cada ves finalizado el ciclo for
print(f"{texto_1_y_final}\n{texto_2}\n{texto_3}\n{texto_4}")
texto_final = [texto_3]
animales_exiliados = [animal_actual]
animales.remove(animal_actual)
mov = 0
while animales:
    animal_actual_in = random.choice(animales)
    texto_2_in = f"Hay que llamar a el {animal_actual_in} para que saque a el {animales_exiliados[mov]}"
    texto_3_in = f"el {animal_actual_in} no quiere sacar a el {animales_exiliados[mov]}"
    print(f"{texto_2_in}\n{texto_3_in}")
    print("\n".join(reversed(texto_final)))
    print(texto_4)
    texto_final.append(texto_3_in)
    animales_exiliados.append(animal_actual_in)
    animales.remove(animal_actual_in)
    mov += 1