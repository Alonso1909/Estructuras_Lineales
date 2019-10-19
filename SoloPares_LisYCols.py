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

#SE IMPLEMENTA EL CODIGO QUE REALIZA LAS OPERACIONES BASICAS DE UNA COLA DINAMICA
    _listaCola = []

#INSERTA UN ELEMENTO EN LA PILA
    def InsertarC(self, elemento):
        self._listaCola.append(elemento)
        return True

#QUITA UN ELEMENTO DE LA PILA (EL PRIMERO EN SER AGREGADO)
    def QuitarC(self):
        if self.ColaVacia():
            return False
        else:
            return self._listaCola.pop(0)

#SE VERIFICA SI LA COLA ESTA VACIA
    def ColaVacia(self):
        if len(self._listaCola) == 0:
            return True
        else:
            return False

#LIMPIA TODA LA COLA, ELIMINA SUS ELEMENTOS
    def LimpiarCola(self):
        self._listaCola.clear()

#IDENTIFICA EL ELEMENTO QUE ESTA EN LA CABEZA
    def MostrarFrente(self):
        return self._listaCola[0]

#IDENTIFICA EL TAMAÑO DE LA COLA
    def MostrarTamCola(self):
        return len(self._listaCola)