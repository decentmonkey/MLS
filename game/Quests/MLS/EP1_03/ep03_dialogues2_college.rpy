define student_arnie = Character(t_("Арни"), who_color=c_blue) # студент из колледжа, Арни Уокер (classmate4)
define student_girl1 = Character(t_("Студентка"), who_color=c_pink) # студентка
define student_girl2 = Character(t_("Студентка"), who_color=c_green) # студентка
define student_girl3 = Character(t_("Студентка"), who_color=c_orange) # студентка - девочка с каре и в джинсах из группы Барди
define student_girl4 = Character(t_("Студентка"), who_color=c_pink) # студентка
define student_boy1 = Character(t_("Студент"), who_color=c_gray) # студент
define student_boy2 = Character(t_("Студент"), who_color=c_blue) # студент
define student_abby = Character(t_("Эбби"), who_color=c_pink) # студентка из группы Барди (Abby)
define student_katie = Character(t_("Кэти"), who_color=c_orange) # студентка - девочка с каре и в джинсах из группы Барди (Katie)

default mlsBardiDay4College1 = 0 # Эмили согласилась провести Барди экскурсию
default mlsBardiDay4College2 = 0 # Роуз предложила Барди работать над эссе вместе
default mlsBardiDay4College3 = 0 # Барди солгал Морис, что занимался раньше живописью
#default mlsBardiDay4College4 = 0 # Барди должен доделать картину к следующему занятию живописи
default mlsBardiDay4College5 = 0 # Барди выпил виски в начале вечеринки
default mlsBardiDay4College6 = 0 # Барди пообщался на вечеринке с ботаном Лео
default mlsBardiDay4College7 = 0 # Барди пообщался на вечеринке с фриком Хлоей
#default mlsBardiDay4College8 = 0 # Барди на вечеринке общался с Сарой
default mlsBardiDay4College9 = 0 # Барди на вечеринке ахнул двух подружек

default ep03_dialogues2_college_3_menu1 = False
default ep03_dialogues2_college_3_menu2 = False
default ep03_dialogues2_college_3_menu3 = False

default ep03_dialogues2_college_4_menu1 = False
default ep03_dialogues2_college_4_menu2 = False

default ep03_dialogues2_college_18_menu1 = False
default ep03_dialogues2_college_18_menu2 = False

default ep03_dialogues2_college_19_menu1 = False
default ep03_dialogues2_college_19_menu2 = False

define v_MC_Classmate_Nicole1_25_sound_name = "v_MC_Classmate_Nicole1_25"
define v_MC_Classmate_Nicole2_25_sound_name = "v_MC_Classmate_Nicole2_25"
define v_MC_Classmate_Nicole3_25_sound_name = "v_MC_Classmate_Nicole3_25"
define v_MC_Classmate_Nicole4_25_sound_name = "v_MC_Classmate_Nicole4_25"
define v_MC_Classmate_Nicole5_25_sound_name = "v_MC_Classmate_Nicole5_25"
define v_MC_Classmate_Nicole6_25_sound_name = "v_MC_Classmate_Nicole6_25"

#call ep03_dialogues2_college_1() # разговор с Шоном у колледжа
#call ep03_dialogues2_college_2() # разговор у шкафчиков с Эмили
#call ep03_dialogues2_college_3() # урок инглиша
#call ep03_dialogues2_college_3a() # мысли после урока инглиша
#call ep03_dialogues2_college_4() # встреча в холле с Миссис Морис
#call ep03_dialogues2_college_5() # урок живописи
#call ep03_dialogues2_college_5a() # после крока живописи встреча в холле с Шоном
#call ep03_dialogues2_college_6() # при клике на библиотеку
#call ep03_dialogues2_college_6a() # при клике на строку контакта "cynthia"
#call ep03_dialogues2_college_7() # при клике на спортзал
#call ep03_dialogues2_college_8() # при клике на кабинет математики
#call ep03_dialogues2_college_9() # при клике на дверь приемной директора колледжа, либо на какие-то другие локации
#call ep03_dialogues2_college_10() # при клике на выход из колледжа
#call ep03_dialogues2_college_11() # звонок на телефон от Шона после того, как вышел от тети Дейзи вечером
#call ep03_dialogues2_college_12() # пришел на вечеринку
#call ep03_dialogues2_college_13() # при клике на столик с алкоголем
#call ep03_dialogues2_college_13a() # при клике на Лео до общения с Хлоей
#call ep03_dialogues2_college_15() # при клике на Эмили и Гарри
#call ep03_dialogues2_college_16() # при клике на фрика Хлою
#call ep03_dialogues2_college_14() # подходит к дивану, где сидит Лео
#call ep03_dialogues2_college_18() # при клике на зануду Сару
#call ep03_dialogues2_college_19() # при клике на парочку целующихся девчонок

# при клике на локацию Колледж на карте города
label ep03_dialogues2_college_1:
    # Барди стоит перед входом в колледж
    # внезапно его хлопает по плечу рука Шона
    music Shining_Through
    imgf 900767
    w
    sound Jump1
    img 901418 hpunch
    bardi "Черт!"
    # в кадре возникает его довольная мина
    sound Jump2
    img 901419 vpunch
    sean "Эй, бро! Привет!"
    imgd 901420
    bardi "Чувак, ты меня напугал!.."
    imgd 901421
    sound laughing_male2
    sean "Думал, что это твой приятель Гарри с тобой решил поздороваться?" # хихикает
    imgd 901422
    bardi "Ага. Поздороваться и пожелать мне хорошего дня... После того, как вчера чуть не прибил меня."
    imgd 901423
    sean "О, серьезно?! А что случилось, бро?"
    imgd 901424
    bardi "А, ну да. Вчера же кое-кто был очень занят своими делами и все пропустил."
    imgd 901425
    sean "Давай рассказывай!"
    imgd 901424
    bardi "По ходу, Гарри приревновал меня к Эмили. Прикинь?!"
    imgd 901426
    sean "Да ладно! Ты шутишь!"
    imgd 901424
    bardi "Вчера мне было не до шуток. Этот придурок гонялся за мной по колледжу."
    # если днем, в колледже, Барди смотрел фотку Эмили и выложил в сеть (крыса)
    if mlsBardiDay3College4 > 0:
#        img 901424
        bardi "А после занятий я видел, что он разругался с Эмили."
    # если днем, в колледже, не смотрел фотку Эмили и сразу отдал телефон (кролик)
    else:
#        img 901424
        bardi "А после занятий подкараулил у входа в колледж и вцепился в меня."
        bardi "На этот раз обошлось без синяков."
    imgd 901427
    sean "Охренеть! А из-за чего он так взбесился?"
    imgd 901424
    bardi "Да я ничего такого не сделал... Просто взял Эмили за руку, а он это увидел..."
    imgd 901421
    sean "Ты что, решил подкатить к первой красотке колледжа?! Ха-ха, ну ты даешь!"
    sean "Тебе не светит трах с ней, приятель. Она с такими простыми смертными, как мы с тобой, даже не разговаривает."
    sean "Не уверен, что она вообще знает о нашем существовании."
    sean "У тебя нет шансов, [mcname]!"
    music Step_By_Step
    imgd 901422
    bardi "Посмотрим..."
    imgd 901428
    sean "Зря потратишь свое время, бро."
    # если Барди ходил к Шону и была сцена с Бекки
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        imgd 901422
        bardi "Ты мне лучше расскажи подробнее про свою 'подружку' Бекки..."
        bardi "Что там у тебя за темы с ней? Или ты все-таки заплатил ей за встречу?"
    # если знакомства с Бекки не было
    else:
        imgd 901422
        bardi "Ты мне лучше расскажи, что у тебя за дела такие важные вчера были?"
    imgd 901428
    sean "Чувак, я тебе обязательно все расскажу. Только не здесь и не сейчас." # подмигивает и довольно улыбается
    sound Jump1
    imgd 901429
    w
    imgd 901422
    sean "У меня сейчас математика, поэтому лучше поторопиться."
    # Шон разворачивается и идет ко входу в колледж, на ходу поворачивается к Барди
    sound step_stairs_short
    imgf 901430
    w
    imgd 901431
    sean "Пошли! Чего ты там застрял?"
    imgd 901430
    bardi_t "Хмм... Он явно не торопится делиться со мной подробностями..."
    # Барди догоняет Шона и они заходят в колледж
    return

# в холле колледжа, у шкафчика Барди
label ep03_dialogues2_college_2:
    # Шон уходит по коридору в сторону лестницы, машет Барди рукой
    fadeblack 1.0
    music Shining_Through
    imgfl 901432
    w
    imgf 901433
    sean "Встретимся после занятий, бро!"
    imgd 901434
    bardi "Окей."
    # у шкафчиков стоит Эмили, как обычно с телефоном в руке, делает селфи
    sound snd_runaway
    imgd 910035
    w
    fadeblack 1.0
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgf 901435
    bardi_t "А вот и красотка Эмили..."
    # две фразы, взависимости от того, присылала ли она ему фотки ранее
    imgd 901436
    bardi "Привет, Эмили!"
    $ photoshoot_flash()
    imgd 901437
    student_emily "Привет." # продолжая фоткаться
    $ photoshoot_flash()
#    sound snd_photo_capture
    imgd 901436
    bardi "Делаешь фотки для своей инсты?"
    # если днем, в колледже, Барди смотрел фотку Эмили и выложил в сеть (крыса)
    if mlsBardiDay3College4 > 0:
        # она, не глядя на него, продолжает фоткаться
        imgd 901438
        student_emily "Чего тебе? Не видишь, я занята?"
#        sound snd_photo_capture
        $ photoshoot_flash()
        imgd 901439
        bardi "Да я просто хотел спросить, как дела."
        bardi "Ты вчера была такая расстроенная после разговора со своим парнем..."
        # она отрывается от своего телефона и с подозрением смотрит на Барди
        sound Jump1
        img 901440 hpunch
        student_emily "Что-то я не пойму, с чего ты так интересуешься моими делами?"
        student_emily "И я не была расстроена!"
        imgd 901441
        bardi "Ну-ну. Значит, мне показалось."
        imgd 901442
        sound iphone_typing
        student_emily "Вот именно!" # снова отворачивается от него
        imgd 901443
        bardi "Слушай, Эмили..."
        imgd 901444
        student_emily "Ну что еще?"
        imgd 901445
        bardi "Я видел твой аккаунт в инсте. У тебя крутые фотки..."
        imgd 901444
        student_emily "Да, но в сеть я выкладываю далеко не все свои фото... Есть еще лучше."
        imgd 901445
        bardi "Хм... Я не отказался бы посмотреть на них."
        imgd 901446
        student_emily "Намекаешь на то, чтобы я тебе их скинула?" # холодно
    # если днем, в колледже, не смотрел фотку Эмили и сразу отдал телефон (кролик)
    else:
    # Барди говорит, что классные фотки
        imgd 901444
        student_emily "Ага. Давно ничего нового не выкладывала."
        imgd 901445
        bardi "Мне понравились фотки, которые ты мне прислала..."
        imgd 901446
        student_emily "Намекаешь на то, чтобы я тебе еще свои фото скинула?"
    menu:
        "Было бы неплохо...":
            music Step_By_Step
            imgd 901447
            bardi "Да, было бы здорово."
            # тут она загадочно улыбается, глядя на него
            imgd 901448
            student_emily "Я подумаю..."
            # если накануне переписывался с Эмили
            if mlsBardiDay3College4 == 0:
                imgd 901447
                bardi "А что насчет небольшой экскурсии по городку?"
                bardi "Может, договоримся о встрече?"
            # если не перписывался
            else:
                imgd 901447
                bardi "А еще я не против небольшой экскурсии по Санвилю."
                bardi "В знак благодарности, что я помог тебе найти твой телефон..."
            imgd 901449
            student_emily "Хмм..."
            bardi "Встретимся на днях? Можно было бы сходить вместе на пляж..."
            imgf 901450
            bardi "Или просто прогуляться. Посмотреть какие-нибудь красивые места..." # взгляд на грудь Эмили
            imgd 901449
            w
            # она улыбается ему
            pass
        "Конечно! Но я хотел спросить не об этом...":
            music Step_By_Step
            imgd 901447
            bardi "Конечно! Но я хотел спросить не об этом..."
            # она на него подозрительно косится
            imgd 901451
            student_emily "О чем же?"
            imgd 901447
            bardi "Я вчера помог тебе с поиском твоего телефона..."
            # если накануне переписывался с Эмили
            if mlsBardiDay3College4 == 0:
#                img 901447
                bardi "А ты уже дала свое согласие на экскурсию..."
                bardi "Может, договоримся о встрече?"
            # если не перписывался
            else:
#                img 901447
                bardi "Проведешь мне небольшую экскурсию по городку? В знак благодарности."
#            img 901447
            bardi "Я так давно тут не был и совсем забыл Санвиль..."
            # она недружелюбно
            imgd 901451
            student_emily "Проблемы с памятью?"
            imgd 901447
            bardi "Видимо, да..."
            bardi "Ну так что ты скажешь насчет экскурсии? Как-нибудь на днях..."
            student_emily "..."
            # она с покерфейсом смотрит на него оценивающе, задумчиво
            imgd 901452
            student_emily "Хмм..."
            imgd 901449
            w
            # потом внезапно эмоция меняется на улыбку (у нее возникла какая-то идея)
            pass
    $ mlsBardiDay4College1 = day # Эмили согласилась провести Барди экскурсию
    music Shining_Through
#    sound2 Jump1
    imgd 901453
    student_emily "А знаешь... Почему бы и нет?.."
    imgd 901445
    bardi "О, круто!"
    imgd 901454
    student_emily "Только не в ближайшие дни, у меня уже есть планы..."
    student_emily "Слышал, что Арни Уокер устраивает в субботу вечеринку у себя дома?"
    student_emily "Его предки свалили куда-то на выходные."
    student_emily "Кстати, ты там будешь? Или тебя не пригласили?"
    imgd 901445
    bardi "Эээм... Первый раз слышу про вечеринку. А он учится с нами в группе?"
    imgd 901454
    student_emily "Нет, в параллельной."
    student_emily "В общем, я иду на эту вечеринку. Поэтому нашу экскурсию придется отложить до следующих выходных."
    imgd 901445
    bardi "Понял. Окей, договорились."
    # она предупреждающе поднимает руку, указывая на Барди пальчиком
    sound Jump2
    img 901440 vpunch
    student_emily "И никому ни слова, понял?"
    # Барди поднимает руки
#    sound vjuh3
    img 901455
    bardi "Конечно!"
    # в этот момент к ним подлетает зануда-Сара
    # Эмили закатывает глаза и поспешно утыкается в свой телефон
    imgf 901456
    student_sarah "[mcname], Эмили!"
    music Postcard_From_Hell
    bardi_t "Фак! Только не она!"
    # Сара начинает поучительно вещать
    imgd 901457
    w
    sound step_stairs_short
    imgf 901458
    student_sarah "Между прочим, через пять минут начинается занятие по английскому!"
    student_sarah "Вы и так постоянно в числе опаздывающиъ студентов!"
    imgd 901459
    student_sarah "Это сказывается негативно на дисциплине всей нашей группы!"
    student_sarah "Идите быстро в кабинет английского!"
    # Эмили недовольно смотрит на Сару, потом на Барди
    imgd 901460
    w
    imgd 901461
    student_emily "Пошли. А то она не отцепится..."
    imgd 901462
    student_sarah "Да, не отцеплюсь!"
    student_sarah "Вообще-то, можно было бы потрудиться прийти вовремя на единственный обязательный предмет сегодня."
    # Эмили перестает ее слушать и отходит от них, направляясь к лестнице на второй этаж
    sound highheels_short_walk
    imgd 901463
    student_sarah "Неужели это так сложно, я не понимаю?!"
    imgd 901464
    bardi "Кроме английского больше нет обязательных предметов сегодня?"
    imgd 901465
    student_sarah "Нет. Но я надеюсь, что ты записался на какой-либо дополнительный предмет..."
    student_sarah "И не будешь бездельничать оставшуюся часть дня."
    student_sarah "Если ты еще не записался, то можешь прийти..."
    # Барди перебивает ее
    img 901464
    bardi "Все-все! Я понял."
    bardi "Мы на английский опаздываем, помнишь?"
    # Барди разворачивается и идет вслед за Эмили
    # Сара ворчит
    imgf 901466
    sound step_stairs_short
    sound2 highheels_short_walk
    student_sarah "Ох!.. Это все из-за тебя и Эмили! Нашли время для пустых разговоров!.."
    fadeblack 1.0
    # затемнение
    return

