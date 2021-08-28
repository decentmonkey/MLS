label gallery_33039:
    # Моника с Филиппом заходят в комнату
    # серая мышь сидит в клетке
    # Моника сначала ее не замечает
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Master_Disorder
    imgfl 33027
    w
    img 33028 vpunch
    w
    imgd 33029
    philip "Проходите, Миссис Бакфетт."
    philip "Я давно уже задумывался о том, чтобы показать вам подвал своего дома."
    # Моника с отвращением оглядывается
    imgf 33169
    w
    img 33031 vpunch
    mt "!!!"
    img 33032 vpunch
    mt "!!!!"
    imgd 33033
    mt "Что это за ужасное место?!"
    mt "Это... Это что, место для извращений?!"
    mt "О Боги!!!"
    imgd 33030
    mt "Какие-то кошмарные механизмы!"
    mt "Он больной на всю голову извращенец!"
    mt "Моника, он опасен!!!"
    fadeblack 1.5
    music Groove2_85
    imgf 33034
    philip "Миссис Бакфетт, я вижу замешательство на вашем лице."
    philip "Вам совершенно не о чем беспокоиться."
    img 33035
    mt "Неужели?!"
    mt "!!!"
    imgd 33036
    philip "Для начала я хочу познакомить вас с этим..."
    philip "Уверен, вы будете заинтересованы, Миссис Бакфетт."
    # он подходит к клетке и открывает ее
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 33037
    sound snd_jail_door_locked
    w
    # из клетки на четвереньках выползает серая мышь, которая проводила кастинг перед Мелани
    # она подползает к ногам Филиппа и встает на колени перед ним, голова опущена, руки за спину, взгляд в пол
    sound snd_jail_door
    fadeblack 2.0
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 33038
    w
    imgf 33170
    sound barefoot_walk2
    w
    imgd 33171
    w
    # добавить мысли Моники "Я ее знаю!"
    sound snd_barefoot3
#    sound snd_walk_barefoot
    imgf 33039
    w
    imgd 33040
    w
    imgf 33041
    model1 "Этот раб готов выполнять приказы Мастера."
    # Моника смотрит на нее в потрясении
    music stop
    sound plastinka1b
    img 33042 hpunch
    mt "О БОЖЕ!!!"
    mt "!!!"
    music Power_Bots_Loop
    mt "Я ее знаю!"
    # если был кастинг с серой мышью перед Мелани
    if monicaMelanieCastingLickedDildo == True:
        #
        $ notif(_("Моника проходила кастинг перед серой мышью и Мелани."))
        #
        imgd 33043
        mt "Это та мерзкая серая мышь!"
        mt "Она унизила меня перед Мелани!"
        mt "Гребаная мартышка!!!"
        mt "Ненавижу ее!!!"
    # если кастинга с Мелани не было
    else:
        #
        $ notif(_("Моника проводила кастинг для моделей журнала."))
        #
        imgd 33042
        mt "Это же одна из мартышек, которые приходили на кастинг в мой журнал!!!"
        #
    mt "Какого черта она тут делает?!"
    mt "Почему она в таком виде?!"
    mt "Я ничего не понимаю!!!"
    mt "!!!"
    # Филипп обращается к серой мыши
    fadeblack 1.5
    music Groove2_85
    imgf 33044
    philip "Оно сейчас поползет к своей миске."
    philip "Мастер разрешает ему поесть..."
    model1 "Этот слуга рад исполнить волю Мастера."
    philip "Оно будет молчать, пока Мастер не разрешит ему говорить."
    philip "Если оно все поняло, пусть оно кивнет."
    # мышь кивает, глядя в пол
    imgd 33045
    w
    img 33046
    w
    img 33045
    w
    imgd 33047
    philip "Выполняй приказ Мастера."
    philip "Когда оно поест, пусть ждет возле миски."
    philip "Мастер позовет его, когда сочтет нужным."
    # мышь на коленях ползет к миске с едой (кошачей-?)
    # при этом смотрит не в пол, а бросает взгляд на Монику
    sound snd_barefoot3
    imgf 33048
    model1 "!!!"
    m "!!!"
    # Филипп это видит и рявкает на нее
    music Power_Bots_Loop
    img 33049 hpunch
    philip "Оно должно смотреть в пол!"
    philip "Оно ослушалось приказа Мастера!"
    philip "После того, как уйдет наш гость, оно будет высечено плетью!"
    # мышь быстро опускает голову
    # Моника с ужасом наблюдает за этим
#    music Power_Bots_Loop
    img 33051 hpunch
    mt "Он садист!!!"
    mt "!!!"
    # Филипп обращается к мыши
    fadeblack 1.5
    music Groove2_85
    imgd 33050
    philip "Теперь Мастер позволяет ему ползти к миске."
    # мышь встает на четвереньки, ползет к миске и начинает есть
    sound snd_barefoot3
    imgf 33053
    w
    imgd 33054
    sound cat_eating
    w
    imgd 33055
    w
    music Power_Bots_Loop
    img 33052 vpunch
    mt "О Боже!"
    mt "Она что, будет есть корм для животных?!"
    mt "Фууу!"
    # Филипп подходит к Монике
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgf 33056
    philip "Миссис Бакфетт, на вас лица нет."
    philip "Вы хорошо себя чувствуете?"
    m "Д-да..."
    imgd 33057
    philip "Я немного отвлекся от нашего с вами разговора, Миссис Бакфетт."
    m "Д-да..."
    # Филипп отходит к той штуке, на которой потом распнет Монику
    sound man_steps
    imgf 33058
    w
    imgd 33059
    philip "Подойдите ко мне, Миссис Бакфетт."
    menu:
        "Подойти к Филиппу.":
            pass
    sound highheels_short_walk
    imgf 33060
    m "..."
    imgd 33061
    philip "Вы знаете, я был приятно удивлен..."
    philip "Что вы приготовили такой приятный презент для ваших инвесторов."
    philip "В число которых я тоже могу войти..."
    imgf 33062
    philip "Вернее, не вы приготовили, а Биф."
    philip "Думаю, что вы, Миссис Бакфетт, были удивлены не меньше остальных, услышав об этом?"
    m "..."
    imgd 33063
    philip "Полагаю, что этот номер журнала, вышедший ограниченным тиражом..."
    philip "Будет весьма интересен."
    philip "И не только мне..."
    m "!!!"
    imgf 33064
    philip "Я подумал, что если размещу этот номер в публичный доступ..."
    philip "То смогу получить от этого много удовольствия."
    philip "Пикантные фотографии леди Миссис Бакфетт."
    imgd 33065
    philip "Как вы считаете, хороший заголовок?"
    philip "Под такую публикацию даже можно создать свой журнал."
    philip "Он мигом наберет популярность на весь мир..."
    music Power_Bots_Loop
    img 33066
    mt "О, нет!!!"
    mt "Вот сволочь!!!"
    mt "Я должна отговорить его!"
    mt "Нельзя допустить, чтобы мои фотографии..."
    mt "Чтобы ТАКИЕ мои фотографии увидела общественность!"
    mt "!!!"
    menu:
        "Попытаться отговорить Филиппа.":
            pass
    music Groove2_85
    imgd 33067
    m "..."
    m "Филипп, я хотела бы попросить вас не делать этого..."
    philip "Да?"
    philip "Почему же?"
    m "Эти фотографии..."
    m "Они только для ограниченного круга людей."
    m "И не предназначены для общественности."
    imgf 33068
    philip "Сама Миссис Моника Бакфетт меня просит об одолжении?"
    m "Да, Филипп."
    philip "Хммм... Как же поступить?"
    philip "Я потратил сегодня немаленькую сумму, чтобы спасти вас..."
    philip "И увезти из отеля."
    imgd 33069
    philip "А я не сторонник бесполезного разбрасывания деньгами, Миссис Бакфетт."
    philip "Вы ведь знаете, что не стоите столько, сколько я сегодня за вас заплатил."
    m "!!!"
    imgf 33070
    philip "Я мог бы компенсировать потраченные деньги удовольствием от публикации ваших фотографий..."
    philip "Но раз вы меня просите не делать этого."
    philip "А я джентельмен. Я не смею отказывать просьбе такой леди, как вы."
    philip "Так что же мне делать?"
    imgd 33071
    philip "Может, мне стоит вернуть вас в отель?"
    philip "И пусть все узнают, кто вы на самом деле."
    philip "И где работаете..."
    # Моника с ужасом смотрит на него
    img 33072
    w
    imgd 33073
    philip "Вечеринка там в самом разгаре, Миссис Бакфетт."
    philip "И вы присоединитесь к ней..."
    music Master_Disorder
    philip "Либо вам придется отработать потраченные мною деньги."
    m "Отработать?!"
    m "?!"
    imgd 33074
    philip "Да, Миссис Бакфетт, вы сейчас разденетесь и залезете на это..." # показывает рукой на штуку, где будет пялить Монику
    philip "И отработаете деньги, которые я за вас заплатил."
    m "..."
#    $ menu_corruption = [monicaPhilipBDSMCorruptionRequired1, 0]
    menu:
        "Согласиться.":
#            $ monicaBiffInvestorsPhilip2 = day # Моника согласилась отработать в БДСМ-ной комнате у Филиппа
            pass
        "Убежать! (Филипп запомнит это)":
            label gallery_33076:
            music Master_Disorder
            imgd 33066
            mt "Я не собираюсь тут оставаться ни секунды!"
            mt "И ни в какой отель он меня не повезет обратно!"
            mt "Пошел к черту этот гребаный садист!!!"
            mt "Мерзкое животное!!!"
            music Pyro_Flow
            imgf 33075
            m "Нет! Я не буду делать этого!!!"
            m "Только попробуй сделать это и я убью тебя, клянусь!"
            img 33076
            philip "Аха-ха!"
            philip "Хорошо, Миссис Бакфетт, я не буду делать этого..."
            philip "Прямо сейчас..."
            m "!!!"
            fadeblack
            sound highheels_run2
            pause 2.0
            # Моника убегает, затемнение
            return
    # Моника в растерянности
    imgd 33077
    mt "Залезть на эту штуку?!"
    mt "Чтобя Я, Моника Бакфетт, леди из высшего общества..."
    mt "Отрабатывала деньги какого-то жалкого жадного извращенца?!"
    # бросает взгляд на мышь, та уже поела и сидит возле миски на коленях, сложив руки за спину, голова вниз
    imgf 33078
    mt "Он что, совсем ненормальный?!"
    mt "Как он это себе представляет?!"
    mt "?!?!?!"
    mt "Черт..."
    imgd 33079
    mt "А вдруг он не блефует и правда увезет меня обратно в отель, если я откажусь сейчас?"
    mt "Заведет в номер, где Биф и инвесторы развлекаются с этими проститутками..."
    mt "И скажет им, что купил МЕНЯ!!!"
    mt "Что обо мне тогда подумают эти никчемные инвесторы?!"
    mt "!!!"
    img 33066
    mt "Я не могу допустить этого!"
    music Groove2_85
    imgf 33080
    m "Филипп, я..."
    philip "Полагаю, вы согласны, Миссис Бакфетт?"
    m "Я не готова лезть на эту... эту штуку."
    m "Может, есть какой-то другой способ?"
    philip "Есть, Миссис Бакфетт."
    imgd 33081
    philip "Вы можете не делать этого..."
    philip "Но в таком случае ваши фотографии увидит общественность..."
    m "!!!"
    # Филипп снова указывает рукой на эту штуку
    music Master_Disorder
    imgd 33082
    philip "Прошу вас, Миссис Бакфетт..."
    philip "Для начала вам нужно снять ваше платье."
    menu:
        "Раздеться.":
            pass
    # Моника зло
    imgd 33083
    mt "Дьявол!"
    mt "Я не могу допустить, чтобы эти фотографии увидели все!"
    mt "И ни в коем случае нельзя допустить, чтобы инвесторы и Биф узнали..."
    mt "Что я имею отношение к ВИП-эскорту!"
    mt "В таком случае, мою репутацию ничего не спасет!"
    mt "!!!"
    # затемнение, шуршание одежды
    # Моника голая, в одних каблуках, стоит возле Филиппа
    # косится на мышь, которая продолжает стоять возле миски
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 33084
    w
    imgf 33086
    w
    imgd 33085
    w
    imgf 33087
    mt "Эта серая мышь будет смотреть на меня?!"
    mt "?!?!?!"
    # вопросительно смотрит на мышь, потом на Филиппа
    # тот видит ее замешательство и ехидно улыбается
    imgd 33088
    w
    imgd 33089
    w
    imgf 33090
    philip "Прошу..." # жест рукой в сторону штуки
    # Моника кладет руку на штуку, куда ее просит залезть Филипп, и ставит на нее ногу
    # залезает
    fadeblack 1.5
    music Master_Disorder
    imgf 33091
    w
    imgd 33092
    w
    fadeblack
    sound swish
    pause 2.0
    music Master_Disorder
    imgfl 33093
    sound metal_slide
    philip "Руку сюда..." # закрепляет
    imgf 33094
    sound metal_slide
    philip "Теперь ваши ножки..." # закрепляет
    fadeblack 1.5
    music Master_Disorder
    imgfl 33095
    philip "Отлично, Миссис Бакфетт."
    # Моника раскоряченная, на лице страх
    mt "Боже, это какой-то кошмарный сон!"
    imgf 33096
    mt "Не верю, что это все происходит наяву!"
    imgd 33097
    mt "Скоро я проснусь в своей кровати и сон развеется!"
    mt "!!!"
    # Филипп приспускает штаны и подхоит к Монике сзади
    # нацеливает член на ее киску
    imgf 33098
    w
    label gallery_33129:
    fadeblack
    sound snd_fabric1
    pause 1.5
