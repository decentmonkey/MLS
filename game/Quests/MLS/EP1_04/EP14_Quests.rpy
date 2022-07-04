default ep14_update_init_flag = False

default sophieKitchenHelpEnabled1 = False
default sophieKitchenHelpLastDay = 0

default ep14_bikerent_work_count = 0
default ep14_bikerent_work_lastday = 0

default ep14_home_afterwork_stage = 0

default collegeLastDay = 0
default ep14_sister2_room_visited = False
default ep14_call_emily_flag = False

default ep14_mall_becky_lastday = 0

label ep14_update_init:
    if ep14_update_init_flag == True:
        return
    $ day = day + 1
    $ ep14_update_init_flag = True
    $ remove_hook(quest="college_day3")
    $ remove_hook(quest="day4")
    call change_scene("house_bedroom_mc") from _rcall_change_scene_142
    call process_change_map_location("HOUSE") from _rcall_process_change_map_location_4
    call changeDayTime("morning") from _rcall_changeDayTime_25
    call ep04_dialogues1_family_sophie_1a() from _rcall_ep04_dialogues1_family_sophie_1a

    if questHelpGetStatus("college_15") != 1:
        $ questHelp("college_15", False)

    python:
        sophieKitchenHelpEnabled1 = True

        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "college_empty")
        move_object("Friend_Bardie", "college_empty")

        #move_object("Sister2", "house_sister2")
        sister1RoomDoorLocked = True
        #sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0
        seanCallStage = 0
        map_enabled = False
        miniMapDisabled["HOUSE"] = ["House_Street"]

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        questHelp("house_22")
        questHelp("house_23")
        questHelpDesc("college_desc12", False)
        add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block", quest="day5")
        add_hook("before_open", "ep14_quests1_sophie", scene="house_kitchen", once=True, quest="day5")

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_19
    return

label ep14_quests1_sophie:
    call ep04_dialogues1_family_sophie_1() from _rcall_ep04_dialogues1_family_sophie_1
    $ clear_object_follow_all()
    $ questHelp("house_22", True)
    $ questHelp("college_29")
    $ map_enabled = True
    $ miniMapDisabled["HOUSE"] = []
    $ set_object_follow("Floor1", scene="minimap")
    $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_COLLEGE", scene="map")
    $ set_object_follow("Teleport_Coridor1", scene="college_street")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor3"]

    $ remove_hook(label="house_block")
    $ add_hook("Teleport_Coridor1", "ep14_quests2_college", scene="college_street", quest="day5", once=True)
    $ add_hook("before_open", "ep14_quests2_college", scene="college_coridor3", quest="day5", once=True)
    $ focus_map("Teleport_COLLEGE", "ep04_dialogues1_family_sophie_1b")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_36
    return

label ep14_quests2_college:
    call ep04_dialogues6_college_sarah_1a() from _rcall_ep04_dialogues6_college_sarah_1a
    $ remove_hook(label="ep14_quests2_college")
    $ clear_object_follow_all()
    $ questHelp("college_29", True)
    call ep04_dialogues6_college_sarah_1() from _rcall_ep04_dialogues6_college_sarah_1
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Gym", scene="college_coridor2")
    $ miniMapEnabledOnly = ["none"]
    $ set_active("Teleport_Stairs", False, scene="college_coridor2")
    $ add_hook("before_open", "ep14_quests2_college2_gym", scene="college_gym", quest="day5")
    $ unfocus_map()


    call change_scene("college_coridor2", "Fade_long") from _rcall_change_scene_143


    return False

label ep14_quests2_college2_gym:
    $ clear_object_follow_all()
    call ep04_dialogues6_college_sarah_2() from _rcall_ep04_dialogues6_college_sarah_2
    $ set_active("Teleport_Stairs", True, scene="college_coridor2")
    $ set_object_follow("Teleport_Coridor2", scene="college_gym")
    $ set_active("Teleport_Coridor2", True, scene="college_gym")
    $ miniMapEnabledOnly = []
    $ add_hook("Teleport_Coridor2", "ep14_quests2_college3_end", scene="college_gym", once=True)
    $ questHelpDesc("college_desc13")

    return False


