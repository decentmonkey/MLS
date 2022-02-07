default mlsBardiDay4FamilyMorning1 = 0 # Синтия застала Барди в душе
default mlsBardiDay4FamilyMorning2 = 0 # Мистер Райт ждет Барди после колледжа на пляже

#call ep03_dialogues1_family_morning_1() # утро, комната Барди
#call ep03_dialogues1_family_morning_1a() # если заходит в душ
#call ep03_dialogues1_family_morning_2() # при клике на кухню, разговор с Софи
#call ep03_dialogues1_family_morning_3() # телефонный разговор с Софи на перемене в колледже
#call ep03_dialogues1_family_morning_4() # мысли после разговора с Софи по телефону в колледже
#call ep03_dialogues1_family_morning_5() # утро следующего дня, комната Барди
#call ep03_dialogues1_family_morning_6() # при клике на кухню, разговор с Софи

# утро, Барди открывает глаза
label ep03_dialogues1_family_morning_1:
    # звонит будильник
    fadeblack 2.0
    music iphone_alarm
    imgf 900062
    bardi_t "Что, уже утро?!"
    imgd 900065
    bardi_t "Мне такой сон снился... И такой облом на самом интересном месте!.."
    music Jail_Clock
    imgd 900066
    bardi_t "..."
    # в комнату заходит Софи
    sound2 snd_walk_barefoot
    imgf 901076
    music Little_Tomcat
    sophie "[mcname], милый, доброе утро." ##->#####inc
    #####inc mother "Сынок, доброе утро."
    imgd 901077
    bardi "Доброе..."
    # косится на его одеяло
    img 901078 hpunch
    w
    imgd 901079
    sophie "Хорошо, что ты уже проснулся..."
    # потом смотрит на него и мило улыбается
    imgd 901080
    sophie "Я уже приготовила завтрак. Одевайся и приходи на кухню."
    imgd 901081
    bardi "Окей. Сейчас приду."
    # Барди смотрит ей вслед (кадр на ноги Софи или на попу) - далее показать момент неловкости
    sound2 snd_walk_barefoot
    imgf 901082
    music The_Heat
    w
    imgd 901085
    bardi_t "..."
    # на фоне этого кадра голос Софи
    sophie "Милый, поторопись, иначе опоздаешь в колледж..."
    music stop
    sound plastinka1b
    img 901083 hpunch
    bardi_t "Черт!"
    # Барди поднимает глаза на ее лицо (смена кадра с ног (попы) на лицо Софи)
    # она смотрит на него задумчиво
    # неловкая пауза
    sophie "..."
    music Step_By_Step
    imgd 901084
    bardi "Эээм... Да-да, пара минут, Софи." ##->#####inc
    #####inc bardi "Эээм... Да-да, пара минут, ма."
    imgd 901086
    sound snd_walk_barefoot
    w
    fadeblack
    sound snd_walk_barefoot
    pause 1.5
    imgf 901087
    w
    # она снова улыбается ему и выходит из комнаты
    # Барди встает с постели
    # переход на движок
    return

# игрок самостоятельно топает на кухню

