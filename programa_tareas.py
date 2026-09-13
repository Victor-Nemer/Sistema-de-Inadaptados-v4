# RETO 2.1 — EL REFACTOR REAL
# Regla del reto: la clase debe producir EXACTAMENTE el mismo output que
# programa_tareas.py con los mismos datos de entrada.

class Tarea:
  def __init__(self, descripcion):
      # TODO 1: guarda como atributos de self lo mismo que ponía crear_tarea():
      #         la descripción que llega, y completada en False.
     self.descripcion = descripcion
     self.completada = False

  def completar(self):
      # TODO 2: haz lo mismo que completar_tarea(tarea), pero sobre self.
      self.completada = True

  def mostrar(self):
      # TODO 3: imprime "<descripcion> - <estado>", igual que mostrar_tarea(tarea),
      #         donde el estado es "completada" o "pendiente".
      print(f"{self.descripcion} - {"Completado" if self.completada else "Incompleto"}")


# No modifiques de aquí para abajo — es la prueba de paridad de Ximena.
tarea = Tarea("Subir el DoD del sprint")
tarea.mostrar()
tarea.completar()
tarea.mostrar()

# TODO 4: escribe en un comentario, en una línea, qué comportamiento verificaste
#         que sigue siendo idéntico al de programa_tareas.py.


#Es identico en el resultado, pero en este esta mas ordenado, y no tenemos que pasar todo el rato los parametros
