label party1:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_Party1"
#    music party_ambience
    return

label party1_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Alco1", {"type" : 2, "base" : "Party1_Alco1", "click" : "party1_environment", "actions" : "l", "zorder":6, "b":0.17, "tint":[1.0, 1.0, 0.7]}, scene="party1")
    $ add_object_to_scene("Alco2", {"type" : 2, "base" : "Party1_Alco2", "click" : "party1_environment", "actions" : "l", "zorder":4}, scene="party1")
    $ add_object_to_scene("Alco3", {"type" : 2, "base" : "Party1_Alco3", "click" : "party1_environment", "actions" : "l", "zorder":2, "b":0.17, "tint":[1.0, 1.0, 0.7]}, scene="party1")

    $ add_object_to_scene("GirlFrik", {"type" : 2, "base" : "Party1_GirlFrik", "click" : "party1_environment", "actions" : "l", "zorder":0}, scene="party1")
    $ add_object_to_scene("ClassmateFrik", {"type" : 2, "base" : "Party1_ClassmateFrik", "click" : "party1_environment", "actions" : "l", "zorder":2}, scene="party1")
    $ add_object_to_scene("Classmate9ClassmateNerd", {"type" : 2, "base" : "Party1_Classmate9ClassmateNerd", "click" : "party1_environment", "actions" : "l", "zorder":6}, scene="party1")
    $ add_object_to_scene("Classmate10", {"type" : 2, "base" : "Party1_Classmate10", "click" : "party1_environment", "actions" : "l", "zorder":0}, scene="party1")
    $ add_object_to_scene("Classmate3", {"type" : 2, "base" : "Party1_Classmate3", "click" : "party1_environment", "actions" : "l", "zorder":6}, scene="party1")
    $ add_object_to_scene("Classmate1Classmate11", {"type" : 2, "base" : "Party1_Classmate1Classmate11", "click" : "party1_environment", "actions" : "l", "zorder":2}, scene="party1")
    $ add_object_to_scene("Classmate7", {"type" : 2, "base" : "Party1_Classmate7", "click" : "party1_environment", "actions" : "l", "zorder":10}, scene="party1")
    $ add_object_to_scene("HarryEmily", {"type" : 2, "base" : "Party1_HarryEmily", "click" : "party1_environment", "actions" : "l", "zorder":1}, scene="party1")
    $ add_object_to_scene("NicoleClassmate1", {"type" : 2, "base" : "Party1_NicoleClassmate1", "click" : "party1_environment", "actions" : "l", "zorder":10, "active":False}, scene="party1")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label party1_environment:
    call ep13_quests11_party4()
    return
