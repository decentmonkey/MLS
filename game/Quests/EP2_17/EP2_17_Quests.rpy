default ep217_quests_bugfix1_initialized = False


label ep217_quests:
    if ep215_quests_betty_visit2_completed_day > 0: # если Бетти общалась с соседом, инциализируем квест с Бетти
        $ questHelp("house_45", skipIfExists=True)
        $ add_hook("fitness_end", "ep217_quests_betty1_check", scene="global", label="betty_neighbour_check")

    if monica_escort_service_started == True and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False:
        $ questHelp("escort_14", skipIfExists=True)
        $ questHelp("escort_15", skipIfExists=True)


    $ ep217_quests_office_menu_enabled = True
    $ questHelp("office_53")

    if monica_shiny_hole_queen_day > 0 and monicaPubFiredTips1 == False:
        $ questHelp("shinyhole_50")
        call ep217_quests_shinyhole1_init() from _rcall_ep217_quests_shinyhole1_init

    if fallingPathStarted == True:
        $ citizen5BForced = True
        $ citizen9BForced = True
        $ citizen4BForced = True
        $ questHelp("work_slums_52")
        $ questHelp("work_slums_53")
        $ questHelp("work_slums_54")
    return

label ep217_quests_bugfix1:
    if ep217_quests_bugfix1_initialized == True:
        return
    $ ep217_quests_bugfix1_initialized = True
    if monica_shiny_hole_queen_day > 0 and monicaPubFiredTips1 == True:
        $ questHelpRemove("shinyhole_50")
    return
