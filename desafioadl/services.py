# Importar los modelos Tarea y SubTarea de la aplicación desafioad
from desafioadl.models import Tarea, SubTarea

# Definir una función para recuperar todas las tareas y subtareas
def recupera_tareas_y_sub_tareas():
    # Obtener todas las tareas de la base de datos
    tareas = Tarea.objects.all()

    # Obtener todas las subtareas de la base de datos
    subtareas = SubTarea.objects.all()

    # Devolver un diccionario que contiene las tareas y subtareas
    return {
        "tareas": tareas,
        "subtareas": subtareas
    }

# Definir una función para crear una nueva tarea
def crear_nueva_tarea(descripcion):
    # Crear un nuevo objeto Tarea con la descripción proporcionada
    tarea = Tarea.objects.create(descripcion=descripcion)

    # Devolver el objeto tarea creado
    return tarea

def crear_subtarea(descripcion, tarea_id):
    # Buscar la tarea a la que pertenece la subtarea
    tarea = Tarea.objects.get(pk=tarea_id)

    # Crear la subtarea
    subtarea = SubTarea.objects.create(descripcion=descripcion, tarea=tarea)

    # Devolver la subtarea creada
    return subtarea

def eliminar_tarea(tarea_id):
    # Buscar la tarea a eliminar
    tarea = Tarea.objects.get(pk=tarea_id)

    # Eliminar la tarea y sus subtareas
    tarea.delete()

    # Devolver un mensaje de confirmación
    return "Tarea eliminada correctamente"           

def eliminar_subtarea(subtarea_id):
    # Buscar la subtarea a eliminar
    subtarea = SubTarea.objects.get(pk=subtarea_id)

    # Eliminar la subtarea
    subtarea.delete()

    # Devolver un mensaje
    return "Sub Tarea eliminada correctamente"


# Definir una función para imprimir tareas y subtareas en la pantalla
def imprimir_en_pantalla(tareas_y_sub_tareas):
    # Extraer las tareas y subtareas del diccionario
    tareas = tareas_y_sub_tareas["tareas"]
    subtareas = tareas_y_sub_tareas["subtareas"]

    # Iterar sobre cada tarea
    for tarea in tareas:
        # Imprimir la descripción de la tarea
        print(f"Tarea: {tarea.descripcion}")

        # Filtrar las subtareas relacionadas con la tarea actual
        related_subtareas = subtareas.filter(tarea=tarea)

        # Iterar sobre cada subtarea relacionada
        for subtarea in related_subtareas:
            # Imprimir la descripción de la subtarea con sangría
            print(f"   Subtarea: {subtarea.descripcion}")

