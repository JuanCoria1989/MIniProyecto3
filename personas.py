##############################################################
from random import randint, sample
import random
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self,n):
        self.nombre=n
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, n,ti):
        super().__init__(n)
        self.tiempo_entrega= ti
        self.energia=randint(75,100)
    pass  

    def repartir(self,pedido): #Recibe como parametro o argumento una lista de platos 
        factor_tamaño=0 # Se utiliza para restar energía a los repartidores según la cantidad de platos entregados
        factor_velocidad=0
        if len(pedido)<=2:
            factor_tamaño=5
            factor_velocidad=1.25
        elif len(pedido)>=3:
            factor_tamaño=15
            factor_velocidad=0.85
        self.energia-=factor_tamaño
        demora=(self.tiempo_entrega*factor_velocidad)
        return demora


### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, n,h):
        super().__init__(n)
        self.habilidad= h
        self.energia=randint(50,80)

    pass
    
    def cocinar(self,informacion_plato):#Recibe un argunemnto una lista con el nombre y tipo de plato a cocinar EJ: ["Papas Duqueza", "Comestible"] o ["Jugo Natural", "Bebestible"]
        if informacion_plato[1]=="Comestible":
            instancia=Comestible(informacion_plato[0])
            self.energia-=15
            if instancia.dificultad > self.habilidad:
                instancia.calidad *= 0.7 #Factor_Calidad
            else:
                instancia.calidad *= 1.5 #Factor_Calidad

            
        elif informacion_plato[1]=="Bebestible":
            instancia=Bebestible(informacion_plato[0])
            if instancia.tamano=="Pequeño":
                self.energia-=5
            elif instancia.tamano=="Mediano":
                self.energia-=8
            elif instancia.tamano=="Grande":
                self.energia-=10
            
            if instancia.dificultad > self.habilidad:
                instancia.calidad *= 0.7 #Factor_Calidad
            else:
                instancia.calidad *= 1.5 #Factor_Calidad
        return instancia
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, n, p):
        super().__init__(n)
        #self.platos_preferidos= random.choice(["Porotos","Lentejas","Garbanzos","Alcachofas","Frijoles"])
        #self.platos_preferidos= random.sample(INFO_PLATOS.keys(),5)
        self.platos_preferidos= p # Para probarlo se recibe un diccionario, pero en realidad recibe una lista con el nombre de los platos favoritos del cliente

    pass

    def recibir_pedido(self,pedido,demora):# pedido es una lista de objetos bebestible o comestible "En este caso retoran la instancia creada en el metodo cocinar del Cocinero"
        #Bebestible("Papas Duqueza")
        calificacion=10
        if len(pedido)< len(self.platos_preferidos) or demora >=20 :
            calificacion/=2

        """for e in pedido:
            print(e)"""

        for i in pedido:
            if i.calidad >= 11:
                calificacion += 1.5
            elif i.calidad <= 8:
                calificacion -= 3
            else:
                calificacion=calificacion  # Dar una vuelta
        return calificacion

### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA )
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
        
    except AttributeError:
       print("Algún atributo esta mal definido y/o todavia no defines una clase")
        
