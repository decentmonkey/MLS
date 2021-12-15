default phone_max_typing_time = 3.0
default phone_default_image_typing_time = 2.0
default phone_pause_before_typing_time = 1.0
default phone_buttons_list = []
default phone_buttons_new = {}
default phone_menu_active = "main"
default phone_chat_history = []
default phone_chat_history_new_flags = {}
default phone_contact = False
default phone_current_chat = []
default phone_current_chat_name = False
default phone_typing = False
default phone_typing_name = False
default phone_close_enabled = True
default phone_live_chat_closing = False
default phone_gallery = []
default phone_gallery_page = 0
default phone_gallery_items_on_page = 10
default phone_gallery_delete_mode = False
default phone_last_contacts_count = 0
default phone_orientation = 0
default phone_camera_image = False
default phone_background = 0
default phone_backgrounds_list = []
default phone_preferences_list = []
default phone_instagram_posts = []
default phone_instagram_posts_multi = {}
default phone_instagram_current_name = False
default phone_instagram_new = []
default phone_instagram_mode = 0
default phone_inited = False
default phone_notes_text = ""
default camera_enabled = True
default camera_icon_enabled = True
default phoneNewForced = False
default phone_incoming_call_active = False
default phone_incoming_call_name = False
default phone_icon_flashing = False

#history:
# [{"chat_name":name, "contact_name":contact_name, "chat_content":[]}]
# chat format:
# ["speaker", "message", pause]

# phone_focus_icon(True/False) - фокусировка на иконке телефона, new message if true
# phone_incoming_call(contact_name) - фокусировка на иконке телефона, начало чата при открытии

# phone_add_history(chat_name, contact_name, chat_list)
# phone_set_new(menu_name)

# call phone_open() - открывается на главном меню
# call phone_open_menu(menu_name) - открывается на определенном меню
# call phone_hide() - закрывается
# call phone_camera_open() - открывается в режиме камеры

# add_hook("phone_open", "", scene="phone") - open phone
# add_hook("phone", "", scene="phone") - every phone iteration
# add_hook("phone_close", "", scene="phone") - close phone

# add_hook("contacts", "", scene="phone") - open contacts
# add_hook("before_call_contact", "", scene="phone")
# add_hook("call_contact", "", scene="phone")
# add_hook("open_history_chat", "", scene="phone")
# add_hook("open_gallery_image", "", scene="phone")

# add_hook("messages", "", scene="phone") - open messages
# add_hook("gallery", "", scene="phone") - open gallery
# add_hook("camera", "", scene="phone") - open camera in scene
# add_hook("camera_shoot", "", scene="phone") - shoot camera in scene

# add_hook("preferences", "", scene="phone") - open preferences
# add_hook("preferences_rrmeter", "", scene="phone")
# add_hook("preferences_backgrounds", "", scene="phone")
# add_hook("preferences_backgrounds_select", "", scene="phone")

# add_hook("instagram", "", scene="phone") - open instagram
# add_hook("notes", "", scene="phone") - open notes



label phone_open:
    $ phoneNewForced = False
    $ phone_icon_flashing = False
    if phone_incoming_call_active == True:
        $ phone_incoming_call_active = False
        jump phone_incoming_call
    hide screen phone_icon_focus
    sound metal_slide
    if phone_inited == False:
        call phone_init() from _rcall_phone_init
        call phone_contacts1() from _rcall_phone_contacts1
    call process_hooks("phone_open", "phone") from _rcall_process_hooks_21
    $ phone_menu_active = "main"
    $ phone_orientation = 0
    call phone_controller() from _rcall_phone_controller
    return

label phone_open_menu(menu_active):
    hide screen phone_icon_focus
    $ phoneNewForced = False
    $ phone_icon_flashing = False
    if phone_inited == False:
        call phone_init() from _rcall_phone_init_1
        call phone_contacts1() from _rcall_phone_contacts1_1
    call process_hooks("phone_open", "phone") from _rcall_process_hooks_22
#    $ phone_menu_active = "main"
    $ phone_menu_active = menu_active
    $ phone_orientation = 0
    call phone_controller() from _rcall_phone_controller_1
    return

