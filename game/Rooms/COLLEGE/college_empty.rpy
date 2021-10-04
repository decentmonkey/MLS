    # место, куда можно посылать персонажей и они здесь будут (можно проверить get_active_objects)
label college_empty:
    $ miniMapData = []
    $ scene_image = "black_screen"
    return

label college_empty_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Sister2", {"type" : 2, "base" : "empty", "click" : "college_empty_environment", "actions" : "l", "zorder":10}, scene="college_empty")
    $ add_object_to_scene("Friend_Bardie", {"type" : 2, "base" : "empty", "click" : "college_empty_environment", "actions" : "l", "zorder":10}, scene="college_empty")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_empty_environment:
    return