label ep03_dialogues2_college_2a:
    bardi_t "Нет времени гулять по колледжу."
    bardi_t "Я опаздываю на Английский!"
    return False

# кабинет инглиша
label ep03_dialogues2_college_3:
    # Эмили, Барди и Сара заходят в кабинет
    # остальные студенты уже за своими партами, в том числе и Гарри
    # Гарри смотрит на Эмили, затем переводит злобный взгляд на Барди
    # и, как обычно, показывает ему кулак
    music Montana
    sound2 highheels_short_walk
    imgfl 910780
    w
    imgf 910779
    sound highheels_short_walk
    w
    imgd 910781
    w
    music Secretions_Vocal
    sound2 Jump2
    img 910782
    student_harry "Ррр!.."
    imgd 910784
    sound2 ma5
    w
    # в это время училка по инглишу, миссис Адамс
    music Montana
    imgf 910783
    teacher_adams "Доброе утро, студенты."
    teacher_adams "Занимайте свои места."
    # Барди и Сара с Эмили идут к своим партам
    imgd 910785
    teacher_adams "Сегодня нам предстоит подготовительное занятие перед написанием эссе."
    teacher_adams "Надеюсь, вы помните тему?"
    # зануда быстро поднимает руку
    sound vjuh3
    imgd 910786
    student_sarah "Я помню, миссис Адамс! Литература 17 века и ее основные тенденции."
    teacher_adams "Спасибо, Сара."
    # Барди уже сидит за партой
    imgf 910787
    bardi_t "Какая-то скучная хрень..."
    bardi_t "Я не собираюсь писать никакое эссе!.."
    # смотрит на миссис Адамс
    imgd 910788
    bardi_t "Хмм... Эмили сказала, что в субботу будет вечеринка у какого-то Уокера..."
    bardi_t "И там будет Эмили..."
    bardi_t "Как бы мне попасть на эту вечеринку?"
    bardi_t "Интересно, а Шон в курсе?"
    # Барди достает телефон и пишет сообщение Шону
    sound swish
    imgf 910789
    w
    return

    # sean_chat5
    sound2 iphone_typing
    bardi "В субботу вечеринка у какого-то Уокера."
    bardi "Ты знаешь этого чувака?"
    sound iphone_text_message2
    sean "Ага. Давай позже. Я на математике."
    # следом от Шона приходит фотка, на которой Кларк орет и тычет пальцем на одного из студентов, которые не в группе Барди, у доски
    # студент стоит, опустив голову, с виноватым видом
    # Барди смотрит на эту фотку
    sound2 iphone_text_message2
    imgd 910790
    bardi_t "Смотрю, миссис Кларк вовсю 'веселится'..."
    bardi_t "Что он сделал? Опоздал на математику?"
    return

label ep03_dialogues2_college_3next1:
    # внезапно раздается голос
#    imgd 910791
#    w
    sound highheels_short_walk
    imgd 910791
    teacher_adams "[mcname], а ты что скажешь?"
    # Барди поднимает голову от телефона - рядом с его партой стоит миссис Адамс и вопросительно смотрит на него
    # Барди тупит и продолжает держать телефон с фоткой Кларк в руках
    music stop
    sound plastinka1b
    img 910792 hpunch
    w
    music Adventures_of_the_Deaf_Dreamer
    img 910793
    bardi "!!!"
    # синеволосый одногруппник отклоняется на своем стуле и заглядывает к нему в телефон
    imgd 910794
    sound laughing_male2
    student_jacob "Ему некогда. Он по ходу собрался дрочить на Кларк."
    # раздаются смешки в классе
    # Барди резко прячет свой телефон
    bardi "Заткнись!"
    sound Jump2
    img 910795 vpunch
    student_jacob "Придурок." # показывает Барди фак и отворачивается
    # училка продолжает стоять над Барди с вопросительным видом
    imgf 910793
    bardi "Вы можете повторить ваш вопрос, миссис Адамс?"
    imgd 910796
    teacher_adams "Я спрашивала, нашел ли ты себе пару?"
    imgd 910793
    bardi "???"
    menu:
        "Я над этим работаю.":
            imgd 910797
            bardi "Я над этим работаю..."
            # Адамс удивленно смотрит на него
            # синеволосый снова встревает
            imgd 910798
            student_jacob "Рассматривая сиськи математички? Ха-ха-ха!"
            sound laughing_male2
            sound2 snd_woman_laugh4a
            # в классе снова хихикают
            # все студенты смотрят на Барди
            imgd 910799
            bardi_t "Какого черта все уставились на меня?!"
            pass
        "Вы хотели бы предложить свою кандидатуру?":
            imgd 910797
            bardi "Вы хотели бы предложить свою кандидатуру, миссис Адамс?"
            # Адамс удивленно смотрит на него
            # синеволосый встревает
            imgd 910798
            student_jacob "Стремный подкат, [mcsurname]. Ты облажался, придурок."
            img 910800
            teacher_adams "Джейкоб!"
            student_jacob "Все-все. Молчу." # отворачивается
            imgd 910801
            w
            pass
    music Montana
    imgf 910802
    teacher_adams "Я не знаю, правильно ли ты меня понял, [mcname]..."
    # Адамс слегка улыбается
    imgd 910803
    teacher_adams "Я имела ввиду, нашел ли ты себе в пару студента, с которым будешь работать над эссе?"
    bardi_t "Оу, фак! Вот я кретин!"
    bardi "Я да. То есть, нет... Не нашел еще."
    imgd 910802
    teacher_adams "Тебе нужно будет определиться с этим сегодня, [mcname]. И сообщить мне."
    imgd 910803
    bardi "Окей. Я понял."
    # она улыбается ему и разворачивается, чтобы идти в сторону доски
    # Барди опускает взгляд на ее попу и ноги, обсматривает (observing -?)
    sound highheels_short_walk
    imgf 910804
    w
    imgd 910805
    bardi_t "Зачетная попка у этой Адамс."
    $ camera_enabled = False
    if mlsBardiSeanDay3Whore2 > 0:
        # перед глазами Барди пара кадров со сцены с Бекки, где она стоит в одних трусиках и он представляет Адамс вместо Бекки
        img white_screen
        with diss
        pause 1.0
        music Stylish_Hip_Hop_Rock
        img 900634
        show screen dream()
        with Dissolve(1.0)
        w
        img 900633
        show screen dream()
        with fade
        teacher_adams "И еще я просто обожаю, когда член заполняет всю мою киску."
        teacher_adams "Хочу скорее трахнуть тебя, студент!.."
    $ camera_enabled = True
    # Барди смотрит на свою ширинку - у него встал
    music stop
    sound plastinka1b
    img 910806 hpunch
    bardi_t "Вот черт! Только не сейчас!.."
    # прикрывает стояк руками, оглядывается
    music Secretions_Vocal
    sound2 Jump2
    img 910807 vpunch
    w
    # на его попытки скрыть стояк смотрит девочка-фрик Хлоя, потом закатывает глаза и отворачивается
    imgd 910808
    w
    imgd 910809
    w
    imgd 910810
    student_chloe "..."
    imgd 910811
    w
    # Барди смотрит в другую сторону - на него никто не обращает внимания, все слушают училку
    imgd 910812
    w
    imgd 910807
    bardi_t "Нужно подумать о чем-то неприятном! Срочно!"
    label ep03_dialogues2_college_3_loop:
    music Adventures_of_the_Deaf_Dreamer_short
    imgd 910807
    bardi_t "!!!"
    $ camera_enabled = False
    menu:
        "Ричардсон.":
            $ ep03_dialogues2_college_3_menu1 = True
            imgd 910813
            bardi_t "О, точно! Ричардсон! Монстр в юбке!"
            # кадры директрисы из v1, где она говорит ему
            img white_screen
            with diss
            pause 1.0
            img 900404
            show screen dream()
            with Dissolve(1.0)
            w
            img 900405
            show screen dream()
            with diss
            principal_richardson "Чтобы никаких нарушений дисциплины в моем колледже, [mcsurname]!"
            principal_richardson "Я этого не терплю! Ясно тебе?"
            # кадры меняются на директрису в латексном черном костюме и она ему подмигивает
            img white_screen
            with diss
            pause 1.0
            music The_Heat
            img 900422
            show screen dream()
            with diss
            w
            img 900423
            show screen dream()
            with diss
            bardi_t "О, черт! Только хуже стало!"
            jump ep03_dialogues2_college_3_loop
        "Кларк.":
            $ ep03_dialogues2_college_3_menu2 = True
            imgd 910813
            bardi_t "О, это должно сработать!"
            # кадры с урока математики, где Кларк его отчитывает за опоздание
            img white_screen
            with diss
            pause 1.0
            img 900825
            show screen dream()
            with Dissolve(1.0)
            w
            img 900826
            show screen dream()
            with diss
            teacher_clark "Студент, ты бы еще к концу занятия пришел и стал извиняться!"
            teacher_clark "Ты что, не видел расписания своей группы?!"
            teacher_clark "Имя!"
            # кадры меняются на грудь Кларк крупным планом, видно торчащие соски под блузкой
            img white_screen
            with diss
            pause 1.0
            music Stylish_Hip_Hop_Rock
            img 900855
            show screen dream()
            with diss
            w
            img 900856
            show screen dream()
            with diss
            bardi_t "Фаак!"
            jump ep03_dialogues2_college_3_loop
        "Оливия.":
            $ ep03_dialogues2_college_3_menu3 = True
            imgd 910813
            bardi_t "Да! Злобная Оливия - это то, что надо!"
            # кадры, на которых Оливия наезжает на него в v1, вечером
            img white_screen
            with diss
            pause 1.0
            img 900134
            show screen dream()
            with Dissolve(1.0)
            w
            img 900135
            show screen dream()
            with diss
            olivia "О, неудачник вернулся со своей шараги. Да еще и с синяком на лице."
            # кадры меняются на Оливию в душе
            img white_screen
            with diss
            pause 1.0
            music Stylish_Hip_Hop_Rock
            img 900157
            show screen dream()
            with diss
            w
            img 900158
            show screen dream()
            with diss
            w
            img 900159
            show screen dream()
            with diss
            w
            img 900160
            show screen dream()
            with diss
            bardi_t "Твою же мать!!!"
            jump ep03_dialogues2_college_3_loop
        "Гарри." if ep03_dialogues2_college_3_menu1 == True and ep03_dialogues2_college_3_menu2 == True and ep03_dialogues2_college_3_menu3 == True:
            # кадры с v1 после удара Гарри кулаком после инглиша и тот смотрит на лежащего на полу Барди
            img white_screen
            with diss
            pause 1.0
            music Fly_With_Me_short
            img 910105
            show screen dream()
            with diss
            w
            sound snd_punch_face2
            sound2 snd_kick_fred1
            img 910106
            show screen dream()
            with hpunch
            w
            sound snd_bodyfall
            img 910107
            show screen dream()
            with vpunch
            student_harry "Добро пожаловать, лузер."
            # кадр исчезает, Барди оглядывается на Гарри
            # тот как обычно показывает ему кулак
            $ camera_enabled = True
            imgf 910078
            student_harry "Ррр!.."
            pass
    $ camera_enabled = True
    # Барди убирает руки с ширинки
    imgd 910807
    w
    sound vjuh3
    imgd 910814
    bardi_t "Уф... Вроде помогло..."
    # Адамс тем временем заканчивает занятие
    music Adventures_of_the_Deaf_Dreamer
    imgd 910081
    teacher_adams "На этом наше сегодняшнее занятие подходит к концу."
    teacher_adams "Прошу всех до конца дня сообщить мне пару, с которой вы будете работать над эссе."
    teacher_adams "Спасибо. Все свободны."
    # студенты встают и идут к выходу, Адамс садится за свой стол
    # Барди как всегда копается, к его парте подходит Роуз
    imgf 910815
    sound highheels_short_walk
    sound2 step_stairs
    w
    imgd 910816
    student_rose "[mcname], привет."
    music Montana
    imgd 910817
    bardi "Привет, Роуз. Как дела?"
    # она очень смущается, опускает глаза
    imgd 910818
    student_rose "Все хорошо. Спасибо, что спросил."
    imgd 910819
    student_rose "Я тут подумала..."
    student_rose "Если ты еще не знаешь, с кем будешь писать это эссе по английскому..."
    imgd 910820
    student_rose "Ты мог бы... Мы могли бы... Сделать это вместе..."
    # если Барди не толкал Гарри и в первый день разговаривал с Роуз
    if mlsBardiFirstDayCollege1 > 0:
        student_rose "Я ведь говорила тебе, что можешь обращаться ко мне, если нужна помощь по учебе..."
    # если Барди прятался от Гарри в раздевалке для девочек
    if mlsBardiDay3College6 > 0:
        #
        $ notif(_("[mcname] прятался от Гарри в женской раздевалке."))
        #
        student_rose "Тем более, за тобой должок. Ты ведь помнишь?"
    imgd 910819
    student_rose "Что скажешь?"
    imgd 910821
    bardi_t "Хмм... Это же отличный способ не заниматься гребаным эссе!"
    bardi_t "Милашка Роуз все сделает за меня!"
    imgd 910822
    bardi "Конечно, Роуз. Я только за..."
    # Роуз обрадованно смотрит на него
    student_rose "Правда?!"
    bardi "Ага. Сделаем это вместе..."
    # она радостно улыбается
    music Shining_Through
    imgd 910823
    student_rose "Как здорово!"
    student_rose "Тогда я сообщу миссис Адамс, что мы работаем вместе!"
    imgd 910824
    bardi "Окей."
    imgd 910825
    student_rose "И нам нужно будет договориться с тобой, когда мы приступим к работе."
    student_rose "Тебе удобно будет заниматься у меня дома?"
    student_rose "Или будет лучше, если я к тебе буду приходить?"
    menu:
        "Эээм... Давай, я к тебе приду.":
            pass
    imgd 910826
    bardi "Эээм... Давай, я к тебе приду."
    imgd 910827
    student_rose "Хорошо. Тогда после выходных приступим?"
    bardi "Да, без проблем."
    bardi "Ну, я пошел. До встречи, Роуз."
    imgd 910828
    student_rose "Пока, [mcname]."
    # Барди идет к выходу мимо училки, а Роуз подходит к ней
    imgf 910829
    sound highheels_short_walk
    sound2 step_stairs
    bardi "До свидания, миссис Адамс."
    teacher_adams "До встречи, [mcname]."
    $ mlsBardiDay4College2 = day # Роуз предложила Барди работать над эссе вместе
    fadeblack 1.0
    return

# мысли Барди после инглиша
label ep03_dialogues2_college_3a:
    ## не рендерить!!
    bardi_t "Отлично!"
    bardi_t "Проблема с эссе решилась сама собой."
    bardi_t "По ходу, на сегодня все... Можно валить отсюда!"
    # звонок на телефон - звонит Софи и говорит о встрече с Райтом (jump ep03_dialogues1_family_morning_3)
    return