# если заходит в душ
label ep03_dialogues1_family_morning_1a:
    # один арт из старых + сделать пару артов, как заглядывает Синтия
    music Adventures_of_the_Deaf_Dreamer
    imgfl 910311
    bardi_t "У меня еще есть время до колледжа, чтобы принять душ..."
    menu:
        "Принять душ.":
            $ mlsBardiDay4FamilyMorning1 = day # Синтия застала Барди в душе
            # кадры стены душа и капли воды, как будто Барди смотрит
            # вид из глаз вниз, видно стояк Барди
            music2 snd_shower3
            imgf 901094
            w
            imgd 900472
            bardi_t "Нужно снять напряжение после такого сна..."
            # кадры из сна с сестрами, где они целуются
            img white_screen
            with diss
            pause 1.0
            music The_Heat
            img 910661
            show screen dream()
            with diss
            w
            sound snd_longkiss1
            img 910660
            show screen dream()
            with diss
            bardi_t "Это выглядит чертовски возбуждающе..."
            img 910659
            show screen dream()
            with diss
            bardi_t "Увидеть бы такое на самом деле, а не во сне..."
            # сменяется кадром на сток Барди, он водит рукой по нему
            imgf 900472
            bardi_t "..."
            sound drkanje5
            imgd 900473
            w
            sound drkanje5
            img 900474
            w
            sound drkanje5
            imgd 900473
            w
            sound drkanje5
            imgd 900472
            w
            # внезапно дверь открывается и в ванную комнату заходит Синтия в домашнем аутфите
            # только после того, как зашла, она замечает, что Барди в душе
            sound snd_door_open1
            sound2 snd_walk_barefoot
            img 901095 vpunch
            bardi_t "!!!"
            # она смотрит на него, округлив глаза
            music stop
            sound plastinka1b
            img 901096 hpunch
            sound2 fear1
            cynthia "ОЙ!"
            # потом резко прикрывает глаза руками
            music Adventures_of_the_Deaf_Dreamer_short
            sound2 Jump1
            img 901097 vpunch
            cynthia "Ой, прости, [mcname]! Я не знала, что ты тут!.."
            # смущенная Синтия выбегает из ванной комнаты
            sound step_stairs
            imgd 901098
            cynthia "!!!"
            # Барди смотрит на свой стояк
            sound2 snd_door_open1
            music Adventures_of_the_Deaf_Dreamer
            imgf 901099
            bardi_t "Фак! Неудобно вышло."
            bardi_t "Может, она не заметила, что я дрочил?.."
            # если смотрел ТВ с Синтией
            if mlsBardiDay3FamilyEvening4 == 0:
                img 901099
                bardi_t "Как и вчера не заметила, что у меня дымилось все в штанах."
            imgd 901100
            bardi_t "Было бы прикольно, если бы Синтия могла присоединиться ко мне и..."
            bardi_t "..."
            bardi_t "Черт! Мне определенно нужна разрядка..."
            # снова берется рукой за член
            imgd 900473
            bardi_t "..."
            # затемнение, шум воды стихает
            music2 stop
            pass
        "Позже.":
            imgd 910311
            bardi_t "Я пока не хочу принимать душ."
            pass
    fadeblack 1.5
    return

# двери в комнаты сестер и спальню Софи закрыты

# при клике на кухню
label ep03_dialogues1_family_morning_2:
    # на столешнице или столе стоит стакан с водой
    # Барди заходит на кухню
    # Софи стоит на кухне, на столе завтрак, как обычно
    # озадаченно смотрит на него, потом опускает глаза
    fadeblack 1.5
    sound2 step_stairs
    music Little_Tomcat
    imgfl 901101
    w
    imgf 901102
    w
    imgd 901103
    sophie "Вот твой завтрак, милый."
    imgd 901102
    bardi "Ага. Спасибо."
    bardi "Вы с Генри вчера поздно вернулись?"
    imgd 901104
    sophie "Да, поздно ночью. Ты и девочки уже спали..."
    sophie "Как прошел вечер? Чем занимались?"
    imgd 901102
    bardi "Да вроде все окей было. Ничем таким не занимались..."
    imgd 901105
    sophie "Точно?" # пристальный взгляд
    music Postcard_From_Hell
    imgd 901106
    bardi_t "Фак. Почему она так заинтересована вчерашним вечером?"
    # если делал массаж ног Оливии
    if mlsBardiDay3FamilyEvening5 == 0:
        #
        $ notif(_("[mcname] делал массаж ног пьяной Оливии."))
        #
#        img 901106
        bardi_t "Это же был просто массаж ног Оливии. Ничего такого."
        if mlsBardiDay3FamilyEvening3 > 0:
            bardi_t "Ну почти..."
    # если смотрел ТВ с Синтией
    if mlsBardiDay3FamilyEvening4 == 0:
        #
        $ notif(_("[mcname] смотрел фильм с Синтией."))
        #
#        img 901106
        bardi_t "И в просмотре фильма с Синтией я ничего криминального не вижу."
        # если смотрели ужастики
        if mlsBardiDay3FamilyEvening1 > 0:
#            img 901106
            bardi_t "За исключением одного момента... Но о моем внезапном стояке знаю только я. Или Синтия что-то заметила и рассказала Софи?.."
        # если смотрели боевик
        else:
