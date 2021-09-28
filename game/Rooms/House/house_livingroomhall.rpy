default houseLivingRoomSophieSuffix = 1
default houseLivingRoomFatherSuffix = 1

label house_livingroomhall:
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ scene_image = "scene_House_LivingRoomHall[day_suffix]"
    return

label house_livingroomhall_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Sophie", {"type" : 2, "base" : "House_LivingRoomHall[day_suffix]_Mother_[houseLivingRoomSophieSuffix]", "click" : "house_livingroomhall_environment", "actions" : "l", "zorder":10}, scene="house_livingroomhall")
    $ add_object_to_scene("Henry", {"type" : 2, "base" : "House_LivingRoomHall[day_suffix]_Father_[houseLivingRoomFatherSuffix]", "click" : "house_livingroomhall_environment", "actions" : "l", "zorder":10}, scene="house_livingroomhall")

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_livingroomhall_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="house_livingroomhall")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_livingroomhall_environment:
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1")
        return
    return