# после разговора с Софи Барди видит, что по коридору в его сторону идет миссис Морис
label ep03_dialogues2_college_4:
    music Montana
    sound2 step_stairs_short
    # если до этого не разговаривал с Моррис
    if mlsBardiFirstDayCollege1 == 0 and mlsBardiDay3College5 == 0:
        imgfl 901489
        bardi_t "Ух ты! Какая красотка!.."
        # она идет в его сторону и равняется с ним
        sound highheels_short_walk
        imgf 901490
        bardi "Здрасьте."
        # Барди пялится на нее и в это время нечаянно роняет свой телефон (либо надевает рбкзак так коряво, что роняет его на пол)
        imgd 901491
        teacher_morris "Здравствуй."
        # он наклоняется, чтобы поднять телефон (рюкзак) с пола и обсматривает ноги Морис
        imgd 901492
        w

        sound vjuh3
        img 901493 hpunch
        w
        sound2 down7
        imgd 901494
        w
        imgf 901495
        w
        music The_Heat

        # video
        # v_Observe_Teacher11_3_25
        img black_screen
        with diss
        pause 1.0
        scene black
        image videov_Observe_Teacher11_3_25 = Movie(play="video/v_Observe_Teacher11_3_25.mkv", fps=25, loop=False, image="/images/Slides/img_901496.jpg")
        show videov_Observe_Teacher11_3_25
        $ renpy.pause(0.5, hard=True)
        pause 6.0
        img 901496
        show screen image_shake("/images/Slides/img_901496.jpg")
        w
        bardi "!!!"
        teacher_morris "Ты новый студент? Я тебя здесь раньше не видела."
        imgd 901497
        bardi "Ага." # пялится на нее, выпрямляется, подняв с пола телефон (рюкзак)
        music Montana
        imgf 901498
        w
        imgd 910177
        bardi "Я [mcname]."
        imgd 910178
        teacher_morris "Меня зовут миссис Морис."
        # меню диалога с Морис (использовать имеющиеся арты)
        label ep03_dialogues2_college_4_loop1:
        imgd 910176
        bardi "..."
        menu:
            "Спросить, работает ли она тут.":
                imgd 910176
                bardi "А вы здесь работаете, миссис Морис?"
                imgd 910175
                teacher_morris "Да, [mcname]."
                teacher_morris "Я совсем недавно устроилась в этот колледж."
                teacher_morris "Работаю всего пару недель."
                $ ep03_dialogues2_college_4_menu1 = True
                jump ep03_dialogues2_college_4_loop1
            "Спросить, какой предмет она ведет.":
                imgd 910176
                bardi "А какой предмет вы преподаете?"
                imgd 910180
                teacher_morris "Живопись."
                $ ep03_dialogues2_college_4_menu2 = True
                jump ep03_dialogues2_college_4_loop1
            "Спросить, есть ли свободные места на ее предмет." if ep03_dialogues2_college_4_menu1 == True and ep03_dialogues2_college_4_menu2 == True:
                imgd 910176
                bardi "О, я как раз сомневался, какой дополнительный предмет мне выбрать."
                bardi "А живописью я... Кхм... Очень интересуюсь, да!"
                bardi "У вас есть свободные места?"
                imgd 910179
                teacher_morris "Да, [mcname]."
                teacher_morris "Ты можешь прямо сейчас пойти со мной на занятие..."
                teacher_morris "А я позже сама запишу тебя у секретаря."
                teacher_morris "Пойдем? Уверена, тебе понравится."
                imgd 910176
                w
                imgf 901499
                bardi_t "Я не сомневаюсь..." # пялится на нее
                bardi_t "Ей бы не живопись преподавать, а в порно сниматься..."
                bardi_t "Мне нужно обязательно попасть к ней на занятия."
                bardi_t "Живопись - это скучно. Но мне пофиг. Буду старательно изображать интерес к ее предмету."
                pass
        pass
    # если уже знаком с Морис
    else:
#    if mlsBardiFirstDayCollege1 > 0 or mlsBardiDay3College5 > 0:
        # она идет в его сторону и равняется с ним
        imgfl 901489
        w
        sound highheels_short_walk
        imgf 910175
        teacher_morris "Добрый день, [mcname]."
        imgd 910176
        bardi "Здрасьте, миссис Морис."
        imgd 910179
        teacher_morris "Как у тебя дела? Я помню, ты говорил, что хотел бы заняться живописью..."
        teacher_morris "Еще не передумал? У меня как раз сейчас начнется занятие."
        # если уже записался
        if mlsBardiDay3College1 > 0:
            imgd 910181
            bardi "Да, все в силе. Я записался на живопись, миссис Морис."
            imgd 910182
            teacher_morris "Отлично! Тогда пойдем со мной."
        # если не записался
        else:
            imgd 910181
            bardi "Я как раз собирался это сделать."
            imgd 910182
            teacher_morris "Ты можешь прямо сейчас пойти со мной на занятие..."
            teacher_morris "А я позже сама запишу тебя у секретаря."
            teacher_morris "Пойдем?"
            pass
    imgd 910176
    bardi "Что, прямо сейчас?"
    # она улыбается ему
    imgd 910175
    teacher_morris "Да, [mcname]. Начало через пять минут."
    # она проходит по коридору, он смотрит на ее попу и идет следом
    imgd 910176
    bardi "Окей."
    imgf 901500
    sound highheels_short_walk
    w
    imgd 901501
    w
    # затемнение, шаги
    return

# кабинет исскуств
label ep03_dialogues2_college_5:
    # в кабинете стоит несколько мольбертов, среди которых одни не занят (для Барди)
    # в кабинете присутствуют другие студенты, человека 5-6, они стоят у своих мольбертов
    # из группы Барди девочка-фрик и девочка с каре в джинсах, остальные с других групп
    # Морис, следом за ней Барди, заходят в кабинет
    fadeblack 1.0
    music Postcard_From_Hell
    imgfl 901502
    teacher_morris "Добрый день, студенты."
    imgf 901503
    teacher_morris "У нас новенький. Знакомьтесь. Это [mcname]."
    teacher_morris "[mcname] интересуется живописью и записался в нашу группу."
    imgd 901504
    bardi "Да, интересуюсь... Очень..."
    # фрик бросает на него удивленный взгляд, как и вторая одногруппница в джинсах
    bardi "Всем привет."
    imgd 901505
    teacher_morris "[mcname], расскажи нам, ты раньше посещал занятия по живописи?"
    teacher_morris "Может быть, в своем бывшем колледже или школе?"
    menu:
        "Не занимался.": # кролик
            imgd 901506
            bardi "Да... То есть, нет..."
            bardi "Я собирался, но никак не получалось. По разным причинам..."
            imgd 901505
            teacher_morris "Ну ничего страшного. Главное, что у тебя есть желание."
            teacher_morris "С остальным я тебе помогу."
            imgd 901506
            bardi "Отлично. Спасибо, миссис Морис."
            pass
        "Солгать.": # крыса
            $ mlsBardiDay4College3 = day # Барди солгал Морис, что занимался раньше живописью
            music Step_By_Step
            imgd 901506
            bardi "Конечно, занимался."
            bardi "В колледже."
            bardi "Меня вообще очень интересует и влечет все, что связано с живописью..."
            imgd 901505
            teacher_morris "Отлично. Я очень рада, что ты теперь в нашей группе."
            pass
    # Морис указывает рукой на свободный мольберт
    imgd 901507
    teacher_morris "[mcname], проходи за тот мольберт."
    # Барди встает у мольберта, смотрит на чистый холст, на кисточки и краски на мольберте
    sound step_stairs_short
    imgf 901509
    w
    sound step_stairs_short
    imgd 901508
    w
    imgd 901510
    bardi_t "???"
    imgd 901511
    bardi_t "Сколько всякой хрени... Как этим вообще пользоваться?"
    # Морис тем временем берет в руки вазу с цветами
    imgf 901512
    teacher_morris "Итак, студенты."
    teacher_morris "Сегодня будет совсем простое занятие."
    teacher_morris "Вам сегодня нужно будет написать натюрморт."
    imgd 901513
    teacher_morris "Если не уложитесь во время занятия, то работу можно будет дописать дома..."
    teacher_morris "И сдать мне по готовности после выходных."
    # она хлопает в ладошки
    imgd 901514
    teacher_morris "Ну что, ребята? Приступаем к работе!"
    sound snd_slap1
    imgd 901515
    w
    # все студенты, кроме Барди, берут в руки кисти и начинают творить, усердно глядя в свои холсты
    # Барди не торопится хвататься за кисть, смотрит на остальных
    fadeblack 1.0
    music Montana
    imgf 901547
    w
    imgd 901516
    w
    imgd 901517
    bardi_t "Черт..."
    bardi_t "Так, ладно..."
    bardi_t "Нужно взять кисть, макнуть ее в банку с краской и нарисовать цветы."
    bardi_t "Что тут сложного то?"
    bardi_t "Подумаешь, цветочки рисовать... Это тебе не математика со злющей Кларк."
    # Морис подходит к одному из студентов и смотрит на его холст
    sound highheels_short_walk
    imgf 901518
    teacher_morris "У тебя хорошо получается. Молодец!"
    imgd 901519
    w
    # Барди берет кисть и окунает ее в черную краску
    # потом к фрику Хлое
    sound highheels_short_walk
    imgf 901520
    teacher_morris "О, хлоя, я уже вижу, что это будет прекрасная работа!"
    teacher_morris "Ты, как всегда, меня радуешь своими успехами!"
    imgd 901521
    student_chloe "Спасибо, миссис Морис." # с улыбкой
    imgd 901522
    bardi_t "Ух ты! Хлоя оказывается разговаривать умеет. И даже улыбаться."
    # Морис идет к следующему студенту
    sound highheels_short_walk
    imgf 901523
    teacher_morris "Ну-ка. А здесь у нас что?.."
    # Барди начинает вести линию черной краской по холсту, пытаясь нарисовать вазу
    imgd 901524
    bardi_t "..."
    imgd 901525
    w
    # Морис тем временем наклоняется, оттопырив попу, и внимательно рассматривает холст того студента, к которому подошла
    imgf 901526
    teacher_morris "Давай я тебе немного помогу. Возьми кисть вот так и выводи контур..."
    # Барди, продолжая возюкать кистью по холсту, не смотря на него, пялится на Морис
    # холст Барди не показываем

    imgd 901527
    bardi_t "Какая клевая поза, миссис Морис..."
    bardi_t "Интересно, а будут занятия по написанию картин с натуры?.."
    # Барди продолжает пялится на Морис и представляет ее в нижнем белье (резкая смена кадра - Морис стоит также возле студента, но в белье, а не в юбке и кофте)
    # observing либо кадры крупным планом на ее попу, грудь, лицо
    music stop
    $ camera_icon_enabled = False
    img white_screen
    with diss
    pause 0.5
    music The_Heat
    pause 0.5
    img 901528
    show screen dream()
    with Dissolve(1.0)
    show screen image_shake("/images/Slides/img_901528.jpg")
    bardi_t "Это было бы круто!.."

#    img 901529
#    show screen dream()
#    with fade
#    show screen image_shake("/images/Slides/img_901529.jpg")

    # video
    # v_Observe_Teacher11_4_25
    img black_screen
    with diss
    pause 1.0
    scene black
    image videov_Observe_Teacher11_4_25 = Movie(play="video/v_Observe_Teacher11_4_25.mkv", fps=25, loop=False, image="/images/Slides/v_Observe_Teacher11_4_end.jpg")
    show videov_Observe_Teacher11_4_25
    $ renpy.pause(0.5, hard=True)
    pause 4.5
    img v_Observe_Teacher11_4_end
    show screen dream()
    with diss
    show screen image_shake("/images/Slides/v_Observe_Teacher11_4_end.jpg")
    w
    bardi_t "Я не отказалася бы..."


    img 901530
    show screen dream()
    with Dissolve(1.0)
#    show screen image_shake("/images/Slides/img_901530.jpg")
    w
    bardi_t "Ееее!"


    # внезапно кадр меняется - Морис в своей обычной одежде стоит перед Барди у его мольберта, напротив Барди (мольберт между ними, она не видит его творение)
    $ camera_icon_enabled = True
    music stop
    img white_screen
    with diss
    pause 0.5
    music Montana
    pause 0.5
    img 901531
    with Dissolve(0.5)
    teacher_morris "[mcname], как у тебя дела с натюрмортом?"
    imgd 901532
    bardi "Эээм..."
    # кадр на холст Барди - там жуткая мазня черной краской
    menu:
        "Не показывать свою работу миссис Морис.":
            music Step_By_Step
            img 901532
            bardi "С картиной полный порядок, миссис Морис..."
            # она пытается заглянуть и посмотреть на его холст, но Барди закрывает его руками
            bardi "Но я предпочитаю, чтобы мою работу никто не видел, пока..."
            bardi "Эээ... Пока я ее не доделаю. Вот."
            # Морис удивленно улыбается
            imgd 901533
            teacher_morris "Вот как?"
            imgd 901532
            bardi "Ага."
            imgd 901531
            teacher_morris "Ты уверен, что тебе не нужна помощь, [mcname]?"
            imgd 901532
            bardi "Уверен."
            bardi "Я покажу вам свою работу, когда завершу ее... На следующем занятии..."
            # она улыбается и обходит мольберт, чтобы все-таки взглянуть на работу Барди
            sound vjuh3
            img 901534 hpunch
            teacher_morris "Я заинтригована, [mcname]. Все-таки, я хочу взглянуть на твои наброски..."
            bardi_t "Фак!"
            # встает с ним рядом, он руками прикрывает мазню на холсте
            # она берет его за руку и пытается отвести ее в сторону от рисунка
            # при этом она стоит совсем близко
            music Story_of_One_Success_short
            sound2 Jump1
            img 911015 vpunch
            bardi "Миссис Морис, давайте не сейчас!.."
            teacher_morris "Сейчас, [mcname]."
            imgd 911016
            w
            # еще одна попытка Морис отвести его руку, она случайно прижимается к нему грудью
            imgd 911017
            bardi "Но!.."
            teacher_morris "Никаких 'но'!.."
            sound vjuh3
            img 911018 hpunch
            w
            # она предпринимает еще одну попытку и не специально прижимается к нему еще плотнее
            # Барди отвлекается на то, как она к нему прижимается
            imgd 911019
            bardi_t "Ох, черт!"
            bardi_t "Если она так будет жаться ко мне, стояк мне обеспечен!.."
            sound Jump1
            img 911020 vpunch
            w
            # из-за этого ослабевает его сопротивление и она пользуется моментом, отводит его руки от картины
            music stop
            sound plastinka1b
            img 901534 hpunch
            teacher_morris "Ох!"
            bardi_t "Твою мать!.."
            pass
        "Показать свою работу.":
            # Барди показывает ей рукой на свою картину
            img 901532
            bardi "Дела в порядке... Вот, сами посмотрите, миссис Морис."
            # Морис заглядывает через мольберт и смотрит на холст Барди
            sound highheels_short_walk
            imgf 901535
            teacher_morris "?!"
            imgd 901536
            w
            # она непонимающе смотрит на Барди, потом обходит мольберт и встает рядом с ним, глядя на его мазню
            pass
    # она удивленно смотрит на холст
    music Step_By_Step
    imgd 901537
    teacher_morris "Ох... Я даже не знаю, что сказать, [mcname]..."
    teacher_morris "Это... Это..."
    # если Барди солгал, что ранее занимался живописью
    if mlsBardiDay4College3 > 0:
        imgd 901538
        bardi "Абстракция, миссис Морис."
        bardi "У меня оригинальный стиль. Я заложил в эту работу..."
        bardi_t "Что ты несешь, придурок?! Просто заткнись!.."
        # Морис поправляет очки и снова внимательно смотрит на мазню на холсте
        imgd 901537
        teacher_morris "Хмм... Что ж, [mcname], это очень... Оригинально..."
        teacher_morris "Но я думаю, что тебе не помешало бы взять несколько дополнительных занятий по живописи..."
        #
        $ notif(_("Миссис Морис поняла, что [mcname] солгал ей, что ранее занимался живописью."))
        #
        imgd 901539
        teacher_morris "Твой оригинальный стиль будет таковым, если ты сначала научишься писать картины." # улыбается
        imgd 901538
        bardi "Извините, миссис Морис... Просто я..."
        bardi "Я подумал, что вы не запишите меня к себе на занятия, если я скажу, что раньше никогда не рисовал."
        bardi "А я так давно хотел заняться живописью..."
    # если не лгал
    else:
        imgd 901538
        bardi "Это провал."
        bardi "По ходу, мне не светит стать художником... Так жаль..."
    # она с сочувствием
    music Montana
    imgd 901539
    teacher_morris "Ох, [mcname], не расстраивайся."
    # она кладет руку ему на плечо
    imgd 901540
    teacher_morris "Главное, что тебе это интересно и ты хочешь научиться."
    teacher_morris "Я тебе помогу и у тебя обязательно все получится! Вот увидишь!"
    imgd 901541
    bardi "Вы так считаете, миссис Морис?.."
    # она улыбается ему
    imgd 901540
    teacher_morris "Ну, конечно!"
    teacher_morris "Я проведу для тебя несколько дополнительных уроков после занятий в колледже."
    teacher_morris "И в итоге ты сможешь писать прекрасные картины!"
    teacher_morris "Готов работать над этим?"
    # пялится на ее грудь
    imgf 901542
    w
    imgd 901541
    bardi "Да, конечно. Я готов."
    bardi "Я очень хочу научиться!.."
    # она улыбается ему
    imgd 901542
    teacher_morris "Хорошо. Договорились."
    # Морис отходит от Барди и обращается к студентам
    fadeblack 1.0
    music Postcard_From_Hell
    sound2 highheels_short_walk
    imgfl 901543
    teacher_morris "Сегодняшнее занятие подошло к концу."
    teacher_morris "Сдаем свои работы. Кто не успел - принесете мне их после выходных."
    # студенты идут на выход
    # Барди подходит к Морис
    imgf 901544
    sound highheels_short_walk
    sound2 step_stairs
    w
    imgd 901545
    sound step_stairs_short
    bardi "Спасибо за занятие, миссис Морис. Мне очень понравилось."
    imgd 901546
    teacher_morris "Я рада, [mcname]."
    # если ранее не записывался на живопись у секретаря
    if mlsBardiDay3College1 == 0:
        img 901546
        teacher_morris "Значит, я могу записать тебя на свой предмет у секретаря?"
        imgd 901545
        bardi "Да, конечно, миссис Морис."
        imgd 901546
        teacher_morris "Хорошо, [mcname]."
    img 901546
    teacher_morris "На днях я посмотрю свое расписание и скажу тебе, когда мы сможем провести дополнительные занятия для тебя."
    imgd 901545
    bardi "Окей. Хорошего дня, миссис Морис."
    # она улыбается
    imgd 901546
    teacher_morris "Спасибо. И тебе хорошего дня, [mcname]."
    # Барди выходит из кабинета искусств
    fadeblack 1.0
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgf 901548
    bardi_t "Чертовы цветочки не так просты, как это казалось..."
    bardi_t "Но я был убедителен. Морис поверила, что меня интересует живопись..."
    bardi_t "Круто-круто. Дополнительные занятия с Морис - то, что мне и было нужно!.."
    return

