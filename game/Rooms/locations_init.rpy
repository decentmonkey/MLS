label locations_init:
    #MAP
    $ add_location("map", caption="", label="map", parent="World")
    $ add_location("COLLEGE", caption="", label="empty_label", parent="World")
    $ add_location("HOUSE", caption="", label="empty_label", parent="World")

    #HOUSE
    $ add_location("house_street", caption=t_("ДВОР ДОМА"), label="house_street", init_label="house_street_init", parent="HOUSE")
    return
#
