default monicaCitizens9Slums1 = 0 # Моника согласилась сдать апартаменты в аренду для курения Найджелу
default monicaCitizens9Slums2 = 0 # Моника согласилась на минет и косяк
default monicaCitizens9Slums3 = 0 # Моника предложила Филу косяк Найджела
default monicaCitizens9Slums4 = 0 # Моника согласилась на секс с Филом

default monicaCitizens5Slums1 = 0 # Моника согласилась пойти Акирой саном в свои апартаменты
default monicaCitizens5Slums2 = 0 # Моника согласилась, чтобы Акира нацепил зажимы на ее грудь
default monicaCitizens5Slums3 = 0 # Моника согласилась, чтобы Акира нацепил зажимы на ее киску

define monicaCitizens9CorruptionRequired1 = 350 # Моника согласилась привести Найджела к себе в квартиру
define monicaCitizens9CorruptionRequired2 = 450 # Моника согласилась на то, чтобы сделать минет и участвовать в состязании
define monicaCitizens9CorruptionRequired3 = 500 # Моника начала делать минет Найджелу
define monicaCitizens9CorruptionRequired4 = 590 # Моника согласилась на секс с Филом
define monicaCitizens9CorruptionRequired5 = 550 # Моника наступила каблуком на член Фила
define monicaCitizens5CorruptionRequired1 = 350 # Моника согласилась привести Акира Сан к себе в квартиру
define monicaCitizens5CorruptionRequired2 = 400 # Моника согласилась, чтобы Акира нацепил на ее грудь зажимы
define monicaCitizens5CorruptionRequired3 = 450 # Моника согласилась, чтобы Акира нацепил на вторую грудь зажимы
define monicaCitizens5CorruptionRequired4 = 500 # Моника согласилась, чтобы Акира нацепил на ее киску зажимы

default v_Monica_Citizen6_Blowjob1_1_sound_name = "v_Monica_Citizen6_Blowjob1_1"
default v_Monica_Citizen9_Blowjob1_1_sound_name = "v_Monica_Citizen9_Blowjob1_1"
default v_Monica_Citizen6_Sex1_1_sound_name = "v_Monica_Citizen6_Sex1_1"

default ep217_dialogues4_citizens_cumzone = 0

default monicaMadeBlowjobNigel = False
#call ep217_dialogues4_citizens_1() # при клике на упоротого чувака в парке
#call ep217_dialogues4_citizens_2() # при клике на азиата у ресторана (Akira San)

# при клике на упоротого чувака в парке
label ep217_dialogues4_citizens_1:
    music Groove2_85
    imgr Dial_Citizen_9_3
    citizen9 "Йо, дамочка - на попе ямочка!"
    citizen9 "Ты чего такая серьезная?"
    citizen9 "А?...А?...А?"
    # Моника высокомерно
    imgl Dial_begin35_18
    mt "Кажется этот придурок прокурил остатки мозгов!"
    mt "Никчемный жалкий отброс общества! Фи!"
    m "Что тебе нужно?!"
    imgr Dial_Citizen_9_4
    citizen9 "Сегодня дамочка особенно серьезна..."
    citizen9 "Но ничего..."
    citizen9 "У Найджела есть отличное предложение, которое поднимет дамочке настроение..."
    citizen9 "Только..."
    citizen9 "Тссс..."
    citizen9 "Пойдем обсудим это в укромном месте."
    # Найджел подмигивает Монике
    citizen9 "Хы!"
    imgl Dial_begin35_16
    mt "Кретин!!!"
    mt "Никчемный обитатель трущоб!"
    m "..."
    menu:
        "Пойти с ним.":
            imgl Dial_begin35_21
            m "Что еще за 'отличное предложение'?"
            imgr Dial_Citizen_9_2
            citizen9 "Тсссс..."
            citizen9 "Хы-хы, я же сказал..."
            citizen9 "В укромном месте."
            imgl Dial_begin35_21
            mt "Может, я смогу заработать на его 'отличном предложении'?"
            mt "Он выглядит придурком. Я смогу получить его деньги и практически ничего не делать для этого."
            m "Пошли..."
            # затемнение
            pass
        "Отказать!":
            music Stealth_Groover
            imgl Dial_begin35_17
            m "Вряд ли у такого как ты найдется 'отличного предложение' для меня!"
            m "И вообще, такие леди, как Я, не ходят по всяким укромным местам с такими..."
            m "Такими, как ты! Фи!"
            music Groove2_85
            imgr Dial_Citizen_9_4
            citizen9 "Оу-оу! Ну ты и злюка сегодня, дамочка!"
            citizen9 "Но если захочешь стать добрее или веселее..."
            citizen9 "Я тут... Хы-хы..."
            imgr Dial_Citizen_9_3
            citizen9 "Или там... Хы-хы..."
            citizen9 "Короче, найдешь меня!"
            imgl Dial_begin35_16
            mt "Укуренный придурок!"
            mt "!!!"
            return -1
    # рендерить отсюда!!
    # стоят у пилона
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 12241
    m "Говори, что у тебя там за 'отличное предложение'!"
    m "Или ты и дальше будешь попусту тратить мое время?"
    imgd 12242
    citizen9 "Оу-оу-оу!"
    # Найджел оглядывается по сторонам и достаёт из внутреннего кармана косяк
    music Marty_Gots_a_Plan
    imgd 33403
    w
    imgd 33404
    citizen9 "Смотри, дамочка... Йоу!"
    sound Jump1
    img 33405
    citizen9 "Какой жирный косяк..."
    citizen9 "Хы-хы!"
    # проводит косяком у себя под носом и затягивается запахом
    imgf 33406
    citizen9 "Агрррр!!! Отменная дурь!!!"
    citizen9 "Мои кореша куда-то свалили..."
    citizen9 "А курить такую дурь в одиночестве..."
    citizen9 "Еще и на улице - неправильно!!" # Найджел подмигивает Моника указывая двумя указательными пальцами в её сторону
    imgd 33407
    mt "?!?!?!"  # Моника в недоумении приподнимает бровь
    if monicaCitizensPunksBlowjob1 == True:
        # если Моника приводила домой панков
        imgf 12244
        citizen9 "Так что я вспомнил, как мои кореша..."
        citizen9 "Рассказывали, что у дамочки есть сутенерская хата..."
        citizen9 "На которой она всем сосет!"
        citizen9 "Хы-хы!"
        # У Моники офигевшее лицо
        #
        $ notif(_("Моника приводила в свои апартаменты в трущобах Тима и Тома."))
        #
        music Power_Bots_Loop
        img 40333 hpunch
        mt "ЧТОООООО?!"
        mt "Эти идиоты уже всем рассказали?!"
        mt "Твою мать!!!"
        mt "Придурки!!!"
        mt "Кретины!!!"
        music Marty_Gots_a_Plan
        imgd 12268
        citizen9 "Поэтому я хочу пойти твою сутенерскую квартирку!"
        citizen9 "И курнуть там этот жирный косяк. Хы-хы!"
        citizen9 "Ну что скажешь?"
        imgd 33408
        citizen9 "Отличное предложение?" # Найджел подмигивает Монике с ухмылкой
        music Groove2_85
        img 12269
        m "Скажу что ты придурок, а твои кореша ИДИОТЫ !!!"
        m "Эта квартира не сутенерская!!!"
        m "И я не со... Не делала того, что они говорят!"
        # Найджел отпрыгивает
        imgd 33409
        citizen9 "Оу-оу-оу! Да ладно тебе!"
        citizen9 "Я дам тебе $ 20!"
        citizen9 "Вот, смотри дамочка!"  # Найджел трясет купюрой перед Моникой
        #
    else:
        # если не приводила панков
        music Marty_Gots_a_Plan
        imgd 33409
        citizen9 "Так что я подумал, может у дамочки есть местечко, где можно курнуть?"
        citizen9 "Я бы щедро заплатил!"
        citizen9 "Вот $ 20!"  # Найджел трясет купюрой перед Моникой
        citizen9 "Отличное предложение от отличного парня - Найджела!!!"
        citizen9 "Еееее!!!"
        #
    m "..."
    $ menu_corruption = [monicaCitizens9CorruptionRequired1, 0]
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                imgf 40334
                mt "Хммм..."
                mt "Деньги за место, где он может просто покурить..."
                mt "Я могу заработать на этом болване $ 20."
                mt "Мне даже не нужно для этого делать какие-нибудь мерзости."
                mt "Черт! Но у меня нет такого места!"
                #
                $ notif(t_("Монике некуда вести клиентов."))
                #
                imgd 12288
                m "Мне некуда тебя вести!"
                citizen9 "Уууууу, дамочка!"
                citizen9 "Ты упускаешь такой шанс!"
                citizen9 "Обращайся, как появится место..."
                imgf 33408
                citizen9 "Сможешь немного подзаработать..."  # Найджел подмигивает
                return False
            # если арендует квартиру у Джека
            $ monicaCitizens9Slums1 = day # Моника согласилась сдать апартаменты в аренду для курения Найджелу
            pass
        "Мой дом не притон для наркоманов!":
            music Stealth_Groover
            imgf 40334
            mt "От этого грязного наркомана за милю несет травой!"
            mt "Еще не хватало, чтобы он мне прокурил весь дом!"
            imgd 12273
            m "Мой дом не место для вонючих наркоманов из трущоб!!!"
            music Groove2_85
            imgd 33410
            citizen9 "Уууууу!!!"
            citizen9 "Сама ты вонючка, дамочка!"
            citizen9 "И рожа у тебя кислая!!!"
            # Моника в ярости дает Найджелу поджопник
            sound snd_kick_fred1
            img 33411 hpunch
            m "Аааггггррррр!!!"
            sound snd_runaway
            img 33412
            # Найджел убегает
            return -2
    # Моника задумчиво
    music Groove2_85
    imgf 40333
    mt "Хммм, $ 20..."
    mt "Может, мне просто сдавать эти апартаменты для таких отбросов, как он?" # Моника задумалась и считает
    mt "Тогда мне не придется показывать свое прекрасное тело за деньги."
    mt "Или делать всякие извращенские гадости..."
    imgd 12270
    citizen9 "Эй, дамочка, ну так что?"
    imgd 12271
    m "..."
    menu:
        "$ 30!":
            pass
    imgf 12243
    m "$ 30!"
    m "Или можешь искать другое место для себя... И своего косяка!" # Моника принебрежительно
    m "!!!"
    imgd 40344
    mt "Мне нужны эти деньги!"
    mt "Я должна оплачивать эту уродливую дыру в трущобах!"
    # выглядывает мамочка
    music Master_Disorder
    img 24343 vpunch
    mt "А тут еще эта старая карга..."
    mt "Неужели у нее нет других дел, кроме как следить за мной!"
    imgd 24344
    w
    if ep214_perry_debt > 0:
        #
        $ notif(_("Моника должна выплачивать Перри долг."))
        imgd 19174
        mt "Я должна выплачивать долг этой мерзкой извращенке Перри!"
        #
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 40334
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    music Groove2_85
    imgf 12244
    m "..."
    citizen9 "Хорошо, дамочка..."
    citizen9 "30 баксов! Найджел сегодня щедрый!"
    citizen9 "Показывай дорогу!"
    # затемнение, спустя некоторое время
    # апартаменты Моники
    # Моника и Найджел стоят в гостиной в апартаментах
    # он оглядывается
    fadeblack 1.5
