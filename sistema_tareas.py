class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True


class GestorDeTareas:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, descripcion):
        self._tareas.append(Tarea(descripcion))

    def listar_tareas(self):
        for tarea in self._tareas:
            print(f"{tarea.descripcion} - {"completada" if tarea.completada else "pendiente"}")

    def marcar_completada(self, indice):
        self._tareas[indice].completar()

    def total_pendientes(self):
        pendientes = 0
        for tarea in self._tareas:
            if not tarea.completada:
                pendientes += 1
        return pendientes


gestor = GestorDeTareas()
gestor.agregar_tarea("Enviar el reporte semanal a Contabilidad")
gestor.agregar_tarea("Pagar a los proveedores del comedor")
gestor.marcar_completada(0)
gestor.listar_tareas()
print("Pendientes:", gestor.total_pendientes())