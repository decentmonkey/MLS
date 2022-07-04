default persistent.pause_before_change_slide = False
default persistent.auto_clipboard = False
default persistent.music_scenes = True

default map_enabled = True
default map_disabled_forced = False
default last_map_enabled = True

define fadehold = Fade(0.5, 1.0, 0.5)
define fadelong = Fade(0.5, 0.5, 0.5)
define diss = Dissolve(0.5)

default define_version = 1
default define_version_current = 0

default text_button_default_layout = "default"

default clickHoldMode = True #блокировка клика после диалога, если мышкой не двигали
default clickHoldFlag = False
default clickHoldLastTime = 0
default clickHoldLastMouseX = 0
default clickHoldLastMouseY = 0
default screenActionHappened = False
default obj_name = ""

default bitchmeterValue = 0
default bitchmeter_places = {}
default corruption = 0
default corruptionMax = 1000
default corruption_places = {}
default char_progress_stored = {}
default char_data = False
default dialogue_active_flag = False

define imagesSizesCache = {}
default sceneSpriteSurfacesCacheIdle = {}
default sceneSpriteSurfacesCache = {}
default sceneSpriteSurfacesCacheSceneName = False
default assetsStorageDirectory = False
default menuName = False
default currentMenuItem = -1
default char_info = {}
default i = 0

label characters_init:
    $ char_info = {
#        "Biff":{"name": t_("Биф"), "name_orig":"Биф", "enabled":True, "face":"Face_biff", "style":"char_face_style1_orange",  "bar_suffix": "orange", "level":1, "current_progress":0, "caption": t_("Биф обещал взять Монику работать в офис."), "max_progress":100, "uplevel_label":"biffProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":t_("Work in progress...")},
    }

    $ char_progress_stored = {}
    return

label define_autorun:
    $ define_version_current = define_version

    $ actions_objects = { #иконки действий
        "l" : {
            "description" : t_("Смотреть"),
            "label_suffix" : "_use",
            "icon" : "/Icons/eye" + res.suffix + ".png",
        },
        "h" : {
            "description" : t_("Взять"),
            "label_suffix" : "_hand",
            "icon" : "/Icons/hand" + res.suffix + ".png"
        },
        "t" : {
            "description" : t_("Говорить"),
            "label_suffix" : "_talk",
            "icon" : "/Icons/talk3" + res.suffix +".png",
        },
        "w" : {
            "description" : t_("Идти"),
            "label_suffix" : "_walk",
            "icon" : "/Icons/walk" + res.suffix + ".png",
        },
        "i" : {
            "description" : t_("Инфо"),
            "label_suffix" : "_info",
            "icon" : "/Icons/info" + res.suffix + ".png",
        }

    }


    $ text_button_layouts = {
        "default": {
            "text_button.spacing1" : gui.resolution.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.text_button.spacing2,
            "text_button.style" : gui.resolution.text_button.style,
            "text_button.force_hovered.style" : gui.resolution.text_button.force_hovered.style,
            "text_button.padding" : gui.resolution.text_button.padding
        },

        "map" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_disabled" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_disabled.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_disabled.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_active" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_active.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_active.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_house" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_active.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_active.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        }
    }

    call define_hudpresets() from _call_define_hudpresets

    $ calendar_days = [t_("Пн"), t_("Вт"), t_("Ср"), t_("Чт"), t_("Пт"), t_("Сб"), t_("Вс")]
    return

label define_hudpresets:
    $ hud_presets = {
        "default" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : True,
            "display_scene_map" : True,
            "display_bitchmeter" : True,
            "display_closemap" : True,
            "display_face_hud": False,
            "display_phone": True
        },
        "default_map_disabled" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : True,
            "display_scene_map" : False,
            "display_bitchmeter" : True,
            "display_closemap" : True,
            "display_face_hud": False,
            "display_phone": False
        },
        "map": {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : False,
            "display_scene_map" : False,
            "display_bitchmeter" : False,
            "display_closemap" : True,
            "display_face_hud": False,
            "display_phone": False
        },
        "map_locked" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : False,
            "display_scene_map" : False,
            "display_bitchmeter" : False,
            "display_closemap" : False,
            "display_face_hud": False,
            "display_phone": False
        },
    }
    return

