class ContactList:
    contacts = []
    def __init__(self):
        pass
    def new_contact(self):
        my_contacts = {}
        my_contacts['name'] = input('Enter Name: ')
        my_contacts['phone'] = input('Enter Phone Number: ')
        
        option = int(input('How do you know this contact\n'
                       '(1) Work:\n'
                       '(2) Friend:\n'))
        if option == 1:
                my_contacts['friend_type'] = 'work'
        else:
                my_contacts['friend_type'] = 'friend'
        ContactList.contacts.append(my_contacts)

    def remove_contact(self):
        self.view_contacts()
        remove = input('Type the name you would like to delete? ')
        for x in ContactList.contacts:
            try:
                if x['name'] == remove:
                    j = ContactList.contacts.index(x)
                    ContactList.contacts.pop(j)
                else:
                    print('Cannot delete that!')
            except Exception as e:
                print(e)
    def view_contacts(self):
        if len(ContactList.contacts) == 0:
            print('No contacts!\n')
        else:
            for i in range(len(ContactList.contacts)):
                print(ContactList.contacts[i])
    def find_shared_contacts(contacts):
        if len(contacts) == 0:
            print('No contacts!\n')
        else:
            try:
                for x in contacts:
                    if x['friend_type'] == 'work':
                        for i in contacts:
                            if i['friend_type'] == 'friend' and x['name'] == i['name']:
                                print({'name': x['name'], 'phone': x['phone']})
            except Exception as e:
                print(e)
my_contact_list = ContactList()
while True:
    options = int(input('What would you like to do? \n'
                        '(1)Add a Contact\n'
                        '(2)Remove a contact\n'
                        '(3)View Contacts\n'
                        '(4)Shared Contacts\n'
                        '(-1)Exit\n'))
    if options == -1:
        break
    if options == 1:
        my_contact_list.new_contact()
    if options == 2:
        my_contact_list.remove_contact()
    if options == 3:
        my_contact_list.view_contacts()
    if options == 4:
        my_contact_list.find_shared_contacts()