label ep14_quests2_college3_end:
    $ clear_object_follow_all()
    call ep03_dialogues2_college_10b() from _rcall_ep03_dialogues2_college_10b
    call changeDayTime("day") from _rcall_changeDayTime_26
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3"]
    $ autorun_to_object("ep04_dialogues6_college_sarah_2a", scene="college_street") # диалог что надо идти работать
    $ questHelp("work_4")
    $ questHelp("work_5")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_DAISY", scene="map")
    $ set_object_follow("Teleport_PARK", scene="map")
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", quest="day5")
    $ add_hook("Teleport_LivingRoom", "ep14_quests3_daisy1", scene="daisy_street", quest="daisy_work")
    $ add_hook("FatherFriend", "ep14_quests3_bikerent1", scene="beach_park", label="bikerent_work")
    $ add_hook("Bed", "ep14_quests4_evening_bed", scene="house_bedroom_mc", label="bed_sleep")
    $ houseLifeStage = 3
    $ homeButtonEnabled = True
    $ add_hook("Sophie", "ep14_quests4_evening_sophie1", scene="house_livingroomhall", label="sophie_evening")
    $ collegeLastDay = day
    call change_scene("college_street") from _rcall_change_scene_144
    return False

label ep14_quests3_daisy1:
    if day_time_idx > 1:
        call ep04_dialogues4_family_daisy_1a() from _rcall_ep04_dialogues4_family_daisy_1a
        return False
    if mlsBardiFamilyV4Daisy2 > 0:
        call ep04_dialogues4_family_daisy_3() from _rcall_ep04_dialogues4_family_daisy_3
        if _return == -1:
            return False
        call ep14_quests4_evening_afterwork() from _rcall_ep14_quests4_evening_afterwork
    else:
        call ep04_dialogues4_family_daisy_1() from _rcall_ep04_dialogues4_family_daisy_1
        call ep04_dialogues4_family_daisy_2() from _rcall_ep04_dialogues4_family_daisy_2
        $ questHelp("work_4", True)
        $ questHelpDesc("work_desc0", False)
        $ questHelpDesc("work_desc2", "work_desc3")
        call phone_contact6() from _rcall_phone_contact6
        $ daisyCallStage = 1
        $ sophieCallStage = 5
        if day != 9:
            $ phone_focus_icon(True)
            $ phone_incoming_call("Sophie")

        call ep14_quests4_evening_afterwork() from _rcall_ep14_quests4_evening_afterwork_1
    return False

label ep14_quests3_bikerent1:
    $ clear_object_follow_all()

    if ep14_bikerent_work_count >= 2:
        call ep04_dialogues8_work_bikerental_2() from _rcall_ep04_dialogues8_work_bikerental_2
        $ ep14_bikerent_work_count += 1
        $ questHelp("work_7", True)
        $ questHelp("work_8")

    if ep14_bikerent_work_count == 1:
        call ep04_dialogues8_work_bikerental_3() from _rcall_ep04_dialogues8_work_bikerental_3
        $ ep14_bikerent_work_count = 2
        $ questHelpDesc("work_desc4")
        call locations_mall1() from _rcall_locations_mall1
        call map_init_mall() from _rcall_map_init_mall
        python:
            clear_object_follow_all()
            move_object("Whore", "mall_street")
            set_object_follow("Teleport_Map", scene="beach_park")
            set_object_follow("Teleport_MALL", scene="map")
            add_hook("Whore", "ep14_quests7_whore_mall1", scene="mall_street", label="whore_mall")
            add_hook("enter_scene", "ep14_quests7_mall1", scene="mall_street", label="enter_mall_street")
            add_hook("enter_scene", "ep14_quests7_mall2", scene="mall_street", label="enter_mall_street")
            questHelp("becky_1")
            questHelp("work_6", True)
            questHelp("work_7")
            ep14_bikerent_work_lastday = day
        if questHelpGetStatus("sean_2") != 1:
            $ questHelp("sean_2", False)
        call changeDayTime("evening") from _rcall_changeDayTime_27
        call refresh_scene_fade() from _rcall_refresh_scene_fade_37
        return False

    if ep14_bikerent_work_count == 0:
        call ep04_dialogues8_work_bikerental_1() from _rcall_ep04_dialogues8_work_bikerental_1
        $ ep14_bikerent_work_count = 1
        $ sophieCallStage = 5
        if day != 9:
            $ phone_focus_icon(True)
            $ phone_incoming_call("Sophie")
        $ questHelp("work_5", True)
        $ questHelp("work_6")

    $ ep14_bikerent_work_lastday = day
    call ep14_quests4_evening_afterwork() from _rcall_ep14_quests4_evening_afterwork_2
    return False


