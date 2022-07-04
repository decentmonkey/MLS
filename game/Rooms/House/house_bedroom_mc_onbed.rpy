default house_bedroom_mc_onbed_suffix = 1

label house_bedroom_mc_onbed:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_14
    $ scene_image = "scene_House_Bedroom_MC_OnBed[day_suffix]"
    return

label house_bedroom_mc_onbed_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Bedroom_MC", {"type":3, "text" : t_("ВСТАТЬ С КРОВАТИ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "house_bedroom_mc_onbed_environment", "xpos" : 357, "ypos" : 979, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bedroom_mc_onbed")
    return

label house_bedroom_mc_onbed_init2:
    $ add_object_to_scene("MC", {"type" : 2, "base" : "House_Bedroom_MC_OnBed_MC[house_bedroom_mc_onbed_suffix][day_suffix]", "click" : "house_kitchen_environment", "actions" : "l", "zorder":10}, scene="house_bedroom_mc_onbed")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bedroom_mc_onbed_environment:
    if obj_name == "Teleport_Bedroom_MC":
        call change_scene("house_bedroom_mc", "Fade_long", "put_dress") from _rcall_change_scene_130
        return

    return