#    music Loved_Up
    music Master_Disorder
    imgfl 33099
    philip "Миссис Бакфетт, леди из высшего общества..."
    imgf 33100
    philip "Любой из ваших инвесторов хотел бы оказаться сейчас на моем месте."
    # Филипп водит членом туда-отсюда
    imgd 33101
    w
    sound lick3
    imgd 33102
    w
    imgd 33103
    w
    sound lick3
    imgd 33104
    w
    imgd 33101
    w
    imgf 33105
    philip "Миссис Бакфетт, о как же прекрасно вы смотритесь!"
    philip "Знаете, вы хорошо вписываетесь в интерьер этой комнаты."
    philip "Помните, я говорил, что не использую одну и ту же женщину повторно?"
    imgd 33106
    philip "Вы удостоились великой чести, Миссис Бакфетт..."
    philip "И сегодня я...."
    # а потом хоп и нацеливается на анус
    mt "!!!" # шок, испуг
    imgf 33100
    philip "Попробую ваш великосветский зад!"
    img 33108
    w
    fadeblack 1.5
    music Power_Bots_Loop
    img 33107 hpunch
    m "ЧТО?!"
    m "НЕТ!"
    m "Филипп, не надо!"
    imgd 33109
    philip "О, как же хорошо вас распялить, Миссис Бакфетт!"
    philip "Я не мог не воспользоваться шансом!"
    fadeblack 1.5
    music Master_Disorder
    # начинает медленно вводить головку члена, Моника в ужасе
    imgf 33110
    w
    imgd 33111
    w
    music Power_Bots_Loop
    img 33107 hpunch
    m "Нет-нет!"
    m "Я никогда такого не делала!"
    # он игнорирует ее и вводит головку члена еще чуть-чуть
    music Master_Disorder
    imgf 33111
    w
    sound hlup25
    imgd 33112
    w
    imgf 33115
    philip "Какая тугая у вас дырочка, Миссис Бакфетт..."
    philip "Ммммм..."
    philip "Мне приятно лишать вас анальной девственности."
    m "Филипп, не надо!!!"
    m "!!!"
    imgd 33100
    philip "Получается, я первый, кто это сделает..."
    # и еще чуть-чуть
    imgf 33112
    w
    sound hlup25
    img 33113 hpunch
    w
    imgf 33116
    philip "Мммм..."
    philip "А помните, когда вы только начали работать над своим журналом..."
    philip "Я подходил к вам на одном из модных показов?"
    philip "Я тогда искренне был заинтересован в вашей персоне, Миссис Бакфетт."
    imgd 33106
    philip "Это было так давно..."
    philip "Но вы мне ответили грубостью и высокомерием."
    philip "Даже не захотели разговаривать со мной."
    m "Я не помню!"
    m "Вы меня с кем-то путаете!"
    # головка вошла со чпоком, дальше не вводит
    imgf 33113
    w
    sound chpok6
    img 33114 hpunch
    w
    fadeblack 1.5
    music Power_Bots_Loop
    img 33117 hpunch
    m "ААА!!!"
    m "Прекрати! Мне больно!!!"
    imgf 33118
    philip "Зато я все отлично помню, Миссис Бакфетт..."
    philip "Ммммм..."
    m "Филипп, я отменяю нашу сделку!"
    m "Вытащи из меня ЭТО!!!"
    philip "Тогда поедем обратно в отель, Миссис Бакфетт..."
    imgd 33172
    w
    imgd 33173
    w
    # он вынимает полностью член из нее и отходит на шаг назад
    # рассматривает ее голый зад
    imgf 33114
    w
    sound chpok6
    img 33110 hpunch
    w
    fadeblack 1.5
    music Master_Disorder
    imgf 33119
    philip "Скажите мне, что не хотите..."
    philip "Просто скажите..."
    # меню с зацикливанием
#    $ ep217_dialogues5_phillip2_loop1_flag = False
    label gallery_ep217_dialogues5_phillip2_loop1:
    menu:
        "Не надо!!!":
            fadeblack 1.5
            music Power_Bots_Loop
            imgd 33120
            m "Филипп, не делай этого! Мне больно!"
            philip "Скажите, что вы не хотите Миссис Бакфетт."
            philip "И я не буду делать этого."
            menu:
                "Филипп, отпусти меня!":
                    imgf 33121
                    m "Филипп, отпусти меня!"
                    philip "Тогда я буду вынужден отвезти вас обратно в отель..."
                    philip "Пусть все узнают, что вы обычная шлюха, Миссис Бакфетт."
                    jump gallery_ep217_dialogues5_phillip2_loop1
                "У меня болит попа!":
                    imgf 33122
                    m "Филипп, у меня болит попа!"
                    philip "Я сегодня спас эту попу от позорного разоблачения."
                    philip "Ей бы пришлось намного хуже, если бы не мой поступок."
                    menu:
                        "Промолчать": # if gallery_ep217_dialogues5_phillip2_loop1_flag == True:
                            pass
                        "Мне больно!":
#                            $ ep217_dialogues5_phillip2_loop1_flag = True
                            imgd 33119
                            m "Филипп, мне больно!"
                            philip "Вы сами согласились на это, Миссис Бакфетт."
                            jump gallery_ep217_dialogues5_phillip2_loop1
    # Филипп снова подходит и начинает медленно вводить головку в анус
    fadeblack 2.0
#    music Loved_Up
    music Master_Disorder
    imgf 33110
    w
    sound hlup25
    img 33111 hpunch
    w
    fadeblack 1.5
    music Power_Bots_Loop
    img 33107 hpunch
    m "Нет, Филипп, не надо!"
    m "Я не хочу!"
    m "Мне больно!!!"
    imgf 33115
    philip "Инвесторам будет очень интересно увидеть ваше истинное лицо."
    m "Я отменяю сделку! Мне все равно!"
    m "Вези меня обратно в отель!"
    # вводит головку
    imgd 33112
    w
    sound chpok6
    img 33114 hpunch
    w
    fadeblack 1.5
    music Master_Disorder
    imgf 33116
    philip "Вы уверены, Миссис Бакфетт?!"
    philip "Ммммм..."
    # проталкивает член немного дальше, чем в первый раз, но не до конца
    imgd 33114
    w
    sound hlup25
    imgd 33123 hpunch
    w
    fadeblack 1.5
    music Power_Bots_Loop
    img 33125 vpunch
    m "АААА!!!"
    m "Не надо меня насиловать!!!"
    # вводит его еще чуть-чуть, входит не до конца
    imgf 33123
    w
    sound hlup25
    img 33124 hpunch
    w
    imgf 33125
    philip "А я вас и не насилую, Миссис Бакфетт."
    philip "Вы сами ко мне приехали..."
    philip "Сами сюда залезли..."
    philip "Сами согласились отрабатывать уплаченные за вас деньги."
    with hpunch
    m "Нет! Мне больно!"
    m "Прекрати сейчас же!!!"
    # Филипп вытаскивает из нее свой член и снова отходит на шаг, как в прошлый раз
    imgd 33124
    w
    sound chpok6
    img 33110 hpunch
    w
    fadeblack 1.5
    music Master_Disorder
    imgf 33119
    philip "Миссис Бакфетт, попросите меня не вставлять член в ваш зад..."
    philip "Просто скажите это и я не буду делать этого..."
#    $ ep217_dialogues5_phillip2_loop2 = False
    label gallery_ep217_dialogues5_phillip2_loop2:
    menu:
        "Филипп, я не давала согласия на подобное!":
            music Power_Bots_Loop
            imgd 33120
            m "Филипп..."
            m "Я не соглашалась на подобное!"
            philip "Вы сами согласились поехать ко мне домой, Миссис Бакфетт."
            jump gallery_ep217_dialogues5_phillip2_loop2
        "Филипп, джентельмены так не ведут себя!":
            music Power_Bots_Loop
            imgd 33121
            m "Филипп, джентельмены так не ведут себя!"
            philip "С меня достаточно одного джентельменского поступка..."
            philip "Теперь леди благодарит меня за это."
            philip "Ну что скажете, Миссис Бакфетт?"
            fadeblack 1.5
            music Master_Disorder
            imgd 33100
            philip "Вы попросите не вставлять мой член в вашу великосветскую задницу?"
            menu:
                "Промолчать": # if gallery_ep217_dialogues5_phillip2_loop2 == True:
                    pass
                "Мне больно!":
#                    $ ep217_dialogues5_phillip2_loop2 = True
                    music Power_Bots_Loop
                    imgf 33119
                    m "Филипп, мне больно!"
                    philip "Вы сами согласились на это, Миссис Бакфетт."
                    jump gallery_ep217_dialogues5_phillip2_loop2
    # Филипп снова подходит к Монике и пристраивает к ее попе член
    # мышь, пользуясь тем, что Мастер на нее не обращает внимания, вовсю пялится на их секс
    # на лице злорадство над Моникой
    # Филипп снова медленно вводит головку
    fadeblack 2.0
    music Master_Disorder
    imgf 33127
    w
    imgf 33110
    w
    imgd 33111
    w
    sound hlup25
    img 33112 hpunch
    w
    fadeblack 1.5
    music Power_Bots_Loop
    img 33107 hpunch
    m "Прекрати!"
    m "Я дам тебе денег! Только не делай этого!"
    imgf 33109
    philip "Откуда у вас деньги, Миссис Бакфетт?"
    philip "Я прекрасно осведомлен о вашем истинном положении..."
    # головка вошла - чпок
    imgd 33113
    w
    sound chpok6
    img 33114 hpunch
    w
    img 33117 vpunch
    m "НЕЕЕЕТ!"
    fadeblack 1.5
    music Master_Disorder
    imgf 33118
    philip "У вас совсем ничего нет!"
    philip "Кроме этого девственного великосветского зада."
    # медленно проталкивается понемногу
    imgd 33114
    w
    sound hlup25
    img 33123 hpunch
    w
    imgf 33129
    philip "Ммммм..."
    philip "Какая тугая дырочка..."
    m "ААААА!!!"
    # проталкивается еще дальше
    imgd 33123
    w
    sound hlup25
    img 33124 hpunch
    w
    imgf 33128
    philip "Как же приятно трахать зад такой леди, как вы..."
    philip "Даааа..."
    # вводит член до основания
    imgd 33124
    w
    fadeblack 1.5
    music Gearhead
    sound chpok6
    img 33130 hpunch
    w
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_Philip_Anal1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_1= Movie(play="video/v_Monica_Philip_Anal1_1.mkv", fps=30)
    show videov_Monica_Philip_Anal1_1
    with fade
    philip "Вот так..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 33131
    w
    img 33132 hpunch
    m "АААА!!!"
    m "!!!"

    #2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_2= Movie(play="video/v_Monica_Philip_Anal1_2.mkv", fps=30)
    show videov_Monica_Philip_Anal1_2
    with fade
    m "!!!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    # Филипп начинает жарить ее



    imgf 33133
    philip "Даааа..."

    #3
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_3= Movie(play="video/v_Monica_Philip_Anal1_3.mkv", fps=30)
    show videov_Monica_Philip_Anal1_3
    with fade
    philip "Вот это я понимаю..."
    philip "Благодарность леди..."
    m "Нееет!!!" with hpunch
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgd 33134
    philip "Ммммм..."
    philip "Один поступок джентельмена..."

    #4
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_4= Movie(play="video/v_Monica_Philip_Anal1_4.mkv", fps=30)
    show videov_Monica_Philip_Anal1_4
    with fade
    philip "И девственная задница леди в подарок..."
    with hpunch
    m "Хватиииит!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #5
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_5= Movie(play="video/v_Monica_Philip_Anal1_5.mkv", fps=30)
    show videov_Monica_Philip_Anal1_5
    with fade
    model1 "!!!"
    m "!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_6= Movie(play="video/v_Monica_Philip_Anal1_6.mkv", fps=30)
    show videov_Monica_Philip_Anal1_6
    with fade
    philip "Еще ни один член не бывал в этой заднице... Да, я первый... Да..."
    with hpunch
    m "Нееет! Мне больно!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 33131
    philip "Оооо..."

    #7
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_7= Movie(play="video/v_Monica_Philip_Anal1_7.mkv", fps=30)
    show videov_Monica_Philip_Anal1_7
    with fade
    philip "Мммммм... Как же здорово, Миссис Бакфетт..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #8
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_8= Movie(play="video/v_Monica_Philip_Anal1_8.mkv", fps=30)
    show videov_Monica_Philip_Anal1_8
    with fade
    philip "О дааа..."
    with hpunch
    m "Прекрати сейчас же!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #9
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_9= Movie(play="video/v_Monica_Philip_Anal1_9.mkv", fps=30)
    show videov_Monica_Philip_Anal1_9
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 33120 hpunch
    m "ААААА!!!"
    m "Прекрати!!!"
    m "!!!"

    #10
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_10= Movie(play="video/v_Monica_Philip_Anal1_10.mkv", fps=30)
    show videov_Monica_Philip_Anal1_10
    with fade
    philip "Какая тугая у вас дырочка, Миссис Бакфетт... Как же хорошо, да..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #11
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_11= Movie(play="video/v_Monica_Philip_Anal1_11.mkv", fps=30)
    show videov_Monica_Philip_Anal1_11
    with fade
    philip "Оооо! Охренительно! Ааааа!!!"
    with hpunch
    m "!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #12
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Philip_Anal1_12= Movie(play="video/v_Monica_Philip_Anal1_12.mkv", fps=30)
    show videov_Monica_Philip_Anal1_12
    with fade
    model1 "..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    menu:
        "Кончить внутрь Моники.":
#            $ ep217_dialogues5_phillip_cumzone = 1
            imgf 33135
            w
            imgd 33136
            philip "Аааа..."
            imgd 33135
            w
            img 33136
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 33137
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            philip "Аааааааа..."
            imgd 33138
            sound hlup25
            philip "ААААААА!!!"
            fadeblack 1.5
#            imgf 33141
#            w
            scene black
            sound v_Monica_Philip_Anal2_sound_name
            image videov_Monica_Philip_Anal2 = Movie(play="video/v_Monica_Philip_Anal2.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_Philip_Anal2_end.jpg")
            show videov_Monica_Philip_Anal2
            pause 2.0
            wclean
            # кадр на анус Моники, сперма вытекает из нее
            pass
        "Кончить на попу Моники.":
#            $ ep217_dialogues5_phillip_cumzone = 2
            imgf 33135
            w
            imgd 33136
            philip "Аааа..."
            imgd 33135
            w
            img 33136
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 33139
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            philip "Аааааааа..."
            imgd 33140
            philip "ААААААА!!!"
            pass
    # затемнение
    # Моника, распятая висит на штуке, она в шоке от произошедшего
    fadeblack 2.0
    music Master_Disorder
    imgfl 33142
    w
    sound man_steps
    imgf 33143
    w
    imgd 33144
    mt "..."
    mt "ОН БУДЕТ ПЕРВЫМ."
    mt "КОГО Я УБЬЮ!"
    mt "!!!"
    # Моника остается висеть, Филипп все еще со спущенными штанами идет в сторону мыши
    imgf 33145
    mt "..."
#    $ menu_corruption = [monicaPhilipBDSMCorruptionRequired2, 0]
    menu:
        "Смотреть на Филиппа и его рабыню.": # corruption
            # та, видя внимание Мастера, быстро принимает свою стандартную позу
            # Моника поворачивает голову в их сторону, взгляд полон ярости
            imgd 33146
            w
            label gallery_33152:
            music Groove2_85
            imgf 33147
            philip "Оно поело?"
            philip "Отвечай. Мастер разрешает ему говорить."
            model1 "Этот раб благодарит Мастера за еду."
            menu:
                "Продолжить смотреть на рабыню (экстремальный контент, Extra version) (disabled)." if game.extra == False:
                    pass
                "Продолжить смотреть на рабыню (экстремальный контент)." if game.extra == True:
#                    $ monicaBiffInvestorsPhilip5 = day # Моника смотрела, как Филипп унижает мышь (писсинг)
                    imgd 33148
                    philip "Время пить..."
                    philip "Оно не получало сегодня питье."
                    # мышь поднимает голову и открывает рот
                    imgd 33149
                    w
                    # Филипп нацеливается членом и начинает писать ей в рот
                    sound snd_shower
                    img 33150 vpunch
                    w
                    sound snd_piss
                    imgd 33151
                    w
                    # Моника в шоке смотрит на это зрелище
                    sound snd_piss
                    imgd 33152
                    w
                    # после того как Филипп помочился на мышь
                    imgf 33153
                    w
                    imgd 33154
                    sound snd_gulp
                    w
                    # Мышь глотает
                    imgf 33155
                    philip "Оно все выпило?"
                    model1 "Да, Мастер."
                    model1 "Этот раб благодарит Мастера."
                    philip "Оно может ползти в клетку и ждать Мастера для прохождения наказания."
                    philip "Мастер скоро вернется к нему."
                    pass
                "Отвернуться.":
                    # Показать как Моника отвернулась вблизи
                    # звук льющейся жидкости, глотание
                    sound snd_piss
                    imgd 33156
                    mt "Я не могу смотреть на эти извращения!"
                    mt "Это мерзко!"
                    mt "Отвратительно!"
                    mt "Как подобное может нравится нормальному человеку?!"
                    sound snd_gulp
                    mt "Он больной!!!"
                    mt "!!!"
                    # Моника поворачивает голову в сторону Филиппа
                    pass
        "Отвернуться.":
            # Показать как Моника отвернулась вблизи
            #sound Groove2_85
            imgd 33156
            mt "Я не могу смотреть на эти извращения!"
