define daisy = Character(t_("Дейзи"), who_color=c_pink) # сестра Софи - Daisy Hinton

default mlsBardiDay4FamilyEvening1 = 0 # Барди вызвался помочь Оливии собирать бутылки во дворе
default mlsBardiDay4FamilyEvening2 = 0 # Дейзи пригласила Барди в гости
default mlsBardiDay4FamilyEvening4 = 0 # Барди был у Дейзи дома

default ep03_dialogues3_family_evening_6_menu1 = False
default ep03_dialogues3_family_evening_6_menu2 = False
default ep03_dialogues3_family_evening_6_menu3 = False

define v_MC_Emily_Handjob1_25_sound_name = "v_MC_Emily_Handjob1_25"
define v_MC_Whore_Blowjob2_25_sound_name = "v_MC_Whore_Blowjob2_25"
define v_MC_Whore_Sex3_25_sound_name = "v_MC_Whore_Sex3_25"

#call ep03_dialogues3_family_evening_1() # вечером клик на дом, сцена с Оливией во дворе дома
#call ep03_dialogues3_family_evening_2() # заходит в дом, ужин с Софи и Дейзи
#call ep03_dialogues3_family_evening_3() # после ужина разговор с Оливией в холле
#call ep03_dialogues3_family_evening_4() # ложится спать, регулярное меню перед сном
#call ep03_dialogues3_family_evening_5() # мысли перед посещением Дейзи
#call ep03_dialogues3_family_evening_6() # визит к Дейзи


# вечером, после встречи с Райтом, при клике на дом
label ep03_dialogues3_family_evening_1:
    # Барди подходит к дому, во дворе дома, наклонившись попой вверх, стоит Оливия (в домашнем аутфите)
    # как всегда с недовольным видом, убирает пустые бутылки, оставшиеся со вчерашнего
    # Оливия Барди не видит, стоит к нему попой
    # Барди присвистывает
    sound run_stairs_floor
    fadeblack 1.5
    music2 night_ambience
    imgfl 901129
    sound2 wow
    bardi_t "Ух ты! Неплохой ракурс, Оливия!" ##->#####inc
    music Step_By_Step
    $ menu_data = {
        "Предложить свою помощь Оливии.": {"info_rabbit":True},
        "Обойдется. Пусть сама разбирается.": {"info_rat":True}
    }
    menu:
        "Предложить свою помощь Оливии.": # Rabbit
            $ mlsBardiDay4FamilyEvening1 = day # Барди вызвался помочь Оливии собирать бутылки во дворе
            imgf 901130
            bardi "Эй, Оливия! Привет!"
            bardi "Наверное, тяжко собирать все это после вчерашнего? Давай, я тебе помогу?"
            # Оливия распрямляется и смотрит на него
            imgd 901131
            olivia "Так иди и помоги! Чего ты там болтаешь стоишь?!"
            sound step_stairs_short
            imgf 901136
            w
            # Оливия отворачивается от него и снова принимается за уборку
            # Барди подходит ближе, наклоняется, тянется за бутылкой на земле
            # Оливия стоит рядом, он поворачивается и смотрит на ее зад вблизи
            # присвистывает
            imgd 901137
            sound wow
            bardi_t "Ееее... Какая аппетитная попка..."
            bardi_t "Вот бы залезть рукой под эти шортики и..."
            img white_screen
            with diss
            pause 1.0
            music Stylish_Hip_Hop_Rock
            img 901138
            show screen dream()
            with Dissolve(1.0)
            w
            sound vjuh3
            img 901139
            show screen dream()
            with hpunch
            w
            img 901140
            show screen dream()
            with diss
            w
            img 901141
            show screen dream()
            with diss
            w
            img 901140
            show screen dream()
            with diss
            w
            img 901141
            show screen dream()
            with diss
            w
            img 901140
            show screen dream()
            with diss
            w
            sound Jump1
            img 901142
            show screen dream()
            with vpunch
            w
            img 901143
            show screen dream()
            with diss
            w
            img 901142
            show screen dream()
            with diss
            w
            img 901144
            show screen dream()
            with diss
            w
            # в кадре с попой Оливии внезапно появляется рука Барди, которая тянется к ней (мечты)
            # все ближе и ближе
            # прикасается к попе, проводит по ней рукой, сжимает ягодицу
            # потом опускается к краю шортиков и лезет под шортики
            # под шортиками вверх по ягодице, потом медленно вниз, к киске
            # и вот рука уже почти у киски и тут внезапно
            music stop
            sound plastinka1b
            img 901137 vpunch
            olivia "Какого хрена ты делаешь?!"
            # руки исчезают, оставляя только попу в кадре
            # появляется недовольное лицо Оливии
            img 901146
            bardi "А что я делаю?"
            # Барди стоит в прежней позе, тянется к бутылке и пялится на зад Оливии
            music Step_By_Step
            imgd 901145
            olivia "Вот именно, что НИЧЕГО!"
            olivia "Ты сказал, что будешь помогать, а сам чем занимаешься?!"
            imgd 901146
            bardi "Я? Эээ..."
            # Барди быстро поднимает пустую бутылку с земли и показывает ее Оливии
            sound vjuh3
            img 901147 hpunch
            bardi "Я помогаю!"
            # Оливия распрямляется и грозно тычет в него пальцем
            call rrmeter(2, "ep03_dialogues3_family_evening_1") from _rcall_rrmeter_18
            music Adventures_of_the_Deaf_Dreamer
            imgf 901148
            w
            imgd 901149
            olivia "Думаешь, я не вижу, что ты пялишься на мою задницу!"
            olivia "Чертов озабоченный идиот!"
            olivia "Пошел вон отсюда, придурок!"
            # если делал массаж ног Оливии
            if mlsBardiDay3FamilyEvening5 == 0:
                imgd 901150
                bardi "Вчера вечером ты была посговорчивее..."
                sound Jump1
                img 901151 vpunch
                olivia "Еще слово про вчерашний вечер и ты точно получишь! Понял?!"
            else:
                sound Jump1
                img 901151 vpunch
                olivia "Иди отсюда!"
            # Оливия отворачивается от него и снова принимается за уборку
            # Барди бросает бутылку обратно на землю, пинает ее и отходит
            imgfl 901152
            w
            imgf 901153
            w
            sound down10
            img 901154 vpunch
            w
            imgd 901155
            w
            img 901156
            pause 0.3
            sound snd_beer_table
            img 901157 hpunch
            w
            sound steps_park
            imgf 901158
            bardi_t "Она сегодня явно не в настроении. Получила выговор от Софи?" ##->#####inc
            bardi_t "Так ей и надо. Я бы ее за такое отшлепал по попке... Так, чтобы она вся красная стала..."
            pass
        "Обойдется. Пусть сама разбирается.": # Rat
            # Барди рассматривает зад Оливии, но не подходит к ней
            imgf 901130
            bardi_t "Оливии не помешает немного поработать ручками."
            call rrmeter(-2, "ep03_dialogues3_family_evening_1") from _rcall_rrmeter_19
            bardi_t "Обойдется без моей помощи..."
            pass
        "Поддержать ее.":
            imgf 901130
            bardi "Эй, Оливия! Привет!"
            bardi "Тебя заставили убирать следы вчерашней пьянки? Тяжко, наверное?"
            # Оливия распрямляется и недовольно смотрит на него
            music Adventures_of_the_Deaf_Dreamer
            imgd 901131
            olivia "Какой пьянки?! Что ты несешь, идиот?!"
            olivia "Вали отсюда, пока в тебя не полетела одна из этих бутылок!"
            olivia "Лошара!"
            # если делал массаж ног Оливии
            if mlsBardiDay3FamilyEvening5 == 0:
                imgd 901132
                bardi "Вчера вечером ты была посговорчивее..."
                sound Jump1
                img 901133 hpunch
                olivia "Еще слово про вчерашний вечер и ты точно получишь! Понял?!"
                olivia "Иди отсюда!"
            else:
                sound Jump1
                img 901133 hpunch
                olivia "Иди отсюда!"
            # Оливия отворачивается от него и снова принимается за уборку
            # Барди бросает еще один взгляд на ее зад
            imgf 901134
            w
            imgd 901135
            bardi_t "Она сегодня явно не в настроении. Получила выговор от Софи?" ##->#####inc
            bardi_t "Сама виновата. Мало того, что напилась, так еще и бардак во дворе устроила."
            pass
    # Барди подходит к входной двери
    return

