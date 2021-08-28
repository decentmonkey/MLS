default monicaBettyRalphAnal1 = 0 # Бетти не дала Ральфу вечером в спальне
default monicaBettyRalphAnal2 = 0 # Бетти согласилась на секс с Ральфом
default monicaBettyRalphAnal3 = 0 # Моника согласилась на анальный секс с Ральфом впервые
default monicaBettyRalphAnal4 = 0 # у Моники и Ральфа состоялся первый анал

default monicaBettySexRalph_cumzone = 0

define monicaRalphAnalCorruptionRequired1 = 850 # Моника согласилась на анал с Ральфом

define v_Betty_Ralph_Sex1_1_sound_name = "v_Betty_Ralph_Sex1_1"
define v_Monica_Ralph_Anal1_1_sound_name = "v_Monica_Ralph_Anal1_1"
define v_Monica_Ralph_Anal2_1_25_sound_name = "v_Monica_Ralph_Anal2_1"

#call ep219_dialogues1_ralph_1() # Бетти обламывает Ральфа
#call ep219_dialogues1_ralph_2() # секс Бетти и Ральфа
#call ep219_dialogues1_ralph_3() # новый пункт "Анальный секс."
#call ep219_dialogues1_ralph_4() # если Моника взяла у Ральфа деньги, мысли
#call ep219_dialogues1_ralph_5() # если Моника намекнула Ральфу на его с Бетти развод, мысли

# при условии, что у Бетти была групповуха
# вечером в бывшей спальне Моники
label ep219_dialogues1_ralph_1:
    # Бетти лежит на постели, как обычно, только в бюстгалтере, читает журнал
    # к постели подходит Ральф, ложится с ней рядом
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Тем временем...")) from _rcall_textonblack_32
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 34198
    w
    imgf 34197
    w
    imgd 34199
    w
    imgf 34200
    w
    sound Jump2
    img 34203 hpunch
    ralph "Бетти, дорогая, я так по тебе соскучился."
    # кладет руку ей на грудь и лезет целоваться
    # Бетти, не отрываясь от журнала
    imgf 34201
    w
    sound Jump1
    img 34202 vpunch
    w
    imgd 34204
    betty "Ральф, не сегодня!"
    # он продолжает лезть к ней, жмякает ее груди
    imgf 34205
    w
    sound Jump1
    img 34206
    w
    imgd 34205
    w
    sound Jump1
    img 34206
    ralph "Ну, Бетти. Давай по-быстренькому."
    # она скидывает его руки со своей груди
    imgd 34207
    betty "Ральф, перестань! Ты мне мешаешь!"
    ralph "Дорогая, ну оторвись от своего журнала."
    ralph "Ты же не откажешь своему любимому мужу в исполнении супружеского долга?"
    # Бетти поворачивается к нему и грозно на него смотрит
    img 34208
    betty "Ральф! Я же сказала тебе, что не сегодня!"
    betty "Мы совсем недавно делали это!"
    # он удивленно
    imgd 34209
    ralph "Недавно?!"
    ralph "Неделю назад - это по-твоему недавно?!"
    img 34210
    betty "ДА!" # и снова утыкается в журнал
    # Ральф растерянно смотрит на нее, потом снова кладет руку на низ живота Бетти, игриво говорит ей
    imgf 34211
    w
    imgd 34212
    w
    music Hidden_Agenda
    imgf 34213
    ralph "Моя дорогая Бетти решила поиграть со мной в недотрогу?"
    ralph "Мне нравятся такие игры в постели..."
    # смотрит что она без трусиков
    sound Jump2
    imgd 34214
    ralph "Ты ведь даже без трусиков."
    ralph "Я вижу что ты специально соблазняешь меня, любимая."
    imgf 34215
    ralph "Давай, я буду профессором из университета, а ты студенткой, которой нужно сдать зачет?"
    ralph "Здорово я придумал, да?"
    # Бетти закатывает глаза, снова скидывает его руку
    # говорит с ним раздраженно
    music Groove2_85
    sound2 vjuh3
    img 34216 hpunch
    betty "Что за глупости?!"
    betty "Я не буду заниматься какими-то там извращенскими играми!"
    betty "Я..."
    betty "У меня голова болит!"
    imgf 34217
    ralph "Дорогая, я знаю отличный способ от головной боли." # кладет руку на свою ширинку
    # Бетти начинает злиться
    imgd 34219
    w
    img 34218
    betty "И вообще!"
    betty "Ты, как хороший муж, мог бы помогать мне по хозяйству, а потом уже требовать от меня чего-то!"
    # Ральф убирает руку со своей ширинки, растерянно смотрит на нее
    imgd 34220
    ralph "Бетти..."
    # она его перебивает
    betty "Почему я сама должна решать хозяйственные вопросы?!"
    betty "Почему мне ни с чем не помогаешь по дому?!"
    ralph "Но ты мне ничего не говорила..."
    # Бетти наезжает на него
    imgd 34209
    betty "Мог и сам спросить, нужна ли мне помощь по хозяйству, Ральф!"
    betty "Я делаю по дому абсолютно всю работу! Я устаю!"
    betty "А ты целыми днями читаешь свою дурацкую книжку, сидя в кресле!"
    betty "Это нормально, скажи мне, Ральф?!"
    ralph "Дорогая, но ведь у нас есть прислуга... Водитель, гувернантка..."
    # она снова его перебивает
    sound snd_paper2
    img 34221 vpunch
    betty "От этой гувернантки нет никакого толку! Она некомпетентна в своей работе!"
    betty "Мне приходится постоянно контролировать ее работу!"
    betty "Ты хоть представляешь, сколько сил и времени у меня занимает это?!"
    betty "Я задумываюсь о том, чтобы найти ей замену!"
    # Ральф растерянно чешет репу
    imgd 34222
    ralph "Бетти..."
    betty "Хватит, Ральф!"
    betty "Я сегодня целый день занималась хозяйственными делами!"
    betty "Потому что я хорошая хозяйка!"
    betty "И все стараюсь для тебя делать!"
    imgd 34223
    betty "А ты меня утомляешь этими разговорами!"
    betty "И это наглость с твоей стороны требовать сейчас от меня исполнения какого-то супружеского долга!"
    betty "Ты поступаешь эгоистично, Ральф!"
    ralph "Но дорогая..."
    # Бетти раздраженно его перебивает
    imgd 34224
    betty "Все! Хватит! Я устала и хочу спать!"
    betty "И голова у меня разболелась еще больше!"
    imgf 34225
    w
    imgd 34226
    w
    # Бетти откладывает журнал, Ральф разочарованно смотрит на свой стояк, потом на попу Бетти
    # звук выключателя, гаснет свет
    $ monicaBettyRalphAnal1 = day # Бетти не дала Ральфу вечером в спальне
    fadeblack 2.0
    return