#            sound snd_piss
            mt "Это мерзко!"
            mt "Отвратительно!"
            mt "Как подобное может нравится нормальному человеку?!"
            mt "Он больной!!!"
            sound snd_gulp
            mt "!!!"
            # Моника поворачивает голову в сторону Филиппа
            pass
    # Филипп смотрит на Монику и мерзко улыбается
    # мышь сидит возле его ног в своей стандартной позе
    music Master_Disorder
    imgf 33157
    m "?!"
    m "?!?!"
    m "?!?!?!"
    # затемнение, шуршание одежды
    # Моника с Филиппом стоят в той же комнате, Моника одета
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 33158
    w
    imgf 33159
    philip "Миссис Бакфетт..."
    philip "Я рад, что наша с вами сделка прошла так успешно."
    philip "Вам понравилось?"
    m "!!!" # зло смотрит на него
    # потом переводит взгляд на мышь, она сидит в клетке
    music Power_Bots_Loop
    imgd 33160
    m "Ей это нравится?"
    m "Как человек может терпеть такие унижения?"
    # он ей отвечает, улыбаясь
    music Groove2_85
    imgf 33161
    philip "Деньги, Миссис Бакфетт..."
    philip "Этому существу нравятся деньги..."
    philip "Также как и вам..."
    m "..."
    imgd 33162
    philip "Она заработает $ 10 000 за неделю."
    m "Десять тысяч?!"
    m "?!"
    philip "Да, Миссис Бакфетт."
    imgf 33163
    philip "Но для вас я готов сделать исключение. Ведь я джентельмен."
    philip "Вам я готов заплатить $ 30 000 за неделю."
    philip "За то же самое."
    philip "Что скажете?"
    music Power_Bots_Loop
    img 33164 vpunch
    m "В смысле что я скажу?! Это еще что!?"
    philip "Это предложение, Миссис Бакфетт."
    mt "..."
    menu:
        "Отказаться!":
#            $ monicaBiffInvestorsPhilip3 = day # Моника отказалась быть рабыней у Филиппа
            pass
    # Моника зло
    imgd 33165
    mt "Тридцать тысяч?! За подобное унижение?!"
    mt "Нет! Ни за что!!!"
    mt "!!!"
    mt "Пошел к черту этот гребаный садист!!!"
    mt "Мерзкое животное!!!"
    fadeblack 1.5
    music Groove2_85
    img 33166
    m "Нет!"
    m "Я не готова терпеть подобные унижения ни за какие деньги!!!"
    m "!!!"
    # Филипп продолжает мерзко улыбаться
#    music Groove2_85
    imgf 33071
    philip "Я вам дам немного времени подумать, Миссис Бакфетт."
    philip "И в следующий раз мы вернемся к этому вопросу."
    imgd 33167
    m "Никакого следующего раза не будет!!!"
    mt "Отвратительный мерзкий извращенец!!!"
    mt "Гребаный садист!!!"
    imgf 33168
    philip "Только прежде, чем отказать мне, Миссис Бакфетт..."
    philip "Учтите, что я без этого не буду инвестировать в ваш журнал."
    music stop
    sound plastinka1b
    img 33072 hpunch
    mt "ЧТО?!"
    mt "!!!"
    music Master_Disorder
    imgd 33161
    philip "Это условие моей инвестиции."
    philip "До скорой встречи, Миссис Бакфетт."
    philip "Да, и скажите администратору эскорта что вы только полизали мои яички."
    philip "Я хочу заплатить за эту встречу по минимальному тарифу."
    m "Мерзавец!"
    fadeblack
    sound highheels_run2
    pause 2.0
    # затемнение, каблуки, дверь
    return

### v18

label gallery_42337:
    # показываем, как Бетти с высокомерным видом ходит (!!!) вдоль прилавков
    # проходя мимо прилавков ворчит себе под нос
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 Market
    imgfl 42305
    w
    imgf 42306
    w
    imgd 42307
#    betty "Любую скидку, говорите?"
    betty "Что тут у вас есть?"
    betty "Только рыба?"
    imgd 42308
    salesman "Да, Мэм!"
    salesman "Посмотрите!"
    salesman "Эта сардина только сегодня утром была выловлена из океана!"
    salesman "Также, как и эта! И вообще, вся сардина на этом прилавке наисвежайшая!"
    salesman "Возьмите, я сделаю для вас большую скидку!"
    music Stealth_Groover
    imgf 42309
    betty "Я вообще-то, не за рыбой на рынок приехала!"
    betty "И она не похожа на свежую рыбу!"
    imgd 42310
    salesman "Как не похожа, Мэм?! У меня самая свежая рыба! Свежее здесь не найти!"
    imgd 42311
    betty "У вас дохлая рыба!"
    betty "Поэтому вы и готовы сделать скидку!"
    salesman "Она не дохлая, она просто спит!"
    betty "Я что, по-вашему, не разбираюсь в рыбе?!"
    imgf 42312
    salesman "Нет, Мэм, я такого не говорил."
    salesman "Но это свежая рыба!"
    imgd 42313
    betty "И сколько стоит эта ваша свежая рыба?"
    imgd 42314
    salesman "Со скидкой 15 долларов, Мэм!"
    # Бетти возмущается
    music Pyro_Flow
    img 42315 hpunch
    betty "ЧТО?!"
    betty "15 долларов за дохлую рыбу?!"
    betty "Вы в своем уме?!"
    betty "Вы откуда взяли такие цены на рыбу?!"
    betty "Вы решили, что я ничего не понимаю в продуктах?"
    betty "Не на ту нарвались!"
    imgd 42316
    betty "Я прекрасная хозяйка и ни за что не буду кормить своего мужа этой рыбой!"
    betty "Еще и за 15 долларов!"
    betty "Я сюда приехала за фруктами! Зачем мне рыба?!"
    betty "И вообще! Вы настолько грязный и неопрятный!"
    betty "Я не то, что не купила бы ничего у вас, я вообще держалась бы от вас подальше!"
    # тут к прилавку подходит Лиам, здоровается с продавцом
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 42317
    liam "Эй, Робби! Здорово, дружище!"
    salesman "Привет, Лиам! Как ты?"
    liam "Отлично! На сегодня все в силе, Робби?"
    imgf 42318
    robby "Да, я скоро уже освобожусь. Подождешь немного?"
    imgd 42319
    liam "Без проблем, дружище!"
    # Лиам поворачивается и замечает Бетти
    sound Jump1
    img 42320 vpunch
    liam "Мэм?!" # удивленно
    imgd 42321
    betty "Лиам?" # растерянно
    imgd 42322
    betty_t "Черт! Это же мой сосед!"
    betty_t "Какого черта он тут делает?!"
    betty_t "Не хватало еще, чтобы он увидел меня на каком-то занюханном рынке!"
    imgf 42323
    liam "Мэм, как я рад, что встретил вас здесь!"
    liam "Вы так прекрасно выглядите сегодня!"
    betty "Спасибо, Лиам..." # смущенно
    imgd 42324
    liam "Я не знал, что вы сами ездите на рынок за продуктами."
    liam "Это еще раз подтверждает, какая вы хорошая хозяйка, Мэм!"
    liam "Я могу вам чем-то помочь? По-соседски!"
    music Stealth_Groover
    imgf 42325
    betty "Я даже не знаю, Лиам..."
    betty "Я приехала сюда за фруктами для своего мужа..." # начинает выделываться
    betty "Тут все натуральное, без ГМО..."
    betty "Не то что в супермаркетах в центре..."
    # продавец Робби встревает в их разговор
    music Groove2_85
    img 42326
    robby "О, так вы знакомы?!"
    liam "Да, приятель. Это моя хорошая соседка и замечательная женщина!"
    # Робби показывает на рыбу или держит ее в руках
    sound vjuh3
    imgd 42327
    robby "Мэм как раз собиралась купить у меня эту рыбу."
    robby "Но она еще сомневается."
    robby "Хотя я сделал для нее большую скидку, но, наверное, для нее это тоже дорого..."
    # Бетти смотрит на него прищурившись, но молчит
    img 42328
    betty "!!!"
    imgd 42329
    liam "О, Мэм! Это отличный выбор!"
    liam "У Робби самая свежая рыба на этом рынке!"
    imgf 42330
    liam "Я сам всегда покупаю рыбу только у Робби!"
    robby "Вот видите, Мэм?! Я вам говорил чистую правду!"
    # Бетти задумчиво смотрит на рыбу
    music Hidden_Agenda
    imgd 42331
    betty_t "Хм... Если я сейчас откажусь покупать эту чертову рыбу..."
    betty_t "То Лиам может подумать, что у меня нет денег..."
    betty_t "..."
    menu:
        "Купить рыбу за $ 15.":
            #$ monicaBettyLiamFredMarket2 = day # Бетти купила рыбу
            pass
        "Отказаться. (прерывание квеста)":
            imgf 42332
            betty_t "С другой стороны..."
            betty_t "Я сюда ехала совсем не за этим!"
            betty_t "Зачем мне эта дурацкая рыба?"
            betty_t "Нужно пойти и купить фруктов для мужа."
            music Stealth_Groover
            imgd 42333
            betty "Лиам, я планировала совершить другие покупки."
            betty "Приятно было с вами встретиться, но сейчас мне пора."
            betty "Меня ждет мой муж!"
            liam "Приятно было с вами встретиться! Хорошего вам дня, Мэм!"
            sound highheels_short_walk
            imgf 42334
            w
            music2 stop
            # Бетти уходит
            return
    # Бетти обращается к продавцу
    music Stealth_Groover
    imgf 42335
    betty "15 долларов - это недорого для меня!"
    betty "Я хозяйка богатого дома и могу купить тут абсолютно все!"
    betty "Давайте вашу рыбу!"
    # продавец невозмутимо
    robby "15?! Нееет! Эта рыба стоит 60 долларов, Мэм!"
    # у Бетти шок, она начинает возмущаться
    music stop
    sound plastinka1b
    img 42336 hpunch
    betty "СКОЛЬКО?!"
    betty "Вы говорили, что она стоит 15 долларов!"
    music Groove2_85
    imgd 42337
    robby "Это я говорил про другую рыбу, Мэм."
    robby "Вы, наверное, перепутали."
    robby "Эта рыба стоит 60 долларов."
    imgf 42338
    robby "Я не удивлюсь, если вы откажетесь. Это весьма дорогая рыба!"
    robby "Далеко не каждый себе может ее позволить!"
    betty "Это возмутительно! Вы пытаетесь меня обмануть!"
    robby "Что вы, Мэм! Конечно, нет!"
    # продавец примирительно поднимает руки
    imgd 42339
    robby "Так уж и быть! Я готов сделать для вас большую скидку, Мэм!"
    robby "Я же обещал вам скидку? Я готов уступить вам 30 долларов!"
    robby "Я таких щедрых скидок не делал даже своему дружище Лиаму!"
    robby "Только для вас, Мэм!"
    # Бетти возмущенно смотрит на него, Лиам встревает в их спор
    imgf 42340
    liam "Эй, приятель! Для тебя $ 30 долларов - это большие деньги."
    liam "А для Мэм - это копейки!"
    liam "Ты бы видел, в каком богатом и огромном доме Мэм живет!"
    imgd 42341
    liam "Неужели ты думаешь, что для нее это деньги?! Ха-ха!"
    robby "Я вижу, что Мэм очень богата..."
    # Бетти стоит с надменным видом
    robby "Для такой богатой женщины рыба за $ 30 - это недорого."
    imgd 42342
    betty_t "..."
    menu:
        "Купить рыбу за $ 30.":
            pass
    music Hidden_Agenda
    imgf 42332
    betty_t "Черт! Если я сейчас буду продолжать спорить с этим пропахшим рыбой продавцом..."
    betty_t "То Лиам подумает, что я жадная..."
    betty_t "Или что для меня 30 долларов - это большие деньги..."
    betty_t "А это не так!"
    betty_t "!!!"
    imgd 42343
    betty_t "Я богатая женщина и могу себе позволить купить рыбу за 30 долларов!"
    betty_t "Ведь я делаю это для своего мужа!"
    betty_t "Я приготовлю ему вкусный ужин, как хорошая и хозяйственная жена!"
    # Бетти говорит продавцу
    music Groove2_85
    imgf 42344
    betty "Хорошо, я куплю эту рыбу за 30 долларов!"
    liam "Отличный выбор, Мэм!"
    robby "Да, старина Лиам прав! Это действительно отличный выбор, Мэм!"
    # затемнение
    # возле прилавка Бетти стоит с рыбой в руках, Лиам и Робби возле нее
    # Лиам говорит Бетти, указывая на Робби
    fadeblack 2.0
    music Groove2_85
    imgfl 42345
    liam "Мэм, я рад, что смог помочь вам с покупкой."
    liam "Сейчас нам с Робби пора."
    liam "Я хочу пригласить его к себе, чтобы починить газонокосилку, которую я сломал о забор."
    imgf 42346
    betty "Я тоже сейчас поеду домой. Мне нужно готовить ужин для своего мужа."
    betty "И еще, Лиам... В конце концов, я хотела бы забрать свой утюг!"
    imgd 42347
    liam "Да, конечно, Мэм! Вы можете заодно зайти ко мне за утюгом."
    liam "Кстати, про утюг..."
    liam "А где ваш водитель Фред, Мэм?" # улыбается многозначительно
    imgd 42348
    w
    # Бетти смущенно опускает взгляд
    # продавец удивленно
    imgf 42349
    sound wow
    robby "Ого! У вас есть личный водитель?!"
    # Бетти горделиво вскидывает голову
    music Stealth_Groover
    betty "Да!"
    betty "Он ждет меня на парковке!"
    imgd 42350
    betty "Вы же не думали, что такая богатая женщина, как я, пойдет домой пешком с этой рыбой?"
    music Groove2_85
    imgd 42351
    robby "Нет-нет, Мэм! Конечно, я так не думал!"
    # Бетти высокомерно смотрит на Робби
    imgf 42352
    liam "Мэм... А не могли бы вы... Раз уж Фред ждет вас и вы сейчас поедете к себе домой..."
    liam "Не могли бы вы по-соседски подбросить нас с Робби до моего дома?"
    music Hidden_Agenda
    imgd 42353
    betty_t "Не хватало еще, чтобы этот грязный продавец, от которого воняет рыбой..."
    betty_t "Садился в мою машину!"
    betty_t "Но я не могу отказать в просьбе Лиаму."
    betty_t "Мы ведь хорошие соседи..."
    betty_t "А соседи должны помогать друг другу."
    music Groove2_85
    imgf 42354
    betty "Да, Лиам. Я подвезу вас..."
    liam "Какая же вы замечательная соседка, Мэм!"
    betty "Да, я такая!"
    betty "Пойдемте."
    # затемнение, хлопает дверь авто
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music2 stop
    return


