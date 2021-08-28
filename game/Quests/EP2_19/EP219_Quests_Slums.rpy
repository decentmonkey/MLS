default citizen4BForced = False
default citizen4BlockedByDay = 0
default ep219_quest_slums_stage = 0
default ep219_quest_slums_last_day = 0

label ep219_quest_slums1:
    if ep219_quest_slums_stage == 0:
        music2 stop
        call ep219_dialogues5_citizens_1b() from _rcall_ep219_dialogues5_citizens_1b
        $ citizen4BForced = False
        $ move_object("Citizen_4", "empty")
        $ add_hook("before_open", "ep219_quest_slums2_enterhome", scene="monicahome_livingroom", label="citizen4_catch1")
        return False
    if ep219_quest_slums_stage == 1:
        # регулярная встреча
        call ep219_dialogues5_citizens_2() from _rcall_ep219_dialogues5_citizens_2
        if _return == False:
            return False
        call ep219_dialogues5_citizens_1a() from _rcall_ep219_dialogues5_citizens_1a
        if _return == False:
            $ questHelp("work_slums_54", False, skipIfTrue=True)
            call change_scene("street_monicahome") from _rcall_change_scene_244
            $ changeDayTime("evening")
            call process_object_click_forced("HomeEnter", "w") from _rcall_process_object_click_forced_7
            return False

        $ questHelp("work_slums_54", True)
        $ ep219_quest_slums_last_day = day
        $ move_object("Citizen_4", "empty")
        $ citizen4BlockedByDay = day + 3 # блокируем на 3 дня
        call change_scene("street_monicahome") from _rcall_change_scene_245
        $ changeDayTime("evening")
        call process_object_click_forced("HomeEnter", "w") from _rcall_process_object_click_forced_8
    return

label ep219_quest_slums2_enterhome:
    # Монику перехватывает незнакомец
    if day_time == "evening":
        return
    $ remove_hook()
    call ep219_dialogues5_citizens_1() from _rcall_ep219_dialogues5_citizens_1
    $ citizen4BlockedByDay = day + 3 # блокируем на 3 дня
    if _return == False:
        $ questHelp("work_slums_54", False, skipIfTrue=True)

        return
    $ ep219_quest_slums_last_day = day
    $ questHelp("work_slums_54", True)
    if ep219_quest_slums_stage == 0:
        $ ep219_quest_slums_stage = 1
    $ changeDayTime("evening")
    return