# Барди заходит в холл
label ep03_dialogues3_family_evening_2:
    fadeblack
    sound step_stairs_short
    pause 1.5
    music Adventures_of_the_Deaf_Dreamer
    imgf 901159
    bardi_t "Софи говорила, что у нас сегодня гости..." ##->#####inc
    bardi_t "И что она меня ждет к ужину. Так что лучше поторопиться, я и так задержался."
    # Барди заходит в дом
    # голос Софи из кухни
    music Little_Tomcat
    sound2 step_stairs_short
    imgf 901160
    sophie "[mcname], это ты?" ##->#####inc
    bardi "Да!"
    sophie "Мы на кухне. Идем к нам!"
    # шаги, смена кадра на кухню
    # Барди заходит
    # за столом сидят только Софи и Дейзи, ее младшая сестра
    # Дейзи вся из себя, видно, что дама при деньгах и весьма уверена в себе
    # она ведет себя с Софи и Барди приветливо, дружелюбно
    # Дейзи сидит на месте Генри, его нет
    # также нет Оливии (она убирает двор) и нет Синтии
    # Софи поворачивается к Барди и мило улыбается
    fadeblack
    sound step_stairs_short
    pause 1.0
    music Little_Tomcat
    imgfl 901170
    sophie "Милый, садись скорее за стол ужинать."
    # потом указывает на свою сестру
    sound step_stairs_short
    imgf 901171
    w
    imgd 901172
    sophie "Ты же знаком с Дейзи? Она моя младшая сестра." ##->#####inc
    music Shining_Through
    imgd 901173
    sound2 wow
    bardi_t "Ух ты!.." # кадр на грудь Дейзи
    # Софи встает со стула и идет к столешнице за тарелкой для Барди
    daisy "Привет, [mcname]!"
    imgf 901217
    bardi "Здрасьте." # кадр на лицо Дейзи
    imgd 901218
    daisy "Ничего себе, как ты вырос! Я помню тебя совсем маленьким мальчиком!"
    # Дейзи поворачивается к Софи, Барди в это время садится за стол
    imgd 901219
    daisy "Его отец как-то приглашал нас с мужем в гости. У них были какие-то общие дела." ##->#####inc
    daisy "Казалось, это было совсем недавно, а уже столько лет прошло!"
    daisy "Как время летит, да Софи?"
    imgd 901220
    sophie "Это точно, сестра..."
    # Дейзи снова переключает внимание на Барди
    imgf 901221
    daisy "[mcname], я бы тебя не узнала, если бы встретила на улице!"
    imgd 901222
    daisy "Ты стал такой высокий, такой возмужавший..."
    sound Jump1
    img 901223
    daisy "И симпатичный..." # она улыбается ему и подмигивает
    imgd 901224
    bardi "Спасибо, Дейзи..."
    # Софи ставит на стол тарелку для Барди
    imgf 901225
    sound snd_walk_barefoot
    w
    imgd 901226
    sound snd_plates1
    sophie "Вот, милый. Приятного аппетита."
    bardi "Угу. Спасибо."
    # Софи садится за стол
    sound2 highheels_short_walk
    music Little_Tomcat
    imgf 901227
    sophie "Как прошел твой день в колледже, [mcname]?"
    imgd 901217
    bardi "Все нормально."
    bardi "А где все остальные? Ну, Оливию я уже видел. А где Генри и Синтия?"
    # Дейзи встревает в разговор
    imgd 901228
    daisy "Синтия поехала ко мне домой. Они сегодня с Николь будут заниматься домашними заданиями для колледжа."
    daisy "А то, что у Генри что-то случилось на работе - это даже неплохо. Хоть посидим без его мрачной физиономии..."
    music Visions_Of_Plenty
    img 901229 vpunch
    sophie "Дейзи! Ну зачем ты так про Генри?!"
    imgd 901230
    daisy "А что такого я сказала?"
    daisy "Давно бы уже отправила его жить в этот его грязный, вонючий автосервис, Софи!"
    daisy "Все равно он там пропадает целыми днями! А толку то от этого?"
    imgd 901231
    sophie "Генри старается больше работать, чтобы заработать больше денег дня нас..."
    imgd 901232
    daisy "Ну-ну. А ты вообще уверена, что он все это время, что находится вне дома, работает?"
    imgd 901233
    bardi_t "?!"
    bardi_t "Даже так?! Генри обманывает Софи?.. Или это просто подозрения Дейзи?" ##->#####inc
    sound snd_eating
    imgf 901234
    w
    imgd 901235
    sophie "Дейзи! Давай не при [mcname]!.."
    imgd 901236
    daisy "Почему же? Пусть [mcname] знает..."
    img 901237
    sophie "Все, Дейзи! Закрыли тему. Дай ему спокойно поужинать."
    # Дейзи недовольно смотрит на Софи, но замолкает
    imgd 901238
    daisy "!!!"
    imgf 901239
    bardi "А что случилось у Генри?"
    # Софи расстроенно
    music Little_Tomcat
    imgd 901240
    sophie "У него какие-то неприятности на работе."
    sophie "Он позвонил и сказал, что сегодня будет поздно."
    img 901241
    daisy "Пфф!"
    imgd 901240
    sophie "Но что именно произошло, он не рассказывает..."
    imgd 901239
    bardi "Надеюсь, ничего серьезного."
    imgd 901242
    sophie "Да, милый, я тоже надеюсь на это."
    imgd 901243
    sophie "Кстати, ты сегодня встречался с мистером Райтом?"
    sophie "Как прошла встреча? Вы смогли договориться о твоей подработке?"
    imgd 901244
    bardi "Встреча нормально прошла."
    bardi "Но я рассчитывал на большее."
    bardi "В общем, я пока думаю..."
    # Дейзи снова лезет в их разговор
    music Shining_Through
    imgd 901245
    daisy "О, ты ищешь работу, [mcname]?"
    daisy "Слушай, как здорово! Ты мог бы и мне помогать!"
    daisy "У меня, конечно, бизнес пока небольшой и скромный... Но это пока."
    imgd 901246
    bardi "А чем ты занимаешься, Дейзи?"
    imgd 901247
    daisy "Я недавно открыла свой интернет-магазин. Мне нужен курьер, чтобы делать доставку товаров клиентам."
    imgd 901248
    bardi "Просто доставка товаров и все? Думаю, я справлюсь."
    imgd 901249
    daisy "Конечно, справишься!"
    daisy "Тем более, что это не будет занимать много времени. И не помешает твоей учебе в колледже."
    daisy "Так что, если тебя заинтересовало мое предложение, приходи ко мне в гости."
    # Дейзи улыбается ему и подмигивает
    imgd 901250
    daisy "Завтра вечером, например. Обсудим все детали..."
    sound Jump1
    imgd 901251
    w
    imgd 901248
    bardi "Окей. Я приду."
    # Софи радостно улыбается
    imgf 901252
    sophie "Это отличная идея, Дейзи!"
    imgd 901253
    sophie "[mcname], это будет здорово! Ты и Дейзи поможешь, и немного подзаработаешь!"
    imgd 901254
    bardi "Да, согласен."
    # Дейзи говорит Софи
    imgf 901255
    daisy "Ну вот и договорились! Видишь, как хорошо, что я забежала сегодня к тебе в гости, Софи?"
    imgd 901256
    sophie "Приходи к нам почаще, Дейзи. Ты же знаешь, что я всегда тебе рада."
    imgd 901257
    daisy "Спасибо, дорогая." # прикасается к руке Софи
    daisy "С вами хорошо, но мне уже пора."
    daisy "Давай, я помогу тебе убрать со стола, сестра. Потом побегу, у меня еще есть дела на сегодня."
    # Софи с Дейзи встают
    # Софи берет тарелки или что-то из посуды со стола
    # Дейзи передает Софи свою тарелку, потом подхожит к Барди
    # она наклоняется, вырез на платье приоткрывается, она медлит
    sound highheels_short_walk
    sound2 step_stairs_short
    imgf 901258
    w
    sound highheels_short_walk
    imgd 901259
    w
    imgd 901260
    daisy "[mcname], могу я убрать твою тарелку?"
    # пристально смотрит на Барди и улыбается (Софи этой сцены не видит, стоит у столешницы спиной к ним)
    music The_Heat
    imgd 901261
    bardi "Эээм... Да..." # кадры на декольте, либо observing, как она стоит возле Барди
    bardi "Спасибо, Дейзи."
    # Дейзи забирает тарелку и идет к Софи, Барди в это время пялится на попу Дейзи
    sound highheels_short_walk
    imgf 901262
    w
    imgd 901263
    bardi_t "Какая горячая штучка эта Дейзи!.." ##->#####inc
    # Софи прерывает его обглядывание зада Дейзи, поворачиваясь и обращаясь к нему
    music stop
    sound plastinka1b
    img 901264 hpunch
    sophie "[mcname], милый, хочешь я тебе сделаю какао? Или, может быть, чай?"
    # Барди встает из-за стола
    music Little_Tomcat
    sound2 step_stairs_short
    imgf 901265
    w
    imgd 901266
    bardi "Нет, не нужно. Спасибо за ужин."
    bardi "Я пойду, что-то я устал сегодня."
    # Софи ему мило улыбается
    imgd 901267
    sophie "Хорошо, милый. Спокойной ночи."
    # тетя тоже поворачивается к нему
    imgd 901268
    daisy "Пока, [mcname]. Жду тебя завтра вечером."
    imgd 901266
    bardi "Окей. Спокойной ночи."
    # Барди выходит из кухни
    $ mlsBardiDay4FamilyEvening2 = day # Дейзи пригласила Барди в гости
    fadeblack
    sound step_stairs_short
    pause 1.5
    return

