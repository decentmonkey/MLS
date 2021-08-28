default ep218_quests_escort_inited = False
default ep218_quests_meeting1_planned = False
default ep218_quests_meeting2_planned = False
default ep218_quests_meeting1_day = 0
default ep218_quests_meeting2_day = 0
default ep218_quests_escort_completed_day = 0

label ep218_quests_escort_check1:
    if ep218_quests_escort_inited == False and ep217_party_day > 0 and monicaCandiseHotelMeetingPlanned == False and monicaAbbyHotelMeetingPlanned == False:
        # встретились и с Кэндис и с Эбби
        $ questHelp("escort_21")
        $ ep218_quests_meeting1_planned = True
        $ ep218_quests_escort_inited = True
    return

label ep218_quests_escort2_meeting: # встреча с Кэндис
    $ ep218_quests_meeting1_planned = False
    call ep218_dialogues3_escort_1() from _rcall_ep218_dialogues3_escort_1
    if _return == -1:
        $ questHelp("escort_21", False)
        $ add_hook("Visitor1", "ep218_quests_escort3_meeting_resume", scene="rich_hotel_restaurant", label="ep218_quests_escort_resume")
        call change_scene("rich_hotel_restaurant", "Fade_long") from _rcall_change_scene_226
        return
    call ep218_quests_escort4_harry_init() from _rcall_ep218_quests_escort4_harry_init
    return

label ep218_quests_escort3_meeting_resume:
    $ remove_hook(label="ep218_quests_escort_resume")
    call ep218_dialogues3_escort_1a() from _rcall_ep218_dialogues3_escort_1a
    if _return == -1:
        $ questHelp("escort_21", False)
        $ add_hook("Visitor1", "ep218_quests_escort3_meeting_resume", scene="rich_hotel_restaurant", label="ep218_quests_escort_resume")
        return False
    call ep218_quests_escort4_harry_init() from _rcall_ep218_quests_escort4_harry_init_1
    return False

label ep218_quests_escort4_harry_init:
    $ questHelp("escort_21", True)
    $ questHelp("escort_22")
    $ ep218_quests_meeting1_day = day
    $ candiseApartmentsStage = 2
    $ add_hook("Teleport_Rich_Hotel_Reception",  "ep218_dialogues3_escort_2a", scene="street_rich_hotel", label="ep218_quests_escort")
    $ autorun_to_object("ep218_dialogues3_escort_2", scene="street_rich_hotel")
    call change_scene("street_rich_hotel", "Fade_long") from _rcall_change_scene_227
    return

label ep218_quests_escort5_candise_apartments:
    call ep218_dialogues3_escort_3() from _rcall_ep218_dialogues3_escort_3 # Апартаменты Кэндис
    call ep218_dialogues3_escort_5a() from _rcall_ep218_dialogues3_escort_5a # Апартаменты Эбби
    $ questHelp("escort_22", True)
    $ questHelp("escort_23")
    $ map_objects["Teleport_Candise_Apartments"] = {"text" : t_("КЭНДИС И ЭББИ"), "xpos" : 897, "ypos" : 965, "base" : "map_marker", "state" : "visible"}
    $ ep218_quests_escort_completed_day = day
    $ candiseApartmentsStage = 1
    $ ep218_quests_meeting2_planned = True
    $ remove_hook(label="ep218_quests_escort")
    $ map_source_scene = "rich_hotel_reception"
    call change_scene("rich_hotel_reception", "Fade_long") from _rcall_change_scene_228
    if day_time != "evening":
        $ changeDayTime("evening")
    return

label ep218_quests_escort6_candise_after:
    $ ep218_quests_meeting2_planned = False
    $ ep218_quests_meeting2_day = day
    if monicaAbbyRentHelp3 > 0: # согласилась на секс
        call ep218_dialogues3_escort_6() from _rcall_ep218_dialogues3_escort_6
    else:
        # отказала
        call ep218_dialogues3_escort_7() from _rcall_ep218_dialogues3_escort_7
    $ questHelp("escort_23", True)
    call ep224_quests_escort_init() from _rcall_ep224_quests_escort_init_1
    call change_scene("rich_hotel_restaurant", "Fade_long") from _rcall_change_scene_229
    return


#
