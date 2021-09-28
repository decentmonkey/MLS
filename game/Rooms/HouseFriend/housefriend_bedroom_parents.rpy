label housefriend_bedroom_parents:
    $ miniMapData = []
    $ scene_image = "scene_HouseFriend_Bedroom_Parents[day_suffix]"
    return

label housefriend_bedroom_parents_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "housefriend_bedroom_parents_environment", "actions" : "l", "zorder":10}, scene="housefriend_bedroom_parents")

    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("НАЗАД НА КУХНЮ"), "larrow" : "arrow_left_2", "base":"HouseFriend_Bedroom_Parents_Teleport_Kitchen", "click" : "housefriend_bedroom_parents_environment", "xpos" : 502, "ypos" : 990, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_bedroom_parents")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label housefriend_bedroom_parents_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_street_floor1")
        return
    return