# после разговора с Морис или после урока живописи
# Барди стоит в холле
label ep03_dialogues2_college_5a:
    # внезапно к Барди подлетает Шон и хлопает его по плечу
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgd 901481
    w
    sound Jump1
    img 901482 hpunch
    w
    imgd 901483
    sean "Чувак, привет! Готов к субботней вечеринке у Арни?"
    imgd 901484
    bardi "А ты идешь?"
    imgd 901485
    sean "Конечно! Ты еще спрашиваешь?!"
    sean "МЫ идем, бро! МЫ!"
    sean "Море бухла и пьяных девчонок! Ееее! Это будет круто, бро!"
    sean "Встречаемся в субботу у Арни!"
    # Шон снова хллпает Барди по плечу и уже уходя
    imgd 901486
    sean "Все, мне пора! У меня дела. Давай, чувак, пока!"
    sound snd_runaway
    imgf 901487
    bardi "Пока."
    # Шон убегает
    imgd 901488
    bardi_t "Круто! Отличный сегодня день!"
    bardi_t "Мне удалось решить намечающуюся проблему с написанием эссе..."
    bardi_t "Договориться о дополнительных занятиях по живописи..."
    bardi_t "Получить от Эмили согласие на встречу и получить приглашение на вечеринку."
    bardi_t "Осталось еще одно дело - встретиться с мистером Райтом и договориться о подработке..."
    return

# при клике на библиотеку
label ep03_dialogues2_college_6:
    # заходит в библиотеку, библиотекарша стоит на рабочем месте
    sound snd_door_open1
    fadeblack 1.5
    music Postcard_From_Hell
    sound2 step_stairs_short
    imgfl 901467
    w
    imgf 900888
    bardi "Здрасьте, миссис Милсон!"
    # она ему строго
    imgd 900887
    librarian_wilson "Уилсон!"
    librarian_wilson "И говори тише, студент! Тут библиотека!"
    # Барди оглядывается - в библиотеке сидит ботан Лео и зануда Сара, читают
    # Синтии нет
    # зануда Сара замечает Барди
    sound step_stairs_short
    imgf 901468
    w
    imgd 901469
    w
    imgd 901470
    student_sarah "[mcname], ты решил присоединиться к нашему клубу отличников?!"
    student_sarah "Это просто замечательно!.."
    imgd 901471
    bardi_t "Оу, фак! Надо бежать отсюда!"
    bardi "Нет-нет. Может, позже."
    # Барди выходит из библиотеки
    sound step_stairs_short
    imgf 900923
    w
    sound snd_door_open1
    fadeblack 1.5
    music Step_By_Step
    sound2 step_stairs_short
    imgf 901472
    bardi_t "Синтии сегодня нет в библиотеке. Я был уверен, что она тут..."
    # если Синтия утром застала Барди в душе
    if mlsBardiDay4FamilyMorning1 > 0:
        img 901472
        bardi_t "Надеюсь, Синтия не заметила ничего такого утром..."
        bardi_t "Она такая милая, когда смущается."
    return

# при клике на строку контакта "cynthia"
label ep03_dialogues2_college_6a:
    # cynthia_chat3
    menu:
        "Написать Синтии.":
            bardi "Привет, Синтия! Как дела?"
            bardi "Ты в колледже?"
            cynthia "Привет, [mcname]! Уже нет :)"
            cynthia "Мы с Николь договорились встретиться и погулять после колледжа."
            cynthia "Я с ней сейчас."
            bardi "Окей. Хорошей прогулки. Если вечером не увидимся, потом поболтаем :)"
            cynthia "Окей :)"
            return
        "Может, позже.":
            bardi_t "Позже ей напишу."
            return
    return

# при клике на спортзал
label ep03_dialogues2_college_7:
    # Барди открывает дверь и внезапно в дверном проеме возникает тренер Брукс
    sound snd_door_open1
    fadeblack 1.5
    music Shining_Through
    music2 school-corridor-1
    imgf 901473
    w
    sound vjuh3
    img 901474 hpunch
    bardi "Эээ... Здрасьте, тренер Брукс..."
    imgd 901475
    trainer_brooks "Чего тебе здесь нужно, [mcsurname]?!"
    trainer_brooks "У твоей группы сегодня нет тренировки!"
    imgd 901474
    bardi "Да, видимо, я ошибся..."
    imgd 901475
    trainer_brooks "Следи за своим расписанием внимательнее!"
    sound Jump1
    img 900874 vpunch
    trainer_brooks "И в джинсах сюда вход запрещен!"
    imgf 901474
    bardi "Понял. В следующий раз обязательно сниму их."
    imgd 901476
    trainer_brooks "Все, хватит! Свободен!"
    # она закрывает перед ним дверь
    music2 stop
    fadeblack
    sound step_stairs_short
    pause 1.5
    music Step_By_Step
    imgf 900884
    bardi_t "Отличные сиськи, тренер Брукс!.."
    return

# при клике на кабинет математики
label ep03_dialogues2_college_8:
    # Кларк стоит у доски, поворачивается в сторону двери
    sound snd_door_open1
    fadeblack 1.5
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgfl 901477
    w
    sound highheels_short_walk
    imgf 900825
    bardi "Здрасьте, миссис Кларк..."
    # Кларк строго смотрит на него
    imgd 900826
    teacher_clark "Закрой дверь и не мешай вести занятие, [mcsurname]!.."
    teacher_clark "Сейчас же!"
    # Барди закрывает дверь
    fadeblack
    sound step_stairs_short
    pause 1.5
    music Step_By_Step
    imgf 901478
    bardi_t "Кларк, как всегда, не в духе. Она когда-нибудь улыбается?"
    return

# при клике на дверь приемной директора колледжа, либо на какие-то другие локации
label ep03_dialogues2_college_9:
    ## не рендерить!!
    bardi_t "Сегодня мне там нечего делать."
    return False

# при клике на выход из колледжа
label ep03_dialogues2_college_10:
    music Step_By_Step
    imgfl 901479
    bardi_t "Ну все, пора валить отсюда."
    fadeblack
    sound step_stairs_short
    pause 1.5
    music Shining_Through
    imgf 901480
    sound2 step_stairs_short
    w
    return

######################### вечер следующего дня, после визита к тете Дейзи (Day5)

# вечеринка у одного из студентов Арни Уокер (classmate4 - Arnie)
# локация - взять одни из домов учителей
# присутствуют все студенты из колледжа, кроме Роуз и Синтии

# после того, как вышел от тети Дейзи вечером
# звонок на телефон от Шона
label ep03_dialogues2_college_11:
    music Shining_Through
    #sean_chat6
    imgfl 901549
    sean "Эй, бро! Привет!"
    sean "Ты где? Давай скорее на вечеринку! Тут уже все напились!"
    bardi "Привет, Шон. Ага, уже иду."
    sean "Эй, чувак, не забудь презервативы!"
    bardi "Ха-ха! Окей."
    # Барди кладет трубку
    imgf 901550
    bardi_t "Презервативы... Черт!"
    # оглядывается на дом тети
    imgd 901551
    bardi_t "Нет-нет. Это плохая идея."
    bardi_t "Я же не буду спрашивать у Дейзи презервативы..."
    bardi_t "По хрену. Пойду так."
    # квест-лог "Пойти на студенческую вечеринку."
    return

# новая локация на карте - дом Арни

#music Upbeat_Summer
#music She_Is
#music Kimono

# при клике на локацию
# Барди стоит перед домом Арни, из дома слышна музыка и смех
label ep03_dialogues2_college_12:
    fadeblack 1.0
    music Shining_Through
    sound2 step_stairs_short
    imgfl 901552
    bardi_t "О, по ходу я во время..."
    bardi_t "Самое время немного расслабиться."
    # Барди подходит к входной двери и тянет руку, чтобы постучаться или позвонить в дверной звонок
    # в этот момент из двери вываливается синеволосый одногруппник и его выворачивает недалеко от ног Барди, немного в сторону (сам процесс не показываем, слышно звук)
    sound step_stairs_short
    imgf 901553
    w
    music stop
    sound plastinka1b
    img 901554 hpunch
    w
    imgd 901555
    sound gagging_2
    bardi "О, фак!"
    bardi "Ты что делаешь, кретин?!"
    # синеволосый пьяно смотрит на Барди и вытивает рот
    music Adventures_of_the_Deaf_Dreamer
    imgd 901556
    student_jacob "..."
    bardi "Придурок!"
    # из дома выходит пьяный classmate4, говорит синеволосому
    sound step_stairs_short
    imgf 901557
    student_arnie "Эй, Джейкоб, ты в порядке?"
    imgd 901558
    student_jacob "Угу. Мне нужно еще выпить."
    sound Jump1
    img 901559 hpunch
    w
    sound step_stairs_short
    imgf 901560
    w
    # после чего синеволосый показывает Барди фак и заходит в дом
    # classmate4 смотрит на Барди
    imgd 901561
    student_arnie "Привет, я Арни. Ты же новенький, верно?"
    imgd 901562
    bardi "Да, я [mcname]."
    # жмут друг другу руки
    imgf 901563
    w
    imgd 901564
    student_arnie "Заходи, чувак." # машет рукой, приглашая Барди в дом
    # Барди идет следом за ним
    # смена кадра - гостиная дома Арни, свет приглушен до вечернего, громкая музыка и смех
    # Барди оглядывается
    # повсюду пьяные студенты, на всех поверхностях стоят бумажные стаканчики и бутылки
    # на полу валяются пустые бутылки и мятые стаканчики
    # на диване сидит пьяный Лео, очки на лице перекошены, рядом с ним одна из второстепенных девочек из группы, хихикает
    # рядом сидит парочка студентов (из второстепенных) и целуется взасос
    # Эмили сидит в обнимку с Гарри, в руках стаканчики с алкоголем
    # в стороне с сигаретой и бутылкой крепкого алкоголя стоит фрик Хлоя в одиночестве
    # остальные танцуют или стоят по парам
    # все пьют, кроме зануды Сары
    # она стоит в стороне в обнимку с книгой, трезвая, и недовольно смотрит на происходящее
    # перед Барди внезапно появляется Арни с бутылкой вискаря в руках, пьяно улыбается
    fadeblack 1.0
    music2 party_ambience
    imgfl 911193
    music She_Is
    w
    imgf 911194
    w
    imgd 911195
    w
    sound vjuh3
    img 911196 hpunch
    student_arnie "Ты опоздал на вечеринку, новенький!"
    sound Jump2
    img 911197 vpunch
    student_arnie "Это штраф за опоздание!" # демонстрирует ему бутылку (бутылка неполная)
    student_arnie "Пей!"
    bardi "Что, все?! А пиво есть?"
    imgd 911198
    student_arnie "Пей!"
    # Арни вручает Барди бутылку и снова повторяет
    imgd 911199
    student_arnie "Пей! Пей! Пей!"
    # несколько пьяных студентов подхватывают
    imgd 911207
    student_leo "ПЕЙ!"
    imgd 911208
    student_jacob "ПЕЙ!"
    imgd 911199
    student_arnie "ПЕЙ!"
    # Барди смотрит на бутылку, потом кадр на Эмили
    # Эмили, так чтобы Гарри не видел, слегка улыбается Барди и смотрит на него в ожидании
    imgd 911200
    bardi "..."
    menu:
        "Выпить виски.": # кролик
            $ mlsBardiDay4College5 = day # Барди выпил виски в начале вечеринки (Сара)
            imgf 911201
            bardi "Окей. Я это сделаю."
            # наклоняет бутылку над лицом и пьет
            # пьяный Арни довольно смотрит на него
            sound snd_drinking_water
            imgd 911202
            sound2 snd_applause2
            student_arnie "Ееее! Круто, чувак!"
            imgd 911203
            student_arnie "Если хочешь еще, возьми вон там." # тычет пальцем в сторону столика с бутылками
            pass
        "Взять пиво.": # крыса   (минет)
            imgf 911204
            bardi "Окей. Только я буду пиво."
            # пьяный Арни непонимающе смотрит на него
            imgd 911205
            student_arnie "Пиво?"
            # потом машет на него рукой
            imgd 911203
            student_arnie "Поищи вон там." # тычет пальцем в сторону столика с бутылками
            pass
    imgf 911206
    w
    # в этот момент на Арни вешается пьяная студенка и целует его
    # Барди пользуется моментом и отходит
    # переход в движок
    return

# при клике на столик с алкоголем
label ep03_dialogues2_college_13:
    sound bottle1
    imgf 901579
    bardi_t "О, отлично! Возьму еще одну бутылку."
    # у Барди в руке появляется бутылка пива
    return

# при клике на Лео до общения с Хлоей
label ep03_dialogues2_college_13a:
    imgf 911063
    bardi_t "Не, о чем мне разговаривать с пьяным ботаном?.."
    return


