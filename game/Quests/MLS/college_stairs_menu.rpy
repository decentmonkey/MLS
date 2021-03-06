default college_menu_roof_enabled = False
default college_menu_floor3_enabled = True
default college_menu_floor2_enabled = True
default college_menu_floor1_enabled = True

label college_stairs_menu:
    $ menu_data = {
        "КРЫША КОЛЛЕДЖА":{"enabled":college_menu_roof_enabled},
        "ЭТАЖ 3":{"enabled":college_menu_floor3_enabled},
        "ЭТАЖ 2":{"enabled":college_menu_floor2_enabled},
        "ЭТАЖ 1":{"enabled":college_menu_floor1_enabled}
    }
    menu:
        "КРЫША КОЛЛЕДЖА":
            call change_scene("college_roof") from _rcall_change_scene_4
        "ЭТАЖ 3":
            call change_scene("college_coridor10") from _rcall_change_scene_5
        "ЭТАЖ 2":
            call change_scene("college_coridor7") from _rcall_change_scene_6
        "ЭТАЖ 1":
            call change_scene("college_coridor3") from _rcall_change_scene_7
    return
