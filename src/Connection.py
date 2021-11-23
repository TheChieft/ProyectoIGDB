import psycopg2

"""
Este archivo se usa para conectar python con postgreSQL, para ello se utiliza la libreria 
psycopg2 y su metodo connect con los atributos que puede ver en el metodo open Connection de la Clase Connection
"""
class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:

            """ 
            Recuerde cambiar los valores de user, password, dataabse, host y port 
            a los de su base de datos, los datos existentes son los valores ingresados
            para el funcionamiento en mi PC
            """
            self.connection = psycopg2.connect(user="postgres", #Su usuario del postgreSQL
	                                               password="postgres", #su contraseña del postgreSQL
	                                               database="DBProject", #El nombre de la base de Datos creada para que funcione el codigo
	                                               host="localhost", #el servidor/computador de conexion
	                                               port="5434") #el puerto de conexion
        except Exception as e:
            print (e) #En caso de fallar se va ver un error en la conexion

    def closeConnection(self):
        self.connection.close() #Cerrar la conexion con la base de datos
    
    def cursor(self):
        return self.connection #retornar la conexion con la base de datos
    
