label college_coridor5:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Coridor_5_base"
    return

label college_coridor5_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_coridor5_environment", "actions" : "l", "zorder":10}, scene="college_coridor5")

    $ add_object_to_scene("Teleport_Coridor6", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_5_Teleport_Coridor6", "click" : "college_coridor5_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor5")
    $ add_object_to_scene("Teleport_Algebra", {"type":3, "text" : t_("АЛГЕБРА"), "rarrow" : "arrow_down_2_a", "base":"COLLEGE_Coridor_5_Teleport_Algebra", "click" : "college_coridor5_environment", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor5")
    $ add_object_to_scene("Teleport_ArtClass", {"type":3, "text" : t_("КЛАСС РИСОВАНИЯ"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_5_Teleport_ArtClass", "click" : "college_coridor5_environment", "xpos" : 220, "ypos" : 545, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor5")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor5_environment:
    if obj_name == "Teleport_Coridor6":
        call change_scene("college_coridor6")
        return
    if obj_name == "Teleport_Algebra":
        call change_scene("college_algebra")
        return
    if obj_name == "Teleport_ArtClass":
        call change_scene("college_artclass")
        return
    return
