define cynthia_t = Character(t_("Синтия"), who_color=c_green, what_color=c_gray, what_italic=True) # Cynthia Evans thinking

default mlsBardiFamilyV4Cynthia1 = 0 # Барди помогал Синтии собираться на пижамную вечеринку

#call ep04_dialogues2_family_cynthia_1() # разговор с Синтией в ее комнате
#call ep04_dialogues2_family_cynthia_2() # комната Барди, мечты о Синтии


#ВНИМАНИЕ! Если игрок проходит сцену с Синтией, то сцена Дейзи не доступна до следующего дня!!!

#Сцена Синти возможна лишь в том случае если она видела Барди голым в душе (if mlsBardiDay4FamilyMorning1 > 0)
#Триггер сцены - утром в любой будний день кликнуть но дверь Синти.
#ВНИМАНИЕ! СЦЕНА ОЛИВИИ И СИНТИИ СВЯЗАНЫ т.е если была сцена Синтии то сцена Оливии автоматически проигрывается перед сном.


#Барди просыпается утром от будильника
label ep04_dialogues2_family_cynthia_1a:
    # звонит будильник
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("ВТОРНИК"))
    scene black_screen
    fadeblack 2.0
    music iphone_alarm
    imgfl 901088
    bardi_t "Что, уже утро?!"
    imgd 900063
    bardi_t "..."
    # голос Софи из-за двери
    music Adventures_of_the_Deaf_Dreamer
    imgd 901089
    sophie "[mcname], ты уже встал?" ##->#####inc
    #####inc mother "Сынок, ты уже встал?"
    bardi "Да!"
    sophie "Доброе утро, милый!"
    sound snd_walk_barefoot
    imgf 901087
    w
    fadeblack
    sound put_dress
    pause 1.5
    # Барди встает с постели
    # переход на движок
    return

# при клике на дверь в комнату Синтии
label ep04_dialogues2_family_cynthia_1:
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgf 901685
    bardi_t "Хм..."
    bardi_t "Как там дела у Синтии?.."
    #Бард стучит в комнату ситни
    sound snd_door_knock
    imgd 901686
    w
    cynthia "Заходи!"
    #Бард заходит в комнату синти
    #Звук закрывающейся двери
    # смена кадра - комната Синтии
    #На столе у Синтии должна лежать какая-нибудь сумочка.
    #в конце сцены она схватит ее и убежит по делам. подберите что-то миленькое под стать ее наряду в конце.
    #Синти стоит спиной к Барду голая. (если точнее 3\4 но со спины). подбирает одежду.
    sound snd_door_open1
    fadeblack 1.0
    imgfl 901687
    music Stylish_Hip_Hop_Rock
    sound2 wow
    with vpunch
    bardi_t "Оу! Ни хрена себе!.."
    imgf 901688
    cynthia "Ой, а я уже заждалась тебя..."
    bardi_t "Меня?!"
    cynthia "Наконец-то, ты пришла, Оливия... Честно говоря, я уже думала ты не успеешь..."
    bardi "???"
    #Синти замечает барда краем глаза
    #Синти поворачивается к барду. Смотрит на него озадаченным взглядом.
    music stop
    sound plastinka1b
    img 901689 hpunch
    sound2 fear2
    cynthia "Ой!.."
    #Бард отвернулся.
    sound Jump2
    img 901690 vpunch
    bardi "Ой! Прости!"
    music Step_By_Step
    bardi "Ты сказала входить... Я не думал, что ты переодеваешься..."
    cynthia "Я думала это Оливия. Она обещала помочь мне с выбором одежды..."
    cynthia "Подожди минутку."
    imgd 901691
    bardi_t "Черт! Она что, вообще не стесняется меня?!"
    bardi_t "А где эти клишированные крики и визги, как в фильмах?"
    bardi_t "Фак! А фигура то у нее офигенная!.."
    bardi_t "Так, стоп! Не думай об этом! Только бы не возбудиться..."
#    sound2 put_dress
    cynthia "Все. Можешь смотреть."
    #Бард оборачивается и смотрит на Сини.
    #Синти стоит перед бардом в нижнем белье в какой-то милой позе с вопросительным выражением лица и легкой улыбкой.
    music Little_Tomcat
    imgf 901692
    cynthia "Ну как тебе?"
    imgd 901693
    bardi "..."
    #Синти радостная.
    imgd 901692
    cynthia "Ты чего? Язык проглотил?"
    imgd 901693
    bardi "А? Нет-нет."
    bardi "Белье отпад. Тебе очень идет, Синтия."
    #Синти задумчивая смотрит в сторону. Будто витает в своих мыслях..
    music Stylish_Hip_Hop_Rock
    imgfl 901694
