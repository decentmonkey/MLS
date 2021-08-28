default ep217_quests_escort2_check_start_party_flag = False
default candiseApartmentsStage = 0
default ep217_party_day = 0
default ep217_party_monica_danced = False
default ep217_party_whiskey_counter_list = []
default monicaKnowsCandise = False
default monicaCandiseHotelMeetingPlanned = False
default monicaAbbyHotelMeetingPlanned = False

label ep217_quests_escort1:
    call ep217_dialogues1_escort_2() from _rcall_ep217_dialogues1_escort_2
    call ep217_dialogues1_escort_2a() from _rcall_ep217_dialogues1_escort_2a
    $ remove_objective("go_administrator")
    $ add_objective("go_customer", t_("Пойти к клиенту, который ждет Монику у лифта."), c_blue, 105)
    $ move_object("EscortCustomer1", "rich_hotel_lift")

    $ remove_hook(label="escort_scene8_block_lift")

    $ add_hook("Monica", "ep217_dialogues1_escort_3a", scene="rich_hotel_lift", label="escort_scene8")
    $ add_hook("Teleport_Reception", "ep217_dialogues1_escort_3a", scene="rich_hotel_lift", label="escort_scene8")
    $ autorun_to_object("ep217_dialogues1_escort_3a", scene="rich_hotel_lift")
    $ richHotelLiftSceneSuffix = ""

    $ add_hook("Door", "ep217_dialogues1_escort_3b", scene="rich_hotel_reception", label="escort_scene8")
    $ add_hook("Teleport_Restaurant", "ep217_dialogues1_escort_3b", scene="rich_hotel_reception", label="escort_scene8")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep217_dialogues1_escort_3b", scene="rich_hotel_reception", label="escort_scene8")

    $ add_hook("Lift", "ep217_quests_escort1a", scene="rich_hotel_lift", label="escort_scene8")
    $ add_hook("EscortCustomer1", "ep217_dialogues1_escort_3a", scene="rich_hotel_lift", label="escort_scene8")
    $ add_talk("EscortCustomer1", "ep217_quests_escort1a", scene="rich_hotel_lift", label="escort_scene8")
    $ autorun_to_object("ep217_dialogues1_escort_3b", scene="rich_hotel_reception")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_125
    return

label ep217_quests_escort1a:
    call ep217_dialogues1_escort_3() from _rcall_ep217_dialogues1_escort_3
    $ questHelp("escort_15", skipIfExists=True)
    $ questHelp("escort_16", skipIfExists=True)
    $ questHelp("escort_17", skipIfExists=True)
    call ep217_dialogues1_escort_4() from _rcall_ep217_dialogues1_escort_4
    if _return == -1: # Моника убежала
        $ questHelp("escort_14", False, skipIfTrue=True)
        $ questHelp("escort_15", False, skipIfTrue=True)
        $ questHelp("escort_16", False, skipIfTrue=True)
        $ questHelp("escort_17", False, skipIfTrue=True)
        $ autorun_to_object("ep217_dialogues1_escort_5", scene="street_rich_hotel") # мысли если убежала из номера Адриано сразу после того, как фетишист пришел за ней

    if _return == -2: # отказала в сексе
        $ questHelp("escort_14", False)
        $ questHelp("escort_15", True, skipIfTrue=True)
        $ questHelp("escort_16", False, skipIfTrue=True)
        $ questHelp("escort_17", False, skipIfTrue=True)
#        call ep217_dialogues1_escort_5a() # если сказала Адриано, что она не Моника, и был с ним секс или не было секса
        $ autorun_to_object("ep217_dialogues1_escort_5", scene="street_rich_hotel") # мысли если убежала из номера Адриано сразу после того, как фетишист пришел за ней

    if _return == 1:
        # если все ок
        $ questHelp("escort_14", True)
        $ questHelp("escort_15", True)
        $ questHelp("escort_16", True)
        if ep217_quests_escort2_check_start_party_flag == False:
            call ep217_quests_escort2_init_party() from _rcall_ep217_quests_escort2_init_party
