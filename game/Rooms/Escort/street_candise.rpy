label street_candise:
    $ print "enter_street_candise"
    $ miniMapData = []

    $ sceneIsStreet = True

    $ scene_image = "Street_Candise[day_suffix]"
    if day_time == "day":
        music street9
    else:
        music street_evening1
    return

label street_candise_init:
    $ add_object_to_scene("Teleport_Inside", {"type":3, "text" : t_("КЭНДИС И ЭББИ"), "larrow" : "arrow_left_2", "base":"Street_Candise_Apartments", "click" : "street_candise_teleport", "xpos" : 1320, "ypos" : 130, "zorder":11, "teleport":True}, scene="street_candise")
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_candise_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="street_candise")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_candise_teleport:
    if obj_name == "Teleport_Street":
        call map_show() from _rcall_map_show_4
        return

    if obj_name == "Teleport_Inside":
        call ep22_4_dialogues5_escort_7() from _rcall_ep22_4_dialogues5_escort_7
        return
    return
label street_candise_environment:
    return
