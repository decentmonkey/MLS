default collegeAlgebraMC_Suffix = 1
default collegeAlgebraTeacher_Suffix = 1
default collegeAlgebraVisitor1_Suffix = 1
default collegeAlgebraVisitor2_Suffix = 1
default collegeAlgebraVisitor3_Suffix = 1
default collegeAlgebraVisitor4_Suffix = 1
default collegeAlgebraVisitor5_Suffix = 1
default collegeAlgebraVisitor6_Suffix = 1
default collegeAlgebraVisitor7_Suffix = 1
default collegeAlgebraVisitor10_Suffix = 1
default collegeAlgebraVisitor11_Suffix = 1
default collegeAlgebraVisitor12_Suffix = 1

label college_algebra:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Algebra"
    return

label college_algebra_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor5", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Algebra_Teleport_Coridor5", "click" : "college_algebra_environment", "xpos" : 282, "ypos" : 202, "zorder":0, "teleport":True, "group":"teleports"}, scene="college_algebra")
    return

label college_algebra_init2:
    $ add_object_to_scene("MC", {"type" : 2, "base" : "COLLEGE_Algebra_MC_[collegeAlgebraMC_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":4, "selectable":False}, scene="college_algebra")
    $ add_object_to_scene("Teacher8", {"type" : 2, "base" : "COLLEGE_Algebra_Teacher8_[collegeAlgebraTeacher_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":0}, scene="college_algebra")
    $ add_object_to_scene("Visitor1", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor1_[collegeAlgebraVisitor1_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":3, "group":"students", "selectable":False}, scene="college_algebra")
    $ add_object_to_scene("Visitor2", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor2_[collegeAlgebraVisitor2_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":2, "group":"students", "selectable":False}, scene="college_algebra")
    $ add_object_to_scene("Visitor3", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor3_[collegeAlgebraVisitor3_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":3, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor4", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor4_[collegeAlgebraVisitor4_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":1, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor5", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor5_[collegeAlgebraVisitor5_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":4, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor6", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor6_[collegeAlgebraVisitor6_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":3, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor7", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor7_[collegeAlgebraVisitor7_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":2, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor10", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor10_[collegeAlgebraVisitor10_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":2, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor11", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor11_[collegeAlgebraVisitor11_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":1, "group":"students"}, scene="college_algebra")
    $ add_object_to_scene("Visitor12", {"type" : 2, "base" : "COLLEGE_Algebra_Visitor12_[collegeAlgebraVisitor12_Suffix]", "click" : "college_algebra_environment", "actions" : "l", "zorder":1, "group":"students", "selectable":False}, scene="college_algebra")
    $ add_object_to_scene("Ruler", {"type" : 2, "base" : "COLLEGE_Algebra_Ruler", "click" : "college_algebra_environment", "actions" : "l", "zorder":0}, scene="college_algebra")
    
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_algebra_environment:
    if obj_name == "Teleport_Coridor5":
        call change_scene("college_coridor5") from _rcall_change_scene_19
        return

    if obj_name == "Visitor11":
        call ep02_dialogues2_college_5a()
        return
    if obj_name == "Visitor5":
        call ep02_dialogues2_college_5b()
        call refresh_scene_fade()
        return
    if obj_name == "Visitor6":
        call ep02_dialogues2_college_5c()
        call refresh_scene_fade()
        return
    if obj_name == "Visitor4":
        call ep02_dialogues2_college_5d()
        call refresh_scene_fade()
        return
    if obj_name == "Visitor7":
        call ep02_dialogues2_college_5e()
        call refresh_scene_fade()
        return
    if obj_name == "Visitor10":
        call ep02_dialogues2_college_5f()
        return
    if obj_name == "Visitor3":
        call ep02_dialogues2_college_5g()
        call refresh_scene_fade()
        return
    if obj_name == "Ruler":
        call ep02_dialogues2_college_12()
        $ open_secret_object("Ruler")
        return

    return