#    sound2 wow
    show screen image_shake("/images/Slides/img_901694.jpg")
    w
    imgf 901695
    show screen image_shake("/images/Slides/img_901695.jpg")
    w
    imgd 901696
    cynthia "Хмм... Мне тоже так кажется, но нужно посмотреть и другие комплекты."
    music Little_Tomcat
    imgd 901697
    bardi_t "Что? Ей вообще плевать, что я завалился к ней, когда она была голой?.."
    bardi "Слушай, прости, что так неожиданно ввалился когда ты переодевалась... Я правда не знал."
    #Синти смотрит на барда удивленно
    imgd 901698
    cynthia "Что?"
    #Синти нейтральная
    imgd 901699
    cynthia "А, ты об этом?.. Да не переживай, все хорошо."
    #Усмехнувшись Синти махнула рукой.
    imgd 901700
    w
    img 901701
    w
    imgd 901702
    cynthia "Я вообще-то думала, что это Оливия. Но в любом случае, я ведь сама сказала тебе входить..."
    cynthia "Я никого не стесняюсь в этом доме. Ни маму, ни папу, ни Оливию. Так что все окей."
    imgd 901703
    bardi "Но... Я же парень..."
    imgd 901704
    cynthia "Ну и что?"
    cynthia "Моя мама и твой отец хорошие друзья. Мы сейчас живем в одном доме. Ты мне почти как брат, а я почти что твоя сестра." ##->#####inc
    #####inc cynthia "Ты же мой брат, а я твоя сестра. Хоть отцы у нас и разные, но мать одна."
    imgd 901703
    bardi_t "Господи, да что ты такое несешь?!"
    bardi_t "Я парень, а у тебя офигенное сексуальное тело!"
    bardi_t "При этом впервые мы увиделись несколько дней назад! Я чисто физически не могу воспринимать тебя как сестру!"
    #Синти с ошарашенным выражением лица.(Не прям офигевшим, но таким, будто она внезапно поняла что-то)
#    sound2 fear2
    imgd 901705
    cynthia "Ой!.."
    #Синти виноватым взглядом смотрит на Барда.
    cynthia "Прости, [mcname]. Мы ведь не так давно живем вместе и ты, наверное, не привык к подобному."
    cynthia "И ко мне еще не привык..."
    imgd 901706
    bardi "Нуу... Как тебе сказать?.."
    #Синти с виноватой улыбкой.
    imgd 901705
    cynthia "Просто мне так комфортно. Я не хочу стесняться кого-либо, с кем живу под одной крышей."
    imgd 901706
    bardi_t "Сказала бы ты мне это, когда ввалилась ко мне в душ!"
    #Синти смущенно смотрит в сторону
    imgd 901707
    cynthia "Разве это не правильно, что в такой ситуации я пытаюсь воспринимать тебя как брата? Просто мне кажется, что по другому быть и не должно..." ##->#####inc
    #####inc cynthia "А ты мой братик. Мне кажется, что по другому быть и не должно..."
    music Step_By_Step
    imgd 901708
    bardi_t "Господи, какая же ты невинная!.. Сколько же всего ты не знаешь..."
    bardi_t "Да половина сюжетного порно выпускается под названием 'Брат отымел сестру'..."
    #Синти робко смотрит в сторону виноватым взглядом поза зажатая, робкая.
    bardi "Все окей, Синтия. Ты, в принципе, права. Мы все живем под одной крышей." ##->#####inc
    #####inc bardi "Все окей, сестренка. Ты, в принципе, права."
    bardi "Просто мне, действительно, непривычно. Но это дело времени..."
    #Синти переводит взгляд на гг. на лице появляется улыбка.
    imgd 901709
    cynthia "Ты правда так считаешь?"
    imgd 901708
    bardi "Конечно."
    imgd 901702
    cynthia "Отлично!"
    #Синти довольная смотрит в сторону (Это должно выглядеть мило, как зайчик который злится).
    music Little_Tomcat
    imgd 901710
    cynthia "А то Оливия заладила со своим 'никчемный сопляк', 'мелкий извращенец'..."
    cynthia "А я ей говорю, что ты нам почти что брат и не надо так говорить о тебе..." ##->#####inc
    #####inc cynthia "А я ей говорю, что ты наш брат и не надо так говорить о тебе..."
    imgd 901711
    bardi_t "Ну, это вполне в ее духе..."
    #Синти смотрит виноватым робким взглядом на Барди.
    sound fear2
    img 901712 hpunch
    cynthia "Ой! Наверное, не стоило тебе это рассказывать..."
    img 901713
    bardi "Та не переживай. Я знаю об ее отношении ко мне."
    bardi "Она не дает мне это забывать и постоянно хамит мне."
    #Синти возмущенная смотрит в сторону
    imgd 901698
    cynthia "Я этого не понимаю! Ты же такой добрый, такой хороший!.." ##->#####inc
    #####inc cynthia "Я этого не понимаю, братик! Ты же такой добрый, такой хороший!.."
    cynthia "Может я сама, без Оливии, решу как и к кому мне относиться?!"
    cynthia "Я хочу иметь со всеми теплые, доверительные отношения."
    #Синти возмущенная смотрит на барда.
    cynthia "Вот хочу и буду видеть в тебе своего..."
    #Синти косится на вставший член барда. взглядом будто она зависла.
    imgd 911836
    w
    sound erection1
    img 901714
    with Dissolve(1.0)
    pause 0.5
    music stop
    sound plastinka1b
    img 901714 hpunch
    cynthia_t "У него встал?! На меня?!"
    cynthia_t "?!"
    img 901715
    #Бард смотрит на Синти. Она смущенная и красная
    cynthia "Парня..."
