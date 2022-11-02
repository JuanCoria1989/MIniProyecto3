##############################################################
from pdb import Restart
from random import seed, randint, choice, sample

from personas import Repartidor,Cocinero, Cliente
from restaurante import *
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###

def crear_repartidores():
    lista_repartidor=[]
    repartidor_1=Repartidor(choice(NOMBRES),randint(20, 30))
    repartidor_2=Repartidor(choice(NOMBRES),randint(20, 30))

    lista_repartidor.append(repartidor_1)
    lista_repartidor.append(repartidor_2)

    return lista_repartidor

def crear_cocineros():
    lista_cocinero=[]
    cocinero1 = Cocinero(choice(NOMBRES), randint(1, 10))
    cocinero2 = Cocinero(choice(NOMBRES), randint(1, 10))
    cocinero3 = Cocinero(choice(NOMBRES), randint(1, 10))
    cocinero4 = Cocinero(choice(NOMBRES), randint(1, 10))
    cocinero5 = Cocinero(choice(NOMBRES), randint(1, 10))

    lista_cocinero.append(cocinero1)
    lista_cocinero.append(cocinero2)
    lista_cocinero.append(cocinero3)
    lista_cocinero.append(cocinero4)
    lista_cocinero.append(cocinero5)

    return lista_cocinero
    
def crear_clientes():
    lista_clientes=[]
    cliente1=Cliente("choice(NOMBRES)", sample(list(INFO_PLATOS.values()),randint(1,5)))
    cliente2=Cliente(choice(NOMBRES), sample(list(INFO_PLATOS.values()),randint(1,5)))
    cliente3=Cliente(choice(NOMBRES), sample(list(INFO_PLATOS.values()),randint(1,5)))
    cliente4=Cliente(choice(NOMBRES), sample(list(INFO_PLATOS.values()),randint(1,5)))
    cliente5=Cliente(choice(NOMBRES), sample(list(INFO_PLATOS.values()),randint(1,5)))
    lista_clientes.append(cliente1)
    lista_clientes.append(cliente2)
    lista_clientes.append(cliente3)
    lista_clientes.append(cliente4)
    lista_clientes.append(cliente5)
    return lista_clientes

def crear_restaurante():
    cocineros= crear_cocineros()
    repartidores= crear_repartidores()

    instancia_restaurante= Restaurante("Don Pepito",INFO_PLATOS,cocineros,repartidores)

    return instancia_restaurante

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("With Love")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
