label college_artclass:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_ArtClass"
    return

label college_artclass_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor5", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_artclass_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="college_artclass")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_artclass_environment:
    if obj_name == "Teleport_Coridor5":
        call change_scene("college_coridor5") from _rcall_change_scene_20
        return
    return
