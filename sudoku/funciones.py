class Tablero:
    def __init__(self):
        "Funcion que sirve para crear y inicializar un tablero y devolverlo."
        ### Inicializar un tablero 9x9 aqui ###
        tablero = []
        #######################################
        self.tablero = tablero
    
    # == Funciones para comprobar la validez del movimiento del jugador =========================

    def compruebaFila(self, fila: int, valor: int) -> bool:
        "Funcion que comprueba si la fila especificada es valida."
        
        ### Comprovar que la fila no tenga numeros repetidos ###        
        valido = True
        ########################################################
        return valido

    def compruebaColumna(self, columna: int, valor: int) -> bool:
        "Funcion que comprueba si la columna especificada es valida."
        
        ### Comprovar que la columna no tenga valores repetidos ###
        valido = True
        ###########################################################        
        return valido

    def compruebaCuadrado(self, fila: int, columna: int, valor: int) -> bool:
        "Funcion que comprueba si el cuadrado especificado es valido."
        
        ### Comprovar que un cuadrado no tenga valores repetidos ###
        valido = True
        ############################################################        
        return valido
    
    def cambiarValor(self, fila, columna, valor) -> None:
        "Funcion que sirve para actualizar el valor de x fila y x columna"
        if fila not in range(len(self.tablero)) or columna not in range(len(self.tablero[fila])):
            raise BaseException('The specified position is out of the sudoku table.')
        
        self.tablero[fila][columna] = valor
        
    # == Funciones complementarias ==============================================================

    def __str__(self):
        "Metodo que imprime un tablero de manera bonita para jugar"
        res = "--------------------------------------------------\n"
        res += "--------------------------------------------------\n"
        need_double_line = 1
        for linea in self.tablero:
            res = res + "|| " + str(linea[0]) + " | " + str(linea[1]) + " | " + str(linea[2]) + " || " + str(linea[3]) + " | " + str(linea[4]) + " | " + str(linea[5]) + " || " + str(linea[6]) + " | " + str(linea[7]) + " | " + str(linea[8]) + " ||\n"
            res = res + "--------------------------------------------------\n"
            if need_double_line == 3:
                res = res + "--------------------------------------------------\n"
                need_double_line = 1
            else:
                need_double_line += 1
        return res