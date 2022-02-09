label beach_loungers:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_BEACH_Loungers[day_suffix]"
    music audio_beach_waves1
    return

label beach_loungers_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "beach_loungers_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="beach_loungers")
    return

label beach_loungers_init2:
    $ add_object_to_scene("Teleport_Beach_Park", {"type":3, "text" : t_("ПАРК"), "larrow" : "arrow_left_2", "base":"empty", "click" : "beach_loungers_environment", "xpos" : 245, "ypos" : 847, "zorder":11, "teleport":True, "group":"teleports"}, scene="beach_loungers")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label beach_loungers_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_Beach_Park":
        call process_change_map_location("PARK")
        call change_scene("beach_park", "Fade_long", "run_stairs_floor")
        return
    return