# при клике на Эмили и Гарри
label ep03_dialogues2_college_15:
    # Эмили сидит со скучающим видом, недовольная, Гарри ее обнимает, у него в руке бутылка пива
    # он попутно пялится на других девочек, но Эмили этого не видит
    if get_active_objects("NicoleClassmate1", scene="party1") != False:
        imgf 911209
        w
    imgd 911210
    bardi_t "Этот безмозглый качок ни на минуту не отходит от Эмили..."
    # в этот момент одна из пьяных студенток забирается на стол, опрокидывая бутылки и начинает откровенно танцевать (student_girl2, которая потом будет на кухне с Шоном)
    # все студенты начинают свистеть и выкрикивать ей
    # Барди смотрит на танцующую студентку
    # observing - ?
    music Stylish_Fashion_Electronic_Rock
    imgf 911211
    sound2 heel1
    w
    imgd 911212
    w
    # video
    # v_Observe_Classmate10_1_25
    img black_screen
    with diss
    pause 1.0
    scene black
    sound2 snd_applause3
    image videov_Observe_Classmate10_1_25 = Movie(play="video/v_Observe_Classmate10_1_25.mkv", fps=25, loop=False, image="/images/Slides/v_Observe_Classmate10_1_end.jpg")
    show videov_Observe_Classmate10_1_25
    $ renpy.pause(0.5, hard=True)
    pause 4.5
    img v_Observe_Classmate10_1_end
    show screen image_shake("/images/Slides/v_Observe_Classmate10_1_end.jpg")
    w

    imgd 911213
    student_leo "Ого!"
    imgf 911215
    student_boy2 "Оу, какая попка!"
    imgd 911214
    sound snd_applause2
    student_boy1 "Ееее!!!"
    imgd 911216
    student_arnie "Дааа, детка!"
    student_arnie "Давай-давай! Ха-ха!"
    # потом переводит взгляд на Эмили
    # Эмили закатывает глаза и отворачивается в сторону от танцующей студентки
    imgd 911217
    student_emily "!!!"
    # а Гарри, наоборот, пускает слюни и пялится на нее
    sound snd_applause3
    imgd 911218
    student_harry "..."
    # потом замечает взгляд Барди и делает устрашающую рожу, показывая кулак
    sound Jump1
    img 911219 hpunch
    student_harry "Ррр!.."
    # с силой прижимает к себе Эмили и целует ее или лапает демонстративно
    sound vjuh3
    img 911220 vpunch
    bardi_t "Придурок!"
    imgd 911221
    w
    # к танцующей девочке подходит Арни и, взяв за талию, спускает к себе на пол
    # целуются взасос
    return

# при клике на фрика Хлою
label ep03_dialogues2_college_16:
    # она стоит в стороне и курит с бутылкой в руке
    # рядом с ней столик или стул, на котором лежат салфетки
    music Kimono
    imgf 901582
    bardi_t "Неожиданно, что она здесь..."
    bardi_t "Думал, что она не ходит на такие тусовки..."
    # идет к ней, попутно берет себе еще пива
    sound bottle1
    imgd 901583
    w
    sound step_stairs_short
    imgf 901584
    w
    imgd 901585
    bardi "Эй, Хлоя, привет."
    bardi "Как тебе вечеринка?"
    # она бросает на него взгляд и безразлично отворачивается
    imgd 901586
    student_chloe "Отстой."
    imgd 901585
    bardi "М-да..."
    menu:
        "Сделать ей комплимент.": # кролик
            img 901585
            bardi "Отлично выглядишь, Хлоя."
            # она без особого энтузиазма
            imgd 901586
            student_chloe "Ага."
            student_chloe "Говори, чего хотел..."
            imgd 901585
            bardi "Нуу... Мы с тобой не особо общались в школе, но ты мне..."
            # в этот момент мимо проходит пьяный синеволосый и его заносит
            sound step_stairs_short
            imgf 901589
            w
            sound vjuh3
            img 911170
            w
            sound Jump1
            img 911171 hpunch
            student_jacob "Ооооу!!!"
            # он задевает Барди и тот налетает на Хлою, обливая ее грудь алкоголем из своей бутылки
            sound bulk1
            sound2 oooh5
            img 911172 vpunch
            student_chloe "Твою мать!"
            # Барди отталкивает синеволосого и тот шатаясь уходит
            imgd 911173
            student_jacob "Эээй... Ост-торожнее, придурок!"
            # Хлоя смотрит на свой облитый топ
            imgd 911174
            student_chloe "Что за кретин!"
            student_chloe "!!!"
            menu:
                "Оттереть пятно с кофты Хлои.":
                    # Барди тянется рукой к ее груди, чтобы вытереть
                    imgd 911175
                    bardi "Давай помогу!"
                    # она смотрит на его руку, которая приближается к ее груди и резко отталкивает ее
                    sound snd_slap1
                    img 911176 hpunch
                    student_chloe "Ты охренел, [mcname]?!"
                    student_chloe "Иди в жопу! Я сама разберусь с этим!"
                    # она злая отходит от него и выходит из гостиной
                    sound highheels_short_walk
                    imgf 911177
                    bardi_t "Фак. А что я не так сделал то?"
                    bardi_t "Это все из-за придурка Джейкоба!"
                    jump ep03_dialogues2_college_16_1
                "Взять салфетку и помочь Хлое.":
                    imgd 911178
                    bardi "Подожди-подожди! Не трогай!"
                    bardi "Я сейчас!"
                    # он поспешно ставит бутылку на пол и хватает салфетку
                    # Хлоя с непониманием следит за его действиями
                    sound swish
                    imgf 911179
                    w
                    imgd 911180
                    student_chloe "Эй, что ты собрался делать? Я сама!.."
                    # в этот момент Барди прикладывает салфетку к ее груди и начинает возюкать ею туда-сюда (делает все быстро, чтобы она не успела опомниться)
                    # она удивленно на него смотрит
                    imgd 911181
                    bardi "Просто нужно сразу оттереть это! Иначе след останется!.."
                    # туда-сюда салфеткой, сам пялится якобы на пятно, но на самом деле рассматривает грудь
                    # мимо проходит кто-то из парней студентов и присвистывает, глядя на них
                    # Хлоя зло показывает ему фак, а Барди не обращает внимания, весь погружен в процесс
                    sound Jump1
                    img 911190 hpunch
                    w
                    imgd 911182
                    w
                    imgd 911183
                    w
                    imgd 911182
                    w
                    imgd 911183
                    bardi_t "Хмм... Неплохие сиськи..."
                    # Барди снова ведет салфетку, уже медленно
                    imgf 911184
                    bardi_t "Было бы круто увидеть ее без этого топа..."
                    imgd 911185
                    bardi_t "Мммм..."
                    imgd 911184
                    w
                    imgd 911185
                    bardi_t "Может быть?.."
                    menu:
                        "Заставить ее снять топ.":
                            imgf 911182
                            bardi "Черт! Никак не оттирается!.."
                            bardi "Хлоя, тебе нужно снять этот топ!"
                            # она резко отталкивает его руку
                            sound snd_slap1
                            img 911186 hpunch
                            student_chloe "Да пошел ты, [mcname]!"
                            student_chloe "Я сама разберусь с этим!"
                            # она злая отходит от него и выходит из гостиной
                            sound highheels_short_walk
                            imgf 911177
                            bardi_t "Фак. А что я не так сделал то?"
                            # Барди поднимает с пола свою бутылку
                            jump ep03_dialogues2_college_16_1
                        "Потереть еще.":
                            pass
                    imgd 911184
                    w
                    imgd 911185
                    bardi_t "Сделать так, чтобы она сама сняла этот топ?.."
                    imgf 911182
                    w
                    imgd 911183
                    bardi_t "Нет, это плохая идея."
                    imgd 911184
                    w
                    imgd 911185
                    bardi_t "Верный способ быть посланным на хрен."
                    # проводит салфеткой туда-сюда
                    imgd 911187
                    w
                    imgd 911188
                    bardi_t "Лучше воспользоваться моментом и потрогать ее еще немного..."
                    imgd 911187
                    w
                    # Хлоя смотрит на него и видит, что тот залип на ее груди
                    imgd 911184
                    w
                    imgf 911189
                    student_chloe "Эй, по ходу ты увлекся!.."
                    # он ее не слышит, продолжает натирать грудь
                    # водит салфеткой туда-сюда
                    imgd 911184
                    w
                    imgd 911185
                    w
                    imgd 911187
                    w
                    imgd 911188
                    bardi_t "Интересно, она с кем-нибудь встречается?"
                    student_chloe "!!!"
                    # она резко отталкивает его руку
                    sound snd_slap1
                    img 911186 hpunch
                    student_chloe "[mcname], хватит!"
                    student_chloe "Дальше я сама разберусь!"
                    # она злая отходит от него и выходит из гостиной
                    sound highheels_short_walk
                    imgf 911177
                    bardi_t "Отличные сиськи, Хлоя!.."
                    # Барди поднимает с пола свою бутылку
                    jump ep03_dialogues2_college_16_1
        "Спросить, одна ли она на вечеринке.": # крыса
            img 901585
            bardi "Ты здесь одна?"
            # она без особого энтузиазма
            imgd 901586
            student_chloe "Ага."
            student_chloe "Пришла посмотреть на пьяное стадо придурков-студентов."
            student_chloe "Говори, чего хотел..."
            bardi "Нуу..."
            # если Барди был на занятии живописи
            if mlsBardiDay3College1 > 0:
                imgd 901585
                bardi "Я сегодня был приятно удивлен, увидев тебя на живописи."
                bardi "Кажется, у тебя здорово получается. Миссис Морис была довольна твоей работой."
                imgd 901586
                student_chloe "Типа того."
                imgd 901585
                bardi "Давно ты увлекаешься живописью?"
                imgd 901587
                student_chloe "Какое тебе дело до этого?!"
                # она раздраженно смотрит на него
                student_chloe "Слушай, [mcname]... Чего тебе от меня надо?!"
            # если не был на живописи
            else:
                imgd 901585
                bardi "Подумал, что ты не будешь против моей компании..."
                # она раздраженно смотрит на него
                imgd 901588
                student_chloe "Слушай, [mcname]... Чего тебе от меня надо?!"
            # в этот момент мимо проходит пьяный синеволосый и его заносит
            sound step_stairs_short
            imgf 901589
            w
            sound vjuh3
            img 911170
            w
            sound Jump1
            img 911171 hpunch
            student_jacob "Ооооу!!!"
            # он задевает Барди и тот налетает на Хлою, обливая ее грудь алкоголем из своей бутылки
            sound bulk1
            sound2 oooh5
            img 911172 vpunch
            student_chloe "Твою мать!"
            # Барди отталкивает синеволосого и тот шатаясь уходит
            imgd 911173
            student_jacob "Эээй... Ост-торожнее, придурок!"
            # Хлоя смотрит на свой облитый топ
            imgd 911174
            student_chloe "Что за кретин!"
            student_chloe "!!!"
            # она злая отходит от него и выходит из гостиной
            sound highheels_short_walk
            imgf 911177
            bardi_t "Да уж. Хлоя далеко не такая милашка как Роуз..."
            bardi_t "Кстати, а Роуз здесь нет?.."
            jump ep03_dialogues2_college_16_1
    $ mlsBardiDay4College7 = day # Барди пообщался на вечеринке с фриком Хлоей
    label ep03_dialogues2_college_16_1:
    # Барди стоит один и смотрит на остальных студентов
    fadeblack 1.0
    music She_Is
    imgf 911191
    bardi_t "Похоже, здесь все сегодня друг с другом перетрахаются..."
    $ ep13_after_chloe_flag = True
    # Барди пьет пиво и из-за бутылки смотрит
    # сначала на стоящую в сторонке Сару, потом на Лео
    imgd 901581
    bardi_t "Кроме зануды..."
    bardi_t "Хмм..."
    label ep03_dialogues2_college_17_loop:
    # кадр, где одновременно видно и парочку девочек и Сару
    if get_active_objects("NicoleClassmate1", scene="party1") != False:
        imgf 911192
        w
    return

label ep03_dialogues2_college_16_sarah:
    ###
#    menu:
#        "Подойти к зануде.":
            # если Барди выпил виски в начале вечеринки
    if ep13_after_chloe_flag == True or ep13_after_leo_flag == True:
#    if mlsBardiDay4College5 > 0 and ep13_after_chloe_flag == True:
        imgd 901579
        bardi_t "Интересно, не откажется ли зануда от выпивки?.."
        jump ep03_dialogues2_college_18
    # если отказался пить виски в начале вечеринки
    else:
        sound snd_drinking_water
        imgd 901580
        bardi_t "Эээ, нет. Я не собираюсь к ней подходить."
        bardi_t "Я еще не выпил столько, чтобы терпеть ее занудную болтовню."
        jump ep03_dialogues2_college_17_loop


label ep03_dialogues2_college_16_leo:
#        "Подойти к Лео.":
    imgf 911063
    bardi_t "Хмм... А как так получилось, что на этой вечеринке оказался ботан Лео?"
    jump ep03_dialogues2_college_14
#    return

# Барди подходит к дивану, где сидит Лео
label ep03_dialogues2_college_14:
    # на Лео виснет студентка из группы Барди
    sound step_stairs_short
    imgd 901565
    bardi_t "И часто Лео так тусит в свободное от библиотеки время?"
    # Лео расплывается в довольной пьяной улыбке
    imgf 901566
    student_leo "Эй, привет, [mcname]! Ииик!"
    imgd 901567
    student_girl4 "О, Лео, это же наш новенький!"
    # она вцепляется в руку Барди и тянет его к себе
    imgd 901568
    student_girl4 "Привеееет, красавчик!"
    student_girl4 "Пошли к нам!"
    sound step_stairs_short
    imgf 901569
    w
    imgd 901570
    bardi "Привет. Это ты так напоила Лео?"
    imgd 901571
    student_girl4 "Хи-хи. Он просто опоздал, как и ты."
    student_girl4 "Арни его заставил выпить виски и запить пивом, хи-хи."
    # пьяный Лео пытается безрезультатно поправить очки
    imgd 901572
    student_leo "Вообще-то, ик, я не уп-потребляю алкоголь!.."
    student_leo "Согласно исследованиям, ик, алкоголь, поступая в кровь, изменяет ее состав, ик..."
    imgd 901573
    student_leo "Что отрицательно действует на лейкоциты, ик, и они перестают бороться с различными микробами!.."
    student_leo "А микробы, в свою очередь..."
    imgd 901574
    bardi "Стоп-стоп! Мы все поняли, Лео. Остановись!"
    bardi "Ты как вообще попал на эту вечеринку?"
    imgd 901575
    student_leo "Мы пришли сюда с Сарой, ик, потому что Арни нам сказал..."
    student_leo "Что здесь будут настольные игры и всякие вкусняшки, ик..."
    student_leo "Ну там, Монополия и все такое, ик..."
    sound snd_drinking_water
    imgd 901576
    w
    # Лео присасывается к бутылке с пивом
    imgd 901577
    bardi "Монополии тут явно нет, но вкусняшек хоть отбавляй, чувак."
    bardi "Ладно, веселитесь, ребята."
    # Барди отходит от них и идет к столику с бутылками
    sound step_stairs_short
    imgf 901578
    bardi_t "Возьму себе еще пива."
    sound bottle1
    imgd 901579
    w
    sound2 snd_drinking_water
    if get_active_objects("Classmate7", scene="party1") != False:
        imgf 901580
        w
        imgd 901581
        w
    # пьет и смотрит в сторону зануды Сары, которая недовольная стоит в углу
    $ mlsBardiDay4College6 = day # Барди пообщался на вечеринке с ботаном Лео
    return

# если подходит к Лео, то после разговора с ним идет к зануде Саре
# если подходит сразу к зануде, то скип Лео

