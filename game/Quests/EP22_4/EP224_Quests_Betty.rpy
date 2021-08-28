default ep224_quests_betty_init_flag = False
default ep224_quests_betty_visit1_day = 0
default ep224_quests_betty_visit2_day = 0
default ep224_quests_betty_aborted = False
label ep224_quests_betty_init:
    if ep224_quests_betty_init_flag == True:
        return
    $ questHelp("house_49")
    $ add_hook("fitness_end", "ep224_quests_betty1_check", scene="global", label="betty_neighbour_check")

    $ ep224_quests_betty_init_flag = True
    return

label ep224_quests_betty1_check:
    $ remove_hook(label="betty_neighbour_check")
    $ add_hook("change_time_day", "ep224_quests_betty2_morning", scene="global", label="ep224_quests_betty2_morning", priority = 1)
    return

label ep224_quests_betty2_morning:
    $ remove_hook()
    call ep22_4_dialogues1_betty_1() from _rcall_ep22_4_dialogues1_betty_1
    if _return == False:
        $ questHelp("house_49", False)
        $ ep224_quests_betty_aborted = True
        return

    $ street_house_neighbour_betty_suffix = 2
    $ street_house_outside_betty_suffix = 2
    $ set_active("Betty", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Neighbour", True, scene="street_house_outside")
    $ set_active("Betty", True, scene="street_house_neighbour")
    $ set_active("Neighbour", False, scene="street_house_neighbour")
    $ set_active("Door", True, scene="street_house_neighbour")
    $ add_hook("Door", "ep224_quests_betty3_door", scene="street_house_neighbour", label="ep215_quests_betty3_enter_door", owner="Betty")

    $ ep215_stored_vars["scene_name"] = scene_name
    $ ep215_stored_vars["miniMapEnabledOnly"] = miniMapEnabledOnly
    $ ep215_stored_vars["hudDaySkipToEveningEnabled"] = hudDaySkipToEveningEnabled
    $ ep215_betty_floor2 = get_active_objects("Betty", "floor2")
    call change_owner("Betty") from _rcall_change_owner_7
    $ map_objects = {
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active", "owner":"Betty"}
    }
    $ miniMapEnabledOnly = ["none"]
    $ hudDaySkipToEveningEnabled = False

    $ autorun_to_object("ep22_4_dialogues1_betty_1a", scene="street_house_outside")
    call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_246
    return

label ep224_quests_betty3_door:
    call ep22_4_dialogues1_betty_1b() from _rcall_ep22_4_dialogues1_betty_1b
    $ questHelp("house_49", True)
    $ questHelp("house_50")
    $ ep224_quests_betty_visit1_day = day

    # Бетти возвращается к Ральфу
    $ set_active("Teleport_House_Outside_Neighbour", False, scene="street_house_outside")
    call change_owner("Monica") from _rcall_change_owner_8

    $ miniMapEnabledOnly = ep215_stored_vars["miniMapEnabledOnly"]
    $ hudDaySkipToEveningEnabled = ep215_stored_vars["hudDaySkipToEveningEnabled"]
    $ move_object("Betty", "empty")
    if ep215_betty_floor2 == True:
        $ move_object("Betty", "floor2")

    fadeblack 2.0
    call change_scene(ep215_stored_vars["scene_name"], "Fade_long") from _rcall_change_scene_247
    $ ep215_stored_vars = {}
    $ add_hook("change_time_day", "ep224_quests_betty4_door", scene="global", label="ep224_quests_betty4_door", priority = 1)

    return


label ep224_quests_betty4_door:
    $ remove_hook()
    call ep22_4_dialogues1_betty_2() from _rcall_ep22_4_dialogues1_betty_2
    if _return == False:
        $ questHelp("house_50", False)
        $ ep224_quests_betty_aborted = True
        return
    $ ep224_quests_betty_visit2_day = day
    $ questHelp("house_50", True)

    return




#
