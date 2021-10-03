label college_coridor1_locker_mc:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_COLLEGE_Coridor_1_LockerMC"
    return

label college_coridor1_locker_mc_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Bunny", {"type" : 2, "base" : "COLLEGE_Coridor_1_LockerMC", "click" : "college_coridor1_locker_mc_environment", "actions" : "l", "zorder":3}, scene="college_coridor1_locker_mc")

    $ add_object_to_scene("Teleport_Coridor1", {"type":3, "text" : t_("НАЗАД"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_coridor1_locker_mc_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1_locker_mc")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor1_locker_mc_environment:
    if obj_name == "Teleport_Coridor1":
        call change_scene("college_coridor1", "Fade_long", "school_locker_close")
        return
    if obj_name == "Bunny":
        call ep01_dialogues3_day2_college_15b()
        $ open_secret_object("Bunny")
    return
