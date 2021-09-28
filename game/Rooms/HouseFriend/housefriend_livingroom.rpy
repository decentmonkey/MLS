label housefriend_livingroom:
    $ miniMapData = []
    $ scene_image = "scene_HouseFriend_LivingRoom[day_suffix]"
    return

label housefriend_livingroom_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "housefriend_livingroom_environment", "actions" : "l", "zorder":10}, scene="housefriend_livingroom")

    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "housefriend_livingroom_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_livingroom")
    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "housefriend_livingroom_environment", "xpos" : 1542, "ypos" : 898, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_livingroom")
    $ add_object_to_scene("Teleport_Room", {"type":3, "text" : t_("КОМНАТА ШОНА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "housefriend_livingroom_environment", "xpos" : 350, "ypos" : 886, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_livingroom")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label housefriend_livingroom_environment:
    if obj_name == "Teleport_Street":
        call change_scene("housefriend_street")
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("housefriend_kitchen")
        return
    if obj_name == "Teleport_Room":
        call change_scene("housefriend_room")
        return
    return
