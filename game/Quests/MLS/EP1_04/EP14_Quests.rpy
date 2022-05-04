default ep14_update_init_flag = False

default sophieKitchenHelpEnabled1 = False
default sophieKitchenHelpLastDay = 0

default ep14_bikerent_work_count = 0
default ep14_bikerent_work_lastday = 0

default ep14_home_afterwork_stage = 0

default collegeLastDay = 0

label ep14_update_init:
    if ep14_update_init_flag == True:
        return
    $ day = day + 1
    $ ep14_update_init_flag = True
    $ remove_hook(quest="college_day3")
    $ remove_hook(quest="day4")
    call change_scene("house_bedroom_mc")
    call process_change_map_location("HOUSE")
    call changeDayTime("morning")
    call ep04_dialogues1_family_sophie_1a()
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

    call refresh_scene_fade_long()
    return

label ep14_quests1_sophie:
    call ep04_dialogues1_family_sophie_1()
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

    call refresh_scene_fade()
    return

label ep14_quests2_college:
    call ep04_dialogues6_college_sarah_1a()
    $ remove_hook(label="ep14_quests2_college")
    $ clear_object_follow_all()
    $ questHelp("college_29", True)
    call ep04_dialogues6_college_sarah_1()
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Gym", scene="college_coridor2")
    $ miniMapEnabledOnly = ["none"]
    $ set_active("Teleport_Stairs", False, scene="college_coridor2")
    $ add_hook("before_open", "ep14_quests2_college2_gym", scene="college_gym", quest="day5")
    $ unfocus_map()


    call change_scene("college_coridor2", "Fade_long")


    return False

label ep14_quests2_college2_gym:
    $ clear_object_follow_all()
    call ep04_dialogues6_college_sarah_2()
    $ set_active("Teleport_Stairs", True, scene="college_coridor2")
    $ set_object_follow("Teleport_Coridor2", scene="college_gym")
    $ set_active("Teleport_Coridor2", True, scene="college_gym")
    $ miniMapEnabledOnly = []
    $ add_hook("Teleport_Coridor2", "ep14_quests2_college3_end", scene="college_gym", once=True)
    $ questHelpDesc("college_desc13")

    return False


label ep14_quests2_college3_end:
    $ clear_object_follow_all()
    call ep03_dialogues2_college_10b()
    call changeDayTime("day")
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
    call change_scene("college_street")
    return False

label ep14_quests3_daisy1:
    if day_time_idx > 1:
        call ep04_dialogues4_family_daisy_1a()
        return False
    if mlsBardiFamilyV4Daisy2 > 0:
        call ep04_dialogues4_family_daisy_3()
        if _return == -1:
            return False
        call ep14_quests4_evening_afterwork()
    else:
        call ep04_dialogues4_family_daisy_1()
        call ep04_dialogues4_family_daisy_2()
        $ questHelp("work_4", True)
        $ questHelpDesc("work_desc0", False)
        $ questHelpDesc("work_desc2", "work_desc3")
        call phone_contact6()
        $ daisyCallStage = 1
        $ sophieCallStage = 5
        if day != 9:
            $ phone_focus_icon(True)
            $ phone_incoming_call("Sophie")

        call ep14_quests4_evening_afterwork()
    return False

label ep14_quests3_bikerent1:
    
    if ep14_bikerent_work_count == 1:
        call ep04_dialogues8_work_bikerental_3()
        $ ep14_bikerent_work_count = 2
        $ questHelpDesc("work_desc4")
    if ep14_bikerent_work_count == 0:
        call ep04_dialogues8_work_bikerental_1()
        $ ep14_bikerent_work_count = 1
        $ sophieCallStage = 5
        if day != 9:
            $ phone_focus_icon(True)
            $ phone_incoming_call("Sophie")
        $ questHelp("work_5", True)
        $ questHelp("work_6")

    $ ep14_bikerent_work_lastday = day
    call ep14_quests4_evening_afterwork()
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
    call changeDayTime("evening")
    call refresh_scene_fade()

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
    call ep04_dialogues1_family_sophie_4()
    if _return == 1 or _return == 2:
        call changeDayTime("night")
    return False

label ep14_quests4_evening_sister2:
    if day_time_idx != 2 or get_active_objects("Sister2", scene="house_sister2") == False:
        return
    call ep02_dialogues4_family_evening_4()
    return False



#### День 2 (вторник)

label ep14_quests4_evening_bed:
    if day_time_idx < 2:
        return
    call ep03_dialogues3_family_evening_4()
    $ clear_object_follow_all()
    $ remove_hook(quest="day5")
    $ questHelp("house_25", True)
    call changeDayTime("morning")
    call ep04_dialogues2_family_cynthia_1a()
    $ sophieCallStage = 0
    $ add_hook("exit_scene", "ep14_quests5_sister2", scene="house_bedroom_mc", once=True)
    $ map_enabled = False
    call refresh_scene_fade_long()
    return False

label ep14_quests5_sister2:
    call ep04_dialogues2_family_cynthia_1()
    call ep04_dialogues2_family_cynthia_2()
    call change_scene("house_bedroom_mc", "Fade_long")
    $ map_enabled = True
    $ miniMapDisabled["HOUSE"] = []
    $ remove_hook(label="house_block")
    $ questHelp("college_30")

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
    call ep04_dialogues6_college_sarah_1a()
    call ep04_dialogues5_college_emily_1()

    call ep03_dialogues2_college_10b()
    call changeDayTime("day")
    $ clear_object_follow_all()
    $ emilyCallStage = 2
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


    call change_scene("college_street", "Fade_long")
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
        call changeDayTime("evening")
    return

label ep14_quests6_home2_sister1:
    $ clear_object_follow_all()
    $ remove_hook(quest="day6")
    call ep04_dialogues3_family_olivia_1()
    call ep04_dialogues3_family_olivia_2()
    $ questHelp("house_26", True)
    call changeDayTime("morning")
    call ep04_dialogues3_family_olivia_3()
    python:
        add_hook("Teleport_Bedroom_Landlord", "ep04_dialogues3_family_olivia_4", scene="house_floor2", label="morning_block")
        add_hook("Teleport_LivingRoomHall", "ep04_dialogues3_family_olivia_4", scene="house_floor1", label="morning_block")
        add_hook("Teleport_Kitchen", "ep04_dialogues3_family_olivia_4", scene="house_floor1", label="morning_block")
        add_hook("Teleport_Bathroom", "ep04_dialogues3_family_olivia_4", scene="house_floor1", label="morning_block")
        add_hook("Teleport_Sister1", "ep04_dialogues3_family_olivia_6", scene="house_floor2", label="morning_block")
        add_hook("Teleport_Sister2", "ep04_dialogues3_family_olivia_5", scene="house_floor2", label="morning_block")

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Street", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        map_enabled = False
        miniMapDisabled["HOUSE"] = ["House_Street"]


    return