# гостиная дома соседа
label gallery_33546:
    # Бетти с важным видом с рыбой в руках, утюг на столе
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 33425
    w
    imgf 33426
    w
    imgd 33427
    betty "Лиам, давайте мне мой утюг и я пойду. Я тороплюсь."
    liam "Мэм, а вам он очень срочно нужен?"
    imgd 33428
    betty "А почему вы спрашиваете, Лиам?"
    liam "Просто... Я хотел попросить вас оставить его еще хотя бы на день..."
    # Бетти строго
    music Power_Bots_Loop
    img 33429 hpunch
    betty "Лиам, вообще-то, это МОЙ утюг! И мне он тоже нужен!"
    # подходит к Бетти и кладет ладонь ей на попу
    music Hidden_Agenda
    imgd 33430
    liam "Мэм, я просто не успел кое-что погладить..."
    sound Jump2
    img 33431 vpunch
    liam "И если вы не против, тогда я сам завтра вам принесу ваш утюг..."
    betty "Сами принесете?.."
    liam "Да. Мэээм... Я так по вам соскучился..."
    # сосед тянет руки к рыбе, хочет забрать ее
    sound Jump1
    imgd 33432
    liam "Позвольте, я помогу вам?"
    music Pyro_Flow
    imgd 33433
    betty_t "Что он собрался делать?!"
    betty_t "Я ему не позволю больше никаких вольностей!"
    betty_t "Я не собираюсь изменять своему мужу!"
    betty_t "!!!"
    menu:
        "Отдать ему рыбу.":
            pass
        "Не отдавать рыбу! (прерывание квеста)":
            label gallery_33434:
            music Pyro_Flow
            sound2 Jump2
            img 33434 vpunch
            betty "Нет!"
            betty "Мне нужно идти домой и приготовить обед для моего мужа!"
            sound highheels_short_walk
            imgf 33435
            betty "У меня нет времени на всякие глупости!"
            betty "Надеюсь, завтра вы принесете мне мой утюг!"
            liam "Да, Мэм, конечно!"
            fadeblack
            sound highheels_short_walk
            pause 2.0
            sound snd_door_close1
            pause 2.0
            # Бетти уходит с гордым видом и с рыбой в руках
            return
    imgf 33436
    betty "Я вам позволю только в том случае..."
    betty "Если вы пообщаете мне, что это не закончится, как..."
    betty "Как в прошлый раз."
    # он забирает у Бетти рыбу и кладет на стол, на котором стоит утюг
    music Hidden_Agenda
    imgd 33437
    liam "Мэм, ну о чем вы говорите?"
    liam "Конечно, нет!"
    betty "..."
    imgf 33438
    w
    sound down
    imgd 33439
    w
    # подходит к Бетти
    imgf 33440
    liam "Я хотел вам сказать по секрету, что моя проблема решена с вашей помощью."
    #
    $ notif(_("Бетти помогла соседу, проверив, достаточно ли твердый у него член."))
    #
    imgd 33441
    betty "Правда?"
    liam "Да, Мэм!"
    liam "Благодаря вашим умелым ручкам я излечился!"
    liam "И чувствую себя намного уверенее теперь!"
    liam "Смотрите!"
    img 33442
    w
    # демонстративно трогает через штаны свой стояк
    imgd 33443
    w
    sound Jump1
    img 33444 hpunch
    w
    music Groove2_85
    imgd 33447
    betty "Я рада, Лиам, что смогла помочь вам."
    sound highheels_short_walk
    imgf 33445
    betty "Теперь мне нужно идти!"
    img 33446
    w
    # разворачивается, чтобы уходить
    # Лиам подходит к ней вплотную и прижимается
    sound vjuh3
    img 33448 vpunch
    w
    imgd 33449
    liam "Да, Мэм. Мне очень повезло, что у меня такая добрая и отзывчивая соседка, как Вы!"
    # прижимается членом к ее попе через одежду
    music Hidden_Agenda
    imgf 33450
    liam "Сегодня на рынке я был так приятно удивлен, встретив вас!"
    liam "Я никак не могу забыть нашу прошлую встречу..."
    liam "Это было настолько потрясающе, Мэм!"
    # Бетти строго
    music Groove2_85
    img 33451
    betty "Лиам! Давайте не будем говорить об этом!"
    betty "Я не изменяю своему мужу!"
    betty "То, что тогда случилось..."
    #
    $ notif(_("У Бетти был секс с Лиамом и Фредом."))
    #
    imgd 33452
    betty "Это было... Кхм..."
    music Hidden_Agenda
    liam "Вы всего лишь немного расслабились, Мэм..."
    liam "Вы постоянно вся в домашних заботах, у вас столько дел..."
    liam "Вы совсем себя не жалеете, Мэм."
    imgf 33453
    liam "Я хотел бы, чтобы у вас была возможность хотя бы ненадолго вырваться из своей рутины..."
    liam "И забыть обо всем."
    liam "Ведь такая замечательная хозяйка и прекрасная жена заслуживает этого."
    # Лиам берет руку Бетти и кладет на свой стояк
    sound Jump2
    img 33454 vpunch
    w
    img 33455
    betty "Лиам, нет!"
    betty "Я не собираюсь делать этого!"
    liam "Я всего лишь хочу, чтобы Мэм расслабилась..."
    liam "И немного отдохнула от семейных забот..."
    # Бетти сжимает его стояк рукой, начинает водить по нему вверх-вниз
    imgf 33456
    w
    sound vjuh3
    imgd 33457
    w
    sound vjuh3
    imgd 33456
    w
    sound vjuh3
    imgd 33457
    w
    # Лиам кладет ладони ей на грудь
    imgf 33458
    w
    sound vjuh3
    imgd 33459
    w
    sound vjuh3
    imgd 33458
    w
    sound vjuh3
    imgd 33459
    w
    imgf 33460
    liam "Считайте это моей благодарностью за вашу помощь и поддержку, Мэм..."
    betty "Лиам, подождите... Не надо..."
    betty "А как же... Ваш знакомый, который у вас в гараже?"
    liam "Он еще долго будет чинить газонокосилку."
    # просовывает руку ей под платье и если возможно показать, то лезет к ее киске и ласкает ее пальцами
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 33461
    liam "Вам не стоит переживать из-за этого, Мэм."
    imgf 33462
    sound ahhh6
    liam "Мммм... Как я по вам соскучился!"
    imgd 33463
    betty "А если он зайдет?"
    liam "Не зайдет..."
    imgf 33464
    betty_t "Что я делаю?! Я верная жена! Я не могу позволять этому соседу трогать меня!"
    betty_t "А если кто-нибудь увидит?!"
    betty_t "Фред, например! Как в прошлый раз!"
    menu:
        "Я не собираюсь изменять своему мужу!":
            #$ monicaBettyLiamFredMarket3 = day # Бетти согласилась на секс с соседом
            pass
        "Отдайте мне мою рыбу! (прерывание квеста)":
            # Бетти отстраняется от Лиама
            music Pyro_Flow
            sound2 Jump2
            img 33465 vpunch
            betty "Лиам, нет!"
            betty "Мне нужно идти домой и приготовить обед для моего мужа!"
            betty "У меня нет времени на всякие глупости!"
            imgd 33466
            betty "Отдайте мне мою рыбу! И, надеюсь, завтра вы принесете мне мой утюг!"
            liam "Да, Мэм, конечно!"
            sound highheels_short_walk
            imgf 33435
            w
            fadeblack
            sound highheels_short_walk
            pause 2.0
            sound snd_door_close1
            pause 2.0
            # он отдает ей рыбу и Бетти уходит с гордым видом
            return
    # Бетти пытается сдерживаться из последних сил
    imgd 33467
    betty "Лиам, я верная жена своего мужа!"
    liam "Да, Мэм. Вы замечательная, чудесная жена!"
    # продолжая ласкать Бетти рукой
    sound ahhh6
    imgf 33468
    w
    sound lick3
    imgd 33469
    w
    sound lick3
    imgd 33468
    w
    sound lick3
    imgd 33469
    w
    sound lick3
    imgd 33468
    w
    sound lick3
    imgd 33469
    w
    sound lick3
    imgd 33468
    w
    sound lick3
    imgd 33469
    w
    imgf 33470
    liam "Я вам уже говорил, что завидую вашему мужу?"
    betty "Да... Ох..."
    imgd 33471
    w
    sound Jump1
    imgd 33472
    w
    sound ahhh6
    imgf 33470
    liam "Вы сейчас всего лишь немного расслабитесь."
    liam "Ведь это не измена, а просто небольшой отдых..."
    betty "Да... Это не измена..."
    imgd 33473
    liam "Пойдемте на диван, Мэм. Там отдыхать будет намного удобнее..."
    # затемнение, шорох одежды
    # Лиам лежит голый на диване, Бетти стоит голая перед ним
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 33474
    w
    imgf 33475
    betty "Лиам, вы уверены, что ваш друг не зайдет сюда?"
    liam "Уверен. Все в порядке, Мэм..."
    liam "Идите скорее ко мне!"
    imgd 33476
    liam "Вы можете сесть на меня сверху и повернуться лицом к двери..."
    liam "Тогда вы сможете увидеть, если кто-то сюда пойдет."
    betty "Да, я так и сделаю..."
    # Бетти лезет на соседа, раскорячившись
    # он попутно лапает ее за все
    # она неуклюже садится на него сверху, спиной к его лицу
    fadeblack 2.0
    music Loved_Up
    imgfl 33477
    w
    imgf 33478
    w
    imgd 33479
    w
    # Бетти нависает киской над головкой члена, он кладет руку ей на бедро, второй рукой держит член и проводит им по киске туда-сюда
    imgf 33480
    w
    sound lick3
    imgd 33481
    betty "Мммм..."
    sound ahhh6
    imgd 33482
    liam "Да, Мээээм... Я скучал по вашей горячей киске..."
    imgd 33483
    betty "Ооох..."
    sound lick3
    imgd 33481
    w
    imgd 33480
    w
    # он направляет член на ее анус и насаживает Бетти на свой член
    sound ahhh6
    imgf 33484
    w
    music stop
    sound plastinka1b
    img 33485 hpunch
    betty "АААЙ!"
    music Loved_Up2
    imgd 33486
    w
    imgd 33487
    w
    sound vjuh3
    img 33488
    w
    sound chpok6
    img 33489 vpunch
    w
    imgd 33490
    betty "Нет!!! Что ты делаешь?!"
    betty "Убери это из моей попы сейчас же!"
    # он обеими руками держит Бетти за бедра и начинает в ней двигаться
    imgf 33491
    liam "Оооо! Какая тугая у вас дырочка, Мээээм..."
    imgd 33492
    liam "Такой каааайф!"
    imgf 33493
    liam "Мммм..."
    imgd 33494
    w
    imgd 33493
    w
    # продолжает двигаться
    imgd 33494
    betty "Ооох... Н-не н-надоооо..."
    imgd 33493
    w
    imgd 33494
    w
    sound ahhh8
    imgf 33495
    w
    imgd 33496
    w
    imgf 33497
    w
    # Бетти начинает кайфовать и откидывается спиной на грудь соседа (поза, как с Фредом в спальне)
    sound Jump2
    imgd 33498
    w
    # video
    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Neighbour_Sex3_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_1= Movie(play="video/v_Betty_Neighbour_Sex3_1.mkv")
    show videov_Betty_Neighbour_Sex3_1
    with fade
    betty "Ооох!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_2= Movie(play="video/v_Betty_Neighbour_Sex3_2.mkv")
    show videov_Betty_Neighbour_Sex3_2
    with fade
    liam "Вы чувствуете, какой мой член твердый?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_3= Movie(play="video/v_Betty_Neighbour_Sex3_3.mkv",)
    show videov_Betty_Neighbour_Sex3_3
    with fade
    betty "Дааа... Он очень твердый..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound ahhh9
    imgf 33499
    w

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_4= Movie(play="video/v_Betty_Neighbour_Sex3_4.mkv")
    show videov_Betty_Neighbour_Sex3_4
    with fade
    liam "Вам нравится ощущать его в своей упругой попке?"
    betty "Оооох! Дааа..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_5= Movie(play="video/v_Betty_Neighbour_Sex3_5.mkv")
    show videov_Betty_Neighbour_Sex3_5
    with fade
    betty "Но я... Я не разрешала... В мою попу..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_6= Movie(play="video/v_Betty_Neighbour_Sex3_6.mkv")
    show videov_Betty_Neighbour_Sex3_6
    with fade
    betty "Ааах!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 33500
    w

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_7= Movie(play="video/v_Betty_Neighbour_Sex3_7.mkv")
    show videov_Betty_Neighbour_Sex3_7
    with fade
    liam "Мне остановиться, Мэм?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    #8
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex3_8= Movie(play="video/v_Betty_Neighbour_Sex3_8.mkv")
    show videov_Betty_Neighbour_Sex3_8
    with fade
    betty "Не вздумай! Ааах!"
    liam "Ммммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound ahhh6
    imgf 33501
    w
    sound hlup25
    imgd 33502
    w
    sound hlup25
    imgd 33501
    w
    sound hlup25
    imgd 33502
    w
    # Бетти с Лиамом в процессе и раздается звук открывающейся двери
    # заходит приятель Лиама и сначала не смотрит на них
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 33503
    w
    imgf 33504
    robby "Эй, дружище!"
    robby "Твоя газонокосилка готова!"
    robby "Там делов то оказалось - ерунда..."
    # поднимает взгляд и видит перед собой раскоряченную на Лиаме Бетти, ноги широко раздвинуты
    # Бетти открывает глаза и в ужасе смотрит на него
    sound ahhh6
    imgd 33505
    w
    sound wow
    imgd 33506
    w
    music stop
    sound plastinka1b
    img 33507 vpunch
    betty "Что?!"
    music Power_Bots_Loop
    betty "Что вы тут делаете?!"
    # пытается сдвинуть ноги и встать с соседа
    sound Jump2
    imgd 33508
    betty "Не смотрите на меня!"
    # он кладет руки ей на талию или бедра и удерживает
    # начинает снова в ней двигаться
    sound vjuh3
    img 33509 vpunch
    w
    music Loved_Up
    imgf 33510
    w
    sound hlup25
    imgd 33511
    w
    sound hlup25
    imgd 33510
    w
    sound hlup25
    imgd 33511
    w
    sound ahhh6
    imgf 33512
    betty "Лиам, прекрати!"
    betty "Не надо! Мы не одни... Ооох..."
    # мужчина обмениваются взглядами и Робби подходит к Бетти
    imgd 33513
    w
    img 33514
    # Бетти пытается возмущаться
    betty "Что вы делаете?!"
    betty "Отойдите от меня!"
    liam "Все хорошо, Мэм..."
    liam "Робби мой давний приятель..."
    liam "Вы можете не стесняться его."
    # но продолжает сидеть на Лиаме, а он продолжает ее пялить
    imgf 33510
    betty "Мммм..."
    w
    sound hlup25
    imgd 33511
    w
    sound hlup25
    imgd 33510
    w
    sound hlup25
    imgd 33511
    w
    # Бетти зло смотрит на друга соседа
    imgf 33515
    betty "Это не то что вы подумали!"
    betty "Я порядочная женщина!"
    betty "Аааах..."
    betty "Не смотрите на меня! Отвернитесь!"
    # Робби протягивает руку и начинает пальцем водить по клитору Бетти, ее ведет от этого еще больше
    sound Jump2
    img 33516 vpunch
    w
    sound ahhh8
    imgd 33517
    betty "Не трогайте меня! Ааа..."
    imgf 33518
    liam "Мэм, Робби хороший человек..."
    liam "Он помогает мне по работе..."
    liam "А вам сегодня сделал большую скидку."
    betty "Нет! Аааах..."
    # Бетти уже вовсю кайфует от Лиама и от пальцев Робби
    imgf 33517
    w
    sound lick3
    imgd 33519
    w
    sound lick3
    imgd 33517
    w
    sound lick3
    imgd 33519
    w
    imgf 33520
    robby "Мне уйти, Мэм?" # продолжая водить пальцем по клитору
    sound ahhh6
    imgd 33512
    betty "Ммммм..."
    liam "Вы могли бы отблагодарить его за скидку, Мэм..."
    liam "Спросите у Робби, хочет ли он вашей благодарности?"
    betty "Оооох..."
    imgf 33521
    betty "Я... Ммммм..."
    betty "Могла бы я вас отблагодарить?.. За скидку... Аааах..."
    robby "Думаю, что не откажу вам, Мэм..."
    imgd 33522
    w
    sound hlup25
    imgd 33523
    w
    sound hlup25
    imgd 33522
    w
    sound hlup25
    imgd 33523
    w
    sound hlup25
    imgd 33522
    w
    sound hlup25
    imgd 33523
    betty "Оооо..."
    imgf 33524
    robby "Как же я могу отказаться от вашей благодарности..."
    # Бетти тащится, Робби снимает штаны и пристраивается между ног Бетти
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up2
    imgfl 33525
    betty "Что вы собираетесь делать?!"
    betty "Я не это имела ввиду!"
    # нацеливает член на ее киску
    # вводит
    imgf 33526
    w
    sound chpok6
    img 33527 vpunch
    robby "Вот тааак... Даааа..."
    sound ahhh8
    img 33528
    betty "Аааааа!!!"
    betty "Какой большой... Аааа..."
    # video
    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Neighbour_Sex4_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_1= Movie(play="video/v_Betty_Neighbour_Sex4_1.mkv")
    show videov_Betty_Neighbour_Sex4_1
    with fade
    robby "Да, это была большая скидка, Мэм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 33529
    w
    # начинают пялить ее вдвоем
    imgd 33530
    w

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_2= Movie(play="video/v_Betty_Neighbour_Sex4_2.mkv")
    show videov_Betty_Neighbour_Sex4_2
    with fade
    robby "Я готов предоставлять вам эту скидку хоть каждый день..."
    robby "Да..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_3= Movie(play="video/v_Betty_Neighbour_Sex4_3.mkv")
    show videov_Betty_Neighbour_Sex4_3
    with fade
    robby "Вы ведь довольны покупкой, Мэм?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 33531
    betty "Дааа... Очень!"

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_4= Movie(play="video/v_Betty_Neighbour_Sex4_4.mkv")
    show videov_Betty_Neighbour_Sex4_4
    with fade
    robby "Мой босс просит оценить работу продавца."
    robby "Вы же довольны остались моим сервисом, Мэм?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 33532
    w
    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_5= Movie(play="video/v_Betty_Neighbour_Sex4_5.mkv")
    show videov_Betty_Neighbour_Sex4_5
    with fade
    betty "Оооо, даааа! Мне очень понравился ваш сервис!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    sound ahhh9
    imgf 33528
    liam "Мэм, спросите у Робби, достаточно ли вы его отблагодарили за скидку?"
    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_6= Movie(play="video/v_Betty_Neighbour_Sex4_6.mkv")
    show videov_Betty_Neighbour_Sex4_6
    with fade
    betty "Достаточно ли я вас отблагодарила? Ооох..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_7= Movie(play="video/v_Betty_Neighbour_Sex4_7.mkv")
    show videov_Betty_Neighbour_Sex4_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 33533
    robby "О, дааа! Мне нравится, как Мэм благодарит меня за скидку!"

    #8
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_8= Movie(play="video/v_Betty_Neighbour_Sex4_8.mkv")
    show videov_Betty_Neighbour_Sex4_8
    with fade
    robby "Приходите за рыбой, когда захотите... Мммм..."
    robby "Для вас всегда будет самая свежая рыба, Мэм!"
    betty "Оооох..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 33534
    liam "Я же говорил, Мэм, что Робби хороший парень... Да..."

    #9
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_9= Movie(play="video/v_Betty_Neighbour_Sex4_9.mkv")
    show videov_Betty_Neighbour_Sex4_9
    with fade
    liam "А постоянным своим покупательницам он делает просто огромные скидки..."
    liam "И почти ничего не просит взамен!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #10
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex4_10= Movie(play="video/v_Betty_Neighbour_Sex4_10.mkv")
    show videov_Betty_Neighbour_Sex4_10
    with fade
    betty "Огромные... Да..."
    robby "Да, Мэээм..."
    robby "Вас ждет просто огромная скидкааа..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # со стороны входной двери возникает силуэт Фреда
    sound man_steps
    imgf 33535
    w
    # он подходит ближе и с ухмылкой смотрит на Бетти
    imgd 33536
    w
    sound ahhh6
    imgd 33537
    w
    # та уже вовсю плывет и появления Фреда даже не заметила
    # он снимает брюки и подходит к лицу Бетти
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up2
    imgfl 33538
    w
    sound ahhh8
    imgf 33539
    betty "Аааа..."
    betty "Еще-еще!!!"
    betty "Оооо!"
    # берет в руку член и стучит им Бетти по лбу или по губам
    imgd 33540
    fred "Миссис Робертс..."
    sound vjuh3
    img 33541
    fred "Я пришел исполнить свой профессиональный долг."

    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Neighbour_Sex5_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_1= Movie(play="video/v_Betty_Neighbour_Sex5_1.mkv")
    show videov_Betty_Neighbour_Sex5_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # она открывает глаза, взгляд расфокусированный
    img 33542 vpunch
    betty "Фреееед..."
    betty "Уйди!"
    betty "Ооох..."
    betty "Дааа..."
    sound ahhh6
    imgd 33543
