label college_wc_male:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_19
    $ scene_image = "scene_COLLEGE_WC_Male"
    return

label college_wc_male_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor4", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_wc_male_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="college_wc_male")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_wc_male_environment:
    if obj_name == "Teleport_Coridor4":
        call change_scene("college_coridor4") from _rcall_change_scene_82
        return
    return
