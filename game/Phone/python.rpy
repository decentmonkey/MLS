init python:
    v1 = ""
    v2 = ""
    v3 = ""
    v4 = ""
    v5 = ""
    v6 = 0.0
    v7 = 0.0
    list_contact = [
    ["iphone_x/mess/img.png", "Jon", "Sthmit", "blabla", "Я тут вспомнил..."],
    ["iphone_x/mess/1.png", "Jek", "Black", "ГЛАЗАААА!", "Тогда пока"],
    ["iphone_x/mess/2.png", "Nik", "Anderson", "text text text text text text mmmmmmmmm text", "Привет"],
    ["iphone_x/mess/3.jpg", "Andre", "Lisbat", "nnnnn", "Было весело"],
    ["iphone_x/mess/4.png", "Vanesa", "Bekkit", "text text text text text text mmmmmmmmm text", "Пока"],
    ["iphone_x/mess/5.png", "Noname", "", "nnnnn", "Не пиши мне!"],
    ["iphone_x/mess/6.png", "mama", "", "Типо очень много текста чтобы проверить допустимые пределы, в которые можно уложиться чтобы сообщение не выходило за пределы айфона, думаю этого хватит! Этого не хватило, но думаю для ограничения подскаски хватит...", "Люблю тебя"]
    ]
    list_favorite = list_contact[0:4]
    #[[(0,0), (0,1)], [(1,0), (1,1)], [(2,0), (2,1)]]
    chat_what = ""
    chat_who = "me"
    rigth_left = 0
    sms_go_to = ""
    notes_text = ""
    photo_list = []
    def list_append(list, obj):
        list.append(obj)