# на следующий вечер после того, как Бетти отказала Ральфу в интиме
# бывшая спальня Моники
label ep219_dialogues1_ralph_2:
    # Бетти лежит на постели и снова читает журнал
    # Ральф снова ложится с ней рядом и начинает приставать
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Тем временем...")) from _rcall_textonblack_33
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 34227
    w
    imgf 34228
    w
    imgd 34229
    w
    imgf 34230
    w
    music Hidden_Agenda
    sound2 Jump2
    img 34231 vpunch
    ralph "Дорогая, мне так нравится, когда на тебе это белье."
    # проводит рукой по ее груди, потом опускает руку ниже, к трусикам (которых нет)
    imgf 34232
    ralph "Ты такая красивая... Такая сексуальная."
    sound Jump1
    imgd 34233
    ralph "Мне так повезло, что у меня такая замечательная жена..."
    # целует ее в щеку, а она в это время не перестает глазет в журнал
    imgf 34234
    w
    imgd 34235
    betty "Ральф, ты снова за свое!"
    # он продолжает ее целовать, говорит игриво
    imgf 34236
    sound kiss1
    w
    imgd 34235
    ralph "Мммм... Я так хочу тебя, Бетти."
    imgf 34237
    ralph "Ты ведь не откажешь своему любимому мужу, как вчера?"
    ralph "Ты же не хочешь меня расстраивать?" # целует
    imgd 34236
    sound kiss1
    w
    menu:
        "Согласиться на секс с Ральфом.":
            $ monicaBettyRalphAnal2 = day # Бетти согласилась на секс с Ральфом
            pass
        "Отказать ему!":
            # Бетти раздраженно
            music Groove2_85
            sound snd_paper2
            imgf 34238
            betty "Не сегодня, Ральф!"
            betty "Я слишком устала и у меня опять болит голова!"
            imgd 34239
            ralph "Но дорогая..."
            betty "Все, Ральф, хватит! Я хочу спать!"
            imgd 34240
            w
            imgf 34241
            w
            # Бетти откладывает журнал, Ральф разочарованно смотрит на свой стояк, потом на попу Бетти
            # звук выключателя, гаснет свет
            fadeblack 2.0
            return False
    # Бетти отворачивает лицо в сторону, закатывает глаза
    music Groove2_85
    imgf 34242
    betty_t "Если я сейчас опять откажу ему, он завтра ко мне снова будет лезть!"
    betty_t "Зато, если я сейчас соглашусь, то он отстанет от меня на целую неделю."
    betty_t "Думаю, стоит потерпеть..."
    betty_t "Черт! Как же нелегко быть хорошей женой!"
    # Бетти откладывает журнал и снисходительно говорит Ральфу
    imgd 34238
    betty "Ральф, я не откажу тебе сегодня."
    betty "Но ты должен пообещать мне, что будешь чаще помогать мне по хозяйству!"
    # довольный Ральф чмокает ее в губы, кладет руку на ее грудь
    music Loved_Up
    imgf 34243
    sound kiss1
    w
    imgd 34244
    ralph "Конечно, дорогая! Я сделаю все, как ты скажешь!"
    ralph "Снимай скорее это с себя!"
    ralph "Мне не терпится поцеловать твою прекрасную грудь!"
    menu:
        "Снять бюстгальтер с Бетти.":
            pass
    # Бетти снимает с себя бюстгальтер, лежит в одних трусиках с недовольным видом
    # Ральф ласкает ее грудь, целует, а Бетти ворчит в это время
    imgf 34245
    w
    sound vjuh3
    imgd 34246
    w
    sound snd_paper2
    img 34247 vpunch
    w
    fadeblack
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    imgfl 34248
    w
    imgf 34249
    w
    sound kiss1
    imgd 34250
    betty "Ты же сам должен понимать, Ральф, как непросто уследить за всем в таком большом доме."
    betty "У меня за целый день нет ни минуты отдыха!"
    sound lick3
    imgf 34251
    ralph "Да, Бетти. Ты такая замечательная хозяйка..."
    imgd 34252
    w
    sound kiss1
    imgf 34253
    ralph "Так люблю целовать тебя..."
    music Stealth_Groover
    imgd 34254
    betty "Да! И ты должен ценить это, Ральф!"
    ## трусиков же изначально нет. Наверно он скажет, что хочет поцеловать ее там
