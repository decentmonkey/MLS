label house_bedroom_mc_tablenear:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_4
    $ scene_image = "scene_House_Bedroom_MC_TableNear[day_suffix]"
    return

label house_bedroom_mc_tablenear_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Typewriter", {"type" : 2, "base" : "House_Bedroom_MC_TableNear_Typewriter", "click" : "house_bedroom_mc_tablenear_environment", "actions" : "l", "zorder":0}, scene="house_bedroom_mc_tablenear")

    $ add_object_to_scene("Teleport_Bedroom_MC", {"type":3, "text" : t_("НАЗАД"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_bedroom_mc_tablenear_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bedroom_mc_tablenear")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bedroom_mc_tablenear_environment:
    if obj_name == "Teleport_Bedroom_MC":
        call change_scene("house_bedroom_mc") from _rcall_change_scene_87
        return
    if obj_name == "Typewriter":
        if day_time_idx < 2:
            imgfl 910318
        else:
            imgfl 910319
        call ep01_dialogues2_day1_family_1_5() from _rcall_ep01_dialogues2_day1_family_1_5
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_11
        return
    return
