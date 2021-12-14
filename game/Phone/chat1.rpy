default sean_chat4_day = 0
#export_speaker_off
#call_labels_off
label cynthia_chat1:
    $ phone_start_new_chat("cynthia1", "Cynthia")
    call phone_chat([
        ["cynthia", t_("[mcname], как дела? Ты еще в колледже?")]
    ])
    call phone_chat_menu([
        t__("Ответить."),
        t__("Не отвечать.")
    ])
    if _return == 0:
        # ответить
        call phone_chat_menu([
            t__("Я еще в колледже."),
            t__("Уже освободился.")
        ])
        if _return == 0:
            call phone_chat([
                ["", t_("Привет. Да, еще в колледже.")],
                ["", t_("А ты где?")]
            ])
        if _return == 1:
            call phone_chat([
                ["", t_("Привет. Уже освободился.")],
                ["", t_("Скоро буду дома. А ты где?")]
            ])
        call phone_chat([
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
    call phone_chat([
        ["cynthia", t_("[mcname], не могу говорить. Я на занятиях.")],
        ["cynthia", t_("Спишемся позже! :)")]
    ])
    return

label sean_chat1:
    $ phone_start_new_chat("sean_chat1", "Sean")
    $ ep1_college_talk_sean_agree = False
    call phone_chat([
        ["sean", t_("Эй, чувак. Я уже дома. Решил свалить с занятий с тренером.")],
        ["sean", t_("Как дела? Ты еще долго будешь в колледже?")],
    ])
    call phone_chat_menu([
        t__("Ответить."),
        t__("Не отвечать.")
    ])
    if _return == 0:
        # Ответить
        call phone_chat_menu([
            t__("Уже освободился.")
        ])
        call phone_chat([
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
    call ep1_college5_college_init_sean() from _rcall_ep1_college5_college_init_sean
    return

label sean_chat2:
    $ phone_start_new_chat("sean_chat2", "Sean")
    call phone_chat([
        ["sean", t_("Эй, чувак. Я на занятиях.")],
        ["sean", t_("Спишемся позже! Удачи, бро!")]
    ])
    return

label sean_chat3:
    $ phone_start_new_chat("sean_chat3", "Sean")
    call phone_chat([
        ["", t_("Эй, бро. Ты уже в колледже?")],
        ["", t_("Давай пересечемся в перерыве между занятиями.")],
        ["sean", t_("Привет, чувак.")],
        ["sean", t_("Не-а, я не в колледже.")],
        ["sean", t_("Сегодня у меня дела поважнее xD")],
        ["", t_("Что за дела?")],
        ["sean", t_("Расскажу тебе при встрече.")],
        ["sean", t_("Все, мне пора. Спишемся позже.")],
        ["", t_("Окей. Ты меня заинтриговал, бро.")],
        ["sean", t_(";)")]
    ])
    $ mlsBardiDay3College8 = day # Барди переписывался с Шоном в колледже
    return

label sean_chat4:
    $ phone_start_new_chat("sean_chat4", "Sean")
    call phone_chat([
        ["", t_("Эй, бро, ты как?")],
        ["", t_("Твоя мама ничего не заподозрила?")],
        ["sean", t_("Привет, чувак!")],
        ["sean", t_("Нет, все в порядке.")],
        ["sean", t_("Но палево было жесткое!")],
        ["", t_("Эта твоя Бекки подумала, что я - это ты :)")],
        ["sean", t_("Я так и понял, бро. Не парься, все окей. xD")],
        ["", t_("А нахрена ты ей повязку нацепил?")],
        ["sean", t_("Ты не поверишь, чувак. Бекки знакома с моей мамой - они раньше учились вместе.")],
        ["sean", t_("Если бы они встретились, было бы капец как неудобно.")],
        ["", t_("xD")],
        ["sean", t_("Эх, жаль, что я не успел ей присунуть. Надо бы заказать ее еще раз.")],
        ["", t_("Еще раз? А откуда у тебя деньги на шлюху? Накопил?")],
        ["sean", t_("Не-а. Там другая тема, бро.")],
        ["sean", t_("Пока не могу рассказать. Позже.")],
        ["", t_("Окей. Снова интрига :)")],
        ["sean", t_(";)")]
    ])
    $ sean_chat4_day = day
    return

label sophie_chat1:
    $ phone_add_history("sophie_chat1", "Sophie", [
        ["sophie", t_("[mcname], у тебя все в порядке? Занятия в колледже уже давно закончились. Ты где, милый?")],
    ])
    return

label sophie_chat2:
    $ phone_start_new_chat("sophie_chat2", "Sophie")
    call phone_chat([
        ["sophie", t_("[mcname], надеюсь, сегодня ты не задержишься после колледжа. Мы ждем тебя к ужину.")]
    ])
    call phone_chat_menu([
        t__("Ответить."),
        t__("Не отвечать.")
    ])
    if _return == 0:
        call phone_chat_menu([
            t__("Ненадолго зайду к Шону."),
            t__("Скоро буду дома.")
        ])
        if _return == 0:
            call phone_chat([
                ["", t_("Привет, Софи. Я еще в колледже.")],
                ["", t_("После ненадолго заскочу к Шону.")],
                ["", t_("К ужину буду.")]
            ])
        if _return == 1:
            call phone_chat([
                ["", t_("Привет, Софи. Я уже освободился.")],
                ["", t_("Скоро буду дома.")]
            ])
        call phone_chat([
            ["sophie", t_("Хорошо, милый. Жду :)")],
            ["", t_("Окей :)")]
        ])

    if _return == 1:
        bardi_t "Позже ей отвечу."
    return

label sophie_chat3:
    $ phone_start_new_chat("sophie_chat3", "Sophie")
    call phone_chat([
        ["sophie", t_("[mcname], милый, у вас все в порядке?")],
        ["", t_("Да, Софи, у нас все нормально.")],
        ["sophie", t_("Отлично! Хотела предупредить вас, что мы с Генри задержимся...")],
        ["sophie", t_("И будем поздно.")],
        ["", t_("Я понял, Софи. Буду иметь в виду.")],
        ["sophie", t_("Хорошо :) Тогда пока!")],
        ["", t_("Пока!")]
    ])
    return
        
label college_chat1:
    $ phone_add_history("college_chat1", "College", [
        ["college", t_("Студент [mcsurname], ждем вас сегодня в 9:00 am в приемной профессора Ричардсон. Администрация колледжа.")],
    ])
    return

label whore_chat1:
    $ phone_start_new_chat("whore_chat1", "Whore")
    call phone_chat([
        ["", t_("Привет, Бекки.")],
        ["whore", t_("Привет. Это кто?")]
    ])
    call phone_chat_menu([
        t__("[mcname], друг Шона."),
        t__("Позже ей напишу.")
    ])
    if _return == 1:
        return
    call phone_chat([
        ["", t_("[mcname], друг Шона.")],
        ["whore", t_("А, поняла. Привет, красавчик.")],
        ["whore", t_("У тебя появилось желание еще раз поиграть со мной?")],
        ["", t_("Появилось. Я бы повторил.")],
        ["", t_("Сколько это будет стоить?")],
        ["whore", t_("По прайсу, красавчик.")],
        ["", t_("Это сколько?")],
        ["whore", t_("С проникновением 90 баксов.")],
        ["", t_("90?!")],
        ["", t_("А минет?")],
        ["whore", t_("50.")],
        ["", t_("Окей. Я тебе позже напишу.")],
        ["whore", t_("Стой. Для тебя я сделаю скидку. Возьму 70 за секс.")],
        ["", t_("А за минет 30?")],
        ["whore", t_("Да. Мне редко бывает прикольно с клиентами, так как было с тобой ;)")],
    ])
    call phone_chat_menu([
        t__("Как насчет вирта?")
    ])
    call phone_chat([
        ["", t_("Как насчет вирта?")],
        ["whore", t_("Такое только для постоянных клиентов.")],
        ["whore", t_("Давай хотя бы еще раз встретимся лично, красавчик?")],
        ["", t_("Понял. Я тебе напишу, когда у меня будет возможность встретиться.")],
        ["whore", t_("Буду ждать, красавчик. Пока.")],
        ["", t_("Пока.")]
    ])
    $ whoreCallStage = 2
    return

label whore_chat2:
    $ phone_start_new_chat("whore_chat2", "Whore")
    call phone_chat([
        ["whore", t_("Привет, красавчик.")],
        ["whore", t_("Надумал встретиться?")]
    ])
    call phone_chat_menu([
        t__("Написать Бекки."),
        t__("Не писать.")
    ])
    if _return == 1:
        bardi_t "Нет, я не буду платить за секс."
        bardi_t "Я найду способ сделать это, не потратив ни цента."
        bardi_t "Пусть даже не с этой Бекки..."
        return
    call phone_chat([
        ["", t_("Привет, Бекки.")],
        ["", t_("Еще думаю.")]
    ])
    call phone_chat_menu([
        t__("Бекки, ты можешь мне скинуть свою фотку?")
    ])
    call phone_chat([
        ["", t_("Бекки, ты можешь мне скинуть свою фотку?")],
        ["whore", t_("Нахрена мне это делать, красавчик?")],
    ])
    call phone_chat_menu([
        t__("Я тебе заплачу 1 бакс за фотку.")
    ])
    call phone_chat([
        ["", t_("Я тебе заплачу 1 бакс за фотку.")],
        ["whore", t_("1 бакс?")],
        ["", t_("Да.")]
    ])
    $ add_money(-1.0)
    call phone_chat([
        ["whore", t_("За бакс без обнаженки.")],
        ["", t_("Окей.")],
        ["whore", "image", "/images/Phone/Photos/whore_photo1.png", 3],
        ["whore", t_("Доволен?")],
        ["", t_("Ееее! Красотка!")],
        ["whore", t_("После личной встречи смогу кидать тебе фотки погорячее.")],
        ["", t_("Понял. Напишу тебе.")],
        ["whore", t_("Буду ждать, красавчик. Пока.")],
        ["", t_("Пока.")]
    ])
    $ phone_gallery_add_image("Whore_1")
    $ whoreCallStage = 3
    $ add_hook("phone_close", "ep12_quests14b_sean_afterphone", scene="phone", once=True, quest="day2")

    return

label emily_chat1:
    $ phone_start_new_chat("whore_chat2", "Emily")
    call phone_chat([
        ["student_emily", "image", "/images/Phone/Photos/emily_photo1.png", 3],
        ["student_emily", t_("Собираюсь спать. Решила написать, что я согласна провести тебе небольшую экскурсию.")]
#        ["student_emily", "",5]
    ])
    $ phone_close_enabled = False
    pause 2.0
    bardi_t "Ммм... Какая же она красотка!"
    call phone_chat_menu([
        t__("О! Эмили, привет! А как ты узнала мой телефон?")
    ])
    call phone_chat([
        ["", t_("О! Эмили, привет! А как ты узнала мой телефон?")],
        ["student_emily", t_("Все просто, спросила у всезнайки Сары.")],
        ["", t_("Ясно. И какой у нас план?")],
        ["student_emily", t_("Еще не придумала. Я потом тебе напишу. Все, пока!")]
    ])
    $ phone_close_enabled = False
    pause 2.0
    bardi_t "Пока? Вот уж нет! Надо что-то еще ей написать..."
    bardi_t "О, придумал!"
    call phone_chat([
        ["", t_("Сначала шкафчик, потом дорога к спортзалу, теперь это...")],
        ["", t_("Так много общего...")],
        ["", t_("Мне кажется или это неслучайно? ;)")],
        ["student_emily", t_("Ты прав...")]
    ])
    $ phone_close_enabled = False
    pause 2.0
    bardi_t "Ого!"
    call phone_chat([
        ["student_emily", t_("Тебе кажется.")],
        ["", t_("Окей! Это была просто шутка!")],
        ["", t_("И кстати! Где фотка, которую ты обещала?")],
        ["student_emily", t_("Какая фотка? Я ничего не обещала.")],
        ["", t_("Как? Фотка, которую я жду.")],
        ["student_emily", t_("Ах эта! Да, сейчас пришлю...")]
    ])
    $ phone_close_enabled = False
    pause 2.0
    bardi_t "Так-так! Интересно, чем Эмили меня порадует?!"
    call phone_chat([
        ["student_emily", t_("Вот, держи! :)")],
        ["student_emily", "image", "/images/Phone/Photos/cartoon_cat.png", 3],
        ["", t_("Эээм...")],
        ["student_emily", t_("Ты эту фотку просил?")],
        ["", t_("Да... Ну почти. Сохраню себе на память...")],
        ["student_emily", t_("Отлично! Рада, что тебе понравилось! Пока-пока!")]
    ])
    $ phone_close_enabled = False
    pause 2.0
    bardi_t "Да уж. Фотка - огонь! Чего угодно ожидал, но не кота..."
    call phone_chat([
        ["student_emily", t_("Окей! Это была просто шутка!")],
        ["student_emily", t_("Не скучай, шутник. Вот твоя фотка...")],
        ["student_emily", "image", "/images/Phone/Photos/emily_photo2.png", 3]
    ])
    $ phone_close_enabled = False
    pause 2.0
    $ phone_close_enabled = True
    bardi_t "Класс! Эта фотка даже лучше чем первая!"
    bardi_t "Жаль, что их только две..."
    
    $ phone_gallery_add_image("900757")
    $ phone_gallery_add_image("Emily_Cat")
    $ phone_gallery_add_image("900758")

    return


#call_labels_on
#export_speaker_on