#            $ enter_scene("ep217_quests_escort2_check_start_party")
        call ep217_dialogues1_escort_5a() from _rcall_ep217_dialogues1_escort_5a


    call ep217_dialogues1_escort_6() from _rcall_ep217_dialogues1_escort_6 # разговор с админом

    $ move_object("ReceptionGirl", "rich_hotel_reception")
    $ remove_hook(label="escort_scene8")
    $ remove_objective("go_customer")
    $ richHotelLiftMonicaSuffix = 1
    $ richHotelLiftSceneSuffix = "_Closed"
    $ move_object("EscortCustomer1", "empty")
    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_18
    call change_scene("street_rich_hotel", "Fade_long", "snd_lift") from _rcall_change_scene_207


    return False


label ep217_quests_escort2_init_party:
    if ep217_quests_escort2_check_start_party_flag == True:
        return
    $ ep217_quests_escort2_check_start_party_flag = True
    $ autorun_to_object("ep217_dialogues1_escort_7", scene="street_rich_hotel")
    $ map_objects["Teleport_Candise_Apartments"] = {"text" : t_("АПАРТАМЕНТЫ КЭНДИС"), "xpos" : 897, "ypos" : 965, "base" : "map_marker", "state" : "visible"}

#    "Пойти на девичник к Кэндис и Эбби."
    $ questHelp("escort_17", skipIfTrue=True)
    $ candiseApartmentsStage = 0
    $ add_hook("map_teleport", "ep217_quests_escort3_teleport_candise", scene="global", label="escort_candise_teleport")
    return

label ep217_quests_escort3_teleport_candise:
    if obj_name != "Teleport_Candise_Apartments":
        return
    if candiseApartmentsStage == 0:
        if cloth != "CasualDress1":
            call ep217_dialogues1_escort_8() from _rcall_ep217_dialogues1_escort_8
            return False
        if day_time != "evening":
            call ep217_dialogues1_escort_11a() from _rcall_ep217_dialogues1_escort_11a
            return False

        $ ep217_party_whiskey_counter_list = []
        call ep217_dialogues1_escort_9() from _rcall_ep217_dialogues1_escort_9
        call ep217_dialogues1_escort_10() from _rcall_ep217_dialogues1_escort_10
        if _return == False:
            pass
        else:
            $ ep217_party_monica_danced = True

        $ add_hook("Visitor1", "ep217_quests_escort4_candice_after", scene="rich_hotel_restaurant", label="candise_after_candise")
        $ add_hook("Visitor4", "ep217_quests_escort5_abby_after", scene="rich_hotel_restaurant", label="abby_after_candise")

        $ questHelp("escort_17", True)
        $ autorun_to_object("ep217_dialogues1_escort_11", scene="street_house_outside")
        $ ep217_party_day = day
        call ep219_quests_escort1_init() from _rcall_ep219_quests_escort1_init

        $ candiseApartmentsStage = 1
        $ monicaKnowsCandise = True
        $ monicaCandiseHotelMeetingPlanned = True
        $ monicaAbbyHotelMeetingPlanned = True
        $ questHelp("escort_19")
        $ questHelp("escort_20")
        $ add_hook("ReceptionGirl", "ep217_dialogues1_escort_13", scene="rich_hotel_reception", label="reception_administrator_after_candise")
        $ map_source_scene = "street_house_outside"
        call map_close() from _rcall_map_close
        fadeblack 3.0
        call process_change_map_location("House") from _rcall_process_change_map_location_5
        call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_208
        return False
    if candiseApartmentsStage == 1:
        call ep217_dialogues1_escort_9b() from _rcall_ep217_dialogues1_escort_9b
        return False
    if candiseApartmentsStage == 2:
        call ep218_quests_escort5_candise_apartments() from _rcall_ep218_quests_escort5_candise_apartments
        return False
    if candiseApartmentsStage == 3:
        return

    return False

label ep217_quests_escort4_candice_after:
    $ monicaCandiseHotelMeetingPlanned = False
    $ questHelp("escort_19", True)
    call ep217_dialogues1_escort_12() from _rcall_ep217_dialogues1_escort_12_2
    call ep218_quests_escort_check1() from _rcall_ep218_quests_escort_check1_2
    return False

label ep217_quests_escort5_abby_after:
    $ monicaAbbyHotelMeetingPlanned = False
    $ questHelp("escort_20", True)
    call ep217_dialogues1_escort_12a() from _rcall_ep217_dialogues1_escort_12a_2
    call ep218_quests_escort_check1() from _rcall_ep218_quests_escort_check1_3
    return False