# Барди идет из кухни к лестнице
label ep03_dialogues3_family_evening_3:
    # в холл с улицы заходит злая Оливия
    music Adventures_of_the_Deaf_Dreamer
    imgf 901161
    sound2 snd_walk_barefoot
    w
    imgd 901162
    bardi "О, ты только закончила со сбором бутылок, Оливия?"
    bardi "Я думал, ты давно уже в своей комнате..."
    imgd 901163
    olivia "Это не твое дело, сопляк!"
    # если делал массаж ног Оливии
    if mlsBardiDay3FamilyEvening5 == 0:
        imgd 901164
        bardi "Ножки устали? Может, массаж?"
    else:
        imgd 901164
        bardi "Предложение заглянуть к тебе в комнату с крепким алкоголем все еще в силе?"
    # Оливия зло тычет в него пальцем
    sound Jump1
    img 901165 hpunch
    olivia "Да пошел ты, придурок!"
    # она проходит мимо него, намеренно толкнув плечом и поднимается по лестнице
    # он смотрит на ее попу в шортиках, она поворачивается и показывает ему фак
    sound snd_walk_barefoot
    imgf 901166
    w
    imgd 901167
    sound wow
    w
    sound Jump2
    img 901168 hpunch
    olivia "!!!"
    # Оливия скрывается на втором этаже, хлопает дверь
    imgf 901169
    sound step_stairs_short
    bardi_t "Как всегда, Оливия очень мила со мной..." ##->#####inc
    # Барди поднимается по лестнице и идет к себе в комнату
    return

# при клике на кровать в комнате Барди
# в меню три пункта минета с Оливией, Роуз и Моррис повторяются из v1 -> арты и анимации проставить из v1, текст не менялся
# добавлены пункты с Эмили и Бекки
# изменено пробуждение, добавлены if'ы в ранее прописанные пункты с Оливией, Роуз и Моррис
# меню перед сном оставить регулярным
label ep03_dialogues3_family_evening_4:
    if ep15_sleep_regular_dialogue_skip_day == day:
        return
    # ночь, Барди ложится спать
    fadeblack 1.0
    music Jail_Clock
    imgf 900143
    bardi_t "..."
    menu:
        "Помечтать.":
            # Барди приспускает белье и достает свой стояк
            music Adventures_of_the_Deaf_Dreamer
            sound2 swish
            imgd 900163
            bardi_t "Черт! С этим я не усну. Мне явно нужна разрядка."
            sound Jump2
            img 900164 vpunch
            w
            imgd 900165
            w
            imgd 900166
            w
            imgd 900167
            w
            # он начинает водить рукой по члену вверх-вниз
            $ menu_data = {
                    "Оливия.":{"enabled":True if mlsBardiDay2Family2 > 0 or mlsBardiDay3FamilyEvening5 == 0 or mlsBardiDay4FamilyEvening1 > 0 else False},
                    "Роуз.":{"enabled":True if mlsBardiFirstDayCollege1 == 0 or mlsBardiDay3College6 > 0 else False},
                    "Миссис Морис.":{"enabled":True if mlsBardiFirstDayCollege1 > 0 or mlsBardiDay3College5 > 0 else False},
                    "Эмили.":{"enabled":True if mlsBardiDay3College4 == 0 else False},
                    "Бекки.":{"enabled":True if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0 else False}
                }
            menu:
                "Оливия.": # disabled, если не подглядывал за ней в душе или не делал ей массаж ног или не помогал с бутылками
                    # у него перед глазами возникает голая Оливия
                    # уже не его рука двигается на члене, а ее
                    # она ему улыбается игриво и пристально смотрит в глаза
                    music stop
                    img white_screen
                    with diss
                    pause 2.0
                    music Stylish_Hip_Hop_Rock
                    img 900168
                    with Dissolve(1.0)
                    w
                    imgd 900169
                    olivia "[mcname], я так хочу отсосать тебе."
                    olivia "Ты же не будешь против?.."
                    olivia "Если твоя соседка о тебе немного позаботится..."
                    # она проводит языком по головке его члена
                    imgf 900170
                    w
                    imgd 900171
                    w
                    imgd 900172
                    w
                    imgd 900171
                    w
                    imgd 900170
                    w
                    imgd 900173
                    olivia "Мммм..."
                    sound lick3
                    imgd 900174
                    w
                    sound lick3
                    imgd 900173
                    w
                    sound lick3
                    imgd 900174
                    w
                    imgf 900175
                    w
                    imgd 900176
                    olivia "Как же я хочу сделать это..."
                    # она облизывается, потом вводит его член в рот и начинает двигать головой
                    # анимация
                    # Оливия периодически смотрит ему в глаза, отрываясь от члена и облизываясь
                    imgd 900177
                    w
                    sound chpok8
                    img 900178 hpunch
                    w

                    # video
                    # v_Bardie_Sister_Older_Blowjob1
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Bardie_Sister_Older_Blowjob1_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Bardie_Sister_Older_Blowjob1 = Movie(play="video/v_Bardie_Sister_Older_Blowjob1.mkv", fps=30)
                    show videov_Bardie_Sister_Older_Blowjob1
                    wclean
                    olivia "Мпфхфмм..."
                    wclean
                    bardi "О, как же это охрененно!.."
                    olivia "Мммм..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 900180
                    olivia "Какой обалденный член... Хочется облизываеть его снова и снова."