#    bardi "Что?"
    music Adventures_of_the_Deaf_Dreamer_short
    cynthia "Ой! Я имела ввиду брата!"
    #Бард опускает взгляд и видит стояк.
    imgd 901716
    bardi "О, чееерт!"
    #Синти зажатая и смущенная смотрит на член.
    img 901717
    cynthia "Что это? У тебя встал?"
    bardi_t "ФАК!"
    imgd 901718
    bardi "Прости! Я же говорил, что еще не до конца привык... Точнее, я то привык, но мое тело - нет..."
    bardi "Это..."
    bardi_t "Фак, и что мне ей сказать?!"
    bardi_t "О! Точно!"
    #Синти переводит взгляд на барда вытянув руки и отказываясь.
    music Step_By_Step
    imgd 901719
    bardi "Это как у тебя в душе, помнишь? Ты ведь покраснела, а потом сбежала..."
    cynthia "Я... Я просто удивилась..."
    cynthia "Это произошло очень неожиданно!.."
    imgd 901718
    bardi "Но если бы вместо меня в душе была Оливия, ты бы могла отреагировать иначе..."
    #Синти виновато смотрит в пол.
    imgd 901720
    cynthia "Ну... Наверное... Я не знаю..."
    cynthia "Прости, в тот момент я правда не думала ни о чем таком..."
    #Синти смотрит на Барди грустная в отчаянии
    imgd 901721
    bardi "Все хорошо, все в порядке. Я тоже ни о чем таком не думал."
    bardi_t "Почти..."
    bardi "Это просто физиология, понимаешь?"
    bardi "Мы впервые увиделись всего пару дней назад. Все из-за этого."
    bardi "Так что, все в порядке. Нужно просто время, чтобы привыкнуть."
    imgd 901722
    sound snd_walk_barefoot
    w
    imgf 901723
    w
    #Синти садится на кровать и опускает взгляд
    #Бард садится рядом.
    imgd 901724
    bardi_t "Что за бред я несу?!"
    bardi_t "Хорошо, что Синтия такая невинная и верит во все."
    imgd 901725
    bardi_t "Оливия бы уже давно оторвала мне голову..."
    sound step_stairs_short
    imgf 901726
    w
    imgd 901727
    bardi "Нам просто нужно проводить побольше времени друг с другом..."
    bardi "Вот так открыто, как сейчас. И тогда мы привыкнем друг к другу."
    #Синти смотрит на барда с виноватой улыбкой
    imgd 901728
    cynthia "Думаешь?"
    imgd 901727
    bardi "Конечно!"
    #Синти решительная. Вся такая боевая, кулачек на уровн лица все дела...
    music Little_Tomcat
    imgd 901729
    cynthia "Да! Ты прав!"
    #Синти робкая и нерешительная, поза соответствующая
    cynthia "Тогда, может ты поможешь мне подобрать одежду?"
    imgd 901727
    bardi_t "Отлично!"
    bardi "Я только за, если тебя не смущает это..." # указывает на свой стояк
    sound vjuh3
    img 901730 hpunch
    w
    #Синти отнекивается тип "Не, чувак все ок! Поза и выражение лица под этот принцип."
    imgd 901731
    cynthia "Нет, все хорошо! Ты же говоришь, что это естественно..."
    cynthia "И, наверное, скоро это пройдет."
    sound snd_walk_barefoot
    imgf 901732
    w
    imgd 901733
    bardi_t "Ох... Сомневаюсь..."
    #Синти встала с кровати и подошла к шкафу. задумчиво смотрит в открытый шкаф.
    #Далее в тексте она не такая уверенная как в самом начале, немного робкая и стеснительная, иногда косится на член барда.
    sound snd_door_locked1
    imgf 901734
    bardi "А для чего ты вообще решила принарядиться?"
    #Синти обернулась на Барда смотрит с непониманием и робостью. поза слегка зажатая, ей немного не по себе.
    imgd 901735
    cynthia "Что?"
    #Синти Жест, бьет себя по лбу тип: "Вот я дура".
    imgd 901736
    cynthia "Ах! Точно!"
    cynthia "Со всем этим... Разговором... Я совсем забыла рассказать..."
    #Синти смотрит на барда в нейтральной позе с улыбкой.
    imgd 901737
    cynthia "Мы с мамой идем в гости к тете Дейзи."
    cynthia "И у нас с Николь будет пижамная вечеринка."
    imgd 901738
    bardi "Ого, звучит весело."
    imgd 901739
    cynthia "Да."
    #Синти косится на член барда
    imgf 901740
    cynthia_t "И как он живет с этой штуковиной?.."
    #Синти смотрит в лево и в правою робко, будто хочет чет спросить но стесняется.
    imgd 901741
    cynthia "Эм... Слушай..."
    imgd 901742
    bardi "Да?"
    img 901741
    cynthia "Хотя нет, ничего..."
    imgd 901742
    bardi "Да говори уже, раз начала."
    #Синти смотрит на барда красная от смущения и робко говорит.
    imgd 901743
    cynthia "Ну, ладно..."
    cynthia "Ну... понимаешь..."
    #Синти указывает пальцем на член барда Очень смущаясь.
    sound Jump1
    imgd 901744
    cynthia "Как ты с этой штукой живешь? Он тебе не мешает?"
    imgd 901745
    bardi "С какой штукой?"
    #Бард смотрит на член.
    #Бард смотрит на Синти.
    imgd 901746
    bardi "А!.."
    music Step_By_Step
    imgf 901747
    bardi "Так он не всегда такой."
    bardi "Но когда поднимается, становится неловко."
    bardi "Особенно, если это происходит само собой."
    #Синти удивленная