#    betty "Еще!"
    betty "Фред, это не то что ты думаешь!"
    betty "Ооо!!!"
    # во время Ооо!!! Фред вставляет свой член ей в рот
    sound chpok6
    img 33544 vpunch
    betty "Нет!"

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_2= Movie(play="video/v_Betty_Neighbour_Sex5_2.mkv")
    show videov_Betty_Neighbour_Sex5_2
    with fade
    betty "Я вефная фена сффоего муффа!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_3= Movie(play="video/v_Betty_Neighbour_Sex5_3.mkv")
    show videov_Betty_Neighbour_Sex5_3
    with fade
    betty "Мпфхмммм!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 33545
    fred "О да, Миссис Робертс!"
    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_4= Movie(play="video/v_Betty_Neighbour_Sex5_4.mkv")
    show videov_Betty_Neighbour_Sex5_4
    with fade
    fred "Мне так нравится, когда ваш ротик занят моим членом..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 33546
    robby "Ооо, я в следующий раз тоже так сделаю!"
    robby "Да..."

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_5= Movie(play="video/v_Betty_Neighbour_Sex5_5.mkv")
    show videov_Betty_Neighbour_Sex5_5
    with fade
    betty "Ммммм!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_6= Movie(play="video/v_Betty_Neighbour_Sex5_6.mkv")
    show videov_Betty_Neighbour_Sex5_6
    with fade
    fred "Тише-тише, Миссис Робертс..."
    fred "Не отвлекайтесь..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 33547
    fred "Возьмите его поглубже, Миссис Робертс."
    sound hlup25
    imgd 33548
    fred "Вот так, дааа..."
    sound hlup25
    imgd 33547
    w
    sound hlup25
    imgd 33548
    w
    sound hlup25
    imgd 33547
    w
    sound hlup25
    imgd 33548
    w
    sound hlup25
    imgd 33547
    fred "Отлично!"
    sound hlup25
    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_7= Movie(play="video/v_Betty_Neighbour_Sex5_7.mkv")
    show videov_Betty_Neighbour_Sex5_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 33548
    w
    imgf 33549
    w
    imgd 33550
    robby "В следующий раз Мэм будет благодарить меня с моим членом во рту... Мммм..."

    #8
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_8= Movie(play="video/v_Betty_Neighbour_Sex5_8.mkv")
    show videov_Betty_Neighbour_Sex5_8
    with fade
    fred "Или с двумя членами во рту. Да, Миссис Робертс?"
    fred "Вам же это нравится, да?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 33551
    liam "Дааа, Мэм любит это делать..."

    #9
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_9= Movie(play="video/v_Betty_Neighbour_Sex5_9.mkv")
    show videov_Betty_Neighbour_Sex5_9
    with fade
    liam "Какая же у меня хорошая соседка... Ааааа..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #10
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_10= Movie(play="video/v_Betty_Neighbour_Sex5_10.mkv")
    show videov_Betty_Neighbour_Sex5_10
    with fade
    liam "Не думал что богатые люди могут быть такими заботливыми..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #11
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex5_11= Movie(play="video/v_Betty_Neighbour_Sex5_11.mkv")
    show videov_Betty_Neighbour_Sex5_11
    with fade
    wclean
    fred "Кончайте, Миссис Робертс!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 33552
    w
    imgf 33553
    liam "Да, давайте, Мэм!"
    robby "Я тоже! Тоже сейчас кончу!"
    # сначала кончает только Бетти с членом Фреда во рту
    img 33555
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
#    sound woman_moan14
    betty "Мммммм!"
    img 33554
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan14
    betty "ММММММ!!"
    betty "ММММММММ!!!"
    # во время ее оргазма раздается стук в дверь
    sound snd_door_knock
    imgf 33557
    ralph "Бетти, дорогая, ты здесь?"
    # Бетти в ужасе открывает глаза
    music stop
    sound plastinka1b
    imgd 33554
    w
    img 33556 vpunch
    betty_t "ЧТОООО?!"
    betty_t "?!?!?!"
    music Loved_Up2
    with fade
    # в этот момент кончают мужчины
    menu:
        "Кончить внутрь Бетти.":
            #$ monicaBettyLiamRobbyFred_cumzone = 1
            # мужчины кончают внутрь Бетти
            img 33558
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            liam "Я тоже..."
            liam "Кончаааааю!!!"
            img 33553
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            robby "ААА!"
            liam "АААААА!!"
            img 33549
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            imgf 33559
            w
            sound hlup25
            imgd 33560
            w
            img 32971
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            fred "МММММММ!!!"
            img 33561
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan3
            w
            imgd 33562
            sound snd_door_knock
            w
            img 33563 vpunch
            betty "!!!"
            pass
        "Кончить на Бетти.":
            # мужчины кончают на Бетти (Робби и Лиам на попу и киску, Фред на грудь)
            #$ monicaBettyLiamRobbyFred_cumzone = 2
            img 33558
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            liam "Я тоже..."
            liam "Кончаааааю!!!"
            img 33553
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            robby "ААА!"
            liam "АААААА!!"
            img 33549
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 33564
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            imgf 33565
            w
            img 32971
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            fred "МММММММ!!!"
            img 33561
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 33566
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan3
            w
            imgd 33567
            sound snd_door_knock
            w
            img 33568 vpunch
            betty "!!!"
            pass
    # музыка и звуки секса стихают
    # повторно раздается стук в дверь, Бетти испуганно смотрит в сторону двери
#    img 33563
    ## или
#    img 33568
    # затемнение
    sound snd_fabric1
    fadeblack 2.0
    sound snd_door_knock
    pause 2.0
    return


# танец Клэр
# крики толпы из зала
label gallery_34190:
    # когда просто танцует в трусиках
    fadeblack 2.0
    music Road_Trip
    sound2 highheels_short_walk
    imgfl 34194
    w
    imgf 34192
    w
    imgd 34193
    customers5 "Снимай с себя все скорее!"
    customers1 "Дааа! Давай раздевайся!"
    customers2 "Хочу увидеть твою киску!"
    # Клэр снимает трусики и бросает их на сцену
    sound Jump2
    img 34180 vpunch
    sound2 wow
    customers3 "ООООО! ОХРЕНЕТЬ!"
    customers4 "ДА, КЛЭР! ДАВАЙ, ДЕТКА!"
    # один из посетителей пробирается к сцене в тот момент, когда она бросила трусики на сцену
    # его рука тянется к трусикам, хватет их и его силуэт быстро смывается оттуда
    imgf 34181
    w
    imgd 34182
    w
    sound Jump1
    img 34183 hpunch
    w
    # Клэр, когда во время танца поворачивается спиной к залу, поднимает руку к маске, снимает ее, но к залу не поворачивается
    imgf 34184
    w
    imgd 34185
    w
    imgd 34186
    w
    sound vjuh3
    img 34187 hpunch
    w
    # видно, что ей по кайфу, она проводит рукой по своей груди, прикрывая глаза
    imgf 34188
    w
    sound wow
    img 34189 vpunch
    w
    # потом медлит, не поворачиваясь и как-будто очнувшись снова надевает маску, поворачивается к залу и продолжает танец
    imgf 34187
    w
    imgd 34190
    w
    sound vjuh3
    img 34186 hpunch
    w
    imgd 34185
    w
    imgf 34191
    customers5 "Раздвинь ножки шире, красотка! Хочу разглядеть твою киску!"
    customers1 "ЕЕЕЕ! Давай-давай!"
    customers2 "Приласкай свою киску! Покажи, как ты делаешь это!"
    customers3 "Ты чертовски охренительна, крошка!"
    customers4 "Я сейчас кончу!!!"
    customers5 "О, даааа!"
    sound wow
    imgd 34195
    w
    imgf 34183
    w
    fadeblack 2.0
    music Stealth_Groover
    imgfl 34196
    sound highheels_short_walk
    w
    return


