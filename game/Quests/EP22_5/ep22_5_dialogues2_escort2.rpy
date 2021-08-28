define VIP_escort_chief = Character(_("Владелец ВИП-эскорта"), who_color=c_blue)
define maylie = Character(_("Мэйли"), who_color=c_pink) #Reception Administrator (Maylie)

default monicaVipEscortCasting1 = 0 # Моника проголосовала за Миранду
default monicaVipEscortCasting2 = 0 # Моника проголосовала за Эбби
default monicaVipEscortCasting3 = 0 # Моника выдвинула свою кандидатуру
default monicaVipEscortCasting4 = 0 # у Моники состоялся разговор со Стивом в служебном коридоре отеля
default monicaVipEscortCasting5 = 0 # Моника решилась на прохождение кастинга перед Стивом
default monicaVipEscortCasting6 = 0 # Моника согласилась сесть попой на член Стива
default monicaVipEscortCasting7 = 0 # Моника слизала сперму Стива, которая вытекла из ее попы
default monicaVipEscortCasting8 = 0 # Моника после проигрыша потребовала провести повторное собрание

default ep22_5_dialogues2_escort2_4_menu1 = False
default ep22_5_dialogues2_escort2_4_menu2 = False
default ep22_5_dialogues2_escort2_4_menu3 = False
default ep22_5_dialogues2_escort2_4_menu4 = False
default ep22_5_dialogues2_escort2_4_menu5 = False

define v_Visitor3_Steve_Blowjob1_1_sound_name = "v_Monica_RichRestaurant_Blowjob1_1_25"
define v_Visitor3_Steve_Blowjob1_1_25_sound_name = "v_Monica_RichRestaurant_Blowjob1_1_25"
define v_Visitor3_Steve_Sex1_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Visitor3_Steve_Sex2_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Visitor3_Steve_Sex2_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Visitor4_Steve_Titjob1_1_25_sound_name = "v_Monica_RichRestaurant_Blowjob1_1_25"
define v_Visitor4_Steve_Titjob1_1_sound_name = "v_Monica_RichRestaurant_Blowjob1_1_25"
define v_Visitor4_Steve_Titjob2_1_sound_name = "v_Monica_RichRestaurant_Blowjob1_1_25"
define v_Visitor4_Steve_Sex1_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Visitor4_Steve_Sex1_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Monica_Steve_Anal1_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Monica_Steve_Anal1_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"

define monicaVipEscortCastingCorruptionRequired1 = 300 # Моника проголосовала за Миранду
define monicaVipEscortCastingCorruptionRequired2 = 300 # Моника проголосовала за Эбби
define monicaVipEscortCastingCorruptionRequired3 = 950 # Моника выдвинула свою кандидатуру
define monicaVipEscortCastingCorruptionRequired4 = 970 # Моника решилась на прохождение кастинга перед Стивом
define monicaVipEscortCastingCorruptionRequired5 = 980 # Моника согласилась сесть попой на член Стива
define monicaVipEscortCastingCorruptionRequired6 = 990 # Моника слизала сперму Стива, которая вытекла из ее попы

default ep22_5_vip_escort_casting_cum_zone = 0

#call ep22_5_dialogues2_escort2_1() # мысли перед регулярным разговором с админшей перед работой в эскорте
#call ep22_5_dialogues2_escort2_2() # ресторан, разговор с Линдой перед кастингом
#call ep22_5_dialogues2_escort2_3() # Моника пытается уйти с ресторана, если еще не была на кастинге Стива
#call ep22_5_dialogues2_escort2_4() # сцена кастинга в конференц-зале перед Стивом
#call ep22_5_dialogues2_escort2_5() # разговор Моники и Стива у лифта
#call ep22_5_dialogues2_escort2_6() # help, если Моника выиграла и пытается зайти в отель, либо к Стиву
#call ep22_5_dialogues2_escort2_7() # мысли после кастинга, если Моника выиграла и стала главной
#call ep22_5_dialogues2_escort2_8() # мысли после кастинга, если Моника отказалась от кастинга и выиграла админша
#call ep22_5_dialogues2_escort2_9() # в следующий приход в эскорт, при клике на админшу (чтобы повторить кастинг)
#call ep22_5_dialogues2_escort2_10() # мысли в следующий приход в эскорт, при клике на кого-либо из эскортниц


# при условии, что был Escort1 и Моника не сбежала, также должна быть пройдена сцена с Линдой и Мирандой
# Моника пришла в отель, перед тем, как подойти к ресепшну
# мысли
label ep22_5_dialogues2_escort2_1:
    # не рендерить!!
    mt "Интересно, эта сучка скажет мне, что сегодня будет собрание?"
    mt "Или сделает вид, что она не в курсе?.."
    mt "И будет вести себя, как обычно?"
    mt "Что ж, сейчас проверим..."
    mt "Притворюсь, что я не знаю о собрании..."
    return

# далее регулярный диалог с администраторшей, когда Моника идет работать в эскорт (ep210_dialogues7_escort_hotel_8a), после которого Моника переодевается и идет в ресторан работать

# Моника заходит в ресторан
label ep22_5_dialogues2_escort2_2:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgf 44148
    mt "Вот тварь! Она мне ничего не сказала!"
    mt "Если бы я вчера не узнала от проститутки Эбби про собрание..."
    mt "Они провели бы его без моего участия!"
    mt "!!!"
    imgd 44149
    mt "Это говорит о том, Моника, что сучка-администраторша видит в тебе сильного соперника!"
    mt "Поэтому не хочет, чтобы ты там присутствовала! Да!"
    mt "Но ее ждет неприятный сюрприз!"
    mt "!!!"
    # Моника садится за свой столик
    # звук каблуков
    # к столику Моники подбегает Линда
    # она наклоняется торопливо к Монике и шепчет ей на ухо
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Poppers_and_Prosecco
    imgfl 44150
    w
    sound highheels_run2
    imgf 44151
    linda "[monica_hotel_name], сегодня вечером важная встреча в конференц-зале."
    linda "Иди туда после работы."
    linda "Будет голосование за место администраторши."
    # Моника делает вид, что удивлена
    m "Голосование? Сегодня?"
    linda "Да!"
    imgd 44152
    linda "Помнишь, мы с Мирандой говорили тебе о том..."
    linda "Что тебя ждут большие привилегии, если главной стану я или Миранда?"
    m "Помню..."
    linda "Сегодня тебе нужно будет проголосовать за Миранду."
    linda "Нужно, чтобы она стала главной вместо администраторши. Договорились?"
    m "..."
    menu:
        "Согласиться.":
            pass
    # Моника задумчиво
    music Hidden_Agenda
    imgf 44153
    mt "Нужно подыграть ей..."
    mt "Это меня ни к чему не обязывает!"
    mt "..."
    imgd 44154
    m "Хорошо, Линда, я отдам свой голос за Миранду."
    music Poppers_and_Prosecco
    linda "Отлично!"
    linda "Тогда до встречи вечером в конференц-зале."
    imgf 44155
    sound highheels_short_walk
    w
    # Линда торопливо уходит
    # Моника сидит в задумчивости
    fadeblack 1.5
    music Stealth_Groover
    imgf 44156
    mt "Мне нужно подумать, как вести себя на этом собрании..."
    mt "Отдать свой голос за Эбби?" # кадр на сидящую за столиком Эбби
    #
    $ notif(_("Моника 'дружит' с Эбби и Кэндис."))
    #
    imgd 44157
    mt "..."
    imgd 44158
    mt "Или проголосовать за Миранду?" # кадр на сидящую за столиком Миранду
    #
    $ notif(_("Моника 'дружит' с Мирандой и Линдой."))
    #
    img 44159
    mt "..."
    # отворачивается от них
    imgf 44160
    mt "Заслужили ли они того, чтобы я голосовала за них?.."
    mt "После того, в какие гадкие ситуации меня вмешивали что одна, что вторая..."
    mt "..."
    mt "Более того, при голосовании за одну из них..."
    mt "Я раскрою свою 'дружбу' с ней, а это автоматически сделает меня врагом другой компании проституток."
    #
    $ notif(_("Миранда и Линда враждуют с Кэндис и Эбби."))
    #
    imgd 44161
    mt "Как же это все сложно, Моника!"
    mt "!!!"
    # хитрая улыбка на лице
    music Hidden_Agenda
    imgf 44162
    mt "Хорошо, что у меня есть еще один вариант..."
    mt "..."
    return

# Моника пытается уйти с ресторана, если еще не была на кастинге Стива
label ep22_5_dialogues2_escort2_3:
    music Poppers_and_Prosecco
    imgf 30077
    mt "Мне нужно идти в конференц-зал!"
    mt "Я должна присутствовать на этом чертовом собрании проституток!"
    mt "Я, наконец-то, смогу узнать, кто является владельцем ВИП-эскорта!"
    mt "И кто знает, чем это собрание закончится?.."
    call refresh_scene_fade()
    return

label ep22_5_dialogues2_escort2_3a:
    mt "Мне нужно идти в конференц-зал!"
    mt "Я должна присутствовать на этом чертовом собрании проституток!"
    mt "Я, наконец-то, смогу узнать, кто является владельцем ВИП-эскорта!"
    mt "И кто знает, чем это собрание закончится?.."
    return False

