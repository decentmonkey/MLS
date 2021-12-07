default houseBathroomSister1Suffix = 1
default houseBathroomSister2Suffix = 1
default houseBathroomMotherSuffix = 1

label house_bathroom:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_1
    $ scene_image = "scene_House_Bathroom[day_suffix]"
    return

label house_bathroom_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Sister1", {"type" : 2, "base" : "House_Bathroom[day_suffix]_Sister1_[houseBathroomSister1Suffix]", "click" : "house_bathroom_environment", "actions" : "l", "zorder":10}, scene="house_bathroom")
    $ add_object_to_scene("Sister2", {"type" : 2, "base" : "House_Bathroom[day_suffix]_Sister2_[houseBathroomSister2Suffix]", "click" : "house_bathroom_environment", "actions" : "l", "zorder":10}, scene="house_bathroom")
    $ add_object_to_scene("Sophie", {"type" : 2, "base" : "House_Bathroom[day_suffix]_Mother_[houseBathroomMotherSuffix]", "click" : "house_bathroom_environment", "actions" : "l", "zorder":10}, scene="house_bathroom")

    $ add_object_to_scene("Shower", {"type" : 2, "base" : "House_Bathroom_Shower", "click" : "house_bathroom_environment", "actions" : "l", "zorder":0}, scene="house_bathroom")
    $ add_object_to_scene("Bath", {"type" : 2, "base" : "House_Bathroom_Bath", "click" : "house_bathroom_environment", "actions" : "l", "zorder":0}, scene="house_bathroom")
    $ add_object_to_scene("Toilet", {"type" : 2, "base" : "House_Bathroom_Toilet", "click" : "house_bathroom_environment", "actions" : "l", "zorder":0}, scene="house_bathroom")

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "rarrow" : "arrow_right_2", "base":"House_Bathroom_Teleport_Floor1", "click" : "house_bathroom_environment", "xpos" : 1599, "ypos" : 541, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bathroom")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bathroom_environment:
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1") from _rcall_change_scene_83
        return
    return