# при клике на зануду Сару
label ep03_dialogues2_college_18:
    # она стоит в стороне в обнимку с учебниками и сердито смотрит то на пьяного Лео, который продолжает обниматься со студенткой на диване, то на девочек неподалеку
    # Барди подходит к ней
    music Kimono
    imgf 911071
    w
    imgd 911072
    w
    sound step_stairs_short
    imgf 911058
    bardi "Привет. Скучаешь?"
    # она недовольно бурчит
    imgd 911059
    student_sarah "Привет, [mcname]."
    student_sarah "Смотрю, тебе также весело как и остальным!" # указывает на бутылку у него в руках
    imgd 911060
    bardi "Тебе нужно немного расслабиться."
    # протягивает ей бутылку
    bardi "Будешь? Совсем немного."
    # она косится на пиво, мнется
    # потом решительно
    imgd 911061
    student_sarah "Конечно, нет!"
    student_sarah "Как можно травить свой организм этой гадостью?!"
    # она возмущенно указывает рукой на Лео
    imgd 911062
    student_sarah "Вот пример пагубного влияния алкоголя на организм! Посмотри, что происходит с Лео!"
    # Барди оглядывается, Лео также на диване в обнимку с девочкой
    imgf 911063
    bardi "По-моему, он отлично проводит время..."
    imgd 911064
    student_sarah "А ты, [mcname], не намного лучше него выглядишь!"
    bardi "Разве?"
    sound Jump1
    img 911065 hpunch
    student_sarah "Ты еле на ногах стоишь! И все равно продолжаешь пить эту дрянь!"
    # она выхватывает бутылку пива у него из рук
    # не пьет, просто забрала
    imgd 911066
    bardi "?!"
    menu:
        "Ты права. Мне хватит.":
            imgd 911067
            bardi "Окей. Ты права, во мне уже достаточно алкоголя."
            student_sarah "Конечно, я права!"
            pass
        "Отобрать у нее бутылку.":
            # Барди тянет руку за своей бутылкой
            imgd 911068
            bardi "Эй!"
            bardi "А ну верни мне!"
            # она упрямо
            student_sarah "Нет!"
            imgd 911069
            student_sarah "Между прочим, алкоголь, поступая в кровь, изменяет ее состав и..."
            if mlsBardiDay4College6 > 0:
                bardi "И тромбоциты перестают бороться с различными микробами... Бла-бла..."
                student_sarah "Лейкоциты!!!"
            imgd 911070
            bardi "Да какая разница?!"
            student_sarah "Колоссальная!"
            # она упорно прячет от него бутылку
            # он сдается, поднимая руки
            imgd 911067
            bardi "Ну окей. Твоя взяла."
            pass
    imgd 911066
    bardi "Мне надо немного освежиться."
    bardi "Не составишь мне компанию?"
    # она бросает взгляд на Лео
    imgf 911073
    w
    imgd 911074
    student_sarah "Пошли, [mcname]!"
    student_sarah "Так уж и быть, присмотрю за тобой!"
    # они идут из гостиной в сторону ванной
    sound step_stairs_short
    imgf 911075
    w
    # по пути Барди незаметно для Сары отбирает у кого-то из студентов бутылку вискаря
    sound bottle1
    imgd 911076
    w
    # затемнение, смена кадра на ванную
    # над унитазом стоит и дрочит один из студентов
    fadeblack
    music2 stop
    sound snd_door_open1
    pause 1.5
    music Shining_Through
    sound2 sex_moan_man
    music2 male_masturbation1
    imgfl 911077
    w
    imgf 911078
    w
    imgd 911079
    bardi "Эй, чувак! Тебя там ищет какая-то девчонка."
    bardi "Сказала, что ждет тебя в гостиной."
    # парень испуганно-полупьяно подрывается и натягивает штаны
    music2 stop
    sound Jump2
    img 911080 hpunch
    student_boy2 "Я уже все. Ухожу!"
    # парень выбегает, Сара с отвращением смотрит ему вслед
    sound snd_runaway
    imgd 911081
    w
    sound snd_door_open1
    imgf 911082
    student_sarah "Какой кошмар!"
    student_sarah "Это не вечеринка, а сплошной разврат и пьянство!"
    student_sarah "Это отвратительно!.."
    # ее причитания прерывает шум воды - Барди умывается, стоя спиной к Саре
    sound snd_shower
    imgd 911083
    bardi "Бррр!.."
    # та за ним наблюдает
    imgd 911084
    student_sarah "И зачем так издеваться над собой, не понимаю?"
    # Барди поворачивается к ней
    bardi "Как?"
    imgf 911085
    student_sarah "Ходить на такие неприличные сборища!"
    bardi "Неприличные?"
    student_sarah "Да!"
    imgd 911086
    bardi "Все понятно с тобой..."
    bardi "Кстати, как тебя зовут? Никак не могу запомнить..."
    imgd 911085
    student_sarah "Сара."
    # Барди берет в руку бутылку, которую забрал у студента по пути в ванную
    sound bottle1
    imgd 911087
    w
    imgd 911088
    bardi "Ну, за знакомство, Сара!.."
    # наклоняет бутылку и пьет
    # она молча смотрит на него
    label ep03_dialogues2_college_18_loop:
    # Барди смотрит на нее, та стоит строя из себя правильную, при этом продолжает прятать от Барди в руке ту бутылку, которую отняла у него в гостиной
    sound snd_drinking_water
    imgd 911089
    w
    imgd 911090
    w
    imgd 911091
    bardi "..."
    menu:
        "А ты сама как сюда попала?":
            bardi "А ты сама как сюда попала?"
            imgd 911092
            student_sarah "Арни Уокер пришел в библиотеку и сказал нам с Лео..."
            student_sarah "Мы с Лео как раз составляли программу по подготовке работы с эссе."
            imgd 911093
            student_sarah "И Арни нам сказал, что сегодня он с друзьями будет играть в Монополию."
            student_sarah "Сказал, что будет всего пара его знакомых и все будет очень прилично."
            student_sarah "И еще про вкусняшки сказал..."
            sound laughing_male2
            imgd 911094
            bardi "Ха-ха-ха!"
            bardi "То есть ты пришла играть в Монополию?"
            imgd 911095
            student_sarah "Да..." # обиженно
            $ ep03_dialogues2_college_18_menu1 = True
            jump ep03_dialogues2_college_18_loop
        "Почему же ты не ушла отсюда?":
            bardi "Почему же ты не ушла отсюда?"
            imgd 911096
            student_sarah "Ты видел, в каком состоянии Лео?!"
            student_sarah "Как я могу бросить его здесь без присмотра?!"
            student_sarah "Среди этой пьяной беснующейся толпы?!"
            imgd 911097
            bardi "По-моему, он весьма неплохо проводит время..."
            bardi "Ты бы лучше сама расслабилась, чем так переживать за Лео."
            img 911098
            student_sarah "Нет!" # упрямо
            $ ep03_dialogues2_college_18_menu2 = True
            jump ep03_dialogues2_college_18_loop
        "Слушай, а ты с кем-нибудь встречалась?" if ep03_dialogues2_college_18_menu1 == True and ep03_dialogues2_college_18_menu2 == True:
            pass
    bardi "Слушай, Сара, а ты когда-нибудь с кем-нибудь встречалась?"
    imgd 911093
    student_sarah "В смысле?"
    imgd 911094
    bardi "Ну там, обнимашки, подарочки... Романтические прогулки под луной и все такое..."
    imgd 911099
    student_sarah "Какая глупость!"
    student_sarah "У меня нет времени на эти пошлости!"
    student_sarah "Я очень занята другими важными делами. Более важными, чем все это!"
    imgd 911101
    bardi "Разве тебе не хочется всего этого?"
    imgd 911100
    student_sarah "Мне... Я..."
    student_sarah "..."
    # внезапно Сара прикладывается к бутылке, которую ранее отняла у Барди и делает несколько нервных глотков
    sound Jump1
    img 911102 hpunch
    sound2 snd_drinking_water
    bardi "Хм. Давно пора."
    $ blur_effect = 1
    imgd 911102
    w
    $ blur_effect = 0
    imgd 911102
    w
    imgd 911103
    bardi "Ну так что?"
    student_sarah "Не хочется!"
    # она снова хочет приложиться к бутылке, но та уже пуста
    imgd 911104
    bardi "Не ври."
    # Барди услужливо забирает пустыю бутылку пива и вкладывает ей в руку бутылку вискаря
    music Step_By_Step
    imgd 911105
    bardi "Попробуй это."
    # она жадно пьет
    sound vjuh3
    img 911106 hpunch
    w
    sound snd_drinking_water
    imgd 911107
    bardi "Эй-эй, полегче! Не так быстро..."
    $ blur_effect = 2
    imgd 911107
    w
    $ blur_effect = 0
    imgd 911107
    w
    # она отлепляется от бутылки и вытирает рот
    imgd 911108
    student_sarah "Вообще, это не твое дело, [mcname], встречалась ли я с кем-нибудь или нет!.."
    student_sarah "Что за допрос?!"
    student_sarah "Конечно, встречалась!"
    # Сара снова пьет, по ней видно, что она становится пьяная
    sound snd_drinking_water
    imgd 911107
    w
    imgd 911110
    bardi "Да ну?! С кем же?"
    bardi "С Лео?"
    img 911109
    student_sarah "Вот еще!"
    student_sarah "Я не собираюсь тебе ничего рассказывать! Ты все равно их не знаешь!"
    imgd 911110
    bardi "И сколько их было?"
    imgd 911108
    student_sarah "Тебя это не касается!"
    imgd 911110
    bardi "А может это были не парни? Может, ты по девочкам, м?"
    imgd 911111
    student_sarah "Парни! Мне нравятся парни!"
    bardi "Докажи..."
    student_sarah "Ч-что?.."
    imgd 911112
    bardi "Уверен, что ты даже целоваться не умеешь, мисс Всезнайка."
    # Барди отбирает у нее бутылку и отставляет ее в сторону
    student_sarah "Не называй меня так!.."
    student_sarah "И, вообще-то, я умею ВСЕ!"
    bardi "Тогда докажи..."
    # Сара пьяно и задумчиво смотрит на Барди
    imgd 911113
    student_sarah "..."
    student_sarah "......"
    student_sarah "Садись."
    # Сара указывает рукой на унитаз (сделайте ее пьяной, чуть шатающейся)
    sound vjuh3
    imgd 911114
    bardi_t "Намечается что-то интересное..."
    # Барди сидит на унитазе. Сара в важной позе стоит перед ним скрестив руки
    sound step_stairs_short
    imgf 911115
    w
    imgd 911116
    student_sarah "Снимай штаны."
    $ blur_effect = 2
    imgd 911116
    bardi "Ахаха! Ты чего? Зачем?"
    $ blur_effect = 0
    imgd 911116
    w
    # в такой же важной позе Сара указывает на Барди пальцем.
    # Изобразите ее как важную фифу, вот она стоит полубоком
    # и из прошлой позы разворачивает правую руку от локтя в сторону Барди, кисть расслабленна, тыльной стороной вниз, а указательный палец направлен в сторону Барди.
    # в общем вся такая важная, гордая, умелая
    imgd 911117
    student_sarah "Доставай член."
    imgd 911116
    bardi_t "..."
    bardi_t "Ох, что-то мне подсказывает, что это плохая идея..."
    bardi_t "Но зато будет что вспомнить, лол."
    # Барди снял штаны и вытащил член. У него не стоит.
    # Сара встает на колени.
    fadeblack 1.0
    music Step_By_Step
    imgf 911118
    bardi_t "Чувствую, это будет незабываемо..."
    sound Jump1
    imgd 911119
    bardi_t "И угарно."
    # Сара смотрит на член, потом отводит взгляд, потом снова на член, затем в глаза Барди (т.е в камеру).
    # В это время выражение ее лица меняется на робкое и смущенное, а в конце на уверенное.
    imgf 911120
    w
    imgd 911121
    w
    imgd 911122
    student_sarah "Смотри и учись!"
    bardi_t "Я, конечно, посмотрю... Но учиться, пожалуй, не буду, спасибо."
    # Сара обхватывает рукой член. Он не встает
    # Сара поднимает глаза на Барди, выражение лица недовольное
    imgf 911127
    w
    imgd 911123
    student_sarah "Ну и?.."
    bardi "Что?"
    # Выражение лица Сары становится хмурым.
    imgd 911124
    student_sarah "Ну ты и идиот..."
    # Сара отводит усталый взгляд в сторону.
    student_sarah "Господи, как ребенок!.."
    # Сара смотрит на Барди хмуро.
    imgd 911125
    student_sarah "Ну поднимай его!"
    bardi_t "Так. Что?"
    bardi "Ты же вроде отличница... Ты знаешь, как это работает?"
    student_sarah "Конечно, знаю!"
    # Сару начинает немного накрывать от алкоголя
    imgd 911126
    student_sarah "Как ты прикажешь это делать, если даже поднять его не можешь?!"
    bardi "Попробуй ты его поднять."
    # Сара недоверчивым или даже каким-то скептическим взглядом смотрит на член.
    imgd 911130
    student_sarah "Боже! Сколько же проблем! И почему нельзя просто, как в видео?!"
    # Сара берется за головку члена и вытягивает его вверх. Член падает.
    imgf 911128
    w
    sound vjuh3
    img 911129 hpunch
    student_sarah "!!!"
    bardi_t "Как бы только не заржать?! И как у меня должен встать в такой момент?!"
    # Она снова берется за головку и поднимает его, но все по прежнему.
    # Сара смотрит на Барди с сочувствием
    imgd 911127
    w
    imgd 911128
    w
    sound vjuh3
    img 911129 hpunch
    w
    imgd 911123
    student_sarah "Он у тебя сломан. Может ты импотент?"
    sound laughing_male2
    bardi "Ахаха! Нет, не может!"
    # Сара рассерженно смотрит на Барди
    imgd 911125
    student_sarah "Тогда что с ним?!"
    bardi "Попробуй немного поработать ручками и пососать его. Еще можешь оголить грудь..."
    # Сара смотрит на Барди с отвращением
    imgd 911134
    student_sarah "Пф! Много чести! Грудь ему покажи!.."
    bardi_t "А, то есть отсосать в толчке норм... Ясно, буду знать."
    # Сара смотрит на член Барди скептически и недоверчиво.
    # ее начинает явно мутить с бухла
    imgd 911131
    student_sarah "Посмотрим..."
    # Сара опускается к члену, в моменте ее жестко начинает тошнить (без рвоты, просто резко прикладывает ладонь ко рту).
    imgd 911132
    w
    img 911133
    student_sarah "ОЙ!"
    student_sarah "Мне что-то... Нехорошо..."
    bardi "Твою мать!"
    # Барди вскакивает с унитаза и Сара начинает блевать в толчок (сам процесс не показываем, она резко склоняется над унитазом + звуки)
    sound Jump1
    img 911135 hpunch
    sound2 chavc26
    bardi "Мать твою! И это называется, что ты умеешь?!"
    bardi "Господи! Нафиг надо!"
