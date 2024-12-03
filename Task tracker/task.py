from datetime import datetime

class Task():
    
    #Constructor
    def __init__(self, id, description, status):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__createdAt = self.set_createdAt()
        self.__updatedAt = 'No'
        
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
        
    def set_status(self, new_status):
        self.__status = self.validar_string(new_status)
        
    def set_createdAt(self):
        self.__createdAt = datetime.now()
        return f'{self.__createdAt.strftime('%H:%M:%S')}'
        
    
    def set_updatedAt(self):
        self.__updatedAt = datetime.now()
        return f'{self.__updatedAt.strftime('%H:%M:%S')}'
    
    #Métodos de validación
    @staticmethod
    def validar_string(valor):
        if valor.isnumeric():
            raise TypeError("La descripción o el status deben ser un string")
        
        if not valor.strip():
            raise ValueError("El valor no puede estar vacío")
        return valor
    
    @staticmethod
    def validar_cantidad(cantidad):
        if not isinstance(cantidad, int):
            raise TypeError('Introduce un valor válido (int)')
        if cantidad < 0:
            raise ValueError("Introduce una cantidad mayor o igual a 0")
        return cantidad