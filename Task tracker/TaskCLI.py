import argparse
from TaskManager import TaskManager

class TaskCLI:
    
    # Constructor
    def __init__(self):
        self.__task_manager = TaskManager()
    
    # Getter
    def get_taskManager(self):
        return self.__task_manager
        
    def run(self):
        # Configuramos el parser de argumentos
        parser = argparse.ArgumentParser(
            description="Gestor de tareas CLI"
        )
        
        subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
        
        # Comando para añadir tareas
        add_parser = subparsers.add_parser("add", help="Añadir una nueva tarea")
        add_parser.add_argument("description", type=str, help="Descripción de la tarea")
        
        # Comando para actualizar una tarea
        update_parser = subparsers.add_parser("update", help="Actualiza una tarea")
        update_parser.add_argument("id", type=int, help="ID de la tarea a actualizar")
        update_parser.add_argument("description", type=str, help="Nueva descripción de la tarea")
        
        # Parseamos los argumentos
        args = parser.parse_args()
        self.dispatch_command(args)
        
    def dispatch_command(self, args):
        print(f"Comando recibido: {args.command}")  # Depuración
        # Procesa el comando y llamada al método adecuado de TaskManager
        if args.command == "add":
            self.__task_manager.add_tarea(args.description)
        elif args.command == "update":
            self.__task_manager.update_tarea(args.id, args.description)
        else:
            print("Comando desconocido. Usa '--help' para ver los comandos disponibles")