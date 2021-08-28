default ep218_quests_shinyhole_init_flag = False
default ep218_quests_claire_danced_nude_last_day = 0
default ep218_quests_monica_queen_job1_day = 0
default ep218_quests_monica_queen_job1_completed_day = 0
default ep218_quests_ashley_creditline_job1_completed_day = 0

label ep218_quests_shinyhole_check:
    if ep218_quests_shinyhole_init_flag == True:
        return
    if ep217_quests_shinyhole16_molly_after_private_flag == True and questHelpGetStatus("shinyhole_57a") == 1 and questHelpGetStatus("shinyhole_57") == 1:
        $ ep218_quests_shinyhole_init_flag = True
        $ questHelp("shinyhole_59")
        $ questHelp("shinyhole_60")
        $ questHelp("shinyhole_61")
        $ add_talk("Pub_StripteaseGirl2", "ep218_quests_shinyhole1_claire", scene="pub_makeuproom", label="ep218_claire")
        $ add_hook("end_dance_event", "ep218_quests_shinyhole3_private", scene="global", label="ep218_quests_shinyhole3_private")

    return

label ep218_quests_shinyhole1_claire:
    if ep217_quests_shinyhole15_claire_after_private_day == day:
        return
    if cloth != "Whore":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep218_dialogues1_pub_1() from _rcall_ep218_dialogues1_pub_1
    if _return == False: # отказала
        call refresh_scene_fade() from _rcall_refresh_scene_fade_139
        return False

    call pub_dance2_claire_dance2() from _rcall_pub_dance2_claire_dance2
    if ep218_quests_claire_danced_nude_last_day == 0:
        call ep218_dialogues1_pub_3() from _rcall_ep218_dialogues1_pub_3
    $ questHelp("shinyhole_59", True)
    call change_scene("pub", "Fade_long") from _rcall_change_scene_233
    $ notif(t_("Клэр ушла домой."))
    $ move_object("Pub_StripteaseGirl2", "empty")
    $ monicaDancedLastDay = day
    $ ep218_quests_claire_danced_nude_last_day = day
    return False


label ep218_quests_shinyhole3_private: # приходит Эшли и требует приват с банкиром
    $ remove_hook()
    $ ep218_quests_monica_queen_job1_day = day
    call ep218_dialogues1_pub_4() from _rcall_ep218_dialogues1_pub_4
    if _return == True:
        $ ep218_quests_monica_queen_job1_completed_day = day
        $ questHelp("shinyhole_60", True)
        $ questHelp("shinyhole_61", False)
    else:
        $ ep218_quests_ashley_creditline_job1_completed_day = day
        $ questHelp("shinyhole_60", False)
        $ questHelp("shinyhole_61", True)

    $ cloth = "Whore"
    $ cloth_type = "Whore"
    $ pub_makeuproom_monica_suffix = 2
    call change_scene("pub_makeuproom", "Fade_long") from _rcall_change_scene_234
    $ add_hook("before_open", "ep218_quests_shinyhole4_afterprivate", scene="pub", label="ep218_quests_shinyhole4_afterprivate", once=True)
    return False

label ep218_quests_shinyhole4_afterprivate:
    if ep218_quests_monica_queen_job1_completed_day > 0:
        call ep218_dialogues1_pub_8() from _rcall_ep218_dialogues1_pub_8
    if ep218_quests_ashley_creditline_job1_completed_day > 0:
        call ep218_dialogues1_pub_7() from _rcall_ep218_dialogues1_pub_7
    return






#