label phone_incoming_call:
    hide screen phone_icon_focus
    $ phone_orientation = 0
    $ obj_name = phone_incoming_call_name
    $ phone_contact = phone_get_contact_by_contact_name(obj_name)
    $ phone_menu_active = "calling_screen"
    call process_hooks("before_call_contact", "phone") from _rcall_process_hooks_23
    if _return == False:
        $ phone_menu_active = "main"
        jump phone_open_loop1

    show screen phone(phone_menu_active)
    sound snd_phone_notification1
#    pause
    pause 1.0
    $ phone_menu_active = "chat_live"
    $ phone_current_chat = []
    call process_hooks("call_contact", "phone") from _rcall_process_hooks_24
    if _return == False:
        $ phone_menu_active = "main"
        jump phone_open_loop1
    sound snd_phone_notification5
    call process_hooks("call_contact_end", "phone") from _rcall_process_hooks_25
    jump phone_open_loop1

label phone_hide:
    hide screen phone
    return

#label phone_camera_open:
#    sound camera_lens1
#    $ phone_menu_active = "camera"
#    $ phone_orientation = 1
#    $ phone_camera_image = phone_camera_get_current_image()
#    show screen phone_camera_screen2(phone_camera_image)
#label phone_camera_open_loop1:
#    $ interact_data = None
#    $ interact_data = ui.interact()
#    if interact_data != None and interact_data != False:
#        if interact_data[0] == "close":
#            hide screen phone_camera_screen2
#            return
#        if interact_data[0] == "camera_shoot":
#            python:
#                if phone_camera_image in phone_gallery:
#                    phone_gallery.remove(phone_camera_image)
#                phone_gallery.insert(0, phone_camera_image)
##            m "shoot!"
#            hide screen phone_camera_screen2
#            return
#    jump phone_camera_open_loop1

label phone_init:
    $ phone_buttons_new = {
        "contacts": False,
        "messages": False,
        "gallery": False,
        "notes": False,
        "camera": False,
        "instagram": False,
        "preferences": False
    }
    $ phone_buttons_list = [
        {"name": "contacts", "caption": "Contacts", "img":"/images/Phone/icons/contacts.png", "img_new":"/images/Phone/icons/contacts_new.png", "active":True},
        {"name": "messages", "caption": "Messages",  "img":"/images/Phone/icons/messager.png", "img_new":"/images/Phone/icons/messager_new.png", "active":True},
        {"name": "gallery", "caption": "  Photos",  "img":"/images/Phone/icons/gal.png", "img_new":"/images/Phone/icons/gal_new.png", "active":True},
        {"name": "notes", "caption": "  Notes",  "img":"/images/Phone/icons/notes.png", "img_new":"/images/Phone/icons/notes_new.png", "active":True},
        {"name": "camera", "caption": "  Camera",  "img":"/images/Phone/icons/photo.png", "img_new":"/images/Phone/icons/photo_new.png", "active":True},
        {"name": "instagram", "caption": " Instagram",  "img":"/images/Phone/icons/instagram.png", "img_new":"/images/Phone/icons/instagram_new.png", "active":True},
        {"name": "preferences", "caption": "Preferences",  "img":"/images/Phone/icons/preferens.png", "img_new":"/images/Phone/icons/preferens_new.png", "active":True}
#        {"name": "contacts", "caption": t_("Контакты"), "img":"/images/Phone/icons/contacts.png", "img_new":"/images/Phone/icons/contacts_new.png", "active":True},
#        {"name": "messages", "caption": t_("Сообщения"),  "img":"/images/Phone/icons/messager.png", "img_new":"/images/Phone/icons/messager_new.png", "active":True},
#        {"name": "gallery", "caption": t_("Галерея"),  "img":"/images/Phone/icons/gal.png", "img_new":"/images/Phone/icons/gal_new.png", "active":True},
#        {"name": "notes", "caption": t_("Блокнот"),  "img":"/images/Phone/icons/notes.png", "img_new":"/images/Phone/icons/notes_new.png", "active":True},
#        {"name": "camera", "caption": t_("Камера"),  "img":"/images/Phone/icons/photo.png", "img_new":"/images/Phone/icons/photo_new.png", "active":True},
#        {"name": "instagram", "caption": t_("Инстаграм"),  "img":"/images/Phone/icons/instagram.png", "img_new":"/images/Phone/icons/instagram_new.png", "active":True},
#        {"name": "preferences", "caption": t_("Настройки"),  "img":"/images/Phone/icons/preferens.png", "img_new":"/images/Phone/icons/preferens_new.png", "active":True}
    ]
    $ phone_preferences_list = [
        {"name":"preferences_rrmeter", "caption": t_("RR Meter")},
        {"name":"preferences_backgrounds", "caption": t_("Изменить фон")}
    ]
    $ phone_backgrounds_list = [
        "/images/Phone/bg_1.png",
        "/images/Phone/option/bg_2.png"
    ]
    $ phone_inited = True

    return

