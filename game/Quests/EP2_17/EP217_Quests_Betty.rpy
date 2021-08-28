default ep217_quests_betty1_visit3_inited = False
default ep217_quests_betty_visit3_day = 0
default ep217_quests_betty_visit3_completed_day = 0
default ep217_quests_betty_refused = False


label ep217_quests_betty1_check:
    if ep217_quests_betty1_visit3_inited == False:
        $ ep217_quests_betty1_visit3_inited = True
        $ add_hook("change_time_day", "ep217_quests_betty2_begin", scene="global", label="betty_visit3_begin", priority = 1)


    return

label ep217_quests_betty2_begin:
    $ remove_hook()
    call ep217_dialogues3_betty_1() from _rcall_ep217_dialogues3_betty_1 # показываем Бетти в доме
    if _return == False:
        $ questHelp("house_45", False)
        return


    $ street_house_neighbour_betty_suffix = 2
    $ street_house_outside_betty_suffix = 2
    $ set_active("Betty", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Neighbour", True, scene="street_house_outside")
    $ set_active("Betty", True, scene="street_house_neighbour")
    $ set_active("Neighbour", False, scene="street_house_neighbour")
    $ set_active("Door", True, scene="street_house_neighbour")
    $ add_hook("Door", "ep217_quests_betty3_door", scene="street_house_neighbour", label="ep215_quests_betty3_enter_door", owner="Betty")

    $ ep215_stored_vars["scene_name"] = scene_name
    $ ep215_stored_vars["miniMapEnabledOnly"] = miniMapEnabledOnly
    $ ep215_stored_vars["hudDaySkipToEveningEnabled"] = hudDaySkipToEveningEnabled
    $ ep215_betty_floor2 = get_active_objects("Betty", "floor2")
    call change_owner("Betty") from _rcall_change_owner_4
    $ map_objects = {
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active", "owner":"Betty"}
    }
    $ miniMapEnabledOnly = ["none"]
    $ hudDaySkipToEveningEnabled = False

    $ autorun_to_object("ep215_dialogues2_betty_11", scene="street_house_outside")
    call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_205
    return

label ep217_quests_betty3_door:
    if act=="l":
        call ep215_dialogues2_betty_8() from _rcall_ep215_dialogues2_betty_8_1
        return False
    $ remove_hook()
    $ ep217_quests_betty_visit3_day = day

    call ep217_dialogues3_betty_2() from _rcall_ep217_dialogues3_betty_2
    if _return == False:
        $ ep217_quests_betty_refused = True
        $ ep217_quests_betty_visit3_completed_day = -1
        $ questHelp("house_45", False)
    else:
        $ ep217_quests_betty_visit3_completed_day = day
        $ questHelp("house_45", True)
        call ep218_quests_betty_init() from _rcall_ep218_quests_betty_init

    call ep215_dialogues2_betty_7() from _rcall_ep215_dialogues2_betty_7_1
    # Бетти возвращается к Ральфу
    $ set_active("Teleport_House_Outside_Neighbour", False, scene="street_house_outside")
    call change_owner("Monica") from _rcall_change_owner_5

    $ miniMapEnabledOnly = ep215_stored_vars["miniMapEnabledOnly"]
    $ hudDaySkipToEveningEnabled = ep215_stored_vars["hudDaySkipToEveningEnabled"]
    $ move_object("Betty", "empty")
    if ep215_betty_floor2 == True:
        $ move_object("Betty", "floor2")

    fadeblack 2.0
    $ autorun_to_object("ep215_dialogues2_betty_12", scene=ep215_stored_vars["scene_name"])
    call change_scene(ep215_stored_vars["scene_name"], "Fade_long") from _rcall_change_scene_206
    $ ep215_stored_vars = {}

    return










#
