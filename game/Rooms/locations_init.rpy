label locations_init:
    #MAP
    $ add_location("map", caption="", label="map", parent="World")
    $ add_location("COLLEGE", caption="", label="empty_label", parent="World")
    $ add_location("HOUSE", caption="", label="empty_label", parent="World")
    $ add_location("HOUSEFRIEND", caption="", label="empty_label", parent="World")

    #INTRO
    $ add_location("intro_beach", caption=t_(""), label="intro_beach", init_label="intro_beach_init", parent="WORLD")

    #HOUSE
    $ add_location("house_street", caption=t_("ДВОР ДОМА"), label="house_street", init_label="house_street_init", parent="HOUSE")
    $ add_location("house_bathroom", caption=t_("ДУШЕВАЯ КОМНАТА"), label="house_bathroom", init_label="house_bathroom_init", parent="house_floor1")
    $ add_location("house_bedroom_landlord", caption=t_("СПАЛЬНЯ СОФИ И ГЕНРИ"), label="house_bedroom_landlord", init_label="house_bedroom_landlord_init", parent="college_street")
    $ add_location("house_bedroom_mc", caption=t_("МОЯ КОМНАТА"), label="house_bedroom_mc", init_label="house_bedroom_mc_init", parent="house_floor2")
    $ add_location("house_bedroom_mc_tablenear", caption=t_("МОЯ КОМНАТА"), label="house_bedroom_mc_tablenear", init_label="house_bedroom_mc_tablenear_init", parent="house_bedroom_mc")
    $ add_location("house_floor1", caption=t_("ПЕРВЫЙ ЭТАЖ"), label="house_floor1", init_label="house_floor1_init", parent="house_street")
    $ add_location("house_floor2", caption=t_("ВТОРОЙ ЭТАЖ"), label="house_floor2", init_label="house_floor2_init", parent="house_floor1")
    $ add_location("house_garage", caption=t_("ГАРАЖ"), label="house_garage", init_label="house_garage_init", parent="house_street")
    $ add_location("house_kitchen", caption=t_("КУХНЯ"), label="house_kitchen", init_label="house_kitchen_init", parent="house_floor1")
    $ add_location("house_livingroomhall", caption=t_("ГОСТИНАЯ"), label="house_livingroomhall", init_label="house_livingroomhall_init", parent="house_floor1")
    $ add_location("house_sister1", caption=t_("КОМНАТА ОЛИВИИ"), label="house_sister1", init_label="house_sister1_init", parent="house_floor2")
    $ add_location("house_sister2", caption=t_("КОМНАТА СИНТИИ"), label="house_sister2", init_label="house_sister2_init", parent="house_floor2")
    $ add_location("house_storeroom", caption=t_("ПОДВАЛ"), label="house_storeroom", init_label="house_storeroom_init", parent="house_street")

    #HOUSEFRIEND
    $ add_location("housefriend_street", caption=t_("ДОМ ШОНА"), label="housefriend_street", init_label="housefriend_street_init", parent="HOUSEFRIEND")
    $ add_location("housefriend_livingroom", caption=t_("ГОСТИНАЯ ШОНА"), label="housefriend_livingroom", init_label="housefriend_livingroom_init", parent="housefriend_street")
    $ add_location("housefriend_room", caption=t_("КОМНАТА ШОНА"), label="housefriend_room", init_label="housefriend_room_init", parent="housefriend_livingroom")
    $ add_location("housefriend_kitchen", caption=t_("КУХНЯ"), label="housefriend_kitchen", init_label="housefriend_kitchen_init", parent="housefriend_livingroom")
    $ add_location("housefriend_bedroom_parents", caption=t_("СПАЛЬНЯ РОДИТЕЛЕЙ ШОНА"), label="housefriend_bedroom_parents", init_label="housefriend_bedroom_parents_init", parent="housefriend_kitchen")