#    sound fear2
    img 901748
    cynthia "Это может произойти само собой?"
    imgd 901747
    bardi "Чаще всего так и происходит."
    bardi "Хах! Вообще, это извечная проблема парней."
    bardi "Когда едешь в автобусе к примеру, а тут раз - стояк! А уже твоя остановка..."
    #Синти сочувствующим взглядом смотрит на Барда.
    imgd 901749
    cynthia "Боже! Это же так стыдно!"
    cynthia "Тем более, он такой большой... Как ты это скрываешь?"
    imgd 901747
    bardi "Обычно, хватает подумать о чем-то плохом..."
    #Синти смотрит вопросительным взглядом.
    imgd 901750
    cynthia "Вроде плохого дня или неприятной ситуации?"
    imgd 901747
    bardi "Да, что-то типа того..."
    #Звук открывающейся двери.
    #Оливия входит в комнату втыкая в телефон. во второй руке пакет с магазина одежды. Синти смотрит на нее.
    sound snd_door_open1
    imgf 911226
    sound2 highheels_short_walk
    w
    imgd 911227
    olivia "Так, я тут по пути домой прикупила то, что ты просила. Вроде твой размер..."
    #Оливия прерывается на полуслове, увидев Барди
    #в шоке смотрит на него. Синтия смотрит на Оливию, Барди смотрит на Оливию.
    #Оливия и синти переглядываются переводя взгляды то на Барда то друг на друга.
    music stop
    sound plastinka1b
    img 911228 hpunch
    w
    sound vjuh3
    img 911229
    bardi_t "Так... Чувствую, мне жопа..."
    #Оливия роняет пакет  на пол, держа руки на уровне лица ладонями вниз и делает вдох. выдох.
    sound2 down7
    img 911230 vpunch
    music Fly_With_Me_short
    olivia "Так!"
    #Оливия смотрит на Барди с презрением, как на мусор.
    imgd 911231
    olivia "Синтия, откуда у тебя в комнате этот мусор?!"
    #Оливия смотрит на Синти указывая пальцем в сторону барда. злая как черт. Синти робко зажалась.
    sound Jump1
    img 911232 hpunch
    olivia "И с какого хрена ты ходишь раздетой перед этим придурком!?"
    bardi "Эй! Я, вообще-то, тоже тут!"
    img 911233
    #Оливия смотрит на Барди злющая, аж красная со злости.
    olivia "А ты заткнись, мать твою! Мне плевать!"
    bardi "Я просто помогаю Синтии..."
    olivia "Я сказала тебе заткнуться! Говнюк!"
    #Оливия стоит такая же злая подняв палец вверх.
    imgd 911234
    olivia "Решил воспользоваться наивностью Синтии?!"
    # Барди говорит Синтии
    imgd 911235
    bardi "Вот, видишь? Я же говорил, что она особо не скрывает свое отношение ко мне..."
    #Синтия вступается за Барда вся из себя герой.
    imgd 911236
    cynthia "Я сама позвала его!"
    #Оливия сначала офигевшая удивленная а потом такая же злая гонит на барда.
    olivia "И что?!"
    img 911237
    olivia "Ты мог бы и отказаться, придурок!"
    olivia "Она, вообще-то, переодевается! У тебя что, совсем стыда нет?!"
    #Синти уже рассерженная
    sound Jump2
    img 911238 vpunch
    cynthia "Хватит его оскорблять!!!"
    #Оливия смотрит на Синти рассерженно указывая ладонью на Барда.
    olivia "Называть вещи своими именами - это не оскорбление!"
    #Оливия тычет пальцем в Синти.
    imgd 911232
    olivia "Да и ты тоже! Звать его к себе в комнату?! Постыдилась бы!"
    cynthia "Мы живем под одной крышей! Он нам как брат! А я не собираюсь стесняться кого-то в этом доме!" ##->#####inc
    #####inc cynthia "Вообще-то, он наш брат! И мы живем под одной крышей! С чего бы мне стыдиться?!"
    #Оливия снова тычет пальцем в сторону Барди глядя на Синти. Злющая краснющая. Синти стоит скрестив руки хмуро глядя на Оливию.
    img 911239
    olivia "Какой из этого лошары брат?!"
    #Оливия Смотрит на Барда.
    olivia "Он мелкий извращенец! Ты глянь на него - у него даже сейчас в штанах дымится!"
    imgd 911240
    bardi_t "Твою мать! Она заметила!"
    #Оливия смотрит на синти. руки в боки. Синти все такая же боевая стоит на своем.
    imgd 911241
    olivia "И не говори, что ты не заметила его стояк!"
    olivia "И как, после такого, у тебя язык повернулся назвать его братом?!"
    cynthia "Вообще-то, это просто физиология! Это нормально для парней!"
    olivia "Дай угадать!.. Это он тебе наплел только что?!"
    #Синти растерянная. глазки забегали, но она пытается казаться такой же решительной как и секунду назад.
    img 911242
    cynthia "Нет..."
    #Синти обиженная. руки скрестила, стоит полубоком к Оливии
    cynthia "Я... Я, вообще-то, и сама это знала!"
    sound Jump1
    img 911243 hpunch
    bardi "Так! Оливия, может ты уже прекратишь наезжать на нее?!"
    bardi "Хватит тут командовать и доводить Синтию!"
    #Оливия в афиге смотрит на Барди, затем переводит взгляд на Синти.
    imgd 911244
    olivia "Значит... Я еще и виновата?!"
    olivia "И ты тоже так считаешь, Синтия? Я, по-твоему, сейчас бред несу?!"
    #Оливия злая обращается к Синти, но та на нее даже не смотрит.
    imgd 911245
    olivia "Да я пытаюсь тебя, наивную дурочку, уберечь от этого похотливого извращенца!"
    #Синти кричит на Оливию.
    sound vjuh3
    img 911246
    cynthia "Да что он тебе сделал, чтобы ты так к нему относилась?!"
    cynthia "Хватит вести себя как стерва!"
    #Оливия в шоке, лицо и поза ошарашенные, олицетворяющие ее поражение.
    imgd 911247
    cynthia "И не надо меня ни от кого защищать! Я уже не маленькая! И я не наивная дурочка!"
    cynthia "Я сама разберусь, кому мне доверять, а кому нет!!!"
    olivia "!!!"
    #Оливия снова рассерженная притопнул ногой обращается к Синти.
    img 911248
    olivia "Ах так?!"
    cynthia "ДА!"
    olivia "Ну и ладно! Ну и возитесь тут сами!"
    olivia "Я вижу, моя помощь тебе не нужна! Пусть этот придурок тебе помогает!"
    cynthia "И поможет!!!"
    #Оливия разворачивается и пнув пакет который уронила на пол в начале уходит к двери.
    #Перед уходом оборачивается к Барду и тыча в него пальцем говорит.
    sound highheels_short_walk
    imgd 911249
    w
    sound down10
    img 911250 hpunch
    w
    imgd 911251
    olivia "А с тобой, сволочь, я еще поговорю!"
    bardi "Да пожалуйста. Я всегда открыт для продуктивного диалога."
    sound Jump1
    img 911252 vpunch
    olivia "Да пошел ты!"
    #Оливия уходит и захлопывает за собой дверь.
    #Звук захлопнувшейся двери.
    #Синти расслабляется, будто выдыхает с облегчением.
    sound snd_door_close1
    imgf 911253
    w
    music Little_Tomcat
    imgd 911254
    cynthia "Фух..."
    bardi "Ага."
    #Синти смотрит на барда усталым виноватым взглядом.
    imgd 911255
    cynthia "Прости, у тебя опять из-за меня проблемы..."
    imgd 911256
    bardi "Да причем тут ты? Все окей. Не переживай, Синтия."
    bardi "Я вообще думаю, что и ее тоже можно понять. Я тут недавно... Она просто за тебя переживает..."
    #Синти опустив взгляд в пол.
    imgd 911257
    cynthia "Да, я понимаю. Просто..."
    #Синти смотрит на барда.
    cynthia "Ты же ей ничего не сделал. Да и к чему ей вообще тебя опасаться?"
    #Синти с наигранной улыбкой и виноватым выражением лица.
    imgd 911258
    cynthia "И ты не переживай. Она ничего не сделает."
    cynthia "Она вечно так говорит, а на деле побесится и успокоится."
    music Adventures_of_the_Deaf_Dreamer
    bardi_t "Ох... Надеюсь на это..."
    bardi_t "От этой барышни можно ожидать чего угодно..."
    imgd 911259
    bardi "Ладно. Давай глянем, что она притащила?"
    cynthia "Давай!"
    #Бард встает с кровати и подбирает пакет который пнула Оливия.
    #Бард достает содержимое пакета. В нем миленькое нижнее белье.
    #Переводим взгляд на Синти. Синти слегка смущена. поза тоже смущенная.
    sound step_stairs_short
    imgf 911260
    w
    imgd 911261
    w
    sound vjuh3
    imgd 911262
    bardi "Оу..."
    bardi_t "Черт! А вкус у Оливии, действительно, получше, чем у меня."
    bardi_t "Белье совершенно под стать милой, робкой Синтии."
    #Бард протягивает Синти белье. Синти робко принимает его.
    imgf 911263
    bardi "Примеришь?"
    cynthia "Да..."
    #Синти робко и смущенно косится на Барди.
    imgd 911264
    cynthia "Отвернешься?"
    bardi_t "Черт..."
    bardi "Да, конечно."
    #Бард отворачивается.
    sound step_stairs_short
    imgd 911265
    bardi "..."
    bardi "....."
    bardi "......."
    sound put_dress
    imgf 911266
    cynthia "Все."
    #Бард оборачивается на синти. Синти стоит робкая в новом белье. Знаешь, поза такая миленькая, когда пальчики указательные друг в друга упираются.
    imgd 911267
    bardi_t "Ну ни хрена себе!.."
    cynthia "Ну как тебе?"
    bardi "Боже! Что это за милота?.."
    #Синти краснеет и смотрит в пол улыбаясь.
    music Little_Tomcat
    imgd 911268
    cynthia "Спасибо..."
    cynthia "Я не выгляжу слишком глупо? Просто оно такое миленькое..."
