#SE IMPLEMENTA CLASE QUE CREA NODOS
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#SE IMPLEMENTA CODIGO QUE REALIZA LAS OPRACIONES BASICAS DE UNA LISTA CIRCULAR
class ListaCircular():
    palabra = ''
    def __init__(self):
        self.primero = None
        self.ultimo = None

#SE VERIFICA SI LA LISTA ESTA VACIA
    def Vacia(self):
        return self.primero == None

#METODO QUE AGREGA UN ELEMENTO A LA LISTA AL PRINCIPIO DE ESTA
    def AgregarInicio(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

# METODO QUE AGREGA UN ELEMENTO A LA LISTA AL FINAL DE ESTA
    def AgregarFinal(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

# METODO QUE REMUEVE EL ELEMENTO INICIAL DE LA LISTA
    def RemoverInicio(self):
        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

# METODO QUE REMUEVE EL ELEMENTO FINAL DE LA LISTA
    def RemoverFin(self):
        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.primero = aux