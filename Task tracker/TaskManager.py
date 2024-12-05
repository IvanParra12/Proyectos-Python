import json
import os
from Task import Task

class TaskManager:
    
    # Constructor
    def __init__(self, ficheroTareas="tareas.json"):
        self.__ficheroTareas = ficheroTareas
        self.__tareas = []
        self.cargar_tareas()
    
    # Getters
    def get_ficheroTareas(self):
        return self.__ficheroTareas
    
    def get_tareas(self):
        return self.__tareas
        
    def cargar_tareas(self):
        # Carga las tareas desde el archivo JSON. Si no existe, crea uno vacío
        if not os.path.exists(self.__ficheroTareas):
            print(f"El archivo {self.__ficheroTareas} no existe. Creando el archivo...")  # Depuración
            with open(self.__ficheroTareas, 'w') as archivo:
                json.dump([], archivo)
            self.__tareas = []
            print(f'Archivo {self.__ficheroTareas} creado.')  # Depuración
        else:
            with open(self.__ficheroTareas, 'r') as archivo:
                try:
                    datos_tareas = json.load(archivo)
                    self.__tareas = [Task.from_dict(tarea) for tarea in datos_tareas]
                except json.JSONDecodeError:
                    self.__tareas = []
                    print(f'Archivo {self.__ficheroTareas} vacío o con formato inválido. Inicializando una lista vacía.')
    
    # Guardar tareas en el archivo JSON
    def guardar_tareas(self):
        try:
            # Convertir las tareas a diccionarios
            datos_tareas = [tarea.to_dict() for tarea in self.__tareas]
            
            # Guardar las tareas en el archivo JSON
            with open(self.__ficheroTareas, 'w') as archivo:
                json.dump(datos_tareas, archivo, indent=4)
            print(f"Tareas guardadas correctamente en {self.__ficheroTareas}")  # Depuración
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")

    # Añadir tarea
    def add_tarea(self, descripcion):
        try:
            nueva_tarea = Task(descripcion)
            self.__tareas.append(nueva_tarea)
            self.guardar_tareas()  # Guardar en el archivo JSON
            print(f'Tarea añadida correctamente! (ID: {nueva_tarea.get_id()})')
        except Exception as e:
            print(f'Error al añadir la tarea: {e}')
            
    # Actualizar tarea
    def update_tarea(self, id, nueva_descripcion):
        try:
            # Buscar la tarea por ID
            tarea = next((tarea for tarea in self.__tareas if tarea.get_id() == id), None)
            
            if not tarea:
                print(f'No se encontró la tarea con ID: {id}')
                return
            
            tarea.set_description(nueva_descripcion)
            self.guardar_tareas()  # Guardar después de la actualización
            print(f'Tarea con ID: {id} actualizada correctamente!')
        
        except Exception as e:
            print(f'Error al actualizar la tarea: {e}')