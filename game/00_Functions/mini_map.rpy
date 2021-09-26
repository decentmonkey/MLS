default miniMapData = []
default miniMapSubst = {}
default miniMapEnabledOnly = []
default miniMapDisabled = {}
default miniMapDisabled2 = {}
default miniMapOfficeActivated = False
default miniMapTurnedOff2 = False
default miniMapOpened = False
default miniMapOpenButtonImg = "Open_Button_Map1"
default miniMapOpenButtonImg2 = "Open_Button_Map2"

default miniMapHousePreset = "default"

default minimapBettyFloor2Enabled = False
default minimapJuliaGenerateEnabled = False

label miniMapOpen:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = True
    show screen hud_minimap(miniMapData)
    return
label miniMapClose:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = False
    show screen hud_minimap(miniMapData)
    return

label miniMapHouseGenerate:
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_House_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_House_Map2"
    $ miniMapData = []
    if miniMapHousePreset == "default":
        if owner == "Bardie":
            $ miniMapData.append({"name":"House_Bedroom_MC", "caption":t_("МОЯ КОМНАТА"), "img":"House_Bedroom_MC_Map", "teleport_scene":"house_bedroom_mc", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Floor2", "caption":t_("ВТОРОЙ ЭТАЖ"), "img":"House_Floor2_Map", "teleport_scene":"house_floor2", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Floor1", "caption":t_("ПЕРВЫЙ ЭТАЖ"), "img":"House_Floor1_Map", "teleport_scene":"house_floor1", "teleport_type":"scene"})
            $ miniMapData.append({"name":"House_Street", "caption":t_("ДВОР ДОМА"), "img":"House_Street_Map", "teleport_scene":"house_street", "teleport_type":"scene"})
    return

label miniMapCOLLEGEGenerate:
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_COLLEGE_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_COLLEGE_Map2"
    $ miniMapData = []
    $ miniMapData.append({"name":"COLLEGE_Floor3", "caption":t_("ЭТАЖ 3"), "img":"COLLEGE_Coridor_10_Map", "teleport_scene":"COLLEGE_Coridor10", "teleport_type":"scene"})
    $ miniMapData.append({"name":"COLLEGE_Floor2", "caption":t_("ЭТАЖ 2"), "img":"COLLEGE_Coridor_7_Map", "teleport_scene":"COLLEGE_Coridor7", "teleport_type":"scene"})
    $ miniMapData.append({"name":"COLLEGE_Floor1", "caption":t_("ЭТАЖ 1"), "img":"COLLEGE_Coridor_3_Map", "teleport_scene":"COLLEGE_Coridor3", "teleport_type":"scene"})
    $ miniMapData.append({"name":"COLLEGE_Street", "caption":t_("ДВОР КОЛЛЕДЖА"), "img":"COLLEGE_Street_Map", "teleport_scene":"COLLEGE_Street", "teleport_type":"scene"})
    return


label miniMapDisabled(name, minimapCell):
    sound snd_ui_not_working
    return

label miniMapAddDisabled(name):
    if name not in miniMapDisabled:
        $ miniMapDisabled.append(name)
    return

label miniMapRemoveDisabled(name):
    if name in miniMapDisabled:
        $ miniMapDisabled.remove(name)
    return

label miniMapHouseGenerateTeleport(name, minimapCell):
    $ target_scene_name = minimapCell["teleport_scene"]
    $ target_scene_parent = scene_get_parent(target_scene_name)
    call process_hooks("exit_scene", scene_name) from _call_process_hooks_25
    if _return == False:
        call refresh_scene() from _call_refresh_scene_3
        return
    $ exitHookCalled = True
    call process_hooks("mimimap_teleport", "global") from _call_process_hooks_26 #хук до инициализации сцены
    if _return == False:
        call refresh_scene() from _call_refresh_scene_4
        return
    if interface_blocked_flag == True:
        return
#    $ print renpy.get_screen("say")
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    $ _return = True
    if miniMapSubst.has_key("all") and miniMapSubst["all"] != False:
        call expression miniMapSubst["all"] from _call_expression_9
    if miniMapSubst.has_key(name) and miniMapSubst[name] != False:
        call expression miniMapSubst[name] from _call_expression_10
    if _return != False:
        if minimapCell["teleport_type"] == "function":
            $ minimapTeleportButtonName = name
            call expression minimapCell["teleport_scene"] from _call_expression_11
        if minimapCell["teleport_type"] == "scene":
            call change_scene(minimapCell["teleport_scene"]) from _call_change_scene_150
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
