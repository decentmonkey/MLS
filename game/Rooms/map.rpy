default map_source_scene = ""
default map_source_scene_hud_preset = ""
default map_scene = "House"
default previous_map_scene = ""
default target_map_scene = ""
default movingByCar = False
default visitedPlaces = {}
default mapFocusedObjects = []
default mapChangedFlag = True
default mapChangedTeleportFlag = False
default map_hud_preset_current = "map"
default mapStreetCheckShowing = False
default mapTeleportForcedCarSound = False

init python:
    def checkMapVisited(scene_name):
        if visitedPlaces.has_key(scene_name):
            return True
        return False

label map_street_scene_visibility_check: #проверка того надо-ли показывать значок вызова карты в локациях не улица
    if sceneIsStreet == True or scene_name == "house_bedroom_mc":
        $ mapStreetCheckShowing = True
        return
    $ mapStreetCheckShowing = False
    return

label map_show(car=False):
    $ miniMapData = []
    if checkDialogueExists() == True:
        return
    $ movingByCar = car
    call define_autorun() from _call_define_autorun_1

    $ map_source_scene = scene_name
    if hud_preset_current != map_hud_preset_current:
        $ map_source_scene_hud_preset = hud_preset_current
    $ hud_preset_current = map_hud_preset_current
    call change_scene("map", "Fade", "open_map") from _call_change_scene_22
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    return

label map_close:
    $ hud_preset_current = map_source_scene_hud_preset
    call change_scene(map_source_scene, "Fade", "open_map") from _call_change_scene_86
    return

label map:
    $ scene_name = "map"
    $ scene_caption = ""
    $ scene_image = "scene_Map" + day_suffix

    call define_hudpresets() from _call_define_hudpresets_1
    $ clear_scene_from_objects(scene_name)
    if hud_presets[hud_preset_current]["display_closemap"] == True:
        $ add_object_to_scene("Close", {"type" : 2, "img_overlay": "map_close" + res.suffix, "base":"map_close_hover" + res.suffix, "click" : "map_environment", "actions" : "l", "zorder":10, "xsprite":1839, "ysprite":17}, scene="map", owner=owner)

    python:
        for key, val in map_objects.items():
            stateSuffix = {
                "invisible": False,
                "visible" : "",
                "active" : "_active",
                "disabled" : "_disabled",
            }
            if stateSuffix[val["state"]] != False:
                add_object_to_scene(key, {"type":3, "text" : val["text"], "xpos" : val["xpos"], "ypos" : (val["ypos"] - 95), "xsprite":val["xpos"], "ysprite":val["ypos"], "img_overlay": val["base"] + stateSuffix[val["state"]] + res.suffix, "base":val["base"] + stateSuffix[val["state"]] + "_hover" + res.suffix, "click" : "map_environment", "sprite_align":"dc", "high_sprite_hover": True, "layout" : "map" + stateSuffix[val["state"]]}, scene="map", owner=owner)

    return


label map_environment:
    if obj_name == "Close":
        call map_close() from _call_map_close
        return
    if obj_name == "Teleport_" + map_scene:
        call map_close() from _call_map_close_1
        return
    call process_hooks("map_teleport", "global") from _call_process_hooks_12 #хук перед телепортом из карты
    if _return == False: #если отмена, то закрываем карту
        call map_close() from _call_map_close_2
        return

    if obj_name == "Teleport_HOUSE":
        call process_drive_teleport("HOUSE", "house_street") from _rcall_process_drive_teleport
        return
    if obj_name == "Teleport_HOUSE_FRIEND":
        call process_drive_teleport("HOUSE_FRIEND", "housefriend_street") from _rcall_process_drive_teleport_1
        return
    if obj_name == "Teleport_COLLEGE":
        call process_drive_teleport("COLLEGE", "college_street") from _rcall_process_drive_teleport_2
        return
    if obj_name == "Teleport_BEACH":
        call process_drive_teleport("BEACH", "beach_loungers") from _rcall_process_drive_teleport_3
        return
    if obj_name == "Teleport_PARK":
        call process_drive_teleport("PARK", "beach_park") from _rcall_process_drive_teleport_4
        return
    if obj_name == "Teleport_DAISY":
        call process_drive_teleport("DAISY", "daisy_street") from _rcall_process_drive_teleport_5
        return
    if obj_name == "Teleport_ARNIE":
        call process_drive_teleport("ARNIE", "arnie_street") from _rcall_process_drive_teleport_6
        return
    if obj_name == "Teleport_MALL":
        call process_drive_teleport("MALL", "mall_street") from _rcall_process_drive_teleport_7
        return
        
    m "drive!"
    return