# конференц-зал
# сцена кастинга перед Стивом будет повторяющаяся, пока Моника не станет главной
label ep22_5_dialogues2_escort2_4:
    # Моника заходит в конференц-зал (Стива сразу не показываем, он стоит позади всех кресел, отвернувшись спиной, Моника его не видит, а он -ее)
    # кадр на девочек - они стоят в ряд у экрана, админша стоит посередине двух враждующих компаний
    # администраторша поворачивается в сторону вошедшей Моники
    fadeblack
    sound snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 44163
    w
    imgd 44164
    reception "!!!" # недовольно смотрит нее
    # Моника в ответ бросает высокомерный взгляд
    img 44165
    mt "Что, сучка, не ожидала увидеть здесь меня?!"
    mt "!!!"
    # администраторша недовольно отворачивается от Моники и смотрит в зал
    # из зала раздается голос (Стива не показываем, он спрашивает, не поворачиваясь к девочкам)
    imgf 44166
    sound bottle1
    VIP_escort_chief "К нам еще кто-то захотел присоединиться?"
    # администратор с милой улыбочкой
    sound pour_wine
    imgd 44167
    reception "Да, Босс. Это наша новенькая."
    reception "Она тоже хочет принимать участие."
    sound bottle1
    imgd 44168
    VIP_escort_chief "Пусть проходит... Сейчас я посмотрю на нее."
    # админша поворачивается к Монике и зло шипит ей
    imgd 44169
    reception "Подойди сюда, [monica_hotel_name]! Чего ты там стоишь?!"
    img 44170
    mt "Как же ее бесит мое присутствие здесь!.."
    imgd 44171
    reception "Давай быстрее!"
    img 44172
    mt "!!!"
    # Моника проходит и встает в один ряд с девочками перед экраном, рядом с админшей
    sound man_steps
    imgf 44173
    VIP_escort_chief "Пора начинать, девочки."
    # он поворачивается и идет к креслам в первом ряду, звук шагов
    # затемнение
    # кадр на кресла - в первом ряду сидит Стив и удивленно смотрит на Монику
    fadeblack 1.5
    sound plastinka1b
    img 44209 vpunch
    w
    music Power_Bots_Loop
    img 44211
    mt "СТИВ?!"
    mt "?!"
    mt "?!?!"
    mt "?!?!?!"
    mt "КАКОГО ХРЕНА?!"
    music Hidden_Agenda
    img 44210 hpunch
    VIP_escort_chief "Какая у нас интересная новенькая девочка!.."
    VIP_escort_chief "Надо же!.."
    # Моника видит Стива, она в шоке
    # кадр на Стива, он с усмешкой обращается к админше
    imgd 44212
    steve "Мэйли, как ты говоришь зовут нашу новенькую?"
    reception "Ее зовут, [monica_hotel_name], Босс."
    # Моника все еще в шоке
    music Pyro_Flow
    mt "Босс?!"
    mt "Стив?! Босс ВИП-эскорта?!"
    mt "!!!!!"
    # Стив противненько улыбается, оглядывая Монику с ног до головы
    music Groove2_85
    imgf 44213
    steve "[monica_hotel_name]..."
    steve "Какое приятное знакомство..."
    # админша толкает офигевшую Монику локтем, шипит ей злобно
    imgd 44214
    reception "Какого черта ты стоишь, как статуя?!"
    sound Jump1
    img 44215 vpunch
    reception "У тебя что, язык отсох?!"
    img 44216
    reception "Не веди себя, как идиотка!"
    reception "Ответь Боссу, что тебе тоже приятно!"
    music Hidden_Agenda
    imgf 44217
    m "!!!"
    m "Я... Да..."
    m "Кхм..."
    m "Мне тоже приятно... Познакомиться с вами..."
    # Стив довольно усмехается и потирает руки
    imgd 44218
    steve "Хе-хе!"
    # у Моники взрыв мозга
    music Power_Bots_Loop
    imgd 44219
    mt "Я ничего не понимаю!"
    mt "Это сон?! Какой-то бредовый сон?!"
    mt "Стив является владельцем ВИП-эскорта?!"
    mt "КАК?! КАК ОН ЭТО СДЕЛАЛ?! КОГДА?!"
    mt "?!?!?!"
    # потом принимает важный вид и начинает вещать
    fadeblack 1.5
    music Groove2_85
    imgf 44220
    steve "Ну что, девочки, начнем?"
    steve "Я рад приветствовать вас на нашем собрании."
    steve "Последний раз я мог наблюдать и оценивать вашу работу..."
    steve "На важной презентации одного из крупных журналов моды..."
    # смотрит с усмешкой на реакцию Моники
    imgd 44221
    steve "Которую проводила Моника Бакфетт, его глава."
    music Pyro_Flow
    img 44222 vpunch
    mt "Мерзкий мешок с дерьмом!"
    mt "Слизняк!"
    mt "!!!"
    # Линда с Мирандой косятся на Монику, а Стив продолжает
    music Groove2_85
    imgf 44223
    steve "Я был доволен тем, как вы отработали с теми господами, которые присуствовали на презентации."
    steve "У меня нет замечаний. Вы все молодцы, девочки."
    # хлопает в ладоши, девочки улыбаются (все, кроме насупленной Моники)
    imgd 44224
    steve "Сегодня, мои хорошие, я собрал вас для того..."
    steve "Чтобы мы все вместе с вами решили один важный вопрос."
    steve "Лично я весьма доволен качеством работы нашего администратора Мэйли."
    # админша улыбается ему
    imgd 44225
    reception "Спасибо, Босс."
    imgd 44226
    steve "Но я подумал, что поступил не совсем честно перед вами..."
    steve "Выбрав кандидатуру Мэйли единолично и назначив ее администратором."
    steve "Вполне возможно, что кто-то из вас видит себя на месте Мэйли."
    steve "И захочет выдвинуть свою кандидатуру."
    # девочки переглядываются, шепчутся
    imgf 44227
    w
    img 44228 vpunch
    reception "Тихо!"
    sound Jump2
    img 44229
    reception "!!!"
    imgf 44230
    steve "Поэтому я решил провести голосование, по результатам которого..."
    steve "Либо мы все удостоверимся в незаменимости Мэйли и она останется главной среди вас..."
    steve "Либо мы выберем нового администратора ВИП-эскорта."
    steve "Результат голосования зависит от вас, девочки."
    steve "Та из вас, которая наберет 4 голоса, станет администратором."
    imgd 44231
    steve "Если между кандидатками голоса разделятся поровну..."
    steve "В таком случае, мне придется вмешаться в ход голосования и мой голос будет решающим..."
    steve "Но сначала кандидаткам придется доказать мне, что я должен отдать свой голос в ее пользу."
    steve "У вас есть какие-то вопросы, девочки?"
    reception "Всем все ясно, Босс. Вопросов нет."
    # Моника смотрит на него злобно
    music Pyro_Flow
    img 44232 hpunch
    mt "У меня к тебе ооочень много вопросов, сволочь!"
    mt "!!!"
    label ep22_5_dialogues2_escort2_4a: ### repeat
    # Стив в предвкушении потирает руки и довольно улыбается
    fadeblack 1.5
    music Groove2_85
    imgfl 44233
    steve "Ну что, мои хорошие? Не будем терять времени! Приступим!"
    # админша поворачивается к девочкам
    sound highheels_short_walk
    imgf 44234
    reception "Так, девочки!"
    reception "Сначала голосует [monica_hotel_name], так как она у нас новенькая..."
    reception "Потом все остальные."
    reception "Я отдам свой голос после того, как вы все проголосуете."
    # админша смотрит на Монику
    imgd 44235
    reception "Начинай, [monica_hotel_name]!"
    # Моника наконец отрывает убийственный взгляд от Стива
    # растерянно смотрит на админшу
    img 44236 vpunch
    m "А?.. Что?.."
    m "???"
    # та злится
    imgd 44237
    reception "Ты что, не слушала меня, [monica_hotel_name]?!"
    reception "Я говорю, что ты голосуешь первая!"
    reception "Говори имя!"
    # Моника растерянно смотрит на админшу
    music Jail_Clock
    img 44238
    mt "Черт-черт-черт!"
    mt "!!!"
    mt "Появление слизняка Стива здесь... Это... Это настолько меня..."
    mt "Черт! Это меня шокировало!!!"
    # потом смотрит на Линду, та подмигивает Монике
    imgd 44239
    w
    sound Jump1
    img 44240
    linda "!!!"
    imgd 44241
    mt "Я свосем не продумала свой план действий!"
    # потом смотрит на Эбби, та тоже подмигивает Монике
    imgf 44242
    w
    sound Jump1
    img 44243
    w
    imgd 44244
    mt "Мысли путаются..."
    mt "..."
    # Моника отворачивается от всех
    imgd 44245
    mt "Что делать?!"
    mt "Чье имя мне назвать?!"
    mt "?!"
    # высокий коррапшн на выдвижении себя (пункт 3)
    $ menu_corruption = [monicaVipEscortCastingCorruptionRequired1, monicaVipEscortCastingCorruptionRequired2, monicaVipEscortCastingCorruptionRequired3]
    menu:
        "Проголосовать за Миранду.":
            $ monicaVipEscortCasting1 = day # Моника проголосовала за Миранду
            # Моника смотрит на Миранду и Линду, те выжидательно смотрят на нее в ответ
            music Groove2_85
            imgf 44246
            mt "Если я проголосую за проститутку Миранду, как пообещала Линде..."
            imgd 44247
            linda "..."
            miranda "..."
            imgd 44248
            mt "Тогда Кэндис и Эбби поймут, что я не дружила с ними, а притворялась..."
            # смотрит на Эбби с Кэндис, те тоже в напряжении смотрят на нее
            imgd 44249
            candice "..."
            abby "..."
            imgf 44250
            mt "Они разозляться и станут действовать против меня."
            mt "Черт! Только не хватало мне двух воинственно настроенных проституток!"
            mt "Тем более, что именно Эбби мне вчера сказала про это гребаное собрание!"
            mt "Она мне доверила важную информацию..."
            mt "С другой стороны, Линда меня тоже сегодня предупредила!"
            mt "..."
            imgd 44251
            mt "Вообще, самым лучшим решением было бы выдвинуть свою кандидатуру, но..."
            mt "Тогда все эти падшие особы во главе с администраторшей будут против меня!"
            mt "На данный момент это слишком рискованно."
            mt "Сначала мне нужно поговорить с этим мешком дерьма Стивом, а потом обдумывать план, как стать главной!"
            mt "А пока... Кого же мне выбрать?"
            mt "Черт-черт-черт!"
            mt "Думай, Моника, думай!"
            mt "!!!"
            music Stealth_Groover
            imgd 44252
            mt "В договоренности с лицемерными сучками Линдой и Мирандой есть один существенный плюс!.."
            mt "Они думают, что я являюсь сотрудницей Моники Бакфетт!"
            mt "И всячески лебезят передо мной в связи с этим!"
            mt "Они обе у меня под каблуком и готовы делать все, что я скажу!"
            mt "Поэтому выгоднее для меня будет, если главной станет Миранда!.."
            mt "А не эта Эбби, которая на самом деле не так проста!"
            mt "Решено!"
            # админша теряет терпение, пока Моника размышляет
            music Groove2_85
            img 44253
            reception "[monica_hotel_name], нам долго ждать?!"
            reception "Хватит тянуть время! Говори имя!"
            # Моника делает покер фейс
            music Stealth_Groover
            sound2 highheels_short_walk
            imgf 44254
            w
            imgd 44255
            w
            imgd 44256
            w
            sound highheels_short_walk
            imgf 44257
            m "Я отдаю свой голос за Миранду!"
            # Эбби в шоке, Кэндис тоже. обе злобно шипят на Монику
            # Моника все это время продолжает держать покер фейс
            # Линда с Мирандой радостно улыбаются
            imgd 44258
            w
            music Pyro_Flow
            sound2 oooh3
            img 44259 vpunch
            abby "Чтоооо?!"
            abby "Ты! Предательница!!!"
            candice "[monica_hotel_name], я не ожидала от тебя такого!"
            candice "Мы же доверяли тебе!"
            abby "Сучка! Лицемерка!"
            imgd 44260
            candice "Какой кошмар! Эбби, как мы могли так ошибиться?!"
            img 44261 hpunch
            abby "Дрянь!"
            abby "Да я тебе!.."
            # админша перебивает их ругань
            img 44262
            reception "Эбби, Кэндис, а ну-ка замолчали обе! Сейчас же!"
            reception "Вы как себя ведете перед Боссом?!"
            # Эбби тычет пальцем в сторону Моники, возмущенно оправдываясь
            imgd 44263
            abby "Да она!.."
            reception "Тихо!!!"
            # девочки замолкают и враждебно смотрят на Монику
            # та делает вид, что ничего такого не произошло
            imgf 44264
            m "..."
            # Стив доволен накаляющейся обстановкой среди девочек
            music Groove2_85
            imgd 44265
            steve "Итак, у нас есть первый голос! Отлично!"
            steve "Один голос в пользу Миранды!"
            steve "Кто следующий?"
            # Линда поднимает руку
            imgf 44266
            linda "Я тоже голосую за Миранду."
            # Стив довольно
            imgd 44267
            steve "Два голоса за Миранду!"
            steve "Дальше!"
            # Кэндис говорит, зло косясь на Монику
            img 44268
            candice "А я отдаю свой голос за Эбби!!!"
            candice "!!!"
            # Стив
            imgd 44269
            steve "У Миранды появился конкурент!"
            steve "Одни голос за Эбби, два - за Миранду!"
            steve "А как проголосуешь ты, Мэйли?"
            # администраторша делает шаг вперед и поворачивается к девочкам
            sound highheels_short_walk
            imgf 44270
            reception "..."
            # пристально смотрит на каждую
            reception "Я..."
            reception "Отдаю свой голос за..."
            # подходит к Эбби и встает рядом с ней, потом говорит, глядя на Стива
            sound highheels_short_walk
            imgd 44271
            reception "За Эбби!"
            # все девочки в шоке, включая саму Эбби, все удивленно смотрят на админшу
            music Pyro_Flow
            img 44272 vpunch
            sound2 oooh2
            mt "Сучка-администраторша проголосовала за Эбби?!"
            mt "Серьезно?!"
            mt "Эбби с Кэндис говорили, что она их не любит!"
            mt "Они что, обманывали меня? У них есть какая-то договоренность с администраторшей?!"
            mt "?!"
            # Стив почему-то выглядит очень довольным
            music Groove2_85
            imgf 44273
            steve "Итаааак..."
            steve "Мы имеем два голоса за Эбби и два - за Миранду!"
            # разводит руками, довольно ухмыляясь
            steve "У нас ничья, мои хорошие!"
            steve "Что это значит?"
            # админша отходит от Эбби, выходит вперед и говорит Стиву
            label ep22_5_dialogues2_escort2_4b:
            sound highheels_short_walk
            imgd 44274
            reception "Босс, я считаю, раз голоса разделились поровну..."
            reception "И нет никакого единогласного решения по кому-либо из кандидаток..."
            reception "Значит, администратором должна остаться я."
            # Стив ей отвечает, хитро улыбаясь
            imgd 44275
            steve "Мэйли, но за тебя не было вообще ни одного голоса, верно?"
            reception "Но и единогласного решения не принято, Босс."
            steve "Что же..."
            steve "У нас есть две претендентки на место администратора - Миранда и Эбби..."
            steve "А также действующий администратор Мэйли, которая утверждает, что она должна остаться в этой должности."
            imgd 44276
            reception "Да, Босс, все верно."
            # Стив притворно расстроенно вздыхает, хитро поглядывая на девочек
            imgf 44277
            steve "Ну что же теперь нам делать?.."
            steve "Видимо, по-другому никак не решить это разногласие..."
            steve "Я вынужден объявить кастинг, девочки!"
            # Моника прищурившись злобно смотрит на Стива
            music Power_Bots_Loop
            imgd 44278
            mt "У этого гада подозрительно довольная морда..."
            mt "Этот мерзавец что-то задумал!"
            mt "..."
            # Стив говорит девочкам
            music Hidden_Agenda
            imgf 44279
            steve "Миранда, Эбби и Мэйли."
            steve "Сейчас вы по очереди продемонстрируете мне, насколько хорошо вы умеете работать с клиентом."
            steve "В роли которого буду выступать Я!" # довольно указывает на себя
            steve "Начиная с момента знакомства и до логического завершения работы. Хе-хе!"
            steve "После того, как каждая из вас продемонстрирует свои... Свои таланты..."
            steve "Я выберу ту, которая и займет вожделенное место администратора нашего ВИП-эскорта!"
            # Стив хлопает в ладони
            imgd 44280
            steve "Начали, девочки!"
            sound snd_slap1
            img 44281 hpunch
            w
            # достает свой стояк
            fadeblack
            sound snd_zip
            pause 2.0
            music Groove2_85
            imgfl 44296
            steve "Покажите мне, как вы ведете себя с клиентом!"
            steve "Кто будет первой?"
            # кадр на девочек
            label ep22_5_dialogues2_escort2_4_loop1:
            imgf 44297
            w
            menu:
                "Миранда.":
                    # Миранда делает шаг вперед, соблазнительно улыбается Стиву
                    sound highheels_short_walk
                    imgd 44338
                    miranda "Босс не возражает, если я составлю ему компанию?"
                    imgf 44339
                    w
                    # Стив довольно улыбается
                    imgd 44340
                    steve "Конечно, нет, детка!"
                    # она подходит к нему
                    steve "У нас тут демократия. Любая инициатива только приветствуется, детка."
                    # она наклоняется и проводит рукой по его бедру
                    music Loved_Up
                    sound2 highheels_short_walk
                    imgf 44341
                    miranda "Мне нравится, когда меня называют деткой..."
                    miranda "Это так возбуждает меня!"
                    # Стив кладет руку ей на попу
                    imgd 44342
                    miranda "А как к вам обращаться, Босс?"
                    sound Jump1
                    img 44343
                    w
                    imgf 44344
                    w
                    imgd 44345
                    steve "А меня возбуждает, когда меня называют Босс."
                    steve "Что ты готова сделать ради карьерного роста, детка? Хе-хе!"
                    # она задирает свою юбку
                    miranda "Ваша детка хочет сделать вам что-то очень-очень приятное, Босс..."
                    # обхватывает его член, водит рукой по нему
                    imgf 44346
                    w
                    sound drkanje5
                    imgd 44347
                    w
                    sound drkanje5
                    imgd 44346
                    w
                    sound drkanje5
                    imgd 44347
                    w
                    sound drkanje5
                    imgd 44346
                    miranda "Мммм... Какой он большой и твердый!"
                    sound drkanje5
                    imgd 44347
                    steve "Даа..."
                    # она сексуально облизывает губы и наклоняется к губам Стива
                    imgf 44348
                    miranda "Такой манящий!.."
                    # наклоняется, целует его в губы, а он в это время лапает ее за попу
                    sound lick3
                    imgd 44349
                    miranda "Мммм..."
                    # шепчет ему в губы
                    sound snd_longkiss1
                    imgd 44350
                    w
                    imgd 44351
                    w
                    imgd 44352
                    w
                    imgd 44353
                    miranda "Мне не терпится попробовать его на вкус..."
                    steve "Да, давай! Сделай это для своего Босса!"
                    # шлепает ее по попе, она соблазнительно ему улыбается и садится на колени перед ним
                    # Стив сидит в том же кресле в зале, вальяжно развалившись
                    # она наклоняется к его члену и проводит языком по стволу от основания до головки
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 44354
                    w
                    imgf 44355
                    w
                    imgd 44356
                    w
                    imgf 44357
                    w
                    sound lick3
                    imgd 44358
                    w
                    sound lick3
                    imgd 44357
                    w
                    sound lick3
                    imgd 44358
                    w
                    sound lick3
                    imgd 44357
                    w
                    sound lick3
                    imgd 44358
                    miranda "Мпфх... Он и правда вкусный..."
                    # целует его головку, водит ею по своим губам
                    sound lick3
                    imgd 44359
                    w
                    sound lick3
                    imgd 44360
                    miranda "Мммм..."
                    # потом вбирает его в рот, помещается не весь, наполовину
                    sound drkanje5
                    imgd 44361
                    w
                    sound drkanje5
                    imgd 44360
                    w
                    sound drkanje5
                    imgd 44361
                    w
                    sound drkanje5
                    imgd 44360
                    w
                    sound drkanje5
                    imgd 44361
                    miranda "Мпфхфпфф..."
                    # пытается протолкнуть глубже
                    imgf 44362
                    w

                    # video
                    # 1
                    # v_Visitor3_Steve_Blowjob1_1
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Blowjob1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Blowjob1_1= Movie(play="video/v_Visitor3_Steve_Blowjob1_1.mkv")
                    show videov_Visitor3_Steve_Blowjob1_1
                    with fade
                    steve "Молодец, детка."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 2
                    # v_Visitor3_Steve_Blowjob1_4_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Blowjob1_1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Blowjob1_4_25= Movie(play="video/v_Visitor3_Steve_Blowjob1_4_25.mkv")
                    show videov_Visitor3_Steve_Blowjob1_4_25
                    with fade
                    steve "Я вижу, как ты стараешься."
                    wclean
                    steve "Это похвально. Твой Босс доволен. Хе-хе!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # Стив кладет свою руку ей на голову
                    # насаживает ее голову, но до конца она все равно не может взять его член в свой рот, у нее закатываются глаза
                    imgf 44363
                    steve "Я тебе помогу, детка..."
                    miranda "Мпфхфпфф!!!"
                    # она снимает свою голову с его члена

                    imgd 44364
                    w
                    # 3
                    # v_Visitor3_Steve_Blowjob1_5
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Blowjob1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Blowjob1_5= Movie(play="video/v_Visitor3_Steve_Blowjob1_5.mkv")
                    show videov_Visitor3_Steve_Blowjob1_5
                    with fade
                    miranda "Мпфааа..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44365
                    w

                    # 4
                    # v_Visitor3_Steve_Blowjob1_3_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Blowjob1_1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Blowjob1_3_25= Movie(play="video/v_Visitor3_Steve_Blowjob1_3_25.mkv")
                    show videov_Visitor3_Steve_Blowjob1_3_25
                    with fade
                    miranda "Мммпфф!!!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 5
                    # v_Visitor3_Steve_Blowjob1_2_25
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Blowjob1_2_25= Movie(play="video/v_Visitor3_Steve_Blowjob1_2_25.mkv")
                    show videov_Visitor3_Steve_Blowjob1_2_25
                    with fade
                    steve "Дааа, вот так..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44366
                    w
                    # смотрит ему в глаза и сексуально улыбается
                    # потом встает и демонстративно проводит перед лицом Стива рукой по своей киске
                    sound vjuh3
                    imgd 44367
                    miranda "Моя киска уже вся влажная, Босс..."
                    # Стив довольно пялится на нее
                    imgd 44368
                    steve "Приласкай себя немного, детка."
                    steve "Я хочу посмотреть на то, как ты играешь со своей влажной киской."
                    # она ставит одну ногу на кресло, раскрываясь перед Стивом
                    # начинает трогать себя одной рукой, а пальцы второй кладет себе в рот и сексуально облизывает
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Loved_Up
                    imgfl 44369
                    w
                    imgf 44370
                    miranda "Мммм..."
                    imgd 44371
                    w
                    sound drkanje5
                    imgd 44372
                    w
                    sound drkanje5
                    imgd 44371
                    w
                    sound drkanje5
                    imgd 44372
                    w
                    sound drkanje5
                    imgd 44371
                    w
                    sound drkanje5
                    imgd 44372
                    steve "Да, молодец, детка!"
                    imgf 44374
                    miranda "Я вся изнемогаю, Босс..."
                    imgd 44373
                    miranda "Мне так хочется... Оооо..."
                    sound vjuh3
                    imgd 44375
                    miranda "Так хочется поскорее ощутить внутри себя ваш огромный член..."
                    # она лезет на Стива сверху и насаживается киской на его член
                    sound chpok6
                    img 44376 hpunch
                    steve "Оооо, давай, покажи как ты хочешь своего большого Босса!"
                    imgd 44377
                    sound snd_longkiss1
                    w
                    imgd 44378
                    w
                    imgd 44379
                    w
                    imgd 44380
                    w
                    sound snd_longkiss1
                    imgd 44381
                    w
                    imgd 44382
                    w
                    imgd 44383
                    w

                    # video
                    # 1
                    # v_Visitor3_Steve_Sex1_2
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Sex1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex1_2= Movie(play="video/v_Visitor3_Steve_Sex1_2.mkv")
                    show videov_Visitor3_Steve_Sex1_2
                    with fade
                    miranda "Какой же он огромный! Дааа!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 2
                    # v_Visitor3_Steve_Sex1_3
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex1_3= Movie(play="video/v_Visitor3_Steve_Sex1_3.mkv")
                    show videov_Visitor3_Steve_Sex1_3
                    with fade
                    miranda "Аааа... Как же круто!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44384
                    w
                    # 3
                    # v_Visitor3_Steve_Sex1_4
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex1_4= Movie(play="video/v_Visitor3_Steve_Sex1_4.mkv")
                    show videov_Visitor3_Steve_Sex1_4
                    with fade
                    miranda "Он заполняет меня всю! Как здорово!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # начинает двигаться вверх-вниз на его стояке
                    imgf 44385
                    w
                    # 4
                    # v_Visitor3_Steve_Sex1_1
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex1_1= Movie(play="video/v_Visitor3_Steve_Sex1_1.mkv")
                    show videov_Visitor3_Steve_Sex1_1
                    with fade
                    miranda "О, дааа!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 5
                    # v_Visitor3_Steve_Sex1_5
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex1_5= Movie(play="video/v_Visitor3_Steve_Sex1_5.mkv")
                    show videov_Visitor3_Steve_Sex1_5
                    with fade
                    miranda "Оооо!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44386
                    w
                    imgd 44387
                    w

                    # video
                    # 1
                    # v_Visitor3_Steve_Sex2_1_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Sex2_1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex2_1_25= Movie(play="video/v_Visitor3_Steve_Sex2_1_25.mkv")
                    show videov_Visitor3_Steve_Sex2_1_25
                    with fade
                    miranda "Ооо!!! Вот это да!!!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 2
                    # v_Visitor3_Steve_Sex2_2_25
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex2_2_25= Movie(play="video/v_Visitor3_Steve_Sex2_2_25.mkv")
                    show videov_Visitor3_Steve_Sex2_2_25
                    with fade
                    miranda "Аааа!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44388
                    w
                    # 3
                    # v_Visitor3_Steve_Sex2_4
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor3_Steve_Sex2_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex2_4= Movie(play="video/v_Visitor3_Steve_Sex2_4.mkv")
                    show videov_Visitor3_Steve_Sex2_4
                    with fade
                    miranda "Я сейчас кончу, Босс! Кончу!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 4
                    # v_Visitor3_Steve_Sex2_3
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor3_Steve_Sex2_3= Movie(play="video/v_Visitor3_Steve_Sex2_3.mkv")
                    show videov_Visitor3_Steve_Sex2_3
                    with fade
                    steve "Давай, сделай это для меня!"
                    wclean
                    steve "Твой Босс хочет, чтобы ты кончила, детка!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    music Loved_Up2
                    imgf 44389
                    w
                    imgd 44390
                    w
                    imgd 44391
                    w
                    img 44392
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    miranda "Оооо!!!"
                    steve "Кончай!!!"
                    # Миранда содрогается в оргазме, Стив держит ее за зад
                    img 44393
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound woman_moan14
                    miranda "Аааа!"
                    miranda "ААААА!!!"
                    miranda "ААААААА!!!"
                    # потом шлепает ее по заду
                    imgf 44394
                    steve "Умничка!"
                    steve "Вставай, детка."
                    # она соскальзывает с него с довольным лицом
                    fadeblack 1.5
                    music Groove2_85
                    imgfl 44395
                    miranda "О, это было потрясающе, Босс!"
                    steve "Мне тоже понравилось, детка."
                    steve "Сразу видно профессионала в своем деле. Хе-хе!"
                    # Миранда одевается и отходит от него, встает на свое прежнее место
                    # Моника недовольно косится на нее
                    imgf 44396
                    mt "На что только эти проститутки не готовы пойти!"
                    mt "Противно смотреть на этот разврат! Фи!"
                    sound highheels_short_walk
                    imgd 44397
                    mt "!!!"
                    $ ep22_5_dialogues2_escort2_4_menu1 = True
                    jump ep22_5_dialogues2_escort2_4_loop1
                "Эбби.":
                    # Эбби выходит вперед с уверенным видом и сразу начинает стягивать с себя одежду
                    sound highheels_short_walk
                    imgd 44398
                    abby "Думаю, что наш Босс, будучи таким харизматичным и брутальным мужчиной..."
                    abby "Любит уверенных в себе девочек."
                    imgf 44399
                    w
                    sound vjuh3
                    img 44400 hpunch
                    w
                    # подходит к нему и уткнувшись пальцем в грудь облокачивает его на спинку кресла
                    # потом наклоняется к нему и берет его за подбородок
                    music Loved_Up
                    sound2 highheels_short_walk
                    imgf 44401
                    abby "Которые точно знают, чего хотят..."
                    sound Jump1
                    img 44402 vpunch
                    w
                    # проводит языком по его щеке
                    sound vjuh3
                    imgd 44403
                    steve "Ух, какая ты резкая, детка... Ты права, мне это нравится..."
                    # она берет в ладони свои груди и приближает их к лицу Стива
                    imgf 44404
                    w
                    sound lick3
                    imgd 44405
                    w
                    imgf 44406
                    abby "Босс хочет увидеть свой большой член между этими малышками?"
                    imgd 44407
                    steve "Хе-хе!"
                    # она встает на колени перед ним и засовывает ео член между своих грудей
                    # начинает медленно двигать ими
                    fadeblack 1.5
                    music Loved_Up
                    imgf 44408
                    abby "Ох, какой клевый стояк!"
                    imgd 44409
                    w

                    # video
                    # 1
                    # v_Visitor4_Steve_Titjob1_1_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor4_Steve_Titjob1_1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob1_1_25= Movie(play="video/v_Visitor4_Steve_Titjob1_1_25.mkv")
                    show videov_Visitor4_Steve_Titjob1_1_25
                    with fade
                    abby "Дааа..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 2
                    # v_Visitor4_Steve_Titjob1_2
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor4_Steve_Titjob1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob1_2= Movie(play="video/v_Visitor4_Steve_Titjob1_2.mkv")
                    show videov_Visitor4_Steve_Titjob1_2
                    with fade
                    abby "Такая большая сочная головка!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44410
                    w
                    # 3
                    # v_Visitor4_Steve_Titjob1_3
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob1_3= Movie(play="video/v_Visitor4_Steve_Titjob1_3.mkv")
                    show videov_Visitor4_Steve_Titjob1_3
                    with fade
                    abby "Я не могу удержаться, чтобы не попробовать ее..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 4
                    # v_Visitor4_Steve_Titjob1_4
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob1_4= Movie(play="video/v_Visitor4_Steve_Titjob1_4.mkv")
                    show videov_Visitor4_Steve_Titjob1_4
                    with fade
                    steve "Поробуй, детка, твой Босс тебе разрешает сделать это..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # продолжая водить грудями по члену, облизывает головку члена
                    imgf 44411
                    w
                    sound lick3
                    imgd 44412
                    w
                    sound lick3
                    imgd 44411
                    w
                    sound lick3
                    imgd 44412
                    w
                    sound lick3
                    imgd 44411
                    abby "Какой же он огромный!.."
                    sound lick3
                    imgd 44412
                    abby "Это самый большой член, который я видела!"
                    steve "Да, он у меня такой! Хе-хе!"
                    # вбирает головку в рот, продолжая делать титсджоб
                    sound chpok6
                    img 44413 vpunch
                    w
                    # video
                    # 1
                    # v_Visitor4_Steve_Titjob2_4
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor4_Steve_Titjob2_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob2_4= Movie(play="video/v_Visitor4_Steve_Titjob2_4.mkv")
                    show videov_Visitor4_Steve_Titjob2_4
                    with fade
                    abby "Мммм!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # отстраняется
                    imgf 44414
                    abby "Он еле помещается у меня во рту!"
                    abby "Офигенно!"
                    # снова вбирает в рот, делает титсджоб и минет одновременно
                    sound chpok6
                    imgd 44415
                    w
                    # 2
                    # v_Visitor4_Steve_Titjob2_1
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob2_1= Movie(play="video/v_Visitor4_Steve_Titjob2_1.mkv")
                    show videov_Visitor4_Steve_Titjob2_1
                    with fade
                    abby "Мпфхфпфф!!!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # 3
                    # v_Visitor4_Steve_Titjob2_2
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob2_2= Movie(play="video/v_Visitor4_Steve_Titjob2_2.mkv")
                    show videov_Visitor4_Steve_Titjob2_2
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44416
                    w
                    # 4
                    # v_Visitor4_Steve_Titjob2_3
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Titjob2_3= Movie(play="video/v_Visitor4_Steve_Titjob2_3.mkv")
                    show videov_Visitor4_Steve_Titjob2_3
                    with fade
                    abby "Мпфхф..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # снимается с его члена
                    imgf 44417
                    abby "Я тащусь от вашего стояка, Босс!"
                    abby "Какой же он мощный!"
                    sound vjuh3
                    imgd 44418
                    w
                    # встает и, повернувшись спиной к нему, насаживается киской на его член
                    fadeblack 1.5
                    music Loved_Up
                    sound2 chpok6
                    img 44419 vpunch
                    w
                    # video
                    # 1
                    # v_Visitor4_Steve_Sex1_1
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor4_Steve_Sex1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Sex1_1= Movie(play="video/v_Visitor4_Steve_Sex1_1.mkv")
                    show videov_Visitor4_Steve_Sex1_1
                    with fade
                    steve "Оооо... Давай, покажи, как ты хочешь занять место Мейли, детка!"
                    wclean
                    abby "О, дааа!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44420
                    w
                    # 2
                    # v_Visitor4_Steve_Sex1_2_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor4_Steve_Sex1_1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Sex1_2_25= Movie(play="video/v_Visitor4_Steve_Sex1_2_25.mkv")
                    show videov_Visitor4_Steve_Sex1_2_25
                    with fade
                    abby "Охренительно!"
                    wclean
                    abby "Оооо, какой кайф!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44421
                    w
                    # 3
                    # v_Visitor4_Steve_Sex1_5
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Visitor4_Steve_Sex1_1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Sex1_5= Movie(play="video/v_Visitor4_Steve_Sex1_5.mkv")
                    show videov_Visitor4_Steve_Sex1_5
                    with fade
                    steve "Покажи настоящий класс!"
                    wclean
                    abby "Я никогда не хочу слазить с этого клевого стояка!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44422
                    w
                    # 4
                    # v_Visitor4_Steve_Sex1_6
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Sex1_6= Movie(play="video/v_Visitor4_Steve_Sex1_6.mkv")
                    show videov_Visitor4_Steve_Sex1_6
                    with fade
                    abby "Даааа!!!"
                    abby "Я хочу, чтобы Босс всегда меня трахал своим членом!"
                    wclean
                    steve "Дааа!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44423
                    w
                    # 5
                    # v_Visitor4_Steve_Sex1_3
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Sex1_3= Movie(play="video/v_Visitor4_Steve_Sex1_3.mkv")
                    show videov_Visitor4_Steve_Sex1_3
                    with fade
                    abby "Чтобы вытрахал меню всю!!!"
                    steve "И я трахну тебя, детка!"
                    wclean
                    steve "Хочешь, я буду каждый день тебя трахать?!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 44424
                    abby "Оооо!!!"
                    abby "О, дааа! Я хочу этого! Очень хочу!"
                    steve "Ух, какая ты горячая, детка!"
                    steve "Я люблю таких деток!"

                    music Loved_Up2
                    imgd 44425
                    w
                    # 6
                    # v_Visitor4_Steve_Sex1_4
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Visitor4_Steve_Sex1_4= Movie(play="video/v_Visitor4_Steve_Sex1_4.mkv")
                    show videov_Visitor4_Steve_Sex1_4
                    with fade
                    abby "Еще глубже! Оооох!"
                    wclean
                    abby "Да-да-да!!!"
                    abby "Еще немного!!!"
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # Эбби бурно кончает на Стиве, показывая мощный оргазм и выгибаясь
                    img 44426
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    w
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound woman_moan11
                    abby "Аааа! Как круто!"
                    abby "ОООО!!!"
                    abby "ОООООООО!!!"
                    # потом шлепает ее по заду
                    imgf 44427
                    steve "Эбби, ты молодец!"
                    steve "Вставай, детка."
                    # она соскальзывает с него с довольным лицом
                    fadeblack 1.5
                    music Groove2_85
                    imgfl 44428
                    abby "Вот это секс! Улет!"
                    steve "Да, детка. Это было жарко..."
                    # Эбби одевается и отходит от него, встает на свое прежнее место
                    # Моника недовольно косится на нее
                    imgf 44429
                    mt "Что за бред?!"
                    mt "Как можно получать удовольствие от такого извращения?!"
                    mt "Тем более, со Стивом!"
                    sound highheels_short_walk
                    imgd 44430
                    w
                    $ ep22_5_dialogues2_escort2_4_menu2 = True
                    jump ep22_5_dialogues2_escort2_4_loop1
                "Администратор Мэйли." if ep22_5_dialogues2_escort2_4_menu1 == True and ep22_5_dialogues2_escort2_4_menu2 == True:
                    # вперед выходит админша
                    sound highheels_short_walk
                    imgd 44431
                    reception "Босс, я сейчас продемонстрирую этим девочкам, как надо работать."
                    # Стив рукой, вальяжным жестом и с важным видом, подзывает ее к себе
                    imgd 44432
                    steve "Давай, Мэйли."
                    imgf 44433
                    steve "Мы все с нетерпением ждем."
                    sound Jump1
                    imgd 44434
                    w
                    # она скромно подходит к нему, садится перед ним на колени
                    fadeblack
                    sound highheels_short_walk
                    pause 2.0
                    music Loved_Up
                    imgf 44435
                    reception "Если Босс позволит, я обойдусь без льстивых слов..."
                    reception "А лучше сразу перейду к делу."
                    imgd 44436
                    steve "Мне в прошлый раз настолько понравились твои таланты, Мэйли..."
                    steve "Что ты сразу стала главной в моем ВИП-эскорте. Вне всякой конкуренции."
                    steve "Приступай..."
                    # она наклоняется над его стояком, смотрит ему в глаза
                    imgf 44437
                    reception "..."
                    steve "Да, давай, сделай это быстрее!.."
                    # она вбирает его член сначала наполовину
                    sound chpok6
                    img 44438 hpunch
                    reception "..."
                    # потом делает паузу и вбирает до основания
                    sound hlup19
                    imgd 44443
                    w
                    imgf 44439
                    w
                    imgd 44444
                    w
                    sound chpok6
                    img 44441 hpunch
                    reception "Мпфхф..."
                    # Стив восторженно
                    sound man_moan18
                    imgd 44440
                    steve "Охо-хо! Да!.."
                    imgf 44442
                    w
                    # она снова делает паузу и раскрывает рот еще шире
                    # помогая себе рукой, запихивает себе в рот мошонку Стива
                    # щеки у нее надуваются от его мошонки во рту
                    # Стив верещит от восторга
                    imgd 44445
                    w
                    sound hlup19
                    img 44446 vpunch
                    w
                    imgd 44445
                    w
                    sound hlup19
                    imgd 44446
                    w
                    imgd 44445
                    w
                    sound hlup19
                    imgd 44446
                    w
                    sound man_moan18
                    imgf 44448
                    steve "Дааа! Оооо! Вот это класс!"
                    imgd 44523
                    w
                    sound chpok8
                    imgd 44524
                    w
                    sound chpok10
                    img 44447 vpunch
                    reception "Мпфхфпфф..."
                    # все девочки с удивлением смотрят на это, у них шок
                    sound oooh2
                    imgd 44449
                    sound2 oooh3
                    reception "Мпфхф..."
                    abby "Ох, нихрена себе!"
                    linda "!!!"
                    imgd 44450
                    candice "Ого!"
                    miranda "Вот черт! Я так никогда не смогу!"
                    imgd 44451
                    mt "Какой кошмар!"
                    mt "Как можно запихать себе в рот ЭТО?!"
                    mt "!!!"
                    # член Стива выпячивается через ее горло, видно выпуклость
                    # она, продолжая держать все его богатство у себя во рту, не глядя берет его руку
                    # и прислоняет его пальцы к своему горлу, чтобы он пощупал выпуклость через горло
                    music Loved_Up2
                    imgf 44452
                    steve "Охо-хо!.."
                    sound Jump2
                    imgd 44453
                    steve "Оооо!.."
                    sound man_moan18
                    imgf 44526
                    w
                    sound hlup19
                    imgd 44525
                    w
                    imgd 44526
                    w
                    sound hlup19
                    imgd 44525
                    w
                    imgd 44526
                    w
                    sound hlup19
                    imgd 44525
                    w
                    imgd 44526
                    w
                    # она делает одно небольшое движение головой, видно как член ходит у нее в горле
                    # Стив тащится и трогает ее горло
                    imgf 44454
                    steve "ОООО!!!"
                    # она делает еще пару движений и он кончает
                    steve "Это бесподобно!"
                    menu:
                        "Кончить внутрь Мэйли.":
                            $ ep22_5_vip_escort_casting_cum_zone = 1
                            pass
                    sound man_moan18
                    imgd 44455
                    steve "Я сейчас кончу!"
                    imgf 44445
                    w
                    sound hlup19
                    imgd 44446
                    w
                    imgd 44445
                    w
                    sound hlup19
                    imgd 44446
                    w
                    img 44456
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    steve "ААААААААХХХ!"
                    # админша глотает его сперму
                    img 44457
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan18
                    reception "Мпфхф..."
                    imgd 44458
                    sound chpok5
                    w
                    # потом снимается с его члена
                    pass
            ## можно здесь сделать затемнение и звуки одежды? Так как потом Стив у меня сидит одетый.
            # Стив довольно растекается по креслу
            # админша скромненько встает рядом с ним, вытирает рот
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 44459
            reception "..."
            steve "Вот как надо добиваться карьерного роста, девочки!"
            steve "Я отдаю свой голос за Мэйли."
            steve "Она остается на своей должности администратора ВИП-эскорта!"
            # он хлопает в ладони, все девочки присоединяются к нему - аплодисменты
            imgf 44460
            steve "Молодец, Мэйли! Ты доказала нам всем, что ты лучшая в своем деле!"
            # Эбби с Мирандой недовольно переглядываются, но все же аплодируют вместе со всеми
            sound applause2
            imgd 44461
            w
            img 44462
            miranda "!!!"
            imgd 44463
            abby "!!!"
            # Моника стоит, демонстративно сложив руки на груди и не хлопает в ладони
            imgf 44464
            w
            imgd 44465
            w
            music Stealth_Groover
            imgf 44466
            mt "Тоже мне талант!!!"
            mt "Продемонстрировала степень натренированности своей безразмерной глотки!"
            mt "У нас теперь выбирают на должность тех, кто глубже заглотит мерзкий отросток Стива?!"
            mt "Бред какой-то!"
            mt "Может, та мерзость, которую сделала администраторша..."
            mt "Для остальных проституток является чем-то вне конкуренции!.."
            mt "Но я уверена, что это не так!"
            mt "!!!"
            imgd 44467
            mt "Тем не менее... Черт! Эта сучка победила!"
            mt "Как бы кто не голосовал - она все равно осталась тут главной!"
            mt "Твою мать!"
            mt "!!!"
            # затемнение
            fadeblack
            sound highheels_short_walk
            pause 1.5
            sound snd_lift
            pause 2.0
            return -2
        "Проголосовать за Эбби.":
            $ monicaVipEscortCasting2 = day # Моника проголосовала за Эбби
            # Моника смотрит на Эбби и Кэндис, те выжидательно смотрят на нее в ответ
            music Groove2_85
            imgf 44249
            mt "Если я проголосую за проститутку Эбби, как договаривалась с ней..."
            abby "..."
            candice "..."
            imgd 44248
            mt "Тогда Линда и Миранда поймут, что я не дружила с ними, а притворялась..."
            mt "И догадаются, что я обманула их насчет того, что поспособствую продвижению Линды в модели."
            # смотрит на Линду с Мирандой, те тоже в напряжении смотрят на нее
            imgd 44246
            w
            imgd 44247
            linda "..."
            miranda "..."
            imgf 44250
            mt "Они разозляться и станут действовать против меня."
            mt "Черт! Только не хватало мне двух воинственно настроенных проституток!"
            mt "Тем более, что Линда и Миранда - на редкость лицемерные змеи!"
            mt "..."
            imgd 44251
            mt "Вообще, самым лучшим решением было бы выдвинуть свою кандидатуру, но..."
            mt "Тогда все эти падшие особы во главе с администраторшей будут против меня!"
            mt "На данный момент это слишком рискованно."
            mt "Сначала мне нужно поговорить с этим мешком дерьма Стивом, а потом обдумывать план, как стать главной!"
            mt "А пока... Кого же мне выбрать?"
            mt "Черт-черт-черт!"
            mt "Думай, Моника, думай!"
            mt "!!!"
            music Stealth_Groover
            imgd 44252
            mt "Именно Эбби мне вчера сказала про это гребаное собрание!"
            mt "Она мне доверила важную информацию..."
            mt "Она стала давать мне своих клиентов вне эскорта..."
            mt "Значит, она теперь считает меня своей подругой и доверенным лицом."
            mt "Тем более, что я неоднократно помогала ей и Кэндис..."
            mt "В конце концов, они обязаны мне, потому что я вчера помогла решить их проблему с жильем!"
            mt "Если бы не моя помощь, неизвестно, смогли бы они договориться с придурком-соседом и Гарри!"
            mt "Да, они в долгу передо мной, потому что я им помогла не один раз!"
            mt "Поэтому выгоднее для меня будет, если главной станет Эбби!.."
            mt "А не эта лицемерная дрянь Миранда, от которой можно в любой момент ожидать предательства!"
            mt "Решено!"
            # админша теряет терпение, пока Моника размышляет
            music Groove2_85
            img 44253
            reception "[monica_hotel_name], нам долго ждать?!"
            reception "Хватит тянуть время! Говори имя!"
            # Моника делает покер фейс
            music Stealth_Groover
            sound2 highheels_short_walk
            imgf 44254
            w
            imgd 44255
            w
            imgd 44256
            w
            sound highheels_short_walk
            imgf 44282
            m "Я отдаю свой голос за Эбби!"
            # Линда в шоке, Миранда тоже. обе злобно шипят на Монику
            # Моника все это время продолжает держать покер фейс
            # Эбби с Кэндис радостно улыбаются
            imgd 44284
            w
            music Pyro_Flow
            sound2 oooh2
            img 44283 vpunch
            miranda "Чтоооо?!"
            linda "!!!"
            miranda "Вот сучка!"
            linda "[monica_hotel_name], как ты могла?!"
            linda "Мы тебе верили, а ты..."
            miranda "Линда, эта дрянь все это время обманывала нас!"
            # админша перебивает их ругань
            img 44262
            reception "Линда, Миранда, а ну-ка замолчали обе! Сейчас же!"
            reception "Вы как себя ведете перед Боссом?!"
            # Миранда зло указывает пальцем в сторону Моники
            imgd 44285
            miranda "Эта стерва!.."
            reception "Тихо!!!"
            # девочки замолкают и враждебно смотрят на Монику
            # та делает вид, что ничего такого не произошло
            imgf 44286
            m "..."
            # Стив доволен накаляющейся обстановкой среди девочек
            music Groove2_85
            imgd 44287
            steve "Итак, у нас есть первый голос! Отлично!"
            steve "Один голос в пользу Эбби!"
            steve "Кто следующий?"
            # Кэндис поднимает руку
            imgf 44288
            candice "Я тоже голосую за Эбби!"
            # Стив довольно
            imgd 44267
            steve "Два голоса за Эбби!"
            steve "Дальше!"
            # Линда говорит, зло косясь на Монику
            img 44289
            linda "А я отдаю свой голос за Миранду!"
            # Стив
            imgd 44290
            steve "У Эбби появился конкурент!"
            steve "Одни голос за Миранду, два - за Эбби!"
            imgd 44291
            steve "А как проголосуешь ты, Мэйли?"
            # администраторша делает шаг вперед и поворачивается к девочкам
            sound highheels_short_walk
            imgf 44292
            reception "..."
            # пристально смотрит на каждую
            reception "Я..."
            reception "Отдаю свой голос за..."
            # подходит к Миранде и встает рядом с ней, потом говорит, глядя на Стива
            sound highheels_short_walk
            imgd 44293
            reception "За Миранду!"
            # все удивленно смотрят на админшу
            music Pyro_Flow
            img 44294 vpunch
            mt "Сучка-администраторша проголосовала за Миранду..."
            mt "Неудивительно!"
            mt "Эта лицемерная дрянь не зря из кожи вон лезла, чтобы быть в фаворитах администраторши!"
            mt "!!!"
            # Стив почему-то выглядит очень довольным
            music Groove2_85
            imgf 44295
            steve "Итаааак..."
            steve "Мы имеем два голоса за Эбби и два - за Миранду!"
            # разводит руками, довольно ухмыляясь
            steve "У нас ничья, мои хорошие!"
            steve "Что это значит?"
            # админша отходит от Миранды, выходит вперед
            jump ep22_5_dialogues2_escort2_4b

        "Выдвинуть свою кандидатуру.":
            $ monicaVipEscortCasting3 = day # Моника выдвинула свою кандидатуру
            pass
    # Моника в сомнениях смотрит на Эбби и Кэндис, те выжидательно смотрят на нее в ответ
    music Groove2_85
    imgf 44249
    mt "Если я проголосую за проститутку Эбби, как договаривалась с ней..."
    abby "..."
    candice "..."
    imgd 44248
    mt "Тогда Линда и Миранда поймут, что я не дружила с ними, а притворялась..."
    mt "И догадаются, что я обманула их насчет того, что поспособствую продвижению Линды в модели."
    # смотрит на Линду с Мирандой, те тоже в напряжении смотрят на нее
    imgd 44246
    mt "Если я проголосую за проститутку Миранду, как пообещала Линде..."
    linda "..."
    miranda "..."
    mt "Тогда Кэндис и Эбби поймут, что я на самом деле не была их подругой..."
    imgd 44247
    w
    # отворачивается ото всех
    imgf 44250
    mt "В любом случае, независимо от того, как я проголосую..."
    mt "Я настрою против себя двух эскортниц."
    mt "Они разозляться и станут действовать против меня."
    mt "Черт! Только не хватало мне двух воинственно настроенных проституток!"
    mt "Тем более, что Линда и Миранда - на редкость лицемерные змеи!"
    mt "А эта Эбби не так проста, как может показаться на первый взгляд!"
    mt "..."
    imgd 44251
    mt "Вообще, самым лучшим решением было бы выдвинуть свою кандидатуру, но..."
    mt "Тогда все эти падшие особы во главе с администраторшей будут против меня!"
    mt "На данный момент это слишком рискованно."
    mt "Сначала мне нужно поговорить с этим мешком дерьма Стивом, а потом обдумывать план, как стать главной."
    mt "..."
    music Stealth_Groover
    img 44252
    mt "Хотя... Стоп! Что за бред творится в моей голове?!"
    mt "Моника, именно сейчас у тебя появился шанс занять место главной в этом гребаном эскорте!"
    mt "Ты же стремилась к этому!!!"
    mt "Почему ты думаешь, что нужно голосовать за кого-то из этих проституток?!"
    mt "Нет! Пошли эти все сучки к черту!"
    mt "Здесь присутствует лишь один достойный кандидат на место администратора ВИП-эскорта!"
    mt "Этот кандидат - Я!"
    # если Моника сука
    if monicaBitch == True:
        $ notif_monica()
        img 44298 hpunch
        mt "И пусть только этот мерзкий слизняк Стив попробует не назначить меня!!!"
        mt "Я ему яйца оторву!"
    mt "Решено!"
    mt "!!!"
    # админша теряет терпение, пока Моника размышляет
    music Groove2_85
    imgd 44253
    reception "[monica_hotel_name], нам долго ждать?!"
    reception "Хватит тянуть время! Говори имя!"
    # Моника делает покер фейс
    music Stealth_Groover
    sound2 highheels_short_walk
    imgf 44254
    w
    imgd 44255
    w
    imgd 44256
    w
    sound highheels_short_walk
    imgf 44299
    m "Я выдвигаю свою кандидатуру!!!"
    m "[monica_hotel_name] займет место администратора ВИП-эскорта!"
    # все в шоке, немая пауза
    # Моника все это время продолжает держать покер фейс
    m "..."
    # Стив радостно улыбается
    sound oooh2
    img 44300 vpunch
    sound2 oooh3
    reception "Что?!"
    m "Что слышала..."
    # девочки переглядываются, но вслух никто не возмущается
    # Стив с улыбочкой говорит
    music Groove2_85
    imgf 44301
    steve "Итак, у нас есть кандидат..."
    steve "Мо... Кхм... [monica_hotel_name] выдвинула свою кандидатуру."
    # админша пытается возмутиться
    imgd 44302
    reception "Босс, но ведь она новенькая!"
    reception "Как она может занять эту должность?"
    # Стив разводит руками
    imgd 44291
    steve "Мэйли, у нас тут демократия. Она может выдвинуть свою кандидатуру."
    steve "Другой вопрос, кто за нее проголосует, ведь..."
    # Моника возмущенно перебивает его
    music Stealth_Groover
    img 44303
    m "Какие могут быть еще голосования?! Босс!.."
    m "Достаточно того, что я выдвинула себя на эту должность!"
    # Стив с улыбочкой
    imgd 44304
    steve "Сожалею... Этого недостаточно."
    if monicaVipEscortCasting4 == 0:
        # Моника злобно смотрит на него
        img 44305
        mt "Ах ты, сволочь!"
        mt "Негодяй!"
        mt "!!!"
        m "Мне нужно с вами срочно поговорить один на один! Босс!.."
        # админша в офиге от такой наглости
        music Pyro_Flow
        imgd 44306
        reception "[monica_hotel_name], что ты себе позволяешь?!"
        reception "Мистер Стив наш Босс, а ты всего лишь одна из девочек, которая работает на него!"
        reception "По какому праву ты решила, что можешь секретничать с..."
        # Моника прерывает ее жестом, не глядя на нее, пристально смотрит на Стива
        # девочки в это время шушукаются у нее за спиной, админша зло смотрит
        sound Jump2
        img 44307 vpunch
        m "Хватит кудахтать!"
        img 44320
        reception "!!!"
        imgd 44321
        m "Это срочный разговор!!!"
        steve "Настолько срочный, [monica_hotel_name]?"
        imgd 44308
        m "Да!!!"
        m "!!!"
        # Стив вальяжно
        imgf 44309
        steve "Хорошо, давай выйдем..."
        # затемнение, шаги
        fadeblack
        sound highheels_short_walk
        pause 2.0
        jump ep22_5_dialogues2_escort2_5
    else:
        # Моника злобно смотрит на него
        imgd 44304
        m "Что еще я должна сделать?!"
        music Groove2_85
        # Стив улыбается
        steve "Ничего. Ждать результатов голосования."
        imgf 44309
        steve "И если возникнет необходимость кастинга..."
        steve "То, чтобы стать главной, тебе нужно будет обойти всех своих соперниц, [monica_hotel_name]. Хе-хе!"
        imgd 44305
        m "!!!"
        #
    label ep22_5_dialogues2_escort2_4c:
    # все на своих прежних местах, девочки в ряд у экрана, Стив сидит в первом ряду
    # девочки недовольно косятся на Монику
    music Groove2_85
    imgf 44310
    steve "Ну что, девочки! Продолжаем!"
    steve "Кто голосует следующий?"
    # Кэндис поднимает руку
    imgd 44288
    candice "Я отдаю свой голос за Эбби!"
    # Стив довольно
    imgd 44281
    steve "[monica_hotel_name] - нет голосов, Эбби - один голос!"
    steve "Дальше!"
    # Линда задумчиво смотрит на Монику, потом подходит к ней
    imgf 44311
    linda "..."
    linda "Я голосую за нее!"
    sound highheels_short_walk
    imgd 44335
    w
    imgf 44336
    sound snd_kiss2
    w
    sound2 oooh3
    imgd 44337
    w
    # все в афиге, особенно Миранда
    music Stealth_Groover
    imgf 44313
    mt "Ничего удивительного!"
    mt "Все, что ей от меня нужно - залезть в модельный бизнес."
    mt "Она будет делать все, что я скажу."
    mt "И даже пойдет против своих друзей." # взгляд на офигевшую Миранду
    music Pyro_Flow
    img 44312 vpunch
    miranda "Линда?!"
    miranda "?!?!?!"
    abby "!!!"
    candice "!!!"
    # Линда стоит с покер фейсом и ни на кого не смотрит
    imgd 44314
    linda "..."
    # Стив
    music Groove2_85
    imgf 44291
    steve "Итак!"
    steve "[monica_hotel_name] - один голос, Эбби - один голос!"
    steve "А как проголосуешь ты, Мэйли?"
    # администраторша делает шаг вперед и поворачивается к девочкам
    sound highheels_short_walk
    imgd 44315
    reception "..."
    # пристально смотрит на каждую
    sound highheels_short_walk
    imgf 44293
    reception "Я..."
    reception "Отдаю свой голос за..."
    # подходит к Миранде и встает рядом с ней, потом говорит, глядя на Стива
    reception "За Миранду!"
    # все удивленно смотрят на админшу
    # Миранда наклоняется и шепчет ей на ухо так, что их никто не слышит
    imgd 44316
    miranda "Мэйли, я в шоке от поступка Линды!"
    reception "Я тоже, Миранда. Хорошо, что мы с тобой предусмотрели этот вариант."
    # та ей подмигивает
    imgd 44317
    miranda "Да, спасибо, Мэйли."
    sound Jump2
    img 44318
    reception "Все под контролем, не переживай."
    # Моника косится на них
    music Stealth_Groover
    imgd 44294
    mt "Сучка-администраторша проголосовала за Миранду..."
    mt "Неудивительно!"
    mt "Эта лицемерная дрянь не зря из кожи вон лезла, чтобы быть в фаворитах администраторши!"
    mt "!!!"
    # Стив почему-то выглядит очень довольным
    music Groove2_85
    imgf 44295
    steve "Итаааак..."
    # разводит руками, довольно ухмыляясь
    steve "У нас ничья, мои хорошие!"
    steve "Что это значит?"
    # админша отходит от Миранды, выходит вперед
    sound highheels_short_walk
    imgd 44274
    reception "Босс, я считаю, раз голоса разделились поровну..."
    reception "И нет никакого единогласного решения по кому-либо из кандидаток..."
    reception "Значит, администратором должна остаться я."
    # Стив ей отвечает, хитро улыбаясь
    imgf 44275
    steve "Мэйли, но за тебя не было вообще ни одного голоса, верно?"
    reception "Но и единогласного решения не принято, Босс."
    steve "Что же..."
    steve "У нас есть две претендентки на место администратора - Миранда, Эбби и [monica_hotel_name]..."
    steve "А также действующий администратор Мэйли, которая утверждает, что она должна остаться в этой должности."
    imgd 44276
    reception "Да, Босс, все верно."
    # Стив притворно расстроенно вздыхает, хитро поглядывая на девочек
    imgf 44277
    steve "Ну что же теперь нам делать?.."
    steve "Видимо, по-другому никак не решить это разногласие..."
    steve "Я вынужден объявить кастинг, девочки!"
    # Моника прищурившись злобно смотрит на Стива
    imgd 44319
    mt "!!!"
    # Стив говорит девочкам
    music Hidden_Agenda
    imgf 44279
    steve "Миранда, Эбби, [monica_hotel_name] и Мэйли."
    steve "Сейчас вы по очереди продемонстрируете мне, насколько хорошо вы умеете работать с клиентом."
    steve "В роли которого буду выступать Я!" # довольно указывает на себя
    steve "Начиная с момента знакомства и до логического завершения работы. Хе-хе!"
    steve "После того, как каждая из вас продемонстрирует свои... Свои таланты..."
    steve "Я выберу ту, которая и займет вожделенное место администратора нашего ВИП-эскорта!"
    # Стив хлопает в ладони
    imgd 44280
    steve "Начали, девочки!"
    sound snd_slap1
    img 44281 hpunch
    steve "Покажите мне, как вы ведете себя с клиентом!"
    ## можно здесь сделать затемнение?) и шуршание одежды, так как будет следующий кадр где он показывает свой стояк)
    fadeblack
    sound snd_zip
    pause 2.0
    music Groove2_85
    imgfl 44296
    steve "Кто будет первой?"
    label ep22_5_dialogues2_escort2_4_loop2:
    imgf 44297
    w
    # кадр на девочек
    menu:
        "Миранда.": # повтор соответствующего пункта выше
            # Миранда делает шаг вперед, соблазнительно улыбается Стиву
            sound highheels_short_walk
            imgd 44338
            miranda "Босс не возражает, если я составлю ему компанию?"
            imgf 44339
            w
            # Стив довольно улыбается
            imgd 44340
            steve "Конечно, нет, детка!"
            # она подходит к нему
            steve "У нас тут демократия. Любая инициатива только приветствуется, детка."
            # она наклоняется и проводит рукой по его бедру
            music Loved_Up
            sound2 highheels_short_walk
            imgf 44341
            miranda "Мне нравится, когда меня называют деткой..."
            miranda "Это так возбуждает меня!"
            # Стив кладет руку ей на попу
            imgd 44342
            miranda "А как к вам обращаться, Босс?"
            sound Jump1
            img 44343
            w
            imgf 44344
            w
            imgd 44345
            steve "А меня возбуждает, когда меня называют Босс."
            steve "Что ты готова сделать ради карьерного роста, детка? Хе-хе!"
            # она задирает свою юбку
            miranda "Ваша детка хочет сделать вам что-то очень-очень приятное, Босс..."
            # обхватывает его член, водит рукой по нему
            imgf 44346
            w
            sound drkanje5
            imgd 44347
            w
            sound drkanje5
            imgd 44346
            w
            sound drkanje5
            imgd 44347
            w
            sound drkanje5
            imgd 44346
            miranda "Мммм... Какой он большой и твердый!"
            sound drkanje5
            imgd 44347
            steve "Даа..."
            # она сексуально облизывает губы и наклоняется к губам Стива
            imgf 44348
            miranda "Такой манящий!.."
            # наклоняется, целует его в губы, а он в это время лапает ее за попу
            sound lick3
            imgd 44349
            miranda "Мммм..."
            # шепчет ему в губы
            sound snd_longkiss1
            imgd 44350
            w
            imgd 44351
            w
            imgd 44352
            w
            imgd 44353
            miranda "Мне не терпится попробовать его на вкус..."
            steve "Да, давай! Сделай это для своего Босса!"
            # шлепает ее по попе, она соблазнительно ему улыбается и садится на колени перед ним
            # Стив сидит в том же кресле в зале, вальяжно развалившись
            # она наклоняется к его члену и проводит языком по стволу от основания до головки
            fadeblack 1.5
            music Loved_Up
            imgfl 44354
            w
            imgf 44355
            w
            imgd 44356
            w
            imgf 44357
            w
            sound lick3
            imgd 44358
            w
            sound lick3
            imgd 44357
            w
            sound lick3
            imgd 44358
            w
            sound lick3
            imgd 44357
            w
            sound lick3
            imgd 44358
            miranda "Мпфх... Он и правда вкусный..."
            # целует его головку, водит ею по своим губам
            sound lick3
            imgd 44359
            w
            sound lick3
            imgd 44360
            miranda "Мммм..."
            # потом вбирает его в рот, помещается не весь, наполовину
            sound drkanje5
            imgd 44361
            w
            sound drkanje5
            imgd 44360
            w
            sound drkanje5
            imgd 44361
            w
            sound drkanje5
            imgd 44360
            w
            sound drkanje5
            imgd 44361
            miranda "Мпфхфпфф..."
            # пытается протолкнуть глубже
            imgf 44362
            w

            # video
            # 1
            # v_Visitor3_Steve_Blowjob1_1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Blowjob1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Blowjob1_1= Movie(play="video/v_Visitor3_Steve_Blowjob1_1.mkv")
            show videov_Visitor3_Steve_Blowjob1_1
            with fade
            steve "Молодец, детка."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 2
            # v_Visitor3_Steve_Blowjob1_4_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Blowjob1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Blowjob1_4_25= Movie(play="video/v_Visitor3_Steve_Blowjob1_4_25.mkv")
            show videov_Visitor3_Steve_Blowjob1_4_25
            with fade
            steve "Я вижу, как ты стараешься."
            wclean
            steve "Это похвально. Твой Босс доволен. Хе-хе!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Стив кладет свою руку ей на голову
            # насаживает ее голову, но до конца она все равно не может взять его член в свой рот, у нее закатываются глаза
            imgf 44363
            steve "Я тебе помогу, детка..."
            miranda "Мпфхфпфф!!!"
            # она снимает свою голову с его члена

            imgd 44364
            w
            # 3
            # v_Visitor3_Steve_Blowjob1_5
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Blowjob1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Blowjob1_5= Movie(play="video/v_Visitor3_Steve_Blowjob1_5.mkv")
            show videov_Visitor3_Steve_Blowjob1_5
            with fade
            miranda "Мпфааа..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44365
            w

            # 4
            # v_Visitor3_Steve_Blowjob1_3_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Blowjob1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Blowjob1_3_25= Movie(play="video/v_Visitor3_Steve_Blowjob1_3_25.mkv")
            show videov_Visitor3_Steve_Blowjob1_3_25
            with fade
            miranda "Мммпфф!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 5
            # v_Visitor3_Steve_Blowjob1_2_25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Blowjob1_2_25= Movie(play="video/v_Visitor3_Steve_Blowjob1_2_25.mkv")
            show videov_Visitor3_Steve_Blowjob1_2_25
            with fade
            steve "Дааа, вот так..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44366
            w
            # смотрит ему в глаза и сексуально улыбается
            # потом встает и демонстративно проводит перед лицом Стива рукой по своей киске
            sound vjuh3
            imgd 44367
            miranda "Моя киска уже вся влажная, Босс..."
            # Стив довольно пялится на нее
            imgd 44368
            steve "Приласкай себя немного, детка."
            steve "Я хочу посмотреть на то, как ты играешь со своей влажной киской."
            # она ставит одну ногу на кресло, раскрываясь перед Стивом
            # начинает трогать себя одной рукой, а пальцы второй кладет себе в рот и сексуально облизывает
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Loved_Up
            imgfl 44369
            w
            imgf 44370
            miranda "Мммм..."
            imgd 44371
            w
            sound drkanje5
            imgd 44372
            w
            sound drkanje5
            imgd 44371
            w
            sound drkanje5
            imgd 44372
            w
            sound drkanje5
            imgd 44371
            w
            sound drkanje5
            imgd 44372
            steve "Да, молодец, детка!"
            imgf 44374
            miranda "Я вся изнемогаю, Босс..."
            imgd 44373
            miranda "Мне так хочется... Оооо..."
            sound vjuh3
            imgd 44375
            miranda "Так хочется поскорее ощутить внутри себя ваш огромный член..."
            # она лезет на Стива сверху и насаживается киской на его член
            sound chpok6
            img 44376 hpunch
            steve "Оооо, давай, покажи как ты хочешь своего большого Босса!"
            sound snd_longkiss1
            imgd 44377
            w
            imgd 44378
            w
            imgd 44379
            w
            imgd 44380
            w
            sound snd_longkiss1
            imgd 44381
            w
            imgd 44382
            w
            imgd 44383
            w

            # video
            # 1
            # v_Visitor3_Steve_Sex1_2
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Sex1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex1_2= Movie(play="video/v_Visitor3_Steve_Sex1_2.mkv")
            show videov_Visitor3_Steve_Sex1_2
            with fade
            miranda "Какой же он огромный! Дааа!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 2
            # v_Visitor3_Steve_Sex1_3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex1_3= Movie(play="video/v_Visitor3_Steve_Sex1_3.mkv")
            show videov_Visitor3_Steve_Sex1_3
            with fade
            miranda "Аааа... Как же круто!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44384
            w
            # 3
            # v_Visitor3_Steve_Sex1_4
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex1_4= Movie(play="video/v_Visitor3_Steve_Sex1_4.mkv")
            show videov_Visitor3_Steve_Sex1_4
            with fade
            miranda "Он заполняет меня всю! Как здорово!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # начинает двигаться вверх-вниз на его стояке
            imgf 44385
            w
            # 4
            # v_Visitor3_Steve_Sex1_1
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex1_1= Movie(play="video/v_Visitor3_Steve_Sex1_1.mkv")
            show videov_Visitor3_Steve_Sex1_1
            with fade
            miranda "О, дааа!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 5
            # v_Visitor3_Steve_Sex1_5
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex1_5= Movie(play="video/v_Visitor3_Steve_Sex1_5.mkv")
            show videov_Visitor3_Steve_Sex1_5
            with fade
            miranda "Оооо!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44386
            w
            imgd 44387
            w

            # video
            # 1
            # v_Visitor3_Steve_Sex2_1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Sex2_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex2_1_25= Movie(play="video/v_Visitor3_Steve_Sex2_1_25.mkv")
            show videov_Visitor3_Steve_Sex2_1_25
            with fade
            miranda "Ооо!!! Вот это да!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 2
            # v_Visitor3_Steve_Sex2_2_25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex2_2_25= Movie(play="video/v_Visitor3_Steve_Sex2_2_25.mkv")
            show videov_Visitor3_Steve_Sex2_2_25
            with fade
            miranda "Аааа!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44388
            w
            # 3
            # v_Visitor3_Steve_Sex2_4
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor3_Steve_Sex2_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex2_4= Movie(play="video/v_Visitor3_Steve_Sex2_4.mkv")
            show videov_Visitor3_Steve_Sex2_4
            with fade
            miranda "Я сейчас кончу, Босс! Кончу!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 4
            # v_Visitor3_Steve_Sex2_3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor3_Steve_Sex2_3= Movie(play="video/v_Visitor3_Steve_Sex2_3.mkv")
            show videov_Visitor3_Steve_Sex2_3
            with fade
            steve "Давай, сделай это для меня!"
            wclean
            steve "Твой Босс хочет, чтобы ты кончила, детка!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music Loved_Up2
            imgf 44389
            w
            imgd 44390
            w
            imgd 44391
            w
            img 44392
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            miranda "Оооо!!!"
            steve "Кончай!!!"
            # Миранда содрогается в оргазме, Стив держит ее за зад
            img 44393
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan14
            miranda "Аааа!"
            miranda "ААААА!!!"
            miranda "ААААААА!!!"
            # потом шлепает ее по заду
            imgf 44394
            steve "Умничка!"
            steve "Вставай, детка."
            # она соскальзывает с него с довольным лицом
            fadeblack 1.5
            music Groove2_85
            imgfl 44395
            miranda "О, это было потрясающе, Босс!"
            steve "Мне тоже понравилось, детка."
            steve "Сразу видно профессионала в своем деле. Хе-хе!"
            # Миранда одевается и отходит от него, встает на свое прежнее место
            # Моника недовольно косится на нее
            imgf 44396
            mt "На что только эти проститутки не готовы пойти!"
            mt "Противно смотреть на этот разврат! Фи!"
            sound highheels_short_walk
            imgd 44397
            mt "!!!"
            $ ep22_5_dialogues2_escort2_4_menu3 = True
            jump ep22_5_dialogues2_escort2_4_loop2

        "Эбби.": # повтор соответствующего пункта выше
            # Эбби выходит вперед с уверенным видом и сразу начинает стягивать с себя одежду
            sound highheels_short_walk
            imgd 44398
            abby "Думаю, что наш Босс, будучи таким харизматичным и брутальным мужчиной..."
            abby "Любит уверенных в себе девочек."
            imgf 44399
            w
            sound vjuh3
            img 44400 hpunch
            w
            # подходит к нему и уткнувшись пальцем в грудь облокачивает его на спинку кресла
            # потом наклоняется к нему и берет его за подбородок
            music Loved_Up
            sound2 highheels_short_walk
            imgf 44401
            abby "Которые точно знают, чего хотят..."
            sound Jump1
            img 44402 vpunch
            w
            # проводит языком по его щеке
            sound vjuh3
            imgd 44403
            steve "Ух, какая ты резкая, детка... Ты права, мне это нравится..."
            # она берет в ладони свои груди и приближает их к лицу Стива
            imgf 44404
            w
            sound lick3
            imgd 44405
            w
            imgf 44406
            abby "Босс хочет увидеть свой большой член между этими малышками?"
            imgd 44407
            steve "Хе-хе!"
            # она встает на колени перед ним и засовывает ео член между своих грудей
            # начинает медленно двигать ими
            fadeblack 1.5
            music Loved_Up
            imgf 44408
            abby "Ох, какой клевый стояк!"
            imgd 44409
            w

            # video
            # 1
            # v_Visitor4_Steve_Titjob1_1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor4_Steve_Titjob1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob1_1_25= Movie(play="video/v_Visitor4_Steve_Titjob1_1_25.mkv")
            show videov_Visitor4_Steve_Titjob1_1_25
            with fade
            abby "Дааа..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 2
            # v_Visitor4_Steve_Titjob1_2
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor4_Steve_Titjob1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob1_2= Movie(play="video/v_Visitor4_Steve_Titjob1_2.mkv")
            show videov_Visitor4_Steve_Titjob1_2
            with fade
            abby "Такая большая сочная головка!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44410
            w
            # 3
            # v_Visitor4_Steve_Titjob1_3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob1_3= Movie(play="video/v_Visitor4_Steve_Titjob1_3.mkv")
            show videov_Visitor4_Steve_Titjob1_3
            with fade
            abby "Я не могу удержаться, чтобы не попробовать ее..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 4
            # v_Visitor4_Steve_Titjob1_4
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob1_4= Movie(play="video/v_Visitor4_Steve_Titjob1_4.mkv")
            show videov_Visitor4_Steve_Titjob1_4
            with fade
            steve "Поробуй, детка, твой Босс тебе разрешает сделать это..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # продолжая водить грудями по члену, облизывает головку члена
            imgf 44411
            w
            sound lick3
            imgd 44412
            w
            sound lick3
            imgd 44411
            w
            sound lick3
            imgd 44412
            w
            sound lick3
            imgd 44411
            abby "Какой же он огромный!.."
            sound lick3
            imgd 44412
            abby "Это самый большой член, который я видела!"
            steve "Да, он у меня такой! Хе-хе!"
            # вбирает головку в рот, продолжая делать титсджоб
            sound chpok6
            img 44413 vpunch
            w
            # video
            # 1
            # v_Visitor4_Steve_Titjob2_4
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor4_Steve_Titjob2_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob2_4= Movie(play="video/v_Visitor4_Steve_Titjob2_4.mkv")
            show videov_Visitor4_Steve_Titjob2_4
            with fade
            abby "Мммм!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # отстраняется
            imgf 44414
            abby "Он еле помещается у меня во рту!"
            abby "Офигенно!"
            # снова вбирает в рот, делает титсджоб и минет одновременно
            sound chpok6
            imgd 44415
            w
            # 2
            # v_Visitor4_Steve_Titjob2_1
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob2_1= Movie(play="video/v_Visitor4_Steve_Titjob2_1.mkv")
            show videov_Visitor4_Steve_Titjob2_1
            with fade
            abby "Мпфхфпфф!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 3
            # v_Visitor4_Steve_Titjob2_2
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob2_2= Movie(play="video/v_Visitor4_Steve_Titjob2_2.mkv")
            show videov_Visitor4_Steve_Titjob2_2
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44416
            w
            # 4
            # v_Visitor4_Steve_Titjob2_3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Titjob2_3= Movie(play="video/v_Visitor4_Steve_Titjob2_3.mkv")
            show videov_Visitor4_Steve_Titjob2_3
            with fade
            abby "Мпфхф..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # снимается с его члена
            imgf 44417
            abby "Я тащусь от вашего стояка, Босс!"
            abby "Какой же он мощный!"
            sound vjuh3
            imgd 44418
            w
            # встает и, повернувшись спиной к нему, насаживается киской на его член
            fadeblack 1.5
            music Loved_Up
            sound2 chpok6
            img 44419 vpunch
            w
            # video
            # 1
            # v_Visitor4_Steve_Sex1_1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor4_Steve_Sex1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Sex1_1= Movie(play="video/v_Visitor4_Steve_Sex1_1.mkv")
            show videov_Visitor4_Steve_Sex1_1
            with fade
            steve "Оооо... Давай, покажи, как ты хочешь занять место Мейли, детка!"
            wclean
            abby "О, дааа!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44420
            w
            # 2
            # v_Visitor4_Steve_Sex1_2_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor4_Steve_Sex1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Sex1_2_25= Movie(play="video/v_Visitor4_Steve_Sex1_2_25.mkv")
            show videov_Visitor4_Steve_Sex1_2_25
            with fade
            abby "Охренительно!"
            wclean
            abby "Оооо, какой кайф!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44421
            w
            # 3
            # v_Visitor4_Steve_Sex1_5
            $ localSoundVolume = 1.0
            $ localSoundName = v_Visitor4_Steve_Sex1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Sex1_5= Movie(play="video/v_Visitor4_Steve_Sex1_5.mkv")
            show videov_Visitor4_Steve_Sex1_5
            with fade
            steve "Покажи настоящий класс!"
            wclean
            abby "Я никогда не хочу слазить с этого клевого стояка!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44422
            w
            # 4
            # v_Visitor4_Steve_Sex1_6
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Sex1_6= Movie(play="video/v_Visitor4_Steve_Sex1_6.mkv")
            show videov_Visitor4_Steve_Sex1_6
            with fade
            abby "Даааа!!!"
            abby "Я хочу, чтобы Босс всегда меня трахал своим членом!"
            wclean
            steve "Дааа!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44423
            w
            # 5
            # v_Visitor4_Steve_Sex1_3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Sex1_3= Movie(play="video/v_Visitor4_Steve_Sex1_3.mkv")
            show videov_Visitor4_Steve_Sex1_3
            with fade
            abby "Чтобы вытрахал меню всю!!!"
            steve "И я трахну тебя, детка!"
            wclean
            steve "Хочешь, я буду каждый день тебя трахать?!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44424
            abby "Оооо!!!"
            abby "О, дааа! Я хочу этого! Очень хочу!"
            steve "Ух, какая ты горячая, детка!"
            steve "Я люблю таких деток!"

            music Loved_Up2
            imgd 44425
            w
            # 6
            # v_Visitor4_Steve_Sex1_4
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Visitor4_Steve_Sex1_4= Movie(play="video/v_Visitor4_Steve_Sex1_4.mkv")
            show videov_Visitor4_Steve_Sex1_4
            with fade
            abby "Еще глубже! Оооох!"
            wclean
            abby "Да-да-да!!!"
            abby "Еще немного!!!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Эбби бурно кончает на Стиве, показывая мощный оргазм и выгибаясь
            img 44426
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan11
            abby "Аааа! Как круто!"
            abby "ОООО!!!"
            abby "ОООООООО!!!"
            # потом шлепает ее по заду
            imgf 44427
            steve "Эбби, ты молодец!"
            steve "Вставай, детка."
            # она соскальзывает с него с довольным лицом
            fadeblack 1.5
            music Groove2_85
            imgfl 44428
            abby "Вот это секс! Улет!"
            steve "Да, детка. Это было жарко..."
            # Эбби одевается и отходит от него, встает на свое прежнее место
            # Моника недовольно косится на нее
            imgf 44429
            mt "Что за бред?!"
            mt "Как можно получать удовольствие от такого извращения?!"
            mt "Тем более, со Стивом!"
            sound highheels_short_walk
            imgd 44430
            w
            $ ep22_5_dialogues2_escort2_4_menu4 = True
            jump ep22_5_dialogues2_escort2_4_loop2
        "Администратор Мэйли.": # повтор соответствующего пункта выше, кроме концовки
            # вперед выходит админша
            sound highheels_short_walk
            imgd 44431
            reception "Босс, я сейчас продемонстрирую этим девочкам, как надо работать."
            # Стив рукой, вальяжным жестом и с важным видом, подзывает ее к себе
            imgd 44432
            steve "Давай, Мэйли."
            imgf 44433
            steve "Мы все с нетерпением ждем."
            sound Jump1
            imgd 44434
            w
            # она скромно подходит к нему, садится перед ним на колени
            fadeblack
            sound highheels_short_walk
            pause 2.0
            music Loved_Up
            imgf 44435
            reception "Если Босс позволит, я обойдусь без льстивых слов..."
            reception "А лучше сразу перейду к делу."
            imgd 44436
            steve "Мне в прошлый раз настолько понравились твои таланты, Мэйли..."
            steve "Что ты сразу стала главной в моем ВИП-эскорте. Вне всякой конкуренции."
            steve "Приступай..."
            # она наклоняется над его стояком, смотрит ему в глаза
            imgf 44437
            reception "..."
            steve "Да, давай, сделай это быстрее!.."
            # она вбирает его член сначала наполовину
            sound chpok6
            img 44438 hpunch
            reception "..."
            # потом делает паузу и вбирает до основания
            sound hlup19
            imgd 44443
            w
            imgf 44439
            w
            imgd 44444
            w
            sound chpok6
            img 44441 hpunch
            reception "Мпфхф..."
            # Стив восторженно
            sound man_moan18
            imgd 44440
            steve "Охо-хо! Да!.."
            imgf 44442
            w
            # она снова делает паузу и раскрывает рот еще шире
            # помогая себе рукой, запихивает себе в рот мошонку Стива
            # щеки у нее надуваются от его мошонки во рту
            # Стив верещит от восторга
            imgd 44445
            w
            sound hlup19
            img 44446 vpunch
            w
            imgd 44445
            w
            sound hlup19
            imgd 44446
            w
            imgd 44445
            w
            sound hlup19
            imgd 44446
            w
            sound man_moan18
            imgf 44448
            steve "Дааа! Оооо! Вот это класс!"
            imgd 44523
            w
            sound chpok8
            imgd 44524
            w
            sound chpok10
            img 44447 vpunch
            reception "Мпфхфпфф..."
            # все девочки с удивлением смотрят на это, у них шок
            sound oooh2
            imgd 44449
            sound2 oooh3
            reception "Мпфхф..."
            abby "Ох, нихрена себе!"
            linda "!!!"
            imgd 44450
            candice "Ого!"
            miranda "Вот черт! Я так никогда не смогу!"
            imgd 44451
            mt "Какой кошмар!"
            mt "Как можно запихать себе в рот ЭТО?!"
            mt "!!!"
            # член Стива выпячивается через ее горло, видно выпуклость
            # она, продолжая держать все его богатство у себя во рту, не глядя берет его руку
            # и прислоняет его пальцы к своему горлу, чтобы он пощупал выпуклость через горло
            imgf 44452
            steve "Охо-хо!.."
            sound Jump2
            imgd 44453
            steve "Оооо!.."
            sound man_moan18
            imgf 44526
            w
            sound hlup19
            imgd 44525
            w
            imgd 44526
            w
            sound hlup19
            imgd 44525
            w
            imgd 44526
            w
            sound hlup19
            imgd 44525
            w
            imgd 44526
            w
            # она делает одно небольшое движение головой, видно как член ходит у нее в горле
            # Стив тащится и трогает ее горло
            sound man_moan18
            imgf 44454
            steve "ОООО!!!"
            steve "Это бесподобно!"
            imgd 44455
            steve "Молодец, Мэйли!"
            steve "Можешь остановиться. Оставь мне сил на нашу следующую кандидатку. Хе-хе!"
            # админша снимается с его члена
            # Стив довольно растекается по креслу
            # админша скромненько отходит к девочкам на свое прежнее место
            music Groove2_85
            imgf 44468
            reception "..."
            steve "Вот как надо добиваться карьерного роста, девочки!"
            sound highheels_short_walk
            imgd 44469
            m "!!!"
            $ ep22_5_dialogues2_escort2_4_menu5 = True
            jump ep22_5_dialogues2_escort2_4_loop2
        "Моника." if ep22_5_dialogues2_escort2_4_menu3 == True and ep22_5_dialogues2_escort2_4_menu4 == True and ep22_5_dialogues2_escort2_4_menu5 == True:
            # Стив хитро смотрит на Монику
            imgd 44470
            steve "А что нам продемонстрирует наша [monica_hotel_name]?.."
            steve "Которая выдвинула свою кандидатуру?"
            steve "Нелегко будет соперничать с Мэйли, не так ли? Хе-хе!"
            imgd 44471
            w
            # Моника зло на него смотрит
            # коррапшн
            $ menu_corruption = [0, monicaVipEscortCastingCorruptionRequired4]
            menu:
                "Пошел он к черту!":
                    label ep22_5_dialogues2_escort2_4d:
                    music Power_Bots_Loop
                    imgf 44472
                    mt "Я не собираюсь достигать карьерного роста таким путем!"
                    mt "Пошел этот слизняк к черту!"
                    mt "Вместе со всеми этими проститутками!"
                    imgd 44473
                    m "Я не собираюсь принимать участие в этом дурацком кастинге!"
                    # Стив разводит руками
                    music Groove2_85
                    imgd 44474
                    steve "Имеешь на это полное право, [monica_hotel_name]."
                    steve "У нас тут демократия и вы сами, девочки, принимаете решения..."
                    img 44475
                    m "!!!"
                    imgf 44291
                    steve "В таком случае..."
                    steve "Мэйли, дорогая, подойди ко мне."
                    # админша встает рядом с его креслом
                    sound highheels_short_walk
                    imgd 44459
                    reception "..."
                    steve "Я отдаю свой голос за Мэйли."
                    steve "Она остается на своей должности администратора ВИП-эскорта!"
                    # он хлопает в ладони, все девочки присоединяются к нему - аплодисменты
                    imgd 44460
                    steve "Молодец, Мэйли! Ты доказала нам всем, что ты лучшая в своем деле!"
                    # Эбби с Мирандой недовольно переглядываются, но все же аплодируют вместе со всеми
                    sound applause2
                    imgf 44461
                    w
                    img 44462
                    miranda "!!!"
                    imgd 44463
                    abby "!!!"
                    imgf 44464
                    w
                    imgd 44465
                    w
                    # Моника стоит, демонстративно сложив руки на груди и не хлопает в ладони
                    music Stealth_Groover
                    imgf 44466
                    mt "Тоже мне талант!!!"
                    mt "Продемонстрировала степень натренированности своей безразмерной глотки!"
                    mt "У нас теперь выбирают на должность тех, кто глубже заглотит мерзкий отросток Стива?!"
                    mt "Бред какой-то!"
                    mt "Может, та мерзость, которую сделала администраторша..."
                    mt "Для остальных проституток является чем-то вне конкуренции!.."
                    mt "Но я уверена, что это не так!"
                    mt "!!!"
                    imgd 44467
                    mt "Тем не менее... Черт! Эта сучка победила!"
                    mt "Как бы кто не голосовал - она все равно осталась тут главной!"
                    mt "Твою мать!"
                    mt "!!!"
                    # затемнение
                    fadeblack
                    sound highheels_short_walk
                    pause 1.5
                    sound snd_lift
                    pause 2.0
                    return -1
                "Пройти кастинг.":
                    $ monicaVipEscortCasting5 = day # Моника решилась на прохождение кастинга перед Стивом
                    pass
            # Моника стоит, демонстративно сложив руки на груди и злобно смотрит на Стива
            music Stealth_Groover
            imgf 44466
            mt "Тоже мне талант!!!"
            mt "Продемонстрировала степень натренированности своей безразмерной глотки!"
            mt "У нас теперь выбирают на должность тех, кто глубже заглотит мерзкий отросток Стива?!"
            mt "Бред какой-то!"
            mt "Может, та мерзость, которую сделала администраторша..."
            mt "Для остальных проституток является чем-то вне конкуренции!.."
            mt "Но я уверена, что это не так!"
            # все девочки с любопытством смотрят на Монику
            # она выходит вперед
            sound highheels_short_walk
            imgd 44476
            m "Что мне нужно сделать, Босс?"
            # Стив с самодовольной улыбочкой
            music Hidden_Agenda
            steve "Тебе нужно соблазнить своего Босса, [monica_hotel_name]. Хе-хе!"
            m "!!!"
            steve "И тебе придется постараться..."
            steve "Все девочки так здорово отработали, что тебе будет непросто их победить."
            # Стив показывает рукой на свой член
            steve "Но если [monica_hotel_name] будет очень-очень стараться..."
            imgf 44477
            steve "Например, сделает то, что сегодня еще никто не делал..."
            sound Jump1
            img 44478
            steve "А именно - сядет своей попой на мой член..."
            steve "То у нее есть все шансы на победу."
            # Моника зло
            music Pyro_Flow
            img 44479 vpunch
            m "Что?!"
            m "?!?!?!"
            img 44480
            mt "Ах ты, сволочь!!!"
            mt "Мерзкий мешок с дерьмом!!!"
            mt "!!!"
            # коррапшн
            $ menu_corruption = [0, monicaVipEscortCastingCorruptionRequired5]
            menu:
                "Пошел он к черту!":
                    jump ep22_5_dialogues2_escort2_4d
                "Пройти кастинг.":
                    $ monicaVipEscortCasting6 = day # Моника согласилась сесть попой на член Стива
                    pass
            # Моника настроена воинственно
            imgf 44481
            mt "Я не позволю победить этой сучке!!!"
            mt "Я сделаю все, чтобы стать главной в этом гребаном ВИП-эскорте!!!"
            mt "!!!"
            mt "Эта скотина Стив требует от меня, чтобы я пожертвовала ради этого своей попой!"
            mt "Это неоправданно завышенная цена, чтобы занять эту должность!"
            mt "Но я буквально в одном шаге от своей цели и я не упущу этот шанс!"
            mt "Я сделаю это!"
            mt "!!!"
            # Стив указывает на свой член
            music Groove2_85
            imgd 44482
            steve "Ну, [monica_hotel_name]... Давай, поворачивайся ко мне своей попкой."
            # Моника подходит к нему и злобно смотрит на него
            sound highheels_short_walk
            imgd 44483
            mt "Ты мне ответишь за это, мразь!"
            mt "!!!"
            # она задирает юбку и неуклюже раскорячивается над ним
            # Стив сидит, подставив член и заложив руки за голову
            imgf 44484
            w
            sound vjuh3
            img 44485 vpunch
            w
            imgf 44486
            w
            fadeblack 1.5
            music Loved_Up
            imgf 44487
            steve "Охо-хо! Неужели [monica_hotel_name] решилась на это?!"
            # Моника через плечо зло шипит ему
            imgd 44488
            m "Закрой рот!"
            m "!!!"
            # он в ответ широко ей улыбается
            # Моника пытается неумело сесть попой на его член, но он постоянно соскальзывает с попы
            imgf 44489
            w
            sound Jump2
            imgd 44490
            steve "Так у тебя ничего не получится, [monica_hotel_name]..."
            steve "Тебе придется помочь себе своей ручкой. Хе-хе!"
            # Моника кипит от злости
            imgd 44491
            mt "Твою мать! Мне что, придется прикасаться к нему своей рукой?!"
            mt "Ненавижу никчемного мерзавца!"
            mt "!!!"
            menu:
                "Взять рукой член Стива.":
                    pass
            # Моника берет член в руку, неуклюже корячась пытается направить его в свою попу
            # Стив довольно комментирует
            imgf 44492
            steve "Я вижу, как твоя попа хочет вобрать в себя мой член, [monica_hotel_name]..."
            steve "Хе-хе-хе!"
            imgd 44493
            steve "Давай, еще немного. Ты почти попала."
            # член снова соскальзывает
            imgd 44494
            m "Черт!"
            # Стив хватает Монику за попу
            imgf 44495
            steve "Сейчас твой Босс тебе поможет, [monica_hotel_name]."
            # насаживает ее на головку, та немного входит в попу Моники
            sound Jump1
            img 44496 hpunch
            w
            sound chpok12
            img 44497 vpunch
            m "Ай!"
            m "Больно!"
            imgd 44499
            steve "Сейчас твоя попа привыкнет, Мо... [monica_hotel_name]."
            steve "А теперь давай, опускай свою попу на мой член."
            menu:
                "Сесть на член Стива.":
                    pass
            # Моника корчится от боли, но опускает попу еще ниже
            imgf 44498
            m "Черт! Как же больно!"
            m "АЙ!!!"
            # Стив насаживает ее еще ниже
            sound chpok6
            img 44500 vpunch
            steve "Вот так!"
            m "Ай-яй-яй!!!"
            sound snd_monica_ahh
            img 44501
            m "Мне больно!"
            m "!!!"
            # входит до основания
            imgf 44502
            w

            # video
            # 1
            # v_Monica_Steve_Anal1_4
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Steve_Anal1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_4= Movie(play="video/v_Monica_Steve_Anal1_4.mkv")
            show videov_Monica_Steve_Anal1_4
            with fade
            steve "ДА!!!"
            steve "Какая отличная попа!!!"
            wclean
            steve "Ааа!!!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44503
            w
            # 2
            # v_Monica_Steve_Anal1_9_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Steve_Anal1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_9_25= Movie(play="video/v_Monica_Steve_Anal1_9_25.mkv")
            show videov_Monica_Steve_Anal1_9_25
            with fade
            steve "Давай, двигайся!"
            wclean
            m "Я не могу! Мне больно!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # у Моники на лице гримаса боли
            # он шлепает ее по попе
            imgf 44504
            w
            # 3
            # v_Monica_Steve_Anal1_1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Steve_Anal1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_1= Movie(play="video/v_Monica_Steve_Anal1_1.mkv")
            show videov_Monica_Steve_Anal1_1
            with fade
            steve "Давай, покажи мне, как ты хочешь стать главной, [monica_hotel_name]!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 4
            # v_Monica_Steve_Anal1_3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_3= Movie(play="video/v_Monica_Steve_Anal1_3.mkv")
            show videov_Monica_Steve_Anal1_3
            with fade
            m "Аааай!!!"
            wclean
            m "Ой!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # она медленно поднимается на его члене, потом опускается
            # потом еще раз
            imgf 44505
            w
            # 5
            # v_Monica_Steve_Anal1_8
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_8= Movie(play="video/v_Monica_Steve_Anal1_8.mkv")
            show videov_Monica_Steve_Anal1_8
            with fade
            steve "Слишком медленно, [monica_hotel_name]..."
            steve "Давай, быстрее!"
            wclean
            m "Я не могу! Мне больно!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Стив берет инициативу на себя и, держа Монику за бедра на одной высоте, начинает вдалбливаться в нее
            imgf 44506
            w
            # 6
            # v_Monica_Steve_Anal1_6
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_6= Movie(play="video/v_Monica_Steve_Anal1_6.mkv")
            show videov_Monica_Steve_Anal1_6
            with fade
            steve "Аааах!"
            steve "О, да! Какая прелестная попа!"
            wclean
            steve "Такая узкая, такая горячая!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44507
            w
            # 7
            # v_Monica_Steve_Anal1_7_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Steve_Anal1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_7_25= Movie(play="video/v_Monica_Steve_Anal1_7_25.mkv")
            show videov_Monica_Steve_Anal1_7_25
            with fade
            steve "Ооо! Я так хотел сделать это в твою упгругую попку, Мон... [monica_hotel_name]!"
            wclean
            steve "Дааа!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 44508
            m "!!!"
            # 8
            # v_Monica_Steve_Anal1_2
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Steve_Anal1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_2= Movie(play="video/v_Monica_Steve_Anal1_2.mkv")
            show videov_Monica_Steve_Anal1_2
            with fade
            m "Больно!"
            wclean
            m "Ай-яй-яй!!!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Стив наращивает темп, двигается еще быстрее и кончает
            music Loved_Up2
            imgf 44509
            w
            # 9
            # v_Monica_Steve_Anal1_5
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_5= Movie(play="video/v_Monica_Steve_Anal1_5.mkv")
            show videov_Monica_Steve_Anal1_5
            with fade
            steve "ОООО!!!"
            steve "Какая шикарная попа!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # 10
            # v_Monica_Steve_Anal1_10
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Steve_Anal1_10= Movie(play="video/v_Monica_Steve_Anal1_10.mkv")
            show videov_Monica_Steve_Anal1_10
            with fade
            steve "Я хочу кончить прямо в нее!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # кончает
            menu:
                "Кончить внутрь Моники.":
                    $ ep22_5_vip_escort_casting_cum_zone = 2
                    pass
            img 44456
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            steve "ААААААААХХХ!"
            img 44510
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            w
            img 44511
            sound chpok5
            w
            fadeblack 1.5
            music Pyro_Flow
            imgf 44512
            mt "Моя попа!!!"
            mt "Какая ужасная боль!"
            mt "Она вся горит!!!"
            imgd 44513
            mt "Стив мерзкий извращенец!"
            mt "Как он посмел кончить в меня?!"
            mt "Сволочь!!!"
            mt "!!!"
            # она неуклюже встает со Стива, снимаясь с его члена
            # струйка его спермы стекает из попы Моники
            # Стив довольно растекается по креслу и смотрит на нее
            music Groove2_85
            imgd 44515
            steve "А теперь обмакни свои пальцы и слижи мою сперму..."
            steve "Которая вытекает из твоей дырочки, [monica_hotel_name]."
            m "Что?!"
            steve "Тогда ты станешь моей фавориткой сегодня. Ну, давай!"
            # коррапшн
            $ menu_corruption = [monicaVipEscortCastingCorruptionRequired6, 0]
            menu:
                "Слизать сперму Стива.": # +коррапшн
                    $ monicaVipEscortCasting7 = day # Моника слизала сперму Стива, которая вытекла из ее попы
                    # Моника зло смотрит на него
                    # потом обмакивает свои пальцы в его сперме и подносит к своим губам
                    imgd 44515
                    mt "Фу, какая мерзость!"
                    mt "Но я не могу сдаться!"
                    mt "Моника Бакфетт выйдет сегодня победителем!"
                    imgf 44518
                    sound chpok5
                    w
                    imgd 44519
                    w
                    sound lick3
                    imgd 44520
                    w
                    img 44521
                    mt "!!!"
                    # слизывает
                    $ add_corruption(5, "monica_escort_steve_anal_sperm")
                    imgf 44522
                    steve "Хе-хе! Отлично, [monica_hotel_name]!"
                    steve "Итак, я принял свое решение..."
                    pass
                "Не делать этого.":
                    # Моника возмущенно смотрит на него
                    music Power_Bots_Loop
                    img 44516 hpunch
                    m "Я итак доказала, что могу делать большее, чем все они вместе взятые!"
                    m "Какое еще слизывание?!"
                    m "!!!"
                    music Groove2_85
                    imgf 44517
                    steve "Хе-хе! Я пошутил, [monica_hotel_name]."
                    steve "Я и без этого принял свое решение..."
                    pass
            # затемнение
            # все девочки стоят на своих местах
            # Стив сидит в кресле, вальяжно развалившись
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 44322
            w
            imgf 44323
            steve "Девочки, вы все сегодня старались..."
            steve "И вы большие молодцы! Я крайне доволен вашей работой!"
            steve "Я принял решение, девочки!"
            steve "Итак!.."
            imgd 44324
            steve "Победила [monica_hotel_name]!"
            steve "Встречайте нового администратора ВИП-эскорта!.."
            # он хлопает в ладони, все девочки присоединяются к нему - аплодисменты
            sound applause2
            imgf 44325
            steve "Молодец, [monica_hotel_name]! Ты доказала нам всем, что ты лучшая в своем деле!"
            # Эбби с Мирандой недовольно переглядываются, но все же аплодируют вместе со всеми
            img 44327
            miranda "!!!"
            imgd 44326
            abby "!!!"
            # админша злобно косится на Монику
            reception "!!!"
            imgd 44328
            reception "Нечестно, я так тоже могу!"
            miranda "И я!"
            abby "И я могу!"
            # Линда подбегает к Монике
            sound highheels_short_walk
            imgf 44329
            linda "Поздравляю, [monica_hotel_name]! Я так рада!"
            music Stealth_Groover
            # Моника самодовольно с высокомерием смотрит на админшу, потом на Линду
            m "Спасибо, Линда..."
            imgd 44334
            m "Спасибо, девочки."
            # Моника стоит крайне довольная собой
            imgf 44330
            mt "Я победила!"
            mt "Да, я принесла немыслимую жертву в виде своей попы!.."
            mt "Но Я ПОБЕДИЛА!!!"
            mt "!!!"
            mt "Теперь Я здесь главная! Моника, наконец-то!!!"
            mt "Ты это заслужила! Ты этого достойна!"
            mt "Потому что ты - Моника Бакфетт! Лучшая во всем!!!"
            mt "!!!"
            # Стив говорит, хитро глядя на Монику
            music Groove2_85
            imgd 44301
            steve "Девочки, прошу еще минуту внимания!"
            steve "Теперь [monica_hotel_name] будет вашей главной..."
            steve "Но насколько я знаю, [monica_hotel_name] очень занятая девушка..."
            steve "Поэтому в ее отсутствие за работой моего ВИП-эскорта будет присматривать Мэйли..."
            # Моника с админшей обмениваются недовольными взглядами
            imgd 44331
            reception "!!!"
            img 44332
            mt "!!!"
            # Стив встает с кресла
            imgf 44333
            steve "На этом наше собрание объявляется закрытым."
            steve "До встречи, девочки!"
            # затемнение
            fadeblack
            sound highheels_short_walk
            pause 2.0
            sound snd_lift
            pause 1.5
            return 1
    return

