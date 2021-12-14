default sophieCallStage = 0
default cynthiaCallStage = 0
default seanCallStage = 0
default whoreCallStage = 0
default emilyCallStage = 0

label phone1:
    $ add_hook("before_call_contact", "phone_before_call_contact", scene="phone", label="phone_before_call_contact")
    $ add_hook("call_contact", "phone_call_contact", scene="phone", label="phone_call_contact")
    return

label phone_before_call_contact:
    if obj_name == "Whore":
        if whoreCallStage == 3:
            call ep02_dialogues3_sean_5b() from _rcall_ep02_dialogues3_sean_5b
            return False
        if get_active_objects("Whore", scene=scene_name) != False:
            bardi_t "Глупо звонить, когда я нахожусь рядом..."
            return False
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
    if obj_name == "Emily":
        if emilyCallStage == 1:
            call emily_chat1() from _rcall_emily_chat1
            return
    if obj_name == "Whore":
        if whoreCallStage == 2:
            call whore_chat2() from _rcall_whore_chat2
            return
        if whoreCallStage == 1:
            call whore_chat1() from _rcall_whore_chat1
            return

    if obj_name == "Sophie":
        if sophieCallStage == 2:
            call sophie_chat3() from _rcall_sophie_chat3
            return
        if sophieCallStage == 1:
            call sophie_chat2() from _rcall_sophie_chat2
            return

    if obj_name == "Cynthia":
        if cynthiaCallStage == 1 and day_suffix != 3:
            call cynthia_chat1() from _rcall_cynthia_chat1
            return
        if get_active_objects("Sister2", scene="COLLEGE", recursive=True) != False:
            call cynthia_chat2() from _rcall_cynthia_chat2 # регулярный чат днем, Синтия не может говорить, учится
            return
    if obj_name == "Sean":
        if seanCallStage == 3:
            call sean_chat4() from _rcall_sean_chat4
            return
        if seanCallStage == 2:
            call sean_chat3() from _rcall_sean_chat3
            $ questHelp("college_15", True)
            return
        if seanCallStage == 1:
            call sean_chat1() from _rcall_sean_chat1
            return
        if get_active_objects("Friend_Bardie", scene="COLLEGE", recursive=True) != False:
            call sean_chat2() from _rcall_sean_chat2 # регулярный чат днем, Шон не может говорить, учится
            return

    sound snd_phone_short_beeps
    bardi_t "Не отвечает."
    return False
