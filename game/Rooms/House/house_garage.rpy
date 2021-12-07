label house_garage:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_7
    $ scene_image = "scene_House_Garage[day_suffix]"
    return

label house_garage_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_House_Street", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_garage_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="house_garage")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_garage_environment:
    if obj_name == "Teleport_House_Street":
        call change_scene("house_street") from _rcall_change_scene_98
        return
    return
