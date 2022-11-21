class Usuario:
    def __init__(self, nombre, apellido):
     self.nombre = nombre
     self.apellido = apellido

    def saludo(self):
        print('hola!, mi nomnbre es', self.nombre, self.apellido)



usuario = Usuario('miguel','cortes')
usuario2 = Usuario('fidalma','cortes')

usuario.saludo()
usuario2.saludo()