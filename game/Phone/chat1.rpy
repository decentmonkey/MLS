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

label cynthia_chat3:
    $ phone_start_new_chat("cynthia3", "Cynthia")
    call phone_chat([
        ["", t_("Привет, Синтия! Как дела?")],
        ["", t_("Ты в колледже?")],
        ["cynthia", t_("Привет, [mcname]! Уже нет :)")],
        ["cynthia", t_("Мы с Николь договорились встретиться и погулять после колледжа.")],
        ["cynthia", t_("Я с ней сейчас.")],
        ["", t_("Окей. Хорошей прогулки. Если вечером не увидимся, потом поболтаем :)")],
        ["cynthia", t_("Окей :)")]
    ])
    return

label cynthia_chat4:
    $ phone_start_new_chat("cynthia_chat4", "Cynthia")
    call phone_chat([
        ["", t_("Да?")],
        ["cynthia", t_("Прости, [mcname], я тебя разбудила?")],
        ["", t_("Нет, все хорошо. Что-то случилось?")],
        ["cynthia", t_("Нет, ничего особенного. Просто, мы уже вернулись, и...")],
        ["cynthia", t_("Только сейчас поняли, что забыли ключи от дома...")],
        ["cynthia", t_("Я звонила Оливии, но она, видимо, крепко спит.")],
        ["cynthia", t_("Открой, пожалуйста, дверь.")],
        ["", t_("Да, сейчас.")]
    ])
    return