#    ralph "Дай, я сниму с тебя трусики, дорогая."
    # Бетти недовольно смотрит, как Ральф стягивает трусики с нее, бросает на пол
    imgd 34255
    betty "!!!"
    ralph "Конечно, дорогая..."
    # Ральф тем временем наклоняется и целует ее киску
    fadeblack 1.5
    music Loved_Up
    sound2 lick3
    imgfl 34256
    w
    imgf 34257
    w
    imgd 34254
    ralph "Бетти, дорогая, раздвинь ножки."
    ralph "Я хочу приласкать твою киску."
    imgd 34258
    w
    menu:
        "Раздвинуть ноги.":
            pass
    # Бетти раздвигает ноги, продолжая ворчать, а Ральф целует ее между ног
    imgf 34259
    w
    sound lick3
    imgd 34260
    w
    sound lick3
    imgf 34261
    w
    imgd 34262
    betty "Такую хорошую жену, как Я, еще поискать надо!"
    betty "А ты ведешь себя эгоистично, требуя исполнения супружеского долга когда тебе вздумается!"
    # Ральф отвечает между поцелуями
    imgd 34263
    ralph "Всего лишь раз в неделю, дорогая. Это же так редко."
    ralph "Может быть будем делать это чаще?"
    betty "Куда еще чаще, Ральф?!"
    ralph "Но Бетти..."
    img 34264
    betty "Ты должен радоваться, что у нас регулярная интимная жизнь!"
    betty "И что я тебе не отказываю раз в неделю!"
    betty "Я и так слишком многое для тебя делаю!"
    imgf 34265
    w
    sound lick3
    imgd 34266
    w
    sound lick3
    imgd 34265
    w
    sound lick3
    imgd 34266
    w
    sound lick3
    imgd 34265
    w
    sound lick3
    imgd 34266
    w
    sound lick3
    imgd 34265
    w
    sound lick3
    imgd 34266
    w
    imgf 34263
    ralph "Да, Бетти. Мне очень повезло, что у меня такая замечательная жена."
    ralph "К тому же еще и красивая."
    imgd 34267
    w
    sound lick3
    imgd 34268
    w
    sound lick3
    imgd 34267
    w
    sound lick3
    imgd 34268
    w
    sound lick3
    imgd 34267
    w
    sound lick3
    imgd 34268
    w
    sound lick3
    imgd 34267
    w
    sound lick3
    imgd 34268
    w
    imgf 34263
    betty "И еще хозяйственная!"
    ralph "Да..."
    imgd 34269
    sound lick3
    betty "И порядочная!"
    ralph "Да, дорогая."
    imgf 34270
    ralph "Ты у меня самая лучшая, Бетти... Я хочу взять тебя сзади, повернись ко мне спиной."
    # Бетти возводит глаза к потолку, типа как он меня задолбал
    imgd 34271
    w
    imgd 34272
    betty "Ральф, давай уже так, по-быстрому!"
    ralph "Ну дорогая!"
    imgd 34273
    betty_t "Кто придумал этот дурацкий супружеский долг?!"
    betty "!!!"
    menu:
        "Сделать, как просит Ральф.":
            pass
    # затемнение
    # Бетти стоит в коленно-локтевой, подперев лицо ладонями, лицо скучающее
    # Ральф в это время вводит свой член в ее киску, стоя сзади нее, тиская ее за ягодицы
    fadeblack 2.0
    music Loved_Up
    imgfl 34275
    w
    imgf 34274
    w
    imgd 34276
    ralph "Ооооо!!!"
    imgf 34277
    w
    imgd 34278
    w
    imgd 34279
    w
    imgd 34280
    ralph "Как же здорово, Бетти!"
    # Бетти продолжает ворчать во время секса
    imgf 34281
    betty "Ральф, аккуратнее!"
    betty "Из-за тебя у меня на попе будут синяки!"
    ralph "Оооох, дорогая."
    imgd 34282
    ralph "Я просто так соскучился, что еле сдерживаю себя!"
    betty "Ты во время интима со мной, должен думать не только о себе, Ральф!"
    betty "В первую очередь, ты должен думать о моем удовольствии!"
    imgd 34275
    betty "А ты тискаешь меня, как какую-то непорядочную девицу!"
    betty "Думаешь, что мне это доставляет удовольствие, Ральф?!"
    imgf 34283
    ralph "Хорошо, дорогая. Я постараюсь."
    betty "Постарайся, Ральф!"
    # Ральф продолжает ее пялить
    imgd 34284
    w
    sound chpok6
    img 34285 hpunch
    w
    imgf 34286
    ralph "Так тепло у тебя внутри. Мммм..."
    ralph "Вот бы каждый день проникать в твою киску, Бетти!"
    imgd 34287
    w

    #video
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Ralph_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Ralph_Sex1_1= Movie(play="video/v_Betty_Ralph_Sex1_1.mkv")
    show videov_Betty_Ralph_Sex1_1
    with fade
    ralph "Дааа, это было бы замечательно!"
    ralph "Я тогда был бы самым счастливым мужем на свете!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 34275
    betty "Что значит 'был бы', Ральф?!"
    # Ральф шлепает ее по ягодице
    # Бетти раздраженно
    imgd 34289
    w
    sound snd_slap1
    img 34290 hpunch
    w
    img 34291
    w
    img 34292
    betty "Эй, полегче там! Обращайся со мной нежнее!"
    betty "Что за мужланские замашки?! Кошмар!"
    imgf 34288
    betty "Я еще раз повторяю свой вопрос, Ральф!"
    betty "Что значит 'был бы самым счастливым'?!"
    betty "Тебе что-то не нравится?!"
#    w

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Ralph_Sex1_2= Movie(play="video/v_Betty_Ralph_Sex1_2.mkv")
    show videov_Betty_Ralph_Sex1_2
    with fade
    ralph "Ммммм..."
    ralph "Мне все нравится, дорогая."
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
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Ralph_Sex1_3= Movie(play="video/v_Betty_Ralph_Sex1_3.mkv")
    show videov_Betty_Ralph_Sex1_3
    with fade
    betty "Тебе так повезло иметь такую замечательную жену, как Я!"
    betty "Я снимаю с тебя абсолютно все вопросы по хозяйству!"
    betty "И обеспечиваю тебе регулярную интимную жизнь!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Бетти продолжает клевать мозг
    imgf 34293
    ralph "Дааа..."
    imgd 34294
    betty "И еще я слежу за успеваемостью этого мелкого сопляка, твоего сына, в колледже!"
    betty "Хотя это твоя прямая обязанность, Ральф!"
    betty "Которую выполняю Я!"
    imgf 34295
    w

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Ralph_Sex1_4= Movie(play="video/v_Betty_Ralph_Sex1_4.mkv")
    show videov_Betty_Ralph_Sex1_4
    with fade
    betty "А ты еще чем-то недоволен?!"
    betty "Это неблагодарность с твоей стороны, Ральф!"
    betty "Ты совсем не ценишь того, что имеешь!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

#    sound drkanje5
    imgd 34296
    ralph "Я ценю тебя, дорогая..."
    w

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Ralph_Sex1_5= Movie(play="video/v_Betty_Ralph_Sex1_5.mkv")
    show videov_Betty_Ralph_Sex1_5
    with fade
    ralph "Ммммм..."
    ralph "Дааа..."
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
    image videov_Betty_Ralph_Sex1_6= Movie(play="video/v_Betty_Ralph_Sex1_6.mkv")
    show videov_Betty_Ralph_Sex1_6
    with fade
    ralph "Очень ценю! Особенно твою попу!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 34288
    betty "Ральф, в первую очередь..."
    # он перебивает ее, говорит ей возбужденно
    ralph "Бетти!"
