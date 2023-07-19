class Tarea:
    def __init__(self, nombre, valor, horas_estimadas):
        self.nombre = nombre
        self.valor = valor
        self.horas_estimadas = horas_estimadas

class Empleado:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

    def asignar_salario(self, horas_trabajadas, salario_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.salario_por_hora = salario_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.salario_por_hora

    def __str__(self):
        return f"{self.nombre} en '{self.departamento}' trabajó {self.horas_trabajadas} horas y ganó {self.calcular_salario()}."

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.tareas = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)

    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)

    def __str__(self):
        return f"Departamento: {self.nombre}"

def mostrar_empleados_por_departamento(departamento):
    print(departamento)
    if not departamento.empleados:
        print("No hay empleados en este departamento.")
    else:
        for empleado in departamento.empleados:
            print(empleado)

if __name__ == "__main__":
    departamentos = ["Desarrollo", "Recursos Humanos", "Ventas", "Contabilidad"]
    empleados = []

    while True:
        print("\n1. Agregar empleado")
        print("2. Asignar tarea a departamento")
        print("3. Informe de empleados por departamento")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre_empleado = input("Ingrese el nombre del empleado: ")
            print("Departamentos disponibles:")
            for i, depto in enumerate(departamentos, 1):
                print(f"{i}. {depto}")

            num_departamento = int(input("Ingrese el número del departamento para el empleado (1-{}): ".format(len(departamentos))))
            if 1 <= num_departamento <= len(departamentos):
                departamento_elegido = departamentos[num_departamento - 1]
                nuevo_empleado = Empleado(nombre_empleado, departamento_elegido)

                horas_trabajadas = float(input("Ingrese las horas trabajadas por el empleado: "))
                salario_por_hora = float(input("Ingrese el salario por hora del empleado: "))

                nuevo_empleado.asignar_salario(horas_trabajadas, salario_por_hora)

                departamento = Departamento(departamento_elegido)
                departamento.contratar_empleado(nuevo_empleado)
                empleados.append(nuevo_empleado)

        elif opcion == 2:
            if not departamentos:
                print("No hay empleados asignados a departamentos.")
                continue

            print("\nDepartamentos disponibles:")
            for i, depto in enumerate(departamentos, 1):
                print(f"{i}. {depto}")

            num_departamento = int(input("Ingrese el número del departamento para asignar la tarea (1-{}): ".format(len(departamentos))))
            if 1 <= num_departamento <= len(departamentos):
                departamento_elegido = departamentos[num_departamento - 1]
                tarea_nombre = input("Ingrese el nombre de la tarea: ")
                tarea_valor = float(input("Ingrese el valor de la tarea: "))
                tarea_horas = float(input("Ingrese las horas estimadas para la tarea: "))

                tarea = Tarea(tarea_nombre, tarea_valor, tarea_horas)
                departamento = Departamento(departamento_elegido)
                departamento.asignar_tarea(tarea)

        elif opcion == 3:
            if not departamentos:
                print("No hay empleados asignados a departamentos.")
            else:
                print("\nDepartamentos disponibles:")
                for i, depto in enumerate(departamentos, 1):
                    print(f"{i}. {depto}")

                num_departamento = int(input("Ingrese el número del departamento para ver el informe (1-{}): ".format(len(departamentos))))
                if 1 <= num_departamento <= len(departamentos):
                    departamento_elegido = departamentos[num_departamento - 1]
                    departamento = Departamento(departamento_elegido)
                    mostrar_empleados_por_departamento(departamento)

        elif opcion == 4:
            break

        else:
            print("Opción inválida. Intente nuevamente.")