label phone_controller:

label phone_open_loop1:
    window hide
    call remove_dialogue() from _rcall_remove_dialogue_1
    hide screen phone_icon_focus

    python:
        # check new history messages
        for history_flag in phone_chat_history_new_flags:
            if phone_chat_history_new_flags[history_flag] == True:
                phone_buttons_new["messages"] = True
            else:
                phone_buttons_new["messages"] = False

        # check new contacts
        if phone_last_contacts_count != len(phone_contacts):
            phone_buttons_new["contacts"] = True
        else:
            phone_buttons_new["contacts"] = False

    if phone_menu_active != "camera":
        show screen phone(phone_menu_active)

    call process_hooks("phone", "phone") from _rcall_process_hooks_26
    if phone_menu_active == "instagram":
        if phone_instagram_mode == 0:
            call process_hooks("instagram", "phone") from _rcall_process_hooks_27
    if phone_menu_active == "instagram_page":
        call process_hooks("instagram", "phone") from _rcall_process_hooks_52

    if phone_menu_active == "notes":
        call process_hooks("notes", "phone") from _rcall_process_hooks_28

    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data != None and interact_data != False:
        if interact_data[0] == "click_main_icon":
            if interact_data[1] == "contacts":
                sound phone_click
                call process_hooks("contacts", "phone") from _rcall_process_hooks_29
                $ phone_menu_active = "contacts"
                $ phone_last_contacts_count = len(phone_contacts)
#                $ phone_buttons_new["contacts"] = False
                jump phone_open_loop1
            if interact_data[1] == "messages":
                sound phone_click
                call process_hooks("messages", "phone") from _rcall_process_hooks_30
#                $ phone_buttons_new["messages"] = False
                $ phone_menu_active = "messages_list"
                jump phone_open_loop1
            if interact_data[1] == "gallery":
                sound phone_click
                call process_hooks("gallery", "phone") from _rcall_process_hooks_31
                $ phone_menu_active = "gallery"
                $ phone_gallery_page = 0
                $ phone_gallery_delete_mode = False
                jump phone_open_loop1
            if interact_data[1] == "camera":
                sound camera_lens1
                call process_hooks("camera", "phone") from _rcall_process_hooks_32
                $ phone_menu_active = "camera"
                $ phone_orientation = 1
                $ phone_camera_image = phone_camera_get_current_image()
                $ phone_camera_image_path = phone_get_gallery_image_path(phone_camera_image)
                $ phone_camera_scene_data = get_camera_scene_shoot_data()
                $ phone_camera_image_combined = draw_camera_scene_shoot_data(phone_camera_image_path, phone_camera_scene_data)
#                hide screen phone
#                show screen phone_camera_screen()
                show screen phone_camera_screen(phone_camera_image_combined)
                jump phone_open_loop1
            if interact_data[1] == "preferences":
                sound phone_click
                call process_hooks("preferences", "phone") from _rcall_process_hooks_33
                $ phone_menu_active = "preferences_menu"
                jump phone_open_loop1
            if interact_data[1] == "instagram":
                sound phone_click
                $ phone_buttons_new["instagram"] = False
                $ phone_menu_active = "instagram"
                jump phone_open_loop1
            if interact_data[1] == "notes":
                sound phone_click
                $ phone_buttons_new["notes"] = False
                $ phone_menu_active = "notes"
                call show_questlog() from _rcall_show_questlog
                $ phone_notes_text = _return
                if phone_notes_text == "":
                    $ phone_notes_text = ":-)"

                jump phone_open_loop1

        if interact_data[0] == "close":
            if phone_menu_active == "main":
                sound vjuh3
                hide screen phone
                hide screen phone_chat_live_screen
                call process_hooks("phone_close", "phone") from _rcall_process_hooks_34
                return
            if phone_menu_active == "chat_live":
                sound vjuh3
                hide screen phone
                hide screen phone_chat_live_screen