#    ralph "Знаешь, чем ты можешь осчастливить сейчас своего любимого мужа?"
    ralph "Милая, давай попробуем что-то новое? Я очень давно этого хотел!"
    # Бетти подозрительно косится на него, немая пауза
    img 34297 vpunch
    betty "?!"
    # Ральф, не дожидаясь ее ответа, выходит из ее киски
    imgf 34280
    w
    sound chpok6
    img 34279
    w
    imgd 34298
    betty "Что ты делаешь, Ральф?"
    betty "Что ты задумал?"
    ralph "Мммм... Тебе понравится, дорогая..."
    # потом направляет свой член в ее анус и пытается тыкнуться в него
    imgf 34279
    w
    sound Jump1
    imgd 34299
    w
    img 34300
    betty "ЭЙ!!!"
    # Бетти резко вскакивает, повернувшись лицом к нему
    # Ральф продолжает плотоядно пялиться на нее
    sound Jump2
    img 34301 vpunch
    w
    imgd 34302
    ralph "Бетти..."
    ralph "Какая же ты у меня красивая, дорогая!"
    # Бетти начинает возмущаться
    music Pyro_Flow
    img 34303 hpunch
    betty "РАЛЬФ! КАК ТЫ МОГ?!?!?!"
    betty "!!!"
    imgd 34304
    betty "Как ты посмел?!?!?!"
    betty "Ты за кого меня принимаешь, Ральф?!"
    # Ральф растерян, член падает
    imgd 34305
    ralph "Дорогая..."
    betty "Я твоя жена! И Я порядочная женщина!"
    betty "А то, что ты хотел сделать!.. Это!.."
    img 34306
    betty "Это аморально, Ральф!"
    betty "Никогда! Слышишь?! Никогда не смей предлагать мне подобной гадости!!!"
    # она с негодованием вскакивает и идет в сторону выхода из спальни
    # Ральф ей вслед
    imgf 34307
    w
    sound snd_walk_barefoot
    imgd 34308
    w
    img 34309
    ralph "Но Бетти!"
    ralph "Куда же ты?!"
    ralph "Я ведь еще не кончил!"
    # она пренебрежительно машет на него рукой
    imgd 34310
    betty "Все, Ральф!!!"
    betty "С меня довольно!"
    betty "Ты унизил меня своим поступком! МЕНЯ, свою жену!!!"
    betty "Я не хочу больше с тобой разговаривать!"
    imgd 34311
    w
    # она возмущенно уходит
    # Ральф разочарованно смотрит ей вслед
    fadeblack 2.0
    return True

# при условии, что Бетти отказала Ральфу в анальном сексе
# во время очередной встречи Моники и Ральфа, пока Бетти на фитнесе
# в меню из лейбла ep214_dialogues5_bardie_ralph_12 появляется новый пункт "Анальный секс.":
label ep219_dialogues1_ralph_3:
    # Ральф трогает груди Моники
    if ep219_quests_ralph3_last_day == 0:
        fadeblack
        sound snd_fabric1
        pause 2.0
        music Loved_Up
        imgfl 34312
        w
        imgf 34313
        w
        imgd 34314
        ralph "Бетти..."
        ralph "Я так тебя хочу."
        ralph "Какая же ты красивая!"
        # целует губы, потом грудь
        imgf 34315
        w
        sound kiss2
        imgd 34316
        w
        sound kiss1
        imgd 34317
        w
        imgf 34314
        ralph "Бетти..."
        # Моника игриво
        imgd 34318
        m "Мистер Робертс, я тоже хочу вас!"
        # Ральф гладит попу Моники, игриво говорит ей
        imgf 34321
        w
        sound Jump2
        imgd 34320
        w
        music Hidden_Agenda
        imgf 34319
        ralph "Плохая гувернантка принадлежит мне? Она сделает все что я захочу?"
        mt "!!!"
        # Моника притворно улыбаясь
        imgd 34319
        m "Да, Мистер Робертс, плохая гувернантка сделает все что вы захотите..."
        imgd 34322
        mt "Ненавижу притворяться перед этим старикашкой!"
        # Ральф шлепает ее по ягодице
        imgf 34323
        w
        sound snd_slap1
        img 34324 hpunch
        w
        imgd 34325
        ralph "В таком случае, плохая гувернантка даст мне доступ к своей попке."
        m "..."
        m "Мистер Робертс, вы... Вы хотите сделать это в мою..."
        imgd 34326
        ralph "Да, Бетти. Я хочу сегодня войти в твою попку."
        ralph "Ты же не откажешь хозяину дома?"
        m "!!!"
        menu:
            "Отказаться!":
                # Моника в шоке
                music Pyro_Flow
                img 34327 vpunch
                mt "ЧТО?!"
                mt "Этот мерзкий старикашка хочет сделать ЭТО в мою попу?!"
                mt "Гребаный извращенец!"
                imgd 34328
                mt "Я ни за что не позволю ему этого!"
                mt "!!!"
                mt "Мне нужно как-то отвлечь этого никчемного идиота от моей попы!"
                # Моника притворно улыбается ему
                fadeblack 1.5
                music Hidden_Agenda
                imgf 34329
                m "..."
                m "Мистер Робертс..."
                m "У вашей плохой гувернантки Бетти сегодня настроение для кое-чего другого..."
                m "Уверена, хозяину дома это очень понравится."
                # Ральф ведется, игриво спрашивает Монику
                imgd 34330
                ralph "Да?"
                ralph "Звучит заманчиво..."
                ralph "Что же ты хочешь предложить мне, Бетти?"
                return False
                # jump на начало меню с доступом ко всем пунктам (футджоб, титсджоб, минет, секс), кроме анала
            "Вот дьявол!":
                pass
        # Моника в шоке
        music Pyro_Flow
        img 34327 hpunch
        mt "ЧТО?!"
        mt "Этот мерзкий старикашка хочет сделать ЭТО в мою попу?!"
        mt "Гребаный извращенец!"
        # если был анал с Филиппом
        if monicaBiffInvestorsPhilip2 > 0:
            #
            $ notif(_("У Моники был анальный секс с Филиппом."))
            #
            imgd 34328
            mt "Я не хочу, чтобы моя попа болела, как тогда..."
            mt "После того, как подлый мерзавец Филипп водил меня в свой жуткий извращенский подвал!"
            mt "Это было отвратительно! И больно!"
            # если Моника сука
            if monicaBitch == True:
                $ notif_monica()
                img 34331
                mt "Я оторву этому никчемному гаду Филиппу яйца при первой же возможности!"
            mt "!!!"
        imgf 34322
        mt "Что же теперь делать, Моника?"
        mt "Если ты сейчас откажешь этому старому извращенцу и подкаблучнику..."
        mt "То он может заподозрить тебя в неискренности."
        imgd 34332
        mt "А мне это не на руку..."
        mt "Чертов Ральф со своими извращенским желаниями!!!"
        mt "Ненавижу этого старикашку!!!"

