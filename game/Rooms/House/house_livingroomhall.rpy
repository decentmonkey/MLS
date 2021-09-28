label %scene%:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "[day_suffix]"
    return

label %scene%_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "%scene%_environment", "actions" : "l", "zorder":10}, scene="%scene%")

    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "%scene%_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="%scene%")
    $ add_object_to_scene("Teleport_Bedroom2", {"type":3, "text" : t_("ГАРДЕРОБ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "%scene%_environment", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True, "group":"teleports"}, scene="%scene%")
    $ add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : t_("КРОВАТЬ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "%scene%_environment", "xpos" : 220, "ypos" : 545, "zorder":11, "teleport":True, "group":"teleports"}, scene="%scene%")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label %scene%_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_street_floor1")
        return
    return
