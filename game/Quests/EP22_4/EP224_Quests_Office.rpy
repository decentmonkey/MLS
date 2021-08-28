default ep224_quests_office_init_flag = False
default ep224_quests_office_biff_dialogue_enabled = False
default ep224_quests_office_day1 = 0
default ep224_quests_office_day2 = 0
default ep224_quests_office_day3_completed = 0

label ep224_quests_office_init:
    if ep224_quests_office_init_flag == True:
        return
    $ ep224_quests_office_init_flag = True
    $ ep224_quests_office_biff_dialogue_enabled = True
    $ questHelp("office_61")

    return

label ep224_quests_office1:
    $ ep224_quests_office_day1 = day
    call ep22_4_dialogues4_office_1() from _rcall_ep22_4_dialogues4_office_1
    if _return == False:
        $ questHelp("office_61", False)
        # repeat
        $ add_talk("Biff", "ep224_quests_office2_repeat", scene="monica_office_cabinet_table", label="ep224_quests_office2_repeat")
        call putoff_work_clothes() from _rcall_putoff_work_clothes_19
        fadeblack 3.0
        $ autorun_to_object("ep22_4_dialogues4_office_2", scene="street_monica_office")
        $ autorun_to_object("ep22_4_dialogues4_office_3", scene="monica_office_cabinet_table")
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_252
        return False
    jump ep224_quests_office3_start

label ep224_quests_office2_repeat:
    $ ep224_quests_office_day1 = day
    call ep22_4_dialogues4_office_4() from _rcall_ep22_4_dialogues4_office_4
    if _return == False:
        call putoff_work_clothes() from _rcall_putoff_work_clothes_20
        fadeblack 3.0
        $ autorun_to_object("ep22_4_dialogues4_office_2", scene="street_monica_office")
        $ autorun_to_object("ep22_4_dialogues4_office_3", scene="monica_office_cabinet_table")
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_253
        return False
    jump ep224_quests_office3_start

label ep224_quests_office3_start:
    $ add_objective("go_makeuproom", t_("Пойти в гримерную комнату в фотостудии"), c_blue, 155)

    $ remove_hook(label="ep224_quests_office2_repeat")
    $ miniMapEnabledOnly = ["Office_Biff_Cabinet", "Office_PhotoStudio"]
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_4_dialogues4_office_1a", scene="monica_office_secretary", label="ep224_quests_office3_start")
    $ add_talk("Biff", "ep22_4_dialogues4_office_1a", scene="monica_office_cabinet_table", label="ep224_quests_office3_start")
    $ add_hook("before_open", "ep224_quests_office4_makeuproom", scene="monica_office_makeup_room", label="ep224_quests_office3_start")
    return False

label ep224_quests_office4_makeuproom:
    $ remove_objective("go_makeuproom")
    $ remove_hook(label="ep224_quests_office3_start")
    $ miniMapEnabledOnly = []
    $ ep224_quests_office_day2 = day
    call putoff_work_clothes() from _rcall_putoff_work_clothes_21
    call ep22_4_dialogues4_office_5() from _rcall_ep22_4_dialogues4_office_5
    call ep22_4_dialogues4_office_6() from _rcall_ep22_4_dialogues4_office_6
    call ep22_4_dialogues4_office_7() from _rcall_ep22_4_dialogues4_office_7
    $ miniMapEnabledOnly = []
    $ questHelp("office_61", True)
    $ add_talk("Biff", "ep224_quests_office5_biff", scene="monica_office_cabinet_table", label="ep224_quests_office5_biff")
    $ add_hook("Teleport_Inside", "ep22_4_dialogues4_office_8a", scene="street_monica_office", label="evening_time_temp")
    fadeblack 3.0
    call process_change_map_location("House") from _rcall_process_change_map_location_16
    # мысли Моники, если у нее не было секса с Дэниелем и Джорджем
    if monicaInvestorMasonDate5 > 0 or monicaInvestorMasonDate7 > 0:
        $ autorun_to_object("ep22_4_dialogues4_office_10", scene="street_house_outside")
    else:
    # мысли Моники, если у нее был секс с Дэниелем и Джорджем
        $ autorun_to_object("ep22_4_dialogues4_office_9", scene="street_house_outside")

    call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_254
    return False

label ep224_quests_office5_biff:
    $ remove_hook()
    call ep22_4_dialogues4_office_8() from _rcall_ep22_4_dialogues4_office_8
    $ ep224_quests_office_biff_dialogue_enabled = False
    $ autorun_to_object("ep22_4_dialogues4_office_11", scene="monica_office_secretary")
    call change_scene("monica_office_secretary", "Fade_long") from _rcall_change_scene_255
    $ ep224_quests_office_day3_completed = day
    return False



#
