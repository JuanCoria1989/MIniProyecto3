##############################################################
from personas import Cliente,Repartidor,Cocinero
from platos import Comestible,Bebestible

import random
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 3 ###



class Restaurante:
    def __init__(self,n,p,c,r):
        self.nombre=n # Uno le pone el nombre Yo le puse Don Pepito
        self.platos= p # Es un diccionario que recibe todos los platos del Restaurante
        self.cocineros= c #Es una lista de instancias cocineros del Restaurante
        self.repartidor=r # Es una lista de instancias repartidores del Restaurante
        self.calificacion=0
    
    def recibir_pedidos(self, clientes): #Parametro es una lista con objetos de la clase Cliente "Cliente("Alberto", PLATOS_PRUEBA)" PLATOS_PRUEBA es un diccionario "Jugo Natural": ["Jugo Natural", "Bebestible"]
        #clientes = [Cliente("Juan",{"Empanadas": ["Empanadas", "Comestible"],"Mariscos": ["Mariscos", "Comestible"]}),Cliente("Pepe",{"Pepsi": ["Pepsi", "Bebestible"],"Coca-Cola": ["Coca-Cola", "Bebestible"],})]
        cant_cli_entrantes=len(clientes)#Cantidad de clientes entrantes en la lista clientes
        contador=0
        pedido=[]
        for i in range(cant_cli_entrantes):
            for e in clientes[contador].platos_preferidos:
                cocinero_elejido=random.choice(self.cocineros) 

                if cocinero_elejido.energia >0:
                    cocinero_elejido.cocinar(e)
                    if e[1]=="Comestible":
                        instancia_comestible=Comestible(e[0])
                        #print(instancia_comestible)
                        #print(f"Esta es la instancia :{instancia_comestible.nombre}")
                        pedido.append(instancia_comestible)
                    elif e[1]=="Bebestible":
                        instancia_comestible=Bebestible(e[0])
                        #print(instancia_comestible)
                        #print(f"Esta es la instancia :{instancia_comestible.nombre}")
                        pedido.append(instancia_comestible)  
                    
                    #pedido.append(e)
                
            contador=contador+1
        #print(pedido)
        repartidor_elejido=random.choice(self.repartidor) 
        if repartidor_elejido.energia >0:
            demora=repartidor_elejido.repartir(pedido) # retorna la demora del pedido a repartir
            
            for f in clientes:#A cada obejeto clientes llamamos su metodo recibir pedido para calcular la calificacion
                calificacion=f.recibir_pedido(pedido,demora)  
                
            self.calificacion=calificacion    
        elif repartidor_elejido.energia <0:
            pedido=[]
            demora=0
            for f in clientes:
                calificacion=f.recibir_pedido(pedido,demora)
                
            self.calificacion=calificacion 
                

        self.calificacion/cant_cli_entrantes

        
    pass
### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
