from abc import ABC,abstractmethod



class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass 


class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to MySQL database............."
    

class PostgresSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgresSQL database........."
    

class OracleSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to OracleSQL database........." 

class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self)->DatabaseConnection:
        pass

class MySQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self):
        return MySQLConnection()
    
class postgresConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self):
        return PostgresSQLConnection()
        
class OracleConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self):
        return OracleSQLConnection()
    


class DatabaseFactory:
    def __init__(self):
        self.factory = dict(mysql=MySQLConnection,postgresSQL=PostgresSQLConnection,oracleSQL=OracleSQLConnection)

    def create_connection(self,db_name:str):
        if db_name in self.factory:
            connection = self.factory.get(db_name)()
            return connection
        
db_factory = DatabaseFactory()

my_sql = db_factory.create_connection('mysql')
print(my_sql.connect())