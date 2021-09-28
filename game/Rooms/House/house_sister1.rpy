default houseSister1_Sister1Suffix = 1

label house_sister1:
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ scene_image = "scene_House_Sister1[day_suffix]"
    return

label house_sister1_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Sister1", {"type" : 2, "base" : "House_Sister1[day_suffix]_Sister1_[houseSister1_Sister1Suffix]", "click" : "house_sister1_environment", "actions" : "l", "zorder":10}, scene="house_sister1")

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_sister1_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_sister1")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_sister1_environment:
    if obj_name == "Teleport_Floor2":
        call change_scene("house_floor2")
        return
    return
