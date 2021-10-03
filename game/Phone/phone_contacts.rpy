label phone_contacts1:
    $ notif(t__("Добавлен новый контакт"))
    $ phone_set_new("contacts")
    $ phone_contacts = [
        {"name": "Sophie", "caption":t_("Sophie"), "img":"/images/Phone/contacts/Contacts_Sophie.png"}
#        {"name": "Sean", "caption":t_("Sean"), "img":"/images/Phone/contacts/Contacts_Sean.png"},
#        {"name": "Olivia", "caption":t_("Sophie"), "img":"/images/Phone/contacts/Contacts_Olivia.png"},
#        {"name": "Cynthia", "caption":t_("Cynthia"), "img":"/images/Phone/contacts/Contacts_Cynthia.png"}
    ]
    return

label phone_contacts2:
    $ phone_contacts.append({"name": "Sean", "caption":t_("Sean"), "img":"/images/Phone/contacts/Contacts_Sean.png"})
    $ phone_contacts.append({"name": "Cynthia", "caption":t_("Cynthia"), "img":"/images/Phone/contacts/Contacts_Cynthia.png"})
    return
