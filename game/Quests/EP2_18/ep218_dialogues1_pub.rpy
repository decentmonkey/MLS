default monicaStripNudeClare1 = 0 # Клэр полностью разделась на сцене
default monicaAshleyBerkelbauch1 = 0 # Моника пошла на 3-й приват с банкиром
default monicaAshleyBerkelbauch2 = 0 # Моника отказалась танцевать перед банкиром
default monicaAshleyBerkelbauch3 = 0 # Моника отказалась удавлетворять банкира
default monicaAshleyBerkelbauch4 = 0 # Моника согласилась на минет банкиру
default monicaAshleyBerkelbauch5 = 0 # Моника согласилась на секс с банкиром
default monicaAshleyBerkelbauch6 = 0 # Эшли согласилась на секс с банкиром

default monicaAshleySexBerkelbauch_cumzone = 0

define monicaAshleyBerkelbauchCorruptionRequired1 = 700 # Моника пошла на 3-й приват с банкиром
define monicaAshleyBerkelbauchCorruptionRequired2 = 720 # Моника согласилась танцевать для банкира
define monicaAshleyBerkelbauchCorruptionRequired3 = 790 # Моника согласилась удовлетворить банкира
define monicaAshleyBerkelbauchCorruptionRequired4 = 790 # Моника согласилась на минет банкиру
define monicaAshleyBerkelbauchCorruptionRequired5 = 850 # Моника согласилась на секс с банкиром

define v_Monica_Banker_Blowjob1_1_sound_name = "v_Monica_Banker_Blowjob1_1"
define v_Monica_Banker_Sex1_1_sound_name = "v_Monica_Banker_Sex1_1"
define v_Monica_Banker_Sex1_1b_sound_name = "v_Monica_Banker_Sex1_2"
define v_Ashley_Banker_Blowjob1_1_sound_name = "v_Ashley_Banker_Blowjob1_1"
define v_Ashley_Banker_Sex1_1_sound_name = "v_Ashley_Banker_Sex1_1"

#call ep218_dialogues1_pub_1() # разговор с Клэр в гримерке до ее выступления
#call ep218_dialogues1_pub_2() # танец Клэр
#call ep218_dialogues1_pub_3() # разговор с Клэр в гримерке после ее выступления
#call ep218_dialogues1_pub_4() # гримерка, разговор с Эшли перед приватом
#call ep218_dialogues1_pub_5() # подсобка барменов, приват Моники для банкира
#call ep218_dialogues1_pub_6() # подсобка барменов, приват Эшли для банкира
#call ep218_dialogues1_pub_6a() # если Моника ушла с привата, Эшли с банкиром
#call ep218_dialogues1_pub_7() # разговор Моники и Эшли, если Моника ушла с привата
#call ep218_dialogues1_pub_8() # разговор Моники и Эшли, если Моника удовлетворила банкира


