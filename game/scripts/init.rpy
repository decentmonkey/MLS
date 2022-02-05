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
