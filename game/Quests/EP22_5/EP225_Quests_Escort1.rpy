default ep225_quests_escort1_1_init_flag = False

default ep225_quests_meeting1_planned = False
default ep225_quests_meeting2_planned = False
label ep225_quests_escort1_1_init:
    if ep225_quests_escort1_1_init_flag == True:
        return
    $ ep225_quests_escort1_1_init_flag = True
    $ questHelp("escort_31")
    $ ep225_quests_meeting1_planned = True

    return

label ep225_quests_escort1_2_meet_abbycandise:
    $ ep225_quests_meeting1_planned = False
    call ep22_5_dialogues1_escort1_1()
    if _return == False:
        $ add_hook("Visitor1", "ep225_quests_escort1_3_repeat", scene="rich_hotel_restaurant", label="ep225_quests_escort1_3_repeat")
        $ add_hook("Visitor4", "ep225_quests_escort1_3_repeat", scene="rich_hotel_restaurant", label="ep225_quests_escort1_3_repeat")
        $ questHelp("escort_31", False)
        return
    call ep225_quests_escort1_4_init()
    return

label ep225_quests_escort1_3_repeat:
    call ep22_5_dialogues1_escort1_2()
    if _return == False:
        $ questHelp("escort_31", False)
        call refresh_scene_fade()
        return False
    call ep225_quests_escort1_4_init()
    return False

label ep225_quests_escort1_4_init:
    $ remove_hook(label="ep225_quests_escort1_3_repeat")
    $ ep225_quests_meeting2_planned = True
    $ add_hook("MonicaTable", "ep225_quests_escort1_5_table_refuse", scene="rich_hotel_restaurant", label="ep225_quests_escort1")
    $ set_active("Visitor1", False, scene="rich_hotel_restaurant")
    $ set_active("Visitor4", False, scene="rich_hotel_restaurant")
    $ focus_map("Teleport_Candise_Apartments", "ep22_5_dialogues1_escort1_3")
    $ hudDaySkipToEveningEnabled = False
    $ autorun_to_object("ep22_5_dialogues1_escort1_3", scene="street_rich_hotel")
    $ questHelp("escort_31", True)
    $ questHelp("escort_32")

    $ add_hook("Teleport_Inside", "ep225_quests_escort1_6_enter_candiseabby", scene="street_candise", label="ep225_quests_escort1_6_enter_candiseabby")
    return

label ep225_quests_escort1_5_table_refuse:
    call ep22_5_dialogues1_escort1_3()
    return False

label ep225_quests_escort1_6_enter_candiseabby:
    $ remove_hook()
    $ remove_hook(label="ep225_quests_escort1")
    $ set_active("Visitor1", True, scene="rich_hotel_restaurant")
    $ set_active("Visitor4", True, scene="rich_hotel_restaurant")
    $ hudDaySkipToEveningEnabled = True
    $ ep225_quests_meeting2_planned = False
    $ unfocus_map()
    call ep22_5_dialogues1_escort1_4()
    if day_time != "evening":
        $ changeDayTime("evening")

    call ep22_5_dialogues1_escort1_5()
    if _return == False:
        $ questHelp("escort_32", False)
        $ add_hook("Visitor1", "ep225_quests_escort1_3_repeat", scene="rich_hotel_restaurant", label="ep225_quests_escort1_3_repeat")
        $ add_hook("Visitor4", "ep225_quests_escort1_3_repeat", scene="rich_hotel_restaurant", label="ep225_quests_escort1_3_repeat")
        $ autorun_to_object("ep22_5_dialogues1_escort1_6", scene="street_candise")
        call refresh_scene_fade_long()
        return False

    $ autorun_to_object("ep22_5_dialogues1_escort1_7", scene="street_candise")
    $ questHelp("escort_32", True)
    $ questHelp("escort_33")
    $ add_hook("enter_scene", "ep225_quests_escort2_init", scene="rich_hotel_reception", label="ep225_quests_escort2_init")
    call refresh_scene_fade_long()
    return False

#$ ep225_quests_meeting2_planned = False
