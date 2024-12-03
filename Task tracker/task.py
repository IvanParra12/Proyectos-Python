from datetime import datetime

class Task():
    
    #Constructor
    def __init__(self, description):
        self.__id = self.set_id()
        self.__description = self.validar_string(description)
        self.__status = self.set_status()
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
    def set_id(self):
        self.__id += 1
        
    def set_description(self, new_description):
        self.__description = self.validar_string(new_description)
        
    def set_status(self, command, id):
        
        # Obtenemos la tarea por ID
        tarea = self.get_id(id)
        
        if not tarea:
            print(f"No se encontró la tarea con ID {id}.")
            return

        # Mapear comandos a estados
        if command == 'mark-in-progress':
            tarea['status'] = 'In Progress'
        elif command == 'mark-todo':
            tarea['status'] = 'To do'
        elif command == 'mark-done':
            tarea['status'] = 'Done'
        else:
            print(f"Comando '{command}' incorrecto.")
            return

        # Mensaje de confirmación
        print(f"El estado de la tarea con ID {id} ha sido actualizado a '{tarea['status']}'.")
            
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
    def validar_id(numero):
        if not isinstance(numero, int):
            raise TypeError('Introduce un valor válido (int)')
        if numero < 0:
            raise ValueError("Introduce un id mayor o igual a 0")
        return numero