#default ep14_bikerent_work_count = 0
#default ep14_bikerent_work_lastday = 0

label ep14_quests4_evening_afterwork:
    python:
        clear_object_follow_all()
        focus_map("Teleport_HOUSE", "ep04_dialogues8_work_bikerental_1b")
        remove_hook(label="home_afterwork")
        add_hook("before_open", "ep14_quests4_evening_afterwork_home", scene="house_bedroom_mc", label="home_afterwork", priority=200)
        add_hook("before_open", "ep14_quests4_evening_afterwork_home", scene="house_floor1", label="home_afterwork", priority=200)
        add_hook("before_open", "ep14_quests4_evening_afterwork_home", scene="house_floor2", label="home_afterwork", priority=200)
    call changeDayTime("evening") from _rcall_changeDayTime_28
    call refresh_scene_fade() from _rcall_refresh_scene_fade_38

    return

label ep14_quests4_evening_afterwork_home:
    if ep14_home_afterwork_stage == 0:
        $ questHelp("house_24")
        $ questHelp("house_25")
        $ sophieCallStage = 0
        $ add_hook("Teleport_Sister2", "ep14_quests4_evening_sister2", scene="house_floor2", label="sister2_evening_regular1")
        $ ep14_home_afterwork_stage = 1
        $ clear_object_follow_all()
        $ set_object_follow("Teleport_LivingRoomHall", scene="house_floor1")

    $ map_enabled = False
    $ remove_hook(label="home_afterwork")
    $ unfocus_map()
    $ miniMapDisabled["HOUSE"] = ["House_Street"]
    $ add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block")
    return

label ep14_quests4_evening_sophie1:
    $ questHelp("house_24", True)
    call ep04_dialogues1_family_sophie_4() from _rcall_ep04_dialogues1_family_sophie_4
    if _return == 1 or _return == 2:
        call changeDayTime("night") from _rcall_changeDayTime_29
    return False

label ep14_quests4_evening_sister2:
    if day_time_idx != 2 or get_active_objects("Sister2", scene="house_sister2") == False:
        return
    call ep02_dialogues4_family_evening_4() from _rcall_ep02_dialogues4_family_evening_4
    return False



#### День 2 (вторник)

label ep14_quests4_evening_bed:
    if day_time_idx < 2:
        return
    call ep03_dialogues3_family_evening_4() from _rcall_ep03_dialogues3_family_evening_4_1
    $ clear_object_follow_all()
    $ remove_hook(quest="day5")
    $ questHelp("house_25", True)
    call changeDayTime("morning") from _rcall_changeDayTime_30
    call ep04_dialogues2_family_cynthia_1a() from _rcall_ep04_dialogues2_family_cynthia_1a
    $ sophieCallStage = 0
    $ move_object("Sister2", "house_sister2")
    $ add_hook("exit_scene", "ep14_quests5_sister2", scene="house_bedroom_mc", once=True)
    $ map_enabled = False
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_20
    return False

label ep14_quests5_sister2:
    call ep04_dialogues2_family_cynthia_1() from _rcall_ep04_dialogues2_family_cynthia_1
    call ep04_dialogues2_family_cynthia_2() from _rcall_ep04_dialogues2_family_cynthia_2
    call change_scene("house_bedroom_mc", "Fade_long") from _rcall_change_scene_145
    $ map_enabled = True
    $ miniMapDisabled["HOUSE"] = []
    $ remove_hook(label="house_block")
    $ questHelp("college_30")
    $ move_object("Sister2", "college_empty")

    $ set_object_follow("Teleport_Street", scene="minimap")
    $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_COLLEGE", scene="map")
    $ set_object_follow("Teleport_Coridor1", scene="college_street")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor3"]
    $ focus_map("Teleport_COLLEGE", "ep04_dialogues1_family_sophie_1b")

    python:
        move_object("Sister1", "emtpy")
        move_object("Sister2", "emtpy")
        move_object("Sophie", "emtpy")

    $ add_hook("before_open", "ep14_quests5_college1", scene="college_coridor1", quest="day6", label="enter_college6")
    $ add_hook("before_open", "ep14_quests5_college1", scene="college_coridor3", quest="day6", label="enter_college6")
    return False

