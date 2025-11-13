"""
Dependency Inversion Principle - Database Abstraction

>>> mysql = MySQLDatabase()
>>> mysql.connect()
'Connected to MySQL'
>>> mysql.save("user123", "Alice")
'Saved user123: Alice to MySQL'

>>> postgres = PostgreSQLDatabase()
>>> postgres.connect()
'Connected to PostgreSQL'

>>> # Test UserService with different databases
>>> service = UserService(mysql)
>>> service.save_user("user1", "Bob")
'Connected to MySQL\\nSaved user1: Bob to MySQL'

>>> service2 = UserService(postgres)
>>> service2.save_user("user2", "Charlie")
'Connected to PostgreSQL\\nSaved user2: Charlie to PostgreSQL'
"""

from abc import ABC, abstractmethod


# TODO: Zdefiniuj interfejs Database (ABC)
# Metody: connect() i save(user_id, name)

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save(self, user_id, name):
        pass


# TODO: Zaimplementuj MySQLDatabase
# Dziedziczy po Database
# Formaty: "Connected to MySQL", "Saved {user_id}: {name} to MySQL"

class MySQLDatabase(Database):
    def connect(self):
        return 'Connected to MySQL'

    def save(self, user_id, name):
        return f'Saved {user_id}: {name} to MySQL'


# TODO: Zaimplementuj PostgreSQLDatabase
# Dziedziczy po Database
# Formaty: "Connected to PostgreSQL", "Saved {user_id}: {name} to PostgreSQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return 'Connected to PostgreSQL'

    def save(self, user_id, name):
        return f'Saved {user_id}: {name} to PostgreSQL'


# TODO: Zaimplementuj UserService
# Konstruktor przyjmuje database: Database (dependency injection)
# Metoda save_user(user_id, name) używa database.connect() i database.save()

class UserService:
    def __init__(self, database: Database):
        self.database = database
    def save_user(self, user_id, name):
        r = self.database.connect() + '\n'
        r += self.database.save(user_id, name)
        return r


# DIP: High-level (UserService) zależy od abstrakcji (Database)
# Low-level (MySQLDatabase, PostgreSQL) też zależą od abstrakcji
# Możemy dodać MongoDB bez zmiany UserService!


mysql = MySQLDatabase()
mysql.connect()  # 'Connected to MySQL'
mysql.save("user123", "Alice")  # 'Saved user123: Alice to MySQL'

postgres = PostgreSQLDatabase()
postgres.connect()  # 'Connected to PostgreSQL'

# Test UserService with different databases
service = UserService(mysql)
service.save_user("user1", "Bob")  # 'Connected to MySQL\\nSaved user1: Bob to MySQL'

service2 = UserService(postgres)
service2.save_user("user2", "Charlie")  # 'Connected to PostgreSQL\\nSaved user2: Charlie to PostgreSQL'