label house_storeroom:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_12
    $ scene_image = "scene_House_StoreRoom[day_suffix]"
    return

label house_storeroom_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "rarrow" : "arrow_right_2", "base":"House_StoreRoom_Teleport_Street", "click" : "house_storeroom_environment", "xpos" : 1268, "ypos" : 993, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_storeroom")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_storeroom_environment:
    if obj_name == "Teleport_Street":
        call change_scene("house_street") from _rcall_change_scene_103
        return
    return