# при условии, что у Молли был приват с Джо и он разрешил Клэр остаться и танцевать в маске
# Моника приходит в гримерку, работает Клэр
# Моника в одежде шлюхи
label ep218_dialogues1_pub_1:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    if monicaStripNudeClare1 == 0:
        imgfl 40765
        w
        imgf 40769
        mt "Хорошо, что сегодня работает Клэр..."
        mt "Надо бы спросить у нее, что она решила по поводу ухода из этой дыры."
        mt "Уверена, что она не согласится на те условия, которые озвучил Джо."
        mt "Такие порядочные девушки, как она, не станут раздеваться на сцене!"
        mt "А я..."
        imgd 40770
        mt "То, что сделала я - это исключение. Это не считается!"
        mt "Конечно, мне будет немного грустно, если она уйдет..."
        imgd 40771
        mt "Тем более, что я устроила такую прекрасную партию игры этими глупыми человечишками."
        mt "Но, нужно признаться, я получила от этого немалое удовольствие."
        mt "..."
        imgf 16142
        m "Клэр, привет..."
        # Клэр поворачивается к Монике
        music Groove2_85
        imgd 32862
        clare "Привет, Моника!"
        clare "Я как раз вспоминала тебя!"
        sound highheels_short_walk
        imgf 16150
        clare "Слушай, я хотела у тебя спросить..."
        clare "Тот день, когда ты впервые полностью разделась на сцене..."
        clare "Как это было? Что ты при этом чувствовала?"
        # Моника растерянно
        imgd 16151
        m "Я? Ну..."
        m "Мягко говоря, я чувствовала себя немного неловко."
        m "Все эти пошлые крики из зала..."
        m "Я буквально кожей ощущащала их липкие, грязные взгляды!"
        m "Особенно, когда... Сняла трусики."
        m "Это отвратительно!"
        imgf 42765
        clare "Хм..." # задумчиво
        imgd 42766
        m "А почему ты спрашиваешь, Клэр?"
        imgd 16165
        clare "Я подумываю все-таки попробовать сделать этот эксперимент..."
        clare "Конечно, для меня это также, как и для тебя, неприемлемо."
        clare "Но чем больше я об этом думаю, тем мне становится интереснее."
        clare "И я... Мне интересно, как это... Ощутить на себе все эти пошлые взгляды из толпы в тот момент..."
        clare "Когда я буду полностью обнажена."
        img 16144 vpunch
        m "Серьезно?!"
        m "Я сделала это не по своей воле. Меня заставила Эшли."
        m "С подачи этой рыжей сучки Молли!"
        m "А тебя это..."
        m "..."
        imgd 42767
        clare "Заводит... Сама мысль об этом."
        clare "Поэтому я думаю, что мне нужно как минимум один раз сделать это."
        clare "Просто попробовать."
        clare "И решить для себя окончательно, оставаться здесь и танцевать на сцене..."
        clare "Или искать себе другое место для моего, так сказать, творчества, моего хобби."
        music Stealth_Groover
        m "Все-таки меня удивляет, Клэр, что тебе может нравится это..."
        # Клэр с улыбкой
        imgf 16157
        clare "Почему?"
        imgd 16168
        m "Ты такая... Кажешься недоступной и строгой..."
        m "У тебя даже есть хлыст от извращенцев."
        imgd 42768
        clare "Ха-ха-ха! Он тебе нравится?"
        m "Да." # улыбается
        clare "Не представляю, как ты обходишься без такого хлыста, Моника!"
        # Моника и Клэр улыбаются друг другу
        # потом Клэр спрашивает у Моники

### если Моника откажет, то при следующей встрече с Клэр в гримерке, при клике на нее, разговор начнется с этого места
    music Groove2_85
    imgf 42769
    clare "Моника, ты же будешь не против, если я сегодня выступлю вместо тебя?"
    menu:
        "Согласиться.":
            $ monicaStripNudeClare1 = day # Клэр полностью разделась на сцене
            pass
        "Отказать Клэр.":
            imgd 16176
            mt "Я не могу пропустить свое выступление на сцене."
            mt "Мне нужны деньги, а танцуя на сцене я могу неплохо заработать."
            imgf 16172
            m "Клэр, я бы с радостью, но..."
            m "Давай ты сделаешь это в следующий раз?"
            m "Мне сегодня нужно выйти самой на сцену."
            imgd 16174
            clare "Да, Моника. Без проблем."
            clare "У меня как раз будет время еще раз все хорошо обдумать."
            # Клэр улыбается Монике и возвращается за свой столик
            return False
    # Моника задумчиво смотрит на Клэр (Клэр в это время может намазывааться маслом, уже собираясь на сцену)
    imgd 42770
    mt "Думаю, что стоит пропустить свое сегодняшнее выступление ради такого."
    mt "Надеюсь, что ей понравится и она примет решение не уходить из этой дыры."
    mt "Нет, мне, конечно, и одной здесь будет неплохо."
    imgd 42771
    mt "Я ведь здесь Королева, а не какая-нибудь дешевка, как Молли."
    mt "И еще я самая умная здесь... И красивая..."
    mt "Но все же, я уже привязалась к Клэр."
    mt "Она не похожа на всех остальных никчемных людишек, которые меня окружают..."
    imgf 42772
    m "..."
    m "Тебе так не терпится поэкспериментировать?"
    # Клэр улыбается загадочно
    imgd 42773
    clare "Да... Я хочу сейчас выйти на сцену."
    clare "В конце танца я оставлю на себе только маску..." # подмигивает
    sound Jump2
    img 42774
    w
    sound highheels_short_walk
    imgf 42775
    w
    # Клэр выходит из гримерки
    return True

