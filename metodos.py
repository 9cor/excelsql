class Usuario:
    def __init__(self, nombre, apellido):
     self.nombre = nombre
     self.apellido = apellido

    def saludo(self):
        print('hola!, mi nomnbre es', self.nombre, self.apellido)


class Admin(Usuario):
    def gransaludo(self):
        print('¡hola!, soy,', self.nombre, 'y soy el administrador')

usuario = Usuario('miguel','cortes')

usuario.saludo()
usuario.nombre = 'nestor'
usuario.saludo()

admin = Admin('Maria', 'cortes')
admin.saludo()
admin.gransaludo()