#    imgd 911267
    bardi "Конечно, нет! Миленькое и совершенно под стать тебе!"
    bardi "В этом Оливия, конечно, была права. Вкус у нее явно получше, чем у меня."
    #Синти робким взглядом смотрит на гг с милой улыбкой, чуть красная от смущения.
    imgd 911269
    cynthia "Спасибо."
    # Синти оборачивается к шкафу. Наклоняется чтоб достать что-то из нижней полка. сексуально, но не пошло.
    #Синти так-то милая наивная девочка-зайка.
    imgd 911270
    w
    sound snd_walk_barefoot
    imgf 911271
    sound2 wow
    bardi_t "Вау!.. Какая же охренительная у тебя попка для такой милой и робкой девочки!.." ##->#####inc
    #####inc bardi_t "Вау!.. Какая же охренительная у тебя попка для такой милой и робкой девочки, сестренка!.."
    imgd 911272
    cynthia "Так, а костюм мы с Оливией еще вчера вечером подобрали..."
    cynthia "Где же он?.."
    #Синти вертит задницей ища что-то в шкафу.
    sound vjuh3
    imgd 911273
    cynthia "Да блин! Куда я его дела?! Нужно было оставить его на видном месте..."
    cynthia "А! Вот он!"
    #Синти поднимается и поворачивается к Барди с комплектом какой-то миленькой одежды в руках
    #(Выберите что-то под стать ее характеру. миленькое, как на пушистого зайчика.). Выражение лица радостное и милое.
    imgf 911274
    bardi "Ну, пока ничего не ясно..."
    cynthia "Сейчас."
    #Синти натягивает нижнюю часть одежды.
    fadeblack
    sound put_dress
    pause 1.5
    music Little_Tomcat
    imgfl 911275
    cynthia "Оливия говорила, что эта одежда подчеркнет все мои качества."
    #Синти натягивает верхнюю часть одежды.
    imgf 911276
    cynthia "Правда, я не совсем поняла, о каких качествах шла речь..."
    #Синти одетая радостная встает перед бардом в позе "зацени." - уже не такая робкая и смущенная.
    imgd 911277
    cynthia "Ну как-то так..."
    #Синти смущенная. наклонила голову косится на барда. Поза робкая милая.
    bardi "Зато мне офигенно ясно, о каких качествах шла речь. Ты очень миленькая..."
    imgd 911278
    cynthia "Спасибо."
    bardi "И как Оливия так точно подобрала все это для тебя?.. Смотрится просто отпадно!"
    #Синти смотрит на Барди уже прямо. выражение лица задумчивое поза свободная
    imgd 911279
    cynthia "Не знаю. Она же увлекается всякими этими модельными штучками..."
    cynthia "Даже инстаграм ведет..."
    #У Синти звонит телефон.
    #Синти смотрит на экран
    sound snd_phone_ring
    pause 1.0
    sound2 vjuh3
    img 911280 vpunch
    cynthia "Ой, это мама!"
    #Синти поднимает трубку.
    imgf 911281
    cynthia "Да, мам?.."
    sophie "Синтия, ты там скоро? Я уже готова и жду тебя на улице."
    cynthia "Ой, я уже иду, мам."
    sophie "Давай, я тебя жду."
    #Синти подбирает сумку со стола. Стоит перед Барди.
    imgd 911282
    cynthia "Мне пора!"
    bardi "Да, я слышал. Удачи. Надеюсь, вы весело проведете время."
    #Синти робкая. в руках сумка.
    sound step_stairs_short
    imgd 911283
    cynthia "Спасибо, что помог мне сегодня, [mcname]. Было прикольно провести с тобой время."
    bardi "Да, мне тоже."
    #Синти целует Барди в щеку.
    imgf 911284
    sound kiss2
    bardi_t "Оу..."
    #Синти отстранилась. Смотрит на Барди улыбаясь
    sound step_stairs_short
    imgd 911285
    cynthia "Все. Я побежала."
    #Синти развернулась и уходит.
    bardi "Пока."
    #Синти у двери. затем синти вышла. Бард в комнате один.
    sound2 snd_door_open1
    music Adventures_of_the_Deaf_Dreamer
    imgf 911286
    bardi_t "Офигеть, какая же она миленькая и наивная..."
    bardi_t "Надеюсь, мы еще не раз проведем с ней время..."
    bardi_t "Она, вроде, и сама хочет сблизиться со мной..."
    bardi_t "Может, в итоге нам и удастся достаточно сблизиться?.." ##->#####inc
    #####inc bardi_t "Может, в итоге нам и удастся достаточно сблизиться?.. Далеко не как брат с сестрой..."
    #Бард смотрит на свой стояк.
    imgd 901716
    bardi_t "Так, ладно... В сторону эти мысли."
    bardi_t "Мне срочно нужна разрядка."
    $ mlsBardiFamilyV4Cynthia1 = day # Барди помогал Синтии собираться на пижамную вечеринку
    return