# у лифта, разговор Моники со Стивом
# если Моника не выдвигала свою кандидатуру, а голосовала за Эбби или Миранду, то лейбл срабатывает сразу после завершения кастинга девочек
label ep22_5_dialogues2_escort2_5:
    # Моника со Стивом стоят вдвоем
    # Моника злая, разговаривает со Стивом с наездом, Стив ведет себя как обычно, хитрит и улыбается ей
    music Power_Bots_Loop
    img 44177 hpunch
    m "СТИВ!"
    m "ОБЪЯСНИ, КАКОГО ЧЕРТА ТУТ ПРОИСХОДИТ?!"
    m "?!?!?!"
    # он пожимает плечами
    music Groove2_85
    imgd 44178
    steve "А что, собственно, такого тут происходит, Моника?"
    steve "Или мне тебя называть [monica_hotel_name]?"
    music Power_Bots_Loop
    img 44179 vpunch
    m "Хватит валять дурака, Стив!!!"
    m "Ты прекрасно понимаешь, о чем я!!!"
    m "!!!"
    music Groove2_85
    steve "Не понимаю, Моника. Объясни."
    # Моника бесится
    imgd 44180
    m "Какого хрена, Стив, ты тут делаешь?! Еще и в роли владельца ВИП-эскорта?!"
    imgf 44181
    steve "Потому что я и есть владелец ВИП-эскорта, Моника."
    steve "У меня к тебе тот же вопрос, Моника. Что ты тут делаешь?"
    imgd 44182
    m "Сволочь!"
    steve "Судя по всему, ты тут работаешь, да?"
    music Pyro_Flow
    sound2 Jump2
    img 44183 hpunch
    m "Это не важно!!!"
    m "Важно то, что ты являясь моим младшим партнером..."
    m "Откуда-то взял средства на покупку этого гребаного ВИП-эскорта!!!"
    m "А теперь ключевой момент, Стив! Откуда ты взял деньги?!"
    # Стив чешет лысину
    imgd 44184
    steve "Ну, понимаешь, Моника..."
    steve "Ты же знаешь, что я честный бизнесмен..."
    # она продолжает наезжать
    img 44185 vpunch
    m "Ты купил этот чертов эскорт на деньги МОЕЙ КОМПАНИИ?!"
    m "Отвечай мне, честный бизнесмен!!!"
    m "!!!"
    music Groove2_85
    imgd 44186
    steve "Моника, давай поговорим серьезно, как деловые люди."
    steve "Все очень просто."
    steve "Я люблю девочек и ты об этом прекрасно знаешь."
    steve "Обладание этим ВИП-эскортом позволяет мне изрядно сэкономить!"
    img 44187
    m "Какая, к черту, экономия, Стив?!"
    m "Ты потратил МОИ деньги!!!"
    m "Ты стал тут Боссом за МОЙ счет!!!"
    m "!!!"
    imgf 44188
    steve "А экономия элементарная, Моника..."
    steve "Раньше мне приходилось тратиться на девочек..."
    steve "А теперь они сами приносят мне деньги!"
    steve "Выгодная сделка."
    steve "Бизнес."
    # если Моника сука, она в ярости хватает его за горло
    if monicaBitch == True:
        $ notif_monica()
        music Power_Bots_Loop
        sound2 Jump2
        img 44189 hpunch
        m "Ах ты, мерзкий слизняк!"
        m "Ты как был мешком с дерьмом, так им и остался!"
        img 44190
        steve "Моника!.."
        imgd 44191
        m "Заткнись, сволочь!"
        m "Если ты меня не сделаешь главной!.."
        m "Я тебя, скотина, уничтожу!"
        m "Я всем расскажу, как ты распорядился средствами моей компании!!!"
        m "!!!"
    # если Моника приличная, то просто орет на него дальше
    else:
        music Power_Bots_Loop
        sound2 Jump2
        imgd 44192
        m "Выгодная сделка?!"
        m "Для кого выгодная?! Для тебя, сволочь?!"
        steve "Моника, это всего лишь бизнес."
        img 44193
        m "Ты обязан сделать меня главной в этом чертовом эскорте!!!"
        m "Иначе я всем расскажу, как ты распорядился средствами моей компании!!!"
        m "!!!"
        #
    # Стив снова пытается хитрить
    music Groove2_85
    imgd 44194
    steve "Моника, давай договоримся сразу - ты никому ничего рассказывать про меня не будешь..."
    steve "А я, в свою очередь, никому не расскажу про твою тайную работу."
    img 44195
    m "Ты меня еще шантажировать будешь?!"
    m "?!"
    imgf 44196
    steve "Нет-нет, ну что ты такое говоришь, Моника?!"
    steve "Какой шантаж?!"
    steve "Я пытаюсь прийти с тобой к общему знаменателю, так сказать."
    img 44197
    m "Ты меня назначишь главной! Это мое условие!"
    m "!!!"
    music Hidden_Agenda
    imgd 44198
    steve "Моника, ты же знаешь, я честно веду бизнес..."
    steve "И всегда придерживаюсь правил..."
    steve "Поэтому тебе придется заслужить право стать главной в ВИП-эскорте."
    m "Каким образом?!"
    steve "Тебе придется на кастинге сделать так, чтобы я отдал свой голос за тебя."
    music Power_Bots_Loop
    img 44199 hpunch
    m "На кастинге?!"
    m "НА КАСТИНГЕ?!?!"
    m "Пошел ты на хрен со своим кастингом!!!"
    music Hidden_Agenda
    imgd 44200
    steve "Но это будет твоя честная победа, Моника!"
    steve "Тогда никто из девочек не посмеет усомниться, что ты достойно заняла эту должность!"
    steve "Они не станут после этого плести вокруг тебя всякие заговоры и интриги."
    steve "Ты ведь за честность, Моника?"
    # Моника зло молчит
    img 44201
    m "!!!"
    steve "Тебе нужно будет всего лишь пройти кастинг и я отдам свой голос за тебя."
    steve "Вот видишь, Моника, у тебя есть привилегия среди остальных девочек."
    steve "Пройди кастинг - и место администратора ВИП-эскорта станет твоим."
    music Groove2_85
    m "Мерзавец!!!"
    m "!!!"
    imgf 44202
    steve "Кстати, очень аппетитно выглядишь в этом наряде."
    steve "У тебя, наверняка, много богатых клинтов, Моника."
    imgd 44203
    m "Иди в жопу, Стив!"
    imgd 44204
    steve "Хе-хе!"
    # довольный Стив уходит
    fadeblack
    sound man_steps
    pause 2.0
    music Pyro_Flow
    imgf 44205
    mt "Пройти унизительный кастинг и занять место главной!.."
    mt "Или не унижаться, но продолжать работать наравне с проститутками?!"
    mt "И терпеть грязные извращенства от всяких козлов?!!"
    mt "!!!"
    $ monicaVipEscortCasting4 = day # у Моники состоялся разговор со Стивом в служебном коридоре отеля
    if monicaVipEscortCasting3 > 0:
        imgd 44206
        mt "Мне нужно вернуться в конференц-зал!"
        mt "Нужно попытаться сместить сучку-администраторшу!"
        mt "Я уверена, что у меня все получится!"
        mt "!!!"
        # затемнение, каблуки
        fadeblack
        sound highheels_short_walk
        pause 2.0
        jump ep22_5_dialogues2_escort2_4c
    if monicaVipEscortCasting1 > 0 or monicaVipEscortCasting2 > 0:
        imgd 44206
        mt "Если будет еще одно собрание - я выдвину свою кандидатуру!"
        mt "Нужно попытаться сместить эту сучку-администраторшу!"
        mt "Я уверена, что у меня все получится!"
        mt "!!!"
        fadeblack
        sound highheels_short_walk
        pause 2.0
        return

