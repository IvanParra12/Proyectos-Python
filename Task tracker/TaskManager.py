import json
import os
from Task import Task  # Asumimos que la clase Task está en el archivo Task.py

class TaskManager:
    def __init__(self, fichero_tareas="tareas.json"):
        self.__fichero_tareas = fichero_tareas
        self.__tareas = []
        self.crear_archivo()

    def crear_archivo(self):
        
        #Crea el archivo JSON si no existe.
        if not os.path.exists(self.__fichero_tareas):
            print(f"El archivo '{self.__fichero_tareas}' no existe. Creándolo...")
            with open(self.__fichero_tareas, 'w') as archivo:
                json.dump([], archivo)  # Inicializar con una lista vacía
            print(f"Archivo '{self.__fichero_tareas}' creado correctamente.")
        else:
            print(f"El archivo '{self.__fichero_tareas}' ya existe.")
        self.cargar_tareas()  # Cargamos las tareas existentes

    def cargar_tareas(self):
        
        #Carga las tareas desde el archivo JSON.
        try:
            with open(self.__fichero_tareas, "r") as archivo:
                datos_tareas = json.load(archivo)
                self.__tareas = [Task.from_dict(tarea) for tarea in datos_tareas]
        except json.JSONDecodeError:
            print("El archivo JSON está vacío o no tiene un formato válido. Iniciando una lista vacía.")
        except Exception as e:
            print(f"Error inesperado al cargar las tareas: {e}")

    def guardar_tareas(self):

        #Guarda las tareas en el archivo JSON.
        try:
            datos_tareas = [tarea.to_dict() for tarea in self.__tareas]
            with open(self.__fichero_tareas, 'w') as archivo:
                json.dump(datos_tareas, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")

    def add_tarea(self, descripcion):
        
        #Añade una nueva tarea con la descripción proporcionada.
        try:
            nueva_tarea = Task(descripcion)
            self.__tareas.append(nueva_tarea)
            self.guardar_tareas()
            print(f"Tarea añadida correctamente! (ID: {nueva_tarea.get_id()})")
        except Exception as e:
            print(f"Error al añadir la tarea: {e}")
            
    # Actualizar tarea
    def update_tarea(self, id, nueva_descripcion):
        try:
            # Buscar la tarea por ID
            tarea = next((tarea for tarea in self.__tareas if tarea.get_id() == id), None)
            
            if not tarea:
                print(f'No se encontró la tarea con ID: {id}')
                return
            
            tarea.set_description(nueva_descripcion)
            self.guardar_tareas()
            print(f'Tarea con ID: {id} actualizada correctamente!')
        
        except Exception as e:
            print(f'Error al actualizar la tarea: {e}')
            
    def borrar_tarea(self, id):
        try:
            # Buscar la tarea por ID
            tarea = next((tarea for tarea in self.__tareas if tarea.get_id() == id), None)
            
            if not tarea:
                print(f'No se encontró la tarea con ID: {id}')
                return
            
            self.__tareas.remove(tarea)
            self.guardar_tareas()
            print(f'Tarea con ID: {id} borrada correctamente!')
            
        except Exception as e:
            print(f'Error al eliminar la tarea: {e}')