default monicaBiffInvestorsPhilip1 = 0 # Моника осталась у Филиппа после презентации, дождавшись его в гостиной
default monicaBiffInvestorsPhilip2 = 0 # Моника согласилась отработать в БДСМ-ной комнате у Филиппа
default monicaBiffInvestorsPhilip3 = 0 # Моника отказалась быть рабыней у Филиппа
default monicaBiffInvestorsPhilip4 = 0 # Моника согласилась, что Филипп поступил как джентельмен
default monicaBiffInvestorsPhilip5 = 0 # Моника смотрела, как Филипп унижает мышь (писсинг)


default ep217_dialogues5_phillip_cumzone = 0

define v_Monica_Philip_Anal1_1_sound_name = "v_Monica_Philip_Anal1_1"
define v_Monica_Philip_Anal2_sound_name = "v_Monica_Philip_Anal2"

#call ep217_dialogues5_phillip_1() # гостиная в доме Филиппа
#call ep217_dialogues5_phillip_2() # БДСМ-комната
#call ep217_dialogues5_phillip_3() # после сцены Моника стоит возле дома Филиппа, мысли
#call ep217_dialogues5_phillip_4() # после сцены Моника стоит возле дома Филиппа, если хочет вернуться к нему, мысли
#call ep217_dialogues5_phillip_5() # если была сцена БДСМ и Моника в другой день приходит к Филиппу работать субботней шлюхой
#call ep217_dialogues5_phillip_6() # мысли, если убежала от Филиппа и не было сцены в БДСМ-комнате


