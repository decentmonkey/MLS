label phone_contacts1:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts = [
        {"name": "Sophie", "caption":t_("Sophie"), "img":"/images/Phone/contacts/Contacts_Sophie.png", "visible":True}
#        {"name": "Sean", "caption":t_("Sean"), "img":"/images/Phone/contacts/Contacts_Sean.png"},
#        {"name": "Olivia", "caption":t_("Sophie"), "img":"/images/Phone/contacts/Contacts_Olivia.png"},
#        {"name": "Cynthia", "caption":t_("Cynthia"), "img":"/images/Phone/contacts/Contacts_Cynthia.png"}
    ]
    return

label phone_contacts1a_college:
#    $ phone_set_new("contacts")
    $ phone_contacts.append({"name": "College", "caption":t_("College administration"), "img":"/images/Phone/contacts/empty.png", "visible":False})
    return

label phone_contacts2:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts.append({"name": "Sean", "caption":t_("Sean"), "img":"/images/Phone/contacts/Contacts_Sean.png", "visible":True})
    return

label phone_contacts3:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts.append({"name": "Cynthia", "caption":t_("Cynthia"), "img":"/images/Phone/contacts/Contacts_Cynthia.png", "visible":True})
    return

label phone_contact4:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts.append({"name": "Whore", "caption":t_("Becky"), "img":"/images/Phone/contacts/Contacts_Whore.png", "visible":True})
    return

label phone_contact5:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts.append({"name": "Emily", "caption":t_("Emily"), "img":"/images/Phone/contacts/Contacts_Emily.png", "visible":True})
    return

label phone_contact6:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts.append({"name": "Daisy", "caption":t_("Daisy"), "img":"/images/Phone/contacts/Contacts_Daisy.png", "visible":True})
    return