return

label ep217_dialogues4_citizens_1a:
#    call ep211_quests_slums_apartments2_check_enter_forced()
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_18
    scene black_screen
    with Dissolve(1)
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 33174
    w
    imgf 33175
    citizen9 "Охохооооо, дамочка!"
    imgd 33176
    citizen9 "Не думал я, что ты живешь в такой дыре!"
    m "Можешь проваливать, если не нравится!"
    m "!!!"
    imgd 33177
    citizen9 "Не-не, все окей!"
    citizen9 "Просто подумал, вдруг ты хочешь еще подзаработать?"
    m "???"
    m "В смысле?!"
    m "О чем это ты?!"
    music Marty_Gots_a_Plan
    imgf 33178
    citizen9 "Йоу, дамочка, как ты меня слушала?"
    citizen9 "Я же говорил, что курить такую дурь в одиночестве - неправильно!"
    citizen9 "И я предлагаю тебе..."
    # Найджел подмигивает Моника указывая двумя указательными польцами в её сторону
    music Power_Bots_Loop
    img 33179 hpunch
    m "ТЫ ЧТО..."
    m "ПРЕДЛАГАЕШЬ МНЕ ЭТУ ДРЯНЬ!?"
    m "?!?!?!"
    m "МНЕ!!! Мон.."
    # Моника хватается за рот понимая что чуть не проболталась
    music stop
    sound plastinka1b
    img 33180
    m "!!!"
    music Groove2_85
    imgd 33181
    w
    imgd 33182
    mt "Черт! Чуть не сказала свое имя!"
    # Найджел пожимая плечами, разводит руки в стороны
    music Marty_Gots_a_Plan
    imgf 33183
    citizen9 "Я предлагаю тебе подзаработать."
    citizen9 "Найджел - хороший парень, он видит, что дамочка живет в такой дыре."
    citizen9 "И предлагает ей деньги за то..."
    citizen9 "Что она сможет сделать больше тяг, чем Найджел!"
    imgd 33184
    citizen9 "А перед этим отсосет у Найджела!"
    citizen9 "Найджел получит двойной кайф!"
    citizen9 "А дамочка хорошо заработает!"
    music Pyro_Flow
    img 33185
    m "Чтоо?!"
    m "Я!? Курить эту мерзость и делать ЭТО!?"
    m "!!!"
    music Marty_Gots_a_Plan
    imgf 33186
    citizen9 "Дамочка отсосет у Найджела и получит $ 5."
    citizen9 "Если дамочка сделает больше тяг после этого, то..."
    sound Jump1
    img 33187
    citizen9 "Найджел платит ей еще $ 5 сверху!"
    citizen9 "Итого дамочка может заработать 40 баксов!"
    citizen9 "А если выиграет Найджел - дамочка даст Найджелу трахнуть себя!"
    # Моника зло на него смотрит
    music Pyro_Flow
    imgd 33188
    mt "Этот грязный отброс хочет..."
    mt "Чтобы я оскверняла свое прекрасное тело этой дрянью?!"
    mt "Еще и делала эти мерзости с его отростком?!"
    imgd 33189
    mt "За какие-то жалкие $ 10?!"
    mt "О Моника! Какие ужасные вещи ты вынуждена терпеть!!!"
    mt "Утонченая леди вынуждена раскуривать какой-то косяк!"
    imgd 33191
    mt "И заниматься извращенскими гадостями!"
    mt "В трущобах!"
    mt "С этим жалким никчемным отбросом общества!"
    mt "За $ 10!"
    mt "!!!"
    $ menu_corruption = [0, monicaCitizens9CorruptionRequired2]
    menu:
        "Отказаться!":
            music Stealth_Groover
            imgf 33190
            m "Тебе нужно было место, чтобы курить!"
            m "Так что сиди и кури!"
            m "И больше не предлагай мне эти свои мерзкие гадости!"
            citizen14 "Ты мне портишь весь настрой!"
            imgd 33192
            citizen14 "Я, пожалуй, пойду найду корешей!"
            # он уходит
            imgf 33193
            mt "Да пошел ты!"
            mt "Грязный жалкий отброс общества! Фи!"
            mt "!!!"
            fadeblack
            sound snd_door_close1
            pause 2.0
            return -1
        "Видимо этот укуренный кретин не отстанет от меня...":
            $ monicaCitizens9Slums2 = day # Моника согласилась на минет и косяк
            pass
    # Моника зло на него смотрит
    music Hidden_Agenda
    imgf 33194
    mt "С другой стороны, в общей сложности я могу заработать $ 40..."
    mt "Об этом ведь никто не узнает..."
    mt "А мне нужны деньги..."
    imgd 33195
    m "За победу $ 100!"
    imgf 33196
    mt "Я не собираюсь курить это, а просто сделаю вид..."
    mt "Этот придурок ничего не поймет и накурится сам..."
    mt "В итоге, я одержу легкую победу и заработаю деньги!"
    imgd 33197
    mt "Черт!"
    mt "Но мне придется сделать это с ним... С его..."
    mt "Плевать! Я получу за это $ 100 и никто не узнает что здесь было!"
    mt "!!!"
    music Groove2_85
    imgf 33198
    m "Но сначала заплати мои $ 30 за аренду!"
    citizen9 "Ха! Договорились, дамочка!"
    citizen9 "Да хоть $ 110!"
    citizen9 "У тебя нет шансов, Найджел никогда не проигрывает дуэль на дури, хы-хы!"
    $ add_money(30.0)
    imgd 33199
    citizen9 "Повеселимся! Йоу!"
    imgf 33200
    w
    sound Jump2
    img 33201 hpunch
    citizen9 "Ты можешь приступать, дамочка..."
    # приспускает штаны
    # Моника с отвращением опускается на колени перед ним
    imgd 33202
    mt "Какой он отвратительный!"
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 33203
    w
    imgd 33204
    mt "Фу!!!"
    mt "!!!"
    $ menu_corruption = [0, monicaCitizens9CorruptionRequired3, 0]
    menu:
        "Начать делать минет (Extra version) (disabled)." if game.extra == False:
            pass
        "Начать делать минет." if game.extra == True:
            imgf 33205
            mt "Я делаю это только из-за $ 100!"
            mt "Жалкое, отвратительное существо!"
            imgd 33206
            mt "Но я получу с тебя свои деньги!"
            # Моника начинает делать минет
            imgf 33208
            w
            fadeblack 1.5
            music Loved_Up
            sound chpok6
            img 33209 vpunch
            w

            #1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Citizen9_Blowjob1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen9_Blowjob1_1= Movie(play="video/v_Monica_Citizen9_Blowjob1_1.mkv", fps=30)
            show videov_Monica_Citizen9_Blowjob1_1
            with fade
            citizen9 "Крууууть!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33207
            w

            #2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen9_Blowjob1_2= Movie(play="video/v_Monica_Citizen9_Blowjob1_2.mkv", fps=30)
            show videov_Monica_Citizen9_Blowjob1_2
            with fade
            citizen9 "Как дамочка охренительно умеет сосать!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33210
            w

            #3
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen9_Blowjob1_3= Movie(play="video/v_Monica_Citizen9_Blowjob1_3.mkv", fps=30)
            show videov_Monica_Citizen9_Blowjob1_3
            with fade
            citizen9 "Еееее..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33211
            w
            imgd 33212
            w

            #4
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen9_Blowjob1_4= Movie(play="video/v_Monica_Citizen9_Blowjob1_4.mkv", fps=30)
            show videov_Monica_Citizen9_Blowjob1_4
            with fade
            citizen9 "Каааайф!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # пока Моника делает минет, он подносит к своему лицу косяк и смотрит на него
            imgf 33213
            citizen9 "А Найджел пока попробует дурь..."
            citizen9 "Для разогрева перед нашим с тобой спором. Хы!"

            # 5
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen9_Blowjob1_5= Movie(play="video/v_Monica_Citizen9_Blowjob1_5.mkv", fps=30)
            show videov_Monica_Citizen9_Blowjob1_5
            with fade
            citizen9 "О, дааа!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33214
            w
            sound swish
            w

            #6
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen9_Blowjob1_6= Movie(play="video/v_Monica_Citizen9_Blowjob1_6.mkv", fps=30)
            show videov_Monica_Citizen9_Blowjob1_6
            with fade
            citizen9 "Сегодня у Найджела отличный день! Йоу!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33215
            w
            sound snd_sniff1
            w

            $ monicaMadeBlowjobNigel = True
            # Моника перестает сосать и смотрит на него
            pass
        "Попытаться тянуть время.":
            imgf 33205
            mt "Я не хочу этого делать."
            mt "Может быть, предложить ему что-то взамен."
            imgd 33206
            mt "Или сделать это просто руками..."
            imgf 33216
            citizen9 "Давай начинай..."
            # Моника не торопится делать минет, он подносит к своему лицу косяк и смотрит на него
            sound swish
            imgd 33213
            citizen9 "А Найджел пока попробует дурь..."
            citizen9 "Для разогрева перед нашим с тобой спором. Хы!"
            sound snd_sniff1
            imgf 33217
            w
            # Моника смотрит на него
            pass
    # Найджел с любовью смотрит на косяк в своей руке и понтуется перед Моникой
    music Marty_Gots_a_Plan
    imgd 33218
    citizen9 "Сейчас Найджел покажет, как нужно курить... Хы-хы!"
    citizen9 "Это отменная дурь!"
    imgf 33219
    sound snd_sniff1
    citizen9 "Я выкуриваю по 5 косяков в день, так что у дамочки сильный соперник!"
    citizen9 "Готовь свою киску, дамочка! Йоу!"
    # Найджел делает 1 тягу, у него глаза в кучу и он падает лицом вниз (!)
    $ blur_effect = 1
    imgd 33220
    citizen9 "Хыыыы..."
    $ blur_effect = 2
    sound Jump2
    img 33221 vpunch
    w
    sound snd_bodyfall
    img 33223 hpunch
    w
    $ blur_effect = 0
    imgd 33222
    w
    imgd 33224
    w
    # Найджел лежит со спущенными штанами и не шевелится
    # Моника склонилась на Найджелом
    # она тыкает его ногой
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 33225
    m "Эй!!!"
    m "Что за шутки?!"
    m "Вставай! Чего ты тут развалился?!"
    # Моника опять тыкает его ногой
    imgf 33226
    w
    sound Jump1
    imgd 33227
    w
    # она присаживается на корточки и машет рукой у него перед лицом
    imgf 33228
    m "Эй, ты живой?!"
    imgd 33229
    w
    sound Jump2
    img 33230
    w
    imgd 33229
    w
    sound Jump2
    img 33230
    w
    # Моника пугается
    imgd 33231
    mt "О Боже! Он не реагирует!"
    mt "Он что?"
    with hpunch
    mt "УМЕР?!"
    mt "?!?!?!"
    # вскакивает, мечется по квартире
    music Turbo_Tornado
    img 33232 vpunch
    mt "МОНИКА!!!"
    mt "У ТЕБЯ В КВАРТИРЕ ТРУП!!!"
    mt "ТРУП НАРКОМАНА!!!"
    sound highheels_run2
    imgd 33233
    mt "!!!"
    mt "ААААААА!!!"
    mt "Так! Спокойно, Моника!"
    # смотрит на тело
    imgd 33234
    mt "Спокойно!"
    mt "Нужно что-то сделать!"
    mt "Что?! Что делать?!"
    imgf 33235
    mt "Может быть обыскать его и забрать мои деньги?!"
    mt "Черт, я не могу забрать свои деньги у трупа!"
    mt "Или могу?"
    mt "Думай! Думай же!"
    img 33236 vpunch
    mt "!!!"
    mt "Точно!"
    mt "ПУЛЬС!!!"
    mt "Где щупают этот гребаный пульс?!"
    # Моника трясёт руками (как бы отряхивая их)
    # и прикладывает ладошки к щекам
    imgd 33237
    mt "Аааааа!!!"
    mt "По идее, если щупают, то это должно быть что-то выступающее, за что можно ущипнуть..."
    mt "Нос!"
    mt "Точно, так его и проверяют, этот пульс!"
    # хватает его за нос
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    imgf 33228
    w
    sound Jump2
    imgd 33238
    mt "Кажется ничего..."
    mt "У него нет пульса!!!"
    mt "!!!"
    music Pyro_Flow
    imgd 33239
    mt "ЭТОТ ПРИДУРОК СДОХ!"
    mt "В МОИХ АПАРТАМЕНТАХ!"
    mt "Я ЗА НИХ ПЛАЧУ! А ОН! ОН ТУТ СДОХ!!!"
    mt "СДОХ И ДАЖЕ НЕ ЗАПЛАТИЛ!"
    mt "КАКАЯ НАГЛОСТЬ И НЕВОСПИТАННОСТЬ!"
    imgd 33240
    mt "Черт! Черт! ЧЕРТ!!!"
    mt "Что же делать?!"
    mt "?!"
    mt "?!?!"
    mt "?!?!?!"
    imgf 33241
    mt "Черт! Мне нужна помощь!"
    mt "Нужно вызвать полицию..."
    mt "Нет, только не полицию, черт!"
    # Моника В ПАНИКЕ ВЫБЕГАЕТ НА УЛИЦУ
    sound highheels_run2
    imgd 33242
    w
    fadeblack
    sound highheels_run2
    sound2 snd_door_close1
    pause 2.0
    # видит Фила, который спас ее от насильника
    music Turbo_Tornado
    imgf 33399
    w
    imgd 33400
    mt "Точно!"
    mt "Он поможет!"
    mt "Он уже спасал меня!"
    mt "!!!"
    # Моника подбегает к своему спасителю, хватает его за руку и тянет к себе в кв
    sound highheels_run2
    imgf 33401
    m "М-м-мистер!"
    m "!!!"
    m "Мистер, вы можете пойти со мной?!"
    m "В мои апартаменты?!"
    m "Мне очень нужно, что бы вы пошли со мной, мистер!"
    imgd 33402
    citizen6 "Ооо, милочка!" # спаситель с хитрой ухмылкой
    citizen6 "Тебе так приспичило? Хе-хе!"
    citizen6 "Ну пошли..."
    # затемнение, спустя некоторое время
    # апартаменты Моники
    # Моника и Фил в апартаментах
    # Фил заходит в кв Моники и спотыкается о Найджела
    fadeblack
    sound highheels_run2
    pause 2.0
    sound snd_door_open1
    pause 1.5
    music Groove2_85
    imgfl 33243
    w
    imgf 33244
    w
    imgd 33247
    w
    sound snd_bodyfall
    img 33245 hpunch
    w
    imgd 33246
    citizen6 "Эй, милочка, да у тебя тут мужик посреди комнаты валяется!"
    citizen6 "Без штанов! Хе-хе!"
    citizen6 "Кажется, твой клиент еще не ушел!"
    # Моника в панике
    fadeblack 2.0
    music Hidden_Agenda
    imgf 33248
    m "Кажется... Кажется, он не может уйти!"
    m "Поэтому мне и нужна ваша помощь!"
    m "Он... Он! Он, кажется, не дышит!!!"
    # Фил удивленно смотрит на Монику, потом на тело
    music Groove2_85
    imgd 33249
    w
    imgf 33250
    citizen6 "В смысле, не дышит?"
    citizen6 "Ты досмерти затрахала клиента, милочка?"
