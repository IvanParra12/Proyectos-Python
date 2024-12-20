import json
from datetime import datetime

class Task():
    
    #Contador para el ID
    _contador_id = 0
    
    #Constructor
    def __init__(self, description, status="To do"):
        self.__id = self._incrementar_id()
        self.__description = self.validar_string(description)
        self.__status = status
        self.__createdAt = datetime.now()
        self.__updatedAt = None
        
    def __str__(self): 
        return (
            f"\nTarea con ID: {self.get_id()}\n"
            f"Descripcion: {self.get_description()}\n"
            f"Status: {self.get_status()}\n"
            f"Creado: {self.get_createdAt()}\n"
            f"Actualizado: {self.get_updatedAt()}"
        )

    #Getters
    def get_id(self):
        return self.__id
    
    def get_description(self):
        return self.__description
    
    def get_status(self):
        return self.__status
    
    def get_createdAt(self):
        return self.__createdAt
    
    def get_updatedAt(self):
        return self.__updatedAt
    
    #Setters
    def set_description(self, new_description):
        self.__description = self.validar_string(new_description)
        self.set_updatedAt()
        
    def set_status(self, new_status):
        self.__status = self.validar_string(new_status)
        self.set_updatedAt()
        
    def set_updatedAt(self):
        self.__updatedAt = datetime.now()

    @classmethod
    def _incrementar_id(cls):
        cls._contador_id += 1
        
        return cls._contador_id
    
    def to_dict(self):
        # Convertir la tarea a un diccionario, asegurándonos de que las fechas sean cadenas
        return {
            "id": self.__id,
            "description": self.__description,
            "status": self.__status,
            "created_at": self.__createdAt.strftime("%Y-%m-%d %H:%M:%S"),  # Siempre como string
            "updated_at": self.__updatedAt.strftime("%Y-%m-%d %H:%M:%S") if self.__updatedAt else "No"
        }

    @staticmethod
    def from_dict(data):
        #Crear una tarea desde diccionario
        tarea = Task(data['description'])
        tarea.__id = data['id']
        tarea.__status = data['status']
        tarea.__createdAt = datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S")  # String a datetime
        tarea.__updatedAt = datetime.strptime(data['updated_at'], "%Y-%m-%d %H:%M:%S") if data['updated_at'] != "No" else None
        return tarea

    
    #Métodos de validación
    @staticmethod
    def validar_string(valor):
        if valor.isnumeric():
            raise TypeError("La descripción o el status deben ser un string")
        
        if not valor.strip():
            raise ValueError("El valor no puede estar vacío")
        return valor
    
    @staticmethod
    def validar_id(numero):
        if not isinstance(numero, int):
            raise TypeError('Introduce un valor válido (int)')
        if numero < 0:
            raise ValueError("Introduce un id mayor o igual a 0")
        return numero