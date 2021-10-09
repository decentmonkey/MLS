default collegeStudent10_Suffix = 1

label college_coridor4:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_4
    $ scene_image = "scene_COLLEGE_Coridor_4_base"
    return

label college_coridor4_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student10", {"type" : 2, "base" : "COLLEGE_Coridor_4_Student10_[collegeStudent10_Suffix]", "click" : "college_coridor4_environment", "actions" : "l", "zorder":3, "selectable": False, "group":"students"}, scene="college_coridor4")

    $ add_object_to_scene("Teleport_Coridor2", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_coridor4_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="college_coridor4")
    $ add_object_to_scene("Teleport_Pool", {"type":3, "text" : t_("БАССЕЙН"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_4_Teleport_Pool", "click" : "college_coridor4_environment", "xpos" : 1280, "ypos" : 132, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor4")
    $ add_object_to_scene("Teleport_Locker_Girl", {"type":3, "text" : t_("РАЗДЕВАЛКА ДЛЯ ДЕВОЧЕК"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_4_Teleport_Locker_Girl", "click" : "college_coridor4_environment", "xpos" : 850, "ypos" : 113, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor4")
    $ add_object_to_scene("Teleport_Locker_Boy", {"type":3, "text" : t_("РАЗДЕВАЛКА ДЛЯ МАЛЬЧИКОВ"), "rarrow" : "arrow_up_2", "base":"COLLEGE_Coridor_4_Teleport_Locker_Boy", "click" : "college_coridor4_environment", "xpos" : 1399, "ypos" : 654, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor4")
    $ add_object_to_scene("Teleport_WC_Male", {"type":3, "text" : t_("ТУАЛЕТ ДЛЯ МАЛЬЧИКОВ"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_4_Teleport_WC_Male", "click" : "college_coridor4_environment", "xpos" : 897, "ypos" : 751, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor4")
    $ add_object_to_scene("Teleport_WC_Female", {"type":3, "text" : t_("ТУАЛЕТ ДЛЯ ДЕВОЧЕК"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_4_Teleport_WC_Female", "click" : "college_coridor4_environment", "xpos" : 785, "ypos" : 860, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor4")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor4_environment:
    if obj_name == "Teleport_Coridor2":
        call change_scene("college_coridor2") from _rcall_change_scene_40
        return
    if obj_name == "Teleport_Pool":
        call change_scene("college_pool") from _rcall_change_scene_41
        return
    if obj_name == "Teleport_Locker_Girl":
        call change_scene("college_locker_girl") from _rcall_change_scene_42
        return
    if obj_name == "Teleport_Locker_Boy":
        call change_scene("college_locker_boy") from _rcall_change_scene_43
        return
    if obj_name == "Teleport_WC_Male":
        call change_scene("college_wc_male") from _rcall_change_scene_44
        return
    if obj_name == "Teleport_WC_Female":
        call change_scene("college_wc_female") from _rcall_change_scene_45
        return
    return
