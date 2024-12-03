from Task import Task

class TaskManager():
    
    def __init__(self) -> None:
        pass
    
    def update_status(self, command, id):
        
        # Obtenemos la tarea por ID
        tarea = self.get_id(id)
        
        if not tarea:
            print(f"No se encontró la tarea con ID {id}.")
            return

        # Mapear comandos a estados
        if command == 'mark-in-progress':
            tarea.set_status('In Progress')
        elif command == 'mark-todo':
            tarea.set_status('To do')
        elif command == 'mark-done':
            tarea.set_status('Done')
        else:
            print(f"Comando '{command}' incorrecto.")
            return

        # Mensaje de confirmación
        print(f"El estado de la tarea con ID {id} ha sido actualizado a '{tarea.get_status()}'.")