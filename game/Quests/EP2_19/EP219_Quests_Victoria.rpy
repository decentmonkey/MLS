default ep219_quests_victoria1_init_flag = 0
default ep219_quests_victoria_party_day = 0
label ep219_quests_victoria1_init:
    if ep219_quests_victoria1_init_flag > 0:
        return
    $ ep219_quests_victoria1_init_flag = day
    $ questHelp("victoria_18a")
    $ add_hook("office_work_process", "ep219_quests_victoria2_stephanie", scene="global", label="ep219_quests_victoria2_stephanie", priority=1)
    return

label ep219_quests_victoria2_stephanie: # приход Стефани к Виктории
#    if day - ep218_victoria_visit_day1 < 2:
#        return # не прошло 2 дня
    $ remove_hook()
    call ep219_dialogues4_victoria_1() from _rcall_ep219_dialogues4_victoria_1
    $ questHelp("victoria_18a", True)
    $ questHelp("victoria_18b")
    $ add_hook("before_open", "ep219_quests_victoria3_office", scene="working_office", label="ep219_quests_victoria3_office")
    $ add_hook("before_open", "ep219_quests_victoria3_office", scene="working_office_cabinet", label="ep219_quests_victoria3_office")
    return

label ep219_quests_victoria3_office:
    if day_time == "evening" or week_day == 7:
        return
    # Моника в офисе встречает Викторию
    $ remove_hook(label="ep219_quests_victoria3_office")
    call ep219_dialogues4_victoria_2() from _rcall_ep219_dialogues4_victoria_2
    $ questHelp("victoria_18b", True)
    $ questHelp("victoria_18c")
    $ add_hook("change_time_evening", "ep219_quests_victoria4_melanie", scene="global", label="ep219_quests_victoria4_melanie", priority = 1)

    return

label ep219_quests_victoria4_melanie:
    # Разговор Виктории и Мелани о шоппинге
    $ remove_hook()
    call ep219_dialogues4_victoria_3() from _rcall_ep219_dialogues4_victoria_3
    $ move_object("Melanie", "empty")
    $ move_object("DickSecretary", "empty")
    $ questHelp("victoria_18c", True)
    $ questHelp("victoria_18d")
    $ add_hook("change_time_day", "ep219_quests_victoria5_melanie_alex", scene="global", label="ep219_quests_victoria5_melanie_alex", priority = 1)

    return

label ep219_quests_victoria5_melanie_alex:
    # разговор Мелани и Алекса
    $ remove_hook()
    call ep219_dialogues4_victoria_4() from _rcall_ep219_dialogues4_victoria_4
    $ questHelp("victoria_18d", True)
    $ questHelp("victoria_18e")
    $ move_object("DickSecretary", "dick_office_secretary")
    $ add_hook("before_open", "ep219_quests_victoria6_officeworker5", scene="working_office_cabinet", label="ep219_quests_victoria3_office")
    $ set_active("Worker5", False, scene="working_office")


    return

label ep219_quests_victoria6_officeworker5: # Разговор Виктории, Стефани и подхалима у лифта
    if day_time == "evening" or week_day == 7:
        return
    $ remove_hook(label="ep219_quests_victoria3_office")
    call ep219_dialogues4_victoria_5() from _rcall_ep219_dialogues4_victoria_5
    $ set_active("Worker5", True, scene="working_office")
    $ questHelp("victoria_18e", True)
    $ questHelp("victoria_18f")
    $ add_hook("office_work_process", "ep219_quests_victoria7_melanie_victoria", scene="global", label="ep219_quests_victoria7_melanie_victoria", priority=1)
    return

label ep219_quests_victoria7_melanie_victoria: # разговор Виктории и Мелани перед вечеринкой
    $ remove_hook()
    call ep219_dialogues4_victoria_6() from _rcall_ep219_dialogues4_victoria_6
    $ questHelp("victoria_18f", True)
    $ questHelp("victoria_18g")
    $ add_hook("before_open", "ep219_quests_victoria8_party", scene="street_monica_office", label="ep219_quests_victoria8_party")
    $ add_hook("change_time_evening", "ep219_quests_victoria7b", scene="global", label="ep219_quests_victoria7b", priority=1, once=True)
    return

label ep219_quests_victoria7b: # убираем Мелани и Алекса
    $ move_object("Melanie", "empty")
    $ move_object("AlexPhotograph", "empty")
    $ move_object("Biff", "empty")
    return

label ep219_quests_victoria8_party:
    $ remove_hook()
    call ep219_dialogues4_victoria_7() from _rcall_ep219_dialogues4_victoria_7
    $ add_hook("change_time_day", "ep219_quests_victoria9_partyafter", scene="global", label="ep219_quests_victoria9_partyafter", priority=1, once=True)
    $ ep219_quests_victoria_party_day = day
    call ep224_quests_victoria_init() from _rcall_ep224_quests_victoria_init_1
    $ questHelp("victoria_18g", True)
    return

label ep219_quests_victoria9_partyafter:
    # возвращаем Алекса

    $ move_object("AlexPhotograph", "monica_office_photostudio")
    return




#
