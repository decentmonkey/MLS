default ep15_update_init_flag = False

label ep15_update_init:
    if ep15_update_init_flag == True:
        return
    $ questHelp("house_29", True)
    call ep05_dialogues4_college_emily_1()
    call house_bedroom_mc_onbed_init2()
    $ house_bedroom_mc_onbed_suffix = 2
    call change_scene("house_bedroom_mc_onbed")
#    call change_scene("house_bedroom_mc")
    call process_change_map_location("HOUSE")
    call changeDayTime("morning")
    $ questHelp("house_30")
    $ phone_focus_icon(False)


    $ miniMapEnabledOnly = ["none"]
    $ add_hook("Teleport_Bedroom_MC", "ep05_dialogues4_college_emily_1a", scene="house_bedroom_mc_onbed", label="morning_block")
    call phone_instagram3b()
    $ add_hook("instagram", "ep15_quests1_emily_instagram", scene="phone")
#    $ phone_instagram_initial_position = 1.0
    return

label ep15_quests1_emily_instagram:
    if phone_instagram_current_name != "Emily":
        return
    $ remove_hook()
    $ phone_instagram_initial_position = 1.0
    call ep05_dialogues4_college_emily_2()
    $ questHelp("house_30", True)
    $ remove_hook(label="morning_block")
    $ add_hook("phone_close", "ep15_quests1_emily_instagram_close", scene="phone")

    return

label ep15_quests1_emily_instagram_close:
    $ remove_hook()
    $ phone_instagram_initial_position = 0.0
    $ house_bedroom_mc_onbed_suffix = 1
    $ miniMapEnabledOnly = []
    call change_scene("house_bedroom_mc", "Fade_long")
    sound2 put_dress
    call refresh_scene_fade_long()
    return

