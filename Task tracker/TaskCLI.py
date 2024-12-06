import argparse
from TaskManager import TaskManager

class TaskCLI:
    
    # Constructor
    def __init__(self):
        self.__task_manager = TaskManager()  # Crear una instancia de TaskManager
    
    # Getter
    def get_task_manager(self):
        return self.__task_manager
        
    def run(self):
        # Configuración del parser de argumentos
        parser = argparse.ArgumentParser(
            description="Gestor de tareas CLI"
        )
        
        subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
        
        # Comando para añadir tareas
        add_parser = subparsers.add_parser("add", help="Añadir una nueva tarea")
        add_parser.add_argument("description", type=str, help="Descripción de la tarea")
        
        # Comando para actualizar una tarea
        update_parser = subparsers.add_parser("update", help="Actualizar una tarea")
        update_parser.add_argument("id", type=int, help="ID de la tarea a actualizar")
        update_parser.add_argument("description", type=str, help="Nueva descripción de la tarea")
        
        # Parseamos los argumentos
        args = parser.parse_args()
        self.dispatch_command(args)
        
    def dispatch_command(self, args):
        # Procesamos el comando y llamamos al método adecuado de TaskManager
        if args.command == "add":
            # Añadir tarea
            self.__task_manager.add_tarea(args.description)
        elif args.command == "update":
            # Actualizar tarea (si implementas esa funcionalidad más tarde)
            self.__task_manager.update_tarea(args.id, args.description)
        else:
            print("Comando desconocido. Usa '--help' para ver los comandos disponibles")


# Ejecución directa del script (si se ejecuta desde la terminal)
if __name__ == "__main__":
    task_cli = TaskCLI()
    task_cli.run()