#                pause 0.5
                call process_hooks("call_contact_end_close", "phone") from _rcall_process_hooks_35
                call process_hooks("phone_close", "phone") from _rcall_process_hooks_36
                return


            if phone_menu_active == "contacts" or phone_menu_active == "preferences_menu" or phone_menu_active == "preferences_backgrounds" or phone_menu_active == "instagram" or phone_menu_active == "notes" or phone_menu_active=="preferences_rrmeter":
                sound phone_click
                $ phone_menu_active = "main"
                jump phone_open_loop1
            if phone_menu_active == "messages_list":
                sound phone_click
                $ phone_menu_active = "main"
                jump phone_open_loop1
            if phone_menu_active == "open_history_chat":
                sound phone_click
                $ phone_menu_active = "messages_list"
                jump phone_open_loop1
            if phone_menu_active == "gallery":
                sound phone_click
                $ phone_menu_active = "main"
                jump phone_open_loop1
            if phone_menu_active == "instagram_page":
                sound phone_click
                $ phone_menu_active = "instagram"
                jump phone_open_loop1

            if phone_menu_active == "camera":
                sound vjuh3
                hide screen phone_camera_screen
                call process_hooks("phone_close", "phone") from _rcall_process_hooks_37
                return
#                $ phone_menu_active = "main"
#                jump phone_open_loop1


        if interact_data[0] == "call_contact":
            sound phone_click
            $ obj_name = interact_data[1]
            $ phone_contact = interact_data[2]
            $ phone_menu_active = "calling_screen"
            call process_hooks("before_call_contact", "phone") from _rcall_process_hooks_38
            if _return == False:
                $ phone_menu_active = "main"
                jump phone_open_loop1

            show screen phone(phone_menu_active)
            pause 0.5
            sound snd_phone1
            pause 2.0
            $ phone_current_chat = []
            call process_hooks("call_contact", "phone") from _rcall_process_hooks_39
            if _return == False:
                $ phone_menu_active = "main"
                jump phone_open_loop1
            sound snd_phone_notification5
            jump phone_open_loop1

        if interact_data[0] == "open_history_chat":
            sound phone_click
            if phone_chat_history_new_flags.has_key(interact_data[2]["chat_name"]):
                $ phone_chat_history_new_flags[interact_data[2]["chat_name"]] = False
            $ phone_contact = phone_get_contact_by_contact_name(interact_data[1])
            $ phone_current_chat = interact_data[2]["chat_content"]
            $ phone_menu_active = "open_history_chat"
            call process_hooks("open_history_chat", "phone") from _rcall_process_hooks_42
            jump phone_open_loop1

        if interact_data[0] == "gallery_pagination":
            sound phone_click
            if interact_data[1] == "left" and phone_gallery_page > 0:
                $ phone_gallery_page -= 1
            if interact_data[1] == "right" and len(phone_gallery) - (phone_gallery_page+1)*phone_gallery_items_on_page > 0:
                $ phone_gallery_page += 1
            jump phone_open_loop1

        if interact_data[0] == "open_gallery_image":
            sound phone_click
            $ galleryImageCombined = False
            $ galleryImagePath = phone_get_gallery_image_path(phone_gallery[interact_data[1]][0])

            call process_hooks("open_gallery_image", "phone") from _rcall_process_hooks_43
            if galleryImagePath != False:
                show screen phone_gallery_image_screen(galleryImagePath, phone_gallery[interact_data[1]][1])