######### с этого места повторящаяся сцена при выборе пункта "Анал"
    # Ральф смотрит на Монику пошло
    fadeblack 2.0
    music Groove2_85
    imgfl 34333
    w
    imgf 34334
    ralph "Ну что, гувернантка Бетти?"
    ralph "Давай мне скорее свою аппетитную попку."
    # Моника медлит, начинает ломаться
    music Hidden_Agenda
    imgd 34335
    m "Мистер Робертс, ваша гувернантка очень хотела бы порадовать вас..."
    m "Но..."
    ralph "Что, Бетти?"
    if monicaBettyRalphAnal4 > 0:
        imgd 34336
        m "Моя попа... Она так болит после прошлого раза..."
        imgd 34337
        ralph "В этом нет ничего страшного, Бетти."
        ralph "Совсем скоро твоя попа привыкнет и перестанет болеть."
        ralph "Я буду очень-очень аккуратен с твоей попкой сегодня."
    if monicaBettyRalphAnal4 == 0:
        imgd 34336
        m "Просто я... Я никогда не делала этого..."
        imgd 34337
        ralph "Правда? Я буду первым?"
        imgf 34338
        mt "Что значит буду первым?!"
        imgd 34337
        ralph "В этом нет ничего страшного, Бетти."
        ralph "Я буду очень-очень аккуратен с твоей девственной попкой."
    imgf 34339
    m "Но я боюсь..."
    ralph "Ты не представляешь, как я хочу сделать это!"
    ralph "Ну не отказывай мне, Бетти!"
    ralph "Моя первая Бетти не согласилась на это."
    ralph "Не поступай со мной также, как она!"
    imgd 34341
    ralph "Я очень оценю, если ты сейчас согласишься!"
    music Groove2_85
    imgd 34342
    mt "Хмм..."
    mt "Эта дурацкая провинциалка отказала ему?"
    # если Моника видела секс Бетти и Стива в офисе Стива
    if bettySteveOfficeSteveSex == True:
        #
        $ notif(_("Моника видела, что у Бетти был анальный секс со Стивом."))
        #
        img 34343
        mt "Она что, притворяется перед ним невинной овечкой?"
        mt "А сама с готовностью подставляет свой провинциальный зад Стиву!"
        mt "Вот стерва!"
        #
    imgf 34340
    mt "Это немного меняет дело..."
    mt "Если я сейчас соглашусь на эту извращенскую гадость..."
    mt "То он будет тянуться ко мне еще больше."
    mt "А провинциалка Бетти отойдет на второй план!"
    # если Моника сказала Ральфу, что ей нужны деньги
    if monicaBettyRalphSeduction8 == True:
        #
        $ notif(_("Моника встречается с Ральфом за деньги."))
        #
        music Hidden_Agenda
        imgd 34344
        ralph "Я готов за это дать тебе намного больше денег, чем обычно."
        ralph "В качестве компенсации за твои переживания."
        m "Правда?"
        ralph "Конечно, Бетти!"
        ralph "Мне для тебя не жалко никаких денег!"
        imgf 34345
        mt "Хммм..."
        mt "Мне нужны эти деньги..."
        # если Монику выгнали с эскорта
        if ep212_escort_monica_fired == True:
            #
            $ notif(_("Моника больше не работает в ВИП-эскорте."))
            #
            imgd 34346
            mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
            #
        # если должна Перри
        if ep214_perry_debt > 0:
            $ notif(_("Моника должна выплачивать Перри долг."))
            imgd 34347
            mt "Мне еще выплачивать долг мерзкой Перри!"
        # если арендует апартаменты у Джека
        if slumsApartmentsRentActive == True:
            #
            $ notif(t_("Моника арендует апартаменты в трущобах."))
            #
            imgd 34347
            mt "Я должна оплачивать ту грязную дыру, которую мне сдает Джек!"
            #
        imgf 34348
        ralph "Я тебе заплачу на целых сто долларов больше, Бетти!"
        music Pyro_Flow
        img 34336
        mt "Сто долларов?!"
        mt "Он что, издевается?!"
        mt "Он оценивает мою попу в сто долларов?!"
        mt "Мерзкий! Жадный! Отвратительный неудачник!"
        music Groove2_85
        imgd 34343
        mt "Черт! С другой стороны..."
        mt "Я могу сейчас заработать целых $ 300!"
        #

    # если Моника говорила Ральфу, что любит его
    else:
        #
        $ notif(_("Моника говорила Ральфу, что влюблена в него."))
        #
        music Stealth_Groover
        imgd 34345
        mt "Позволить ему сделать эту гадость с моей попой - это немыслимая жертва с моей стороны!"
        mt "!!!"
        mt "Но мне выгодно играть перед ним влюбленную дурочку! Этот жалкий кретин должен оставаться у меня на крючке!"
        imgd 34338
        mt "Моя цель - заполучить мой дом обратно и стать вновь его хозяйкой! Законной хозяйкой!"
        mt "И я сделаю для этого ВСЕ!"
        #
    music Groove2_85
    imgf 34341
    mt "!!!"
    ralph "Бетти, иди ко мне..."
    # коррапшн
    $ menu_corruption = [monicaRalphAnalCorruptionRequired1, 0]
    menu:
        "Согласиться на анальный секс.":
            $ monicaBettyRalphAnal3 = day # Моника согласилась на анальный секс с Ральфом впервые
            pass
        "Отказаться!":
            # Моника зло
            music Pyro_Flow
            imgd 34342
            mt "Нет! Не таким образом!"
            mt "Этот мерзкий старикашка хочет сделать ЭТО в мою попу!"
            mt "Я пока не готова к таким жертвам со своей стороны!"
            mt "Гребаный извращенец!"
            imgd 34349
            mt "Я ни за что не позволю ему этого!"
            mt "!!!"
            mt "Мне нужно как-то отвлечь этого никчемного идиота от моей попы!"
            # Моника притворно улыбается ему
            music Hidden_Agenda
            imgf 34350
            m "..."
            m "Мистер Робертс..."
            m "У вашей плохой гувернантки Бетти сегодня настроение для кое-чего другого..."
            sound lick3
            imgd 34351
            m "Уверена, хозяину дома это очень понравится."
            # Ральф ведется, игриво спрашивает Монику
            ralph "Да?"
            ralph "Звучит заманчиво..."
            imgd 34352
            ralph "Что же ты хочешь предложить мне, Бетти?"
            # jump на начало меню с доступом ко всем пунктам (футджоб, титсджоб, минет, секс), кроме анала
            return False

    ## сделал немного подругому, потому что изначально они уже были в кровати и Моника раздета
    # Моника подходит к Ральфу
    fadeblack 1.5
    music Loved_Up
    imgfl 34353
    w
    imgf 34354
    w
    music Stealth_Groover
    imgd 34355
    mt "Не могу поверить, что я добровольно иду на ЭТО!"
    mt "Это все нереально! Какой-то сюр!"
    mt "На какие только жертвы тебе не приходится идти, Моника!"
    mt "!!!"
    imgd 34356
    mt "Но помни - все это временно!"
    mt "Настанет тот момент, когда все до единого ответят за свои грязные поступки!"
    mt "В том числе и этот мерзкий старикашка Ральф!"
    mt "Ненавижу! Всех! До единого!"
    mt "!!!"
    # трусики Моники падают на пол
    # довольный Ральф тянет к ней руку