# после лейбла ep217_dialogues6_office_6
# звук мотора, каблуки, дверь
# гостиная в доме Филиппа
label ep217_dialogues5_phillip_1:
    # Моника с Филиппом стоят в гостиной, Филипп в костюме, Моника в своем красном платье
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 32994
    w
    imgd 32995
    philip "Миссис Бакфетт, будьте любезны..."
    philip "Подождите здесь буквально пару минут..."
    philip "Я сейчас вернусь к вам."
    # он выходит из гостиной, Моника остается одна
    # Моника с подозрением
    sound man_steps
    imgf 32996
    w
    fadeblack 1.5
    music Pyro_Flow
    imgfl 32997
    mt "Зачем этот мерзавец привез меня сюда?!"
    mt "Чего он хочет?!"
    mt "???"
    # если Моника работала у Филиппа субботней шлюхой
    if monica_philip_visits > 1:
        imgf 32998
        mt "Если он думает, что я буду заниматься с ним всякими извращенскими мерзостями..."
        mt "То он ошибается!!!"
        mt "Пусть кувыркается со своей проституткой!"
    # если не работала субботней шлюхой
    else:
        imgf 32999
        mt "Что этот мерзкий Филипп?!"#дописать 'задумал'
        mt "Что бы это ни было..."
        mt "Я не собираюсь играть в его извращенские игры!"
        #
    music Stealth_Groover
    imgd 33000
    mt "Я Миссис Моника Бакфетт, а не какая-то падшая женщина!"
    mt "!!!"
    mt "Черт!"
    imgf 33001
    mt "Презентация перед инвесторами и я, владелица самого крупного журнала страны..."
    mt "В костюме с вырезом на попе!"
    mt "Кошмар!!!"
    # если администраторша говорила Монике, что она будет работать с девочками для важных гостей
    if monica_escort_service_started == True:
        imgd 33002
        mt "И эта гребаная администраторша!"
        mt "Я была так близка к провалу!!!"
        mt "Буквально одно ее слово при инвесторах и мерзавце Бифе..."
        mt "И они узнали бы, что эскорт - мой дополнительный источник дохода!"
        mt "Что бы я тогда делала?!"
        mt "Я даже думать боюсь о том, какие чудовищные последствия меня ожидали бы в таком случае!"
        #
    imgd 33003
    mt "Моника, сегодня был ужасный день!"
    mt "Но ты справилась со всеми трудностями."
    mt "Я горжусь тобой, Моника!"
    mt "Ты вышла с достоинством из такой непростой для тебя ситуации!"
    mt "Осталось побыстрее отвязаться от этого мерзавца Филиппа..."
    imgd 33004
    mt "..."
    mt "Интересно, о чем он шептался с сучкой-администраторшей?"
    mt "???"
    mt "И вообще!"
    mt "Какого черта я тут стою и жду этого негодяя?!"
    menu:
        "Подождать.":
            $ monicaBiffInvestorsPhilip1 = day # Моника осталась у Филиппа после презентации, дождавшись его в гостиной
            pass
        "Убежать! (Филипп запомнит это)":
            music Pyro_Flow
            imgf 33005
            mt "Я не собираюсь тут оставаться ни секунды!"
            mt "Пошли они все к черту!"
            mt "!!!"
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Моника убегает
            return False
    # Моника задумчиво
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 33007
    mt "С другой стороны..."
    mt "А вдруг он меня сюда привез, чтобы дать согласие на инвестицию в журнал?"
    mt "Ведь это логично..."
    imgf 33006
    mt "Этому никчемному жадному неудачнику настолько понравилась моя презентация..."
    mt "Его настолько потряс проведенный мною глубокий анализ работы журнала..."
    mt "Ведь это были не просто пошлые фотографии, а действительно какие-то графики..."
    mt "Что он понял, что это действительное выгодное для него вложение денег."
    mt "Да, думаю, что это так."
    imgd 33008
    mt "Интересно, какую сумму он хочет инвестировать?"
    mt "Может, он сейчас пошел к сейфу, чтобы взять оттуда деньги..."
    mt "И передать мне."
    mt "Это было бы просто замечательно, Моника!"
    imgf 33009
    mt "Бифу с этих денег не достанется ни цента!"
    mt "Этот мерзавец заставил меня сегодня сгорать от стыда перед инвесторами!"
    mt "Ненавижу его!"
    mt "Куплю на эти деньги яд и отправлю мерзавца!"
    mt "Или найму киллера!"
    sound highheels_short_walk
    imgd 33010
    mt "А остальные деньги потрачу на шоппинг и СПА."
    mt "Ты это заслужила, Моника..."
    mt "Ты с достоинством настоящей леди преодолела столько трудностей..."
    mt "Потому что ты и есть истинная леди!"
    mt "Леди Моника Бакфетт!"
    mt "!!!"
    # в гостиную заходит Филипп, в домашнем аутфите
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 33011
    w
    imgf 33012
    mt "Что это такое?"
    mt "Зачем он нацепил на себя это?!"
    mt "И где мои деньги?"
    mt "???"
    # Филипп подходит к Монике
    imgd 33013
    philip "Миссис Бакфетт, спасибо, что дождались меня..."
    philip "Это было неучтиво с моей стороны оставлять вас здесь в одиночестве..."
    m "..."
    philip "Вы сегодня хорошо держались на презентации."
    imgd 33014
    philip "И подобрали для этого случая великолепный костюм."
    philip "Хотя, честно признаться, я вас практически не слушал."
    m "Не слушал?"
    philip "Все это время меня занимала одна мысль..."
    imgf 33015
    m "..."
    philip "Зная о том, что Биф заказал шлюх после презентации."
    philip "Я смотрел на вас, Миссис Бакфетт, и думал..."
    philip "Отсосали ли вы у того работника отеля или отказали ему?"
    if monicaEscortClientHotel8 == True:
        #
        $ notif(_("Моника делала минет слудащему отеля."))
        #
    philip "Если отсосали, то наверняка вам понравилась мысль зарабатывать таким образом деньги..."
    philip "Работая шлюхой в ВИП-эскорте..."
    # Моника возмущенно
    music Power_Bots_Loop
    img 33016 vpunch
    m "!!!"
    m "ЧТО?!"
    m "Я!"
    m "Я не шлюха!!!"
    # Филипп спокойно
    music Groove2_85
    imgd 33017
    philip "Миссис Бакфетт, я сегодня как истинный джентельмен..."
    philip "Спас леди от весьма неловкой ситуации..."
    philip "Вы согласны со мной, что это был поступок джентельмена?"
    menu:
        "Согласится.":
            $ monicaBiffInvestorsPhilip4 = day # Моника согласилась, что Филипп поступил как джентельмен
            pass
        "Убежать! (Филипп запомнит это)":
            music Power_Bots_Loop
            img 33018
            m "Нет!"
            m "Ты мерзавец!"
            m "Я не собираюсь тут оставаться ни секунды!"
            imgf 33019
            sound highheels_run2
            w
            imgd 33020
            mt "Пошел он к черту!"
            mt "!!!"
            fadeblack
            sound highheels_run2
            pause 2.0
            # Моника убегает
            return False
    imgf 33021
    mt "К чему этот гад ведет разговор?!"
    mt "?!"
    mt "Я и без его помощи смогла бы выкрутиться из той ситуации!"
    mt "Я сильная и независимая женщина!"
    mt "!!!"
    music Hidden_Agenda
    imgd 33022
    mt "Но, пожалуй, с моей стороны будет умным ходом..."
    mt "Согласиться с ним сейчас."
    mt "Возможно, что он все-таки даст свое согласие на инвестицию..."
    m "Да, я согласна..."
    music Groove2_85
    imgf 33023
    philip "Хорошо, Миссис Бакфетт..."
    philip "Я рад, то мы пришли к взаимопониманию."
    philip "И поскольку я спас вас сегодня, то..."
    philip "Мне было бы приятно провести этот вечер в вашей компании..."
    imgd 33024
    philip "И кое-что обсудить."
    philip "Даже не обсудить... Я немного неверно подобрал выражение..."
    philip "Я хочу сделать вам весьма выгодное предложение, Миссис Бакфетт."
    philip "И надеюсь, что вы согласитесь его принять..."
    # Моника смотрит на него с подозрением
    imgf 33021
    mt "Какой-то он странный..."
    mt "Мне кажется, что он задумал какую-нибудь гадость..."
    mt "..."
    mt "Но мне нужно послушать, что он хочет мне предложить."
    mt "В любом случае я могу отклонить его предложение и уйти отсюда!"
    imgd 33025
    m "Что за предложение, Филипп?"
    philip "Пройдемте для начала нашего разговора в более подходящее место."
    philip "Вы ведь еще не видели мой дом?"
    imgd 33026
    # если работает у него субботней шлюхой
    if monica_philip_visits > 1:
        philip "Только эту гостиную, верно?"
        #
    philip "Пройдемте, Миссис Бакфетт..."
    philip "Я хочу вам кое-что показать."
    # затемнение, шаги
    return True

