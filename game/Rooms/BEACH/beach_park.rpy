label beach_park:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_BEACH_Park[day_suffix]"
    if day_time_idx <= 1:
        music city_park
    else:
        music night_ambience
    return

label beach_park_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("FatherFriend", {"type" : 2, "base" : "BEACH_Park_FatherFriend[day_suffix]", "click" : "beach_park_environment", "actions" : "l", "zorder":10}, scene="beach_park")
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "beach_park_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="beach_park")
    $ add_object_to_scene("Teleport_Beach_Loungers", {"type":3, "text" : t_("ПЛЯЖ"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "beach_park_environment", "xpos" : 1700, "ypos" : 855, "zorder":11, "teleport":True, "group":"teleports"}, scene="beach_park")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label beach_park_environment:
    if obj_name == "Teleport_Map":
        call map_show() from _rcall_map_show_6
        return
    if obj_name == "Teleport_Beach_Loungers":
        call process_change_map_location("BEACH") from _rcall_process_change_map_location_3
        call change_scene("beach_loungers", "Fade_long", "run_stairs_floor") from _rcall_change_scene_141
        return
    return
