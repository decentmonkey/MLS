label college_wc_female:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_18
    $ scene_image = "scene_COLLEGE_WC_Female"
    return

label college_wc_female_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor4", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_wc_female_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="college_wc_female")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_wc_female_environment:
    if obj_name == "Teleport_Coridor4":
        call change_scene("college_coridor4") from _rcall_change_scene_81
        return
    return