#                    imgf 900179
#                    w
                    sound chpok8
                    imgd 900178
                    w
                    imgd 900176
                    olivia "Кончи для меня, [mcname]..."
                    menu:
                        "Кончить Оливии в рот.":
                            imgd 900178
                            bardi "О, какой кайф..."
                            bardi "О, Оливия!.. Я сейчас!!!"
                            # Барди бурно кончает ей в рот
                            img 900181
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "О, дааа!!!"
                            olivia "Мпфхф!!!"
                            sound2 chpok5
                            imgd 900182
                            w
                            imgd 900183
                            w
                            sound Jump1
                            img 900184
                            w
                            imgd 900183
                            w
                            # Оливия снимается с его члена
                            # смотрит ему в глаза, губы в сперме
                            # облизывается и подмигивает ему
                            pass
                        "Кончить на лицо Оливии.":
                            imgd 900178
                            bardi "О, какой кайф..."
                            bardi "О, Оливия!.. Я сейчас!!!"
                            bardi "Хочу сделать это на твое лицо!.. Ооо!"
                            # Оливия снимается с его члена и подставляет лицо, доводя его до оргазма рукой
                            # Барди бурно кончает ей на лицо
                            img 900185
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "Оооо!!!"
                            sound2 chpok5
                            imgd 900186
                            olivia "О, дааа!.."
                            imgd 900187
                            w
                            sound Jump1
                            img 900188
                            w
                            # смотрит ему в глаза, лицо в сперме
                            # облизывается и подмигивает ему
                            pass
                        "Кончить на грудь Оливии.":
                            imgd 900178
                            bardi "О, какой кайф..."
                            bardi "О, Оливия!.. Я сейчас!!!"
                            bardi "Хочу сделать это на твою грудь!.. Ооо!"
                            # Оливия снимается с его члена и доводит его до оргазма грудью
                            # Барди бурно кончает на ее грудь
                            imgd 900189
                            w
                            imgd 900190
                            bardi "Оооо!!!"
                            img 900191
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
                            bardi "Дааа!!!"
                            sound2 chpok5
                            imgd 900192
                            olivia "О, дааа!.."
                            # смотрит ему в глаза, грудь в сперме
                            # она берет немного спермы пальчиком и облизывает его, подмигивает
                            pass
                    fadeblack 2.0
                    music stop
                    music2 Jail_Clock
                    pass
                "Роуз.": # disabled, если не разговаривал с Роуз или если не прятался в раздевалке от Гарри
                    # у него перед глазами возникает голая Роуз
                    # уже не его рука двигается на члене, а ее
                    # она ему смущенно улыбается и смотрит в глаза
                    music stop
                    img white_screen
                    with diss
                    pause 2.0
                    music Stylish_Hip_Hop_Rock
                    img 900196
                    with Dissolve(1.0)
                    w
                    imgd 900197
                    student_rose "[mcname], я никогда не делала этого..."
                    imgd 900198
                    student_rose "Он такой... Большой."
                    imgd 900197
                    student_rose "Ты уверен, что он поместится у меня во рту?"
                    # она проводит языком по головке его члена
                    sound lick3
                    imgd 900199
                    w
                    imgd 900200
                    student_rose "Мммм..."
                    imgd 900201
                    w

                    # video
                    # v_Nice_Girl_Blowjob1_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Nice_Girl_Blowjob1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Nice_Girl_Blowjob1_25 = Movie(play="video/v_Nice_Girl_Blowjob1_25.mkv", fps=25)
                    show videov_Nice_Girl_Blowjob1_25
                    wclean
                    bardi "О, Роуз, ты отлично смотришься..."
                    bardi "Мммм... А теперь попробуй взять его в свой ротик..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 900202
                    student_rose "Он такой приятный. Мне нравится."
                    student_rose "Я сейчас попробую сделать это..."
                    # она вводит его член в рот и начинает двигать головой
                    # анимация
                    # Роуз периодически смотрит ему в глаза, отрываясь от члена и улыбаясь ему
                    sound chpok8
                    img 900203 hpunch
                    w
                    imgd 900204
                    w

                    # video
                    # v_Nice_Girl_Blowjob2_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Nice_Girl_Blowjob2_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Nice_Girl_Blowjob2_25 = Movie(play="video/v_Nice_Girl_Blowjob2_25.mkv", fps=25)
                    show videov_Nice_Girl_Blowjob2_25
                    wclean
                    bardi "О, Роуз, у тебя здорово получается..."
                    student_rose "Мпфхфмм..."
                    wclean
                    bardi "Оооу!.. Только не останавливайся!.."
                    student_rose "Мммм..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 900205
                    w
                    imgd 900206
                    student_rose "Мммм..."
                    imgd 900207
                    bardi "О, Роуз, я сейчас кончу!.."
                    menu:
                        "Кончить Роуз в рот.":
                            imgd 900206
                            bardi "О, какой кайф..."
                            bardi "О, Роуз!.. Я сейчас!!!"
                            # Барди бурно кончает ей в рот
                            img 900208
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "О, дааа!!!"
                            student_rose "Мпфхф!!!"
                            sound2 chpok5
                            imgd 900209
                            w
                            # Роуз снимается с его члена
                            # смотрит ему в глаза, губы в сперме
                            # улыбается ему
                            pass
                        "Кончить на лицо Роуз.":
                            imgd 900206
                            bardi "О, какой кайф..."
                            bardi "О, Роуз!.. Я сейчас!!!"
                            # Роуз снимается с его члена и подставляет лицо, доводя его до оргазма рукой
                            # он бурно кончает ей на лицо
                            imgd 900210
                            bardi "Хочу сделать это на твое лицо!.. Ооо!"
                            img 900211
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "Оооо!!!"
                            sound2 chpok5
                            imgd 900212
                            student_rose "Мммм, [mcname]... Да..."
                            # смотрит ему в глаза, лицо в сперме
                            # улыбается ему
                            pass
                        "Кончить на грудь Роуз.":
                            imgd 900206
                            bardi "О, какой кайф..."
                            bardi "О, Роуз!.. Я сейчас!!!"
                            # Роуз снимается с его члена и доводит его до оргазма рукой
                            # Барди бурно кончает на ее грудь
                            imgd 900210
                            bardi "Хочу сделать это на твою грудь!.. Ооо!"
                            img 900213
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "Оооо!!!"
                            sound2 chpok5
                            imgd 900214
                            student_rose "Мммм, [mcname]... Да..."
                            imgd 900215
                            w
                            # смотрит ему в глаза, грудь в сперме
                            # улыбается ему
                            pass
                    fadeblack 2.0
                    music stop
                    music2 Jail_Clock
                    pass
                "Миссис Морис.": # disabled, если не разговаривал с преподавательницей по живописи или не помогал ей с ватманами
                    # у него перед глазами возникает голая преподавательница
                    # уже не его рука двигается на члене, а ее
                    # она ему призывно улыбается и трется голой грудью о член
                    music stop
                    img white_screen
                    with diss
                    pause 2.0
                    music Stylish_Hip_Hop_Rock
                    img 900221
                    with Dissolve(1.0)
                    w
                    imgd 900222
                    teacher_morris "[mcname], я так хочу сделать тебе приятное..."
                    imgf 900223
                    w
                    sound drkanje5
                    imgd 900224
                    w
                    sound drkanje5
                    imgd 900223
                    w
                    sound drkanje5
                    imgd 900224
                    w

                    # video
                    # v_Teacher1_Titjob1_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Teacher1_Titjob1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Teacher1_Titjob1_25 = Movie(play="video/v_Teacher1_Titjob1_25.mkv", fps=25)
                    show videov_Teacher1_Titjob1_25
                    wclean
                    teacher_morris "Твой член... Он такой красивый, такой манящий..."
                    wclean
                    bardi "О, миссис Морис, не ожидал, что это будет так прикольно..."
                    teacher_morris "Тебе еще больше понравится, что я хочу сделать дальше, [mcname]..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")


                    # убирает грудь от члена и проводит языком по головке
                    imgf 900225
                    w
                    imgd 900226
                    w
                    sound lick3
                    imgd 900227
                    w
                    imgd 900228
                    w
                    imgd 900229
                    teacher_morris "Вкусно..."
                    teacher_morris "Мммм..."
                    teacher_morris "Я так хочу тебя, [mcname]!.."
                    # она вводит его член в рот и начинает двигать головой
                    # анимация
                    # преподша периодически смотрит ему в глаза, отрываясь от члена и улыбаясь ему
                    imgd 900230
                    w
                    sound chpok8
                    img 900231 hpunch
                    w

                    # video
                    # v_Teacher11_Blowjob1_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_Teacher11_Blowjob1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_Teacher11_Blowjob1_25 = Movie(play="video/v_Teacher11_Blowjob1_25.mkv", fps=25)
                    show videov_Teacher11_Blowjob1_25
                    wclean
                    teacher_morris "Мпфхфмм..."
                    wclean
                    bardi "Оооо, миссис Морис!.. О, дааа!.."
                    teacher_morris "Мммм..."
                    bardi "Я скоро кончу, миссис Морис!.. Ооо!.."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 900229
                    teacher_morris "Кончи для меня, [mcname]..."
                    menu:
                        "Кончить миссис Морис в рот.":
                            imgd 900231
                            bardi "О, какой кайф..."
                            bardi "О, миссис Морис!.. Я сейчас!!!"
                            # Барди бурно кончает ей в рот
                            img 900233
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "О, дааа!!!"
                            teacher_morris "Мпфхф!!!"
                            sound2 chpok5
                            imgd 900234
                            w
                            sound Jump1
                            imgd 900235
                            w
                            # миссис Морис снимается с его члена
                            # смотрит ему в глаза, губы в сперме
                            # подмигивает ему, улыбаясь
                            pass
                        "Кончить на лицо миссис Морис.":
                            imgd 900231
                            bardi "О, какой кайф..."
                            bardi "О, миссис Морис!.. Я сейчас!!!"
                            # миссис Морис снимается с его члена и подставляет лицо, доводя его до оргазма рукой
                            # Барди бурно кончает ей на лицо
                            imgd 900232
                            bardi "Хочу сделать это на твое лицо!.. Ооо!"
                            img 900236
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "Оооо!!!"
                            sound2 chpok5
                            imgd 900237
                            teacher_morris "О, дааа!.."
                            sound Jump1
                            imgd 900238
                            w
                            # смотрит ему в глаза, лицо в сперме
                            # подмигивает ему, улыбаясь
                            pass
                        "Кончить на грудь миссис Морис.":
                            imgd 900231
                            bardi "О, какой кайф..."
                            bardi "О, миссис Морис!.. Я сейчас!!!"
                            # миссис Морис снимается с его члена и доводит его до оргазма грудью
                            # Барди бурно кончает на ее грудь
                            imgd 900232
                            bardi "Хочу сделать это на твою грудь!.. Ооо!"
                            img 900239
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "Оооо!!!"
                            sound2 chpok5
                            imgd 900240
                            teacher_morris "О, дааа!.."
                            imgd 900241
                            w
                            sound Jump1
                            imgd 900242
                            w
                            # смотрит ему в глаза, грудь в сперме
                            # подмигивает ему, улыбаясь
                            pass
                    fadeblack 2.0
                    music stop
                    music2 Jail_Clock
                    pass
                "Эмили.": # disabled, если отдал ей телефон и переписывался с ней (кролик)
                    # у него перед глазами возникает Эмили в одном нижнем белье (в котором присылала фотку)
                    # уже не его рука двигается на члене, а ее
                    # она ему призывно улыбается и делает хэнджоб
                    music stop
                    img white_screen
                    with diss
                    pause 2.0
                    music Stylish_Hip_Hop_Rock
                    img 901174
                    with Dissolve(1.0)
                    w
                    imgd 901175
                    w
                    imgf 901176
                    student_emily "[mcname], это так мило, что ты отдал мне мой телефон..."
                    student_emily "Я больше не хочу быть с придурком Гарри... Мне нравится быть с тобой."
                    student_emily "Нравится делать тебе приятно..."
                    # наклоняется и проводит языком по головке члена
                    imgd 901177
                    w
                    sound lick3
                    imgd 901178
                    student_emily "Мммм..."
                    sound lick3
                    imgd 901179
                    w

                    # отстраняется и проводит рукой по своей груди (в бра)
                    imgf 901180
                    w
                    imgd 901176
                    student_emily "Я так хочу тебя, [mcname]..."
                    # снова начинает делать хэнджоб
                    imgd 901181
                    w
                    sound drkanje5
                    imgd 901182
                    w
                    sound drkanje5
                    imgd 901181
                    w
                    sound drkanje5
                    imgd 901183
                    w
                    imgd 901185
                    student_emily "Ты такой клевый, такой сексуальный..."
                    # прикусывает губу и строит ему глазки
                    sound lick3
                    imgd 901184
                    student_emily "Мммм..."
                    imgd 901185
                    student_emily "Покажешь, как ты хочешь меня? Кончишь для меня, [mcname]?"

                    # video
                    # v_MC_Emily_Handjob1_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_MC_Emily_Handjob1_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_MC_Emily_Handjob1_25 = Movie(play="video/v_MC_Emily_Handjob1_25.mkv", fps=25)
                    show videov_MC_Emily_Handjob1_25
                    wclean
                    student_emily "Мпфхфмм..."
                    wclean
                    bardi "О, дааа!.."
                    bardi "Я скоро кончу, Эмили!.. Ооо!.."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # движения ее руки ускоряются и Барди кончает
                    menu:
                        "Кончить на грудь Эмили.":
                            # Эмили подставляет свою грудь (в бра)
                            imgf 901186
                            bardi "О, какой кайф..."
                            bardi "О, Эмили!.. Я сейчас!!!"
                            # Барди кончает ей на грудь
                            img 901187
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "О, дааа!!!"
                            sound2 chpok5
                            imgd 901188
                            student_emily "Мммм..."
                            imgf 901191
                            w
                        "Кончить на лицо Эмили.":
                            # Эмили подставляет свое лицо
                            imgf 901186
                            bardi "О, какой кайф..."
                            bardi "О, Эмили!.. Я сейчас!!!"
                            # Барди бурно кончает ей на лицо
                            img 901189
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            bardi "Дааа!!!"
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man moan8
                            bardi "О, дааа!!!"
                            sound2 chpok5
                            imgd 901190
                            student_emily "Мммм..."
                            pass
                    # она смотрит на Барди и призывно улыбается
                    fadeblack 2.0
                    music stop
                    music2 Jail_Clock
                    pass
                "Бекки.": # disabled, если сцены с Бекки не было
                    # у него перед глазами возникает голая Бекки
                    # уже не его рука двигается на члене, а ее
                    # она ему пошло улыбается
                    music stop
                    img white_screen
                    with diss
                    pause 2.0
                    music Stylish_Hip_Hop_Rock
                    imgd 901202
                    whore "Оооо, обожаю твой член!"


                    # пара движений и она снимается с члена, наклоняется и вбирает его в рот
