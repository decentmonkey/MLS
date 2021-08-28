default ep218_quests_victoria_init_flag = False
default ep218_victoria_visit_day1 = 0

label ep218_quests_victoria_init:
    if ep218_quests_victoria_init_flag == True or ep27_melanie_visited_victoria != True:
        return
    $ ep218_quests_victoria_init_flag = True
    # стартуем в ближайший рабочий день
    $ add_hook("office_work_process", "ep218_quests_victoria1_start", scene="global", label="ep218_quests_victoria1_start", priority = 50)
    $ questHelp("victoria_17")
    return

label ep218_quests_victoria1_start:
    $ remove_hook()
    call ep218_dialogues2_victoria_1() from _rcall_ep218_dialogues2_victoria_1
    $ monicaOfficeWorkedToday = True
    $ add_objective("go_victoria", t_("Идти к Виктории."), c_red, 125)

    python:
        focus_map("Teleport_VictoriaHome", "ep216_dialogues5_victoria_12b")
        move_object("Melanie", "empty")
        hudDaySkipToEveningEnabled = False # выключаем телепорт в кровать
        # выключаем сон
        add_hook("slums_apartments_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep218_victoria_block")
        add_hook("hostel_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep218_victoria_block")
        add_hook("juliahome_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep218_victoria_block")
        add_hook("basement_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep218_victoria_block")

        # блокируем перемещения и работу
        add_hook("Building", "ep216_dialogues5_victoria_12", scene="street_police", label="ep218_victoria_block") # блокируем полицию
        add_hook("JuliaHome", "ep216_dialogues5_victoria_12", scene="street_juliahome", label="ep218_victoria_block") # блокируем Юлию
        ep216_juliahome_blocked_day = day # блокируем мини-карту у дома Юлии


        add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_dick_office", label="ep218_victoria_block")
        add_hook("MonicaTable", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep218_victoria_block")
        add_hook("MonicaChair", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep218_victoria_block")
        add_hook("Julia", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep218_victoria_block")
        add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_monica_office", label="ep218_victoria_block")
        add_hook("before_open", "ep216_quests_victoria3_street", scene="street_monica_office", label="ep218_victoria_block")
        add_hook("Worker1", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker2", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker5", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office", label="ep218_victoria_block")
        add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep218_victoria_block")
        add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep218_victoria_block")
        add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep218_victoria_block")
        add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep218_victoria_block")

        add_hook("VictoriaHome_Enter", "ep218_quests_victoria2_enter", scene="street_victoriahome", label="ep218_victoria_visit_day1")
        add_hook("enter_scene", "ep216_quests_victoria3_street2", scene="street_victoriahome", label="ep218_victoria_visit_day1", once=True)
        autorun_to_object("ep216_dialogues5_victoria_12b", scene="working_office_cabinet")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_140
    return False

label ep218_quests_victoria2_enter:
    if act=="l":
        return
    if cloth != "CasualDress1":
        call ep216_dialogues5_victoria_8a() from _rcall_ep216_dialogues5_victoria_8a_2
        return False
    $ remove_hook()
    $ remove_hook(label="ep218_victoria_block")
    $ remove_hook(label="ep216_victoria_visit_day1")
    call ep218_dialogues2_victoria_2() from _rcall_ep218_dialogues2_victoria_2
    if melanieVictoriaMonicaGirlsParty9 > 0:
        # если Моника подставила Мелани и присутствовала при ее наказании
        call ep218_dialogues2_victoria_6() from _rcall_ep218_dialogues2_victoria_6
        $ add_talk("Melanie", "ep218_dialogues2_victoria_6a", scene="monica_office_makeup_room", label="ep218_victoria_afterpiss")
    if melanieVictoriaMonicaGirlsParty4 > 0:
        # мысли Моники, если делала писсинг
        call ep218_dialogues2_victoria_7() from _rcall_ep218_dialogues2_victoria_7
    if melanieVictoriaMonicaGirlsParty5 > 0:
        # мысли Моники, если делала ликинг
        call ep218_dialogues2_victoria_8() from _rcall_ep218_dialogues2_victoria_8

    $ fitness_gym_state = 2
    $ hudDaySkipToEveningEnabled = True
    $ ep216_juliahome_blocked_day = day-1 # разблокируем мини-карту у дома Юлии

    $ move_object("Melanie", "empty")
    $ ep218_victoria_visit_day1 = day
    $ remove_objective("go_victoria")
    $ questHelp("victoria_17", True)
    call ep219_quests_victoria1_init() from _rcall_ep219_quests_victoria1_init
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_30
    return False
