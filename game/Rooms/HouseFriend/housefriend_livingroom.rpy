default houseFriendLivingRoom_MotherFriendSuffix = 1
default houseFriendLivingRoom_FriendBardieSuffix = 1

label housefriend_livingroom:
    $ miniMapData = []
    $ scene_image = "scene_HouseFriend_LivingRoom[day_suffix]"
    return

label housefriend_livingroom_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Mother_Friend", {"type" : 2, "base" : "HouseFriend_LivingRoom[day_suffix]_Mother_Friend_[houseFriendLivingRoom_MotherFriendSuffix]", "click" : "housefriend_livingroom_environment", "actions" : "l", "zorder":10}, scene="housefriend_livingroom")
    $ add_object_to_scene("Friend_Bardie", {"type" : 2, "base" : "HouseFriend_LivingRoom[day_suffix]_Friend_Bardie_[houseFriendLivingRoom_FriendBardieSuffix]", "click" : "housefriend_livingroom_environment", "actions" : "l", "zorder":10}, scene="housefriend_livingroom")

    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "housefriend_livingroom_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="housefriend_livingroom")
    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "housefriend_livingroom_environment", "xpos" : 1542, "ypos" : 898, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_livingroom")
    $ add_object_to_scene("Teleport_Room", {"type":3, "text" : t_("КОМНАТА ШОНА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "housefriend_livingroom_environment", "xpos" : 350, "ypos" : 886, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_livingroom")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label housefriend_livingroom_environment:
    if obj_name == "Teleport_Street":
        call change_scene("housefriend_street") from _rcall_change_scene_110
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("housefriend_kitchen") from _rcall_change_scene_111
        return
    if obj_name == "Teleport_Room":
        call change_scene("housefriend_room") from _rcall_change_scene_112
        return
    return
