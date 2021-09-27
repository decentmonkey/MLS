label locations_init:
    #MAP
    $ add_location("map", caption="", label="map", parent="World")
    $ add_location("COLLEGE", caption="", label="empty_label", parent="World")
    $ add_location("HOUSE", caption="", label="empty_label", parent="World")

    #INTRO
    $ add_location("intro_beach", caption=t_(""), label="intro_beach", init_label="intro_beach_init", parent="WORLD")

    #HOUSE
    $ add_location("house_street", caption=t_("ДВОР ДОМА"), label="house_street", init_label="house_street_init", parent="HOUSE")
    return
#
