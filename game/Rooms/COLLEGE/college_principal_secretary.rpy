label college_principal_secretary:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Principal_Secretary"
    return

label college_principal_secretary_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_principal_secretary_environment", "actions" : "l", "zorder":10}, scene="college_principal_secretary")

    $ add_object_to_scene("Teleport_Coridor8", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_principal_secretary_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_principal_secretary")
    $ add_object_to_scene("Teleport_Principal", {"type":3, "text" : t_("КАБИНЕТ ДИРЕКТОРА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Principal_Secretary_Teleport_Principal", "click" : "college_principal_secretary_environment", "xpos" : 616, "ypos" : 199, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_principal_secretary")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_principal_secretary_environment:
    if obj_name == "Teleport_Coridor8":
        call change_scene("college_coridor8")
        return
    if obj_name == "Teleport_Principal":
        call change_scene("college_principal")
        return
    return
