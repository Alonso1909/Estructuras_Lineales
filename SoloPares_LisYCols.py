class ObtenerPares:

#SE IMPLEMENTA EL CODIGO QUE REALIZA LAS OPERACIONES BASICAS DE UNA PILA DINAMICA
    __listaPila = []

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

#SE IMPLEMENTA LA PARTE DEL CODIGO DONDE SE ENCONTRARAN LOS PARES Y SE IRAN AGREGANDO

#METODO QUE MUESTRA LOS ELEMENTOS AGREGADOS A LA LISTA PILA
    def ElementosPila(self):
        return self.__listaPila

#METODO QUE MUESTRA LOS ELEMENTOS AGREGADOS A LA LISTA COLA
    def ElementosCola(self):
        return self._listaCola

#IDENTIFICA LOS ELEMENTOS PARES DE LA LISTA PILA
# Y LOS QUE SEAN LOS AGREGA A LA LISTA COLA
    def EncontrarPares(self):
        for a in range (0,len(self.__listaPila)):
            if int(self.__listaPila[a] % 2) == 0:
                self.InsertarC(self.__listaPila[a])

DepyPru = ObtenerPares()
elementos = [1,2,3,4,5,6,7,8,9]
for e in range (0,len(elementos)):
    DepyPru.InsertarP(elementos[e])
DepyPru.EncontrarPares()
print('Los elementos en la pila son: ',DepyPru.ElementosPila())
print('Los elementos pares de la pila en la cola son: ',DepyPru.ElementosCola())