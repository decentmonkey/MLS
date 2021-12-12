label ep12_quests1_init:
    call phone_instagram2()
    $ phone_instagram_mode = 1

    #family 
    ep02_dialogues1_family_1() # момент, на котором закончился 1-й апдейт, комната Барди
    call refresh_scene_fade()
    $ questHelp("house_9")
    $ miniMapDisabled["HOUSE"] = []
    $ miniMapEnabledOnly = ["Floor1"]

    $ set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
    $ add_hook("Teleport_Floor2", "ep12_quests2_bathroom", scene="house_bedroom_mc")
    $ add_hook("before_open", "ep12_quests2_bathroom", scene="house_floor1")

#    call phone_instagram3()
    return

label ep12_quests2_bathroom:
    $ remove_hook(label="ep12_quests2_bathroom")
    call ep02_dialogues1_family_1c()

    $ questHelp("house_9", True)
    $ miniMapEnabledOnly = []
    return


#