#    label video_test:
    music Loved_Up
    imgf 34357
    ralph "Я так соскучился по своей гувернантке Бетти..."
    ralph "А ты скучала по мне?"
    # Моника тянет руку ему навстречу и притворно говорит
    m "Конечно, Мистер Робертс."
    # Моника садится на кровать рядом с Ральфом
    # он лезет к ней с поцелуями, она отвечает
    imgd 34358
    ralph "Мммм... Моя Бетти..."
    ## поменять фразу, так как она уже лиежит к нему попой
#    ralph "Повернись ко мне своей попкой."
    m "..."
    m "Все-таки я переживаю, Мистер Робертс..."
    m "А вдруг что-то пойдет не так?"
    imgd 34359
    ralph "Ничего не бойся, Бетти, я буду очень аккуратен."
    mt "Черт!"
    mt "!!!"
#    menu:
        ## тут сооветственно тоже надо поменять пункт (наверное)
#        "Сделать, как просит Ральф.":
#            pass
    # Моника встает в коленно-локтевую, Ральф сзади, целует ее ягодицы
    imgf 34360
    sound kiss1
    w
    imgd 34361
    w
    sound kiss1
    imgf 34362
    w
    sound kiss1
    imgd 34363
    ralph "Какая сладкая попка у моей гувернантки Бетти..."
    ralph "Да, такая гладкая и упругая."
    img 34364
    mt "Гребаный извращенец!"
    mt "!!!"
    # Ральф наклоянется и рассматривает ее анус
    # потом тянет руку и засовывает в попу Монике палец, водит им туда-сюда и смотрит
    imgf 34365
    w
    imgd 34366
    w
    sound hlup10
    imgd 34367
    w
    img 34369
    m "Ай!"
    ralph "Тсс, Бетти. Это всего лишь мой палец. Пока что..."
    imgf 34367
    w
    sound hlup10
    img 34368 hpunch
    ralph "Мммм..."
    if monicaBettyRalphAnal4 == 0:
        imgd 34367
        w
        sound hlup10
        imgd 34368
        ralph "Какая тугая девственная дырочка у моей Бетти..."
    if monicaBettyRalphAnal4 > 0:
        imgd 34367
        w
        sound hlup10
        imgd 34368
        ralph "Мне так нравится ласкать твою дырочку."
    imgf 34358
    ralph "Сейчас хозяин этого дома попробует ее своим членом."
    # Ральф вытаскивает из попы Моники палец и пристраивает к ее анусу свой член
    imgd 34370
    w
    img 34373
    mt "Черт! Черт!! Черт!!!"
    mt "!!!"
    # Ральф медленно начинает входить в ее анус
    imgd 34370
    w
    imgd 34371
    w
    sound chpok6
    img 34372 vpunch
    m "Ой, мне больно!"
    m "Ай-яй-яй!"
    img 34374
    m "Мистер Робертс! Может, не надо?"
    # он приостанавливает свое проникновение, но не выходит, гладит ее по ягодице
    imgd 34375
    ralph "Тише-тише, моя Бетти."
    ralph "Все хорошо, еще немного потерпи."
    ralph "Потом тебе понравится, вот увидишь."
    # снова начинает протискивать свой член в анус Моники
    imgf 34376
    w
    imgd 34377
    w

    # video
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_Ralph_Anal1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_1= Movie(play="video/v_Monica_Ralph_Anal1_1.mkv")
    show videov_Monica_Ralph_Anal1_1
    with fade
    ralph "О, какая же тугая дырочка!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34378
    w
    imgf 34379
    ralph "Оооо!"
    if monicaBettyRalphAnal4 == 0:
        ralph "Сразу видно, что в ней до меня никто не бывал!"
    if monicaBettyRalphAnal4 > 0:
        ralph "Сразу видно, что в ней бывает только член хозяина этого дома!"
    # если был анал с Филиппом
    if monicaBiffInvestorsPhilip2 > 0:
        #
        $ notif(_("У Моники был анальный секс с Филиппом."))
        #
        imgd 34379
        mt "Придурок!"
        mt "Видел бы ты, что со мной сделал гад Филипп в своем кошмарном подвале!"
        # если Моника сука
        if monicaBitch == True:
            $ notif_monica()
            imgd 34379
            mt "Сначала я оторву яйца ему, а потом и тебе, старикашка!"
            mt "!!!"
            #
    # Ральф вводит член в Монику до основания
    imgd 34376
    w
    sound drkanje5
    img 34380 vpunch
    m "АААА!!!"
    imgd 34381
    m "Мистер Робертс!"
    m "Это очень больно!"
    # Ральф начинает медленно двигаться вперед-назад
    # у Моники на лице гримаса боли периодически сменяется злостью
#    imgf 34378
#    w

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_2= Movie(play="video/v_Monica_Ralph_Anal1_2.mkv")
    show videov_Monica_Ralph_Anal1_2
    with fade
    ralph "Сейчас пройдет, моя Бетти."
    ralph "Потерпи немного."
    wclean
    ralph "Мммм... Как же здорово!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

#    sound drkanje5
    img 34382 vpunch
    w
    imgd 34383
    w

    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_3= Movie(play="video/v_Monica_Ralph_Anal1_3.mkv")
    show videov_Monica_Ralph_Anal1_3
    with fade
    mt "Моя попа!!!"
    mt "!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

