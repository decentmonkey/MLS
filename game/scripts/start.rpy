define debugMode = False

default gameStage = 0
default gameSubStage = 0
default rain = False
default rainIntencity = 0
default lightning = False
default sceneIsStreet = False
default hudDaySkipToEveningEnabled = True
default objectives_list = []
default currentMusic = False
default currentMusicPriority = 0
default currentMusic2 = False
default currentMusic3 = False
default storedMusic = []
default storedMusicPriority = []
default day_time = "day"
default day_time_idx = 1
default day = 0
default week_day = 1
default owner = "Bardie"
default showObjectsNotOwner = True
default episode = 1
default notifList = []
default lastNotifTime = 0

default menu_corruption = []
default menu_price = []
default menu_bitchiness = []
default menu_required = {}

default hud_preset_current = "default"
default hud_preset_default = "default"
default minimap_coords_preset = 0
default blur_effect = False

default after_load_ready_to_render = False

default act = ""

default questLogGlobalEnabled = False

default homeButtonEnabled = True
default moneyDisplayEnabled = False
default phoneDisplayEnabled = True
default phoneEnabled = True
default phoneNotifications = []

default obj_follow_list = {}
default images_history_list = {}
default current_slide = False
define steamVersion = False
default rrmeterValue = 0

#temp vars
default maxRRMeter = 100

label start: #for blink here

    #new game
    $ after_load_ready_to_render = True
    $ refresh_list_files_forced()
    $ episode = 2
#    $ debugMode = True

    $ day = 1
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []
    $ owner = "Bardie"
    call game_init() from _rcall_game_init

    $ objectives_list = []
    $ map_objects = {
            "Teleport_HOUSE" : {"text" : t_("ДОМ"), "xpos" : 1580, "ypos" : 427, "base" : "map_marker_house", "state" : "visible"},
    }

    call characters_init() from _rcall_characters_init_1
    call locations_init() from _rcall_locations_init

#########

#    call ep02_dialogues1_family_1() # утро, комната Барди, душ
#    call ep02_dialogues1_family_2() # кухня, разговор с Софи


#########


    call define_hudpresets() from _rcall_define_hudpresets_2
    call questLog_init() from _rcall_questLog_init_2
    # обнуляем квестлог
    python:
        for i in range(0, len(questLogData)):
            questLogData[i][2] = False

    $ cloth = "CasualCloth1"
    $ cloth_type = "CasualCloth"
    $ bitchmeterValue = 280

    $ gameStage = 0
    $ gameSubStage = 0
    $ rain = False
    $ sceneIsStreet = False

    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1

    $ week_day = (day)%7
    if week_day == 0:
        $ week_day = 7

    $ day_suffix = ""
    $ money = 0.0

    $ showObjectsNotOwner = True
    $ faceHudImage = False
    $ hud_preset_current = "default"
    $ hud_preset_default = "default"
    $ minimap_coords_preset = 0
    $ miniMapEnabledOnly = []
    $ miniMapDisabled = {}
    $ miniMapDisabled2 = {}
    $ miniMapOfficeActivated = True
    $ miniMapTurnedOff2 = False

    $ scene_refresh_flag = True
    $ map_scene = "HOUSE"
    $ map_enabled = True
    $ map_disabled_forced = False
    $ scene_name = "none"
    $ api_scene_name = "none"

    $ scene_sound = False
    $ scene_transition = "Fade_long"


    call process_change_map_location("HOUSE") from _rcall_process_change_map_location_10

    $ questHelpActivated = True
    call questHelp_init() from _rcall_questHelp_init_2

#    $ add_hook("change_time_morning", "test1_morning", scene="global")
#    $ add_hook("change_time_day", "test1_day", scene="global")
#    $ add_hook("change_time_evening", "test1_evening", scene="global")
#    $ add_hook("change_time_night", "test1_night", scene="global")

#    $ add_hook("exit_scene", "test1_exit", scene="house_street")
#    $ add_hook("enter_scene", "test1_enter", scene="house_street")

    $ add_hook("before_open", "college_life", scene="college_street", label="college_life")
    $ add_hook("change_day_time", "college_life_change_daytime", scene="global", label="college_life", priority = 200)

    $ add_hook("change_time_morning", "house_life", scene="global", label="house_life", priority = 200)
    $ add_hook("change_time_day", "house_life", scene="global", label="house_life", priority = 200)
    $ add_hook("change_time_evening", "house_life", scene="global", label="house_life", priority = 200)
    $ add_hook("change_time_night", "house_life", scene="global", label="house_life", priority = 200)
    call house_life() from _rcall_house_life


#    call change_scene("house_street") from _rcall_change_scene_220
    call changeDayTime("day") from _rcall_changeDayTime_10

    call phone_init() from _rcall_phone_init_2
    call phone1() from _rcall_phone1
    call phone_instagram1() from _rcall_phone_instagram1
    $ camera_icon_enabled = False

    call change_scene("intro_beach", "Fade_long", False) from _rcall_change_scene_116
    call ep1_intro_quests1() from _rcall_ep1_intro_quests1

    $ set_active("Teleport_Garage", False, scene="house_street")
    $ set_active("Teleport_StoreRoom", False, scene="house_street")

#    $ map_objects["Teleport_HOUSE_FRIEND"] = {"text" : t_("ДОМ ШОНА"), "xpos" : 1303, "ypos" : 318, "base" : "map_marker", "state" : "visible"}
#    $ map_objects["Teleport_COLLEGE"] = {"text" : t_("КОЛЛЕДЖ"), "xpos" : 982, "ypos" : 268, "base" : "map_marker", "state" : "visible"}

#    $ set_object_follow("Teleport_Coridor1", scene="college_street")

#    music stop
#    call change_scene("college_street")

#    $ map_objects["Teleport_HOUSE_FRIEND"] = {"text" : t_("ДОМ ШОНА"), "xpos" : 1303, "ypos" : 318, "base" : "map_marker", "state" : "visible"}
#    $ map_objects["Teleport_COLLEGE"] = {"text" : t_("КОЛЛЕДЖ"), "xpos" : 982, "ypos" : 268, "base" : "map_marker", "state" : "visible"}
#    call changeDayTime("evening")
    jump show_scene


label empty_label:
    return

label test1:
    m "here"
    call changeDayTime("night") from _rcall_changeDayTime_11
    call refresh_scene_fade() from _rcall_refresh_scene_fade_11
    return

label test1_morning:
#    m "morning hooks!"
    return
label test1_day:
#    m "day hooks!"
    return
label test1_evening:
#    m "evening hooks!"
    return
label test1_night:
#    m "night hooks!"
    return

label test1_exit:
#    m "exit scene!"
    return
label test1_enter:
#    m "enter scene!"
    return





#
