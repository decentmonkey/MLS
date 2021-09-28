label house_bedroom_mc:
    $ miniMapData = []
    $ scene_image = "scene_House_Bedroom_MC[day_suffix]"
    return

label house_bedroom_mc_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "house_bedroom_mc_environment", "actions" : "l", "zorder":10}, scene="house_bedroom_mc")

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ЛЕСТНИЦА ВНИЗ"), "larrow" : "arrow_down_2_a", "base":"House_Bedroom_MC_Teleport_Floor2", "click" : "house_bedroom_mc_environment", "xpos" : 633, "ypos" : 954, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bedroom_mc")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bedroom_mc_environment:
    if obj_name == "Teleport_Floor2":
        call change_scene("house_floor2")
        return
    return