label ep14_quests5_college1:
    $ remove_hook(label="enter_college6")
    call ep04_dialogues6_college_sarah_1a() from _rcall_ep04_dialogues6_college_sarah_1a_1
    call ep04_dialogues5_college_emily_1() from _rcall_ep04_dialogues5_college_emily_1

    call ep03_dialogues2_college_10b() from _rcall_ep03_dialogues2_college_10b_1
    call changeDayTime("day") from _rcall_changeDayTime_31
    $ clear_object_follow_all()
    $ emilyCallStage = 2
    call phone_contact5()
    $ questHelp("college_30", True)
    $ unfocus_map()
    $ autorun_to_object("ep04_dialogues5_college_emily_1a", scene="college_street")

    python:
        add_hook("before_open", "ep14_quests6_home1", scene="house_bedroom_mc", label="home_afterwork6", priority=201)
        add_hook("before_open", "ep14_quests6_home1", scene="house_floor1", label="home_afterwork6", priority=201)
        add_hook("before_open", "ep14_quests6_home1", scene="house_floor2", label="home_afterwork6", priority=201)
        set_object_follow("Teleport_Map", scene="house_street")
        set_object_follow("Teleport_PARK", scene="map")
        add_hook("before_open", "ep14_quests6_home2_sister1", scene="house_bedroom_mc", quest="day6", once=True)
        miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3"]
        add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", quest="day5")


    call change_scene("college_street", "Fade_long") from _rcall_change_scene_146
    return False

label ep14_quests6_home1:
    $ remove_hook(label="home_afterwork")
    $ remove_hook(label="home_afterwork6")
    $ questHelp("house_26")
    $ clear_object_follow_all()

    python:
        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Bedroom_MC", scene="house_floor2")
        set_object_follow("Teleport_Floor2", scene="house_floor1")
        set_object_follow("House_Bedroom_MC", scene="minimap")

    python:
        move_object("Sophie", "empty")
        move_object("Sister2", "empty")

    if day_time_idx != 2:
        call changeDayTime("evening") from _rcall_changeDayTime_32
    return

label ep14_quests6_home2_sister1:
    $ clear_object_follow_all()
    $ remove_hook(quest="day6")
    call ep04_dialogues3_family_olivia_1() from _rcall_ep04_dialogues3_family_olivia_1
    call ep04_dialogues3_family_olivia_2() from _rcall_ep04_dialogues3_family_olivia_2
    $ questHelp("house_26", True)
    call changeDayTime("morning") from _rcall_changeDayTime_33
    call ep04_dialogues3_family_olivia_3() from _rcall_ep04_dialogues3_family_olivia_3
    python:
        add_hook("Teleport_Bedroom_Landlord", "ep04_dialogues3_family_olivia_4", scene="house_floor2", label="morning_block")
        add_hook("Teleport_LivingRoomHall", "ep04_dialogues3_family_olivia_4", scene="house_floor1", label="morning_block")
        add_hook("Teleport_Kitchen", "ep04_dialogues3_family_olivia_4", scene="house_floor1", label="morning_block")
        add_hook("Teleport_Bathroom", "ep04_dialogues3_family_olivia_4", scene="house_floor1", label="morning_block")
        add_hook("Teleport_Sister1", "ep04_dialogues3_family_olivia_6", scene="house_floor2", label="morning_block")
        add_hook("Teleport_Sister2", "ep04_dialogues3_family_olivia_5", scene="house_floor2", label="morning_block", once=True)
        add_hook("Teleport_Street", "ep14_quests6_home3_kitchen", scene="house_floor1", label="morning_block")

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Street", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        questHelp("house_27")
        questHelp("house_28")

        move_object("Sister2", "empty")
        move_object("Sophie", "empty")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")

        map_enabled = False
        miniMapDisabled["HOUSE"] = ["House_Street"]

        questHelpDesc("house_desc11")
        sophieCallStage = 0
        cynthiaCallStage = 3


    return