#                with fade
                pause
                sound keyboard_click
                hide screen phone_gallery_image_screen
            jump phone_open_loop1

        if interact_data[0] == "preferences_rrmeter":
            sound phone_click
            $ phone_menu_active = "preferences_rrmeter"
            call process_hooks("preferences_rrmeter", "phone") from _rcall_process_hooks_44
            jump phone_open_loop1

        if interact_data[0] == "preferences_backgrounds":
            sound phone_click
            $ phone_menu_active = "preferences_backgrounds"
            call process_hooks("preferences_backgrounds", "phone") from _rcall_process_hooks_45
            jump phone_open_loop1

        if interact_data[0] == "preferences_backgrounds_select":
            sound phone_click
            $ phone_background = interact_data[1]
            $ phone_menu_active = "main"
            call process_hooks("preferences_backgrounds_select", "phone") from _rcall_process_hooks_46
            jump phone_open_loop1

        if interact_data[0] == "open_instagram_page":
            sound phone_click
            $ phone_menu_active = "instagram_page"
            $ phone_instagram_current_name = interact_data[1]
            python: # remove notif new
                while phone_instagram_current_name in phone_instagram_new: phone_instagram_new.remove(phone_instagram_current_name)
            jump phone_open_loop1


        if interact_data[0] == "camera_shoot":
            call process_hooks("camera_shoot", "phone") from _rcall_process_hooks_47
            if _return == False:
                return
            python:
#                for idx in range(len(phone_gallery)-1,-1,-1):
#                    if phone_gallery[idx][0] == phone_camera_image:
#                        del phone_gallery[idx]
#                if phone_camera_image in phone_gallery:
#                    phone_gallery.remove(phone_camera_image)
                phone_gallery.insert(0, [phone_camera_image, get_camera_scene_shoot_data()])
                if len(phone_gallery) >= 30:
                    steam_achievement("ach_photo1")
                if len(phone_gallery) >= 60:
                    steam_achievement("ach_photo2")
#                print get_camera_scene_shoot_data()
            call photoshop_flash() from _rcall_photoshop_flash
#            pause 0.2
            hide screen phone_camera_screen
            call process_hooks("phone_close", "phone") from _rcall_process_hooks_48
            return


    jump phone_open_loop1

label phone_chat(chat):
    window hide
    call remove_dialogue() from _rcall_remove_dialogue_2
    $ phone_menu_active = "chat_live"
    $ chat_line_idx = 0
    $ phone_close_enabled = False
    $ phone_live_chat_closing = False
    hide screen phone_icon_focus
    show screen phone(phone_menu_active)
label phone_chat_loop1:
    $ chat_line = chat[chat_line_idx]
    python:
        if chat_line[1] != "image":
            message_pause = float(len(chat_line[1])) * 0.1
        else:
            message_pause = phone_default_image_typing_time
        if message_pause > phone_max_typing_time:
            message_pause = phone_max_typing_time
        if len(chat_line) > 2 and chat_line[1] != "image":
            message_pause = float(chat_line[2])
        if len(chat_line) > 3 and chat_line[1] == "image":
            message_pause = float(chat_line[3])

        if chat_line_idx == 0 and chat_line[0] != "" and chat_line[0] != "bardie" and chat_line[0] != "bardie_t":
            message_pause = 0.3
        phone_typing = True

        last_dialogue_character = chat_line[0]
        if last_dialogue_character == "":
            last_dialogue_character = "bardie"

    if chat_line[0] == "" or chat_line[0] == "bardie" or chat_line[0] == "bardie_t":
        sound iphone_typing
        $ phone_typing_name = "[mcname]"
        pass
    else:
        $ phone_typing_name = phone_contact["caption"]
    hide screen phone_chat_live_screen
    show screen phone_chat_live_screen()
    pause float(message_pause)
    if chat_line[0] != "" and chat_line[0] != "bardie" and chat_line[0] != "bardie_t":
#        sound iphone_text_message2
        sound snd_phone_notification2
        pass
    else:
        sound snd_phone_notification3
    $ phone_typing = False
    $ phone_current_chat.append(chat_line)
    $ phone_add_history_line(phone_current_chat_name, chat_line)

    hide screen phone_chat_live_screen
    show screen phone_chat_live_screen()
    pause float(phone_pause_before_typing_time)
    $ chat_line_idx += 1
    if chat_line_idx < len(chat):
        jump phone_chat_loop1

    $ phone_close_enabled = True
    return
label phone_chat_loop2:
    show screen phone(phone_menu_active)
    call process_hooks("call_contact_end", "phone") from _rcall_process_hooks_49
    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data != None and interact_data != False:
        if interact_data[0] == "close":
            $ phone_live_chat_closing = True
            hide screen phone
            hide screen phone_chat_live_screen
            call process_hooks("call_contact_end_close", "phone") from _rcall_process_hooks_50
            return
    jump phone_chat_loop2
    return