#    sound drkanje5
    img 34384 vpunch
    w

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_4= Movie(play="video/v_Monica_Ralph_Anal1_4.mkv")
    show videov_Monica_Ralph_Anal1_4
    with fade
    ralph "Обожаю твою попку!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Ральф кайфует
    imgf 34385
    ralph "Моя Бетти! Оооо!"

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_5= Movie(play="video/v_Monica_Ralph_Anal1_5.mkv")
    show videov_Monica_Ralph_Anal1_5
    with fade
    ralph "Мммм..."
    ralph "Даааа..."
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
    image videov_Monica_Ralph_Anal1_6= Movie(play="video/v_Monica_Ralph_Anal1_6.mkv")
    show videov_Monica_Ralph_Anal1_6
    with fade
    mt "Когда же это все уже прекратится?!"
    mt "Это отвратительно!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34386
    w

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_7= Movie(play="video/v_Monica_Ralph_Anal1_7.mkv")
    show videov_Monica_Ralph_Anal1_7
    with fade
    ralph "Моя гувернантка Бетти радует хозяина этого дома все больше и больше!"
    ralph "Ты не стала меня расстраивать отказом."
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
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal1_8= Movie(play="video/v_Monica_Ralph_Anal1_8.mkv")
    show videov_Monica_Ralph_Anal1_8
    with fade
    ralph "Ты самая лучшая, моя Бетти!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # если Моника сказала Ральфу, что ей нужны деньги
    if monicaBettyRalphSeduction8 == True:
        imgd 34387
        mt "Да, жадный старикашка!"
        mt "Я сделаю так, чтобы ты готов был отдать мне все свои деньги!"
        mt "Хватит с меня сомнительных источников дохода!"
    # если Моника сказала Ральфу, что любит его
    else:
        imgd 34387
        mt "Да, мерзкий старикашка!"
        mt "Я сделаю все, чтобы вышвырнуть эту тупую провинциалку и вернуть свой дом!"
        mt "А следом за ней я вышвырну отсюда и тебя вместе с твоим противным малявкой!"
    #
    # Ральф выходит из Моники
    imgf 34372
    w
    sound chpok6
    img 34370
    w
    imgf 34353
    ralph "Садись на меня сверху, Бетти."
    ralph "Я войду в твою тугую дырочку..."
    ralph "И буду смотреть на твое прекрасное личико."
    imgd 34355
    mt "Твою мать!"
    mt "Он еще растягивает удовольствие!"
    mt "Придурок!"
    mt "!!!"
    menu:
        "Сделать, как просит Ральф.":
            pass
    imgd 34357
    m "Конечно, Мистер Робертс..."
    # Ральф ложится на кровать, Моника садится сверху него
    # член Ральфа вводит в анус
    # при этом Моника морщится от боли, а Ральф балдеет
    fadeblack 2.0
    music Loved_Up
    imgfl 34388
    w
    imgf 34389
    w
    imgd 34390
    w
    imgd 34391
    w
    imgf 34392
    w
    sound chpok6
    img 34393 vpunch
    ralph "Ммммм..."
    imgd 34394
    ralph "Оооох, Бетти!"
    imgf 34395
    ralph "Какая твоя попка упругая! Да!"
    # Моника смотрит на него с притворной игривостью
    imgd 34396
    mt "Мне надоело с ним возиться!"
    mt "Нужно сделать так, чтобы этот идиот скорее кончил и отстал от меня!"
    imgf 34397
    w
    imgd 34398
    mt "И от моей попы!"
    mt "!!!"
    imgf 34399
    w

    # video
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_Ralph_Anal2_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_1_25= Movie(play="video/v_Monica_Ralph_Anal2_1_25.mkv")
    show videov_Monica_Ralph_Anal2_1_25
    with fade
    m "Вам нравится, Мистер Робертс?"
    wclean
    ralph "Ммммм, даааа..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Loved_Up2
    imgd 34400
    ralph "Оооох..."

    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_2_25= Movie(play="video/v_Monica_Ralph_Anal2_2_25.mkv")
    show videov_Monica_Ralph_Anal2_2_25
    with fade
    ralph "О, Беттииии..."
    ralph "Ты самая лучшая!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34401
    ralph "Я хочу заниматься этим каждый день!"
    imgf 34402
    w

    #3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_3_25= Movie(play="video/v_Monica_Ralph_Anal2_3_25.mkv")
    show videov_Monica_Ralph_Anal2_3_25
    with fade
    ralph "Какая горячая и тугая дырочка! Дааа!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34403
    w

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_4_25= Movie(play="video/v_Monica_Ralph_Anal2_4_25.mkv")
    show videov_Monica_Ralph_Anal2_4_25
    with fade
    ralph "И трахать свою плохую гувернантку..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34404
    w

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_5_25= Movie(play="video/v_Monica_Ralph_Anal2_5_25.mkv")
    show videov_Monica_Ralph_Anal2_5_25
    with fade
    ralph "Во все ее дырочки!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 34405
    w

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_6_25= Movie(play="video/v_Monica_Ralph_Anal2_6_25.mkv")
    show videov_Monica_Ralph_Anal2_6_25
    with fade
    ralph "Я вижу, как тебе нравится, когда член хозяина дома в твоей попке, Бетти!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34407
    ralph "Дааа!"
    ralph "Как же здорово!!! Ооооо!"
    imgd 34408
    w

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_7_25= Movie(play="video/v_Monica_Ralph_Anal2_7_25.mkv")
    show videov_Monica_Ralph_Anal2_7_25
    with fade
    ralph "Оооо!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 34409
    w

    #8
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Ralph_Anal2_8_25= Movie(play="video/v_Monica_Ralph_Anal2_8_25.mkv")
    show videov_Monica_Ralph_Anal2_8_25
    with fade
    ralph "Ааааа!"
    ralph "АААА!!!"
    wclean
    ralph "Я сейчас кончу, Бетти!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    menu:
        "Кончить на киску Моники.":
            $ monicaBettySexRalph_cumzone = 1
            # Моника приподнимается и Ральф кончает на ее киску
            imgf 34407
            w
            sound drkanje5
            img 34408 vpunch
            ralph "Бетти!"
            img 31688
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            ralph "Ооооо!!"
            img 31689
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            ralph "ООООООООО!!!"
            # Моника смотрит на Ральфа
            # он прибалдевший смотрит на нее
            imgd 34410
            mt "!!!"
            pass
        "Кончить в попу Моники.":
            $ monicaBettySexRalph_cumzone = 2
            imgf 34407
            w
            sound drkanje5
            img 34408 vpunch
            ralph "Бетти!"
            img 34407
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            img 34406
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            ralph "Ооооо!!"
            sound chpok6
            imgd 34411
            ralph "ООООООООО!!!"
            # Моника смотрит на Ральфа
            # он прибалдевший смотрит на нее
            imgd 34410
            mt "!!!"
            pass
    # затемнение
    # Моника с Ральфом лежат в обнмку в постели
    fadeblack 2.0
    music Groove2_85
    imgfl 31584
    w
    imgf 34412
    ralph "Бетти, это было восхитительно!"
    ralph "Тебе понравилось?"
    imgd 31581
    mt "Кошмарно!!!"
    mt "!!!"
    # Моника притворно
    imgd 34412
    m "Мне очень понравилось, Мистер Робертс..."
    ralph "Как себя чувствует твоя попка?"
    imgd 31581
    mt "Дьявол! Моя попа горит!"
    imgf 31582
    m "Мне больно... Но совсем немного..."
    ralph "В следующий раз будет не так больно, Бетти."
    music Stealth_Groover
    imgd 34413
    mt "!!!"
    mt "Так, Моника. Пока этот мешок с костями лежит в эйфории..."
    mt "Тебе нужно использовать этот момент!"
    # если Моника сказала Ральфу, что ей нужны деньги
    if monicaBettyRalphSeduction8 == True:
        imgd 34414
        mt "Возможно, я смогу сделать так, что он заплатит мне не $ 300, а намного больше..."
        music Hidden_Agenda
        imgf 31585
        m "Мистер Робертс..."
        ralph "Да, Бетти?"
        m "Я же порадовала вас сегодня своим согласием..."
        if monicaBettyRalphAnal4 == 0:
            m "И это было у меня впервые."
        m "Мне было очень страшно, Мистер Робертс."
        m "Но ради вас я пошла на этот шаг..."
        imgd 31589
        ralph "Да, Бетти. Я очень ценю это..."
        ralph "Ты хотела что-то попросить у меня?"
        ralph "Я дам тебе, как обычно, $ 200 и добавлю еще сто, как и обещал."
        ralph "Вот твои $ 300, Бетти."
        $ add_money(300.0)
        menu:
            "Попросить у Ральфа еще денег.":
                pass
        imgf 31587
        m "Может быть, Мистер Робертс даст мне еще немного денег?"
        ralph "Обещаю, что в следующий раз я тебе тоже доплачу за это."
        ralph "Несмотря на то, что это будет не в первый раз для нас..."
        # чмокает ее в щечку, Моника притворно улыбается ему
        music Pyro_Flow
        img 31588
        mt "Мерзкий жадный старикашка!"
        mt "!!!"
        #
    # если Моника сказала Ральфу, что любит его
    else: # может, сделать это пунктом меню из лейбла ep214_dialogues5_bardie_ralph_16 - "Предложить Ральфу узаконить наши отношения"-?
        imgd 34414
        mt "Нужно сделать так, чтобы этот мерзкий Ральф понял, что я лучше его провинциалки!"
        music Hidden_Agenda
        imgf 31585
        m "Мистер Робертс..."
        ralph "Да, Бетти?"
        m "Я же порадовала вас сегодня своим согласием..."
        if monicaBettyRalphAnal4 == 0:
            m "И это было у меня впервые."
        m "Мне было очень страшно, Мистер Робертс."
        m "Но ради вас я пошла на этот шаг..."
        imgd 31589
        ralph "Да, Бетти. Я очень ценю это..."
        m "Мистер Робертс, вы сказали, что я самая лучшая... Вы правда так думаете?"
        ralph "Да, Бетти. Мне очень нравится проводить с тобой время."
        # Моника притворно огорчается
        imgf 34415
        m "Мне тоже с вами очень нравится. Жаль, что мы не можем быть с вами каждый день..."
        m "Как было бы хорошо ни от кого не прятатся и не скрывать наши с вами чувства, Мистер Робертс..."
        m "Мы могли бы целоваться и обниматься в любой момент и в любом месте..."
        imgd 34416
        m "И не только целоваться и обниматься..."
        m "Я хотела бы делать ЭТО с вами везде, а не только в этой спальне."
        m "В этом доме есть столько интересных мест, Мистер Робертс." # игриво
        ralph "Звучит очень заманчиво, Бетти."
        ralph "Ты знаешь, я тоже хотел бы этого."
        imgf 31587
        m "Возможно, я могла бы быть для вас первой Бетти, Мистер Робертс..."
        # Ральф задумчиво чешет лысину и смотрит на Монику
        ralph "Хммм..."
        m "Я вас люблю, Мистер Робертс. И не хочу делить ни с кем..."
        m "Я хочу, чтобы вы были только со мной."
        ralph "Бетти..."
        sound Jump2
        img 34417 hpunch
        m "Не торопитесь мне сейчас давать ответ, Мистер Робертс."
        m "Но помните, что я страдаю каждый раз, когда вижу вас с вашей женой."
        m "И мечтаю быть на ее месте..."
        imgd 34418
        ralph "Моя Бетти, я подумаю, как нам дальше быть..."
        m "Обещаете, Мистер Робертс?"
        ralph "..."
        m "..."
        ralph "Да, Бетти. Обещаю."
        # Моника радостно смотрит на него
        music Stealth_Groover
        imgd 34419
        mt "Да, мерзкий старикашка! Ты попался!!!"
        mt "Скоро, Моника! Совсем скоро!"
        mt "Ты сможешь вернуть свой дом!"
        mt "!!!"
        imgf 31590
        sound kiss2
        w
        # Моника радостно тянется к нему, целует
    $ monicaBettyRalphAnal4 = day # у Моники и Ральфа состоялся первый анал
    return

# если Моника взяла у Ральфа деньги, мысли
label ep219_dialogues1_ralph_4:
    # не рендерить!!
    mt "300 долларов!"
    mt "За то, что мне пришлось вытерпеть его мерзкий отросток в моей попе!"
    mt "Какой кошмар, Моника!"
    mt "Как ты могла согласиться на подобное?!"
    mt "Что с тобой такое творится?!"
    mt "?!?!?!"
    return

# если Моника намекнула Ральфу на его с Бетти развод, мысли
label ep219_dialogues1_ralph_5:
    # не рендерить!!
    mt "Моника, ты сделала это!"
    mt "Этот никчемный неудачник теперь задумается о разводе со своей провинциальной дурой!"
    mt "Правда, для этого мне пришлось пожертвовать своей попой..."
    mt "Черт! Это было ужасно!"
    mt "Но я... Я готова пожертвовать даже этим, чтобы вернуть назад то что у меня отняли!"
    mt "Место хозяйки этого дома уже почти МОЕ!"
    mt "!!!"
    return