#    bardi "Возвращайся, когда будешь трезвой! Алкашка!"
    # в этот момент раздается звонок телефона, Сара продолжает блевать. Барди вытаскивает из ее кармана телефон
    # отвечает на звонок
    fadeblack 1.0
    sound2 snd_phone_ring
    music Shining_Through
    imgf 911136
    w
    imgd 911137
    w
    imgf 911138
    bardi "Такси? Да, вызывали."
    bardi "Да, скоро будем, секунду."
    sound snd_phone_short_beeps
    # звук сброшенного вызова.
    # Сара в обнимку с унитазом
    imgd 911139
    bardi "Когда ты успела вызвать такси?"
    student_sarah "До того, как ты ко мне подошел."
    # Сара поворачивает голову в сторону Барди
    imgd 911140
    student_sarah "Это же такси?"
    bardi "Господи! Да проблюйся ты сначала!"
    student_sarah "Я полностью держу все под контролем!"
    bardi "Да, я вижу..."
    # она встает и покачиваясь идет к двери
    # ее заносит и она чуть ли не падает
    sound highheels_short_walk
    imgf 911141
    student_sarah "Ой!"
    # Сара стоит, схватившись обеими руками за дверь (или стену), буквально обнимая ее
    imgd 911142
    w
    imgd 911143
    student_sarah "Как же все кружится..."
    # Сара поворачивается в сторону Барди и смотрит жалобным взглядом
    imgd 911144
    student_sarah "Кажется, я сама не дойду..."
    bardi "И? Что ты на меня то пялишься?"
    imgd 911145
    student_sarah "Вообще-то, я никогда не пила этой гадости раньше..."
    student_sarah "А еще ты должен мне за отсос!"
    bardi "Да уж. Однозначно, лучший минет в моей жизни..."
    # Сара с довольной улыбкой
    imgd 911146
    student_sarah "Вот! Я же говорила!"
    bardi "Ты врала."
    student_sarah "Нет. Я просто немного перебрала с алкоголем..."
    # Сара смотрит на Барди хмуро
    imgd 911147
    student_sarah "..."
    student_sarah "Ну помоги мне или так и будешь смотреть?! Меня такси, вообще-то, ждет!"
    bardi "..."
    # Барди лениво делает еще глоток из бутылки и нехотя отставляет ее
    bardi "Ладно-ладно. Так уж и быть, дотащу тебя до такси."
    sound step_stairs_short
    imgf 911148
    w
    # подходит к ней и приобнимает за талию, она на него облокачивается и идут к выходу
    # смена кадра на гостиную
    sound snd_door_open1
    fadeblack 1.5
    music2 party_ambience
    music Kimono
    imgf 911149
    w
    imgd 911150
    student_sarah "Надо позвать с собой Лео..."
    student_sarah "Я же не могу оставить его здесь одного!.."
    bardi "Лео не скучает, поверь мне. Пошли скорее в такси." # кадр на пьяного Лео в обнимку со студенткой
    # На Сару чуть ли не падает какой-то пьяный чел, Барди отталкивает его
    sound vjuh3
    img 911152 hpunch
    w
    sound Jump1
    img 911153 vpunch
    bardi "Друг, ЭТО тебе не по плечу. Не нужно оно тебе."
    # Барди, держа Сару проходит мимо парочки девочек, целующихся в стороне от остальных студентов
    # одна из целующихся - танцовшица на столе, вторая - девочка с каре и в джинсах
    imgf 911151
    bardi_t "Опа! А вот это уже интересно!"
    bardi_t "Надо скорее избавляться от пьяной зануды..."
    $ steam_achievement("ach_nerd1")

    # затемнение, звук мотора
    fadeblack
    music2 stop
    sound snd_car_turn_on
    pause 3.0
    sound snd_door_open1
    pause 1.5
#    music She_Is
    return 2

