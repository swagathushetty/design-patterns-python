from abc import ABC,abstractmethod

#database connection
class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass 

class MySQLConnection(Connection):

    def connect(self):
        print('connecting to MySQL database........')


class PostgresSQLConnection(Connection):

    def connect(self):
        print('connecting to postgres database........')




# database cursor
class Cursor(ABC):
    @abstractmethod
    def execute(self,query:str):
        pass

class MySQLCusor(Cursor):
    def execute(self, query):
        print(f"Executing query {query} on MySQL")

class PostgresCusor(Cursor):
    def execute(self, query):
        print(f"Executing query {query} on Postgres")



class AbstractDBFactory(ABC):

    @abstractmethod
    def create_connection(self):
        pass 

    @abstractmethod
    def create_cursor(self):
        pass

class MySQLFactory(AbstractDBFactory):
    def create_connection(self):
        return MySQLConnection()
    def create_cursor(self):
        return MySQLCusor()
    
class PostgresFactory(AbstractDBFactory):
    def create_connection(self):
        return PostgresSQLConnection()
    def create_cursor(self):
        return PostgresCusor()
    

def client():
    factories = dict(mysql=MySQLFactory,postgres=PostgresFactory)

    fact_list = ", ".join(factories)

    while True:

        db = input(f"Enter database type {fact_list}  ")

        if db in factories:
            break 
        print(f"This database does not exist-- Try again.. {fact_list}")

    print("="*30)
    return factories.get(db)()

db_factory = client()
connection = db_factory.create_connection()
cursor = db_factory.create_cursor()

connection.connect()
cursor.execute("Select * from students")