#    music Hidden_Agenda
    imgd 33251
    m "Я... Я не... Я не уверена..."
    m "То есть нет!"
    m "Я ничего такого не делала!"
    m "Он просто упал!"
    m "Это не из-за меня!"
    imgd 33252
    citizen6 "Ну помер значит."
    citizen6 "Зови копов. Зачем меня притащила?"
    # у Моники снова паника
    music Power_Bots_Loop
    img 33253 vpunch
    m "НЕТ! НЕТ!"
    m "Я НЕ МОГУ КОПОВ!!!"
    m "НЕЛЬЗЯ КОПОВ!!!"
    imgd 33254
    m "Я сделаю все, что захотите!"
    m "Только помогите мне от него избавиться!"
    m "Не надо копов!!!"
    # Фил подходит к Найджелу и тыкает в него ногой, и ухмыляется
    music Groove2_85
    imgf 33255
    citizen6 "Все, что захочу, говоришь..." # Фил глядя на Найджела
    imgd 33256
    w
    sound Jump2
    img 33257
    w
    music Turbo_Tornado
    imgf 33258
    citizen6 "Так с этого и нужно было начинать! Хе-хе!" # Фил радостно разводит руками
    citizen6 "Ничего сложного. В нашем районе это дело обычное!"
    citizen6 "Отвезем твоего жмурика на какую-нибудь свиноферму и дело с концом!"
    citizen6 "Ты не знаешь какого-нибудь фермера, у которого есть дюжина свиней?"
    # Моника в шоке
    imgd 33259
    mt "Что он несет? Свиноферма?"
    mt "Что он имеет ввиду?"
    img 33260
    m "Нет!"
    citizen6 "Или можем его... Ну того..." # делает жест рукой, как-будто пилит
    imgf 33261
    w
    sound vjuh3
    imgd 33262
    w
    sound vjuh3
    imgd 33261
    w
    sound vjuh3
    imgd 33262
    citizen6 "На кусочки..."
    imgd 33263
    m "Мне плевать, как!"
    m "Только убери его и все!"
    m "Мне не нужны эти проблемы!"
    imgf 33264
    citizen6 "Не переживай, милочка. Все сделаем."
    music Hidden_Agenda
    citizen6 "А сейчас давай перейдем к награде. Хе-хе!"
    imgd 33265
    citizen6 "Можешь сейчас же отблагодарить меня своей киской."
    citizen6 "Дело-то рисковое!"
    citizen6 "Поэтому сначала награда, потом я займусь трупом!"
    mt "Черт!"
    mt "!!!"
    $ menu_corruption = [0, monicaCitizens9CorruptionRequired4]
    menu:
        "Предложить косяк Найджела в качестве оплаты":
            $ monicaCitizens9Slums3 = day # Моника предложила Филу косяк Найджела
            music Pyro_Flow
            imgf 33266
            mt "Очередной извращенец!"
            mt "Здесь хоть кто-то делает хоть что-нибудь просто так?!"
            mt "У меня стресс!!!"
            mt "А он требует ЭТОГО!"
            mt "!!!"
            imgd 33267
            mt "Может, предложить ему ту гадость, что притащил сюда этот дохлый придурок!?"
            # смена кадра, гостиная Фил со спущенными штанами и полустояком
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 33268
            w
            imgf 33269
            citizen6 "Ну же, милочка!"
            citizen6 "Я уже готов принять твою благодарность! Хе-хе!"
            citizen6 "Иди скорей ко мне!"
            music Hidden_Agenda
            imgd 33270
            m "Я... Я немного напряжена."
            m "Давай сначала расслабимся?"
            m "Как смотришь на то, чтобы сначала покурить?"
            music Groove2_85
            imgd 33271
            citizen6 "Меня устраивает и мой вариант!"
            citizen6 "Или ты хочешь обмануть меня?"
            citizen6 "Хочешь, что бы я сделал за тебя всю грязную работу..."
            citizen6 "А потом кинешь, не поблагодарив?!"
            imgd 33272
            citizen6 "Нееет, так дело не пойдет!"
            citizen6 "Я ухожу и сама возись со своим жмуриком!"
            # Моника останавливает его
            sound Jump2
            img 33273
            m "Я могу предложить тебе кое-что получше!"
            m "!!!"
            # Моника указывает на косяк Найджела, который лежит на полу
            music Hidden_Agenda
            imgd 33274
            m "Это... Это... Как он там называется?"
            m "Это отменный жирный косяк! Вот!"
            m "Это будет лучшей благодарностью!"
            # Фил подозрительно
            imgf 33275
            citizen6 "Хмм..."
            citizen6 "А почему он тогда валяется на полу?"
            # Моника раздрожительно
            m "От того, что он лежит на полу, он хуже не становится!"
            citizen6 "Но я уже настроился на благодарность от твоей киски..."
            imgd 33271
            citizen6 "И мой дружок в боевой готовности!"
            citizen6 "Смотри, какой он твердый!"
            # гостиная Фил со спущенными штанами и стояком
            imgf 33276
            m "Это отличный косяк!"
            m "Отменное предложение!!!"
            m "!!!"
            music Groove2_85
            imgd 33267
            citizen6 "Отменное предложение, говоришь?.."
            # Фил берет косяк с пола
            sound vjuh3
            img 33277
            citizen6 "Окей... Я должен это проверить!"
            sound snd_sniff1
            imgf 33278
            w
            $ blur_effect = 2
            imgd 33279
            w
            $ blur_effect = 0
            sound snd_bodyfall
            img 33280 hpunch
            w
            # затягивается и отрубается падая на Найджела
            pass

        "Согласиться на секс в качестве оплаты за помощь":
            $ monicaCitizens9Slums4 = day # Моника согласилась на секс с Филом
            music Pyro_Flow
            imgf 33266
            mt "Он пользуется моим положением!"
            mt "Но я без него не справлюсь!"
            mt "Я ведь даже не знаю, что мне делать с телом!"
            mt "А если откажусь, он не будет мне помогать!"
            imgd 33332
            mt "Или еще хуже - сдаст полиции!!!"
            mt "Я не могу снова попасть в эту ужасную камеру!"
            mt "И к Маркусу!!!"
            mt "!!!"
            imgd 33331
            mt "Приспичило же этому никчемному идиоту сдохнуть здесь!"
            mt "В моих апартаментах!!!"
            mt "Развалился тут, а мне теперь решать эту проблему!!!"
            imgf 33268
            w
            imgd 33269
            m "..."
            m "Ты собираешься заниматься этим, пока он лежит тут?!" # МОника указывая на Найджела
            music Groove2_85
            citizen6 "Ну да, а что?"
            citizen6 "Ему уже все равно, а я уже давно хочу попробовать твою киску! Хе-хе!"
            # Моника в шоке
            img 33270
            mt "!!!"
            citizen6 "Ну ж, милочка! Я уже готов принять твою благодарность!"
            # Фил достает член наружу
            citizen6 "Только для начала освежи мой член своим ротиком."
            music Power_Bots_Loop
            img 33333
            mt "Фууу!!!"
            mt "Какая мерзость!!!"
            mt "Он хочет, чтобы я засунула его грязный член себе в рот?!"
            mt "!!!"
            music Groove2_85
            imgf 33334
            citizen6 "Иди скорей ко мне!"
            menu:
                "Сделать минет Филу.":
                    pass
            # Моника встает на колени
            # Фил резко засовывает свой член Монике в рот
            $ add_corruption(10, "ep217_nigel2")
            fadeblack
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            imgf 33335
            m "А ты точно мне поможешь?"
            citizen6 "Конечно, помогу! Только сначала благодарность!"
            fadeblack 1.5
            sound Jump2
            img 33336 vpunch
            m "!!!"
            music Loved_Up
            imgd 33337
            w

            #1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Citizen6_Blowjob1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_1= Movie(play="video/v_Monica_Citizen6_Blowjob1_1.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_1
            with fade
            citizen6 "Дааа! Как офигенно!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33338
            w

            #2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_2= Movie(play="video/v_Monica_Citizen6_Blowjob1_2.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_2
            with fade
            citizen6 "Глубже! Ааааа... Да!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # кадр на Найджела, на него никто не смотрит и не видит, что он жив
            # он открывает глаза, лежа на полу, голова вниз
            # Смотрит в пол глазами в упор
            imgf 33339
            w
            music Marty_Gots_a_Plan
            imgd 33293
            citizen9_t "Вот меня вштырило! Йоу!"
            citizen9_t "Вот это дурь!"
            citizen9_t "Что это у меня перед глазами?"
            $ blur_effect = 1
            w
            $ blur_effect = 0

            music Loved_Up
            #3
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_3= Movie(play="video/v_Monica_Citizen6_Blowjob1_3.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_3
            with fade
            citizen6 "Оооо!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")




            # кадр на Монику и Фила
            # Моника делает минет упираясь руками (отталкивая Фила)
            music Loved_Up2
            imgf 33340
            citizen6 "Оооо! Даааа!"
            imgd 33341
            citizen6 "Хорошая сделка!"
            #4
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_4= Movie(play="video/v_Monica_Citizen6_Blowjob1_4.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_4
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33342
            citizen6 "Постарайся, милочка, чтобы я не передумал тебе помогать!"
            imgd 33343
            citizen6 "Даааа!"

            $ blur_effect = 2
            imgd 33292
            w
            $ blur_effect = 0
            with diss
            citizen9_t "Какие-то полосы..."
            citizen9_t "Черная... Коричневая..."

            #5
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_5= Movie(play="video/v_Monica_Citizen6_Blowjob1_5.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_5
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33345
            citizen6 "Давай, бери его глубже!"

            imgd 33346
            citizen6 "Я помогу тебе!"

            #6
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_6= Movie(play="video/v_Monica_Citizen6_Blowjob1_6.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_6
            with fade
            citizen6 "Вот так! Дааа!"
            with hpunch
            m "!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33344
            citizen6 "Ммммм..."

            #7
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_7= Movie(play="video/v_Monica_Citizen6_Blowjob1_7.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_7
            with fade
            citizen6 "Еще глубже! Мммм..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33292
            citizen9_t "Еще какие-то паутинки..."
            $ blur_effect = 2
            with diss
            citizen9_t "Это такой глюк?"
            citizen9_t "Круто! Ееееее!!!"
            $ blur_effect = 0

            imgd 33347
            citizen6 "ДАААА!"
            citizen6 "Какая ты усердная!"
            citizen6 "Тебе, похоже, и самой нравится это!"

            #8
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Blowjob1_8= Movie(play="video/v_Monica_Citizen6_Blowjob1_8.mkv", fps=30)
            show videov_Monica_Citizen6_Blowjob1_8
            with fade
            citizen6 "ДАААА!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            menu:
                "Кончить в рот Моники.":
                    $ ep217_dialogues4_citizens_cumzone = 1
                    # кончает Монике в рот
                    imgf 33348
                    w
                    img 33349
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    citizen6 "МММММ!"
                    img 33350
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen6 "ОООО..."
                    imgf 33351
                    citizen6 "ДАААААА!!!"
                    # Моника зло смотрит на него
                    mt "Мерзавец!"
                    mt "!!!"
                    pass
                "Кончить на лицо Моники.":
                    $ ep217_dialogues4_citizens_cumzone = 2
                    # кончает Монике на лицо
                    imgf 33348
                    w
                    img 33349
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    citizen6 "АААААААА!!!"
                    img 33352
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen6 "КОООНЧААААЮ!!!"
                    imgf 33353
                    citizen6 "АААА..."
                    # Моника зло смотрит на него
                    mt "ФУУУ!!!"
                    mt "МЕРЗКОЕ ЖИВОТНОЕ!"
                    mt "!!!"
                    pass
                "Кончить на грудь Моники.":
                    $ ep217_dialogues4_citizens_cumzone = 3
                    # кончает Монике на грудь
                    imgf 33348
                    w
                    img 33349
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    citizen6 "АААААААА!!!"
                    img 33354
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen6 "ГОТОВЬ СИСЬКИ, ШЛЮХА!!!"
                    imgf 33355
                    citizen6 "ДАААА..."
                    # Моника зло смотрит на него
                    mt "МЕРЗАВЕЦ!!!"
                    mt "ЖИВОТНОЕ!"
                    mt "!!!"
                    pass
            # затемнение, Фил со спущенными штанами, Моника стоит злая
            fadeblack 2.0
            music Groove2_85
            imgfl 33356
            w
            imgf 33357
            m "Все! Теперь убери отсюда ЭТО!" # Моника указывает на Найджела
            citizen6 "Подожди! Ты только освежила мой член!"
            citizen6 "Я сказал, что ты отблагодаришь меня СВОЕЙ КИСКОЙ!"
            citizen6 "Так что, теперь принимайся за дело!"
            citizen6 "Отблагодари меня и я тебе помогу с твоим жмуриком!"
            music Power_Bots_Loop
            img 33259
            mt "МЕРЗКОЕ ЖИВОТНОЕ!"
            mt "Грязный извращенец!"
            mt "Пользуется тем, что мне нужна его помощь!"
            mt "!!!"
            music Groove2_85
            imgf 33269
            citizen6 "Ты чего?!"
            citizen6 "Засмотрелась на мой член?"
            citizen6 "Я смотрю, он тебе понравился..."
            citizen6 "Давай скорей уже! Не терпится засунуть его в тебя!"
            imgd 33333
            mt "Черт!"
            mt "Если я ему откажу, он уйдет!"
            mt "А сама я ничего не смогу сделать с этим телом!!!"
            mt "!!!"
            menu:
                "Идти к кровати.":
                    pass
            music Pyro_Flow
            imgd 33358
            mt "Твою мать!"
            mt "Грязный мешок с дерьмом!"
            mt "Пользуется тем, что леди попала в непростую ситуацию!"
            mt "Чертов шантажист!!!"
            imgf 33359
            m "Только быстро!"
            m "!!!"
            # Моника зло смотрит на Фила и встает на четвереньки на кровать
            # попа отклячена в сторону Найджела (ни она, ни Фил его не видят во время секса)
            fadeblack
            sound highheels_short_walk
            pause 1.5
            sound snd_fabric1
            pause 2.0
            music Loved_Up
            imgfl 33360
            w
            imgf 33362
            w
            imgd 33363
            w
            imgf 33361
            citizen6 "Хе-хе!"
            # он подходит и пристраивается к ней сзади
            imgd 33364
            w
            imgf 33365
            citizen6 "Попроси у меня разрешения засунуть мой огромный член в себя!"
            music stop
            sound plastinka1b
            with vpunch
            # Моника недоумевает
            m "Что?!"
            m "Что ты вообще несешь?!"
            music Groove2_85
            citizen6 "Ты хочешь, чтобы я тебе помогал или нет?"
            citizen6 "Я могу уйти и сама будешь прятать своего жмурика!"
            # Моника зло
            imgd 33366
            m "Ты что, собираешь делать это прямо над трупом?!"
            m "Может быть ты сначала уберешь отсюда это?!"
            citizen6 "Само это отсюда не уберется..."
            citizen6 "Только с моей помощью, милочка."
            citizen6 "Благодари меня скорее..."
            imgd 33367
            citizen6 "И Фил тебе поможет."
            citizen6 "Давай, проси разрешения у Фила вставить в тебя член!"
            music Power_Bots_Loop
            img 33368
            mt "Извращенец!"
            mt "Ненавижу!!!"
            mt "!!!"
            music Groove2_85
            imgf 33369
            m "Я..."
            m "Могу..."
            m "Могу я засунуть твой большой член в себя?!"
            citizen6 "Тебе так не терпится, милочка? Хе-хе!"
            citizen6 "Дааа... Засунь его в себя, только меееедленно!"
            # сцена секса с Филом
            menu:
                "Вставить член Фила в киску.":
                    pass
            # Моника берет в руку его член и вставляет в себя
            $ add_corruption(20, "ep217_nigel3")
            fadeblack 1.5
            music Loved_Up
            imgf 33370
            citizen6 "Дааа, милочка!"
            imgd 33371
            w
            sound chpok6
            img 33372 hpunch
            citizen6 "Какая же ты горячая!"
            # Фил начинает двигаться в Монике
            sound snd_monica_ahh
            img 33373 vpunch
            w

            #1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Citizen6_Sex1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_1= Movie(play="video/v_Monica_Citizen6_Sex1_1.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_1
            with fade
            citizen6 "Оооох... Круто!"
            m "!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33374
            citizen6 "Аааа... Да-да!"

            #2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_2= Movie(play="video/v_Monica_Citizen6_Sex1_2.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_2
            with fade
            citizen6 "Какая горячая киска! Аааа!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgf 33375
            w

            #3
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_3= Movie(play="video/v_Monica_Citizen6_Sex1_3.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_3
            with fade
            citizen6 "Как у тебя тепло и узко внутри!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33376
            w

            #4
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_4= Movie(play="video/v_Monica_Citizen6_Sex1_4.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_4
            with fade
            citizen6 "Ммммммм...."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Фил жарит Монику, стоят задом к Найджелу, не видят его
            # Найджел снова открывает глаза и рассматривает пол
            imgd 33377
            w

            #5
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_5= Movie(play="video/v_Monica_Citizen6_Sex1_5.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_5
            with fade
            citizen6 "Оооо!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            #
            fadeblack 1.5
            music Marty_Gots_a_Plan
            imgf 33293
            w
            $ blur_effect = 1
            with diss
            w
            imgd 33292
            citizen9_t "Коричневая... Черная..."
            citizen9_t "Круууууть!"
            # на фоне слышит
            $ blur_effect = 0
            with diss
            w


            imgf 33378
            citizen6 "Оооох... Даааа!!!"
            citizen6 "Какая кискаааа!!!"
            $ blur_effect = 2
            with diss
            citizen9_t "Ни хрена себе меня вштырило!"
            citizen9_t "В этом глюке кто-то шпилится! Еееее!!"
            citizen9_t "Вот это дурь!!!"
            $ blur_effect = 0
            with diss
            w

            # снова на фоне
            imgd 33379
            w

            citizen6 "Аааа!!!"
            citizen6 "Я скоро кончууу!!"

            citizen6 "Мммм..."
            citizen9_t "???"

            fadeblack 1.5
            music Loved_Up2
            #6
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_6= Movie(play="video/v_Monica_Citizen6_Sex1_6.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_6
            with fade
            citizen6 "Еще немного! Аааа!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")


            # Найджел поворачавает голову в бок и смотрит на голый зал Фила, который шпилит Монику
            fadeblack 1.5
            music Marty_Gots_a_Plan
            $ blur_effect = 0
            imgd 33380
            w
            sound Jump1
            imgd 33413
            w
            $ blur_effect = 2
            with diss
            citizen9_t "Это кто?"
            citizen9_t "Где я?"
            $ blur_effect = 0
            fadeblack 1.5

            music Loved_Up2
            #7
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_7= Movie(play="video/v_Monica_Citizen6_Sex1_7.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_7
            with fade
            citizen6 "О, как же здорово! Да!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # поднимается сначала на четвереньках, потом еле встает
            # Найджел стоит сзади и смотрит на то, как Фил жарит Монику
            # с интересом и не понимая
            fadeblack 1.5
            music Marty_Gots_a_Plan
            $ blur_effect = 1
            imgd 33381
            w
            $ blur_effect = 0
            with diss
            w
            imgf 33382
            w
            $ blur_effect = 2
            with diss
            w
            imgd 33383
            citizen9_t "Это что, не глюк?"
            $ blur_effect = 0
            with diss
            citizen9_t "Кто это тут трахается?"
            citizen9_t "Или меня еще не отпустило?"
            $ blur_effect = 0
            # Фил продолжает двигаться в Монике
            music Loved_up2
            #8
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_8= Movie(play="video/v_Monica_Citizen6_Sex1_8.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_8
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 33384
            w
            imgd 33385
            w
            #

            imgf 33386
            citizen6 "Тебе нравится благодарить Фила за помощь, да?!"

            #9
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_9= Movie(play="video/v_Monica_Citizen6_Sex1_9.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_9
            with fade
            citizen6 "Ты только поэтому попадаешь во всякие передряги?!"
            citizen6 "Все лишь для того, чтобы Фил трахнул тебя!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 33368
            mt "Что этот придурок вообще несет?!"

            imgf 33387
            mt "Недоумок!"
            mt "!!!"

            #10
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_10= Movie(play="video/v_Monica_Citizen6_Sex1_10.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_10
            with fade
            citizen6 "Дааааа!"
            citizen6 "Аааа!"
            citizen6 "Давай скажи, что хочешь, чтобы я в тебя кончил!"
            m "ЧТО?!"
            m "НЕТ!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 33388
            citizen6 "Ну же!"
            citizen6 "Или я уйду!!!"
            img 33389
            m "!!!"

            #11
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen6_Sex1_11= Movie(play="video/v_Monica_Citizen6_Sex1_11.mkv", fps=30)
            show videov_Monica_Citizen6_Sex1_11
            with fade
            mt "Чертов извращенец!"
            mt "!!!"
            m "Кончи в... В меня..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # он кончает в Монику
            img 33390
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            citizen6 "КОНЧААААЮ!!!"
            img 33392
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan8
            citizen6 "ДААААААА!!!"
            imgf 33391
            citizen6 "АААААААА!!!"
            # сразу после того, как он кончил
            # Найджел подает голос, стоит на том же месте
            music Marty_Gots_a_Plan
            imgd 33393
            citizen9 "Йоу! Круто вы жаритесь!"
            citizen9 "А как же я?"
            music stop
            sound plastinka1b
            citizen9 "Давай, чувак, отходи!"
            citizen9 "Теперь очередь Найджела оттрахать эту дамочку!"
            # Моника в шоке соскакивает с кровати
            fadeblack 0.5
            music Power_Bots_Loop
            img 33394 hpunch
            m "ТЫ ЧТО?!"
            m "ЖИВ?!"
            # Фил начинает ржать
            music Groove2_85
            citizen6 "Аха-ха-ха!!!"
            sound male_laugh4
            citizen6 "А твой жмурик то не совсем дохлым оказался, милочка!"
            music Marty_Gots_a_Plan
            citizen9 "Ээээй! Кто дохлый?!"
            citizen9 "Вы еще не знаете Найджела!"
            imgd 33395
            citizen9 "Найджел лучший в дуэли по дури! Еееее!!!"
            citizen9 "Поняла, дамочка?"
            citizen9 "Давай свою киску сюда!"
            citizen9 "Ты мне проспорила!"
            # Монику бомбит
            music Pyro_Flow
            img 33396 hpunch
            m "ЧТООО?!"
            m "Я ПРОСПОРИЛА?!"
            # Моника начинает орать сначала на Найджела, потом на Фила
            imgd 33397
            m "ТЫ!!!"
            m "Никчемное грязное животное!"
            m "Пошел вон отсюда, урод!"
            sound male_laugh4
            citizen6 "Аха-ха!"
            img 33398
            m "Ничего смешного!!!"
            m "Выметайся отсюда!!!"
            m "Пошли вон! Оба!!!"
            citizen6 "Милочка отблагодарила Фила, а жмурик живой!"
            sound male_laugh4
            citizen6 "Хорошо, что фермера искать не пошла!"
            citizen6 "Аха-ха!"
            m "ЗАТКНИСЬ!!!"
            # Моника выталкивает их из апартаментов, возможно дает поджопники обоим
            ## возможно через затемнение - чтобы они оделись
            fadeblack 0.5
            music Power_Bots_Loop
            imgf 33329
            m "ПОШЛИ!"
            m "ОТСЮДА!"
            img 33330 hpunch
            m "ВООООН!!!"
            # остается одна
            fadeblack
            sound snd_door_close1
            pause 1.5
            music Pyro_Flow
            imgf 31806
            mt "Это какой-то кошмар!"
            mt "Как ты могла попасть в такую ужасную ситуацию, Моника?!"
            mt "!!!"
            imgd 33193
            mt "Я сойду с ума с этими бесполезными грязными отбросами!"
            mt "До чего же они все безмозглые!"
            mt "Никому не нужные!"
            mt "Никчемные!"
            mt "!!!"
            return 1
    # Моника офигевшая и в еще большей панике
    music Turbo_Tornado
    img 33281 vpunch
    m "ААААААААА!!!"
    m "НЕЕЕТ!!!"
    m "!!!"
    m "БЕЗМОЗГЛЫЙ КРЕТИН!!!"
    # Моника пинает Фила и Найджела
    imgf 33282
    sound highheels_run2
    w
    imgd 33283
    w
    sound Jump2
    img 33284
    m "ЭЙ, ВСТАВАЙТЕ!!!"
    imgd 33283
    w
    sound Jump2
    img 33285
    m "ХВАТИТ ДОХНУТЬ В МОИХ АПАРТАМЕНТАХ!!!"
    # садится на кровать перед ними и хватается в ужасе за голову
    fadeblack
    sound highheels_run2
    pause 2.0
    music Stealth_Groover
    imgf 33286
    w
    imgd 33287
    mt "Что мне теперь делать с ними?!"
    mt "Мне срочно нужен фермер со свиньями!!!"
    mt "Но где такого найти?!"
    mt "Он же не разгуливает по улицам с вывеской 'фермер со свиньями'!!!"
    imgd 33288
    mt "Может, надо их оттащить в ванную?!"
    mt "И там их... На куски!"
    mt "А потом выбросить в мусорку!!!"
    mt "Или лучше найти фермера?!"
    mt "Что делать?!"
    mt "!!!"
    imgd 33289
    mt "А может Джек знает, где свиноферма?!"
    mt "Нет! Это будет подозрительно!"
    mt "Он сразу догадается, что я хочу от кого-то избавиться!"
    mt "!!!"
    sound highheels_short_walk
    imgf 33290
    mt "Я просто уйду отсюда!"
    mt "К черту эту вонючую дыру!"
    mt "Да! Скажу Джеку, что ухожу!"
    mt "Это его проблемы, что делать с этими двумя!"
    mt "Ведь это его апартаменты!"
    # Показываем тела
    imgd 33291
    mt "Скажу, что пришла и увидела двух голых мужиков..."
    mt "Которые лежат друг на друге..."
    mt "Скорее всего, они пробрались сюда и хотели чем-то заняться, но что-то пошло не так..."
    mt "Да, точно!"
    mt "!!!"
    # пока Моника сидит в раздумьях, Найджел очухивается
    music Marty_Gots_a_Plan
    $ blur_effect = 1
    imgf 33292
    w
    imgd 33293
    w
    $ blur_effect = 2
    imgf 33294
    citizen9 "Эй, кореш!"
    citizen9 "Эй! Ты меня придавил!"
    # пытается столкнуть с себя Фила
    $ blur_effect = 0
    imgd 33295
    citizen9 "Слезай с меня!"
    imgf 33294
    citizen9 "Я не могу дышать!"
    # Моника в шоке смотрит на него
    music stop
    sound plastinka1b
    img 33296 vpunch
    mt "ОЖИЛ?!"
    mt "?!"
    mt "ОН ОЖИЛ!!!"
    mt "!!!"
    # Найджел скидывает с себя Фила, отталкивая, тот скатывается с Найджела, лежит в отключке на спине, член торчит
    # Найджел садится на полу
    sound snd_bodyfall
    img 33297 hpunch
    w
    music Marty_Gots_a_Plan
    imgf 33298
    citizen9 "Ох, нихрена себе!"
    citizen9 "Вот это убойная дурь!"
    citizen9 "Вот это меня вырубило! Йоу!"
    # Найджел смотрит на косяк, потом на Фила, потом встает
    imgd 33299
    w
    imgf 33300
    w
    # Моника продолжает в шоке смотреть на него, он у нее спрашивает
    imgd 33301
    citizen9 "А это что за чувак?"
    citizen9 "Или это не чувак..."
    citizen9 "А мой косяяяк..."
    citizen9 "Вот это дууууурь!!! Еееее!!!"
    music Pyro_Flow
    m "Ты что, совсем все мозги прокурил?"
    m "Это не косяк!"
    # он непонимающе смотрит на нее
    imgd 33302
    citizen9 "Не косяк?!"
    m "Это... Это..."
    m "Да неважно, кто это!!!"
    img 33303
    mt "Черт!"
    mt "Не говорить же ему, что это тот..."
    mt "Кто должен был избавиться от его тела!"
    music Marty_Gots_a_Plan
    imgf 33304
    citizen9 "Это твой кореш что-ли, дамочка?"
    citizen9 "Йоу! Я понял!"
    citizen9 "Ты его вырубила!!!"
    citizen9 "Чтоб он не забрал косяк Найджела! Ееее!!"
    music Pyro_Flow
    img 33259
    mt "Придурок!!!"
    mt "!!!"
    # переводит взгляд на Фила
    imgf 33305
    mt "И что, теперь этот никчемный неудачник умер?!"
    mt "Черт!!!"
    mt "Что делать?!"
    mt "..."
    music Hidden_Agenda
    imgd 33306
    mt "Мне что, просить этого укуренного придурка избавиться теперь от него?!"
    mt "Может у него есть знакомый фермер, который держит свиней?"
    mt "Или распилить его..."
    mt "Этот укуренный придурок все равно подумает, что это глюк..."
    mt "..."
    # переводит взгляд на Найджела
    imgf 33307
    mt "Хотя..."
    mt "Этот кретин ведь живой..."
    # переводит взгляд на Фила
    imgd 33306
    mt "Может быть, и этот..."
    mt "..."
    # Монику озаряет мысль и она вскакивает
    music stop
    sound plastinka1b
    img 33308 hpunch
    mt "Член!"
    mt "У него стоит член!"
    music Groove2_85
    mt "Этот урод жив!!!"
    # подбегает к Филу
    sound highheels_short_walk
    imgd 33309
    mt "!!!"
    $ menu_corruption = [0, monicaCitizens9CorruptionRequired5]
    menu:
        "Наступить каблуком на его член!":
            # Моника злобно смотрит на него, заносит над ним ногу и придавливает каблуком его член
            # Фил начинает орать
            music Stealth_Groover
            imgf 33318
            w
            imgd 33319
            w
            imgd 33310
            call bitch(10, "ep217_nigel_heel") from _rcall_bitch_21
            m "Хватит здесь валяться посреди моего дома!"
            sound Jump2
            img 33311 hpunch
            sound scream_steve3
            citizen6 "АААА!!!"
            citizen6 "Твою мать!!!"
            citizen6 "Мой член!!!"
            citizen6 "ААААААА!!!!"
            # Монику убирает ногу
            # Фил вскакивает, хватается за член и убегает из апартаментов
            fadeblack 2.0
            music Pyro_Flow
            imgf 33312
            sound scream_steve3
            citizen6 "ААААААА!!!"
            imgd 33313
            w
            fadeblack
            sound running
            pause 2.0
            sound snd_door_close1
            pause 2.0
            music Pyro_Flow
            # Моника поворачивается и злобно смотрит на Найджела
            img 33314 hpunch
            m "ТЫ!!!"
            m "Никчемное грязное животное!"
            m "Пошел вон отсюда, урод!"
            m "Выметайся отсюда!!!"
            imgd 33315
            citizen9 "Йоу! Дамочка!!!"
            citizen9 "Мы же с тобой кореша теперь!"
            citizen9 "Ты чего?!"
            m "ЗАТКНИСЬ!!!"
            # Моника выталкивает его из апартаментов, дает поджопник
            sound snd_kick_fred1
            img 33316 vpunch
            w
            img 33317
            m "ПОШЕЛ!"
            m "ОТСЮДА!"
            m "ВООООН!!!"
            fadeblack
            sound running
            pause 2.0
            sound snd_door_close1
            pause 2.0
            pass
        "Схватить рукой!":
            # Моника хватает рукой за его член
            music Groove2_85
            imgf 33320
            w
            sound Jump2
            imgd 33321
            $ add_corruption(10, "ep217_nigel1")
            mt "Фу! Грязный вонючий отросток!"
            mt "!!!"
            # Фил очухивается
            $ blur_effect = 1
            imgf 33322
            citizen6 "Ох..."
            citizen6 "Что это было?"
            citizen6 "Где я?"
            # оглядывается, смотрит на Монику, потом на ее руку на члене
            $ blur_effect = 0
            imgd 33323
            w
            img 33324
            citizen6 "Аааа, милочка!"
            citizen6 "Ты решила поиграть с моим дружком..."
            # Моника одергивает руку
            sound Jump2
            img 33325 vpunch
            w
            imgd 33326
            citizen6 "Давай, продолжай..."
            citizen6 "Верни свою руку на место..."
            # Моника встает и начинает орать сначала на Найджела и Фила
            music Pyro_Flow
            imgf 33327
            m "ВЫ!!!"
            m "Никчемные грязные животные!"
            m "Пошли вон отсюда!"
            citizen6 "Эй! Все же было хорошо!"
            citizen6 "Ты чего разоралась, милочка?!"
            imgd 33328
            m "Ничего хорошего!!!"
            m "Выметайся отсюда!!!"
            m "Пошли вон! Оба!!!"
            # Моника выталкивает их из апартаментов, возможно дает поджопники обоим
            fadeblack 0.5
            music Power_Bots_Loop
            img 33329 hpunch
            m "ПОШЛИ!"
            m "ОТСЮДА!"
            img 33330
            m "ВООООН!!!"
            fadeblack
            sound running
            pause 2.0
            sound snd_door_close1
            pause 2.0
            pass
    # остается одна
    music Pyro_Flow
    imgf 31806
    mt "Это какой-то кошмар!"
    mt "Как ты могла попасть в такую ужасную ситуацию, Моника?!"
    mt "!!!"
    imgd 33193
    mt "Я сойду с ума с этими бесполезными грязными отбросами!"
    mt "До чего же они все безмозглые!"
    mt "Никому не нужные!"
    mt "Никчемные!"
    mt "!!!"
    return 2

label ep217_dialogues4_citizens_1b:
    mt "Придурок!!!"
    return

# при клике на азиата у ресторана (Akira San)
label ep217_dialogues4_citizens_2:
    music Groove2_85
    imgr Dial_Citizen_5_3
    citizen5 "О, манящие груди!"
    citizen5 "Мистер знал, что вы скоро придете!"
    citizen5 "Потому что Мистер кое-что знает о вас!"
    imgl Dial_begin35_24
    mt "Он что-то знает обо мне?!"
    mt "Может он где-то видел мое фото?!"
    mt "Я должна выяснить, что ему известно..."
    imgl Dial_begin35_22
    m "Что вы знаете?"
    imgr Dial_Citizen_5_2
    imgl Dial_begin35_23
    citizen5 "Я знать. что это тайна!"
    citizen5 "Я рассказать тебе это в тайном месте для танцев."
    m "..."
    menu:
        "Пойти с ним.":
            imgl Dial_begin35_21
            mt "Я должна пойти с ним, что бы все выяснить!"
            mt "Что еще за тайны?"
            mt "Вдруг он что-то знает обо мне?"
            mt "Этого еще не хватало!"
            m "Ну пошли..."
            # затемнение
            pass
        "Нет!":
            music Stealth_Groover
            imgl Dial_begin35_18
            mt "Очередной извращенец!"
            mt "Ничего ему не известно!"
            mt "Он просто заманивает меня!"
            mt "Чтобы в поглазеть на мою прекрасную грудь!"
            imgl Dial_begin35_16
            m "Нет!"
            m "Я не собираюсь ходить ни в какие тайные места!"
            m "У меня есть более важные дела!"
            music Groove2_85
            imgr Dial_Citizen_5_4
            citizen5 "Глупый сиськи..."
            citizen5 "Мистер знает страшный тайн..."
            citizen5 "Приходи, когда будешь готова!"
            return -1
    # стоят у пилона
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 11941
    m "Что тебе известно?"
    m "Про какую тайну ты говоришь?!"
    imgf 11908
    citizen5 "Мистер платил за твои услуги, теперь ты плати мистеру за тайн!"
    imgd 11909
    m "Ты что, выбиваешь из меня деньги!?"
    imgf 11936
    citizen5 "Нееет, мне не нужны твой доллар!"
    citizen5 "Я хотеть нажимать твои Фудзиямы и лотос!"
    img 13317
    m "Что ты несешь?!"
    m "Какие фудзиямы? Какой лотос?!"
    m "Говори, что тебе известно или я ухожу!"
    imgd 13318
    citizen5 "Я сказать и даже заплатить тебе."
    citizen5 "Но только после того, как нажимать твои Фудзиямы и лотос!"
    imgd 13316
    m "..."
    $ menu_corruption = [monicaCitizens5CorruptionRequired1, 0]
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                imgf 40344
                mt "Может этот болван ничего не знает."
                mt "А я зря трачу свое время"
                mt "С другой стороны, он сказал, что все равно заплатит."
                mt "..."
                mt "Черт! Но мне некуда его вести!"
                #
                $ notif(t_("Монике некуда вести клиентов."))
                #
                imgd 13314
                m "Мне некуда тебя вести!"
                m "А раздеваться здесь для тебя я не буду!"
                imgd 13311
                citizen5 "Прекрасные Фудзиямы скрывают холодный сердце..."
                return -2
            # если арендует квартиру у Джека
            $ monicaCitizens5Slums1 = day # Моника согласилась пойти Акирой саном в свои апартаменты
            pass
        "Отказаться.":
            music Stealth_Groover
            imgf 40344
            mt "Я не понимаю, что этот тип от меня хочет!"
            mt "Пусть и дальше скрывает свою тайн!"
            mt "Пошел он к черту!"
            imgd 13310
            m "Нет!"
            m "Я не пойду с тобой никуда!"
            m "Можешь и дальше скрывать свою тайн!"
            imgf 13307
            citizen5 "Хм..."
            citizen5 "Мистер разочарован!"
            return -2
    # Моника в сомнениях
    music Groove2_85
    imgf 40334
    mt "Деньги мне в любом случае нужны..."
    mt "..."
    mt "Если я ему откажу сейчас, то ничего не узнаю и не заработаю..."
    # выглядывает мамочка
    music Master_Disorder
    img 24343 vpunch
    mt "И эта старая карга следит за мной..."
    imgd 24344
    w
    if ep214_perry_debt > 0:
        #
        $ notif(_("Моника должна выплачивать Перри долг."))
        imgd 40333
        mt "Я должна выплачивать долг этой мерзкой извращенке Перри!"
        #
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 40333
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    music Groove2_85
    imgf 13313
    m "Сколько ты мне заплатишь за то, что бы пойти ко мне?"
    imgd 13315
    citizen5 "Это ты должна мне платить..."
    imgd 13347
    m "Или плати деньги, или уходи!"
    imgf 13350
    citizen5 "Мистер хочет нажимать твои Фудзиямы и лотос."
    citizen5 "Мистер согласен! $ 10 тебя устроить?"
    # затемнение
    # апартаменты Моники
    # Акира сан в гостиной, а Моника в домашней одежде
    fadeblack 1.5
#    call ep211_quests_slums_apartments2_check_enter_forced() # Моника входит в апартаменты (смена одежды)
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_19
    scene black_screen
    with Dissolve(1)
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 41465
    citizen5 "Мистер не будет платить за твой одежда!"
    citizen5 "Оголи свои манящие груди, раскрой свой лотос передо мной!"
    citizen5 "Я хотеть нажимать их."
    music Stealth_Groover
    imgf 41466
    mt "Этот болван будет указывает мне, что делать?!"
    mt "Как он смеет?!"
    mt "Приказывать мне - Монике Бакфетт?!"
    mt "Самой прекрасной и утонченной леди этого города!"
    imgd 41467
    mt "Оголяться перед ним, этим жалким ничтожеством!"
    mt "И что он имеет ввиду под 'нажимать'?!"
    mt "Он хочет прикасаться к моему прекрасному телу своими грязными руками!?"
    m "Нажимать?!"
    music Groove2_85
    imgf 41468
    citizen5 "Да, я принес специальные вещи для нажимать."
    citizen5 "Но сначала ты должна раздеться!"
    citizen5 "Я платить тебе за это $ 2."
    imgd 41469
    m "Тогда ты должен мне уже $ 12!"
    imgf 41470
    citizen5 "Это не проблема для Мистера."
    citizen5 "Снимай свой одежда!"
    imgd 41471
    m "..."
    menu:
        "Раздеться и получить оплату в $ 12.":
            pass
    $ add_money(12.0)
    # затемнение, Моника разделась, стоит голая перед ним, он в одежде
    imgf 41472
    w
    sound vjuh3
    imgd 41473
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 41474
    citizen5 "Ооо! Какие красивые изгибания!"
    m "Что за тайну ты хотел рассказать?!"
    m "Говори!!!"
    imgf 41475
    citizen5 "Сначала я буду нажимать тебя, а потом расскажу все."
    # Акира достает прищепки 3 шт и показывает их Монике
    # Моника в ужасе
    music stop
    sound plastinka1b
    img 41476 hpunch
    m "Что ты собираешься делать?!"
    music Pyro_Flow
    m "Что это за штуки?!"
    imgd 41477
    m "Для чего ты их притащил?!"
    m "Я не позволю прикосаться этими штуками ко мне!!!"
    m "!!!"
    music Groove2_85
    imgf 41478
    citizen5 "Мистер платить тебе за одну штучка $ 5!"
    imgd 41479
    m "$ 5?"
    m "Да я даже за $ 50 не соглашусь!!!"
    m "Убери их, извращенец!!!"
    imgd 41480
    citizen5 "$ 10!"
    citizen5 "Или я всем расскажу твой страшный тайн!"
    $ menu_corruption = [0, monicaCitizens5CorruptionRequired2]
    menu:
        "НЕТ!!!":
            music Pyro_Flow
            imgd 41481
            m "Забирай свои штуки, тайны и проваливай отсюда!"
            m "Воооон!!!"
            imgd 41482
            citizen5 "Акира Сан оскарблен!"
            citizen5 "Kosho benjo!"
            pass
        "Согласиться.":
            $ monicaCitizens5Slums2 = day # Моника согласилась, чтобы Акира нацепил зажимы на ее грудь
            music Groove2_85
            imgf 41486
            mt "Черт!"
            mt "$ 10!"
            mt "Мне нужны деньги..."
            mt "..."
            # Акира подходит к Монике и вешает зажим на грудь Моники
            fadeblack 1.5
            music Loved_Up
            imgf 41487
            w
            sound snd_monica_ahh
            img 41488 hpunch
            m "АААААААААА!"
            m "БОЛЬНО!"
            imgd 41489
            m "КАК ЖЕ ЭТО БОЛЬНО!"
            imgd 41490
            w
            # мОНИКА ТЯНЕТ РУКУ ЧТО БЫ СНЯТЬ ПРИЩЕПКУ, НО аКИРА ЛОВИТ ЕЕ РУКУ
            sound Jump1
            img 41491
            citizen5 "Если ты убрать ее, я не буду платить!"
            # Моника закусывает губу от боли
            imgf 41492
            citizen5 "Тебе нравится, yariman?!"
            citizen5 "Хочешь еще?"
            citizen5 "Еще один зажим и еще $ 10..."
            imgd 41493
            w
            $ menu_corruption = [0, monicaCitizens5CorruptionRequired3]
            menu:
                "НЕТ!":
                    music Pyro_Flow
                    imgf 41494
                    mt "Это не выносимо больно!"
                    mt "Я не смогу это стерпеть второй раз!"
                    imgd 41495
                    m "НЕТ!"
                    imgd 41496
                    m "Нецепи эти штуки себе, извращенец!"
                    # Моника отцепляет прищепку и одевает ее Акире на нос
                    sound Jump2
                    img 41497 hpunch
                    sound scream_steve
                    citizen5 "АААААААААА!"
                    imgd 41498
                    citizen5 "Акира Сан оскарблен!"
                    citizen5 "Kosho benjo!"
                    pass
                "Согласиться.":
                    music Groove2_85
                    imgf 41494
                    mt "Какие унижения мне приходится терпеть?!"
                    mt "И ради чего?! Ради $ 10!"
                    imgd 41499
                    m "Следующая будет $ 20!"
                    imgf 41500
                    citizen5 "Ааааа, yariman нравится?!"
                    citizen5 "Мистер знал!"
                    citizen5 "$ 15!"
                    citizen5 "Потому что ты дать мистеру величайшее наслаждение!"
                    imgd 41501
                    m "..."
                    m "$ 15!"
                    # Акира вешает вторую пришепку на грудь Моники
                    fadeblack 1.5
                    music Loved_Up
                    img 41502 hpunch
                    sound snd_monica_ahh
                    m "АААААААААА!"
                    imgd 41503
                    w
                    imgd 41504
                    mt "Это ужасно!"
                    mt "Нацепить бы ему этих прищепок на его отросток!"
                    mt "АААААААААААА!"
                    # Моника снова закусывает губу от боли
                    imgf 41505
                    w
                    imgd 41492
                    citizen5 "Мистер видит как yariman сдерживает удовольствие!"
                    citizen5 "Но у меня есть еще одна штучка..."
                    citizen5 "Чтобы нажимать твой лотос!"
                    # Моника в ужасе
                    $ menu_corruption = [0, monicaCitizens5CorruptionRequired4]
                    menu:
                        "НЕТ!!!":
                            music stop
                            sound plastinka1b
                            img 41506 vpunch
                            mt "ЧТОООО?!"
                            mt "ОН СОБИРАЕТСЯ ПРИЦЕПИТЬ ЭТУ ПРЕЩЕПКУ МНЕ НА..."
                            music Pyro_Flow
                            img 41507
                            m "НЕТ!!!"
                            m "УБЕРИ СВОИ РУКИ!"
                            # Моника отцепляет обе прищепкИ и одивает их Акире на ущи, как серьги
                            # Моника дает Акире поджопник
                            sound Jump2
                            img 41508 hpunch
                            sound scream_steve
                            citizen5 "АААААААААА!"
                            imgd 41509
                            citizen5 "Теперь все узнают твой тайн!"
                            citizen5 "Дешевая Kosho benjo!"
                            sound snd_kick_fred1
                            img 41510 vpunch
                            w
                            imgd 41511
                            w
                            fadeblack
                            sound snd_door_close1
                            pause 2.0
                            music Stealth_Groover
                            # Акира уходит, Моника злая
                            imgf 41485
                            mt "Мерзкий слизняк!"
                            mt "Ничтожество!!!"
                            mt "Я сравняю эти гребаные трущобы с землей!"
                            mt "Вместо со всеми ее бесполезными обитателями!"
                            mt "!!!"
                            return -3
                        "Согласиться.":
                            music Groove2_85
                            $ monicaCitizens5Slums3 = day # Моника согласилась, чтобы Акира нацепил зажимы на ее киску
                            imgf 41494
                            mt "Моника, соберись!"
                            mt "Ты сильная! Ты это сделаешь!"
                            mt "Этот гребаный извращенец заплатит тебе деньги..."
                            mt "И в твоем кармане прибавится еще немного денег!"
                            imgd 41512
                            citizen5 "Сейчас Мистер будет нажимать твой лотос!"
                            citizen5 "А ты получать еще $ 15 за твой лотос!"
                            m "..."
                            # Акира вешает третью пришепку Монике на клитор
                            fadeblack 1.5
                            music Loved_Up
                            img 41513 hpunch
                            sound snd_woman_scream2
                            m "ААА!"
                            m "ААААА!"
                            imgd 41514
#                            sound snd_woman_pain
                            m "АААААААА!"
                            imgf 41515
                            citizen5 "Зачем ты так кричишь, yariman?"
                            citizen5 "Я буду целовать тебя! И заплачу еще $ 5!"
                            imgd 41516
                            w
                            # Моника не успевает ни чего ответить, а Акира уже целует ее в засос с языком и дергает за прищепки на груди
                            # Моника сопративляется и пытается оттолкнуть его
                            sound kiss2
                            imgd 41517
                            w
                            imgd 41518
                            w
                            sound snd_kiss2
                            imgd 41519
                            w
                            sound Jump2
                            img 41520 vpunch
                            w
                            imgd 41521
                            w
                            imgf 41522
                            citizen5 "Еще $ 10 и я буду целовать твой лотос!"
                            # Моника офигевшая, руки в разные сторны , а Акира делает монике ликинг и мнет груть
                            # Моника отодвигается от Акиры
                            sound vjuh3
                            img 41523 hpunch
                            w
                            imgd 41524
                            w
                            imgf 41525
                            w
                            imgd 41526
                            w
                            imgf 41527
                            w
                            sound lick3
                            imgd 41528
                            w
                            sound lick3
                            imgd 41527
                            w
                            sound lick3
                            imgd 41528
                            w
                            sound lick3
                            imgd 41527
                            w
                            sound lick3
                            imgd 41528
                            w
                            imgf 41529
                            w
                            imgd 41530
                            w
                            imgd 41531
                            w
                            sound Jump1
                            img 41532
                            w
                            sound snd_woman_pain1
                            img 41533 hpunch
                            w
                            music Power_Bots_Loop
                            imgd 41534
                            m "ХВАТИТ!"
                            sound vjuh3
                            img 41535
                            w
                            fadeblack 2.0
                            music Groove2_85
                            imgfl 41536
                            m "Ты получил, что хотел!"
                            m "Теперь плати мне"
                            m "И говори свою тайну!"
                            imgf 41537
                            citizen5 "Мистер даволен!"
                            citizen5 "Ему понравилась yariman!"
                            $ add_money(55.0)
                            m "Говори, что знаешь!"
                            imgd 41538
                            mt "Извращенец!"
                            music Hidden_Agenda
                            imgf 41470
                            citizen5 "Мистер знает тайну, что ты всем сосешь!"
                            citizen5 "Потому что ты - yariman!"
                            citizen5 "Но мистер никому не скажет!"
                            music Pyro_Flow
                            img 41539
                            m "АХ ТЫ ИЗВРАЩЕНЕЦ!!!"
                            m "САМ ТЫ yariman!!!"
                            m "Сволочь!!!!"
                            pass
    # Моника В БЕШЕНСТВЕ
    music Pyro_Flow
    img 41483 hpunch
    m "ПРОВАЛИВАЙ ИЗ МОИХ АПАРТАМЕНТОВ!!!"
    m "А СВОИ ТАЙНЫ..."
    m "И ИЗВРАЩЕНСКИЕ ШТУЧКИ ОСТАВЬ СЕБЕ!!!"
    sound man_steps
    imgf 41484
    w
    fadeblack
    sound snd_door_close1
    pause 2.0
    music Stealth_Groover
    # Акира уходит, Моника злая
    imgf 41485
    mt "Мерзкий слизняк!"
    mt "Ничтожество!!!"
    mt "Я сравняю эти гребаные трущобы с землей!"
    mt "Вместо со всеми ее бесполезными обитателями!"
    mt "!!!"
    return -3