label object_follow_array_init:
    python:
        object_follow_array = {
            "World": {
                "arnie_street" : "ARNIE",
                "house_street" : "HOUSE",
                "housefriend_street" : "HOUSE_FRIEND",
                "college_street" : "COLLEGE",
                "beach_loungers" : "BEACH",
                "beach_park" : "PARK",
                "daisy_street" : "DAISY",
                "arnie_street" : "ARNIE",
                "mall_street" : "MALL"
            },

            "arnie_street" : {
                "World" : "Teleport_Map",
                "arnie_livingroom" : "Teleport_LivingRoom"
            },
            "beach_loungers" : {
                "World" : "Teleport_Map",
                "beach_park" : "Teleport_Beach_Park"
            },
            "beach_park" : {
                "World" : "Teleport_Map",
                "beach_loungers" : "Teleport_Beach_Loungers"
            },
            "college_algebra" : {
                "college_coridor5" : "Teleport_Coridor5"
            },
            "college_artclass" : {
                "Teleport_Coridor5" : "Teleport_Coridor5"
            },
            "college_biology" : {
                "college_coridor1" : "Teleport_Coridor1"
            },
            "college_chemistry" : {
                "college_coridor2" : "Teleport_Coridor2"
            },
            "college_computer" : {
                "college_coridor7" : "Teleport_Coridor7"
            },
            "college_coridor1_locker_mc" : {
                "college_coridor1" : "Teleport_Coridor1"
            },
            "college_coridor1" : {
                "college_biology" : "Teleport_Biology",
                "college_hall" : "Teleport_Hall",
                "college_coridor1_locker_mc" : "Teleport_LockerMC",
                "college_coridor3" : "Teleport_Stairs",
                "college_street" : "Teleport_Street"
            },
            "college_coridor2" : {
                "college_coridor3" : "Teleport_Stairs",
                "college_coridor4" : "Teleport_Coridor4",
                "college_gym" : "Teleport_Gym",
                "college_medical" : "Teleport_Medical",
                "college_chemistry" : "Teleport_Chemistry"
            },
            "college_coridor3" : {
                "college_coridor7" : "Teleport_Floor2",
                "college_roof" : "Teleport_Floor2",
                "college_coridor10" : "Teleport_Floor2",
                "college_coridor3" : "Teleport_Floor2",

                "college_coridor1" : "Teleport_Coridor1",
                "college_coridor2" : "Teleport_Coridor2",
                "college_geography" : "Teleport_Geography"
            },
            "college_coridor4" : {
                "college_coridor2" : "Teleport_Coridor2",
                "college_pool" : "Teleport_Pool",
                "college_locker_girl" : "Teleport_Locker_Girl",
                "college_locker_boy" : "Teleport_Locker_Boy",
                "college_wc_male" : "Teleport_WC_Male",
                "college_wc_female" : "Teleport_WC_Female"
            },
            "college_coridor5" : {
                "college_coridor6" : "Teleport_Coridor6",
                "college_algebra" : "Teleport_Algebra",
                "college_artclass" : "Teleport_ArtClass"
            },
            "college_coridor6" : {
                "college_coridor7" : "Teleport_Coridor7",
                "college_english" : "Teleport_English",
                "college_physics" : "Teleport_Physics",
                "college_coridor5" : "Teleport_Coridor5"
            },
            "college_coridor7" : {
                "college_coridor7" : "Teleport_Stairs",
                "college_roof" : "Teleport_Stairs",
                "college_coridor10" : "Teleport_Stairs",
                "college_coridor3" : "Teleport_Stairs",

                "college_computer" : "Teleport_Computer",
                "college_coridor6" : "Teleport_Coridor6"
            },
            "college_coridor8" : {
                "college_coridor9" : "Teleport_Coridor9",
                "college_principal_secretary" : "Teleport_Principal_Secretary"
            },
            "college_coridor9" : {
                "college_coridor10" : "Teleport_Coridor10",
                "college_teachers" : "Teleport_Teachers",
                "college_library" : "Teleport_Library",
                "college_coridor8" : "Teleport_Coridor8"
            },
            "college_coridor10" : {
                "college_coridor7" : "Teleport_Stairs",
                "college_roof" : "Teleport_Stairs",
                "college_coridor10" : "Teleport_Stairs",
                "college_coridor3" : "Teleport_Stairs",

                "college_coridor9" : "Teleport_Coridor9",
                "college_utilityroom" : "Teleport_UtilityRoom"
            },
            "college_english" : {
                "college_coridor6" : "Teleport_Coridor6"
            },
            "college_france" : {
                "college_coridor1" : "Teleport_Coridor"
            },
            "college_geography" : {
                "college_coridor3" : "Teleport_Coridor3"
            },
            "college_gym" : {
                "college_coridor2" : "Teleport_Coridor2"
            },
            "college_hall" : {
                "college_coridor1" : "Teleport_Coridor1"
            },
            "college_library" : {
                "college_coridor9" : "Teleport_Coridor9"
            },
            "college_locker_boy" : {
                "college_coridor4" : "Teleport_Coridor4"
            },
            "college_locker_girl" : {
                "college_coridor4" : "Teleport_Coridor4"
            },
            "college_medical" : {
                "college_coridor2" : "Teleport_Coridor2"
            },
            "college_physics" : {
                "college_coridor6" : "Teleport_Coridor6"
            },
            "college_pool" : {
                "college_coridor4" : "Teleport_Coridor4"
            },
            "college_principal_secretary" : {
                "college_coridor8" : "Teleport_Coridor8",
                "college_principal" : "Teleport_Principal"
            },
            "college_principal" : {
                "college_principal_secretary" : "Teleport_Principal_Secretary"
            },
            "college_roof" : {
                "college_coridor10" : "Teleport_Coridor10"
            },
            "college_street" : {
                "World" : "Teleport_Map",
                "college_coridor1" : "Teleport_Coridor1",
                "college_streetyard" : "Teleport_StreetYard"
            },
            "college_streetyard" : {
                "college_street" : "Teleport_Street"
            },
            "college_teachers" : {
                "college_coridor9" : "Teleport_Coridor9"
            },
            "college_utilityroom" : {
                "college_coridor10" : "Teleport_Coridor10"
            },
            "college_wc_female" : {
                "college_coridor4" : "Teleport_Coridor4"
            },
            "college_wc_male" : {
                "college_coridor4" : "Teleport_Coridor4"
            },

            "daisy_street" : {
                "World" : "Teleport_Map",
                "Teleport_LivingRoom" : "daisy_livingroom"
            },

            "house_bathroom" : {
                "house_floor1" : "Teleport_Floor1"
            },

            "house_bedroom_landlord" : {
                "house_floor2" : "Teleport_Floor2"
            },
            "house_bedroom_mc_onbed" : {
                "house_bedroom_mc" : "Teleport_Bedroom_MC"
            },
            "house_bedroom_mc_tablenear" : {
                "house_bedroom_mc" : "Teleport_Bedroom_MC"
            },
            "house_bedroom_mc" : {
                "house_floor2" : "Teleport_Floor2"
            },
            "house_floor1" : {
                "house_livingroomhall" : "Teleport_LivingRoomHall",
                "house_kitchen" : "Teleport_Kitchen",
                "house_bathroom" : "Teleport_Bathroom",
                "house_street" : "Teleport_Street",
                "house_floor2" : "Teleport_Floor2"
            },
            "house_floor2" : {
                "house_sister2" : "Teleport_Sister2",
                "house_sister1" : "Teleport_Sister1",
                "house_bedroom_landlord" : "Teleport_Bedroom_Landlord",
                "house_floor1" : "Teleport_Floor1",
                "house_bedroom_mc" : "Teleport_Bedroom_MC"
            },
            "house_garage" : {
                "house_street" : "Teleport_House_Street"
            },
            "house_kitchen" : {
                "house_floor1" : "Teleport_Floor1"
            },
            "house_livingroomhall" : {
                "house_floor1" : "Teleport_Floor1"
            },
            "house_sister1" : {
                "house_floor2" : "Teleport_Floor2"
            },
            "house_sister2" : {
                "house_floor2" : "Teleport_Floor2"
            },
            "house_storeroom" : {
                "house_street" : "Teleport_Street"
            },
            "house_street" : {
                "World" : "Teleport_Map",
                "house_floor1" : "Teleport_Floor1",
                "house_garage" : "Teleport_Garage",
                "house_storeroom" : "Teleport_StoreRoom"
            },
            "housefriend_bedroom_parents" : {
                "housefriend_kitchen" : "Teleport_Kitchen"
            },
            "housefriend_kitchen" : {
                "housefriend_livingroom" : "Teleport_LivingRoom",
                "housefriend_bedroom_parents" : "Teleport_Bedroom_Parents"
            },
            "housefriend_livingroom" : {
                "housefriend_street" : "Teleport_Street",
                "housefriend_kitchen" : "Teleport_Kitchen",
                "housefriend_room" : "Teleport_Room"
            },
            "housefriend_room" : {
                "housefriend_livingroom" : "Teleport_LivingRoom"
            },
            "housefriend_street" : {
                "World" : "Teleport_Map",
                "housefriend_livingroom" : "Teleport_LivingRoom"
            },

            "mall_street" : {
                "World" : "Teleport_Map"
            }


        }
        object_follow_array_floors = {
            "house_bedroom_mc" : "House_Bedroom_MC",
            "house_floor2" : "Floor2",
            "house_floor1" : "Floor1",
            "house_street" : "House_Street",

            "college_coridor10" : "COLLEGE_Floor3",
            "college_coridor7" : "COLLEGE_Floor2",
            "college_coridor3" : "COLLEGE_Floor1",
            "college_street" : "COLLEGE_Street"
        }

    return

label run_after_load:
    call define_hudpresets() from _call_define_hudpresets_2
    call questLog_init() from _call_questLog_init_1
    return

label game_init:
    $ image_screen_scene_flag = False
    $ show_scene_loop_flag = False
    $ interface_blocked_flag = False
    define dissolve1 = Dissolve(0.5)
    default last_dialogue_character = "bardi"

    $ width_half = config.screen_width / 2

    $ preferences.show_empty_window = False
    $ config.log = True

    call define_autorun() from _call_define_autorun_2

#    $ define_inventory_object("papers", {"description" : t_("Papers"), "label_suffix" : "_use_papers", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/big_papers" + res.suffix + ".png"})

    $ scene_transition = False
    $ scene_sound = False
#    $ add_inventory("phone", 5, True)
#    $ add_inventory("shovel", 5, True)
#    $ remove_inventory("papers", 3, True)

    return

label showLog(str):
    show screen notify(str)

    return
