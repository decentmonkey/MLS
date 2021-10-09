default collegeEnglishVisitor1_Suffix = 1
default collegeEnglishVisitor2_Suffix = 1
default collegeEnglishVisitor3_Suffix = 1
default collegeEnglishVisitor4_Suffix = 1
default collegeEnglishVisitor5_Suffix = 1
default collegeEnglishVisitor6_Suffix = 1
default collegeEnglishVisitor7_Suffix = 1
default collegeEnglishVisitor8_Suffix = 1
default collegeEnglishVisitor9_Suffix = 1
default collegeEnglishMC_Suffix = 1
default collegeEnglishTeacher_Suffix = 1

label college_english:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_English"
    return

label college_english_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("MC", {"type" : 2, "base" : "COLLEGE_English_MC_[collegeEnglishMC_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":10}, scene="college_english")
    $ add_object_to_scene("Teacher", {"type" : 2, "base" : "COLLEGE_English_Teacher_[collegeEnglishTeacher_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":1}, scene="college_english")
    $ add_object_to_scene("Visitor1", {"type" : 2, "base" : "COLLEGE_English_Visitor1_[collegeEnglishVisitor1_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":5, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor2", {"type" : 2, "base" : "COLLEGE_English_Visitor2_[collegeEnglishVisitor2_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":5, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor3", {"type" : 2, "base" : "COLLEGE_English_Visitor3_[collegeEnglishVisitor3_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":10, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor4", {"type" : 2, "base" : "COLLEGE_English_Visitor4_[collegeEnglishVisitor4_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":3, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor5", {"type" : 2, "base" : "COLLEGE_English_Visitor5_[collegeEnglishVisitor5_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":10, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor6", {"type" : 2, "base" : "COLLEGE_English_Visitor6_[collegeEnglishVisitor6_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":5, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor7", {"type" : 2, "base" : "COLLEGE_English_Visitor7_[collegeEnglishVisitor7_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":5, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor8", {"type" : 2, "base" : "COLLEGE_English_Visitor8_[collegeEnglishVisitor8_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":3, "group":"students"}, scene="college_english")
    $ add_object_to_scene("Visitor9", {"type" : 2, "base" : "COLLEGE_English_Visitor9_[collegeEnglishVisitor9_Suffix]", "click" : "college_english_environment", "actions" : "l", "zorder":3, "group":"students"}, scene="college_english")

    $ add_object_to_scene("Teleport_Coridor6", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_English_Teleport_Coridor6", "click" : "college_english_environment", "xpos" : 426, "ypos" : 248, "zorder":0, "teleport":True, "group":"teleports"}, scene="college_english")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_english_environment:
    if obj_name == "Teleport_Coridor6":
        call change_scene("college_coridor6") from _rcall_change_scene_61
        return
    return
