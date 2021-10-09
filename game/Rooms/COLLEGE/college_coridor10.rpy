label college_coridor10:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_1
    $ scene_image = "scene_COLLEGE_Coridor_10_base"
    return

label college_coridor10_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_10_Teleport_Stairs", "click" : "college_coridor10_environment", "xpos" : 1765, "ypos" : 562, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor10")
    $ add_object_to_scene("Teleport_Coridor9", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_10_Teleport_Coridor9", "click" : "college_coridor10_environment", "xpos" : 525, "ypos" : 959, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor10")
    $ add_object_to_scene("Teleport_UtilityRoom", {"type":3, "text" : t_("КАБИНЕТ ЗАВХОЗА"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_10_Teleport_UtilityRoom", "click" : "college_coridor10_environment", "xpos" : 1600, "ypos" : 1002, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor10")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor10_environment:
    if obj_name == "Teleport_Stairs":
        call college_stairs_menu() from _rcall_college_stairs_menu
        return
    if obj_name == "Teleport_Coridor9":
        call change_scene("college_coridor9") from _rcall_change_scene_29
        return
    if obj_name == "Teleport_UtilityRoom":
        call change_scene("college_utilityroom") from _rcall_change_scene_30
        return
    return