#    $ add_location("", caption=t_(""), label="", init_label="_init", parent="college_street")

    #COLLEGE

    $ add_location("college_street", caption=t_("ДВОР КОЛЛЕДЖА"), label="college_street", init_label="college_street_init", parent="COLLEGE")
    $ add_location("college_coridor1", caption=t_("КОЛЛЕДЖ ЭТАЖ 1"), label="college_coridor1", init_label="college_coridor1_init", parent="college_street")
    $ add_location("college_coridor1_locker_mc", caption=t_("МОЙ ШКАФЧИК"), label="college_coridor1_locker_mc", init_label="college_coridor1_locker_mc_init", parent="college_coridor1")
    $ add_location("college_coridor3", caption=t_("ЛЕСТНИЦА ЭТАЖ 1"), label="college_coridor3", init_label="college_coridor3_init", parent="college_coridor1")
    $ add_location("college_coridor2", caption=t_("КОРИДОР ЭТАЖ 1"), label="college_coridor2", init_label="college_coridor2_init", parent="college_coridor3")
    $ add_location("college_coridor4", caption=t_("РАЗДЕВАЛКИ ЭТАЖ 1"), label="college_coridor4", init_label="college_coridor4_init", parent="college_coridor3")
    $ add_location("college_coridor7", caption=t_("ЛЕСТНИЦА ЭТАЖ 2"), label="college_coridor7", init_label="college_coridor7_init", parent="college_coridor3")
    $ add_location("college_coridor6", caption=t_("КОРИДОР ЭТАЖ 2"), label="college_coridor6", init_label="college_coridor6_init", parent="college_coridor7")
    $ add_location("college_coridor5", caption=t_("КОРИДОР ЭТАЖ 2"), label="college_coridor5", init_label="college_coridor5_init", parent="college_coridor7")
    $ add_location("college_coridor10", caption=t_("ЛЕСТНИЦА ЭТАЖ 3"), label="college_coridor10", init_label="college_coridor10_init", parent="college_coridor7")
    $ add_location("college_coridor9", caption=t_("КОРИДОР ЭТАЖ 3"), label="college_coridor9", init_label="college_coridor9_init", parent="college_coridor10")
    $ add_location("college_coridor8", caption=t_("КОРИДОР ЭТАЖ 3"), label="college_coridor8", init_label="college_coridor8_init", parent="college_coridor10")
    $ add_location("college_algebra", caption=t_("АЛГЕБРА"), label="college_algebra", init_label="college_algebra_init", parent="college_coridor5")
    $ add_location("college_artclass", caption=t_("КЛАСС РИСОВАНИЯ"), label="college_artclass", init_label="college_artclass_init", parent="college_coridor5")
    $ add_location("college_biology", caption=t_("БИОЛОГИЯ"), label="college_biology", init_label="college_biology_init", parent="college_coridor1")
    $ add_location("college_chemistry", caption=t_("ХИМИЯ"), label="college_chemistry", init_label="college_chemistry_init", parent="college_coridor2")
    $ add_location("college_computer", caption=t_("КОМПЬЮТЕРНЫЙ КЛАСС"), label="college_computer", init_label="college_computer_init", parent="college_coridor7")
    $ add_location("college_english", caption=t_("АНГЛИЙСКИЙ"), label="college_english", init_label="college_english_init", parent="college_coridor6")
    $ add_location("college_france", caption=t_("ФРАНЦУЗСКИЙ"), label="college_france", init_label="college_france_init", parent="college_coridor1")
    $ add_location("college_geography", caption=t_("ГЕОГРАФИЯ"), label="college_geography", init_label="college_geography_init", parent="college_coridor3")
    $ add_location("college_gym", caption=t_("СПОРТЗАЛ"), label="college_gym", init_label="college_gym_init", parent="college_coridor2")
    $ add_location("college_hall", caption=t_("АКТОВЫЙ ЗАЛ"), label="college_hall", init_label="college_hall_init", parent="college_coridor1")
    $ add_location("college_library", caption=t_("БИБЛИОТЕКА"), label="college_library", init_label="college_library_init", parent="college_coridor9")
    $ add_location("college_locker_boy", caption=t_("РАЗДЕВАЛКА ДЛЯ МАЛЬЧИКОВ"), label="college_locker_boy", init_label="college_locker_boy_init", parent="college_coridor4")
    $ add_location("college_locker_girl", caption=t_("РАЗДЕВАЛКА ДЛЯ ДЕВОЧЕК"), label="college_locker_girl", init_label="college_locker_girl_init", parent="college_coridor4")
    $ add_location("college_medical", caption=t_("МЕД КАБИНЕТ"), label="college_medical", init_label="college_medical_init", parent="college_coridor2")
    $ add_location("college_physics", caption=t_("ФИЗИКА"), label="college_physics", init_label="college_physics_init", parent="college_coridor6")
    $ add_location("college_pool", caption=t_("БАССЕЙН"), label="college_pool", init_label="college_pool_init", parent="college_coridor4")
    $ add_location("college_principal", caption=t_("КАБИНЕТ ДИРЕКТОРА"), label="college_principal", init_label="college_principal_init", parent="college_principal_secretary")
    $ add_location("college_principal_secretary", caption=t_("ПРИЕМНАЯ ДИРЕКТОРА"), label="college_principal_secretary", init_label="college_principal_secretary_init", parent="college_coridor8")
    $ add_location("college_roof", caption=t_("КРЫША КОЛЛЕДЖА"), label="college_roof", init_label="college_roof_init", parent="college_coridor10")
    $ add_location("college_teachers", caption=t_("УЧИТЕЛЬСКАЯ"), label="college_teachers", init_label="college_teachers_init", parent="college_coridor9")
    $ add_location("college_utilityroom", caption=t_("КАБИНЕТ ЗАВХОЗА"), label="college_utilityroom", init_label="college_utilityroom_init", parent="college_coridor10")
    $ add_location("college_wc_female", caption=t_("ТУАЛЕТ ДЛЯ ДЕВОЧЕК"), label="college_wc_female", init_label="college_wc_female_init", parent="college_coridor4")
    $ add_location("college_wc_male", caption=t_("ТУАЛЕТ ДЛЯ МАЛЬЧИКОВ"), label="college_wc_male", init_label="college_wc_male_init", parent="college_coridor4")
    $ add_location("college_streetyard", caption=t_("СПОРТИВНАЯ ПЛОЩАДКА"), label="college_streetyard", init_label="college_streetyard_init", parent="college_street")
    $ add_location("college_empty", caption=t_("ДВОР КОЛЛЕДЖА"), label="college_empty", init_label="college_empty_init", parent="college_street")

    return

label locations_init2:
    $ add_location("house_bedroom_mc_onbed", caption=t_("МОЯ КОМНАТА"), label="house_bedroom_mc_onbed", init_label="house_bedroom_mc_onbed_init", parent="house_bedroom_mc_onbed")
    return

label locations_beach1:
    $ add_location("BEACH", caption="", label="empty_label", parent="World")
    $ add_location("beach_loungers", caption=t_("ПЛЯЖ"), label="beach_loungers", init_label="beach_loungers_init", parent="BEACH")
    return

label locations_beach2:
    $ add_location("beach_park", caption=t_("ПАРК"), label="beach_park", init_label="beach_park_init", parent="BEACH")
    return

label locations_daisy1:
    $ add_location("DAISY", caption="", label="empty_label", parent="World")
    $ add_location("daisy_street", caption=t_("ДОМ ДЕЙЗИ"), label="daisy_street", init_label="daisy_street_init", parent="DAISY")
    return

label locations_arnie1:
    $ add_location("ARNIE", caption="", label="empty_label", parent="World")
    $ add_location("arnie_street", caption=t_("ДОМ АРНИ"), label="arnie_street", init_label="arnie_street_init", parent="ARNIE")
    return




#