# танец Клэр
# крики толпы из зала
label ep218_dialogues1_pub_2:
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

# сразу после выступления Клэр, в гримерке
# Моника в одежде шлюхи, Клэр без трусиков
label ep218_dialogues1_pub_3:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 42776
    w
    imgf 40767
    mt "А вот и Клэр..."
    mt "Интересно, какие у нее впечатления после танца полностью обнаженной?"
    sound highheels_short_walk
    imgd 42777
    m "Клэр, привет..."
    # Клэр поворачивается к Монике
    imgf 42778
    clare "Привет, Моника!"
    m "Как прошло твое выступление?"
    clare "Это было потрясающе, Моника!"
    # Моника удивленно на нее смотрит
    music stop
    sound plastinka1b
    img 42779 hpunch
    m "?!"
    m "Потрясающе?!"
    music Stealth_Groover
    imgd 42780
    clare "Да!"
    clare "Я помню свое первое выступление на сцене."
    clare "Я тогда испытала такую гамму эмоций!"
    clare "Смущение, волнение... И меня это заводило..."
    clare "Выходя на сцену каждый раз после этого, я хотела испытать это снова."
    clare "И каждый раз мне было прикольно, но не так, как в самый первый раз."
    clare "Но когда я сняла трусики на сцене..."
    imgd 42781
    clare "Меня захватила такая волна эмоций!"
    clare "Я чуть было не сняла с себя маску!"
    clare "Ха-ха! Опомнилась в последний момент, представляешь?!"
    clare "Моника, у меня давно такого не было!"
    clare "Я с удовольствием выйду на сцену еще раз и разденусь."
    clare "Ведь это так... Возбуждает..."
    # Моника удивлена таким подробностям
    music Groove2_85
    imgf 42782
    mt "Странно..."
    mt "Звучит как-то... По-извращенски."
    mt "Как можно испытывать удовольствие от такого?!"
    mt "?!"
    mt "Но с другой стороны..."
    mt "Мне какая разница?"
    imgd 42783
    mt "Главное, что Клэр остается здесь."
    mt "А значит моя гениальная актерская игра перед никчемными обитателями этой дыры не была напрасной."
    imgf 42784
    m "Клэр, я рада, что тебе понравилось."
    m "И что ты останешься здесь."
    imgd 42785
    clare "Да, Моника, я тоже рада."
    clare "Спасибо тебе за то, что ты помогла мне и поддержала меня."
    clare "Помни, что ты в любой момент можешь обратиться ко мне, если у тебя возникнут трудности."
    imgf 42786
    m "Спасибо, Клэр."
    clare "Кстати, после выступления я не смогла найти свои трусики."
    clare "Их кто-то стащил прямо со сцены, представляешь?! Ха-ха!"
    m "Какой-нибудь извращенец!"
    clare "Ну и ладно. У меня есть точно такие же."
    imgd 42787
    w
    imgd 42788
    w
    # они улыбаются дрг другу
    # Клэр возвращается на свое место, Моника подходит к вешалке
    sound highheels_short_walk
    imgf 42789
    w
    music Stealth_Groover
    imgd 42790
    mt "Не думаю, что у меня могут возникнуть какие-либо трудности!"
    mt "Я Королева Shiny Hole!"
    mt "А все остальные - глупые и никчемные человечишки!"
    mt "Мне ничего не стоит поставить любого из них на место!"
    mt "!!!"
    return

