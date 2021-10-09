label cynthia_chat1:
    $ phone_start_new_chat("cynthia1", "Cynthia")
    call phone_chat([ from _rcall_phone_chat
        ["cynthia", t_("[mcname], как дела? Ты еще в колледже?")]
    ])
    call phone_chat_menu([ from _rcall_phone_chat_menu
        t__("Ответить."),
        t__("Не отвечать.")
    ])
    if _return == 0:
        # ответить
        call phone_chat_menu([ from _rcall_phone_chat_menu_1
            t__("Я еще в колледже."),
            t__("Уже освободился.")
        ])
        if _return == 0:
            call phone_chat([ from _rcall_phone_chat_1
                ["", t_("Привет. Да, еще в колледже.")],
                ["", t_("А ты где?")]
            ])
        if _return == 1:
            call phone_chat([ from _rcall_phone_chat_2
                ["", t_("Привет. Уже освободился.")],
                ["", t_("Скоро буду дома. А ты где?")]
            ])
        call phone_chat([ from _rcall_phone_chat_3
            ["cynthia", t_("Я сегодня задержусь у кузины.")],
            ["cynthia", "Ей нужно помочь с заданием по математике."],
            ["cynthia", "image", "/images/Phone/Photos/cynthia_math2.png", 2],
            ["", t_("Окей. Если вечером не увидимся, завтра поболтаем :)")],
            ["cynthia", t_("Окей :)")],
        ])


    if _return == 1:
        # не отвечать
        bardi_t "Позже ей отвечу."
        return
    return

label cynthia_chat2:
    $ phone_start_new_chat("cynthia2", "Cynthia")
    call phone_chat([ from _rcall_phone_chat_4
        ["cynthia", t_("[mcname], не могу говорить. Я на занятиях.")],
        ["cynthia", t_("Спишемся позже! :)")]
    ])
    return

label sean_chat1:
    $ phone_start_new_chat("sean_chat1", "Sean")
    $ ep1_college_talk_sean_agree = False
    call phone_chat([ from _rcall_phone_chat_5
        ["sean", t_("Эй, чувак. Я уже дома. Решил свалить с занятий с тренером.")],
        ["sean", t_("Как дела? Ты еще долго будешь в колледже?")],
    ])
    call phone_chat_menu([ from _rcall_phone_chat_menu_2
        t__("Ответить."),
        t__("Не отвечать.")
    ])
    if _return == 0:
        # Ответить
        call phone_chat_menu([ from _rcall_phone_chat_menu_3
            t__("Уже освободился.")
        ])
        call phone_chat([ from _rcall_phone_chat_6
            ["", t_("Дела норм, бро.")],
            ["", t_("Я только вышел из колледжа.")],
            ["sean", t_("Какие планы на вечер?")],
            ["", t_("Домой сейчас пойду.")],
            ["sean", t_("Хочешь, заглядывай ко мне.")],
            ["", t_("А ты также в квартире недалеко от колледжа живешь?")],
            ["sean", t_("Не, бро. Мы уже давно переехали в дом.")],
            ["sean", t_("Он недалеко от твоего :)")],
            ["", t_("Окей. Тогда я к тебе.")],
            ["sean", t_("Жду.")],
        ])
        $ ep1_college_talk_sean_agree = True

    if _return == 1:
        bardi_t "Позже ему отвечу."
    call ep1_college5_college_init_sean() from _rcall_ep1_college5_college_init_sean
    return

label sean_chat2:
    $ phone_start_new_chat("sean_chat2", "Sean")
    call phone_chat([ from _rcall_phone_chat_7
        ["sean", t_("Эй, чувак. Я на занятиях.")],
        ["sean", t_("Спишемся позже! Удачи, бро!")]
    ])
    return

label sophie_chat1:
    $ phone_add_history("sophie_chat1", "Sophie", [
        ["sophie", t_("[mcname], у тебя все в порядке? Занятия в колледже уже давно закончились. Ты где, милый?")],
    ])
    return

label college_chat1:
    $ phone_add_history("college_chat1", "College", [
        ["college", t_("Студент [mcsurname], ждем вас сегодня в 9:00 am в приемной профессора Ричардсон. Администрация колледжа.")],
    ])
    return
