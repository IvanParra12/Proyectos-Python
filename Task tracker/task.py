class Task():
    
    #Constructor
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__createdAt = createdAt
        self.__updatedAt = updatedAt