from turtle import *
from random import randint
from termcolor import colored

# --------------------------- CONFIGURACION INICIAL
speed(1)  # ESTABLECEMOS UNA VELOCIDAD
penup()  # NO PINTA CON EL LAPIZ
goto(-140, 140)

# --------------------------- PINTAR PISTA
cantidadDePasos = 6

for paso in range(cantidadDePasos):
    write(paso)  # ESCRIBE EL PASO
    right(90)  # GIRA 90 GRADOS HACIA LA DERECHA
    forward(10)  # AVANZA 10
    pendown()  # PINTA CON EL LAPIZ
    forward(150)  # AVANZA 150
    penup()  # NO PINTA CON EL LAPIZ
    backward(160)  # REGRESA 160
    left(90)  # GIRA 90 GRADOS HACIA LA IZQUIERDA
    forward(20)  # AVANZA 20

# --------------------------- PINTAR TORTUGAS
cantidadDeTortugas = 4
colors = ['yellow', 'green', 'red', 'blue', 'cyan']
tortugas = []

for indice in range(cantidadDeTortugas):
    tortuga = Turtle()
    tortuga.color(colors[indice])
    tortuga.shape('turtle')

    tortuga.penup()
    tortuga.goto(-160, 120 - (indice * 40))

    tortugas.append(tortuga)

# --------------------------- COMPETIR TORTUGAS
finalizaCarrera = False
tortugaGanadora = Turtle()  # Inicializamos la tortuga ganadora como None

for paso in range(100):
    for tortugaKey in tortugas:
        tortugaKey.forward(randint(1, 5))

        if float(tortugaKey.xcor()) > 0.0:
            finalizaCarrera = True
            tortugaGanadora = tortugaKey  # Asignamos la tortuga ganadora

    if finalizaCarrera:
        break

# --------------------------- PREMIACION DE LA TORTUGA GANADORA
color = tortugaGanadora.color()[0]
mensaje = colored(f'La tortuga ganadora es la de color {color}', color, attrs=['bold', 'underline'])
print(mensaje)