# на следующий рабочий день
# после того, как Моника возвращается со сцены в гримерку заходит Эшли
# Монка в сценическом костюме
label ep218_dialogues1_pub_4:
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgf 33945
    w
    imgd 33944
    mt "Этой извращенке снова что-то от меня нужно!"
    mt "Как же она меня достала!"
    mt "!!!"
    # Эшли подходит к Монике, заигрывая
    music Loved_up
    sound2 man_steps
    imgf 33946
    ashley "[monica_pub_name]..."
    ashley "Ты сегодня как никогда хороша..."
    imgd 33947
    ashley "Я смотрела на твое выступление и представляла, что ты танцуешь только для меня."
    # запускает руку Монике в трусики и гладит ее киску
    sound Jump2
    img 33948 vpunch
    ashley "У меня даже стало влажно между ног."
    mt "Фууу!"
    mt "Избавь меня от этих гадких подробностей, извращенка!"
    mt "Я и так с трудом терплю твои грязные домогательства!"
    mt "!!!"
    sound Jump1
    img 33949 hpunch
    ashley "Так хочется уединиться с тобой в подсобке..."
    ashley "И чтобы нас никто не беспокоил."
    imgf 33950
    ashley "Сесть на диван и смотреть, как ты танцуешь для меня абсолютно голенькая."
    ashley "И раздвигаешь свои ножки, чтобы я получше рассмотрела твою киску."
    ashley "Да... Повезло сегодня Мистеру Беркельбауху..."
    ashley "Мне остается только завидовать ему..."
    music stop
    sound plastinka1b
    img 33951 hpunch
    mt "?!?!?!"
    music Pyro_Flow
    m "В смысле, ему повезло?! С чем?!"
    m "Причем здесь этот банкиришка?!"
    m "!!!"
    # Эшли убирает руку
    music Groove2_85
    imgd 33952
    ashley "Так, [monica_pub_name]. Я тебя просила не называть его так!"
    ashley "Я тебе уже говорила, что Мистер Беркельбаух уважаемый человек!"
    ashley "И он очень помогает мне в развитии моего бара!"
    m "А я здесь причем?!"
    ashley "Притом, что Мистер Беркельбаух ждет тебя в подсобке, [monica_pub_name]!"
    imgd 33953
    ashley "Ты знаешь, что меня с ним связывают деловые отношения."
    ashley "И он оказывает мне помощь в вопросах финансов."
    ashley "И я не могу отказать ему, если он просит устроить ему приват с Королевой Shiny Hole!"
    ashley "Поэтому давай, [monica_pub_name], тащи свою королевскую попку в подсобку!"
    ashley "Он уже ждет!"
    img 40869
    m "!!!"
    menu:
        "Сколько он заплатит за это?":
            pass
    music Stealth_Groover
    imgf 33954
    m "Эшли!"
    m "Я не собираюсь кривляться перед этим самодовольным козлом за бесплатно!"
    m "Почему я должна делать это?!"
    m "Вообще-то, я здесь Королева!"
    music Groove2_85
    imgd 33955
    ashley "Вообще-то, у королевы есть определенные ообязанности!"
    ashley "И сейчас одну из них ты должна исполнить!"
    ashley "Мистер Беркельбаух итак достаточно помогает мне с банковскими вопросами!"
    ashley "Поэтому ты сейчас же пойдешь и проведешь с ним приват!"
    imgd 33956
    ashley "Иначе я стану сомневаться, что ты, [monica_pub_name], достойна своей короны!"
    ashley "С Молли таких проблем никогда не было!"
    #
    $ notif(_("Моника подбросила Молли деньги и обвинила ее в воровстве."))
    #
    m "Вот только не надо сравнивать ее и МЕНЯ!"
    m "Она воровка и обманщица!"
    img 33957 vpunch
    ashley "[monica_pub_name], все, хватит!"
    ashley "Нельзя заставять долго ждать уважаемого Мистера Беркельбауха!"
    ashley "Пошли!"
    # Эшли отходит к выходу из гримерки
    imgd 33958
    mt "Черт!"
    $ menu_corruption = [0, monicaAshleyBerkelbauchCorruptionRequired1]
    menu:
        "Отказаться":
            # Моника высокомерно
            music Stealth_Groover
            imgd 33959
            mt "Нет!"
            mt "Я не собираюсь танцевать перед ним за бесплатно!"
            mt "Пошла эта гребаная Эшли к черту!"
            mt "Это же ей нужно договариваться с банкиром, а не мне!"
            mt "Вот пусть сама и кривляется перед ним!"
            mt "Дура!"
            mt "!!!"
            imgf 33960
            m "Нет, Эшли!"
            m "Я Королева и у меня есть привилегии!"
            m "Я не пойду на этот приват!"
            # Эшли зло на нее смотрит
            img 33961
            ashley "То есть ты отказываешься?"
            m "Отказываюсь!"
            ashley "Это неисполнение своих прямых королевских обязанностей, [monica_pub_name]!"
            ashley "Я тебе этого просто так не оставлю!"
            imgd 33962
            m "А что ты сделаешь?!"
            m "Ты не имеешь права лишать меня моего заработка!"
            m "Если ты это сделаешь, то я просто не приду больше сюда!"
            m "И эта твоя дыра, которую ты называешь баром, потеряет в выручке!"
            music Pyro_Flow
            img 33963 vpunch
            ashley "Тебе придется извиняться за этот твой поступок!"
            ashley "Иначе ты останешься без короны!"
            m "..."
            music Stealth_Groover
            imgf 40886
            mt "Мне плевать на ее угрозы!"
            mt "Она слишком тупая, чтобы сделать мне каую-то подлость!"
            music Power_Bots_Loop
            imgd 33964
            ashley "Сегодня я сама проведу переговоры с Мистером Беркельбаухом..."
            ashley "Но если ты еще раз откажешься от исполнения своих обязанностей!"
            ashley "Я тебя накажу!"
            ashley "Тебе все понятно, [monica_pub_name]!?"
            m "Да!"
            # Эшли зло смотрит на Монику и уходит
            jump ep218_dialogues1_pub_6
        "Пойти на приват.":
            $ monicaAshleyBerkelbauch1 = day # Моника пошла на 3-й приват с банкиром
            pass
    music Stealth_Groover
    imgf 33959
    mt "Почему Я, Королева, должна обслуживать какого-то козла?!"
    mt "С другой стороны, мне совсем не нравится, что эта дура Эшли намекает, что Молли королева, а не Я!"
    mt "Как вообще можно сравнивать нас?!"
    mt "Нет! Я не оставлю ни единого шанса этой рыжей шлюхе вернуть себе корону Shiny Hole!"
    mt "Даже если мне придется терпеть этого никчемного банкира!"
    # Моника делает шаг к Эшли, чтобы пойти с ней в подсобку
    music Groove2_85
    sound2 highheels_short_walk
    imgd 33965
    ashley "И без глупостей, [monica_pub_name]!"
    ashley "Я лично буду контролировать, чтобы Мистер Беркельбаух остался доволен этим приватом!"
    ashley "Это очень важно!"
    ashley "Поняла меня, [monica_pub_name]?"
    music Loved_up
    imgd 33966
    ashley "Иначе я отшлепаю тебя по твоей королевской попке!" # подмигивает
    mt "Да пошла ты! Мерзкая извращенка!"
    mt "!!!"