#            img 901106
            bardi_t "За исключением одного момента... Но не могла же Синтия рассказать Софи про порнуху? Или могла?.."
    # Софи перебивает его размышления, также пристально глядя на него
    imgd 901105
    sophie "[mcname], у нас во дворе валяются пустые бутылки из-под алкоголя."
    sophie "Это ты с друзьями отдыхал?"
    imgd 901106
    bardi "Бутылки во дворе?"
    bardi "Нет, я тут ни при чем."
    imgd 901107
    sophie "Может, кто-то из девочек? Синтия?"
    sophie "Ты не замечал ничего странного в ее поведении вчера?"
    imgd 901108
    bardi "Эээм..."
    # в это время на кухню заходит Оливия в домашнем аутфите
    # волосы растрепаны, на лицо все признаки похмелья, держится за голову
    # Софи удивленно смотрит на нее
    music Adventures_of_the_Deaf_Dreamer
    imgf 901109
    sound2 snd_walk_barefoot
    w
    imgd 901110
    sophie "Оливия? Что-то ты сегодня рано встала..."
    img 901111
    olivia "Пфф..."
    # Оливия проходит на кухню и хватает стакан с водой, начинает жадно пить
    sound snd_walk_barefoot
    imgf 901112
    sound2 ahhh13
    sophie "Дорогая, с тобой все в порядке?"
    sophie "Ты себя плохо чувствуешь?"
    sound snd_drinking_water
    imgd 901113
    w
    imgd 901114
    w
    # ставит стакан обратно на столешницу или стол
    sound snd_glass_table
    imgd 901115
    olivia "Я в порядке!.."
    # если был массаж ног
    if mlsBardiDay3FamilyEvening5 == 0:
        # Оливия зло рявкает на Барди
        sound Jump1
        img 901116 hpunch
        olivia "Чего ты уставился, придурок?!"
        imgd 901117
        bardi "Эй-эй, полегче!"
        bardi_t "Да уж... Вчера, пьяной и сонной, Оливия мне нравилась гораздо больше."
        # Софи возмущенно
        img 901118
        sophie "Оливия! Прекрати так разговаривать с [mcname]!" ##->#####inc
        #####inc mother "Оливия! Прекрати так разговаривать с братом!"
        # Оливия отмахивается от Софи
    sound snd_walk_barefoot
    imgf 901119
    olivia "Ой, все! Пойду еще посплю."
    # Оливия выходит из кухни
    # Софи, проводя ее взглядом, поворачивается к Барди
    # она обеспокоена
    fadeblack 1.0
    music Little_Tomcat
    imgf 901120
    sophie "Мне показалось или Оливии не здоровится?"
    imgd 901121
    bardi "Похоже, у кого-то дикое похмелье..."
    imgd 901122
    sophie "Теперь понятно, кто разбросал пустые бутылки по двору..."
    sophie "Странно. Она ведь говорила вчера, что проведет время с Марком."
    sophie "У них что-то случилось? Они поругались?"
    imgd 901123
    bardi "Я не в курсе, Софи." ##->#####inc
    #####inc bardi "Я не в курсе, мам."
    bardi "Оливия не особо делится со мной своими переживаниями..."
    imgd 901120
    sophie "Ох, ну ладно. Я поговорю с ней сегодня."
    sophie "И, несмотря на дикое похмелье, кое-кому придется убираться во дворе."
    imgd 901121
    bardi "Я ей не завидую."
    # Софи улыбается
    imgd 901124
    sophie "Тебе пора в колледж, [mcname]. Иначе ты опоздаешь на занятия."
    # она протягивает руку и гладит его по волосам
    # смотрят друг на друга
    imgf 901125
    sophie "..."
    imgd 901126
    sophie "Хорошего тебе дня, милый."
    imgd 901127
    bardi "Спасибо, Софи. И тебе хорошего дня." ##->#####inc
    sound snd_walk_barefoot
    imgf 901128
    #####inc bardi "Спасибо, ма. И тебе хорошего дня."
    w
    # Софи убирает руку, улыбается ему и отворачивается к столешнице
    # квест-лог "Идти в колледж."
    return

# при повторном клике на Софи, если уже разговаривали - ep01_dialogues3_day2_family_5 (регулярный разговор)