label process_drive_teleport(in_target_map_scene, in_target_scene):
    $ previous_map_scene = map_scene
    $ target_map_scene = in_target_map_scene
    $ target_scene = in_target_scene
    python:
        for item1 in map_objects:
            if map_objects[item1]["state"] == "active":
                map_objects[item1]["state"] = "visible"
    $ map_objects["Teleport_" + target_map_scene]["state"] = "active"
    $ map_scene = target_map_scene
    $ hud_preset_current = map_source_scene_hud_preset
    $ mapChangedFlag = True
    if mapTeleportForcedCarSound == False:
        call start_walk_direct() from _call_start_walk_direct
    else:
        call start_drive_direct() from _rcall_start_drive_direct
    $ mapChangedFlag = True
    call process_hooks("map_teleport_after", "global") from _rcall_process_hooks_40
    return

label process_drive_teleport_direct(in_target_map_scene, in_target_scene):
    $ previous_map_scene = map_scene
    $ target_map_scene = in_target_map_scene
    $ target_scene = in_target_scene
    python:
        for item1 in map_objects:
            if map_objects[item1]["state"] == "active":
                map_objects[item1]["state"] = "visible"
    $ map_objects["Teleport_" + target_map_scene]["state"] = "active"
    $ hud_preset_current = map_source_scene_hud_preset
    call start_drive_direct() from _call_start_drive_direct
    if driveCanceled == True:
        return
    $ visitedPlaces[target_map_scene] = True
    $ mapChangedFlag = True
    call process_hooks("map_teleport_after", "global") from _rcall_process_hooks_41
    return
label process_change_map_location(target_map_scene):
    $ map_objects["Teleport_" + map_scene]["state"] = "visible"
    python:
        for obj1 in map_objects:
            if map_objects[obj1]["state"] == "active":
                map_objects[obj1]["state"] = "visible"
    $ map_objects["Teleport_" + target_map_scene]["state"] = "active"
    $ map_scene = target_map_scene
    $ mapChangedFlag = True
    return

label start_walk_direct():
    $ mapChangedTeleportFlag = True
    call change_scene(target_scene, "Fade_long", "run_stairs_floor") from _rcall_change_scene_115
    return

label map_init_beach:
    $ map_objects["Teleport_BEACH"] = {"text" : t_("ПЛЯЖ"), "xpos" : 883, "ypos" : 819, "base" : "map_marker", "state" : "visible"}
    return

label map_init_park:
    $ map_objects["Teleport_PARK"] = {"text" : t_("ПАРК"), "xpos" : 1354, "ypos" : 815, "base" : "map_marker", "state" : "visible"}
    return

label map_init_daisy:
    $ map_objects["Teleport_DAISY"] = {"text" : t_("ДОМ ДЕЙЗИ"), "xpos" : 1475, "ypos" : 305, "base" : "map_marker", "state" : "visible"}
    return

label map_init_arnie:
    $ map_objects["Teleport_ARNIE"] = {"text" : t_("ДОМ АРНИ"), "xpos" : 989, "ypos" : 569, "base" : "map_marker", "state" : "visible"}
    return

label map_init_mall:
    $ map_objects["Teleport_MALL"] = {"text" : t_("МОЛЛ"), "xpos" : 380, "ypos" : 325, "base" : "map_marker", "state" : "visible"}
    return