# подсобка барменов
# банкир сидит на диване, Эшли и Моника заходят в подсобку
label gallery_33991:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 33967
    w
    imgf 33968
    w
    imgd 33969
    mt "Меня тошнит от одного его самодовольного вида!"
    mt "Мерзкий самовлюбленный мешок с дерьмом!"
    mt "!!!"
    # Эшли встает сбоку от столика
    imgf 33970
    ashley "Мистер Беркельбаух, извините за ожидание."
    ashley "У нашей Королевы Shiny Hole только что закончилось выступление на сцене."
    # банкир недовольно
    imgd 33971
    banker "Да, я уже заждался..."
    banker "Ты же знаешь, Эшли, мне это не нравится."
    banker "Я трачу свое время здесь, а мое время дорого стоит."
    # банкир небрежным жестом указывает на Монику
    imgd 33972
    banker "Я надеюсь, эта Королева компенсирует мне мое ожидание."
    ashley "Мистер Беркельбаух, конечно!"
    ashley "Вы можете не сомневаться в этом!"
    banker "Как там тебя зовут, напомни? Молли?"
    music Power_Bots_Loop
    img 33969
    mt "Вот ублюдок!"
    mt "!!!"
    music Groove2_85
    imgd 33973
    ashley "Это [monica_pub_name]."
    ashley "Теперь она Королева Shiny Hole."
    banker "Ага. Лезь на стол, [monica_pub_name]."
    banker "Не будем терять времени."
    banker "Начинай."
    # Моника стоит и зло смотрит на него
    img 33974 vpunch
    mt "!!!"
    # Эшли ее одергивает
    imgd 33975
    ashley "[monica_pub_name]!"
    ashley "Делай, что говорит Мистер Беркельбаух!"
    #$ menu_corruption = [monicaAshleyBerkelbauchCorruptionRequired2, 0]
    menu:
        "Залезть на стол.":
            pass
        "Не делать этого!":
            #$ monicaAshleyBerkelbauch2 = day # Моника отказалась танцевать перед банкиром
            music Pyro_Flow
            img 33976 hpunch
            m "Я не собираюсь раздеваться перед ним!"
            m "Достаточно было прошлого раза!"
            ashley "[monica_pub_name]! Не смей так говорить!"
            imgd 33978
            ashley "У тебя есть обязанности, которые ты должна выполнять!"
            ashley "Залезь на этот чертов стол!!!"
            m "Нет! Я Королева и мне плевать на какие-то там обязанности!"
            # Моника разворачивается и уходит
            sound highheels_short_walk
            imgf 33977
            mt "Пошла эта Эшли к черту!"
            mt "Пусть сама кривляется перед банкиришкой!"
            mt "Гребаная дура!"
            mt "!!!"
            # затемнение
            fadeblack
            sound highheels_short_walk
            pause 2.0
            return
    # Моника ставит ногу на стол и высокомерно смотрит на банкира
    fadeblack 2.0
    music Road_Trip
    sound2 heel1
    imgfl 33979
    w
    imgf 33980
    mt "Ничтожный банковский клерк!"
    mt "Строит из себя хозяина мира!"
    mt "Какой же он жалкий и никчемный! Фи!"
    mt "Пусть порадуется, что сама Королева удостоит его чести смотреть на нее!"
    mt "Неудачник!"
    # Моника лезет на стол и танцует
    imgd 33981
    w
    sound heel1
    imgf 33982
    w
    imgd 33983
    w
    imgf 33984
    banker "Да, это новая Королева то что надо..."
    imgd 33985
    w
    imgd 33986
    banker "Я хотел бы видеть ее попку почаще."
    imgf 23330
    w
    sound vjuh3
    img 23331
    w
    imgf 33987
    w
    imgd 33988
    w
    sound Jump2
    img 33989 hpunch
    banker "Наклонись, раздвинь ноги пошире и замри."
    imgf 33991
    banker "Я хочу внимательно рассмотреть новую Королеву этого бара."
    imgd 33990
    banker "Да, я представляю, как каждый из посетителей этого заведения..."
    imgd 33992
    banker "Хочет разложить тебя прямо на сцене, когда ты танцуешь."
    # расстегивает ширинку и достает свой стояк
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Road_Trip
    imgfl 23362
    w
    imgf 33993
    banker "Я посмотрел бы на такое выступение..."
    banker "Ты смогла бы заняться сексом с одним из них прямо на сцене, Королева?"
    banker "У всех на глазах, а? Хе-хе!"
    imgd 33994
    mt "Что за чушь он несет?!"
    mt "Озабоченный извращенец!"
    mt "!!!"
    # банкир обращается к Эшли
    music Groove2_85
    imgf 33995
    banker "Эшли?"
    ashley "Да, Мистер Беркельбаух?"
    banker "Не думаю, что танца этой Королевы достаточно для открытия новой кредитной линии..."
    imgd 33996
    ashley "Мистер Беркельбаух, но как же?"
    ashley "Мы же с вами говорили, что..."
    banker "Королеве придется сделать еще кое-что..."
    # показательно смотрит на свой член
    imgd 33997
    banker "Для глубокой оценки платежеспособности клиента..."
    banker "Нужно провести, соответственно, глубокий анализ, Эшли."
    banker "И если я останусь доволен, тогда считай, что кредит тебе одобрен."
    # Эшли смотрит на него в растерянности
    imgf 33998
    ashley "Оценки чего? Платежегодности?"
    ashley "В смысле, глубокой?"
    ashley "Я ничего не понимаю..."
    imgd 33999
    banker "Эшли, скажи этой Королеве, чтобы она подошла ближе ко мне."
    banker "И сделала так..."
    banker "Чтобы я признал твою, Эшли, платежеспособность удовлетворительной."
    banker "Это заведение уже накопило кредиты и стало высокорисковым активом."
    imgf 34000
    banker "Поэтому, я должен убедиться в том, что это заведение может обслуживать клиентов как полагается."
    banker "И что у него есть шанс расплатиться с банком..."
    ashley "..."
    # до Эшли доходит, что банкир намекает на минет, она смотрит на Монику
    img 34001
    ashley "[monica_pub_name]!"
    ashley "Делай, что говорит Мистер Беркельбаух!"
    m "..."
    m "Что делать?!"
    imgd 34002
    ashley "Подойди к Мистеру Беркельбауху и сделай так, чтобы он остался доволен!"
    ashley "Чего здесь непонятного?!"
    m "ЧТООО?!"
    m "!!!"
    #$ menu_corruption = [monicaAshleyBerkelbauchCorruptionRequired3, 0]
    menu:
        "Сделать, как говорит Эшли.":  # коррапшн
            # Моника поворачивается и смотрит на Эшли с возмущением
            label gallery_34020:
            music Groove2_85
            img 34003 vpunch
            m "Эшли!"
            ashley "[monica_pub_name]!!!"
            ashley "Чего ты на меня смотришь?!"
            ashley "Тебе же ясно сказали, что нужно делать!"
            ashley "Выполняй!"
            img 34004
            mt "!!!"
            #$ menu_corruption = [monicaAshleyBerkelbauchCorruptionRequired4, monicaAshleyBerkelbauchCorruptionRequired5]
            menu:
                "Минет (in Extra version) (disabled)." if game.extra == False:
                    pass
                "Минет." if game.extra == True:
                    #$ monicaAshleyBerkelbauch4 = day # Моника согласилась на минет банкиру
                    # Моника стоит в раздумьях
                    imgf 34007
                    mt "Вот черт!"
                    mt "Чего ему от меня нужно?!"
                    mt "Он хочет, чтобы я..."
                    mt "Взяла в рот его мерзкий отросток?!"
                    mt "Фу!!!"
                    mt "!!!"
                    imgd 34008
                    mt "Как мне поступить?"
                    mt "Ведь если я сейчас откажусь, то эта гребаная дура Эшли..."
                    music Stealth_Groover
                    mt "Черт! Она сказала, что Молли была лучшей королевой, чем я!"
                    mt "А это не так!"
                    mt "Я здесь лучшая! Со мной никто не сравнится!"
                    mt "!!!"
                    imgd 34009
                    mt "Я не допущу, чтобы Эшли ставила под сомнение мой статус!"
                    mt "И я докажу, что Молли никто, а Я - Королева!"
                    mt "Даже если мне придется ради этого терпеть этого мерзкого клерка!"
                    mt "!!!"
                    # банкир прерывает мысли Моники
                    music Groove2_85
                    imgf 34010
                    banker "Эшли, я уже начинаю скучать."
                    banker "Знаешь, из-за этого я обычно становлюсь нервным и со мной сложнее договориться."
                    banker "Поэтому советую быстрее начинать глубокий анализ твоей платежеспособности."
                    banker "Скажи этой Королеве, пусть поторопится..."
                    # Эшли раздраженно
                    imgd 34011
                    ashley "[monica_pub_name], ты чего тормозишь?"
                    ashley "Мистер Беркельбаух ясно тебе сказал, что нужно сделать!"
                    ashley "Выполняй, если хочешь оставаться Королевой в моем баре!!!"
                    # Моника на нее зло смотрит
                    img 34012
                    m "Я не буду!"
                    m "Эшли, я здесь только танцую и..."
                    imgd 34013
                    ashley "Будешь, если хочешь и дальше оставлять все чаевые себе!"
                    ashley "Я знаю, [monica_pub_name], сколько ты зарабатываешь здесь!"
                    ashley "И, учти, что эти деньге недополучает заведение, которое находится в финансовом кризисе!"
                    ashley "Потому, ты сделаешь это исключение для мистера Беркельбауха сейчас же!"
                    m "!!!"
                    # потом наклоняется к банкиру
                    fadeblack 1.5
                    music Groove2_85
                    sound2 highheels_short_walk
                    imgf 34014
                    banker "Иди сюда. Сделай это по-королевски."
                    imgd 34015
                    ## вставить фразу банкира о том, чтобы Мон сняла маску (не нашел больше поводов чтобы она это сделала)
                    banker "Только сначала сними эту маску..."
                    banker "Я хочу видеть твое лицо, Королева. Хе-хе!"
                    menu:
                        "Снять маску.":
                            pass
                    imgf 34016
                    mt "!!!"
                    sound vjuh3
                    img 34017
                    w
                    imgf 34018
                    banker "Сделай так, чтобы я признал платежеспособность Эшли удовлетворительной."
                    banker "И уже завтра новая кредитная линия будет открыта."
                    # Моника берет в рот его член
                    # Эшли радостно спрашивает у банкира
                    fadeblack 1.5
                    music Loved_up
                    imgfl 34019
                    w
                    imgf 34020
                    w
                    imgd 34021
                    ashley "Уже завтра?!"
                    banker "Завтра, все верно."
                    banker "Возьми глубже член, хватит его облизывать."
                    imgf 34019
                    w
                    sound chpok6
                    img 34023 vpunch
                    mt "!!!"
                    imgd 34022
                    w
                    imgf 34024
                    ashley "А банк мне одобрит всю сумму, которую я просила?"
                    imgd 34025
                    banker "Да, Эшли. Мммм..."
                    # Моника двигает головой вверх-вниз
                    # video
                    sound hlup25
                    imgd 34026
                    w
                    sound hlup25
                    imgd 34027
                    w

                    #1
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Monica_Banker_Blowjob1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_1= Movie(play="video/v_Monica_Banker_Blowjob1_1.mkv")
                    show videov_Monica_Banker_Blowjob1_1
                    with fade
                    banker "Вот тааак... Хорошо, да..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")


                    #2
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_2= Movie(play="video/v_Monica_Banker_Blowjob1_2.mkv")
                    show videov_Monica_Banker_Blowjob1_2
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    sound hlup25
                    imgd 34026
                    w
                    sound hlup25
                    imgd 34025
                    w
                    imgf 34028
                    w

                    #3
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_3= Movie(play="video/v_Monica_Banker_Blowjob1_3.mkv")
                    show videov_Monica_Banker_Blowjob1_3
                    with fade
                    banker "Оценка проходит вполне успешно, Эшли..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 34029
                    w

                    #4
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_4= Movie(play="video/v_Monica_Banker_Blowjob1_4.mkv")
                    show videov_Monica_Banker_Blowjob1_4
                    with fade
                    banker "Ммммм..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    music Loved_up2
                    imgf 34030
                    banker "Еще-еще! Ааааа..."
                    imgd 34031
                    w

                    #5
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_5= Movie(play="video/v_Monica_Banker_Blowjob1_5.mkv")
                    show videov_Monica_Banker_Blowjob1_5
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    #6
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_6= Movie(play="video/v_Monica_Banker_Blowjob1_6.mkv")
                    show videov_Monica_Banker_Blowjob1_6
                    with fade
                    banker "Оценка почти завершена! Оооо..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 34032
                    banker "Еще немного!"
                    imgf 34023
                    w


                    sound hlup25
                    imgd 34019
                    banker "Быстрее! Давай!"
                    sound hlup25
                    imgd 34023
                    w
                    sound hlup25
                    imgd 34019
                    w
                    sound hlup25
                    img 34023
                    w

                    #7
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Blowjob1_7= Movie(play="video/v_Monica_Banker_Blowjob1_7.mkv")
                    show videov_Monica_Banker_Blowjob1_7
                    with fade
                    banker "Дааааа..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")
                    menu:
                        "Кончить на лицо Моники.":
                            #$ monicaAshleySexBerkelbauch_cumzone = 1
                            img 34033
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            banker "Оооох..."
                            img 34034
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            w
                            img 34035
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan18
                            banker "Ммммммм..."
                            sound hlup10
                            imgd 34036
                            w
                            pass
                        "Кончить в рот Моники.":
                            #$ monicaAshleySexBerkelbauch_cumzone = 2
                            img 34033
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            banker "Оооох..."
                            img 34019
                            w
                            img 34023
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            w
                            img 34037
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan18
                            banker "Ммммммм..."
                            sound2 hlup10
                            imgd 34038
                            w
                            pass
                "Секс.":
                    #$ monicaAshleyBerkelbauch5 = day # Моника согласилась на секс с банкиром
                    # Моника медлит
                    imgf 34008
                    mt "Твою мать!"
                    mt "Она овца Эшли требует от меня..."
                    mt "Требует, чтобы Я..."
                    mt "Занялась с ним этой гадостью?!"
                    mt "!!!"
                    mt "!!!!"
                    # Эшли стоит руки в боки
                    imgd 34012
                    m "Я не буду!"
                    m "Эшли, я здесь только танцую и..."
                    ashley "Будешь, если хочешь и дальше оставлять все чаевые себе!"
                    ashley "Я знаю, [monica_pub_name], сколько ты зарабатываешь здесь!"
                    ashley "И, учти, что эти деньге недополучает заведение, которое находится в финансовом кризисе!"
                    ashley "Потому, ты сделаешь это исключение для мистера Беркельбауха сейчас же!"
                    img 34013
                    m "Нет!"
                    ashley "Или ты сейчас же выполнить пожелание многоуважаемого Мистера Беркельбауха!"
                    ashley "Или с завтрашнего дня корона будет принадлежать Молли!"
                    ashley "Как и все королевские привилегии!!!"
                    imgd 34009
                    mt "!!!"
                    mt "Я не допущу, чтобы Эшли ставила под сомнение мой статус!"
                    mt "И я докажу, что Молли никто, а Я - Королева!"
                    mt "Даже если мне придется ради этого терпеть этого мерзкого клерка!"
                    img 34039 vpunch
                    ashley "Делай, что тебе сказал Мистер Беркельбаух!"
                    ashley "Быстро!"
                    music Groove2_85
                    imgf 34010
                    banker "Эшли, я уже начинаю скучать."
                    banker "Знаешь, из-за этого я обычно становлюсь нервным и со мной сложнее договориться."
                    banker "Поэтому советую быстрее начинать глубокий анализ твоей платежеспособности."
                    banker "Скажи этой Королеве, пусть поторопится..."
                    music Stealth_Groover
                    imgd 34007
                    mt "Это моя корона! Я ее заслужила!"
                    mt "Я не отдам ее дешевке Молли!"
                    mt "Корона МОЯ!!!"
                    mt "!!!"
                    music Hidden_Agenda
                    mt "А это... это делаю не я..."
                    mt "Это делает [monica_pub_name]..."
                    # Моника бросает злой взгляд на Молли, потом смотрит на банкира
                    music Groove2_85
                    imgd 34040
                    banker "Ну... Чего ты ждешь, Королева? Хе-хе!"
                    sound highheels_short_walk
                    imgf 34014
                    banker "Только сначала сними эту маску..."
                    banker "Я хочу видеть твое лицо!"
                    menu:
                        "Снять маску.":
                            pass
                    # Моника встает и закидывает на него одну ногу
                    ## вставку про снятие маски
                    imgd 34041
                    w
                    sound vjuh3
                    img 34042
                    w
                    imgf 34043
                    mt "Отвратительный!"
                    # потом вторую ногу