label phone_chat_menu(chat_menu):
    $ phone_close_enabled = False
    $ last_dialogue_character = "bardie"
    call screen phone_live_chat_menu_screen(chat_menu)
    $ phone_close_enabled = True
    return _return


init python:
    def phone_incoming_call(call_name):
        global phoneNewForced, phone_incoming_call_active, phone_incoming_call_name, phone_icon_flashing
        phone_incoming_call_name = call_name
        phone_incoming_call_active = True
        phoneNewForced = True
        phone_icon_flashing = True
#        renpy.play("/Sounds/iphone_text_message1.ogg")
        renpy.play("/Sounds/snd_phone_notification4.ogg")
        notif(t_("Новое сообщение!"))
        renpy.show_screen("phone_icon_focus")
        return

    def phone_focus_icon(new_message = False):
        global phoneNewForced, phone_icon_flashing
        if new_message == True:
            phoneNewForced = True
            phone_icon_flashing = True
            #renpy.play("/Sounds/iphone_text_message1.ogg")
            renpy.play("/Sounds/snd_phone_notification4.ogg")
            notif(t_("Новое сообщение!"))
        renpy.show_screen("phone_icon_focus")
        return

    def phone_start_new_chat(chat_name, contact_name):
        global phone_chat_history, phone_current_chat_name
        for idx in range(len(phone_chat_history)-1, -1, -1):
            if phone_chat_history[idx]["chat_name"] == chat_name:
                # нашли такой же чат, удаляем
                del phone_chat_history[idx]
        new_chat = {"chat_name": chat_name, "contact_name": contact_name, "chat_content":[]}
        phone_chat_history.insert(0, new_chat)
        phone_current_chat_name = chat_name
        return

    def phone_add_history_line(chat_name, chat_line):
        global phone_chat_history
        for idx in range(0, len(phone_chat_history)):
            if phone_chat_history[idx]["chat_name"] == chat_name:
                phone_chat_history[idx]["chat_content"].append(chat_line)
        return

    def phone_add_history(chat_name, contact_name, chat_list):
        global phone_chat_history, phone_chat_history_new_flags
        for idx in range(len(phone_chat_history)-1, -1, -1):
            if phone_chat_history[idx]["chat_name"] == chat_name:
                # нашли такой же чат, удаляем
                del phone_chat_history[idx]
        renpy.play("/Sounds/snd_phone_notification4.ogg")
        notif(t_("Новое сообщение!"))
        new_chat = {"chat_name": chat_name, "contact_name": contact_name, "chat_content":chat_list}
        phone_chat_history.insert(0, new_chat)
        phone_chat_history_new_flags[chat_name] = True
        phone_set_new("messages")
        return



    def phone_get_contact_by_contact_name(contact_name):
        global phone_contacts
        for contact in phone_contacts:
            if contact["name"] == contact_name:
                return contact

    def phone_set_new(menu_name):
        global phone_buttons_new
        if phone_buttons_new.has_key(menu_name):
            phone_buttons_new[menu_name] = True
        return

    def phone_get_gallery_image_path(image_name):
        imagePathExt = img_find_path_ext(image_name)
        imagePath = imagePathExt[0]
        return imagePath

    def phone_camera_get_current_image():
        global scene_image, current_slide, phone_camera_subst
        if renpy.get_screen("show_image_screen_image") != None:
            if current_slide != False:
                if phone_camera_subst.has_key(str(current_slide)):
                    return phone_camera_subst[str(current_slide)]
                return current_slide
        if renpy.get_screen("show_image_screen") != None and renpy.get_screen("screen_sprites") != None:
            return parse_str(scene_image)
        return "black_screen"

    def phone_open_camera_capture():
        global phone_menu_active, phone_orientation, phone_camera_image
        renpy.play("/Sounds/camera_lens1.ogg")
        phone_menu_active = "camera"
        phone_orientation = 1
        phone_camera_image = phone_camera_get_current_image()
        if phone_camera_image == "black_screen":
            return
        renpy.show_screen("phone_camera_screen2", phone_camera_image)
        return

    def phone_open_camera_capture_action(action_name):
        global phone_gallery, phone_camera_image
        if action_name == "denied":
            renpy.play("/Sounds/denied.ogg")
            return
        if action_name == "close":
            renpy.play("/Sounds/vjuh3.ogg")
            renpy.hide_screen("phone_camera_screen2")
            return
        if action_name == "shoot":
