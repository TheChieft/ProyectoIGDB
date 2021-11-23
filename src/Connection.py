import psycopg2

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
	                                               password="postgres",
	                                               database="DBProject",
	                                               host="localhost",
	                                               port="5434")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()
    
    def cursor(self):
        return self.connection
    
