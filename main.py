"""
Programa para guaradar contacto en un archivo CSV, inicialmente solo guardara los contacto, segunda implementacion
que envie mensajes de whatsapp  a los contactos.
Autor: Jan3r
Date: 2020-06-25
"""
from contactbook import ContactBook
def run():
    """ Funcion que se Encarga de correr el programa """

    contactbook = ContactBook()
    contactbook.readercsv()
    while True:
        command = input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [m]Enviar Mensaje Whatsapp
            [s]alir
        ''')

        if command == 'a':
            name = input('Escribe el nombre del contacto: ')
            phone = input('Escriba el telefono: ')
            email = input('Escribe el email: ')
            contactbook.add(name=name,phone=phone,email=email)

        elif command == 'ac':
            name = input('Escribe el nombre del contacto: ')
            phone = input('Escriba el telefono: ')
            email = input('Escribe el email: ')
            contactbook.update(name=name,phone=phone,email=email)

        elif command == 'b':
            name = input('Escribe el nombre del contacto: ')
            contactbook.search(name=name)

        elif command == 'e':
            name = input('Escribe el nombre del contacto: ')
            contactbook.delete(name=name)

        elif command == 'l':
            contactbook.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