# БДСМ комната
label ep217_dialogues5_phillip_2:
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
            $ monicaBiffInvestorsPhilip2 = day # Моника согласилась отработать в БДСМ-ной комнате у Филиппа
            pass
        "Убежать! (Филипп запомнит это)":
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
            return False
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
    $ ep217_dialogues5_phillip2_loop1_flag = False
    $ ep217_dialogues5_phillip2_loop1b_flag = False
label ep217_dialogues5_phillip2_loop1:
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
                    $ ep217_dialogues5_phillip2_loop1b_flag = True
                    jump ep217_dialogues5_phillip2_loop1
                "У меня болит попа!":
                    imgf 33122
                    m "Филипп, у меня болит попа!"
                    philip "Я сегодня спас эту попу от позорного разоблачения."
                    philip "Ей бы пришлось намного хуже, если бы не мой поступок."
                    menu:
                        "Промолчать" if ep217_dialogues5_phillip2_loop1_flag == True:
                            pass
                        "Мне больно!":
                            $ ep217_dialogues5_phillip2_loop1_flag = True
                            imgd 33119
                            m "Филипп, мне больно!"
                            philip "Вы сами согласились на это, Миссис Бакфетт."
                            jump ep217_dialogues5_phillip2_loop1
                "Промолчать" if ep217_dialogues5_phillip2_loop1_flag == True:
                    pass
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
    $ ep217_dialogues5_phillip2_loop2 = False
    $ ep217_dialogues5_phillip2_loop2b = False
