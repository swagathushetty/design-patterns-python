from abc import ABC,abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self,message):
        pass

class ConsoleLogger(Logger):
    def log(self,message):
        print(f"[ConsoleLogger] {message}")

class FileLogger(Logger):
    def log(self,message):
        with open("log.txt","a") as file:
            file.write(f"[FileLogger] {message}")

class DatabaseLogger(Logger):
    def log(self,message):
        #implement database logic
        print(f"[DatabaseLogger] {message}")

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self)->Logger:
        pass 

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self)->Logger:
        return ConsoleLogger()

class FileLoggerFactory(LoggerFactory):
    def create_logger(self)->Logger:
        return FileLoggerFactory()

class DatabaseLoggerFactory(LoggerFactory):
    def create_logger(self)->Logger:
        return DatabaseLogger()