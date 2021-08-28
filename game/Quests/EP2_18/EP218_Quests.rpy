default ep218_quests_load_init_flag = False

label ep218_quests_load_init:
    if ep218_quests_load_init_flag == False:
        $ ep218_quests_load_init_flag = True
        if ep217_quests_betty_visit3_completed_day > 0:
            call ep218_quests_betty_init() from _rcall_ep218_quests_betty_init_1
        if ep217_party_day > 0:
            if monicaCandiseHotelMeetingPlanned == True:
                $ questHelp("escort_19")
            if monicaAbbyHotelMeetingPlanned == True:
                $ questHelp("escort_20")
            call ep218_quests_escort_check1() from _rcall_ep218_quests_escort_check1_4
        call ep218_quests_julia_init() from _rcall_ep218_quests_julia_init
        call ep218_quests_victoria_init() from _rcall_ep218_quests_victoria_init
        call ep218_quests_shinyhole_check() from _rcall_ep218_quests_shinyhole_check_2
        $ questHelp("other1")
        $ questHelp("other2")

    return
