label intro_beach:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_Intro_Beach"
    return

label intro_beach_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Girl1", {"type" : 2, "base" : "Intro_Beach_Girl1", "click" : "intro_beach_environment", "actions" : "lt", "zorder":10}, scene="intro_beach")
    $ add_object_to_scene("Girl2", {"type" : 2, "base" : "Intro_Beach_Girl2", "click" : "intro_beach_environment", "actions" : "lt", "zorder":10}, scene="intro_beach")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label intro_beach_environment:
    if obj_name == "Girl1":
        if act=="l":
            call ep01_dialogues1_start_1a3() from _rcall_ep01_dialogues1_start_1a3
        if act=="t":
            call ep1_intro_quests2() from _rcall_ep1_intro_quests2
            return
    if obj_name == "Girl2":
        if act=="l":
            call ep01_dialogues1_start_1a4() from _rcall_ep01_dialogues1_start_1a4
        if act=="t":
            call ep1_intro_quests2() from _rcall_ep1_intro_quests2_1
            return
    call refresh_scene_fade() from _rcall_refresh_scene_fade_10
    return
