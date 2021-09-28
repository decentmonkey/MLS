label college_principal:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Principal"
    return

label college_principal_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_principal_environment", "actions" : "l", "zorder":10}, scene="college_principal")

    $ add_object_to_scene("Teleport_Principal_Secretary", {"type":3, "text" : t_("СЕКРЕТАРЬ"), "rarrow" : "arrow_down_2_a", "base":"COLLEGE_Principal_Teleport_Principal_Secretary", "click" : "college_principal_environment", "xpos" : 1474, "ypos" : 881, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_principal")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_principal_environment:
    if obj_name == "Teleport_Principal_Secretary":
        call change_scene("college_principal_secretary")
        return
    return