label ep14_quests6_home3_kitchen:
    $ remove_hook(label="morning_block")
    $ questHelp("house_27", True)
    if ep14_sister2_room_visited != True:
        $ questHelp("house_28", False)
    call ep04_dialogues3_family_olivia_7() from _rcall_ep04_dialogues3_family_olivia_7
    call changeDayTime("day") from _rcall_changeDayTime_34
    $ sister2RoomDoorLocked = True
    python:
        sister1RoomDoorLocked = True
        landLordRoomDoorLocked = True
        move_object("Sister2", "house_sister2")
        move_object("Sophie", "house_bedroom_landlord")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        miniMapDisabled["HOUSE"] = []
        questHelp("college_31")
    $ map_enabled = True
    $ cynthiaCallStage = 0
    $ autorun_to_object("ep04_dialogues5_college_emily_3", scene="house_floor2")
    $ emilyCallStage = 3
    $ add_hook("phone_close", "ep14_quests6_beach_emily1", scene="phone", label="emily_dating1")
    $ add_hook("enter_scene", "ep14_quests6_beach_emily1", scene="beach_loungers", label="emily_dating1")
    $ add_hook("Teleport_Beach_Park", "ep04_dialogues5_college_emily_3a", scene="beach_loungers", label="emily_dating1")
    $ unfocus_map()
    $ focus_map("Teleport_BEACH", "ep04_dialogues5_college_emily_3")
    call change_scene("house_floor2", "Fade_long") from _rcall_change_scene_147
    return False

label ep14_quests6_beach_emily1:
    if scene_name != "beach_loungers" or ep14_call_emily_flag != True:
        return
    $ remove_hook(label="emily_dating1")
    $ emilyCallStage = 0
    call ep04_dialogues5_college_emily_6() from _rcall_ep04_dialogues5_college_emily_6
    $ questHelpDesc("college_desc11", "college_desc14")
    $ questHelp("college_31", True)
    $ add_hook("Teleport_Coridor1", "ep04_dialogues5_college_emily_6a", scene="college_street", label="college_block", quest="day7")
    $ unfocus_map()
    if _return == 2:
        $ autorun_to_object("ep04_dialogues5_college_emily_6a", scene="mall_street")
        call locations_mall1() from _rcall_locations_mall1_1
        call map_init_mall() from _rcall_map_init_mall_1
        call process_change_map_location("MALL") from _rcall_process_change_map_location_5
        python:
            clear_object_follow_all()
            move_object("Whore", "empty")
            set_object_follow("Teleport_Map", scene="mall_street")
            set_object_follow("Teleport_PARK", scene="map")

        call change_scene("mall_street", "Fade_long") from _rcall_change_scene_148
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_21
    else:
        python:
            clear_object_follow_all()
            set_object_follow("Teleport_Beach_Park", scene="beach_loungers")
            set_object_follow("Teleport_PARK", scene="map")
        $ autorun_to_object("ep04_dialogues5_college_emily_6a", scene="beach_loungers")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_22

    $ emilyCallStage = 0
    $ questHelp("house_29")
    $ add_hook("Bed", "ep14_quests8_sleep", scene="house_bedroom_mc", label="sleep_v4")

    return

label ep14_quests7_mall1:
    if day_time_idx < 2:
        $ remove_hook()
        call ep04_dialogues7_work_becky_1a() from _rcall_ep04_dialogues7_work_becky_1a
    return
label ep14_quests7_mall2:
    if day_time_idx >= 2:
        $ remove_hook()
        call ep04_dialogues7_work_becky_1b() from _rcall_ep04_dialogues7_work_becky_1b
    return
label ep14_quests7_whore_mall1:
    if ep14_mall_becky_lastday == 0:
        call ep04_dialogues7_work_becky_1() from _rcall_ep04_dialogues7_work_becky_1
    else:
        call ep04_dialogues7_work_becky_2() from _rcall_ep04_dialogues7_work_becky_2
    $ questHelp("becky_1", True)
    $ ep14_mall_becky_lastday = day
    return False

label ep14_quests8_sleep:
    if day_time_idx < 2:
        return
    $ remove_hook(label="sleep_v4")
    $ remove_hook(quest="day7")
    call ep04_dialogues7_work_becky_3() from _rcall_ep04_dialogues7_work_becky_3
    call ep03_dialogues3_family_evening_4() from _rcall_ep03_dialogues3_family_evening_4_2
    call ep15_update_init()
    return False
#    jump end_update
