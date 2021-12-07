default sophieCallStage = 0
default cynthiaCallStage = 0
default seanCallStage = 0

label phone1:
    $ add_hook("before_call_contact", "phone_before_call_contact", scene="phone", label="phone_before_call_contact")
    $ add_hook("call_contact", "phone_call_contact", scene="phone", label="phone_call_contact")
    return

label phone_before_call_contact:
    if obj_name == "Sophie":
        if get_active_objects("Sophie", scene=scene_name) != False:
            bardi_t "Глупо звонить, когда я нахожусь рядом..."
            return False
    if obj_name == "Cynthia":
        if get_active_objects("Sister2", scene=scene_name) != False:
            bardi_t "Глупо звонить, когда я нахожусь рядом..."
            return False
    if obj_name == "Sean":
        if get_active_objects("Friend_Bardie", scene=scene_name) != False:
            bardi_t "Глупо звонить, когда я нахожусь рядом..."
            return False
    return

label phone_call_contact:
    if obj_name == "Cynthia":
        if cynthiaCallStage == 1 and day_suffix != 3:
            call cynthia_chat1() from _rcall_cynthia_chat1
            return
        if get_active_objects("Sister2", scene="COLLEGE", recursive=True) != False:
            call cynthia_chat2() from _rcall_cynthia_chat2 # регулярный чат днем, Синтия не может говорить, учится
            return
    if obj_name == "Sean":
        if seanCallStage == 1:
            call sean_chat1() from _rcall_sean_chat1
            return
        if get_active_objects("Friend_Bardie", scene="COLLEGE", recursive=True) != False:
            call sean_chat2() from _rcall_sean_chat2 # регулярный чат днем, Шон не может говорить, учится
            return

    sound snd_phone_short_beeps
    bardi_t "Не отвечает."
    return False
