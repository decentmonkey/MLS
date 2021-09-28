label college_utilityroom:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_UtilityRoom"
    return

label college_utilityroom_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor10", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_utilityroom_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="college_utilityroom")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_utilityroom_environment:
    if obj_name == "Teleport_Coridor10":
        call change_scene("college_coridor10")
        return
    return
