## Ejercicio extra: AGENDA
def agregar_contacto_a_agenda(un_nombre, un_email, una_agenda):
    una_agenda[un_nombre] = un_email
    return una_agenda

agenda = dict()
print(agenda)
agenda = agregar_contacto_a_agenda("mariano", "mariano@coder.com", agenda)
agenda = agregar_contacto_a_agenda("facundo", "facundo@coder.com", agenda)
agenda = agregar_contacto_a_agenda("mariano", "este mail es incorrecto", agenda)
print(agenda)