#                    fadeblack 0.5
                    sound2 chpok6
                    img 901204 hpunch
                    whore "Мпфх!.."
                    imgd 901205
                    whore "Мммм..."
                    imgf 901206
                    w
                    imgd 901207
                    w

                    # video
                    # v_MC_Whore_Blowjob2_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_MC_Whore_Blowjob2_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_MC_Whore_Blowjob2_25 = Movie(play="video/v_MC_Whore_Blowjob2_25.mkv", fps=25)
                    show videov_MC_Whore_Blowjob2_25
                    wclean
                    whore "Мпфх!.."
                    wclean
                    bardi "О, дааа!.."
                    whore "Мммм..."
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    music Stylish_Hip_Hop_Rock
                    img 901192
                    with Dissolve(1.0)
                    w
                    imgd 901193
                    whore "Хочу скорее оттрахать тебя, красавчик!.."
                    whore "Мне не терпится почувствовать своей киской твой каменный стояк!"
                    # она лезет на него и, приставив член к своей киске, начинает водить им туда-сюда
                    # Барди тянет руку и лапает ее грудь, бедра, киску
                    imgf 901194
                    w
                    imgd 901195
                    whore "О, да!.."
                    imgd 901196
                    whore "Ооо!.."
                    imgd 901195
                    w
                    imgf 901197
                    w
                    # напрявляет член на киску и вводит
                    sound lick3
                    imgd 901198
                    whore "Оооох!.."
                    sound chpok6
                    img 901199 hpunch
                    bardi "Ееее!.."
                    # она начинает двигаться на нем
                    imgf 901200
                    whore "Оооо!"
                    #imgd 901201
                    #w

                    # потом снова садится на его член, секс
                    imgfl 901208
                    whore "Даа!.. Как же кайфово!"
                    whore "Аааа!"
                    imgd 901203
                    w
                    imgd 901201
                    w

                    # video
                    # v_MC_Whore_Sex3_25
                    $ localSoundVolume = 1.0
                    $ localSoundName = v_MC_Whore_Sex3_25_sound_name
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
                    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
                    scene black
                    image videov_MC_Whore_Sex3_25 = Movie(play="video/v_MC_Whore_Sex3_25.mkv", fps=25)
                    show videov_MC_Whore_Sex3_25
                    wclean
                    whore "Оттрахай меня, красавчик! Оттрахай Бекки как следует!"
                    bardi "Дааа!.."
                    wclean
                    whore "Ооо! Бекки сейчас кончит!"
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # шлюха кончает
                    img 901209
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound woman_moan11
                    w
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound woman_moan12
                    whore "ААААА!"
                    whore "АААААААА!!!"
                    bardi "О, дааа!!!"
                    # Барди кончает следом
                    menu:
                        "Кончить на киску Бекки.":
                            # Бекки снимается с члена и сидит над ним, широко раздвинув ноги
                            imgd 901210
                            bardi "О, какой кайф..."
                            bardi "О, Бекки!.."
                            # Барди кончает ей на киску
                            img 901213
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
                            bardi "Дааа!!!"
                            sound2 chpok5
                            imgd 901411
                            bardi "О, дааа!!!"
                            imgf 901215
                            whore "Мммм..."
                            imgd 901216
                            w
                            pass
                        "Кончить в киску Бекки.":
                            imgd 901210
                            bardi "О, какой кайф..."
                            bardi "О, Бекки!.."
                            # Барди бурно внутрь киски
                            img 901211
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
                            bardi "Дааа!!!"
                            sound2 chpok5
                            imgd 901212
                            bardi "О, дааа!!!"
                            imgf 901215
                            whore "Мммм..."
                            imgd 901216
                            w
                            # Бекки снимается с члена и сидит над ним, широко развинув ноги
                            pass
                    # она смотрит на Барди и призывно улыбается, сперма стекает с ее киски
                    fadeblack 2.0
                    music stop
                    music2 Jail_Clock
                    pass
                "Лечь спать.":
                    imgd 900144
                    bardi_t "Уже поздно. Я сегодня очень устал и хочу спать."
                    # затемнение, тиканье часов
                    pass
            # виденье тает и комната становится темной
            # тиканье часов
        "Лечь спать.":
            imgd 900144
            bardi_t "Уже поздно. Я сегодня очень устал и хочу спать."
            # затемнение, тиканье часов
            pass
    imgf 900045
    w
    # комната, тиканье часов
    music2 stop
    return

