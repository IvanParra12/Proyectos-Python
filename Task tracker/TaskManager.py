import json
import os
from Task import Task

class TaskManager():
    
    def __init__(self, ficheroTareas = "tareas.json"):
        self.__ficheroTareas = ficheroTareas
        self.__tareas= []
        self.cargar_tareas()
        
    def get_ficheroTareas(self):
        return self.__ficheroTareas
    
    def get_tareas(self):
        return self.__tareas
        
    def cargar_tareas(self):
        # Carga las tareas desde el archivo JSON. Si no existe, crea uno vacío
        if not os.path.exists(self.get_ficheroTareas()):
            with open(self.get_ficheroTareas(), 'w') as archivo:
                json.dump([], archivo)
            self.get_tareas() = []
            print(f'Archivo {self.get_ficheroTareas()} creado.')
        else:
            with open(self.get_ficheroTareas(), 'r') as archivo:
                try:
                    datos_tareas = json.load(archivo)
                    self.get_tareas() = [Task.from_dict(tarea) for tarea in datos_tareas]
                except json.JSONDecodeError:
                    self.get_tareas() = []
                    print(f'Archivo {self.get_ficheroTareas()} vacío o con formato inválido. Inicializando una lista vacía.')
    
    def guardar_tareas(self):
        try:
            # Convertir la lista de tareas a una lista de diccionarios
            datos_tareas = [tarea.to_dict() for tarea in self.get_tareas()]
            
            # Guardar en el archivo JSON
            with open(self.get_ficheroTareas(), 'w') as archivo:
                json.dump(datos_tareas, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")

    
    def add_tarea(self, descripcion):
        
        try:
            nueva_tarea = Task(descripcion)
            self.get_tareas().append(nueva_tarea)
            self.guardar_tareas()
        except Exception as e:
            print(f'Error al añadir la tarea: {e}')
      
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