# если Моника выиграла и пытается зайти в отель, либо к Стиву
label ep22_5_dialogues2_escort2_6:
    help "Продолжение ВИП-эскорта в следующих обновлениях игры!"
    return False

# если Моника выиграла и стала главной
# мысли после кастинга
label ep22_5_dialogues2_escort2_7:
    # не рендерить!!
    mt "Моника, я тобой горжусь!"
    mt "Ты сделала ЭТО!"
    mt "Ты теперь главная в этом гребаном ВИП-эскорте!"
    mt "Ура! Наконец-то!"
    mt "Теперь я покажу всем этим проституткам, кто они, а кто Я!"
    mt "!!!"
    return

# если Моника отказалась от кастинга и выиграла админша
# мысли после кастинга
label ep22_5_dialogues2_escort2_8:
    # не рендерить!!
    mt "Дьявол! Эта сучка-администраторша победила!"
    mt "Как бы кто не голосовал - она все равно осталась тут главной!"
    mt "Твою мать!"
    mt "!!!"
    return

# если Моника отказалась от кастинга и выиграла админша
# в следующий приход в эскорт, при клике на админшу (чтобы повторить кастинг, после регулярного диалога ep210_dialogues7_escort_hotel_8a, возникает меню)
label ep22_5_dialogues2_escort2_9:
    fadeblack 1.5
    music Groove2_85
    imgfl 20391
    w
    sound highheels_short_walk
    imgf 20394
    w
    imgd 44207
    mt "Снова эта дрянь командует мной!"
    mt "Как же меня все это достало!!!"
    mt "!!!"
    menu:
        "Потребовать провести собрание с Боссом.":
            $ monicaVipEscortCasting8 = day # Моника после проигрыша потребовала провести повторное собрание
            music Stealth_Groover
            imgd 44208
            mt "Я не собираюсь больше терпеть эту сучку-администраторшу!"
            mt "Главной здесь должна стать Я! И только Я!"
            mt "!!!"
            # Моника говорит, обращаясь к админше
            imgf 20395
            m "Я требую провести еще одно собрание с Боссом!"
            music Groove2_85
            imgd 20398
            reception "[monica_hotel_name], что за глупости?!"
            reception "Иди работай и не отвлекай меня!"
            reception "И вообще, ты кто такая, чтобы Босс приезжал сюда по твоему требованию?!"
            reception "Что еще за требования такие?!"
            reception "Ты!.."
            # Моника перебивает ее
            img 20397
            m "Я хочу повторить голосование!"
            m "Иначе я не выйду на работу в следующий раз!"
            # админша зло на нее смотрит, прищурившись
            imgd 20396
            reception "!!!"
            reception "Я передам твою просьбу Боссу, [monica_hotel_name]."
            reception "А сейчас за работу! Быстро!!!"
            return
        "Не делать этого.":
            # Моника возмущенно смотрит на нее
            music Stealth_Groover
            imgf 44208
            mt "Нет, я пока не готова смотреть на все эти гадости!"
            mt "А тем более, принимать в них участие!"
            mt "!!!"
            return
    return

# в следующий приход в эскорт, при клике на кого-либо из эскортниц
# мысли
label ep22_5_dialogues2_escort2_10:
    ## не рендерить!!
    mt "Я не собираюсь подходить к этой проститутке!"
    mt "Мне надоело притворяться чьей-либо подружкой!!"
    return
