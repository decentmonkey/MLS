default houseFriendRoom_Friend_BardieSuffix1 = 1
default housefriend_room_forced_evening_Flag = False
default housefriend_room_forced_evening_time_suffix = "day"

label housefriend_room:
    $ miniMapData = []
    $ housefriend_room_forced_evening_time_suffix = day_suffix
    if housefriend_room_forced_evening_Flag != False:
        $ housefriend_room_forced_evening_time_suffix = housefriend_room_forced_evening_Flag
    $ scene_image = "scene_HouseFriend_Room[housefriend_room_forced_evening_time_suffix]"
    return

label housefriend_room_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Friend_Bardie", {"type" : 2, "base" : "HouseFriend_Room[housefriend_room_forced_evening_time_suffix]_Friend_Bardie_[houseFriendRoom_Friend_BardieSuffix1]", "click" : "housefriend_room_environment", "actions" : "l", "zorder":10}, scene="housefriend_room")

    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("НАЗАД В ГОСТИНУЮ"), "larrow" : "arrow_left_2", "base":"HouseFriend_Room_Teleport_LivingRoom", "click" : "housefriend_room_environment", "xpos" : 547, "ypos" : 1007, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_room")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label housefriend_room_environment:
    if obj_name == "Teleport_LivingRoom":
        call change_scene("housefriend_livingroom")
        return
    return