#            for idx in range(len(phone_gallery)-1,-1,-1):
#                if phone_gallery[idx][0] == phone_camera_image:
#                    del phone_gallery[idx]
#            if phone_camera_image in phone_gallery:
#                phone_gallery.remove(phone_camera_image)

            phone_gallery.insert(0, [phone_camera_image, {"sprites": [], "overlaysList" : []}])
            if len(phone_gallery) >= 30:
                steam_achievement("ach_photo1")
            if len(phone_gallery) >= 60:
                steam_achievement("ach_photo2")
            renpy.play("/Sounds/snd_photo_capture.ogg")
            renpy.show_screen("phone_camera_screen2_shoot")
            return
        return

    def phone_gallery_add_image(phone_camera_image):
        phone_gallery.insert(0, [phone_camera_image, {"sprites": [], "overlaysList" : []}])
        return


    def get_camera_scene_shoot_data(): # собираем данные спрайтов и оверлеев из сцены
        global scene_data, day_time
        overlaysList = []
        spritesList = []
        zorder_list = []
        for i in scene_data: zorder_list.append([i, scene_data[i]["zorder"]])
        zorder_list.sort(key=lambda x:x[1])
        for zorder_ptr in zorder_list:
            i = zorder_ptr[0]
            day_time_suffix = "_" + day_time if day_time in ["evening"] else ""
            if scene_data[i]["type"] == 2: # обрабатываем только type 2
                spriteImageStr = scene_data[i]["img" + day_time_suffix] if scene_data[i]["img" + day_time_suffix] != False else scene_data[i]["img"] if scene_data[i]["img"] != False else False
                canvas_offset = scene_data[i]["canvas_img" + day_time_suffix] if scene_data[i].has_key("canvas_img" + day_time_suffix) != False else scene_data[i]["canvas_img"] if scene_data[i].has_key("canvas_img") else False
                if spriteImageStr != False and canvas_offset != False: # обрабатываем только если есть картинка спрайта
                    spritesList.append([spriteImageStr, canvas_offset])
                overlayName = scene_data[i]["img" + day_time_suffix + "_overlay"] if scene_data[i]["img" + day_time_suffix + "_overlay"] != False else scene_data[i]["img" + "_overlay"] if scene_data[i]["img" + "_overlay"] != False else False
                overlay_canvas_offset = scene_data[i]["canvas_img" + day_time_suffix + "_overlay"] if scene_data[i].has_key("canvas_img" + day_time_suffix + "_overlay") != False else scene_data[i]["canvas_img_overlay"] if scene_data[i].has_key("canvas_img_overlay") else False
                if overlayName != False and overlay_canvas_offset != False: # обрабатываем оверлеи
                    overlaysList.append([overlayName, overlay_canvas_offset])

        return {"sprites": spritesList, "overlaysList" : overlaysList}

    def draw_camera_scene_shoot_data(image_name, data):
        global scene_data, day_time
#        img = Image(image_name)
        compositeList = [(1920,1080), (0,0), image_name]
        try:
            for overlay in data["overlaysList"]:
                if renpy.exists(overlay[0]):
                    compositeList.append((overlay[1][1], overlay[1][0]))
                    compositeList.append(overlay[0])
            for sprite in data["sprites"]:
                if renpy.exists(sprite[0]):
                    compositeList.append((sprite[1][1], sprite[1][0]))
                    compositeList.append(sprite[0])
            img = im.Composite(*compositeList)
        except:
            img = Image(image_name)
        return img

    def phone_gallery_switch_delete():
        global phone_gallery_delete_mode
        if phone_gallery_delete_mode == True:
            phone_gallery_delete_mode = False
        else:
            phone_gallery_delete_mode = True
        return

    def phone_gallery_delete_action(gal_idx):
        global phone_gallery
#        renpy.play("/Sounds/snd_cardboard1.ogg")
        renpy.play("/Sounds/click1.ogg")
        del phone_gallery[gal_idx]
        return

#
