label college_coridor2:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_Coridor_2_base"
    return

label college_coridor2_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_coridor2_environment", "actions" : "l", "zorder":10}, scene="college_coridor2")

    $ add_object_to_scene("Teleport_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_coridor2_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor2")
    $ add_object_to_scene("Teleport_Coridor4", {"type":3, "text" : t_("РАЗДЕВАЛКИ"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_2_Teleport_Coridor4", "click" : "college_coridor2_environment", "xpos" : 1607, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor2")
    $ add_object_to_scene("Teleport_Gym", {"type":3, "text" : t_("СПОРТЗАЛ"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_2_Teleport_Gym", "click" : "college_coridor2_environment", "xpos" : 828, "ypos" : 200, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor2")
    $ add_object_to_scene("Teleport_Medical", {"type":3, "text" : t_("МЕД КАБИНЕТ"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_2_Teleport_Medical", "click" : "college_coridor2_environment", "xpos" : 266, "ypos" : 321, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor2")
    $ add_object_to_scene("Teleport_Chemistry", {"type":3, "text" : t_("ХИМИЯ"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_Coridor_2_Teleport_Chemistry", "click" : "college_coridor2_environment", "xpos" : 1402, "ypos" : 211, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor2")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor2_environment:
    if obj_name == "Teleport_Stairs":
        call change_scene("college_coridor3")
        return
    if obj_name == "Teleport_Coridor4":
        call change_scene("college_coridor4")
        return
    if obj_name == "Teleport_Gym":
        call change_scene("college_gym")
        return
    if obj_name == "Teleport_Medical":
        call change_scene("college_medical")
        return
    if obj_name == "Teleport_Chemistry":
        call change_scene("college_chemistry")
        return
    return