label ep217_dialogues5_phillip2_loop2:
    menu:
        "Филипп, я не давала согласия на подобное!":
            music Power_Bots_Loop
            imgd 33120
            m "Филипп..."
            m "Я не соглашалась на подобное!"
            philip "Вы сами согласились поехать ко мне домой, Миссис Бакфетт."
            $ ep217_dialogues5_phillip2_loop2b = True
            jump ep217_dialogues5_phillip2_loop2
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
                "Промолчать" if ep217_dialogues5_phillip2_loop2 == True:
                    pass
                "Мне больно!":
                    $ ep217_dialogues5_phillip2_loop2 = True
                    music Power_Bots_Loop
                    imgf 33119
                    m "Филипп, мне больно!"
                    philip "Вы сами согласились на это, Миссис Бакфетт."
                    jump ep217_dialogues5_phillip2_loop2
        "Промолчать" if ep217_dialogues5_phillip2_loop2 == True:
            pass
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
            $ ep217_dialogues5_phillip_cumzone = 1
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
            $ ep217_dialogues5_phillip_cumzone = 2
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
            music Groove2_85
            imgf 33147
            philip "Оно поело?"
            philip "Отвечай. Мастер разрешает ему говорить."
            model1 "Этот раб благодарит Мастера за еду."
            menu:
                "Продолжить смотреть на рабыню (экстремальный контент, Extra version) (disabled)." if game.extra == False:
                    pass
                "Продолжить смотреть на рабыню (экстремальный контент)." if game.extra == True:
                    $ monicaBiffInvestorsPhilip5 = day # Моника смотрела, как Филипп унижает мышь (писсинг)
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
            $ monicaBiffInvestorsPhilip3 = day # Моника отказалась быть рабыней у Филиппа
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
    return True

# после сцены Моника стоит возле дома Филиппа, мысли
label ep217_dialogues5_phillip_3:
    # не рендерить!!
    mt "Боже! Какое унижение!"
    mt "Этот мерзавец надругался над моей попой!"
    mt "У меня до сих пор все болит!!!"
    mt "И все это видела та отвратительная мартышка!!!"
    mt "Какой ужас!!!"
    mt "Филипп оказался настоящим садистом!"
    mt "И он думает, что я могу согласиться стать на неделю его секс-рабыней?!"
    mt "Думает, что я способна на подобное?!"
    mt "Тварь!!!"
    mt "Я заставлю его страдать!!!"
    mt "Он будет долго мучится!!!"
    mt "И молить у меня прощения за все!!!"
    mt "А потом убью его!!!"
    mt "!!!"
    return

# после сцены Моника стоит возле дома Филиппа, если хочет вернуться к нему, мысли
label ep217_dialogues5_phillip_4:
    # не рендерить!!
    mt "Я не пойду туда!"
    mt "Ноги моей больше не будет в этом ужасном месте!"
    mt "Ненавижу мерзавца Филиппа!"
    return False

# если была сцена БДСМ и Моника в другой день приходит к Филиппу работать субботней шлюхой
# в меню выбора - ep210_dialogues2_escort_start_Phillip_12 - вставить if
label ep217_dialogues5_phillip_5:
    philip "Для субботней шлюхи номер 2 есть другое предложение..."
    philip "О котором она знает."
    m "Нет!"
    m "Я не готова терпеть подобные унижения ни за какие деньги!!!"
    m "!!!"
    # Моника оказывается на улице возле дома Филиппа
    return


# мысли, если убежала от Филиппа и не было сцены в БДСМ-комнате
label ep217_dialogues5_phillip_6:
    # не рендерить!!
    mt "Пошел к черту этот гребаный садист!!!"
    mt "И мне плевать на последствия!!!"
    mt "Я не собираюсь быть игрушкой в его руках!!!"
    mt "Мерзкое животное!!!"
    mt "Ненавижу!!!"
    return False