#Бард выходит из комнаты Синти. Идет в свою комнату. Ложится на кровать.
label ep04_dialogues2_family_cynthia_2:
    # Достает член. Начинает дрочить с мыслями о Синти.
    #Несколько Рендеров о том как Бард передергивает свой член.
    fadeblack 1.5
    music Adventures_of_the_Deaf_Dreamer
    imgfl 901751
    sound2 step_stairs_short
    w
    imgf 901752
    w
    fadeblack
    sound put_dress
    pause 1.5
    music Adventures_of_the_Deaf_Dreamer
    imgf 901753
    bardi_t "Твою мать, как же я возбудился со всеми этими переодеваниями..."
    imgd 901754
    w
    imgd 901755
    w
    sound drkanje5
    imgd 901756
    w
    imgd 901755
    bardi_t "Ох... А ведь не только у Оливии есть вкус."
    imgd 901754
    w
    sound drkanje5
    imgd 901753
    w
    imgd 901754
    w
    imgd 901755
    bardi_t "Думаю, я бы тоже нашел костюмчик под стать твоей натуре, милашка Синтия..."
    sound drkanje5
    imgd 901756
    w
#    img 901755
#    w
#    img 901756
    #картинка расплывается
    #На экране синти в комнате Барда в костюме зайки.
    #она стоит перед ним в этом костюмчике.
    #Робкая зажатая красная от смущения. поза как у этой анимешной шняги косплеящей кошек тим "Ня!"
    #тип кулачки подняты почти на уровне лица и опущены костяшками вниз. Синти от смущения отворачивает лицо и косится в сторону.
    $ camera_enabled = False
    music stop
    img white_screen
    with diss
    pause 2.0
    music Stylish_Hip_Hop_Rock
    img 911287
    show screen dream()
    with Dissolve(1.0)
    w
    img 911288
    show screen dream()
    with diss
    cynthia "[mcname], ты уверен, что этот костюм мне идет?" ##->#####inc
    #####inc cynthia "Братик, ты уверен, что этот костюм мне идет?"
    cynthia "Просто, мне так непривычно..."
    cynthia "Это очень смущает..."
    bardi "Более чем, зайка. Ты безумно милая и сексуальная."
    #Синти смущенно косится на Барда
    img 911289
    show screen dream()
    with diss
    cynthia "Ну... Раз ты так говоришь..."
    $ menu_data = {
        "Позвать Синтию к себе на кровать.":{"extra":True}
    }
    menu:
        "Позвать Синтию к себе на кровать.":
            pass
        "Кончить.":
            # несколько кадров на Синтию, может observing - ?
            # картинка Синтии исчезает, Барди кончает себе на живот
            img white_screen
            with diss
            pause 0.5
            img 911290
            with Dissolve(1.0)
            w
            imgd 901756
            w
            img 911291
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man moan8
            bardi "Ах..."
            sound2 chpok5
            imgd 911292
            bardi "О, да!.."
            # затемнение
            #Конец сцены. игрок получает свободу действий.
            fadeblack 1.5
            $ camera_enabled = True
            return
    # Барди позывает Синтию к себе
    img 911293
    show screen dream()
    with diss
    bardi "Подойди ко мне, Синтия." ##->#####inc
    #####inc bardi "Подойди ко мне, сестренка."
    cynthia "..."
    #Синти очень смущается, но подходит. Смущенно косится на Барди. Поза робкая зажатая
    sound highheels_short_walk
    img 911294
    show screen dream()
    with diss
    bardi "Ложись рядом."
    img 911295
    show screen dream()
    with diss
    cynthia "Но... Мы не должны... Мы же с тобой..."
    #Синти смущенно смотрит в пол, указательные пальцы выпрямлены и упираются друг в друга на уровне груди.
    img 911296
    show screen dream()
    with diss
    bardi "Я бы никогда не заставил тебя сделать то, чего ты не хочешь..."
    bardi "Тебе не о чем переживать, Синтия."
    cynthia  "Я..."
    #Синти смущенно смотрит на барда в той же позе.
    img 911295
    show screen dream()
    with diss
    cynthia "Л-ладно."
    #Синти на залезает на кровать и на четвереньках подползает к Барду и ложится рядом.
    #(Ну как ложится, она в такой позе чтоб читателю был обеспечен сексуальный ракурс а ей было удобно дрочить Барди.)
    #Синти смущенная косится на член Барди.
    sound vjuh3
    img 911297
    show screen dream()
    with vpunch
    w
    sound Jump2
    img 911298
    show screen dream()
    with hpunch
    cynthia "..."
    bardi "Возьмешь его в руку?"
    #Синти смущенная смотрит снова на Барди.
    img 911299
    show screen dream()
    with diss
    cynthia "Можно?"
    bardi "Конечно."
    #В двух рендерах изобразите как Синти нерешительно берет в руку член Барди. Тип сначала потянулась к нему и тронула его, а потом взяла в руки.
    img 911300
    show screen dream()
    with fade
    w
    img 911301
    show screen dream()
    with diss
    w
    img 911300
    show screen dream()
    with diss
    w
    img 911302
    show screen dream()
    with diss
    w
    img 911303
    show screen dream()
    with fade
    cynthia "Он огромный..."
    cynthia "И что мне с ним делать?"
    img 911304
    show screen dream()
    with diss
    bardi "Не строй из себя саму невинность. Уверен, ты уже давно представляла это и успела почитать об этом..."
    #Синти бросила на Барди смущенный нерешительный взгляд. красная от стыда. Отвела взгляд и зажмурилась.
    img 911305
    show screen dream()
    with diss
    w
    img 911306
    show screen dream()
    with diss
    cynthia "Ну, я... Я видела пару обучающих видео..."
    #Синти зажмурившись дрочит Барди в нескольких рендерах.
    img 911302
    show screen dream()
    with fade
    w
    img 911307
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911308
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911307
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911308
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911307
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911308
    show screen dream()
    with diss
    w
    img 911306
    show screen dream()
    with fade
    w
    img 911309
    show screen dream()
    with diss
    cynthia "Вот так?"
    bardi "Ох, да. Только побыстрее..."
    cynthia "Л-ладно..."
    #Синти приоткрыв один глаз косится на член Берди и до безумия смущенная дрочит ему.
    img 911310
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911311
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911310
    show screen dream()
    with diss
    bardi "Ох... Да..."
    sound drkanje5
    img 911311
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911310
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911311
    show screen dream()
    with diss
    w
    img 911309
    show screen dream()
    with fade
    cynthia "Тебе хорошо?"
    bardi "Да."
    img 911306
    show screen dream()
    with diss
    cynthia "Мне делать это еще быстрее?"
    bardi "Да, давай."
    #Синти ускоряется.
    img 911312
    show screen dream()
    with fade
    bardi "Боже, Синтия! У тебя охрененно умелые ручки!"
    img 911313
    show screen dream()
    with diss
    cynthia "..."
    img 911302
    show screen dream()
    with diss
    bardi "Ах..."
    sound drkanje5
    img 911307
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911308
    show screen dream()
    with diss
    bardi "Это просто улет!"
    #Синти ускоряется еще быстрее.
    sound drkanje5
    img 911307
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911302
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911308
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911302
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911308
    show screen dream()
    with diss
    bardi "О да!"
    img 911314
    show screen dream()
    with fade
    bardi "Боже, малышка..."
    sound drkanje5
    img 911315
    show screen dream()
    with diss
    bardi "Я уже скоро!"
    sound drkanje5
    img 911314
    show screen dream()
    with diss
    w
    sound drkanje5
    img 911315
    show screen dream()
    with diss
    bardi "Не останавливайся!"
    #Бард кончает на руку Синтии.
    img 911316
    show screen dream()
    sound2 fear2
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    bardi "О ДАААА!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man moan8
    bardi "ОООО!!!"
    sound2 chpok5
    img 911317
    show screen dream()
    with diss
    w
    #Синти чуть опустив голову косится на Барди со смущенной улыбкой.
    img 911318
    show screen dream()
    with diss
    cynthia "Тебе понравилось, [mcname]?" ##->#####inc
    #####inc cynthia "Тебе понравилось, братик?"
    img 911319
    show screen dream()
    with diss
    bardi "Это было отпадно!"
    bardi "Но, все же, тебе предстоит еще многому научиться..."
    #Синти отводит взгляд.
    img 911320
    show screen dream()
    with diss
    cynthia "Только если ты научишь меня всему. Ладно?"
    bardi "Конечно, малышка." ##->#####inc
    #####inc bardi "Конечно, сестренка."
    #Фантазия заканчивается. Барди в комнате один.
    img white_screen
    with diss
    pause 0.5
    img 911321
    with Dissolve(1.0)
    bardi "Обязательно научу..."
    #Конец сцены. игрок получает свободу действий.
    fadeblack 1.5
    $ camera_enabled = True
    return
