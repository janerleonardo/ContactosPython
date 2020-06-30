"""
Clase ContactBook, Clase Principal y metodos de ejecucion
"""
from contact import Contact
from twilio.rest import Client
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

    def send_message_text(self, name,message):
        account_sid = 'ACd5c58243ab007611fa74b86e5dd33c32'
        auth_token = '99472456738012b5a4244c2b873fc8ce'
        phone= ''
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                phone = contact.phone
                break

        else:
            print('!No se encontro¡')
            return
        print(phone, message)
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="{}".format(message),
            from_='+12058787187',
            to='+57{}'.format(phone)
        )

        print(message.sid)
    def send_message_whatsapp(self):
        account_sid = 'ACd6c58243ab007611fa74b86e5dd33c32'
        auth_token = '99472456738013b5a4244c2b873fc8ce'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Hello, there!',
            to='whatsapp:+573166280358'
        )

        print(message.sid)

    def _print_contact(self,contact):
        print('-*-*-*-*-*-*-*-*-*-')
        print('Nombre: {} Phone: {}, Email:{}'.format(contact.name, contact.phone,contact.email))
        print('-*-*-*-*-*-*-*-*-*-')