#    return

# подсобка барменов
# банкир сидит на диване, Эшли и Моника заходят в подсобку
label ep218_dialogues1_pub_5:
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
    $ menu_corruption = [monicaAshleyBerkelbauchCorruptionRequired2, 0]
    menu:
        "Залезть на стол.":
            pass
        "Не делать этого!":
            $ monicaAshleyBerkelbauch2 = day # Моника отказалась танцевать перед банкиром
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
            jump ep218_dialogues1_pub_6a
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
    $ menu_corruption = [monicaAshleyBerkelbauchCorruptionRequired3, 0]
    menu:
        "Сделать, как говорит Эшли.":  # коррапшн
            # Моника поворачивается и смотрит на Эшли с возмущением
            music Groove2_85
            img 34003 vpunch
            m "Эшли!"
            ashley "[monica_pub_name]!!!"
            ashley "Чего ты на меня смотришь?!"
            ashley "Тебе же ясно сказали, что нужно делать!"
            ashley "Выполняй!"
            img 34004
            mt "!!!"
            $ menu_corruption = [monicaAshleyBerkelbauchCorruptionRequired4, monicaAshleyBerkelbauchCorruptionRequired5]
            menu:
                "Минет (in Extra version) (disabled)." if game.extra == False:
                    pass
                "Минет." if game.extra == True:
                    $ monicaAshleyBerkelbauch4 = day # Моника согласилась на минет банкиру
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
                            $ monicaAshleySexBerkelbauch_cumzone = 1
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
                            $ monicaAshleySexBerkelbauch_cumzone = 2
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
                    $ monicaAshleyBerkelbauch5 = day # Моника согласилась на секс с банкиром
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
                            $ monicaAshleySexBerkelbauch_cumzone = 3
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
                            $ monicaAshleySexBerkelbauch_cumzone = 4
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
            $ monicaAshleyBerkelbauch3 = day # Моника отказалась удовлетворять банкира
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
            jump ep218_dialogues1_pub_6a
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
    return True