#                    sound Jump2
                    imgd 34044
                    mt "Никчемный!"
                    # потом нависает попой над его членом
                    imgd 34045
                    mt "Ничтожный!"
                    # держит его член рукой и садится на него, возможно не с первой попытки
                    imgf 34046
                    banker "Ммммм... Ну давай же..."
                    mt "Грязный извращенец!!!"
                    # села и начинает двигаться
                    fadeblack 1.5
                    music Loved_up
                    sound2 chpok6
                    img 34047 hpunch
                    banker "Да, тааак..."
                    mt "Ненавижу!!!"
                    # со злым лицом прыгает на его члене

                    # video
                    #1
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Monica_Banker_Sex1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_1= Movie(play="video/v_Monica_Banker_Sex1_1.mkv")
                    show videov_Monica_Banker_Sex1_1
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")


                    imgf 34048
                    w
                    imgd 34049
                    banker "Оооо... Тебе нравится, Королева?"
                    m "..."
                    imgf 34050
                    banker "Покажи мне, как тебе нравится чувствовать мой член!"
                    m "..."
                    # Эшли прикривает на Монику
                    #2
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_2= Movie(play="video/v_Monica_Banker_Sex1_2.mkv")
                    show videov_Monica_Banker_Sex1_2
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 34051
                    ashley "[monica_pub_name]!"
                    ashley "Исполняй свои обязанности как полагается!"
                    ashley "Покажи, как тебе нравится быть с Мистером Беркельбаухом!"
                    m "!!!"
                    menu:
                        "Притворяться, что Монике нравится.":
                            pass
                    # Моника стонет, но лицо все равно недовольное
                    imgf 34052
                    sound ahhh4
                    m "Оооо..."
                    banker "Вот теперь вижу, что тебе нравится... Мммм..."

                    #3
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Monica_Banker_Sex1_1b_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_3= Movie(play="video/v_Monica_Banker_Sex1_3.mkv")
                    show videov_Monica_Banker_Sex1_3
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    sound hlup25
                    imgd 34053
                    w
                    sound ahhh2
                    imgf 34054
                    m "Аааа..."
                    imgd 34055
                    banker "Старайся лучше! Быстрее!"

                    #4
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_4= Movie(play="video/v_Monica_Banker_Sex1_4.mkv")
                    show videov_Monica_Banker_Sex1_4
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    #5
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_5= Movie(play="video/v_Monica_Banker_Sex1_5.mkv")
                    show videov_Monica_Banker_Sex1_5
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 34056
                    w
                    sound ahhh3
                    imgd 34054
                    m "Оооох..."
                    imgd 34057
                    w

                    #6
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_6= Movie(play="video/v_Monica_Banker_Sex1_6.mkv")
                    show videov_Monica_Banker_Sex1_6
                    with fade
                    mt "Когда же этот кретин уже кончит?!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    music Loved_up
                    sound2 ahhh5
                    imgf 34058
                    w

                    #7
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_7= Movie(play="video/v_Monica_Banker_Sex1_7.mkv")
                    show videov_Monica_Banker_Sex1_7
                    with fade
                    banker "Еще-еще! Ааааа..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 34059
                    banker "Оценка почти завершена! Оооо..."

                    #8
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_8= Movie(play="video/v_Monica_Banker_Sex1_8.mkv")
                    show videov_Monica_Banker_Sex1_8
                    with fade
                    banker "Еще немного!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")



                    sound ahhh3
                    imgd 34052
                    m "АААА!!!"
                    imgd 34053
                    w

                    #9
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_9= Movie(play="video/v_Monica_Banker_Sex1_9.mkv")
                    show videov_Monica_Banker_Sex1_9
                    with fade
                    banker "Быстрее! Давай!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    sound hlup25
                    imgd 34060
                    w
                    imgd 34053
                    w

                    #10
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Monica_Banker_Sex1_10= Movie(play="video/v_Monica_Banker_Sex1_10.mkv")
                    show videov_Monica_Banker_Sex1_10
                    with fade
                    banker "Дааааа..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    sound hlup25
                    img 34060 vpunch
                    m "ААААААА!!!"
                    menu:
                        "Кончить на киску Моники.":
                            #$ monicaAshleySexBerkelbauch_cumzone = 3
                            img 34061
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            w
                            img 34062
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            w
                            img 34063
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan18
                            banker "Оооох..."
                            sound hlup10
                            imgd 34064
                            banker "Ммммммм..."
                            imgf 34065
                            w
                            pass
                        "Кончить внутрь Моники.":
                            #$ monicaAshleySexBerkelbauch_cumzone = 4
                            img 34053
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            w
                            img 34060
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            w
                            img 34066
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan18
                            banker "Оооох..."
                            sound2 chpok6
                            imgd 34067
                            banker "Ммммммм..."
                            pass
            pass
        "Не делать этого!":
            #$ monicaAshleyBerkelbauch3 = day # Моника отказалась удовлетворять банкира
            music Power_Bots_Loop
            img 34005 vpunch
            m "Я не собираюсь делать этого!"
            m "Я тебе не проститутка какая-нибудь!"
            ## затемнение, звук надевания одежды
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 33975 hpunch
            ashley "[monica_pub_name]! Не смей так говорить!"
            ashley "У тебя есть обязанности, которые ты должна выполнять!"
            ashley "Делай, как тебе говорят!"
            imgd 33976
            m "Нет! Я Королева и мне плевать на какие-то там обязанности!"
            # Моника разворачивается и уходит
            sound highheels_short_walk
            imgf 34006
            mt "Пошла эта Эшли к черту!"
            mt "Пусть сама кривляется перед банкиришкой!"
            mt "Гребаная дура!"
            mt "!!!"
            # затемнение
            fadeblack
            sound highheels_short_walk
            pause 2.0
            return
    # банкир расслабленно откидывается на диван
    # Моника встает рядом с диваном и зло смотрит на банкира и на Эшли
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Power_Bots_Loop
    imgf 34068
    w
    imgd 34069
    mt "Омерзительно! Грязно!"
    mt "Гадко! Фу!"
    mt "Меня тошнит от него!"
    mt "От всех их тошнит!!!"
    mt "Взорву к чертям эту гребаную дыру!!!"
    mt "!!!"
    # Эшли спрашивает у банкира
    music Groove2_85
    imgf 34070
    w
    imgd 34071
    ashley "Ну как, Мистер Беркельбаух?"
    ashley "Банк одобряет мне кредит?"
    banker "Хе-хе!"
    imgf 34072
    banker "Королева твоего заведения постаралась, поэтому..."
    banker "Поздравляю тебя, Эшли. Оценка платежеспособности заведения прошла успешно."
    banker "Завтра можешь прийти ко мне в офис."
    banker "Мы подпишем все необходимые документы."
    # Эшли довольно улыбается
    imgd 34073
    ashley "Как здорово!"
    ashley "Спасибо огромное, Мистер Беркельбаух!"
    ashley "Вы меня так выручаете!"
    banker "Обращайся, Эшли! Хе-хе!"
    # смотрит на Монику
    imgf 34074
    banker "Я к тебе еще вернусь, Королева Shiny Hole..."
    # Моника сердито смотрит и думает
    music Pyro_Flow
    mt "Ненавижу этого банкиришку!"
    mt "И извращенку Эшли ненавижу!"
    if monicaBitch == True:
        $ notif_monica()
        mt "Мерзкие жалкие людишки!"
        mt "Они у меня все до единого поплатятся за то, что мне приходится терпеть!"
    mt "!!!"
    # затемнение
    fadeblack
    sound snd_fabric1
    pause 2.0
    sound highheels_short_walk
    pause 1.5
    return


