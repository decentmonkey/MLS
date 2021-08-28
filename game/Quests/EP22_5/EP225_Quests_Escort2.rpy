default ep225_quests_escort2_1_planned = False
default ep225_quests_escort2_status = 0
label ep225_quests_escort2_init:
    $ remove_hook()
    $ ep225_quests_escort2_1_planned = True
    call ep22_5_dialogues2_escort2_1()
    return

label ep225_quests_escort2_2:
    $ ep225_quests_escort2_1_planned = False
    call ep22_5_dialogues2_escort2_2()
    $ add_hook("MonicaTable", "ep22_5_dialogues2_escort2_3a", scene="rich_hotel_restaurant", label="ep225_quests_escort2")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep22_5_dialogues2_escort2_3a", scene="rich_hotel_reception", label="ep225_quests_escort2")
    $ add_hook("Teleport_Restaurant", "ep22_5_dialogues2_escort2_3a", scene="rich_hotel_reception", label="ep225_quests_escort2")
    $ set_active("ReceptionGirl", False, scene="rich_hotel_reception")
    $ set_active("Visitor1", False, scene="rich_hotel_restaurant")
    $ set_active("Visitor2", False, scene="rich_hotel_restaurant")
    $ set_active("Visitor3", False, scene="rich_hotel_restaurant")
    $ set_active("Visitor4", False, scene="rich_hotel_restaurant")
    $ add_hook("Lift", "ep225_quests_escort2_3_lift", scene="rich_hotel_lift", label="ep225_quests_escort2")
    $ add_hook("Teleport_Reception", "ep22_5_dialogues2_escort2_3", scene="rich_hotel_restaurant", once=True)
    $ questHelp("escort_33", True)
    $ questHelp("escort_34")
    $ questHelp("escort_35")
    fadeblack 2.0
    return

label ep225_quests_escort2_3_lift:
    if act=="l":
        return
    sound snd_lift
    fadeblack 2.0
    if day_time != "evening":
        $ changeDayTime("evening")
    call ep22_5_dialogues2_escort2_4()
    $ ep225_quests_escort2_status = _return
    if _return == -1:
        # отказалась проходить кастинг
        $ autorun_to_object("ep22_5_dialogues2_escort2_8", scene="street_house_outside")
        $ questHelp("escort_35", False)
    if _return == 1:
        # Моника победила
        $ autorun_to_object("ep22_5_dialogues2_escort2_7", scene="street_house_outside")
        $ questHelp("escort_35", True)
    if _return == -2:
        # Админша победила
        $ autorun_to_object("ep22_5_dialogues2_escort2_8", scene="street_house_outside")
        $ questHelp("escort_35", False)
    #monicaVipEscortCasting2 > 0 - Моника проголосовала за Эбби
    #monicaVipEscortCasting1 > 0 - Моника проголосовала за Миранду
    call ep211_quests_escort2_end_day()
    $ set_active("ReceptionGirl", True, scene="rich_hotel_reception")
    $ set_active("Visitor1", True, scene="rich_hotel_restaurant")
    $ set_active("Visitor2", True, scene="rich_hotel_restaurant")
    $ set_active("Visitor3", True, scene="rich_hotel_restaurant")
    $ set_active("Visitor4", True, scene="rich_hotel_restaurant")
    $ questHelp("escort_34", True)
    $ remove_hook(label="ep225_quests_escort2")
    $ add_hook("Teleport_Rich_Hotel_Reception", "ep22_5_dialogues2_escort2_6", scene="street_rich_hotel", label="ep225_quests_escort2_block")
    $ add_hook("Teleport_Building", "ep22_5_dialogues2_escort2_6", scene="street_steve_office", label="ep225_quests_escort2_block")
    fadeblack 2.0
    call process_change_map_location("House")
    call change_scene("street_house_outside", "Fade_long")
    return False
