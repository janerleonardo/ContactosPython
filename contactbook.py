"""
Clase ContactBook, Clase Principal y metodos de ejecucion
"""
from contact import Contact
import csv

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add (self, name, phone, email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()

    def update(self,name,phone,email):
        for index, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                self._contacts[index] = contact
                self._save()
                print('¡Actualizacion exitosa!')
                break
        else:
            print('El contacto no existe')


    def _save(self):
      try:
          with open('contacts.csv', 'w', newline='') as f:
              writer = csv.writer(f)
              writer.writerow( ('name', 'phone', 'email') )

              for contact in self._contacts:
                  writer.writerow( (contact.name, contact.phone, contact.email) )
      except:
          print('Error al crear')



    def show_all(self):
        if len(self._contacts) > 0:
            for contact in self._contacts:
                self._print_contact(contact)

            input("Enter para salir.....")
        else:
            print('No hay registros que consultar')
            input('Enter para salir .....')

    def delete(self, name):
        for index,contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[index]
                self._save()
                break
        print('Registro eliminado......')
        input('Enter para salir .....')

    def readercsv(self):
        try:
            with open('contacts.csv', 'r') as f:
                reader = csv.reader(f)
                for index, row in enumerate(reader):
                    if index == 0:
                        continue

                    self.add(name=row[0], phone=row[1],email=row[2])
        except IndexError:
            print('Error de Indice posible linea en blanca')
        except FileNotFoundError:
            print("El archivo no existe se creara uno nuevo")

    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact=contact)
                break

        else:
            print('!No se encontro¡')
            input('Enter para salir .....')



    def _print_contact(self,contact):
        print('-*-*-*-*-*-*-*-*-*-')
        print('Nombre: {} Phone: {}, Email:{}'.format(contact.name, contact.phone,contact.email))
        print('-*-*-*-*-*-*-*-*-*-')