label gallery_34102:
    # Эшли стоит перед банкиром и неуверенно мнется
    music Hidden_Agenda
    imgf 33998
    ashley "Мистер Беркельбаух, я..."
    music Groove2_85
    img 34081
    banker "Эшли, тебе нужна новая кредитная линия?"
    ashley "Да, Мистер Беркельбаух."
    banker "Тебе придется что-то придумать, Эшли, чтобы исправить это недоразумение с этой Королевой..."
    banker "Например, танцевать вместо нее..."
    music stop
    sound plastinka1b
    img 34082 hpunch
    ashley "Я?! Вместо [monica_pub_name]?!"
    # Эшли нервно хихикает
    music Groove2_85
    ashley "Мистер Беркельбаух, я это... В общем..."
    banker "Подумай, прежде чем дать ответ мне, Эшли."
    imgd 34083
    ashley "Ну вы же сами видели, что моя попа..."
    ashley "Не такая красивая, как у остальных девочек."
    banker "За неимением лучшего, Эшли, я готов это потерпеть."
    banker "Поэтому лезь на стол, не теряй времени..."
    # Эшли уже ставит одну ногу на стол, но продолжает отнекиваться
    fadeblack 1.5
    music Groove2_85
    sound heel1
    imgf 34084
    w
    imgd 34085
    w
    imgd 34086
    ashley "Но, Мистер Беркельбаух, я ведь не умею так, как [monica_pub_name]..."
    banker "Если ты хочешь новый кредит, то тебе придется постараться, Эшли."
    # Эшли уже залезла на стол, но не прекращает попыток отмазаться
    fadeblack
    sound heel1
    pause 1.5
    music Groove2_85
    imgfl 34087
    ashley "Я... А вдруг сюда зайдет Джо?"
    ashley "Он вечно пытается контролировать девочек на приватах."
    banker "Я уже был на нескольких приватных танцах здесь и Джо ни разу не заходил."
    imgf 34088
    banker "Эшли, я уже начинаю скучать."
    banker "Из-за этого я обычно становлюсь нервным и со мной сложнее договориться."
    banker "Поэтому советую тебе начинать танец."
    # Эшли неуверенно смотрит на него
    music Hidden_Agenda
    imgd 34089
    ashley "Но, Мистер Беркельбаух..."
    ashley "Может, мы с вами сможем договориться без этого?"
    ashley "Я ведь не сумею станцевать так, как [monica_pub_name]..."
    music Groove2_85
    imgd 34090
    banker "Что ж, Эшли..."
    banker "Ты могла бы получить кредит уже завтра."
    banker "Но раз ты отказываешься..."
    # банкир встает с дивана
    sound heel1
    imgf 34091
    banker "Тогда я пойду."
    banker "Не вижу смысла тратить время на пустые разговоры."
    banker "Раз не будет нового кредита, который перекроет все твои просрочки..."
    banker "Банк предпримет меры по реализации залога по обеспечению твоих кредитов."
    banker "Эта дыра уйдет с молотка."
    # Эшли его останавливает
    img 34092 vpunch
    ashley "Нет-нет! Мистер Беркельбаух! Не уходите!"
    ashley "Я..."
    ashley "Я сделаю это..."
    # банкир возвращается на свое место на диване
    sound vjuh3
    imgf 34088
    banker "Хорошо, Эшли."
    banker "Можешь начинать."
    # Эшли начинает двигаться
    # банкир смотрит, как она танцует и раздевается, комментируя
    fadeblack 1.5
    music All_Stars_Loop
    imgfl 34093
    w
    imgf 34094
    banker "А ты танцуешь так для своего мужа, Эшли?"
    imgd 34095
    ashley "Нет, Мистер Беркельбаух..."
    imgd 34096
    banker "Я удостоин чести стать первым, Эшли? Хе-хе!"
    banker "Сама хозяйка Shiny Hole танцует для меня."
    # банкир расстегивает ширинку и достает член
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Indo_Rock
    imgf 34097
    banker "Сейчас я буду производить комплексную оценку для обеспечения нового кредита, Эшли."
    banker "Поэтому старайся еще лучше..."
    # Эшли танцеут, банкир теребит свой отросток
    imgd 34098
    w
    imgd 34099
    banker "Да, конечно, это не королевский приват, Эшли..."
    banker "Не уверен, что это тянет на тот кредитный лимит, который ты просишь."
    # Эшли меняет позу
    imgf 34100
    w
    sound vjuh3
    img 34101
    w
    imgf 34102
    banker "Хотя... Если посмотреть с этого ракурса..."
    banker "Все не так уж и плохо."
    banker "Тебе нравится танцевать для меня, Эшли?"
    ashley "Да, Мистер Беркельбаух... Нравится."
    sound vjuh3
    imgd 34103
    ashley "Вы одобрите кредит?"
    banker "Неплохой способ взять кредит в банке, не правда-ли? Хе-хе!"
    banker "Но думаю, что этого недостаточно, Эшли..."
    imgf 34104
    ashley "Мистер Беркельбаух, я стараюсь изо всех сил."
    imgd 34105
    w
    sound Jump2
    img 34106 vpunch
    w
    imgf 34107
    ashley "Вы же сами видите..."
    imgd 34108
    banker "Эшли, ты не достаточно грациозна, чтобы я кончил от твоего танца."
    banker "Поэтому, тебе придется сделать еще кое-что..."
    # показательно смотрит на свой член
    imgd 34109
    banker "Для глубокой оценки платежеспособности клиента..."
    banker "Нужно провести, соответственно, глубокий анализ, Эшли."
    banker "И если я останусь доволен, тогда считай, что кредит тебе одобрен."
    # Эшли смотрит на него в растерянности
    music stop
    sound plastinka1b
    img 34110 hpunch
    ashley "Оценки чего? Платежегодности?"
    music Groove2_85
    ashley "В смысле, глубокой?"
    ashley "Я ничего не понимаю..."
    # банкир подзывает ее к себе ближе
    imgd 34111
    banker "Иди сюда, Эшли."
    banker "Сделай так, чтобы я признал твою платежеспособность удовлетворительной."
    ashley "К-какой?"
    banker "Не вникай, Эшли. Просто сделай это."
    banker "Если ты, конечно, не передумала кредитоваться в нашем банке."
    # Эшли медлит, обиженно смотрит на банкира
    sound heel1
    imgf 34112
    w
    imgd 34113
    ashley "Я..."
    img 34114
    banker "Ты можешь обратиться в другой банк, но я сомневаюсь что кто-то пойдет навстречу твоей финансовой ситуации."
    banker "Только такой кредитный эксперт как я может разглядеть потенциал возврата выданных кредитных средств."
    banker "Сделай это, Эшли. Пойди навстречу кредитной организации."
    imgd 34113
    ashley "Но ведь я..."
    ashley "Вы же знаете, что я замужем..."
    ashley "И я никогда... С другим мужчиной не изменяла Джо..."
    ashley "Это так... Неправильно так договариваться о кредите."
    imgf 34115
    banker "Эшли, ты сама оттягиваешь тот момент, когда банк одобрит тебе требуемую сумму."
    banker "Сумму, необходимую для перекредитования твоих просроченных долгов."
    imgd 34116
    banker "Мне становится скучно... Снова."
    banker "Думаю, что в таком случае, банк тебе вынужден будет отказать."
    img 34117 vpunch
    ashley "Нет-нет! Мистер Беркельбаух..."
    ashley "Может, я вместо этого могу представить вам какое-то обеспечение по новому кредиту?"
    banker "Какое обеспечение ты можешь предоставить, Эшли?"
    banker "У тебя все имеющиеся имущество уже заложено."
    imgd 34109
    banker "И если бы не моя доброта и помощь тебе..."
    banker "У тебя не было бы ни единого шанса получить еще один кредит."
    banker "Понимаешь, о чем я говорю, Эшли?"
    banker "Я на твоем месте не стал бы спорить с представителем банка, то есть со мной..."
    # Эшли молчит
    imgf 34118
    w
    imgd 34119
    banker "Ну? Чего ты ждешь?"
    banker "Я готов дать тебе еще один шанс, чтобы произвести оценку и договориться."
    banker "Иначе..."
    # Эшли приближается к банкиру и наклоняется над его членом
    # ее лицо уже близко к члену
    # он держит член в своей руке и водит головкой по губам Эшли
    label gallery_34124:
    fadeblack
    sound heel1
    pause 1.5
    music Loved_up
    imgfl 34120
    w
    imgf 34121
    w
    sound hlup2
    imgd 34122
    w
    sound hlup2
    imgd 34123
    w
    sound chpok2
    imgd 34124
    w
    imgf 34120
    ashley "А банк мне одобрит всю сумму, которую я просила?"
    banker "Да, Эшли."
    banker "Лизни его."
    ashley "..."
    # Эшли высовывает язык и облизывает головку
    imgd 34125
    w
    sound lick3
    img 34126
    w
    imgf 34127
    ashley "Уже завтра?"
    banker "Завтра, все верно."
    banker "Если ты сможешь сделать чтобы я кончил."
    banker "Возьми его в рот."
    # Эшли неуверенно смотрит на него
    imgd 34120
    banker "Ну, смелее, Эшли."
    ashley "..."
    # Эшли вбирает в себя член банкира и начинает водить головой вверх-вниз
    fadeblack 1.5
    music Loved_up
    sound chpok6
    img 34128 vpunch
    w
    imgd 34129
    w

    #video
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Ashley_Banker_Blowjob1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_1= Movie(play="video/v_Ashley_Banker_Blowjob1_1.mkv")
    show videov_Ashley_Banker_Blowjob1_1
    with fade
    banker "Вот тааак... Хорошо, да..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 34130
    w
    imgd 34131
    w

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_2= Movie(play="video/v_Ashley_Banker_Blowjob1_2.mkv")
    show videov_Ashley_Banker_Blowjob1_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 34132
    w

    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_3= Movie(play="video/v_Ashley_Banker_Blowjob1_3.mkv")
    show videov_Ashley_Banker_Blowjob1_3
    with fade
    banker "Оценка проходит вполне успешно, Эшли..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34133
    w
    imgf 34134
    w

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_4= Movie(play="video/v_Ashley_Banker_Blowjob1_4.mkv")
    show videov_Ashley_Banker_Blowjob1_4
    with fade
    ashley "Мпфхмхпф..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34135
    w

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_5= Movie(play="video/v_Ashley_Banker_Blowjob1_5.mkv")
    show videov_Ashley_Banker_Blowjob1_5
    with fade
    banker "Не отвлекай меня от моей работы своей болтовней."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_6= Movie(play="video/v_Ashley_Banker_Blowjob1_6.mkv")
    show videov_Ashley_Banker_Blowjob1_6
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34136
    w
    imgf 34137
    w

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_7= Movie(play="video/v_Ashley_Banker_Blowjob1_7.mkv")
    show videov_Ashley_Banker_Blowjob1_7
    with fade
    banker "Занимайся своим делом, активнее!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #8
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Blowjob1_8= Movie(play="video/v_Ashley_Banker_Blowjob1_8.mkv")
    show videov_Ashley_Banker_Blowjob1_8
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound hlup25
    imgd 34138
    w
    sound hlup25
    imgd 34137
    w
    sound hlup25
    imgd 34138
    w
    sound hlup25
    imgd 34137
    w
    sound hlup25
    imgd 34138
    banker "Ммммм..."
    # Эшли усокряется
    # стук в дверь, голос из-за двери
    imgf 34139
    joe "Эшли! Ты куда пропала?!"
    # Эшли испуганно, с широко открытыми глазами смотрит на банкира, не вынимая его член из своего рта
    sound snd_door_knock
    img 34140
    sound2 Jump2
    joe "Эй, ты тут?"
    joe "Эшли!"
    # Эшли выпускает его член и испуганно
    music stop
    sound plastinka1b
    img 34141 hpunch
    ashley "Черт!!!"
    music Turbo_Tornado
    ashley "Это Джо!!!"
    imgd 34135
    banker "Муж? Хе-хе!"
    banker "Прячься! Чего ты смотришь на меня?"
    ashley "Куда?!"
    ## думаю будет лучше заменить "Это удобное место" (в следующей строчке), на "Там он тебя не увидит."
    banker "Прыгай за диван. Это удобное место..."
    banker "Там он тебя не увидит."
    # Эшли бежит за диван
    sound running
    sound2 snd_door_knock
    img 34142 vpunch
    w
    sound Jump2
    img 34143 hpunch
    w
    # в подсобку заходит Джо
    fadeblack
    sound snd_door_open1
    pause 1.5
    music Groove2_85
    imgf 34144
    joe "Эшли..."
    sound Jump1
    img 34145 vpunch
    joe "Ой, Мистер Беркельбаух?!"
    joe "Это вы здесь?"
    joe "А я подумал, что Эшли..."
    joe "А вы тут кого-то ждете?"
    # кадр на голую Эшли за диваном
    imgd 34146
    ashley "Чертов Джо! Скотина!"
    ashley "Какого хрена он шарахается по бару вместо того, чтобы работать?!"
    ashley "Бездельник!!!"
    # банкир с покерфейсом
    imgf 34147
    banker "Да, Джо... Я жду эту вашу королеву."
    # Джо любезно извиняется, ведет себя подчеркнуто вежливо, улыбается заискивающе
    ## было бы интересно если бы Джо сказал, что Моника горячая штучка и что он ее "пробовал" и это услышала бы Эшли
    music Hidden_Agenda
    imgd 34148
    joe "Ой, извините меня, Мистер Беркельбаух!"
    joe "Я не хотел вас потревожить."
    joe "Не буду отвлекать вас."
    joe "Приятного вам вечера!"
    imgd 34149
    banker "Да-да... Тебе тоже, Джо."
    joe "Спасибо, Мистер Беркельбаух! До свидания!"
    banker "Ага..."
    sound man_steps
    imgf 34150
    w
    fadeblack
    sound snd_door_open1
    pause 1.5
    music Groove2_85
    # Джо выходит
    # банкир поворачивает голову и смотрит за диван
    imgf 34151
    banker "Эшли, продолжим оценку платежеспособности?"
    # Эшли напряженно
    sound vjuh3
    img 34152
    ashley "Джо ушел?"
    banker "Да, Эшли, твой муж ушел. Хе-хе!"
    banker "Возвращайся на свою прежнюю позицию."
    # Эшли подходит к нему, неуверенно
    label gallery_34160:
    fadeblack
    sound man_steps
    pause 2.0
    music Hidden_Agenda
    imgfl 34113
    ashley "Мистер Беркельбаух, я сделала как вы просили."
    ashley "Вы уже приняли решение по моей платеже... Как там? Платежегодности?"
    banker "Я еще не признал твою платежеспособность достаточно удовлетворительной."
    # показывает на свой член
    imgf 34109
    banker "Теперь потребуется более глубокий анализ, Эшли."
    music Groove2_85
    ashley "Ч-что?"
    # банкир подрачивает и смотрит на киску Эшли
    imgd 34114
    banker "Сядь на мой член, Эшли."
    banker "И подвигай своей попкой."
    ashley "Но!"
    banker "И после этого мы завершим оценку твоей платежеспособности."
    imgd 34118
    ashley "Мы так не договаривались, Мистер Беркельбаух!"
    ashley "После того, как меня чуть не увидел мой муж..."
    ashley "Как вы можете требовать это от меня?!"
    # банкир с деланным разочарованием
    menu:
        "Боюсь, Эшли, наши переговоры зашли в тупик... (in Extra version) (disabled)" if game.extra == False:
            pass
        "Боюсь, Эшли, наши переговоры зашли в тупик..." if game.extra == True: # экстра
            #$ monicaAshleyBerkelbauch6 = day # Эшли согласилась на секс с банкиром
            pass
        "Мне надоело это, Эшли...":
            imgf 34119
            banker "Банк выдвинул тебе свои условия, Эшли."
            banker "И тебе радоваться бы, что у тебя появился хоть какой-то шанс получить новый кредитный лимит."
            banker "Для этого требовалось всего лишь выполнить небольшое неформальное условие."
            banker "Сделать так, чтобы я кончил."
            imgd 34153
            banker "В общем, мне надоело это."
            banker "Твои девочки неспособны сделать это."
            banker "Сама ты также неспособна."
            banker "У меня нет времени на все это."
            # банкир встает, собирается уходить
            img 34154 vpunch
            ashley "!!!"
            ashley "Но, Мистер Беркельбаух!"
            ashley "Я ведь все сделала, как вы просили!"
            # он хитро смотрит на нее
            imgf 34113
            w
            imgd 34114
            banker "..."
            banker "Ладно, черт с тобой."
            banker "Придешь завтра в мой офис для оформления документов. Без опозданий."
            imgd 34118
            ashley "Спасибо, Мистер Беркельбаух..."
            imgf 34119
            banker "Видишь, как Мистер Беркельбаух добр к тебе, Эшли?"
            ashley "..."
            imgd 34118
            banker "Теперь ты моя должница. Хе-хе!"
            banker "В следующий раз я не приму никаких отказов и отговорок, Эшли!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound snd_door_open1
            pause 1.5
            # уходит
            scene black_screen
            with Dissolve(1)
            music stop
            call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_21
            scene black_screen
            with Dissolve(1)
            music Pyro_Flow
            music2 pub_noise1_low
            imgf 31333
            w
            img 31334 vpunch
            ashley "Джо, какого черта ты шляешься по бару без дела?!"
            ashley "Быстро вымыл все бокалы, бездельник!"
            joe "Эшли, я..."
            # толкает его ногой
            sound Jump2
            img 31336 hpunch
            ashley "Заткнись, лентяй!"
            ashley "Пошел работать!"
            music2 stop
            # затемнение
            return
    imgf 34153
    banker "Боюсь, Эшли, наши переговоры зашли в тупик..."
    banker "Банк выдвинул тебе свои условия, Эшли."
    banker "И тебе радоваться бы, что у тебя появился хоть какой-то шанс получить новый кредитный лимит."
    banker "Для этого требовалось всего лишь выполнить небольшое неформальное условие."
    imgd 34154
    banker "Сделать так, чтобы я кончил."
    banker "В общем, мне надоело это."
    banker "Твои девочки неспособны сделать это."
    banker "Сама ты также неспособна."
    banker "Мы закрываем этот вопрос без возможности возобновить наши переговоры. Я ухожу."
    img 34155 vpunch
    ashley "!!!"
    ashley "Мистер Беркельбаух!"
    banker "Что, Эшли?"
    ashley "..."
    banker "Иди сюда. Я жду..."
    # Эшли подходит к банкиру и садится на него или наклоняется, упершись руками на стол и подставляет ему зад
    fadeblack
    sound heel1
    pause 2.0
    music Loved_up
    imgfl 34156
    banker "Ну вот. Другое дело, Эшли..."
    # он вставляет в нее свой член

    #video
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Ashley_Banker_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_1= Movie(play="video/v_Ashley_Banker_Sex1_1.mkv")
    show videov_Ashley_Banker_Sex1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 34157
    w
    imgd 34158
    w

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_2= Movie(play="video/v_Ashley_Banker_Sex1_2.mkv")
    show videov_Ashley_Banker_Sex1_2
    with fade
    banker "Мммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 34159
    w

    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_3= Movie(play="video/v_Ashley_Banker_Sex1_3.mkv")
    show videov_Ashley_Banker_Sex1_3
    with fade
    banker "Я знал, что такая умная и деловая женщина, как ты..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 34160
    banker "Не упустит свой шанс..."

    imgf 34161
    banker "Оооо..."

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_4= Movie(play="video/v_Ashley_Banker_Sex1_4.mkv")
    show videov_Ashley_Banker_Sex1_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34162
    w

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_5= Movie(play="video/v_Ashley_Banker_Sex1_5.mkv")
    show videov_Ashley_Banker_Sex1_5
    with fade
    banker "Двигай своей попой по-активнее..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34163
    banker "От нее сейчас зависит решение банка."

    imgd 34164
    w

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_6= Movie(play="video/v_Ashley_Banker_Sex1_6.mkv")
    show videov_Ashley_Banker_Sex1_6
    with fade
    banker "Да, тааак..."
    banker "Ааааа..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 34165
    w

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_7= Movie(play="video/v_Ashley_Banker_Sex1_7.mkv")
    show videov_Ashley_Banker_Sex1_7
    with fade
    banker "Старайся лучше, Эшли!"
    banker "Давай!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Loved_up2
    imgd 34166
    w
    sound hlup25
    imgd 34167
    w
    sound hlup25
    imgd 34166
    w
    sound hlup25
    imgd 34167
    w

    #8
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.166666666666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Ashley_Banker_Sex1_8= Movie(play="video/v_Ashley_Banker_Sex1_8.mkv")
    show videov_Ashley_Banker_Sex1_8
    with fade
    banker "Оценка почти завершена! Оооо..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    sound hlup25
    imgd 34166
    w
    sound hlup25
    imgd 34167
    banker "Еще немного!"
    banker "Дааааа..."
    menu:
        "Кончить на киску Эшли.":
            ## на попу удобнее, так как она задом к нему
            #$ monicaAshleySexBerkelbauch_cumzone = 5
            img 34168
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            banker "Оооох..."
            img 34172
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 34173
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            banker "Ммммммм..."
            sound hlup10
            imgd 34174
            w
            imgf 34175
            w
            pass
        "Кончить внутрь Эшли.":
            #$ monicaAshleySexBerkelbauch_cumzone = 6
            img 34168
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            banker "Оооох..."
            img 34169
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            banker "Ммммммм..."
            imgd 34170
            sound2 chpok6
            w
            imgf 34171
            w
            pass
    # банкир расслабленно откидывается на диван
    # Эшли смотрит на него вопросительно
    fadeblack 2.0
    music Groove2_85
    imgfl 34070
    w
    imgf 34176
    ashley "..."
    ashley "Мистер Беркельбаух, вы получили что хотели?!"
    banker "Хе-хе!"
    ashley "Банк одобряет мне кредит?"
    imgd 34177
    banker "Поздравляю тебя, Эшли. Оценка прошла успешно."
    banker "Завтра можешь прийти ко мне в офис."
    banker "Мы подпишем все необходимые документы."
    # Эшли обиженно
    imgf 34178
    banker "Ты довольна, Эшли?"
    ashley "!!!"
    banker "Эшли, я повторяю, ты довольна сотрудничеством с представителем кредитного отдела?!"
    ashley "Да, Мистер Беркельбаух..."
    ashley "Вы меня так выручаете..."
    imgd 34179
    banker "Обращайся, Эшли! Хе-хе!"
    ashley "Мистер Беркельбаух, пожалуйста, пусть это останется между нами."
    ashley "Никому не стоит знать, что..."
    banker "Эшли, результаты финансового анализа являются собственностью банка и не подлежат разглашению."
    ashley "Спасибо... Мистер Беркельбаух..."
    # затемнение, спустя несколько минут
    # барная стойка, Эшли и Джо
    # Эшли наезжает на Джо
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_22
    scene black_screen
    with Dissolve(1)
    music Pyro_Flow
    music2 pub_noise1_low
    imgf 31333
    w
    img 31334 vpunch
    ashley "Джо, какого черта ты шляешься по бару без дела?!"
    ashley "Быстро вымыл все бокалы, бездельник!"
    joe "Эшли, я..."
    # толкает его ногой
    sound Jump2
    img 31336 hpunch
    ashley "Заткнись, лентяй!"
    ashley "Пошел работать!"
    music2 stop
    # затемнение
    return