# подсобка барменов
# спустя несколько минут
# банкир сидит на диване, Эшли заходит в подсобку одна, без Моники
label ep218_dialogues1_pub_6:
    # банкир смотрит недовольно
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 34075
    w
    imgf 34076
    banker "Эшли..."
    ashley "Да, Мистер Беркельбаух?"
    banker "Я так долго ждал Королеву Shiny Hole и где же она?"
    banker "Мне придется еще ждать?"
    imgd 34077
    banker "Ты же знаешь, Эшли, мне это не нравится."
    banker "Я трачу свое время здесь, а мое время дорого стоит."
    # Эшли смущенно
    music Hidden_Agenda
    imgf 34078
    ashley "Мистер Беркельбаух, у нашей королевы..."
    ashley "В общем, она не смогла прийти."
    ashley "Попросила передать вам свои извинения и..."
    ashley "И сказала, что очень сожалеет, что не смогла прийти к вам..."
    music Groove2_85
    imgd 34079
    banker "Очень плохо, Эшли."
    banker "Я взамен на свою помощь прошу немногого..."
    banker "Всего лишь вечер с лучшей девочкой этого бара."
    banker "А ты мне не то что лучшую девочку, ты мне вообще никого не привела сюда."
    imgd 34080
    ashley "Мистер Беркельбаух, извините!"
    ashley "А хотите, мы перенесем этот приват на другой день?"
    ashley "И я устрою вам приват со всеми девочками? Как в прошлый раз?"
    banker "Мне это уже не интересно, Эшли..."
    banker "Я занятой человек и не могу проводить столько времени в баре."
### отсюда начало, если Моника отказалась от минета
label ep218_dialogues1_pub_6a:
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
            $ monicaAshleyBerkelbauch6 = day # Эшли согласилась на секс с банкиром
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
            call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_25
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
            return False
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
            $ monicaAshleySexBerkelbauch_cumzone = 5
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
            $ monicaAshleySexBerkelbauch_cumzone = 6
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
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_26
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
    return False

