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
        
        # Comandos para actualizar el estado de una tarea
        status_commands = ["mark-in-progress", "mark-todo", "mark-done"]
        for command in status_commands:
            status_parser = subparsers.add_parser(command, help=f"Marcar una tarea como {command.split('-')[-1]}")
            status_parser.add_argument("id", type=int, help="ID de la tarea a actualizar")
        
        #Comando para borrar una tarea
        delete_parser = subparsers.add_parser("delete", help="Borrar una tarea")
        delete_parser.add_argument("id", type=int, help="ID de la tarea a eliminar")
        
        #Comando para mostrar todas las tareas
        list_parser = subparsers.add_parser("list", help="Mostrar todas las tareas o filtrar por estado")
        list_parser.add_argument("status", type=str, nargs="?", default=None, help="Filtrar las tareas por estado ('done', 'todo', 'in-progress')")
        
        # Parseamos los argumentos
        args = parser.parse_args()
        self.dispatch_command(args)
        
    def dispatch_command(self, args):
        # Procesamos el comando y llamamos al método adecuado de TaskManager
        if args.command == "add":
            # Añadir tarea
            self.__task_manager.add_tarea(args.description)
        elif args.command == "update":
            # Actualizar tarea
            self.__task_manager.update_tarea(args.id, args.description)
        elif args.command in ["mark-in-progress", "mark-todo", "mark-done"]:
            # Actualizar el estado de una tarea
            self.__task_manager.update_status(args.command, args.id)
        elif args.command == "delete":
            #Borrar tarea
            self.__task_manager.borrar_tarea(args.id)
        elif args.command == "list":
            #Mostrar tareas por status
            self.__task_manager.mostrar_tareas_byStatus(args.status)
        else:
            print("Comando desconocido. Usa '--help' para ver los comandos disponibles")


# Ejecución directa del script (si se ejecuta desde la terminal)
if __name__ == "__main__":
    task_cli = TaskCLI()
    task_cli.run()