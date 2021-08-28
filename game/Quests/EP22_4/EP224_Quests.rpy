default ep224_quests_load_init_flag = False
label ep224_quests_load_init:
    if ep224_quests_load_init_flag == True:
        return
    $ ep224_quests_load_init_flag = True
    if ep218_quests_julia_completed_last_day > 0:
        call ep224_quests_julia_init() from _rcall_ep224_quests_julia_init
    if ep219_quests_photoshoot10_day > 0:
        call ep224_quests_office_init() from _rcall_ep224_quests_office_init
    if ep219_quests_linda_after_stage_day > 0 and ep218_quests_meeting2_day > 0:
        call ep224_quests_escort_init() from _rcall_ep224_quests_escort_init # инитим эскорт
    if ep218_quests_betty_completed_day > 0:
        call ep224_quests_betty_init() from _rcall_ep224_quests_betty_init
    if ep219_quests_victoria_party_day > 0:
        call ep224_quests_victoria_init() from _rcall_ep224_quests_victoria_init
    $ monicaCleaningRoomsAmount = 1
    $ move_object("Bardie", "empty")
    $ remove_hook(label="menu_betty_panties_show_to_monica")
    $ set_active("Panties_Box", False, scene="basement_laundry")
    return
