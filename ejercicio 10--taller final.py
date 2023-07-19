import datetime

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def enviar_mensaje(self, contenido, sala):
        mensaje = Mensaje(self, contenido)
        sala.enviar_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"[{mensaje.fecha}] {mensaje.emisor.nombre}: {mensaje.contenido}")

class Mensaje:
    def __init__(self, emisor, contenido):
        self.emisor = emisor
        self.contenido = contenido
        self.fecha = datetime.datetime.now()

class SalaDeChat:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def enviar_mensaje(self, mensaje):
        for usuario in self.usuarios:
            if usuario != mensaje.emisor:
                usuario.recibir_mensaje(mensaje)

if __name__ == "__main__":
    # Crear dos usuarios
    usuario1 = Usuario(str(input("escriba el nombre del primer usuario: ")))
    usuario2 = Usuario(str(input("escriba el nombre del segundo usuario: ")))

    # Crear una sala de chat con los usuarios
    sala = SalaDeChat()
    sala.agregar_usuario(usuario1)
    sala.agregar_usuario(usuario2)

    # Simulación de conversación donde un usuario escribe y otro responde
    while True:
        mensaje_usuario1 = input(f"{usuario1.nombre}: ")
        usuario1.enviar_mensaje(mensaje_usuario1, sala)

        mensaje_usuario2 = input(f"{usuario2.nombre}: ")
        usuario2.enviar_mensaje(mensaje_usuario2, sala)