label cynthia_chat5:
    $ phone_start_new_chat("cynthia_chat5", "Cynthia")
    call phone_chat([
        ["", t_("Привет, Синтия.")],
        ["cynthia", t_("Привет! :)")],
        ["cynthia", t_("Как дела? Все готово?")],
        ["", t_("Еще нет...")],
        ["", t_("Но скоро все будет, не переживай.")],
        ["cynthia", t_("Мне уже не терпится! :)")],
        ["", t_("Как будет все сделано, я тебе сразу сообщу.")],
        ["", t_("Хорошо. Жду.")],
        ["", t_("Спасибо тебе за помощь, [mcname]!")],
        ["", t_("Ты лучший! :)")]
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

label sean_chat5:
    $ phone_start_new_chat("sean_chat5", "Sean")
    call phone_chat([
        ["", t_("В субботу вечеринка у какого-то Уокера.")],
        ["", t_("Ты знаешь этого чувака?")],
        ["sean", t_("Ага. Давай позже. Я на математике.")],
        ["sean", "image", "/images/Phone/Photos/clark_photo1.png", 3]
    ])
    $ phone_gallery_add_image("Clark_foto")
    # следом от Шона приходит фотка, на которой Кларк орет и тычет пальцем на одного из студентов, которые не в группе Барди, у доски
    return

label sean_chat6:
    $ phone_start_new_chat("sean_chat6", "Sean")
    call phone_chat([
        ["sean", t_("Эй, бро! Привет!")],
        ["sean", t_("Ты где? Давай скорее на вечеринку! Тут уже все напились!")],
        ["", t_("Привет, Шон. Ага, уже иду.")],
        ["sean", t_("Эй, чувак, не забудь презервативы!")],
        ["", t_("Ха-ха! Окей.")]
    ])
    return

label sean_chat7:
    $ phone_start_new_chat("sean_chat7", "Sean")
    call phone_chat([
        ["", t_("Привет, бро.")],
        ["", t_("Спасибо, что выручил меня вчера!")],
        ["sean", t_("Привет, чувак!")],
        ["sean", t_("Да без проблем :)")],
        ["sean", t_("Как ты? Много синяков?")],

        ["", t_("Не-а. Вообще никаких следов, прикинь?!")],
        ["sean", t_("Воу! Ну круто!")],
        ["", t_("Давай сегодня пересечемся в перерыве между занятиями?")],
        ["sean", t_("Я сегодня не иду в колледж, бро. У меня дела.")]
    ])
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        call phone_chat([
            ["", t_("Опять какую-нибудь красотку домой притащишь?")],
            ["sean", t_("Ахаха! Неее...")]
        ])
    call phone_chat([
        ["", t_("Что за дела?")],
        ["sean", t_("Да так... Семейные дела.")],
        ["", t_("Я понял.")],
        ["sean", t_("Ну все, мне пора. Спишемся позже. Передавай привет Софи!")],
        ["", t_("Окей. Пока.")],
        ["sean", t_("Пока :)")],
    ])
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

label sophie_chat4:
#label ep03_dialogues1_family_morning_3:
    ## не рендерить!
    $ phone_start_new_chat("sophie_chat4", "Sophie")
    call phone_chat([
        ["sophie", t_("[mcname], милый, я тебя не отвлекаю?")],
        ["", t_("Нет. У меня как раз перерыв между занятиями. Что-то случилось?")],
        ["sophie", t_("Мне сейчас позвонил Генри. Мистер Райт сегодня заезжал к нему на работу.")],
        ["sophie", t_("Генри поговорил с ним насчет твоей подработки.")],
        ["", t_("О, ну хорошо. Что этот Райт сказал?")],
        ["sophie", t_("Он согласен взять тебя к себе в помощники.")],
        ["sophie", t_("Мистер Райт сказал, что сегодня ближе к вечеру он будет на пляже.")],
        ["sophie", t_("Так что, если для тебя все еще актуальна подработка, то можешь после колледжа встретиться с ним.")],
        ["", t_("Это отличная новость. Спасибо, Софи!")],
        ["sophie", t_("Не за что, милый.")],
        ["sophie", t_("Удачно провести встречу с мистером Райтом.")],
        ["sophie", t_("Да, и постарайся не задерживаться. К нам в гости сегодня придет моя сестра.")],
        ["sophie", t_("Так что мы будем тебя ждать к ужину.")],
        ["", t_("Окей. Договорились.")],
        ["sophie", t_("До вечера, милый.")],
        ["", t_("Пока.")]
    ])
    $ mlsBardiDay4FamilyMorning2 = day # Мистер Райт ждет Барди после колледжа на пляже
    return

label sophie_chat5:
    $ phone_start_new_chat("sophie_chat5", "Sophie")
    call phone_chat([
        ["sophie", t_("[mcname], мы ждем тебя на ужин. Ты не забыл?")],
        ["sophie", t_("Моя сестра Дейзи уже пришла. Поторопись, пожалуйста, милый.")],
        ["", t_("Окей. Уже иду домой.")],
        ["sophie", t_("Хорошо :)")]
    ])
    return

label sophie_chat6:
    $ phone_start_new_chat("sophie_chat6", "Sophie")
    call phone_chat([
        ["sophie", t_("[mcname], как у тебя дела?")],
        ["sophie", t_("Мы уже поужинали, не дождались тебя.")],
        ["sophie", t_("Время позднее. У тебя все в порядке?")],
        ["", t_("Окей. Уже иду домой.")],
        ["sophie", t_("Хорошо :)")]
    ])
    call phone_chat_menu([
        t__("Скоро буду дома."),
        t__("Не отвечать.")
    ])
    if _return == 0:
        call phone_chat([
            ["", t_("У меня были важные дела. Прости, что не предупредил.")],
            ["", t_("Скоро буду дома.")],
            ["sophie", t_("Хорошо, милый. Жду :)")],
            ["", t_("Окей :)")]
        ])
    else:
        bardi_t "Позже ей отвечу."
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
    $ phone_start_new_chat("emily_chat1", "Emily")
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

label emily_chat2:
    # chat emily
    $ phone_start_new_chat("emily_chat2", "Emily")
    call phone_chat([
        ["", t_("Привет, Эмили!")],
        ["", t_("Как насчет погулять сегодня?")],
        ["student_emily", t_("Привет, [mcname].")],
        ["student_emily", t_("Сегодня не получится, я занята :(")],
        ["student_emily", t_("Давай, в среду днем, как и договаривались.")],
        ["", t_("Окей.")]
    ])
    return

label emily_chat3:
    # chat emily
    $ phone_start_new_chat("emily_chat3", "Emily")
    call phone_chat([
        ["", t_("Привет, Эмили!")],
        ["student_emily", t_("Привет, [mcname]! :)")],
        ["", t_("Я тут на пляже. Мы договаривались погулять, помнишь?")],
        ["student_emily", t_("Да, точно!")],
        ["student_emily", t_("Я скоро буду! Жди! ;););)")],
        ["", t_("Жду :)")]
    ])
    return

label emily_chat4:
    # chat emily
    $ phone_start_new_chat("emily_chat4", "Emily")
    call phone_chat([
        ["", t_("Привет, Эмили!")],
        ["student_emily", t_("Привет, [mcname]! :)")],
        ["", t_("Я тут на пляже. Мы договаривались погулять, помнишь?")],
        ["student_emily", t_("Да, точно! Ты уже на пляже?")],
        ["", t_("Скоро буду там. Если ты, конечно, свободна сегодня.")],
        ["student_emily", t_("Да-да, я свободна. Я скоро буду! ;););)")],
        ["", t_("Отлично, тогда выдвигаюсь :)")]
    ])
    return

label emily_chat5:
    # chat emily
    $ phone_start_new_chat("emily_chat5", "Emily")
    call phone_chat([
        ["student_emily", "image", "/images/Phone/Photos/emily_photo3.png", 3]
    ])
    return

label emily_chat6:
    $ phone_start_new_chat("emily_chat6", "Emily")
    call phone_chat([
        ["", t_("Привет, принцесса!")],
        ["student_emily", t_("Привет, [mcname] :)")],
        ["student_emily", t_("Как ты после вчерашнего?")],
        ["", t_("Могло бы быть лучше, если бы ты не сбежала...")],
        ["student_emily", t_("А если бы твой друг зашел в раздевалку на пять минут позже?..")],
        ["", t_("Ахаха! Я представляю эту сцену!")],
        ["student_emily", t_("Нет, я даже представлять этого не хочу...")],
        ["", t_("xD")],
        ["student_emily", t_("Я рада, что ты в порядке :)")],

        ["", t_("Может, встретимся как-нибудь вечером?")],
        ["student_emily", t_("Возможно. Но точно не сегодня.")],
        ["student_emily", t_("Я тебе напишу, когда у меня будет свободное время.")],
        ["", t_("Окей. Буду ждать :)")],
        ["student_emily", t_("Договорились. Пока :)")],
        ["", t_("Пока.")]
    ])
    return


label daisy_chat1:
    $ phone_start_new_chat("daisy_chat1", "Daisy")
    call phone_chat([
        ["", t_("Дейзи, привет.")],
        ["daisy", t_("Привет, [mcname] :)")],
        ["", t_("Как дела на работе? Помощь не нужна?")],
        ["daisy", t_("Ахаха! Я тебе напишу, когда мне нужна будет твоя помощь с краш-тестами.")],
        ["daisy", t_("Наберись терпения, красавчик ;)")],
        ["", t_("Окей. Буду ждать :)")],
        ["daisy", t_("Чмоки!")]
    ])
    return

label daisy_chat2:
    $ phone_start_new_chat("daisy_chat2", "Daisy")
    call phone_chat([
        ["daisy", t_("Привет, красавчик! :)")]
    ])
    call phone_chat_menu([
        t__("Ответить."),
        t__("Позже.")
    ])
    if _return == 0:

        call phone_chat([
            ["", t_("О, Дейзи! Привет!")],
            ["", t_("Как у тебя дела? Как бизнес?")],
            ["daisy", t_("Ой, все хорошо!")],
            ["daisy", t_("Как раз пишу тебе, чтобы похвастаться новым поступлением товара :):):):):)")],
            ["", t_("Ну круто. И что это за товары?")],
            ["daisy", t_("Вряд ли их названия тебе что-то скажут...")],
            ["daisy", t_("Но я могу показать фотографии ;)")],
        ])
        call phone_chat_menu([
            t__("Хммм... Ну, давай."),
        ])
        call phone_chat([
            ["", t_("Хммм... Ну, давай.")],
            ["daisy", t_("Ты сейчас один?")],
            ["", t_("Да.")],
            ["daisy", t_("Тогда держи ;)")],
            ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo1.png", 3],
            ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo2.png", 3]
        ])
        if mlsBardiFamilyDaisyCrashTest1 == 0:
            $ phone_gallery_add_image("foto_Daisy_1")
            $ phone_gallery_add_image("foto_Daisy_2")
        $ phone_close_enabled = False
        bardi_t "Вот это да!.."
        $ phone_close_enabled = True
        call phone_chat([
            ["", t_("Вау! Ты безумно секси!")],
            ["daisy", t_("У тебя встал? :)")],
            ["", t_("Естественно!")],
            ["daisy", t_("Я знала. Можешь использовать мои фото, чтобы снять напряжение...")],
            ["daisy", t_("Ну а если об игрушке...")],
            ["daisy", t_("Это обалденно!")],
            ["daisy", t_("Материал безумно приятный для кожи.")],
            ["daisy", t_("При этом совершенно не раздражает ее, а еще он гипоаллергенный.")],
            ["daisy", t_("В общем, качество на высоте.")],
            ["daisy", t_("Да и на практике показывает себя вполне достойно.")],
            ["daisy", t_("Я кончила с ним 4 раза!")],
            ["", t_("Я смотрю, ты там веселишься вовсю?")],
            ["daisy", t_("Ничего подобного! Это рабочий процесс!")],
            ["", t_("Хах! Охрененная у тебя работа!..")],
            ["daisy", t_("Я знаю ;)")],
            ["daisy", t_("Кстати, о работе. Заходи ко мне вечером.")],
            ["daisy", t_("У меня для тебя есть кое-какая работа.")],
            ["", t_("Окей. Отлично.")],
            ["daisy", t_("Ладно, надеюсь, я смогла поднять тебе настроение.")],
            ["daisy", t_("Пошла дальше работать.")],
            ["daisy", t_("Удачи :)")],
            ["", t_("И тебе тоже :)")]
        ])
        call process_hooks("daisy_call_event2", "events")

        $ mlsBardiFamilyDaisyCrashTest1 = day # Дейзи прислала Барди свои фотки
    else:
        bardi_t "Позже ей напишу."
    return


label daisy_chat3:
    $ phone_start_new_chat("daisy_chat3", "Daisy")
    call phone_chat([
        ["daisy", t_("[mcname], прости за эти таблетки. Как ты?")],
        ["", t_("Нормально... Ты сама то как?")],
        ["daisy", t_("Ох, лучше некуда. Только устала как собака...")]
    ])
    $ phone_close_enabled = False
    bardi_t "Это она то устала?! Мне бы так уставать!"
    $ phone_close_enabled = True
    call phone_chat([
        ["", t_("Понимаю...")],
        ["daisy", t_("В общем, прости за таблетки. И за то, что все так вышло...")],
        ["daisy", t_("Я не знала, что девочки вернутся так рано.")],
        ["daisy", t_("Николь говорила, что они будут гулять допоздна...")],
        ["", t_("Все окей, Дейзи.")],
        ["", t_("Но то, что я пообещал тебе перед уходом, так все и будет.")],
        ["daisy", t_("Будто я против ;)")],
        ["daisy", t_("Когда все лягут спать, я скину тебе кое-что особенное. Так что жди :)")],
        ["", t_("Окей. Жду :)")]
    ])
    return

label daisy_chat4:
    $ phone_start_new_chat("daisy_chat4", "Daisy")
    call phone_chat([
        ["daisy", t_("Привет, красавчик. Я снова тут ;)")],
        ["daisy", t_("Как и обещала, кидаю тебе несколько фоток, чтобы снять напряжение :)")],
        ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo_b1.png", 2],
        ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo_b2.png", 2],
        ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo_b3.png", 2],
        ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo_b4.png", 2],
        ["daisy", "image", "/images/Phone/Photos/phone_daisy_photo_b5.png", 2]
    ])
    $ phone_gallery_add_image("Daisy_1")
    $ phone_gallery_add_image("Daisy_2")
    $ phone_gallery_add_image("Daisy_3")
    $ phone_gallery_add_image("Daisy_4")
    $ phone_gallery_add_image("Daisy_5")
    $ phone_close_enabled = False
    bardi_t "Мдаа... Веселая же была ночка..."
    $ phone_close_enabled = True
    call phone_chat([
        ["", t_("Фотки огонь!")],
        ["", t_("Ты такая секси! ;)")]
    ])
    $ daisyCallStage = 0
    return

label olivia_chat1:
    $ phone_start_new_chat("olivia_chat1", "Olivia")
    call phone_chat([
        ["olivia", t_("Скажи, что мне просто приснился плохой сон.")],
        ["", t_("Ой нет. Ну точно нет. Люди, которых мучают кошмары, априори так крепко дрыхнуть не могут.")],
        ["olivia", t_("Засунь свои шутки себе в задницу. Я про вчерашний вечер.")],
        ["", t_("Ну а что? Вечер как вечер... Не считая задушевных разговоров под бутылочку вискаря...")],
        ["", t_("Который ты любезно всосала в одного почти весь за считанные минуты.")],
        ["", t_("Хах...")],
        ["", t_("Твой вечер ну точно никак нельзя назвать кошмаром.")],
        ["", t_("Тебе, на сколько я понял, было вообще по кайфу. А вот мой вечер - да...")],
        ["", t_("Тащить тебя на второй этаж, а потом еще носить тебя на руках по комнатам...")],
        ["olivia", t_("ФАК!!!")],
        ["olivia", t_("Это все из-за того, что ты влез не в свое дело! Вот надо тебе оно было?!")],
    ])
    call phone_chat_menu([
        t__("Да... А потом еще и отбиваться от твоих пьяных домогательств...")
    ])
    call phone_chat([
        ["", t_("Да... А потом еще и отбиваться от твоих пьяных домогательств...")],
        ["olivia", t_("Врешь! Быть такого не может! Я помню вчерашний вечер.")],
        ["", t_("Ладно, это было просто дружеское преувеличение.")],
        ["olivia", t_("Пошел ты!")],
        ["olivia", t_("Все уже пришли?")],
    ])
    call phone_chat_menu([
        t__("Да. Все, кроме Генри, дома.")
    ])
    call phone_chat([
        ["", t_("Да. Все, кроме Генри, дома.")],
        ["olivia", t_("Че-е-ерт!")],
        ["olivia", t_("Ладно, как все разойдутся, зайдешь ко мне! Понял?")],
        ["", t_("И даже без волшебного слова?")],
        ["olivia", t_("Не нарывайся!")],
        ["", t_("Хах... Ладно-ладно.")],
        ["", t_("Только не злись. Будь добрее и люди к тебе потянутся.")],
        ["", t_("В особенности, маленькие миленькие блондинки...")],
        ["olivia", t_("Я убью тебя!")],
        ["", t_("Так ладно, все. Мне тут нужно слушать офигенные истории от Синтии.")],
        ["", t_("Сообщу тебе, когда все разойдутся.")]
    ])
    return

label olivia_chat2:
    $ phone_start_new_chat("olivia_chat2", "Olivia")
    call phone_chat([
        ["", t_("Привет :)")],
        ["olivia", t_("Ты уже поговорил с Синтией?")],
        ["", t_("Еще нет. Как раз собираюсь заняться этим вопросом...")],
        ["olivia", t_("Какого черта так долго?!")],
        ["olivia", t_("Давай скорее, я жду!")]
    ])
    return

label olivia_chat3:
    $ phone_start_new_chat("olivia_chat3", "Olivia")
    call phone_chat([
        ["", t_("Привет, Оливия!")],
        ["olivia", t_("Ну? Какие новости?")],
        ["", t_("Я пообщался с Синтией. Скоро расскажу тебе все.")],
        ["olivia", t_("Давай скорее, я жду!")]
    ])
    return

label olivia_chat4:
    $ phone_start_new_chat("olivia_chat4", "Olivia")
    call phone_chat([
        ["", t_("Привет, Оливия! Как дела?")],
        ["olivia", t_("Привет. Ты уже нашел деньги для подарка?")],
        ["", t_("Воу! Не так быстро!")],
        ["", t_("Нашла миллионера!")],
        ["", t_("Мне еще надо обдумать, как все это провернуть...")],
        ["olivia", t_("Сообщи, как все уладишь.")],
        ["olivia", t_("Я жду.")],
        ["", t_("Вас понял, госпожа.")],
        ["olivia", t_("Да пошел ты!")]
    ])
    return


label sarah_chat1:
    $ phone_start_new_chat("sarah_chat1", "Sarah")
    call phone_chat([
        ["student_sarah", t_("[mcname], привет :)")],
    ])
    $ phone_close_enabled = False
    bardi_t "Опа... Сара пишет..."
    bardi_t "Наверное, сдаться надумала, да?"
    $ phone_close_enabled = True
    call phone_chat([
        ["", t_("Привет. Надеюсь, ты там не с бургером сидишь?")],
        ["student_sarah", t_("Конечно, нет! Ты что?!")],
        ["student_sarah", t_("Просто хотела тебе сказать...")],
        ["student_sarah", t_("Спасибо большое, что помог мне.")],
        ["student_sarah", t_("Дальше я, наверное, сама позанимаюсь.")],
        ["student_sarah", t_("Но если мне будет нужна твоя помощь, я тебе напишу, ок?")],
        ["", t_("Окей. Удачи!")],
        ["student_sarah", t_("Спасибо. Я не подведу :)")]
    ])
    return

label sarah_chat2:
    $ phone_start_new_chat("sarah_chat2", "Sarah")
    call phone_chat([
        ["", t_("Эй, Сара. Как дела с тренировками?")],
        ["student_sarah", t_("[mcname], привет! Все отлично! :)")]
    ])
    call phone_chat_menu([
        t__("Предложить помощь."),
        t__("Позже.")
    ])
    if _return == 0:
#        "Предложить помощь.":
        call phone_chat([
            ["", t_("Моя помощь нужна?")],
            ["student_sarah", t_("Нет-нет. У меня все под контролем, [mcname].")],
            ["student_sarah", t_("Я же сказала, что не подведу ;)")],
            ["", t_("Окей. Если что - я на связи.")],
            ["student_sarah", t_("Хорошо. Спасибо за поддержку, [mcname].")],
            ["", t_("Без проблем. Пока, Сара.")],
            ["student_sarah", t_("До встречи.")]
        ])
    else:
#        "Позже.":
        call phone_chat([
            ["", t_("Окей. Пиши, если что.")],
            ["student_sarah", t_("Хорошо, [mcname]. Спасибо :)")]
        ])
    return    


#call_labels_on
#export_speaker_on
