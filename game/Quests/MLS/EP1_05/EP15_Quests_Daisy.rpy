label ep15_quests9_morning_daisy:
    if mlsBardiFamilyV4Daisy1 > 0:
        $ autorun_to_object("ep15_quests9_morning_daisy_call", scene="house_bedroom_mc")
        $ remove_hook()
    return

label ep15_quests9_morning_daisy_call:
    $ add_hook("daisy_call_event2", "ep15_quests9_morning_daisy_init2", scene="events", once=True, label="daisy_init2")
    $ daisyCallStage = 2
    $ phone_incoming_call("Daisy")
    return

label ep15_quests9_morning_daisy_init2: # инитим Дейзи после звонка
    $ add_hook("Teleport_LivingRoom", "ep15_quests9_daisy3", scene="daisy_street", label="daisy2")
    $ questHelp("work_9")
    $ set_object_follow_way("daisy_street", merge=True)

    return

label ep15_quests9_daisy3: # заходим в дом
    if ep05_dialogues2_family_daisy_visit_day > 0 and ep05_dialogues2_family_daisy_visit_day < day:
        if day_time_idx >= 2:
            call ep05_dialogues3_work_daisy_4b() from _rcall_ep05_dialogues3_work_daisy_4b
            return False
        # работа после встречи с Дейзи
        call ep05_dialogues3_work_daisy_2() from _rcall_ep05_dialogues3_work_daisy_2
        call ep05_dialogues3_work_daisy_4() from _rcall_ep05_dialogues3_work_daisy_4 # сцена с клиенткой
        call changeDayTime("evening") from _rcall_changeDayTime_48
        $ questHelpDesc("work_desc5")
        $ questHelpDesc("work_desc3", False)
        $ clear_object_follow_all()
        $ questHelp("work_11", True)
        call refresh_scene_fade() from _rcall_refresh_scene_fade_46
        return False
    if ep05_dialogues2_family_daisy_visit_day == day:
        call ep01_dialogues2_day1_family_1_12() from _rcall_ep01_dialogues2_day1_family_1_12_3 #Мне пока там нечего делать.
        return False
    if day_time_idx < 2:
        if ep15_quests9_daisy3_Flag == True:
            call ep05_dialogues2_family_daisy_2a() from _rcall_ep05_dialogues2_family_daisy_2a
            call refresh_scene_fade() from _rcall_refresh_scene_fade_47
            return False

        call ep05_dialogues2_family_daisy_2() from _rcall_ep05_dialogues2_family_daisy_2
        if _return == False:
            call refresh_scene_fade() from _rcall_refresh_scene_fade_48
            return False
        if mlsBardiFamilyV4Daisy2 == day:
            call changeDayTime("evening") from _rcall_changeDayTime_49
        $ ep15_quests9_daisy3_Flag = True
        $ questHelp("work_9", True)
        $ questHelp("work_10")
        $ add_hook("Bed", "ep15_quests9_bed_skip_evening", scene="house_bedroom_mc", label=["evening_time_temp", "daisy_evening"])

        call refresh_scene_fade() from _rcall_refresh_scene_fade_49
        return False

    # вечер
    if ep15_quests9_daisy3_refuse_day == day:
        call ep05_dialogues2_family_daisy_3a() from _rcall_ep05_dialogues2_family_daisy_3a
        return False
    $ clear_object_follow_all()
    $ remove_hook(label="daisy_evening")
    $ questHelp("work_10", True)
    call ep05_dialogues2_family_daisy_3() from _rcall_ep05_dialogues2_family_daisy_3
    if _return == False:
        $ ep15_quests9_daisy3_refuse_day = day
        call refresh_scene_fade() from _rcall_refresh_scene_fade_50
        return False
    $ ep05_dialogues2_family_daisy_visit_day = day
    $ daisyCallStage = 0
    $ add_hook("before_sleep_actions", "ep15_quests9_daisy4", scene="global", label="daisy3", once=True) # вечером сообщение от Дейзи
#    $ remove_hook(label="daisy2")
    $ add_hook("Teleport_LivingRoom", "ep01_dialogues2_day1_family_1_12", scene="daisy_street", label=["evening_time_temp", "daisy_block"]) #Мне пока там нечего делать.
    call refresh_scene_fade() from _rcall_refresh_scene_fade_51
    return False

label ep15_quests9_daisy4: # вечером сообщение от Дейзи
    $ ep15_sleep_regular_dialogue_skip_day = day
    call ep05_dialogues2_family_daisy_4() from _rcall_ep05_dialogues2_family_daisy_4
    $ daisyCallStage = 3
    $ autorun_to_object("ep15_quests9_daisy4a", scene="house_bedroom_mc_onbed")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_52
    return False

label ep15_quests9_daisy4a:
    $ phone_incoming_call("Daisy")
    $ add_hook("phone_close", "ep15_quests9_daisy4b", scene="phone", once=True)
    return

label ep15_quests9_daisy4b:
    pause 0.5
    call ep05_dialogues2_family_daisy_4b() from _rcall_ep05_dialogues2_family_daisy_4b
    $ add_hook("after_sleep", "ep15_quests9_daisy4c", scene="global", once=True, label="daisy4")
    call process_hooks("before_sleep_actions", "global") from _rcall_process_hooks_64
#    $ add_hook("change_time_day", "ep15_quests9_daisy4c", scene="global", once=True, label="daisy4")
    return

label ep15_quests9_daisy4c:
    $ daisyCallStage = 0
    $ add_hook("Teleport_Bedroom_MC", "ep15_quests9_daisy4d", scene="house_bedroom_mc_onbed", label="daisy4", once=True, priority=1000)
    return

label ep15_quests9_daisy4d:
    $ questHelp("work_11")
    $ daisyCallStage = 4
    $ phone_incoming_call("Daisy")
    $ set_object_follow_way("daisy_street", merge=True)
    return False