# разговор Моники и Эшли, если минет банкиру делала Эшли (Моника ушла с привата)
# возле барной стойки, Джо нет рядом
label ep218_dialogues1_pub_7:
    # Эшли орет на Монику, та стоит с невозмутимым королевским видом
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Pyro_Flow
    music2 pub_noise1_low
    img 42791 vpunch
    ashley "[monica_pub_name]!"
    m "Что, Эшли?"
    ashley "То, как ты себя повела при Мистере Беркельбаухе - это непозволительно!"
    imgd 40730
    m "А что я такого сделала?!"
    m "!!!"
    img 42792 hpunch
    ashley "Ты издеваешься, [monica_pub_name]?!"
    ashley "Ты серьезно думаешь, что если ты здесь Королева, то тебе все позволено?!"
    imgd 40737
    m "Я Королева и у меня есть привилегии!"
    img 42793
    ashley "В первую очередь, ты должна выполнять свои королевские обязанности!"
    ashley "А потом уже думать о привилегиях! Тем более, пользоваться ими и задирать свой нос!"
    ashley "Ты постоянно пользуешься тем, что я хорошо к тебе отношусь!"
    ashley "Но всему есть предел, [monica_pub_name]!"
    imgf 40735
    m "..."
    imgd 42794
    ashley "Если ты не будешь выполнять свои обязанности, то не будешь Королевой! Ею станет Молли!!!"
    ashley "И после того, как ты себя повела на привате с Мистером Беркельбаухом..."
    ashley "Я начинаю задумываться о том, что настоящая Королева тут не ты, а Молли!"
    ashley "Она никогда не создавала мне подобных проблем с клиентами!!!"
    ashley "Тебе все понятно?!"
    # Моника с недовольным видом
    imgd 42795
    m "..."
    m "Да!"
    music Stealth_Groover
    sound2 highheels_short_walk
    imgf 42796
    mt "Да пошла ты вместе со своей Молли!"
    mt "Королева здесь одна! Это Я!"
    mt "А вы все - жалкие никчемные человечешки!"
    mt "Глупые и ничего не значащие!"
    mt "!!!"
    music2 stop
    fadeblack 2.0
    return

# разговор Моники и Эшли, если минет банкиру делала Моника
# возле барной стойки, Джо нет рядом
label ep218_dialogues1_pub_8:
    # Эшли игриво смотрит на Монику
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgf 40783
    ashley "[monica_pub_name]..."
    ashley "Я, кажется, не разрешала тебе трахаться с клиентами..."
    # Моника возмущенно
    img 40784 vpunch
    m "В смысле?!"
    m "?!"
    m "Ты же сама заставила меня сделать ЭТО!!!"
    m "!!!"
    # подмигивает ей
    imgf 40792
    ashley "Ладно-ладно, [monica_pub_name]... Теперь я разрешаю тебе удовлетворять клиентов."
    ashley "Ты так хорошо поработала своей королевской попкой!"
    ashley "Мистер Беркельбаух доволен тобой."
    music Stealth_Groover
    imgd 40782
    m "Еще бы! Я и не сомневалась!"
    m "Он о такой, как Я, даже мечтать не мог!"
    m "И Эшли, это было в первый и последний раз, ты слышишь?!"
    music Loved_up
    imgf 40736
    ashley "Ты очень хорошая Королева, [monica_pub_name]."
    ashley "Мне нравится, как ты исполняешь свои королевские обязанности."
    ashley "Не забывай и дальше их исполнять."
    # пошло подмигивает
    sound Jump2
    imgd 40731
    ashley "Они у тебя еще будут."
    imgd 40730
    m "..."
    music Stealth_Groover
    sound2 highheels_short_walk
    imgf 40738
    mt "Вот еще!"
    mt "С меня хватило этого мерзкого банкиришки!"
    mt "Больше никаких обязанностей!"
    mt "Только королевские привилегии!"
    mt "Ведь я это заслужила!"
    music2 stop
    fadeblack 2.0
    return
