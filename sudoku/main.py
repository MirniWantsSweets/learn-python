from funciones import Tablero

# == Variables globales =============================================
max_row_size = ...
max_col_size = ...
...

# == Funcion principal ==============================================
def main():
    # = Inicializar variables =============================
    fila = 0
    columna = 0
    valor = 0

    # = Crear y inicializar un tablero ====================
    tablero = Tablero()
    print(tablero)

    # = Preguntar posicion y valor para insertar ==========
    ...

    # == Preguntamos la fila hasta obtener un valor de fila valido
    ...

    # == Preguntamos la columna hasta obtener un valor de columna valido
    ...

    # == Preguntamos el valor hasta obtener un valor valido
    ...

    ###
    ### Llegados a este punto tenemos un tablero creado y inicializado
    ### y las variables fila, columna y valor
    ###

    # = Comprobamos que los valores introducidos se puedan meter en la tabla
    # == Comprobamos si se pueden meter en la fila
    ...

    # == Comprobamos si se pueden meter en la columna
    ...

    # == Comprobamos si se pueden meter en el cuadrado
    ...

    # = Si no es valido mostrar mensaje de error ==========
    ...

    # = Si es valido cambiar el valor de la posicion por el valor obtenido
    tablero.cambiarValor(fila, columna, valor)

# == Condicion para encender la funcion principal ===================
if __name__ == "__main__":
    main()
