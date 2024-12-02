class Task():
    
    #Constructor
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__createdAt = createdAt
        self.__updatedAt = updatedAt
        
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
        self.__description = new_description
        
    def set_status(self, new_status):
        self.__status = new_status
        
    def set_createdAt(self, new_created_time):
        self.__createdAt = new_created_time
    
    def set_updatedAt(self, new_updated_time):
        self.__updatedAt = new_updated_time