# после урока инглиша, в перерыве между занятиями, у Барди звонок на телефон
# телефонный разговор с Софи
label ep03_dialogues1_family_morning_3:
    ## не рендерить!
    sophie "[mcname], милый, я тебя не отвлекаю?"
    bardi "Нет. У меня как раз перерыв между занятиями. Что-то случилось?"
    sophie "Мне сейчас позвонил Генри. Мистер Райт сегодня заезжал к нему на работу."
    sophie "Генри поговорил с ним насчет твоей подработки."
    bardi "О, ну хорошо. Что этот Райт сказал?"
    sophie "Он согласен взять тебя к себе в помощники."
    sophie "Мистер Райт сказал, что сегодня ближе к вечеру он будет на пляже."
    sophie "Так что, если для тебя все еще актуальна подработка, то можешь после колледжа встретиться с ним."
    bardi "Это отличная новость. Спасибо, Софи!" ##->#####inc
    #####inc bardi "Это отличная новость. Спасибо, ма!"
    sophie "Не за что, милый."
    sophie "Удачно провести встречу с мистером Райтом."
    sophie "Да, и постарайся не задерживаться. К нам в гости сегодня придет моя сестра."
    sophie "Так что мы будем тебя ждать к ужину."
    bardi "Окей. Договорились."
    sophie "До вечера, милый."
    bardi "Пока."
    $ mlsBardiDay4FamilyMorning2 = day # Мистер Райт ждет Барди после колледжа на пляже
    return

# мысли после разговора с Софи по телефону
label ep03_dialogues1_family_morning_4:
    ## не рендерить!
    bardi_t "Ееее! Подработка - это то, что нужно!"
    bardi_t "Буду работать по максимуму, чтобы быстрее накопить денег и свалить из этой дыры!"
    return

######################### утро следующего дня (Day5)

label ep03_dialogues1_family_morning_5:
    # звонит будильник
    fadeblack 2.0
    music iphone_alarm
    imgfl 901088
    bardi_t "Очередное утро в этой дыре..."
    bardi_t "Хорошо хоть, что сегодня выходной и не нужно тащиться в гребаный колледж."
    bardi_t "..."
    music Visions_Of_Plenty
    imgf 900457
    bardi_t "Круто, что мои дела уже налаживаются!.."
    bardi_t "Появились варианты подработки."
    bardi_t "Нужно будет сходить в этот прокат великов..."
    bardi_t "А потом загляну к Дейзи... Чтобы обсудить условия работы у нее. Возможно, она предложит что-то более высокооплачиваемое..."
    bardi_t "Скоро я начну зарабатывать и, наконец-то, смогу начать копить деньги..."
    # голос Софи из-за двери
    imgd 901089
    sophie "[mcname], ты уже встал?" ##->#####inc
    #####inc mother "Сынок, ты уже встал?"
    bardi "Да!"
    sophie "Доброе утро, милый! Спускайся к завтраку."
    bardi "Ага, сейчас приду!"
    fadeblack
    sound snd_walk_barefoot
    pause 1.5
    imgf 901087
    w
    # Барди встает с постели
    # переход на движок
    return

# если заходит в душ - стандартный лейбл ep01_dialogues2_day1_family_1_14

# при клике на кухню
label ep03_dialogues1_family_morning_6:
    # Барди заходит на кухню
    # Софи стоит на кухне, на столе завтрак, как обычно
    fadeblack 1.5
    sound2 step_stairs
    music Little_Tomcat
    imgf 900055
    sophie "Привет, [mcname]. Вот твой завтрак."
    imgd 900056
    bardi "Хорошо. Спасибо, Софи." ##->#####inc
    #####inc bardi "Хорошо. Спасибо, ма."
    imgd 900057
    sophie "Какие планы у тебя на сегодня, милый?"
    imgd 900058
    bardi "Думаю, сходить в велопрокат мистера Райта. Ознакомиться с работой, так сказать."
    imgd 900057
    sophie "Отлично, милый. А потом?"
    sophie "Не забудь, тебя сегодня вечером будет ждать Дейзи."
    imgd 900056
    bardi "Да, я планировал зайти к ней."
    imgd 901090
    sophie "Я рада, что у тебя появилась возможность немного подзаработать."
    imgd 900056
    bardi "Да, это круто."
    bardi "Ну, я пошел. Сегодня много дел."
    # Софи проводит рукой по его волосам и улыбается ему
    imgf 901091
    w
    imgd 901092
    sophie "Хорошего тебе дня, милый."
    imgd 901093
    bardi "Спасибо, Софи. И тебе хорошего дня." ##->#####inc
    sound snd_walk_barefoot
    imgf 900470
    w
    #####inc bardi "Спасибо, ма. И тебе хорошего дня."
    # Софи убирает руку, улыбается ему и отворачивается к столешнице
    # квест-лог "Идти в велопрокат."
    return
