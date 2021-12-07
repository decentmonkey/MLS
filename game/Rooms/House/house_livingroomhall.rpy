default houseLivingRoomSophieSuffix = 1
default houseLivingRoomFatherSuffix = 1

label house_livingroomhall:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_9
    $ scene_image = "scene_House_LivingRoomHall[day_suffix]"
    return

label house_livingroomhall_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Sophie", {"type" : 2, "base" : "House_LivingRoomHall[day_suffix]_Mother_[houseLivingRoomSophieSuffix]", "click" : "house_livingroomhall_environment", "actions" : "l", "zorder":10}, scene="house_livingroomhall")
    $ add_object_to_scene("Henry", {"type" : 2, "base" : "House_LivingRoomHall[day_suffix]_Father_[houseLivingRoomFatherSuffix]", "click" : "house_livingroomhall_environment", "actions" : "l", "zorder":10}, scene="house_livingroomhall")
    $ add_object_to_scene("TV", {"type" : 2, "base" : "House_LivingRoomHall_TV", "click" : "house_livingroomhall_environment", "actions" : "l", "zorder":0}, scene="house_livingroomhall")

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_livingroomhall_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="house_livingroomhall")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_livingroomhall_environment:
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1") from _rcall_change_scene_100
        return
    if obj_name == "TV":
        call ep01_dialogues2_day1_family_1_10() from _rcall_ep01_dialogues2_day1_family_1_10
        return
    return
