class ObtenerPares:

#SE IMPLEMENTA EL CODIGO QUE REALIZA LAS OPERACIONES BASICAS DE UNA PILA DINAMICA
    __listaPila = []

    def __init__(self):
        self.__listaPila = []

#INSERTA UN ELEMENTO EN LA PILA
    def InsertarP(self, elemento):
        self.__listaPila.append(elemento)

#SE VERIFICA SI LA PILA ESTA VACIA
    def PilaVacia(self):
        if len(self.__listaPila) == 0:
            return True
        else:
            return False
#QUITA UN ELEMENTO DE LA PILA (EL ULTIMO EN SER AGREGADO)
    def QuitarP(self):
        if self.PilaVacia():
            return False
        else:
            elemento = self.__listaPila.pop()
            return elemento

#LIMPIA TODA LA PILA, ELIMINA SUS ELEMENTOS
    def limpiarPila(self):
        self.__listaPila.clear()

#INDICA EL TAMAÑO DE LA PILA
    def tamPila(self):
        return len(self.__listaPila)