# далее лейбл ep03_dialogues1_family_morning_5 (утро следующего дня)

######################### вечер следующего дня (Day5)

# мысли перед посещением Дейзи
label ep03_dialogues3_family_evening_5:
    ## не рендерить!!
    bardi_t "У меня еще есть время до вечеринки."
    bardi_t "Нужно зайти к Дейзи. Она говорила, что будет ждать меня..."
    return

# локация на карте - до тети

# при клике на локацию
# Барди стоит у дома Дейзи
label ep03_dialogues3_family_evening_6:
    # Барди присвистывает
    music Adventures_of_the_Deaf_Dreamer
    imgfl 901269
    bardi_t "Неплохой такой дом у Дейзи!.."
    bardi_t "С халупой, где живет Софи конечно не сравнить..." ##->#####inc
    bardi_t "Интересно, чем занимается ее муж?"
    sound step_stairs_short
    imgf 901270
    sound2 snd_door_bell1
    w
    # Барди подходит к входной двери и звонит в дверной звонок
    # дверь открывается, на пороге возникает Дейзи в том же платье, что и была у Софи
    # она пристально смотрит на Барди и улыбается ему
    fadeblack 1.0
    sound snd_door_open1
    pause 1.5
    music Shining_Through
    imgf 901271
    sound2 highheels_short_walk
    w
    imgd 901272
    daisy "Ох, [mcname], а я тебя уже заждалась..."
    imgd 901273
    bardi "Да, привет."
    imgd 901274
    daisy "Заходи в дом."
    # затемнение, шаги
    # смена кадра на гостиную дома Дейзи
    # она проходит в глубь гостиной и плюхается на диван, хлопает ладонью по дивану, подзывая Барди к себе
    sound snd_door_open1
    imgf 901275
    sound2 highheels_short_walk
    w
    imgd 901276
    w
    sound highheels_short_walk
    imgf 901277
    w
    imgd 901278
    daisy "Садись. Будешь чай или кофе? Или чего-нибудь повеселее?"
    imgd 901279
    w
    sound Jump1
    img 901280
    w
    imgd 901279
    w
    sound Jump1
    img 901280
    w
    imgf 901281
    bardi "Нет, спасибо. У меня еще дела сегодня..."
    # Дэйзи смотрит на Барди с ухмылкой
    imgd 901278
    daisy "Оу... Все эти ваши молодежные дела? Алкоголь, девочки?.."
    imgd 901281
    bardi "Да не то что бы... Просто договорились встретиться с другом."
    # Барди отводит взгляд в сторону
    imgd 901282
    bardi_t "Ну и двинуть в местечко, наполненное алкоголем и девушками... Черт! Шон, наверное, уже ждет."
    imgd 901283
    daisy "Да брось ты! Знаю я все эти ваши дела..."
    # Барди садится на диван, она двигается к нему ближе
    sound step_stairs_short
    imgf 901284
    w
    imgd 901285
    daisy "Жаль конечно, что ты торопишься. Мы могли бы немного поболтать, может, выпить немного шампанского..."
    imgd 901286
    bardi "Шампанского?"
    # она улыбается и подмигивает ему

    imgd 901287
    daisy "Да. Совсем немного, чтобы расслабиться."
    sound Jump1
    imgd 901288
    daisy "Уверена, моя сестра была бы не против..."
    imgd 901289
    bardi "..."

    music Future_Bass
    # video
    # v_Observe_Auntie_1_25
    img black_screen
    with diss
    pause 1.0
    scene black
    image videov_Observe_Auntie_1_25 = Movie(play="video/v_Observe_Auntie_1_25.mkv", fps=25, loop=False, image="/images/Slides/img_911222.jpg")
    show videov_Observe_Auntie_1_25
    $ renpy.pause(0.5, hard=True)
    pause 7.0
    img 911222
    show screen image_shake("/images/Slides/img_911222.jpg")
    w

    # Дейзи поворачивается к Барди, закидывает ногу на ногу
    # ведет себя, демонстрируя свое расположение к Барди
    imgf 901291
    w
    sound vjuh3
    imgd 901290
    w
    imgd 901292
    daisy "Да и Николь с Синтией как раз уже ушли..."
    imgd 901293
    bardi_t "Мне кажется или она флиртует со мной?!"
    bardi_t "Хах, может Шон все же немного подождет?.."
    # Дэйзи отстраняется от Барди
    music Shining_Through
    imgf 901294
    daisy "Но, думаю, у нас еще будет на это время. Не будем заставлять твоих друзей ждать..."
    imgd 901295
    bardi_t "Черт!"
    bardi "Да, так что там с интернет-магазином?.."
    imgd 901296
    daisy "Ах да, интернет-магазин..."
    daisy "В общем, если кратко, я решила развлечь себя хоть чем-то, пока муж скачет от командировки к командировке..."
    daisy "И остановила свой выбор на собственном интернет-магазине."
    daisy "Знаешь, а оказывается, это так интересно!"
    daisy "Узнавать информацию по всяким товарам, читать отзывы по ним, вести обсуждения..."
    # Дэйзи смотрит на Барди с двухсмысленной игривой ухмылкой
    imgd 901297
    daisy "Ну и, конечно же, читать отзывы заказчиков с фотографиями и благодарностями..."
    daisy "Пожалуй, это лучшее в моей работе!"
    # Дэйзи подмигивает Барди вальяжно и сексуально усевшись на диване
    sound Jump2
    imgd 901298
    daisy "Да, думаю это самое интересное в этой работе..."
    daisy "Эти фотографии, конечно, конфиденциальные..."
    daisy "Но, думаю, ничего не случится, если я как-нибудь покажу тебе некоторые из них."
    imgf 901299
    w
    imgd 901300
    bardi "А какие товары в твоем магазине?"
    imgd 901301
    daisy "А ты как думаешь? Учитывая то, что я считаю, что тебе будет интересно?"
    # Барди задумчиво - рукой придерживает подбородок
    imgd 901302
    bardi "Может одежда и аксессуары?"
    imgd 901303
    bardi_t "Было бы классно заполучить фотки в нижнем белье одной из преподавательниц в колледже..."
    # показываем арт, где профессорша в одном бра
    music stop
    img white_screen
    with diss
    pause 0.5
    music The_Heat
    $ camera_icon_enabled = False
    pause 0.5
    img 901304
    show screen dream()
    with Dissolve(1.0)
    show screen image_shake("/images/Slides/img_901304.jpg")
    bardi_t "К примеру, профессора Ричардсон."
    w
    $ camera_icon_enabled = True
    # арт сменяется снова на Дейзи
    # она многозначительно улыбается
    music stop
    img white_screen
    with diss
    pause 0.5
    music Shining_Through
    pause 0.5
    img 901305
    with Dissolve(1.0)
    daisy "Еще есть предположения?"
    # Барди предполагает вытянув руку ладонью вверх на уровне груди, кончики пальцев направлены в сторону Дэйзи
    imgd 901306
    bardi "Мммм... Может быть, косметика?"
    bardi "Хотя, вряд ли она была бы мне интересна..."
    bardi "Просто у меня нет больше предположений."
    # она хихикает
    sound snd_woman_laugh2
    imgd 901307
    daisy "И снова не угадал, [mcname]..."
    # у Дэйзи искренняя милая улыбка
    daisy "Я продаю игрушки. Ну и улыбки вместе с радостью."
    # Барди разочарованно думает
    imgd 901308
    bardi "О, это будет весьма мило привозить клиентам плюшевых мишек и-и..."
    # внезапно кадр меняется - профессор Ричердсон в том же нижнем белье стоит, обнимая плюшевого мишку
    $ camera_icon_enabled = False
    music stop
    img white_screen
    with diss
    pause 0.5
    music The_Heat
    pause 0.5
    img 901309
    show screen dream()
    with Dissolve(1.0)
    show screen image_shake("/images/Slides/img_901309.jpg")
    w
    bardi_t "И с чего она взяла, что мне будет интересно смотреть на фотки плюшевых зверей?"
    bardi "Хотя, это весьма мило..."
    w
    $ camera_icon_enabled = True
    # кадр снова меняется на тетю - Дэйзи кладет руку на его бедро и он замолкает
    img white_screen
    with diss
    pause 0.5