# при клике на парочку целующихся девчонок
label ep03_dialogues2_college_19:
    # Барди подходит к девочкам, те перестают целоваться и с любопытством смотрят на него
    # по ним видно, что они очень не трезвы
    music She_Is
    music2 party_ambience
    sound2 step_stairs_short
    imgfl 911154
    w
    sound snd_longkiss1
    imgf 911155
    bardi "Эй, привет."
    bardi "Не знал, что вы встречаетесь..."
    # девочки переглядываются и пьяно хихикают
    sound snd_woman_laugh4
    imgd 911156
    student_girl3 "Хи-хи..."
    # потом снова смотрят на Барди
    imgd 911157
    student_girl1 "Тебя ведь [mcname] зовут?"
    student_girl3 "Это правда, что ты приехал из мегаполиса?"
    imgd 911158
    bardi "Да, я [mcname] и я переехал сюда из большого города."
    bardi "Не надолго. Скоро я свалю отсюда..."
    imgd 911159
    student_girl1 "Уедешь обратно?"
    imgd 911158
    bardi "Да. У меня в городе осталось много друзей, престижный колледж и все такое..."
    bardi "Так что, здесь мне ловить нечего. Вынужденная временная мера."
    # девочки на него смотрят с интересом
    imgd 911160
    student_girl1 "Ух ты!.."
    bardi "Ага. Я тут подумал..."
    bardi "Может, пойдем в более тихое место? Поболтаем?"
    # Сара в этот момент бросает на Барди уничтожающий взгляд и снова отворачивается
    ### проверка, есть ли Сара в помещении
    if get_active_objects("Classmate7", scene="party1") != False:
        imgf 911163
        student_sarah "!!!"
    # девочка с каре улыбается Барди и подмигивает подружке
    imgd 911161
    student_girl3 "Отличная идея!"
    student_girl1 "Пошли. Сначала возьмем еще выпить на кухне..."
    # девочки и Барди идут мимо Сары, которая недовольно провожает их взглядом
    imgd 911162
    w
    ### проверка, есть ли Сара в помещении
    if get_active_objects("Classmate7", scene="party1") != False:
        sound highheels_short_walk
        imgf 911164
        w
    # смена кадра - они втроем заходят на кухню
    # смена кадра на кухню дома
    # на кухне та же полутьма и такой же бардак, как в гостиной - везде бутылки и стаканчики
    # из-за кухонного стола торчат ноги (Шон и одна из второстепенных одногруппниц Барди)
    fadeblack
    music2 stop
    sound highheels_short_walk
    pause 1.5
    music Step_By_Step
    imgfl 911165
    w
    imgf 911166
    sound snd_woman_laugh4a
    student_girl2 "Мне щекотно!.."
    student_girl2 "Что ты делаешь, Шон?! Хи-хи!"
    imgd 911167
    bardi "Шон?.."
    # из-за стола резко показывается голова Шона
    sound Jump1
    img 911168 hpunch
    sean "О, чувак!"
    sean "Ты принес презервативы?"
    bardi "Не-а. Забыл."
    bardi_t "Вернее, забил..."
    sean "Фак, хреново! Ну ладно, спрошу у кого-нибудь!"
    sound vjuh3
    img 911167 vpunch
    w
    # голова Шона снова скрывается за столом
    # девочка с каре с невозмутимым видом проходит мимо стола, берет бутылку вискаря и идет к выходу
    sound bottle1
    imgf 911169
    student_girl3 "..."
    # затемнение, шаги
    # смена кадра на спальню
    # Барди и девочки заходят в спальню
    # student_girl3 (с каре) закрывает дверь на ключ
    # вторая (student_girl1, она же student_abby) плюхается на кровать
    # бутылку ставит рядом с кроватью
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Shining_Through
    imgf 910830
    w
    sound snd_keys_door_open
    imgd 910831
    w
    sound highheels_short_walk
    imgf 910833
    w
    sound snd_glass_table
    imgd 910832
    w
    sound highheels_short_walk
    imgf 910834
    student_girl1 "[mcname], Кэти, у меня идея!"
    student_girl1 "Давайте поиграем в правду или действие?"
    # девочка с каре (student_katie) тоже лезет на кровать
    imgd 910841
    student_katie "Да, отличная идея, Эбби!"
    imgd 910835
    w
    imgd 910836
    student_katie "[mcname], идем к нам!"
    # Барди заваливается к ним на кровать
    sound step_stairs_short
    imgf 910837
    w
    imgd 910867
    w
    imgd 910838
    bardi "Какие правила игры?"
    imgd 910839
    student_abby "Каждый из нас задает по вопросу остальным игрокам."
    student_abby "Если тебе задали вопрос, ты можешь либо ответить на него... Только правду!"
    student_abby "Либо ты можешь не отвечать, а выбрать действие. И мы скажем, что нужно сделать."
    imgd 910838
    bardi "Окей. Звучит интересно."
    imgd 910839
    student_abby "Играем?"
    imgd 910840
    student_katie "Да-да, давайте!"
    imgd 910838
    bardi "Играем! Кто первый задает вопрос?"
    # кадр на Эбби (Кэти и Барди потом разденутся, их не брать в кадр)
    label ep03_dialogues2_college_19_loop:
    music Step_By_Step
    imgd 910838
    menu:
        "Кэти.":
            # Кэти смотрит на Эбби
            imgf 910842
            student_katie "Вопрос к Эбби."
            student_katie "Ты когда-нибудь делала минет парню? Правда или действие?"
            imgd 910843
            student_abby "Правда!"
            student_abby "Делала. И даже не один раз, хи-хи."
            sound snd_woman_laugh4
            imgd 910844
            w
            # Кэти поворачивается к Барди
            imgf 910845
            student_katie "Вопрос к [mcname]."
            student_katie "Ты любишь делать девушкам куни? И делал ли вообще?"
            student_katie "Правда или действие?"
            imgd 910846
            w
            menu:
                "Правда.":
                    imgd 910847
                    bardi "Правда."
                    bardi "Делал, конечно."
                    # девочки с большим любопытством
                    imgd 910848
                    student_abby "И?.."
                    bardi "Что?"
                    imgd 910850
                    student_katie "Тебе нравится делать ЭТО?"
                    bardi "Да, нравится."
                    # девочки пристально на него смотрят и улыбаются
                    imgd 910849
                    student_abby "Нам с Кэти тоже нравится делать это..."
                    student_katie "Хи-хи. Очень нравится."
                    student_abby "Играем дальше. Кто следующий?"
                    pass
                "Действие.":
                    imgd 910847
                    bardi "Действие."
                    imgf 910851
                    student_abby "Оооо, Кэти!"
                    student_abby "Наш красавчик не хочет отвечать на этот неудобный вопрос."
                    imgd 910852
                    student_katie "В таком случае, [mcname] должен поцеловать Эбби, хи-хи..."
                    bardi_t "Оу, даже так?.."
                    # Эбби смотрит на Барди пьяными глазками и подмигивает
                    imgd 910853
                    bardi_t "Хмм... Девочки явно хотят повеселиться сегодня как следует..."
                    bardi_t "Что ж, я не против..."
                    # Барди наклоняется к ней и Эбби, закрыв галаз, подставляет свои губы, сложенные для поцелуя
                    # целуются
                    sound vjuh3
                    img 910854 hpunch
                    w
                    imgd 910855
                    w
                    imgd 910873
                    w
                    imgd 910856
                    w
                    sound snd_longkiss1
                    imgd 910857
                    w
                    sound lick10
                    imgf 910858
                    w
                    imgd 910859
                    w
                    imgd 910860
                    student_abby "Мммм..."
                    # Эбби после долгого поцелуя отстраняется от него и смотрит томно
                    imgf 910861
                    w
                    imgd 910862
                    student_abby "А он отлично целуется, Кэти..."
                    student_katie "Хи-хи. Почему-то, я не сомневалась в этом."
                    imgd 910839
                    student_abby "Играем дальше. Кто следующий?"
                    pass
            $ ep03_dialogues2_college_19_menu1 = True
            jump ep03_dialogues2_college_19_loop
        "Эбби." if ep03_dialogues2_college_19_menu1 == True:
            # Эбби смотрит на Кэти
            imgf 910863
            student_abby "Вопрос к Кэти."
            student_abby "Кэти, ты когда-нибудь хотела заняться сексом втроем?"
            # Кэти смущенно опускает глаза
            imgd 910864
            student_katie "Ой... Действие!"
            imgd 910865
            student_abby "Ты раздеваешься до нижнего белья!"
            student_katie "Что, прямо до нижнего?!"
            student_abby "Да, давай!"
            imgd 910866
            bardi_t "Отлично! Мне определенно нравится эта игра..."
            # Кэти встает с постели, пьет из бутылки, а потом снимает одежду и швыряет ее на пол
            # остается в одном нижнем белье и залезает обратно на постель
            # Барди пялится на нее
            # observing - ?
            # Кэти в это время смотрит на Барди
            ## во время всего этого действа можно какие-нибудь мысли Барди, а то много кадров без диалога
            sound snd_walk_barefoot
            imgf 910868
            w
            imgd 910870
            w
            sound snd_drinking_water
            imgd 910869
            w
            sound snd_glass_table
            img 910870
            w
            music Stylish_Hip_Hop_Rock
            imgf 910871
            w
            sound vjuh3
            img 910872 hpunch
            bardi_t "Ух ты!.."
            sound wow
            imgd 910874
            bardi_t "Оу, какая попка!"
            imgf 910875
            w
            sound vjuh3
            img 910876 vpunch
            w
            imgd 910877
            w
            sound Jump1
            imgd 910878
            bardi_t "Ееее!!!"
            fadeblack 1.0
            music Step_By_Step
            imgf 910879
            w
            imgd 910881
            student_katie "Нравится?"
            imgd 910880
            bardi "Конечно. Потрясная фигура."
            imgd 910881
            student_katie "Спасибо."
            # тем временем Эбби обращается к Барди
            imgf 910882
            student_abby "Вопрос к [mcname]."
            student_abby "Ты когда-нибудь занимался анальным сексом?"
            imgd 910883
            student_abby "Правда или действие?"
            menu:
                "Правда.":
                    imgd 910884
                    bardi "Правда."
                    bardi "Не занимался, но хотелось бы это исправить скорее..."
                    # девочки уже откровенно пошло ему улыбаются и строят глазки
                    imgf 910885
                    sound snd_woman_laugh4
                    w
                    imgd 910886
                    student_abby "Играем дальше. Кто следующий?"
                    pass
                "Действие.":
                    imgd 910884
                    bardi "Действие."
                    imgd 910882
                    student_abby "Отлично! Ты, [mcname], снимаешь с себя футботку и джинсы!"
                    imgd 910883
                    bardi "Без проблем. Только у меня под джинсами нет белья..."
                    imgd 910885
                    sound snd_woman_laugh4
                    student_katie "О, правда?!"
                    student_abby "Окей. Тогда только футболку."
                    # Барди встает с постели и раздевается, потом возвращается
                    # девочки уже откровенно пошло ему улыбаются и строят глазки
                    sound step_stairs_short
                    imgf 910887
                    w
                    imgd 910888
                    sound put_dress
                    w
                    imgd 910886
                    student_abby "Играем дальше. Кто следующий?"
                    pass
            $ ep03_dialogues2_college_19_menu2 = True
            jump ep03_dialogues2_college_19_loop
        "[mcname]." if ep03_dialogues2_college_19_menu1 == True and ep03_dialogues2_college_19_menu2 == True:
            pass
    # девочки выжидающе смотрят на Барди
    imgf 910889
    w
    imgd 910886
    student_abby "[mcname], твоя очередь задавать вопросы..."
    bardi "..."
    imgd 910890
    bardi "Вопрос к Кэти."
    student_katie "Я вся во внимании, хи-хи..."
    # можно будет выбрать только один пункт меню
    menu:
        "Как часто ты занимаешься онанизмом?":
            imgd 910892
            bardi "Как часто ты занимаешься онанизмом?"
            bardi "Правда или действие?"
            # Кэти проводит рукой по своему бедру
            imgf 910901
            w
            imgd 910902
            w
            imgf 910891
            student_katie "Часто... А еще Эбби очень любит мне помогать с этим..."
            student_katie "Хочешь посмотреть на это?"
            bardi "Да..."
            # Кэти смотрит на Эбби
            imgd 910885
            student_katie "Пошалим немного в присутствии [mcname]?.."
            student_abby "Да, меня это так возбуждает. Иди сюда..."
            # Эбби наклоняется к своей подружке и они целуются
            music Stylish_Hip_Hop_Rock
            imgf 910893
            sound2 snd_longkiss1
            bardi_t "Охрененно!"
            imgd 910894
            w
            imgd 910895
            w
            sound snd_longkiss1
            imgf 910896
            w
            imgd 910897
            w
            sound lick3
            imgd 910896
            w
            imgd 910898
            w
            sound lick3
            imgd 910899
            w
            imgd 910900
            w
            # при этом Эбби трогает грудь Кэти, приспуская бра
            # потом она опускает руку ниже и запускает ее в трусики
            # Кэти начинает стонать
            imgf 910903
            w
            sound Jump1
            img 910904 hpunch
            w
            imgf 910905
            w
            sound vjuh3
            img 910906 vpunch
            student_katie "Ооох... Мне очень нравится, когда ты делаешь так, Эбби..."
            imgd 910907
            student_katie "Мммм..."
            # Эбби остраняется от ее губ и начинает целовать грудь, снимает бра
            imgd 910908
            w
            imgf 910909
            w
            imgd 910910
            w
            imgd 910911
            w
            imgd 910912
            sound ahhh13
            student_katie "О, как же клево!.."
            student_katie "Прикуси мой сосок своими зубками..."
            imgf 910913
            w
            sound lick3
            imgd 910914
            w

            # video
            # v_MC_Classmate_Nicole2_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Classmate_Nicole2_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Classmate_Nicole2_25 = Movie(play="video/v_MC_Classmate_Nicole2_25.mkv", fps=25)
            show videov_MC_Classmate_Nicole2_25
            wclean
            student_katie "Ооо, да!.."
            wclean
            student_katie "Мммм..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Эбби опускается еще ниже и снимает с нее трусики
            # проводит пальцами по ее киске
            imgf 910915
            w
            sound vjuh3
            img 910916 hpunch
            w
            imgf 910923
            w
            imgd 910917
            sound ahhh13
            w
            sound2 snd_longkiss1
            imgd 910918
            w

            # video
            # v_MC_Classmate_Nicole1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Classmate_Nicole1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Classmate_Nicole1_25 = Movie(play="video/v_MC_Classmate_Nicole1_25.mkv", fps=25)
            show videov_MC_Classmate_Nicole1_25
            wclean
            student_katie "Мммм..."
            wclean
            student_katie "Снимай скорее с себя все, Эбби!.."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Эби начинает раздеваться
            # Кэти тем временем поворачивается к Барди
            # он сидит со стояком
            sound highheels_short_walk
            imgf 910919
            student_katie "Тебе нравится смотреть на нас, [mcname]?.."
            imgd 910920
            bardi "Ты еще спрашиваешь? Конечно, нравится!"
            bardi "Но я предпочел бы не просто смотреть..."
            imgd 910921
            sound put_dress
            w
            # Эбби уже разделась и вернулась к своей подруге
            # обе голые лежат перед ним на кровати
            imgf 910922
            student_abby "Тогда чего ты ждешь, красавчик? Иди к нам..."
            pass
        "Тебе нравится вкус спермы?":
            imgd 910892
            bardi "Тебе нравится вкус спермы?"
            bardi "Правда или действие?"
            # Кэти сексуально облизывает губы и прикусывает губу
            imgd 910924
            student_katie "Нравится... Я люблю когда кончают мне на лицо, а я потом слизываю сперму со своих губ..."
            bardi "Оу... А как к этому относится Эбби?"
            imgd 910891
            student_abby "Эбби это очень возбуждает..."
            # Кэти смотрит на Эбби
            imgd 910885
            student_katie "Пошалим немного в присутствии [mcname]?.."
            student_abby "Иди сюда..."
            # Эбби наклоняется к своей подружке и они целуются
            music Stylish_Hip_Hop_Rock
            imgf 910893
            sound2 snd_longkiss1
            bardi_t "Охрененно!"
            # они целуются и одновременно с этим снимают друг с друга всю одежду
            imgd 910894
            w
            imgf 910895
            w
            sound snd_longkiss1
            imgd 910896
            w
            imgd 910897
            w
            sound lick3
            imgd 910896
            w
            imgd 910898
            w
            sound lick3
            imgd 910899
            w
            imgf 910915
            w
            sound vjuh3
            img 910916 hpunch
            w
            imgf 910925
            sound put_dress
            w
            imgd 910926
            w
            imgd 910927
            w
            # Кэти наклоняется и целует соски Эбби, потом отстраняется и говорит Эбби, смотря на стояк Барди
            imgf 910928
            w
            imgd 910929
            w
            imgd 910930
            w

            # video
            # v_MC_Classmate_Nicole3_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Classmate_Nicole3_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Classmate_Nicole3_25 = Movie(play="video/v_MC_Classmate_Nicole3_25.mkv", fps=25)
            show videov_MC_Classmate_Nicole3_25
            wclean
            student_katie "Мммм... Какая у тебя красивая грудь, Эбби."
            wclean
            student_katie "Так люблю целовать твои сосочки..."
            student_abby "О, да..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 910931
            w
            imgd 910932
            student_katie "Эбби, я так хочу почувствовать его член в своей киске!.."
            imgf 910933
            student_katie "Моя киска стала вся влажная от этих мыслей, пока мы играли."
            # они обе голые, ложатся на кровати перед Барди
            imgd 910934
            student_abby "Ты слышал, красавчик? Тебя ждет влажная киска моей подружки..."
            student_abby "Снимай скорей с себя свои джинсы."
            pass
    # Барди встает с постели, звук расстегивающейся ширинки
    # девочки в это время целуются, лежа на кровати
    # Барди бросает джинсы на пол и лезет к ним
    sound step_stairs_short
    imgf 910935
    bardi_t "Сегодня я выиграл джек-пот. Я еще никогда не трахался с двумя девушками."
    sound put_dress
    imgd 910936
    bardi_t "Только во сне..."
    # Эбби тянется к нему за поцелуем
    imgd 910937
    if checkImageShown("img_910857") != False: # арт показывался
        student_abby "Ты отпадно целуешься. Хочу еще..."
    else:
        w
    # поцелуй
    sound snd_walk_barefoot
    imgf 910938
    w
    imgd 910939
    w
    imgd 910940
    student_abby "Мммм..."
    # отстраняется и прикусив губу смотрит на Барди, говоря своей подружке
    imgd 910941
    student_abby "Кэти, ты должна попробовать это..."
    # Кэти с готовностью тянется к Барди
    # они целуются, а Эбби смотрит на них и трогает рукой грудь Кэти
    # Кэти вцепилась в Барди и продолжает целовать его
    imgf 910942
    w
    imgd 910943
    sound snd_longkiss1
    w
    imgf 910944
    w
    imgd 910945
    student_katie "Мммм..."
    # он начинает лапать ее, трогает грудь, попу
    # Эбби в это время перемещает руку на член Барди и водит по нему рукой
    # наконец Кэти отлепляется
    imgd 910948
    w
    sound snd_longkiss1
    imgf 910949
    w
    imgd 910950
    w
    imgd 910951
    w
    sound drkanje5
    imgd 910952
    w
    sound drkanje5
    imgd 910951
    w
    sound drkanje5
    imgd 910952
    w
    sound drkanje5
    imgd 910951
    w
    sound drkanje5
    imgd 910952
    w
    imgf 910945
    w
    imgd 910946
    student_katie "Отпад!"
    student_katie "Уверена, ты трахаешься также клево!"
    imgd 910947
    bardi "Проверим?.."
    student_katie "Да!"
    # она укладывается на кровать, он берет ее а колени и разводит ее ноги в стороны
    # приближает руку к ее киске и вводит в нее пальцы
    imgf 910953
    w
    imgd 910954
    w
    imgd 910955
    w
    sound drkanje5
    imgd 910956
    w
    imgd 910957
    sound ahhh13
    student_katie "Ооох!.."
    # водит ими туда-сюда
    # в это время к нему приближается Эбби и снова берется рукой за его член, облизывается
    imgf 910958
    w
    sound drkanje5
    imgd 910959
    w
    sound drkanje5
    imgd 910958
    w
    sound drkanje5
    imgd 910959
    w
    sound drkanje5
    imgd 910958
    w
    sound drkanje5
    imgd 910959
    w
    imgf 910960
    w
    imgd 910962
    w
    imgd 910961
    student_abby "Давай я пока займусь этим..."
    # опускается и вбирает его член сразу глубоко
    # минет
    imgf 910963
    w
    sound chpok6
    img 910964 hpunch
    student_abby "Мпфх..."
    imgf 910965
    w
    imgd 910966
    w
    imgd 910967
    w
    imgd 910968
    bardi "О, ееее!.."
    sound chpok7
    imgd 910969
    w
    sound chpok9
    imgd 910968
    student_abby "Мммм..."
    # он в это время продолжает двигать пальцами в киске Кэти
    sound chpok7
    imgd 910969
    w
    sound chpok9
    imgd 910968
    w
    imgf 910958
    w
    sound drkanje5
    imgd 910959
    w
    sound drkanje5
    imgd 910958
    w
    sound drkanje5
    imgd 910959
    w

    # video
    # v_MC_Classmate_Nicole4_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Classmate_Nicole4_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Classmate_Nicole4_25 = Movie(play="video/v_MC_Classmate_Nicole4_25.mkv", fps=25)
    show videov_MC_Classmate_Nicole4_25
    wclean
    student_katie "Ааах, я сейчас так кончу!"
    wclean
    student_katie "Я хочу тебя!.. Войди в меня скорее, [mcname]!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910970
    sound ahhh11
    student_katie "Ооох!.."
    # Эбби выпускает его член изо рта и отодвигается
    # Барди направляет член в киску Кэти
    # водит им несколько раз по киске, потом резко и глубоко вводит его
    imgd 910964
    w
    sound chpok9
    imgd 910963
    w
    imgf 910971
    w
    sound drkanje5
    imgd 910972
    w
    imgd 910971
    w
    sound drkanje5
    imgd 910972
    w
    sound lick3
    imgd 910973
    w
    sound chpok6
    img 910974 hpunch
    student_katie "ОООО!!!"
    sound ahhh12
    imgd 910975
    student_katie "ДААА!!!"
    # он берет ноги Кэти и высоко задирает их вверх и разводит в стороны
    imgf 910976
    w
    sound ahhh11
    imgd 910977
    student_katie "Оооо!"
    imgd 910978
    w
    imgf 910979
    w
    imgd 910981
    student_katie "Даа!.."
    sound ahhh12
    imgd 910975
    w

    # video
    # v_MC_Classmate_Nicole5_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Classmate_Nicole5_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Classmate_Nicole5_25 = Movie(play="video/v_MC_Classmate_Nicole5_25.mkv", fps=25)
    show videov_MC_Classmate_Nicole5_25
    wclean
    student_katie "Как же кайфово!"
    wclean
    student_katie "Какой у тебя клевый член!.."
    bardi "Мммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Барди ахает Кэти, а Эбби в этом время ласкает свою киску и смотрит на них
    # потом Эбби говорит Барди
    imgf 910982
    w
    imgd 910983
    student_abby "Переверни ее, [mcname]. Я хочу, чтобы она поработала своим язычком..."
    # Барди выходит из Кэти и ставит ее на четвереньки
    # вводит в нее член и продолжает ахать в этой позе
    imgd 910974
    w
    sound chpok5
    imgd 910973
    w
    fadeblack 1.0
    music Stylish_Hip_Hop_Rock
    imgf 910985
    student_katie "Да-да!"
    imgd 910986
    student_katie "Еще! Хочу еще!"
    imgd 910987
    student_katie "Даа!.."
    # Эбби в этот момент берет ее за голову и прижимает лицом к своей киске, стоя перед ней на коленях с широко разведенными ногами
    imgd 910988
    w
    imgd 910984
    student_abby "О, дааа! Кэти!"
    imgd 910989
    student_abby "Ох, это просто улет!"
    # Кэти вылизывает киску Эбби
    imgf 911000
    w
    imgd 910998
    w
    imgd 910990
    bardi "Чертовски охренительно трахать вас!.."
    imgd 910991
    student_katie "Мпфхфмм!.."
    imgd 910992
    sound ahhh12
    student_abby "Аааа!"
    imgf 910993
    w
    sound drkanje5
    imgd 910994
    w
    sound drkanje5
    imgd 910993
    w
    sound drkanje5
    imgd 910994
    w

    # video
    # v_MC_Classmate_Nicole6_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Classmate_Nicole6_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Classmate_Nicole6_25 = Movie(play="video/v_MC_Classmate_Nicole6_25.mkv", fps=25)
    show videov_MC_Classmate_Nicole6_25
    wclean
    student_katie "Мпфх!.."
    wclean
    student_abby "Оттрахай Кэти! Оттрахай как грязную шлюшку!"
    bardi "О, ееее!.."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910995
    w
    sound lick3
    imgd 910996
    w
    sound lick3
    imgd 910995
    w
    sound lick3
    imgd 910996
    student_abby "Я сейчас кончу!"
    # Эбби кончает
    img 910997
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    student_abby "ААААА!"
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan11
    student_abby "АААААААА!!!"
    imgf 910999
    w
    # следом за ней Кэти, отстранившись от ее киски
    imgd 910987
    student_katie "ООООО!!!"
    img 911001
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan12
    student_katie "ДАААА!!!"
    imgd 911002
    w
    $ mlsBardiDay4College9 = day # Барди на вечеринке ахнул двух подружек
    menu:
        "Кончить на Кэти.":
            # Барди вытаскивает член из киски и бурно кончает на киску Кэти
            imgd 911003
            bardi "Дааа!!!"
            img 911004
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            bardi "Оооо!!!"
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man moan8
            bardi "О, какой кайф..."
            sound2 chpok5
            imgd 911005
            w
            imgd 911006
            student_katie "Мммм..."
            student_abby "Улет!"
            pass
        "Кончить на Эбби.":
            # Барди вытаскивает член из киски Кэти
            imgd 911003
            w
            imgd 911007
            bardi "Эбби, наклонись сюда! Быстро!"
            # она наклоняется и он бурно кончает на ее грудь
            imgd 911008
            bardi "Дааа!!!"
            img 911009
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            bardi "Оооо!!!"
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man moan8
            bardi "О, какой кайф..."
            sound2 chpok5
            imgd 911010
            w
            imgf 911012
            student_katie "Мммм..."
            imgd 911011
            student_abby "Улет!"
            pass
    fadeblack 1.5
    music Stylish_Hip_Hop_Rock
    imgf 911013
    w
    imgd 911014
    w
    # Барди остраняется от Кэти и падает на кровать
    # девчонки обнимают его
    # затемнение - конец v3
    img white_screen
    with Dissolve(2.0)
    w
#    fadeblack 2.0
    return

label ep03_dialogues2_college_20:
    sound Jump1
    img 911223 hpunch
    student_jacob "Чего уставился, придурок?!" # показывает Барди фак и отворачивается
    bardi_t "О, а этот все бухает... Даже после того, как уже оставил 'частичку себя' перед домом."
    bardi_t "Надеюсь, утром этому уроду будет вдвое хуже..."
    return

label ep03_dialogues2_college_21:
    # смотрит на целующуюся парочку на диване
    imgf 911225
    bardi_t "Воу! Нет, им сейчас уж точно не до меня..."
#    bardi_t "Да и два хрена - это хорошо лишь в том случае, когда между ними есть хотя бы одна девушка."
#    bardi_t "Стоп! Это что, девушка?!"
#    bardi_t "Охренеть... Беру свои слова назад."
    return

label ep03_dialogues2_college_22:
    # смотрит на пьяное тело, лежащее у стола
    imgf 911224
    bardi_t "Твою мать, это еще кто? Он живой вообще?"
    bardi_t "Хотя, кому какая разница?.. Он пришел не со мной, а значит мне, как и всем, насрать."
    bardi_t "Знать бы только, чем он так убился?.. Не хотелось бы закончить сегодняшний вечер, как этот тип."
    return

label ep03_dialogues2_college_23:
    # делает комментарий о девочке, которая потом танцует на столе (справа от Элими с Гарри)
    bardi_t "Вау! А она ничего!.."
    bardi_t "Хотя нет... Я еще не настолько пьян, чтобы уводить бабу из центра внимания в толпе бухих парней..."
    return

# в v4 он проснется утром с диким похмельем у себя дома, не помня как пришел домой