#    music The_Heat
    pause 0.5
    img 901310
    with Dissolve(1.0)
    w
    sound Jump2
    img 901311 hpunch
    bardi_t "Оу!.."
    imgd 901312
    w
    music Shining_Through
    imgd 901313
    daisy "И снова ты не угадал, [mcname]..."
    daisy "Боже! Откуда ты такой милый и невинный?! Так и хочется тебя затискать!"
    imgd 901310
    bardi_t "Ну нихрена себе! Это я то невинный?"
    # рука Дэйзи скользит по бедру Барди чуть выше, он с интересом и удивлением смотрит на этот процесс
    imgf 901311
    w
    sound vjuh3
    img 901314 hpunch
    bardi_t "А впрочем, почему бы и нет?.."
    imgd 901310
    bardi "Ну и что в итоге я буду доставлять?"
    imgd 901313
    daisy "Игрушки для взрослых." # ее рука остановилась и она пристально смотрит на него.
    # Барди сидит в изумлении.
    music stop
    sound plastinka1b
    img 901310 hpunch
    bardi "?!?!"
    # смена кадра снова на директрису - она в своем черном кожанном БДСМ костюме, с дилдо, в откровенной позе (резкий контраст с предыдущими кадрами директрисы)
    $ camera_icon_enabled = False
    music stop
    img white_screen
    with diss
    pause 0.5
    music The_Heat
    pause 0.5
    img 901315
    show screen dream()
    with Dissolve(1.0)
    show screen image_shake("/images/Slides/img_901315.jpg")
    bardi_t "Ну нихрена себе!"
    w
    # Дэйзи все также сидит положив ладонь на бедро Барди и поглядывает на его пах
    # у него начинает вставать но это не особо заметно. Гг слегка удивленно смотрит на Дэйзи
    $ camera_icon_enabled = True
    music stop
    img white_screen
    with diss
    pause 0.5
    music Step_By_Step
    pause 0.5
    img 901316
    with Dissolve(1.0)
    bardi "Для взрослых? То есть... Все эти штуки?.."
    imgd 901317
    daisy "Да. Дилдо, вибраторы... Также есть лубриканты, презервативы... Ну и все тому подобное..."
    imgd 901318
    bardi_t "Охренеть!"
    imgf 901317
    daisy "И мне очень нужен помощник для доставки товаров моего магазина..."
    imgd 901316
    bardi "Окей. Я понял."
    bardi "Моей задачей будет разносить товары клиентам, верно?"
    bardi "Все эти дилдо и вибраторы?.."
    imgd 901317
    daisy "Да, ты все правильно понял, милый."
    imgd 901316
    bardi "А что насчет оплаты?"
    # Дейзи немного смущена
    # Дэйзи убирает руку с бедра Барди и улыбаясь поднимает указательный палец вверх на уровне головы, при этом наклонившись к Барди
    imgd 901319
    daisy "К слову, мои клиентки обычно твои ровесницы. Да и городок у нас маленький..."
    daisy "Может, тебе даже встретятся твои знакомые..."
    # Барди с коварной ухмылкой сидит направив взгляд в пустоту.
    # Представляет поочередно несколько своих знакомых в сексуальных позах
    # смена кадра - одноклассница-фрик, затем след. кадр зануда Сара, затем след. кадр Роуз
    # на всех кадрах они сидят (стоят) в нижнем белье в сексуальных позах (можно в колледже)
    imgd 901320
    bardi_t "А вот это интересно..."
    menu:
        "Одногруппница.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901321 #Кэти
            show screen dream()
            with Dissolve(1.0)
            show screen image_shake("/images/Slides/img_901321.jpg")
            w
            img 901322
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901322.jpg")
            w
            pass
        "Сара.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901323 #Сара
            show screen dream()
            with Dissolve(1.0)
            show screen image_shake("/images/Slides/img_901323.jpg")
            w
            img 901324
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901324.jpg")
            w
            pass
        "Хлоя.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901325 #Хлоя
            show screen dream()
            with Dissolve(1.0)
            show screen image_shake("/images/Slides/img_901325.jpg")
            w
            img 901326
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901326.jpg")
            w
            pass
        "Роуз.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901327 #Роуз
            show screen dream()
            with Dissolve(1.0)
            show screen image_shake("/images/Slides/img_901327.jpg")
            w
            img 901328
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901328.jpg")
            w
            pass
        "Эмили.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901329 #Эмили
            show screen dream()
            with Dissolve(1.0)
            show screen image_shake("/images/Slides/img_901329.jpg")
            w
            img 901330
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901330.jpg")
            w
            pass
    $ camera_icon_enabled = True
    music stop
    img white_screen
    with diss
    pause 0.5
    music Step_By_Step
    pause 0.5
    # смена кадра на Дейзи
    # Дэйзи видит что Барди заинтересовался и с ухмылкой продолжает эротично наклонившись к нему
    # нужно показать ее с красивых ракурсов, будто она пытается соблазнить Барди. кладет руку на бедро и так далее.
    # Барди переводит взгляд на ее лицо
    img 901333
    with Dissolve(1.0)
    daisy "Ну а другая половина - мои ровесницы..."
    # Барди смотрит на прелести Дэйзи
    imgd 901334
    daisy "И, чаще всего, это одинокие женщины, которым не хватает ласки и заботы..."
    # Барди отводит задумчивый взгляд в сторону
    # смена кадра - миссис Морис в сексуальной позе в нижнем белье
    menu:
        "Миссис Морис.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901331 #Морис
            show screen dream()
            with Dissolve(1.0)
            show screen image_shake("/images/Slides/img_901331.jpg")
            bardi_t "Очень даже интересно..."
            daisy "И плюс ко всему этому - ты будешь еще и зарабатывать. По 5 баксов за выход на работу."
            img 901332
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901332.jpg")
            bardi "Ага. Заманчиво..."
            pass
        "Миссис Кларк.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901412 #Кларк
            show screen dream()
            with Dissolve(1.0)
#            show screen image_shake("/images/Slides/img_901412.jpg")
            bardi_t "Очень даже интересно..."
            daisy "И плюс ко всему этому - ты будешь еще и зарабатывать. По 5 баксов за выход на работу."
            img 901413
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901413.jpg")
            bardi "Ага. Заманчиво..."
            pass
        "Мисс Янг.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901414 #Янг
            show screen dream()
            with Dissolve(1.0)
#            show screen image_shake("/images/Slides/img_901414.jpg")
            bardi_t "Очень даже интересно..."
            daisy "И плюс ко всему этому - ты будешь еще и зарабатывать. По 5 баксов за выход на работу."
            img 901415
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901415.jpg")
            bardi "Ага. Заманчиво..."
            pass
        "Миссис Адамс.":
            music stop
            $ camera_icon_enabled = False
            img white_screen
            with diss
            pause 0.5
            music Stylish_Hip_Hop_Rock
            pause 0.5
            img 901416 #Адамс
            show screen dream()
            with Dissolve(1.0)
#            show screen image_shake("/images/Slides/img_901416.jpg")
            bardi_t "Очень даже интересно..."
            daisy "И плюс ко всему этому - ты будешь еще и зарабатывать. По 5 баксов за выход на работу."
            img 901417
            show screen dream()
            with fade
            show screen image_shake("/images/Slides/img_901417.jpg")
            bardi "Ага. Заманчиво..."
            pass
    $ camera_icon_enabled = True
    # фантазия рушится (смена кадра на тетю), Барди возвращается в реальность ошарашенный
    music stop
    sound plastinka1b
    img 901335 hpunch
    bardi "Погоди! Сколько?!"
    music Visions_Of_Plenty
    imgd 901336
    daisy "Нуу... Понимаешь, мой магазин только открылся..."
    imgd 901337
    bardi "Пять баксов?! Серьезно?! Это же будет цена моего обеда на работе!"
    bardi_t "Она что, прикалывается надо мной?! Это же практически работа за бесплатно!"
    # она торопливо
    imgd 901338
    daisy "Но позже я увеличу тебе оплату! Обязательно!"
    imgd 901337
    bardi_t "Так и знал, что это ловушка! А ведь так все хорошо начиналось!"
    bardi_t "Ну ведь точно не могло быть все так идеально!"
    bardi "Но!.."
    # она снова кладет руку ему на бедро и наклоняется к нему ближе, демонстрируя вырез на платье
    # Барди пялится
    sound vjuh3
    img 901339 vpunch
    daisy "Ты же не откажешь мне в помощи, [mcname]?.." ##->#####inc
    imgd 901316
    bardi "Я..."
    # Барди продолжает пялится на прелести тети
    # она загадочно ему улыбается и также держит руку на его бедре
    bardi_t "Хмм..."
    bardi_t "Я, конечно, рассчитывал на большее..."
    bardi_t "Но если есть перспектива увеличения оплаты..."
    music Shining_Through
    imgf 901340
    bardi_t "Да кого я обманываю?!"
    bardi_t "Я буду обходить дома одиноких девушек, которым критически не хватает члена!.."
    bardi_t "Да и... Я правда могу встретить знакомых... Думаю, будет полезно знать, кто из них шалит сама с собой."
    bardi_t "Стоит заняться этим. Хотя бы до тех пор, пока я не познакомлюсь с парочкой горячих нимфоманок."
    imgd 901335
    bardi "Да, давай я попробую, Дейзи."
    bardi "Тебе нужна помощь, а мне - деньги."
    bardi "Думаю, глупо было бы отказываться."
    # она обрадованно улыбается
    imgd 901341
    daisy "Ой, как здорово!"
    # она прикасается к его волосам, ее лицо совсем близко
    imgd 901342
    daisy "Я рада, что ты согласился, [mcname]!"
    daisy "Предлагаю тебе уже на днях приступить к работе! Каждую субботу я доставляю товар. А до тех пор он копится на складе."
    daisy "Для начала я тебя ознакомлю со всем ассортиментом товара моего магазина!.."
    sound Jump1
    imgd 901343
    daisy "Вот увидишь, тебе понравится работать со мной." # подмигивает
    imgd 901344
    bardi_t "Оу, даже не сомневайся в этом!"
    bardi "Да, думаю мне понравится."
    # Дэйзи улыбается
    imgd 901342
    daisy "Ладно, тогда я не буду тебя задерживать. Твои друзья, наверное, уже заждались..."
    # Барди встает с дивана
    imgd 901344
    bardi "Ох, точно! Я совсем забыл..."
    # Дейзи встает следом
    sound highheels_short_walk
    imgf 901345
    w
    imgd 901346
    daisy "Я рада, что ты заглянул ко мне и мы поболтали... О делах..."
    # она приближается к нему и чмокает его в щеку
    daisy "Заходи ко мне в гости почаще да и Николь хотела познакомиться с тобой ближе." ##->#####inc
    imgd 901347
    sound kiss2
    w
    imgd 901348
    daisy "Ну или... К слову, я часто бываю дома одна по вечерам." # многозначительно улыбается
    daisy "Мы могли бы обсудить еще раз нашу совместную работу..."
    imgd 901349
    bardi "Окей. Хорошего вечера, Дейзи."
    daisy "И тебе хорошо провести вечер, [mcname]."
    # смена кадра, Барди выходит из дома Дейзи
    fadeblack
    sound snd_door_open1
    pause 1.5
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgf 901350
    bardi_t "Уфф!.. Какая горячая штучка эта Дейзи!.." ##->#####inc
    bardi_t "Работа с ней обещает быть очень... Хмм... Интересной."
    $ mlsBardiDay4FamilyEvening4 = day # Барди был у Дейзи дома
    return


# далее звонок от Шона - ep03_dialogues2_college_11 (написан в файле колледжа)
