label gallery_43538:
    # смена кадра, Моника заходит на темную лестничную площадку, про себя ворчит
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 street13_ambulance
    imgf 43513
    mt "О, Боги!"
    mt "Каждый раз, когда захожу в этот подъезд - содрогаюсь!"
    mt "Такая леди, как Я, никогда не сможет привыкнуть к этой грязи! И вони! Фу!"
    imgd 43514
    mt "Этот отвратительный подъезд - идеальное место для какого-нибудь извращенца!"
    mt "Так, Моника, не задерживайся здесь!"
    mt "Быстрее иди в свои апартаменты!"
    # Моника делает шаг в сторону и тут из ниоткуда появляется незнакомец, его лица не видно в темноте
    # Моника орет от страха
    sound highheels_short_walk
    imgf 43515
    w
    music Malicious
    sound2 Jump1
    img 43516 vpunch
    sound snd_julia_scream1
    m "ААААА!!!"
    m "ААААААА!!!!!"
    # пытается удрать от него, но он хватает ее за руку
    sound snd_julia_scream1
    img 43517
    m "ОТПУСТИ МЕНЯ!!!"
    m "ААААА!!!"
    m "ПОМОГИТЕ!!!"
    # он говорит ей, отпуская ее руку
    imgd 43518
    citizen4 "Эй, детка. Тише ты!"
    citizen4 "Разоралась..."
    # Моника в ужасе смотрит на него, лица все еще не видит
    img 43519
    citizen4 "Зачем так кричать?"
    citizen4 "Тебя все равно тут никто не услышит."
    m "Ч-что тебе нужно?"
    imgd 43520
    citizen4 "Эй, ну ты чего так разнервничалась?"
    # он снова тянет к ней руку
#    sound Jump2
    img 43521 vpunch
    m "Не трогай меня!"
    m "Я вызову полицию!!!"
    # она снова пытается удрать
    # он ее хватает за руки и выходит из тени
    imgd 43522
    citizen4 "Когда ты отсасывала у меня возле пилона, ты была намного сговорчивее!"
    # на лице Моника страх и ужас сменяется на гнев
    music stop
    sound plastinka1b
    img 43523 hpunch
    m "Что?!"
    music Pyro_Flow
    m "ТЫ?!"
    m "Ах ты идиот! Кретин!"
    # толкает его со злостью
    imgd 43524
    m "Какого черта ты тут делаешь?!"
    music Groove2_85
    citizen4 "Жду тебя, детка!"
    m "Чего тебе нужно от меня?!"
    m "И вообще! Как ты узнал, где я живу?!"
    # он смеется
    # если Моника водила панков к себе домой
    if monicaCitizensPunksBlowjob1 == True:
        #
        $ notif(_("Моника водила в свои апартаменты Тима и Тома."))
        #
        imgf 43525
        citizen4 "Тут два чувака всем на районе тебя рекомендуют, детка!"
        citizen4 "Подгоняют тебе клиентов! Ха-ха!"
        citizen4 "Смотри, скоро у тебя тут очередь будет."
        music Power_Bots_Loop
        img 43526
        m "Рекомендуют?!"
        m "Да я их!.."
        music Groove2_85
        imgd 43527
        citizen4 "Да ладно, остынь."
        imgd 43528
        mt "Два никчемных недоумка!"
        mt "Зачем я вообще с ними связалась!"
        img 43529
        m "Что значит остынь?!"
        m "Это все наглая ложь!"
        m "Ничего не было!"
        citizen4 "Ну конечно, не было. Ха-ха-ха!"
    # если пила с Василием у себя в апартаментах
    if monicaCitizens14Slums1 == True:
        #
        $ notif(_("Моника употребляла алкоголь с Василием за деньги."))
        #
        imgf 43530
        citizen4 "И с Василием ты тоже не бухала, да?"
        citizen4 "Ха-ха-ха!"
        imgd 43531
        m "!!!"
        m "С кем?!"
        m "Я не понимаю, что за бред ты несешь?!"
        m "Я не знаю никакого Василия!"
        imgd 43532
        mt "Чертовы трущобные жители!"
        mt "Они что, всем все рассказали?!"
        mt "Безмозглые животные!"
        mt "Бесполезные существа!"
        mt "Насекомые!"
        mt "!!!"
        #
    music Groove2_85
    imgf 43533
    citizen4 "Давай сразу к делу, детка."
    citizen4 "В прошлый раз ты мне кое-что не доделала. Помнишь?"
    # Моника стоит, сложив руки на грузи, и зло на него смотрит
    m "..."
    imgd 43534
    citizen4 "Ну, чего молчим?"
    citizen4 "У тебя так много чуваков, которым ты сосешь возле пилона?"
    img 43535
    m "!!!"
    imgd 43536
    citizen4 "Даже если и так, то не каждый тебе предлагает сотку баксов за это."
    m "Чего тебе от меня нужно?!"
    citizen4 "Хочу, чтобы ты доделала свою работу..."
    citizen4 "Условия нашей сделки те же: отсасываешь у меня - получаешь $ 100."
    citizen4 "Ну что? Пошли в твою хату!"
    imgf 43537
    m "Я никуда с тобой не собираюсь идти за сто баксов!"
    # берет ее за руку и тянет в сторону ее двери
    sound Jump2
    img 43538 vpunch
    citizen4 "Окей. 130 баксов и ты мне отсасываешь."
    img 43539
    m "Черт!"
    m "!!!"
    # corruption
#    $ menu_corruption = [monicaCitizen4SexCorruptionRequired1, 0]
    menu:
        "Согласиться на его предложением.":
#            $ monicaCitizen4SlumsApartment1 = day # Моника в подъезде согласилась привести к себе незнакомца
            pass
        "Отказаться!":
            # Моника зло на него смотрит
            music Pyro_Flow
            imgf 43540
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            # Моника резко выдергивает свою руку
            imgd 43542
            m "НЕТ!!!"
            sound Jump1
            img 43543 hpunch
            m "Я не собираюсь заключать никакие сделки!!!"
            m "Тем более, с тобой!!!"
            imgd 43544
            m "Пошел вон отсюда!" # толкает его
            m "Еще раз увижу тебя здесь - позвоню в полицию!"
            m "Чертов извращенец!"
            sound highheels_short_walk
            imgf 43545
            w
            fadeblack
            sound highheels_short_walk
            pause 2.0
            sound snd_door_open1
            pause 1.5
            music2 stop
            # Моника уходит, затемнение, звук закрывающейся двери
            return
    # Моника в сомнениях смотрит на него
    music Groove2_85
    imgf 43540
    mt "Вот дьявол!"
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."
    #
    $ notif(_("Моника должна выплачивать Перри долг."))
    imgd 43540
    mt "Еще я должна выплачивать долг этой мерзкой извращенке Перри!"
    #
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 43540
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    imgd 43541
    mt "Моника, что же делать?"
    mt "Этот кретин сказал, что он заплатит $ 130..."
    mt "Хммм..."
    mt "В прошлый раз гребаная Перри застукала меня с этим никчемным неудачником..."
    mt "И я ничего не заработала из-за нее!"
    mt "Хотя мне пришлось брать его отвратительный член в свой рот!"
    mt "!!!"
    music Stealth_Groover
    mt "Если я соглашусь сейчас на его предложение, то никто не сможет мне помешать сделать ему..."
    mt "В общем, доделать это извращенство и получить, наконец-то, мои $ 130!"
    # Моника со злостью вырывает руку
    imgf 43542
    m "Отпусти меня!"
    sound Jump1
    img 43543 hpunch
    m "С проститутками в борделе будешь так обращаться!"
    m "Я тебе не какая-то там падшая особа!"
    # он смотрит на нее, еходно улыбаясь
    music Groove2_85
    imgf 43546
    citizen4 "Да? Ха-ха!"
    citizen4 "Ну окей, как скажешь."
    citizen4 "Только пошли уже скорее!"
    citizen4 "У меня уже яйца пухнут!"
### отсюда начнется, если отошьет в подъезде, но потом согласится привести к себе в др. день при клике на улице
    label gallery_42832:
    # затемнение, шаги, звук закрывающейся двери
    # смена кадра
    # апартаменты Моники
    # незнакомец стоит один в гостиной
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music2 stop
    music Groove2_85
    imgfl 42797
    citizen4 "Эй, детка! Ты где?"
    citizen4 "Мне долго еще ждать?!"
    # в гостиную заходит недовольная Моника в домашнем аутфите
    sound snd_walk_barefoot
    imgf 42798
    m "Я здесь!"
    m "И незачем так орать! Это неприлично!"
    imgd 42799
    citizen4 "О, нормальный прикид."
    imgd 42800
    citizen4 "А то всегда вижу тебя в одном и том же."
    # расстегивает штаны и достает свой стояк
    imgf 42801
    w
    sound vjuh3
    imgd 42802
    citizen4 "Сосать будешь с голыми сиськами."
    imgd 42803
    citizen4 "Иначе уменьшу оплату."
    # Моника бесится
    music Pyro_Flow
    img 42804 vpunch
    m "Ты!.."
    m "Да кто ты такой, чтобы разговаривать со мной в подобном тоне?!"
    m "И еще указывать, что мне делать и как?!"
    # он смотрит на нее как на дуру
    music Groove2_85
    imgd 42805
    citizen4 "Слышь, детка. Давай обойдемся без этих реверансов."
    citizen4 "На самом деле все просто. Ты работаешь, я плачу деньги."
    citizen4 "Не хочешь работать - я найду себе другую шлюху."
    citizen4 "А ты останешься без 130 баксов в кармане."
    img 42806 hpunch
    m "!!!"
    imgd 42807
    citizen4 "Все, хорош болать!"
    # он указывает на свой член
    sound Jump1
    img 42808
    citizen4 "Давай, используй свой рот по назначению!"
    # Моника медлит
    imgf 42809
    mt "Черт!"
    mt "..."
    menu:
        "Ты точно мне заплатишь $ 130?":
            pass
        "Отказаться!":
            # Моника зло на него смотрит
            music Pyro_Flow
            imgd 42810
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            # Моника выгоняет его из квартиры
            imgd 42811
            m "НЕТ!!!"
            m "Я не собираюсь делать это!!!"
            m "Тем более, с тобой!!!"
            sound Jump2
            img 42812 vpunch
            m "Пошел вон отсюда!" # толкает его в дверь
            m "Еще раз увижу тебя в своем подъезде - позвоню в полицию!"
            sound anger2
            img 42813 hpunch
            m "Чертов извращенец!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            return
    # Моника в замешательстве
    music Groove2_85
    imgd 42814
    m "Ты точно мне заплатишь $ 130?"
    sound Jump2
    imgd 42815
    citizen4 "Ага. Вот они." # показывает купюры
    imgf 42816
    citizen4 "Оголяй сиськи и соси!"
    citizen4 "Достала меня уже своей болтовней!"
    music Power_Bots_Loop
    img 42817
    mt "Мерзкий! Невоспитанный! Бесполезный и никчемный подонок!"
    mt "!!!"
    # коррапшн
#    $ menu_corruption = [monicaCitizen4SexCorruptionRequired2, 0]
    menu:
        "Оголить грудь и сделать минет.":
#            $ monicaCitizen4SlumsApartment2 = day # Моника согласилась оголить грудь и сделать минет незнакомцу
            pass
        "Отказаться!":
            # Моника зло на него смотрит
            label gallery_42813:
            music Pyro_Flow
            imgd 42810
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            # Моника выгоняет его из квартиры
            imgd 42811
            m "НЕТ!!!"
            m "Я не собираюсь делать это!!!"
            m "Тем более, с тобой!!!"
            sound Jump2
            img 42812 vpunch
            m "Пошел вон отсюда!" # толкает его в дверь
            sound anger2
            img 42813 hpunch
            m "Еще раз увижу тебя в своем подъезде - позвоню в полицию!"
            m "Чертов извращенец!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            return
    # Моника не торопится, думает
    music Groove2_85
    imgf 42818
    mt "Мне нужны эти деньги!"
    mt "В конце концов, мне важен каждый цент в достижении моей цели!"
    mt "Я верну себе свою роскошную жизнь!"
    mt "И забуду все, что со мной происходит сейчас, как страшный сон!"
    # незнакомец вырывает ее из ее мыслей
    imgd 42819
    citizen4 "Эй, детка! Ты всегда такая тормознутая?"
    citizen4 "Снимай свою майку!"
    img 42820
    mt "!!!"
    menu:
        "Оголить грудь.":
            pass
    # Моника снимает топ, либо приспускает лямки, оголяя грудь
    imgf 42821
    w
    sound vjuh3
    imgd 42822
    w
    imgf 42823
    citizen4 "Ну наконец-то!"
    citizen4 "А теперь займись делом!"
    citizen4 "Давай быстрее!"
    menu:
        "Сделать минет.":
            pass
    # Моника опускает перед ним на колени, бросая злые взгляды на него
    fadeblack
    sound snd_walk_barefoot
    pause 2.0
    music Groove2_85
    imgf 42824
    citizen4 "Давай-давай!"
    citizen4 "Открывай свой рот!"
    citizen4 "И доделывай до конца, а не как в прошлый раз!"
    citizen4 "Иначе не заплачу ни цента!"
    imgd 42825
    mt "Как все это мерзко!"
    mt "Грязно!"
    mt "Отвратительно!!!"
    mt "!!!"
    # Моника открывает рот и вбирает в себя его член
    fadeblack 1.5
    music Loved_Up
    sound2 chpok6
    img 42826 hpunch
    citizen4 "Ммммм..."
    imgd 42827
    citizen4 "Даааа..."
    citizen4 "Хорошо..."
    imgd 42828
    citizen4 "Аааа..."
    citizen4 "Наконец-то ты доделаешь начатое..."
    imgf 42829
    citizen4 "И нам никто не помешает..."
    imgd 42830
    citizen4 "Не как в тот раз..."
    # незнакомец довольно закрывает глаза
    music Power_Bots_Loop
    img 19089
    show screen photoshot_screen()
    with hpunch
    perry "Я эту сучку везде ищу!"
    perry "А она тут развлекается с мужиками!"
    # он испуганно открывает глаза
    music stop
    sound plastinka1b
    img 42831 hpunch
    citizen4 "Черт!!!"
    music Turbo_Tornado
    citizen4 "Снова она мне мерещится!"
    citizen4 "Твою мать! Как отсос, так теперь эта дура у меня перед глазами!"
    # Моника выпускает его член изо рта
    imgd 42832
    m "Кого ты назвал дурой?!"
    # он раздраженно берет ее за голову и снова запихивает член ей в рот
    sound Jump1
    imgd 42833
    citizen4 "Да не тебя! Черт!"
    music Loved_Up
    sound2 Jump2
    img 42834 vpunch
    citizen4 "Давай соси!"
    imgd 42835
    citizen4 "И глубже бери!"
    # даваит на ее затылок, толкаясь глубже ей в рот
    sound chavc6
    img 42836 vpunch
    citizen4 "Еще глубже!"
    citizen4 "Давай-давай!"
    # Моника давится
    imgf 42837
    m "!!!"
    # video
    #1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_Citizen4_Blowjob2_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob2_1= Movie(play="video/v_Monica_Citizen4_Blowjob2_1.mkv")
    show videov_Monica_Citizen4_Blowjob2_1
    with fade
    m "ХПФМММ!"
    m "ММПППХХХФФФФ!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 42838
    w
    #2
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob2_2= Movie(play="video/v_Monica_Citizen4_Blowjob2_2.mkv")
    show videov_Monica_Citizen4_Blowjob2_2
    with fade
    citizen4 "Аааа..."
    citizen4 "Охренительно, детка..."
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
    image videov_Monica_Citizen4_Blowjob2_3= Movie(play="video/v_Monica_Citizen4_Blowjob2_3.mkv")
    show videov_Monica_Citizen4_Blowjob2_3
    with fade
    m "ММПППХХХФФФФ!!!"
    m "!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob2_4= Movie(play="video/v_Monica_Citizen4_Blowjob2_4.mkv")
    show videov_Monica_Citizen4_Blowjob2_4
    with fade
    citizen4 "Дааа... Хорошо!"
    citizen4 "Оооо..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 42839
    w
    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob2_5= Movie(play="video/v_Monica_Citizen4_Blowjob2_5.mkv")
    show videov_Monica_Citizen4_Blowjob2_5
    with fade
    citizen4 "Двигай своей головой быстрее!"
    citizen4 "Еще! Еще!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    # начинает кайфовать
    imgf 42840
    citizen4 "Мммм..."
    imgd 42841
    w
    # снова закрывает глаза от удовольствия
    music Power_Bots_Loop
    show screen photoshot_screen()
    imgd 42842
    with hpunch
    perry "130 баксов?!"
    perry "Эта проститутка сосет за 130 баксов?!"
    sound men_scream5
    img 42843 vpunch
    perry "И не отдает мне МОИ деньги!!!"
    music Turbo_Tornado
    citizen4 "Сукааа!"
    img 42844
    citizen4 "Да хватит уже преследовать меня!"
    citizen4 "Уйди! Уйди отсюда!"
    sound men_scream5
    imgd 42845
    citizen4 "Аааа!!!"
    sound Jump1
    img 42844 hpunch
    w
    # он испуганно оглядывается
    # Моника выпускает его член изо рта, тот грустно повисает, стояка как ни бывало
    # Моника смотрит в недоумении на упавший член
    sound vjuh3
    imgd 42846
    w
    imgd 42847
    w
    imgf 42848
    m "?!"
    # потом поднимает глаза на психующего незнакомца
    music Groove2_85
    imgd 42849
    m "?!?!?!"
    m "У тебя что, галлюцинации?"
    img 42850
    citizen4 "Не твое дело!!!"
    imgf 42851
    m "Ты какого черта не предупредил меня, что ты больной?!"
    m "На всю голову притом!"
    # он психует
    imgd 42852
    citizen4 "Хватит задавать вопросы!"
    citizen4 "Работай давай!"
    # Моника многозначительно смотрит на его упавший член
    imgd 42853
    m "..."
    citizen4 "Чего ты смотришь?!"
    citizen4 "Поднимай его!"
    # Моника берет уго упавший член в рот
    fadeblack 1.5
    music Loved_Up
    imgf 42854
    citizen4 "Да..."
    imgd 42855
    w
    sound lick3
    imgd 42856
    w
    sound lick3
    imgd 42855
    w
    sound lick3
    imgd 42856
    w
    sound lick3
    imgd 42855
    w
    sound lick3
    imgd 42856
    w
    sound chpok6
    imgd 42857
    citizen4 "Соси старательнее..."
    citizen4 "Сейчас встанет, да... Сейчас... Вот уже..."
    imgf 42858
    citizen4 "О, да..."
    imgd 42859
    citizen4 "Молодец, детка!"
    citizen4 "Давай, глубже!"
    imgf 42860
    citizen4 "Ты же знаешь, как мне нравится это."
    imgd 42861
    citizen4 "Вот так, да..."
    # снова закрывает глаза, кайфуя
    show screen photoshot_screen()
    imgd 42862
    with hpunch
    perry "Теперь ты от меня никуда не денешься!"
    # незнакомец начинает орать и отталкивает Монику от себя
    # член снова висит
    music Turbo_Tornado
    sound2 men_scream5
    img 42863 hpunch
    citizen4 "Аааа!!!"
    sound Jump1
    img 42864
    citizen4 "Нет-нет-нет!"
    # ситизен машет руками, как-будто отгоняет кого-то невидимого
    imgd 42865
    citizen4 "Я не хочу так!"
    sound Jump2
    img 42866
    citizen4 "Не надо!"
    # Моника смотрит на него как на идиота
    music Groove2_85
    imgf 42867
    mt "Может, он обкурился?"
    sound men_scream5
    # если Моника водила к себе Найджела
    if monicaCitizens9Slums2 > 0:
        imgd 42867
        mt "Не хватало еще одного укурка в моем доме!"
        mt "!!!"
    # Моника встает руки в боки
    music Power_Bots_Loop
    sound2 vjuh3
    img 42868 hpunch
    m "Эй, ты! Хватит орать!"
    m "Если ты так не хочешь, можешь валить отсюда!"
    # он немного подуспокоился и смотрит на Монику, потом на свой член
    sound Jump2
    imgd 42870
    w
    music Groove2_85
    imgd 42869
    w
    img 42870
    citizen4 "Поднимай его!"
    imgd 42871
    m "Ты издеваешься?!"
    m "Сколько можно?!"
    imgd 42872
    citizen4 "Шлюхе рот нужен не для того, чтобы возмущаться!"
    citizen4 "А для того, чтобы сосать!"
    citizen4 "Давай работай!!!"
    # Моника зло на него смотрит снизу вверх
    img 42873
    mt "Мерзавец!"
    mt "Пользуется тем, что мне нужны деньги!"
    mt "Урод!!!"
    menu:
        "Делать минет.":
            pass
    # Моника берет уго упавший член в рот
    label gallery_42964:
    fadeblack 1.5
    music Loved_Up
    imgf 42874
    w
    imgd 42875
    w
    imgf 42876
    w
    sound lick3
    imgd 42877
    w
    sound lick3
    imgd 42876
    w
    sound lick3
    imgd 42877
    w
    sound lick3
    imgd 42876
    w
    sound lick3
    imgd 42877
    w
    sound chpok6
    imgd 42878
    citizen4 "Да..."
    imgf 42879
    citizen4 "Cтарайся лучше..."
    # у него не встает
    imgd 42880
    citizen4 "Давай активнее!"
    citizen4 "Ты что, член ни разу не поднимала?"
    # Моника отстраняется и зло на него смотрит
    img 42881 vpunch
    mt "!!!"
    menu:
        "Делать минет еще усерднее.":
            label gallery_42914:
            music Hidden_Agenda
            imgd 42882
            mt "Черт с ним!"
            mt "Это делает не Моника Бакфетт!"
            if monica_shiny_hole_queen_day == 210:
                mt "Пусть это будет [monica_pub_name]!" # если работает или работала в пабе
            if monica_escort_service_started == True:
                mt "Или [monica_hotel_name]!" # если работает или работала в эскорте
            mt "Зато у меня станет на $ 130 больше!"
            # она снова берет в рот его член и начинает делать минет быстрее
            fadeblack 1.5
            music Loved_Up
            imgf 42886
            sound2 chpok6
            citizen4 "Быстрее!!!"
            citizen4 "Сейчас встанет! Сейчас!.."
            imgd 42887
            citizen4 "О, да..."
            citizen4 "Еще-еще!"
            imgd 42888
            citizen4 "Оооо!"
            imgf 42889
            citizen4 "Дааа!!!"
            # у него встал
            # он торопливо, испуганно оглядываясь
            sound hlup10
            img 42890
            w
            music Groove2_85
            sound2 Jump1
            imgd 42891
            w
            img 42892
            citizen4 "А теперь раздевайся и ложись на кровать!"
            citizen4 "Сейчас я буду тебя трахать!"
            citizen4 "Снимай свои тряпки!"
            imgd 42893
            citizen4 "Ложись и раздвинь ноги!"
            citizen4 "Давай быстрее! Шевелись!"
            mt "!!!"
            # коррапшн
#            $ menu_corruption = [monicaCitizen4SexCorruptionRequired3, 0]
            menu:
                "Сделать, как он говорит.":
#                    $ monicaCitizen4SlumsApartment6 = day # Моника согласилась на секс с незнакомцем
                    pass
                "Отказаться!":
                    # Моника зло на него смотрит
                    music Pyro_Flow
                    imgf 42894
                    mt "Я еще не настолько опустилась!"
                    mt "И, надеюсь, этого не произойдет НИКОГДА!"
                    # Моника выгоняет его из квартиры
                    img 42883 hpunch
                    m "НЕТ!!!"
                    m "Я не собираюсь делать это!!!"
                    sound Jump2
                    imgd 42884
                    m "Пошел вон отсюда!" # толкает его в дверь
                    m "Еще раз увижу тебя в своем подъезде - позвоню в полицию!"
                    sound anger2
                    img 42885 vpunch
                    m "Чертов извращенец!"
                    fadeblack
                    sound snd_door_open1
                    pause 1.5
                    return
            # Моника не торопится, думает
            music Pyro_Flow
            imgf 42894
            mt "Это все, конечно, грязно и отвратительно!"
            mt "Я ни за что не поверила бы, что способна согласиться на такое!"
            mt "Но все же... 130 долларов..."
            mt "В моей ситуации будет очень неумно отказываться от этих денег."
            mt "..."
            menu:
                "Снять трусики.":
                    pass
            # Моника снимает трусики
            # незнакомец стоит и дрочит
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 42895
            citizen4 "Дьявол!!!"
            imgf 42896
            citizen4 "Давай быстрее, пока не упал!"
            sound drkanje5
            imgd 42897
            citizen4 "Давай-давай!"
            # Моника идет к кушетке, ложится на нее, сдвинув ноги
            # незнакомец подходит ближе
            sound vjuh3
            img 42898 vpunch
            w
            sound vjuh3
            img 42899 vpunch
            w
            fadeblack
            sound snd_walk_barefoot
            pause 2.0
            music Groove2_85
            imgfl 42900
            citizen4 "И?!"
            imgf 42901
            citizen4 "Чего ты ждешь?"
            citizen4 "Покажи мне, что там у тебя!"
            menu:
                "Раздвинуть ноги.":
                    pass
            # Моника зло на него смотрит
            imgd 42902
            mt "Никчемный, бесполезный придурок!"
            mt "Псих!"
            imgf 42903
            w
            sound Jump1
            img 42904
            # раздвигает ноги
            # он лезет к ней на кушетку
            # хватает ее за щиколотки и задирает ее ноги
            # входит в нее
            imgf 42905
            citizen4 "Ооо... Твою мать!"
            citizen4 "Охренительно!"
            imgd 42906
            mt "Омерзительно!!!"
            # задирает ноги Моники так, что они практически у ее лица, она почти складывается поплам
            fadeblack 1.5
            music Loved_Up
            imgf 42907
            citizen4 "Давно я не трахал такую аппетитную шлюху!"
            sound Jump2
            img 42908 hpunch
            w
            imgd 42909
            mt "Сволочь! Когда он уже от меня отстанет?!"
            mt "Зачем я вообще согласилась на такое?!"
            mt "Разве $ 130 стоят таких унижений, Моника?!"
            mt "Ты притащила к себе домой какого-то шизанутого хмыря!"
            imgd 42910
            mt "Теперь лежишь на кушетке с его грязным отростком внутри тебя!"
            mt "Моника, как ты могла допустить подобное?"
            mt "Да что с тобой творится?!"
            mt "Неужели для тебя ЭТО становится нормой?!"
            mt "!!!"
            imgf 42911
            w
            # video
            #1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Citizen4_Sex1_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Sex1_1= Movie(play="video/v_Monica_Citizen4_Sex1_1.mkv")
            show videov_Monica_Citizen4_Sex1_1
            with fade
            citizen4 "Буду заходить к тебе почаще теперь, детка!"
            citizen4 "Мммм..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42912
            citizen4 "К черту отсосы! Мне гораздно приятнее трахать тебя в твою дырку!"
            citizen4 "Аааа! Круто как!"
            imgd 42913
            citizen4 "За такое и $ 130 не жалко дать тебе!"
            citizen4 "Оооо..."
            imgf 42914
            w
            #2
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Sex1_2= Movie(play="video/v_Monica_Citizen4_Sex1_2.mkv")
            show videov_Monica_Citizen4_Sex1_2
            with fade
            citizen4 "В следующий раз готовь свою задницу, детка! Да!!"
            citizen4 "Я трахну тебя так, что ты ходить не сможешь несколько дней!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42915
            mt "!!!"
            #3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Sex1_3= Movie(play="video/v_Monica_Citizen4_Sex1_3.mkv")
            show videov_Monica_Citizen4_Sex1_3
            with fade
            citizen4 "Я буду твоим самым щедрым клиентом!"
            citizen4 "А значит, самым желанным. Ха!"
            wclean
            citizen4 "И никакая баба в красном платье мне не помешает больше!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            music Loved_Up2
            imgf 42916
            citizen4 "Какая же охренительная у меня сегодня шлюха!"
            mt "!!!"
            #4
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Sex1_4= Movie(play="video/v_Monica_Citizen4_Sex1_4.mkv")
            show videov_Monica_Citizen4_Sex1_4
            with fade
            citizen4 "Ааааа!"
            citizen4 "Я скоро кончу!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42917
            w
            #5
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Sex1_5= Movie(play="video/v_Monica_Citizen4_Sex1_5.mkv")
            show videov_Monica_Citizen4_Sex1_5
            with fade
            citizen4 "Быстрее! Давай!"
            citizen4 "Дааааа..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42918
            w
            #6
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Sex1_6= Movie(play="video/v_Monica_Citizen4_Sex1_6.mkv")
            show videov_Monica_Citizen4_Sex1_6
            with fade
            citizen4 "Дааа!"
            wclean
            citizen4 "Еще немного!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            menu:
                "Кончить на киску Моники.":
#                    $ monicaCitizen4Sex_cumzone = 1
                    img 42919
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    citizen4 "Ааааа!!!"
                    img 42920
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan18
                    citizen4 "АААААА!!!"
                    sound hlup10
                    imgd 42921
                    w
                    pass
                "Кончить внутрь Моники.":
#                    $ monicaCitizen4Sex_cumzone = 2
                    img 42919
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    citizen4 "Ааааа!!!"
                    img 42923
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan18
                    citizen4 "АААААА!!!"
                    pass
                "Кончить на грудь Моники.":
#                    $ monicaCitizen4Sex_cumzone = 3
                    img 42919
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    citizen4 "Ааааа!!!"
                    img 42920
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan18
                    citizen4 "АААААА!!!"
                    sound hlup10
                    imgd 42922
                    w
                    pass
            # незнакомец довольно садится на кушетке
            fadeblack 1.5
            music Groove2_85
            imgfl 42924
            citizen4 "Кайф!"
            imgf 42925
            citizen4 "Считай, что наша сегодняшняя сделка закрыта."
            # Моника с ненавистью смотрит на него
            music Pyro_Flow
            imgd 42926
            mt "Никчемный мешок дерьма!"
            mt "Моника, больше чтоб ноги его не было в твоем доме!"
            mt "Жалкий трущобный отброс общества!"
            mt "ДНО!!!"
            mt "!!!"
            pass
        "Нет, хватит! (Extra version) (disabled)" if game.extra == False:
            pass
        "Нет, хватит!" if game.extra == True: # в экстру
            # Моника возмущенно
            music Pyro_Flow
            sound2 vjuh3
            img 42927 hpunch
            m "Да сколько можно?!"
            m "Ты что, не видишь, что это бесполезно?!"
            # он психует
            imgd 42928
            citizen4 "Черт с тобой!"
            citizen4 "Больше никаких отсосов!"
            citizen4 "Давай, раздевайся!"
            citizen4 "Сейчас я тебя буду трахать!"
            # Моника насмешливо смотрит на его грустный член
            img 42929
            m "Чем?"
            m "Вот этим?!" # указывает пальцем
            m "Или мне снова нужно поднимать его?"
            # он испуганно оглядываясь
            music Groove2_85
            sound2 Jump2
            img 42930 hpunch
            citizen4 "Нет! Никаких отсосов больше!"
            citizen4 "Не прикасайся ко мне своим ртом!"
            # хватается за свой член и начинает яростно надрачивать
            imgd 42931
            citizen4 "Снимай свои тряпки!"
            citizen4 "Сядь на кушетку и раздвинь ноги!"
            citizen4 "Давай быстрее! Шевелись!"
            #music Groove2_85
            imgd 42932
            mt "!!!"
            # коррапшн
#            $ menu_corruption = [monicaCitizen4SexCorruptionRequired4, 0]
            menu:
                "Сделать, как он говорит.":
#                    $ monicaCitizen4SlumsApartment3 = day # Моника согласилась раздеться и раздвинуть ноги для незнакомца
                    pass
                "Отказаться!":
                    # Моника зло на него смотрит
                    music Pyro_Flow
                    imgf 42933
                    mt "Я еще не настолько опустилась!"
                    mt "И, надеюсь, этого не произойдет НИКОГДА!"
                    # Моника выгоняет его из квартиры
                    imgd 42883
                    m "НЕТ!!!"
                    m "Я не собираюсь делать это!!!"
                    sound Jump2
                    img 42884 vpunch
                    m "Пошел вон отсюда!" # толкает его в дверь
                    m "Еще раз увижу тебя в своем подъезде - позвоню в полицию!"
                    sound anger2
                    img 42885 vpunch
                    m "Чертов извращенец!"
                    fadeblack
                    sound snd_door_open1
                    pause 1.5
                    return
            # Моника не торопится, думает
            music Pyro_Flow
            imgf 42933
            mt "Это все, конечно, грязно и отвратительно!"
            mt "Я ни за что не поверила бы, что способна согласиться на такое!"
            mt "Но все же... 130 долларов..."
            mt "В моей ситуации будет очень неумно отказываться от этих денег."
            mt "..."
            menu:
                "Снять трусики.":
                    pass
            # Моника снимает трусики
            # незнакомец стоит и продолжает дрочить, но стояка все нет
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 42934
            citizen4 "Дьявол!!!"
            citizen4 "Сядь и раздвинь ноги!"
            imgf 42935
            citizen4 "Давай-давай!"
            sound drkanje5
            imgd 42936
            w
            # Моника идет к кушетке, садится на нее, сдвинув ноги
            # незнакомец подходит ближе
            sound vjuh3
            img 42898 hpunch
            w
            sound vjuh3
            img 42899 hpunch
            w
            fadeblack
            sound snd_walk_barefoot
            pause 2.0
            music Groove2_85
            imgf 42937
            citizen4 "И?!"
            citizen4 "Чего ты ждешь?"
            citizen4 "Покажи мне, что там у тебя!"
            menu:
                "Раздвинуть ноги.":
                    pass
            # Моника зло на него смотрит
            imgd 42938
            mt "Никчемный, бесполезный придурок!"
            mt "Псих!"
            imgd 42939
            w
            sound Jump2
            img 42940
            w
            # раздвигает ноги
            music Loved_Up
            imgf 42941
            citizen4 "Да, детка."
            citizen4 "Хорошо, да..."
            imgd 42949
            w
            imgf 42942
            citizen4 "Сейчас он встанет!"
            sound drkanje5
            imgd 42943
            w
            sound drkanje5
            imgd 42942
            w
            sound drkanje5
            imgd 42943
            citizen4 "Еще немного и встанет!"
            sound drkanje5
            imgd 42942
            w
            sound drkanje5
            imgd 42943
            w
            # дрочит-дрочит, а эффекта ноль
            # он психует еще больше
            scene black_screen
            with Dissolve(1)
            music drkanje5
            call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_31
            scene black_screen
            with Dissolve(1)
            music Groove2_85
            imgf 42944
            w
            imgd 42945
            citizen4 "Сейчас я вставлю его и все получится!"
            # пытается тыкнуться в Монику своим вялым членом, но у него ничего не получается
            fadeblack 1.5
            music Groove2_85
            imgf 42946
            citizen4 "Твою мать!"
            sound hlup10
            imgd 42947
            citizen4 "Чертова баба в красном платье!"
            imgd 42948
            citizen4 "Это все из-за нее! Тварь!"
            # Моника удивленно на него смотрит
            imgf 42950
            citizen4 "Да сколько можно!"
            citizen4 "Черт! Давай, хоть отлижу у тебя!"
            # он продолжает дрочить и резко присасывается к киске Моники губами
#            label video_test:
            music Turbo_Tornado
            sound2 Jump1
            img 42951 vpunch
            m "Ай! Что ты делаешь?!"
            # она пытается оттолкнуть его голову, но он присосался намертво
            imgd 42952
            citizen4 "Ммммм..."
            m "Мы так не договаривались!!!"
            # от отрывается от ее киски, чтобы сказать
            img 42953
            citizen4 "Условия нашей сделки изменились."
            citizen4 "Я у тебя отлижу, ты заработаешь $ 130."
            citizen4 "А сейчас закрой свой рот и не мешай мне!"
            # и снова присасывается
            music Loved_Up
            imgf 42954
            w
            # video
            #1
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_Citizen4_Licking1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Licking1_1_25= Movie(play="video/v_Monica_Citizen4_Licking1_1_25.mkv")
            show videov_Monica_Citizen4_Licking1_1_25
            with fade
            citizen4 "Мммм..."
            mt "Ему что, действительно так нравится делать это с моей киской?!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            # Моника в недоумении смотрит на него, сидя на кушетке и широко раздвинув ноги
            imgd 42955
            w
            #2
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Licking1_2_25= Movie(play="video/v_Monica_Citizen4_Licking1_2_25.mkv")
            show videov_Monica_Citizen4_Licking1_2_25
            with fade
            mt "Это же... Гадко!"
            mt "Фу!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42956
            mt "Это удивительно, что вокруг меня столько извращенцев..."
            mt "Еще попадаются и больные на голову, как этот кретин!"
            # он усердно лижет ее киску и продолжает дрочить
            # член встает
#            sound lick3
            imgf 42957
            w
            #3
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Licking1_3_25= Movie(play="video/v_Monica_Citizen4_Licking1_3_25.mkv")
            show videov_Monica_Citizen4_Licking1_3_25
            with fade
            citizen4 "Мпфааа!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42955
            citizen4 "Дааа..."
            sound Jump2
            img 42959 vpunch
            citizen4 "Это сработало!" # радостно
            # снова присасывается и дрочит себе
            imgd 42960
            w
            sound drkanje5
            imgd 42961
            w
            sound drkanje5
            imgd 42960
            w
            sound drkanje5
            imgd 42961
            w
            sound drkanje5
            imgd 42960
            w
            sound drkanje5
            imgd 42961
            w
            imgf 42962
            citizen4 "Вот так тебе, сучка в красном платье!"
            citizen4 "Пошла ты!"
            mt "?!"
            #4
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Licking1_4_25= Movie(play="video/v_Monica_Citizen4_Licking1_4_25.mkv")
            show videov_Monica_Citizen4_Licking1_4_25
            with fade
            citizen4 "Я все равно кончу, слышишь?!"
            citizen4 "И ни хрена ты мне не помешаешь, шлюшка!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42963
            w
            imgf 42964
            mt "Боже, он совсем не в адеквате!"
            mt "Надо заканчивать с этим быстрее!"
            mt "И выгонять его!"
            imgd 42965
            mt "Черт знает, что ему еще померещится!"
            mt "Не хватало мне с ним проблем!"
            mt "!!!"
            # он лижет и приговаривает
            music Loved_Up2
            imgf 42966
            w
            #5
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Licking1_5_25= Movie(play="video/v_Monica_Citizen4_Licking1_5_25.mkv")
            show videov_Monica_Citizen4_Licking1_5_25
            with fade
            citizen4 "Оооо..."
            citizen4 "Дааа!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            imgd 42967
            citizen4 "Я кончу совсем скоро! Наконец-то!"
            citizen4 "Мммм!!!"
            # дрочит, а потом кончает, не переставая присасываться к киске Моники
            imgd 42966
            w
            #6
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_Citizen4_Licking1_6_25= Movie(play="video/v_Monica_Citizen4_Licking1_6_25.mkv")
            show videov_Monica_Citizen4_Licking1_6_25
            with fade
            citizen4 "Я кончаю! Кончаю!"
            citizen4 "Мммпфф!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            img 42969
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            citizen4 "Мпфхфпфф!!!"
            img 42970
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            citizen4 "МПФААА!!!"
            # кончает себе на руку
            img 42971
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            citizen4 "Охренительно!!!"
            imgd 42972
            mt "Омерзительно!!!"
            mt "Дебил!"
            mt "Моника, вытряхивай скорее этого никчемного психа со своей квартиры!"
            mt "!!!"
            pass
    # затемнение
    # они оба стоят одетые
    # незнакомец доволен, как слон
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 42973
    citizen4 "Детка, ты хорошо поработала."
    m "Давай мне мои деньги!"
    imgf 42974
    citizen4 "Держи свои 130 баксов, как договаривались."
    citizen4 "Мне понравилось."
    citizen4 "Я еще приду к тебе."
#    $ add_money(130.0)
    imgd 42817
    mt "Нет!"
    mt "Это был первый и последний раз!"
    mt "!!!"
    imgf 42975
    w
    fadeblack
    sound snd_door_open1
    pause 1.5
    music Pyro_Flow
    # он разворачивается и уходит
    # Моника стоит недвольная
    imgf 42976
    mt "Моника, в твоем кармане стало на $ 130 больше."
    mt "Но каким путем?!"
    mt "?!?!?!"
    mt "Если так и дальше будет продолжаться!.."
    mt "Если ты не прекратишь водить к себе домой всяких трущобных отбросов!.."
    mt "Я боюсь, что тебе будет все тяжелее и тяжелее оставаться нормальным адекватным человеком!"
    mt "И ты превратишься в одну из тех падших женщин, которые стоят рядом со старой грымзой на улице!"
    imgd 42977
    mt "О, Боги! Нет-нет!"
    mt "Не хочу даже думать об этом!!!"
    mt "Моника Бакфетт никогда не опустится до такого дна!!!"
    mt "!!!"
    return

label gallery_34528:
    # как обычно подходит к нему
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Hidden_Agenda
    imgf 34471
    m "Биф..."
    m "Я хотела узнать у тебя..."
    # Биф нетерпеливо перебивает ее
    music Groove2_85
    img 15897
    biff "Наконец-то, пришла!"
    biff "Где тебя носило все это время, а?!"
    # Моника с деловым видом
    imgd 15900
    m "Вообще-то, я работала, Биф!"
    biff "Работала она! Ты только одним местом умеешь хорошо работать!"
    biff "Тем, которым ты себе зарабатывала на хлеб, когда была двадцатидолларовой шлюхой!"
    imgd 15901
    biff "А здесь все, что ты делаешь - создаешь видимость работы!"
    biff "Притворяясь сучкой Бакфетт!"
    biff "Поэтому не надо мне тут кривляться и строить из себя занятую леди!"
    m "Биф!.."
    # Биф перебивает и отмахивается от нее
    img 15902
    biff "Все! Закрой рот!"
    # потом встает с кресла
    sound vjuh3
    img 34472 vpunch
    biff "Так, иди сюда и садись за стол!"
    # Моника в шоке
    m "За стол?"
    imgd 34473
    m "Зачем?"
    m "?!?!?!"
    # он подходит к ней
    sound man_steps
    imgf 34474
    w
    imgd 34475
    biff "Сейчас придет один из тех денежных мешков, которые до сих пор еще не принесли свои деньги в мой журнал..."
    mt "МОЙ ЖУРНАЛ!"
    mt "!!!"
    biff "Он до этого спрашивал, как с тобой переспать."
    img 34476 hpunch
    m "ЧТО?!"
    biff "Он думает, что ты сучка Бакфетт."
    biff "И готов за то, чтобы переспать с тобой, двадцатидолларовой шлюхой, инвестировать в журнал."
    biff "Ха-ха-ха!"
    music Pyro_Flow
    imgd 34477
    m "!!!"
    m "Биф! Я не хочу и не буду!.."
    # он ее перебивает
    img 34478 hpunch
    biff "Я тебя не спрашиваю, хочешь ты этого или нет!"
    biff "Это твоя обязанность - заставить раскошелиться всех инвесторов!"
    biff "А в итоге Я, твой Босс, сам занимаюсь этим и делаю твою работу!"
    m "!!!"
    music Groove2_85
    imgd 34479
    biff "В общем, этот Мэйсон не дождался, пока я тебя, кукла, подложу под него..."
    biff "И решил выдвинуть другое условие своей инвестиции."
    biff "Он привел свою любовницу. Хочет, чтобы она снималась в моем журнале."
    m "???"
    # если Моника работала реквизитом у Линды. Моника злорадно
    if monicaEscortLindaTable1 == True:
        #
        $ notif(_("Моника работала реквизитом Линды в отеле Ле Гранд, когда у той было свидание с инвестором."))
        #
        music Stealth_Groover
        imgf 34480
        mt "Мэйсон? Это тот никчемный идиот, которого пытается окрутить стерва Линда?"
        mt "Интересно, а она в курсе, что у него есть любовница?"
        mt "Посмотрела бы я на ее лицо, когда она узнает про это!"
        mt "Так этой сучке и надо!"
        mt "Значит, этот Мэйсон не такой безмозглый кретин, как я думала."
        mt "И не верит этой мерзкой Линде, раз у него есть любовница."
        #
    # если был секс с инвестором
    if monicaEscortLindaTable6 == True:
        imgd 34481
        mt "Я этого мерзавца инвестора видеть не могу после того..."
        mt "После того случая в номере отеля!"
        mt "Сволочь!"
        #
    # Моника недовольно
    music Groove2_85
    imgd 34482
    m "А от меня что тербуется, Биф?"
    biff "Я не хочу брать его девку к себе в журнал!"
    biff "Если она мне покажется тупой безмозглой и непослушной куклой..."
    biff "Я не смогу ее просто взять и выкинуть на улицу! В отличие от тебя..."
    biff "У меня и без этой девки есть цыпочки, которыми я могу заменить тебя."
    imgf 34483
    biff "Помимо всего прочего, ей придется еще и платить!"
    biff "А мне от него нужны инвестиции, а не какие-либо дополнительные траты!"
    biff "Поэтому мне выгоднее, чтобы он трахнул тебя, чем возиться с его любовницей."
    m "Биф, я!.."
    # Биф снова перебивает ее
    sound Jump1
    img 34484
    biff "Тихо, кукла! Твой Босс еще не договорил!"
    m "!!!"
    biff "Короче, этому Мэйсону нужно отказать. Но это сделаешь ты, а не я!"
    biff "И после этого я договорюсь с ним, чтобы он тебя трахнул!"
    music Power_Bots_Loop
    img 34485 vpunch
    m "ЧТО?!"
    music Groove2_85
    biff "Что слышала, кукла!"
    biff "После твоего отказа он еще больше захочет это сделать!"
    biff "Давай, иди в кресло!"
    biff "Пользуйся тем, что папочка сегодня добрый и тащи свою задницу на его место!"
    imgd 34486
    m "!!!"
    menu:
        "Отказаться!":
            # Моника медлит и зло смотрит на Бифа
            music Pyro_Flow
            imgf 34481
            mt "Как этот мерзкий Биф смеет так со мной обращаться?!"
            mt "Я здесь Босс! Это МОЙ журнал!"
            mt "И я не собираюсь развивать СВОЙ бизнес, используя свое тело!"
            mt "Если ему так нужно, пусть сам договаривается с инвестором!"
            mt "Тупоголовый никчемный идиот!"
            mt "!!!"
            # Моника надменно
            imgd 34487
            m "Я не собираюсь принимать участие в твоих глупых и пошлых планах!"
            m "Сам разбирайся с этим Мэйсоном и его любовницей!"
            biff "Так! Ты снова начала корчить из себя сучку Бакфетт?!"
            biff "Пошла вон отсюда! И больше ты не получишь никакую работу, кукла безмозглая!.."
            biff "Пока не сделаешь так, как говорю тебе Я!"
            # Моника, уходя, бросает ему
            imgf 34488
            sound highheels_short_walk
            m "Пошел ты к черту, Биф!"
            m "!!!"
            fadeblack 2.0
            return
        "Сесть в кресло.":
#            $ monicaLindaMirandaFriendship1 = day # Моника согласилась поговорить с инвестором и его любовницей
            pass
    # Моника зло смотрит на Бифа и медлит
    music Stealth_Groover
    imgf 34481
    mt "Чертов Биф!!!"
    mt "Кто вообще посадил этого безмозглого никчемного идиота на МОЕ место?!"
    mt "У него уровень интеллекта ниже, чем у плинтуса!"
    mt "Но... Мне на руку, что он не блещет умом!.."
    imgd 34480
    mt "Сейчас я сделаю вид, что играю по его правилам."
    mt "И притворюсь послушной 'куклой'..."
    mt "А потом, когда он скажет, что договорился с инвестором Мэйсоном..."
    mt "Я придумаю что-нибудь, чтобы Мэйсон встал на мою сторону!"
    # если был секс с Олафом
    if monicaBiffInvestorDate5 == True:
        imgf 34489
        mt "Да, с подкаблучником Олафом я планировала сделать тоже самое, но..."
        mt "В тот раз что-то пошло не по плану."
        mt "Я учту этот факт и больше не совершу такого промаха!"
        #
    imgd 34490
    mt "А потом, с его помощью, я сделаю все, чтобы избавиться от Бифа!"
    mt "Пора прекращать весь этот цирк и подчиняться его приказам, играя роль бесправной, глупой куклы!"
    mt "Он узнает, кто на самом деле здесь БОСС!"
    mt "И он познает на себе гнев Миссис Бакфетт!!!"
    mt "..."
    imgf 34491
    mt "Что ж, Моника... Пора тебе занять свое законное место в этом кабинете!"
    mt "Пусть это будет только сегодня и совсем недолго, но..."
    mt "Скоро ты все расставишь по своим местам!"
    imgd 34492
    mt "Потому что ты - Моника Бакфетт!"
    mt "Ты самая умная и расчетливая женщина!"
    mt "Ты сможешь манипулировать глупыми мужчинами, используя свой ум и красоту!"
    mt "!!!"
    # Биф торопит Монику, выводя ее из раздумий
    music Groove2_85
    img 34493
    biff "Эй, кукла! Ты долго собираешься тут стоять?!"
    biff "Иди в мое кресло!"
    biff "И притворяйся сучкой Бакфетт так, как ты это умеешь делать!"
    biff "Быстро! Мэйсон сейчас придет сюда! Я встречу его в приемной!"
    # Моника с достоинстовом проходит мимо Бифа и садится в кресло
    # пока Биф бежит к двери, Моника блаженствует в своем кресле
    # задумчиво проводит руками по столешнице или креслу
    imgf 34494
    sound highheels_short_walk
    w
    imgd 34495
    w
    sound man_steps
    imgf 34496
    w
    music RnB4_100
    imgd 34497
    mt "Вот мое законное место!"
    mt "Оно скоро вновь станет моим!"
    mt "Я добьюсь этого!"
    imgf 34498
    mt "И кретина Бифа я не уволю в первый же день! Нет!..."
    mt "Сначала я отомщу ему за все те унижения, которые я вынуждена была пройти из-за него!"
    mt "..."
    imgd 34499
    mt "А теперь, Моника, ты можешь позволить себе побыть собой настоящей..."
    mt "Красивой, умной бизнес-леди, главой известного модного журнала."
    mt "Несравненной Миссис Бакфетт!"
    mt "..."
    # Моника выходит из состояния задумчивости, включает Большойго Босса и недовольно смотрит в сторону двери
    music Stealth_Groover
    imgf 34500
    mt "Так, я что-то не пойму!"
    mt "Где этот жалкий инвесторишка со своей никчемной любовницей?!"
    mt "?!"
    # звук открывающейся двери, шаги
    # в кабинет входит довольный Биф, за ним идет investor3
    # Биф любезничает с ним
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    imgfl 34501
    sound2 man_steps
    biff "Проходите, Мистер Мэйсон!"
    biff "Миссис Бакфетт готова вас принять."
    # потом подбегает к столу Моники, на ходу говорит услужливо
    imgf 34502
    w
    imgd 34503
    biff "Миссис Бакфетт, вам принести воды?"
    # и под соусом этого, пока инвестор не слышит, наклоняется к Монике ближе и угрожающе шепчет
    music Power_Bots_Loop
    img 34504
    biff "И без глупостей, кукла!"
    biff "Действуешь четко по моему плану! Поняла меня?!"
    # Моника издевательски смотрит на него
    music Stealth_Groover
    imgd 34505
    m "Нет, Биф. Мне пока от тебя ничего не нужно."
    m "А пока иди. Не мешай мне общаться с Мистером Мэйсоном..."
    # Биф зло смотрит на Монику, потом притворно улыбаясь отходит от стола в сторону
    # Моника обращается к инвестору надменно
    sound man_steps
    imgf 34506
    m "Здравствуйте, Мистер Мэйсон..."
    # тот общается с ней очень вежливо
    imgd 34507
    mason "Добрый день, Миссис Бакфетт."
    mason "Очень рад, что вы согласились принять меня."
    mason "И выслушать мою небольшую просьбу, так сказать."
    # Моника продолжает вести себя надменно
    imgd 34508
    m "Да, я согласилась..."
    m "Но у меня очень мало времени."
    m "Мне пришлось отменить одну важную встречу из-за этого несвоевременного кастинга."
    m "Который мне придется проводить сейчас по вашей просьбе."
    imgf 34509
    m "Так что давайте не будем тратить мое время и перейдем к делу, Мистер Мэйсон."
    mason "Да конечно, Миссис Бакфетт!"
    mason "Спасибо вам большое!"
    # Моника делает небрежный жест рукой
    imgd 34510
    m "Где эта ваша... Кхм... Протеже?"
    m "Зовите ее сюда. Я посмотрю на нее."
    imgd 34511
    mason "Секунду, Миссис Бакфетт."
    mason "Она ожидает в приемной у вашего секретаря."
    # инвестор поворачивает голову в сторону двери
    mason "Дорогая, заходи!"
    # Моника про себя ворчит
    imgf 34512
    mt "Сейчас зайдет какая-нибудь серая мышь..."
    mt "Которая думает, что через постель может добиться вершин славы."
    mt "Фи! Как это гадко и пошло!"
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    # звук каблуков, в кабинет заходит Линда
    if monica_escort_service_started == True:
        imgfl 34515
        w
        sound highheels_short_walk
        imgf 34513
        w
        imgd 34514
        linda "Миссис Бакфетт, добрый..." # прерывается на полуслове
        # у Линды шок
        imgd 34516
        w
        music stop
        sound plastinka1b
        img 34517 vpunch
        w
        music Power_Bots_Loop
        img 34518 vpunch
        linda "!!!"
        # у Моники шок
        imgd 34519
        m "!!!"
        mt "НЕЕЕТ!"
        mt "Только не это!!!"
        mt "!!!"
        # молча смотрят друг на друга в афиге
        music Groove2_85
        mason "Миссис Бакфетт, это моя хорошая знакомая. Ее зовут Линда."
        mason "Линда мечтает стать моделью вашего журнала."

    else:
        imgfl 34520
        sound highheels_short_walk
        linda "Миссис Бакфетт, добрый день."
        # Моника высокомерно игнорирует ее приветствие
        imgf 34521
        m "..."
        # надменно осматривает ее с головы до ног
        linda "..."
        music Groove2_85
        mason "Миссис Бакфетт, это моя хорошая знакомая. Ее зовут Линда."
        mason "Линда мечтает стать моделью вашего журнала."
    # инвестор, не замечая этого, начинает болтать
    imgd 34522
    mason "И мне кажется, что у нее есть все шансы."
    mason "Мы с Мистером Бифом уже обсуждали это и он предварительно одобрил кандидатуру Линды..."
    # Моника выходит из состояния ступора и прерывает его с видом Большого Босса
    music Pyro_Flow
    img 34523 vpunch
    m "Зато я не одобряю!"
    # инвестор в растерянности смотрит на Бифа, потом снова на Монику
    mason "Но как же?.. И это весь кастинг?"
    mason "Но Мистер Биф..."
    # Моника важно перебивает его
    sound Jump2
    img 34524 hpunch
    m "Здесь Я принимаю решения, а не Мистер Биф!"
    m "Он всего-лишь мой помощник, не более того!"
    m "Я таких, как она, каждый день десятками отправляю вон из моего офиса!"
    music Stealth_Groover
    m "Своим профессиональным взглядом я сразу опеределяю..."
    m "Модель это или очередная посредственность с чрезмерно завышенными амбициями!"
    # Линда зло смотрит на Монику, но молчит
    img 34525
    linda "!!!"
    # Моника продолжает разнос
    imgf 34526
    m "И я вам, Мистер Мэйсон, могу сразу сказать, что это не модель..." # вальяжный, небрежный жест в сторону Линды
    # инвестор растерян
    mason "Но..."
    # Моника перебивает его
    imgd 34527
    m "Что у нее с фигурой?!"
    m "А с лицом?!"
    m "Она что, вообще не умеет улыбаться?!"
    # Моника обращается к Линде
    imgd 34528
    m "Ты вообще-то на кастинг в модный журнал пришла, а не на похороны! Что у тебя с лицом?!"
    linda "!!!"
    # инвестор злясь на Линду, шепчет ей нервно
    img 34529 hpunch
    mason "Да улыбнись же ты!"
    # Линда злая, натягивает улыбку
    imgd 34530
    w
    sound Jump1
    imgd 34531
    linda "..."
    # Моника неприязненно смотрит на нее
    imgf 34532
    m "Ну нет!"
    m "Мне не нравится ее улыбка!"
    # обращается к инвестору
    imgd 34523
    m "Мистер Мэйсон, я вынуждена отказать вам в вашей просьбе..."
    m "Кандидатура этой особы меня не устраивает."
    m "Она абсолютно не подходит для работы моделью!"
    # инвестор офигевая
    imgd 34533
    mason "Миссис Бакфетт, возможно..."
    m "Ответ 'нет'! Никаких 'возможно' или 'может быть'!!!"
    m "Она мне не подходит!"
    imgf 34510
    m "Если вы, Мистер Мэйсон, с Мистером Бифом решили, что это красивая девушка..." # снова небрежный жест на Линду
    imgd 34533
    m "То это не означает, что я думаю так же!"
    m "Я отказываю ей!"
    # Биф что-то хочет сказать
    imgf 34534
    biff "Миссис Бакфетт..."
    # Моника рявкает на него
    music Pyro_Flow
    img 34535 vpunch
    m "Молчи, Биф!"
    m "Прежде, чем давать свое одобрение Мистеру Мэйсону, ты должен был согласовать это со мной!"
    m "Ты оштрафован за свое некомпетентное и непрофессиональное поведение!"
    m "В МОЕМ журнале это недопустимо!!!"
    # Биф смотрит на нее в шоке
    imgd 34536
    biff "..."
    m "Чего ты на меня уставился?!"
    m "Ты все понял или мне нужно повторить тебе, чтобы до твоего недалекого ума дошло это?!"
    # Биф сквозь зубы
    biff "Я... Я все понял, Миссис Бакфетт..."
    # Моника жестом затыкает его
    sound Jump1
    img 34537
    m "Все, замолчи, Биф! Раздражаешь меня!"
    # потом обращается к инвестору
    music Stealth_Groover
    imgf 34538
    m "Мистер Мэйсон..."
    m "Полагаю, наша встреча закончена."
    m "У вас есть еще какие-либо обращения или просьбы?"
    mason "Нет, Миссис Бакфетт."
    mason "Спасибо, что уделили мне время..."
    mason "Надеюсь, до скорой встречи."
    imgd 34539
    m "А я - нет! До свидания!"
    sound highheels_short_walk
    imgf 34540
    w
    imgd 34541
    w
    music Power_Bots_Loop
    # инвестор с Линдой выходят из кабинета
    # если Моника работала или работает в эскорте
    if monica_escort_service_started == True:
        # Моника с ненавистью смотрит им вслед
        imgd 34512
        mt "Линда!!!"
        mt "Проститука-эскортница!!!"
        mt "Метит в МОЙ журнал?!"
        mt "Я тебе, сучка, никогда не позволю это сделать!"
        mt "Лицемерная овца!"
        mt "Дрянь!"
    else:
        # Моника недовольно смотрит им вслед
        imgd 34512
        mt "Никчемный идиот!"
        mt "Где он только нашел эту особу?!"
        mt "Она и двух слов связать не может... И внешность у нее посредственная..."
        mt "А еще метит в МОЙ журнал!"
        mt "Очередная серая мышь!"
    #
    # Биф с восторженной миной подскакивает к столу Моники
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    imgf 34542
    biff "Ух ты! Цыпочка, а ты умеешь набивать себе цену!"
    biff "Как ты круто притворялась сучкой Бакфетт! Я впечатлен!"
    biff "У тебя получается все лучше и лучше, цыпочка!"
    biff "Уверен, после такого обращения, Мэйсон еще больше захочет тебя трахнуть! Ха-ха!"
    # Моника, продолжая сидеть в кресле, бросает ему зло
    imgd 34543
    m "Я не собираюсь ни с кем спать!!!"
    m "!!!"
    # Биф начинает раздражаться
    img 34504 hpunch
    biff "Ты снова за свое?!"
    biff "Я тебе сказал, кукла ты безмозглая, что ты сделаешь это!"
    biff "И вообще! Ну-ка быстро встала с моего кресла!"
    # Моника зло на него смотрит
    img 34505
    m "!!!"
    menu:
        "Встать с кресла.":
            pass
        "Не вставать!":
            # Биф злится
            #music Ready_and_Waiting
            imgf 34544
            biff "Чего ты смотритшь, кукла?!"
            biff "Я сказал тебе встать с моего кресла!"
            biff "Что тут непонятного?!"
            music Funk_Soul1
            m "Если я являюсь двойником Миссис Бакфетт, то почему в этом кресле сижу не Я, а ТЫ?"
            imgd 34545
            biff "Что за дурацкие вопросы?!"
            biff "Это МОЕ кресло!"
            biff "Быстро встала и ушла!"
            m "Это кресло Моники Бакфетт, а не твое!"
            m "А Я заменяю ее!"
            m "Значит, это МОЕ кресло!"
            # Биф начинает орать
            sound Jump1
            img 34546 vpunch
            biff "Так! А ну-ка закрыла свой рот!"
            biff "Безмозглая двадцатидолларовая шлюха!"
            biff "Быстро вытащила свою задницу из МОЕГО кресла!"
            biff "И пошла ВОН!"
            img 34547
            m "НЕТ!"
            biff "Ах ты!.. Ты!.."
            biff "Дешевая потаскушка, притворяющася сучкой Бакфетт!"
            biff "Если ты не встанешь с моего кресла!.."
            biff "То я!.. Я!.. Я полицию вызову!!!"
            imgd 34548
            biff "Скажу, что какая-то шлюха ворвалась ко мне в кабинет и захватила его!"
            biff "Тогда больше твоей ноги чтобы не было в МОЕМ офисе!!!"
            # Моника про себя злится
            imgd 34512
            mt "Дьявол!"
            mt "Только полиции мне не хватало!"
#            $ monicaLindaMirandaFriendship2 = day # Моника спорила с Бифом, отказываясь вставать с кресла босса
            pass
    # Моника насупленно молчит и продолжает сидеть в кресле, Биф грозно нависает над ней
    music RnB4_100
    imgf 34549
    mt "Меньше всего мне сейчас хочется покидать это кресло!"
    mt "Так приятно снова быть собой, не надевая никаких масок, не притворяясь..."
    mt "Но, Моника, ты должна помнить, что ты задалась целью перехитрить глупца Бифа!"
    mt "И сейчас ты должна делать вид, что играешь по его правилам!"
    imgd 34550
    mt "Нужно встать с этого кресла... Еще пару секунд и я уйду..."
    mt "Да, пора... Не стоит затягивать этот момент."
    mt "Все, встаю..."
    # Моника молча поднимается с кресла и идет к выходу
    # Биф довольно усаживает на кресло и бросает в спину Моники
#    music Groove2_85
    imgf 34551
    w
    fadeblack 1.0
    music Groove2_85
    sound2 highheels_short_walk
    imgf 34552
    biff "Кукла!"
    biff "Завтра вечером жду тебя здесь!"  # старт фотосессии у Кэмпбелла в офисе
    biff "Для тебя есть работа!"
    # Моника никак не реагирует и молча выходит
    mt "Да пошел ты!"
    mt "Никчемный человечишко!"
    return

label gallery_34685:
    # Моника с воинственным, злым видом заходит в холл
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.5
    music Pyro_Flow
    imgfl 34588
    w
    imgf 34589
    mt "Сейчас я с тобой разберусь, сучка!"
    imgd 34590
    mt "Я тебе!.."
    # Моника замолкает в недоумении, т.к. Линда к ней обращается очень дружелюбно
#    music Groove2_85
    imgd 34591
    linda "[monica_hotel_name], привет!"
    music stop
    sound plastinka1b
    img 34592 hpunch
    w
    music Groove2_85
    imgf 34593
    sound2 kiss1
    w
    # Линда наклоняется и целует ее в щеку
    # у Моники ступор, она ожидала совсем иного
    imgd 34594
    mt "Что происходит?!"
    mt "?!"
    # Линда берет Монику за руку
    imgf 34595
    linda "Я так рада, что ты пришла!"
    linda "Знаешь, я уже давно хотела позвать к себе в гости!"
    linda "Проходи скорее!"
    imgd 34596
    linda "Пойдем поболтаем немного, посекретничаем. Хи-хи!" # подмигивает ей
    # Моника молчит и смотрит на Линду с подозрением
    imgd 34597
    sound highheels_short_walk
    w
    img 34598
    m "???"
    # затемнение, звук каблуков
    # смена кадра, они заходят в гостиную Линды, Моника оглядывается
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    # если была сцена с Олафом и Линдой
    if monicaBiffInvestorDate8 == True:
        #
        $ notif(_("Моника узнала из разговора Олафа и Линды, что он оплачивает аренду ее апартаментов."))
        #
        imgfl 34599
        w
        sound highheels_short_walk
        imgf 34600
        w
        imgd 34601
        mt "Так вот какие апартаменты тюфяк Олаф оплачивает этой стерве!"
        mt "Какая-то проститутка-эскортница живет в таких условиях!"
        mt "Интересно, кретин Мэйсон знает о ее интрижке с Олафом?"
        # если Моника арендует квартиру у Джека
        if slumsApartmentsRentActive == True:
            imgf 34602
            mt "А я, Моника Бакфетт, леди и владелица многомиллионного бизнеса..."
            mt "Вынуждена арендовать грязную дыру в трущобах!"
            mt "!!!"
            #
    # если сцены с Олафом и Линдой не было
    else:
        imgf 34601
        mt "Так вот в каких апартаментах живет эта стерва!"
        mt "Думаю, что аренду ей опачивает этот кретин Мэйсон!"
        # если Моника арендует квартиру у Джека
        if slumsApartmentsRentActive == True:
            imgd 34602
            mt "А я, Моника Бакфетт, леди и владелица многомиллионного бизнеса..."
            mt "Вынуждена арендовать грязную дыру в трущобах!"
            mt "!!!"
            #
    # Линда продолжает вести себя очень гостеприимно, мило улыбается Монике
    imgd 34603
    linda "[monica_hotel_name], присаживайся."
    # Моника садится на софу у стола
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 34604
    w
    imgf 34605
    linda "Может, вина?"
    linda "Какое вино ты предпочитаешь, [monica_hotel_name]?"
    m "..."
    # Моника продолжает смтреть на нее с подозрением
    ## вставить фразы Линды, что она сходит на кухню за вином и бокалами
    imgd 34607
    sound highheels_short_walk
    linda "Я принесу свое любимое вино."
    linda "Сейчас я схожу за ним. Подожди минутку."
    imgd 34606
    mt "Что ей от меня нужно?!"
    mt "?!"
    sound highheels_short_walk
    imgf 34633
    w
    fadeblack
    sound pour_wine
    pause 2.0
    music Groove2_85
    imgf 34608
    w
    imgd 34634
    w
    fadeblack 1.5
    music Groove2_85
    imgfl 34609
    w
    # Линда протягивает ей бокал вина, Моника берет его в руки, но не пьет
    sound highheels_short_walk
    imgf 34610
    linda "Это мое любимое вино."
    linda "Попробуй, [monica_hotel_name]."
    imgd 34612
    linda "Думаю, что ты, как девушка, посещающая элитные тусовки нашего города..."
    # Линда подмигивает Монике, мило улыбаясь
    sound Jump1
    img 34611
    linda "И привыкшая только к самому изысканному и дорогому вину, оценишь мой выбор."
    # Линда садится на диван, который стоит напротив софы, на которой сидит Моника
    sound highheels_short_walk
    imgf 34613
    mt "На что она намекает?"
    mt "С чего она взяла, что я посещаю элитные мероприятия?"
    music Stealth_Groover
    imgd 34614
    mt "Так, Моника!"
    mt "Пора расставить все на свои места!"
    mt "Хватит играть в какие-то недомолвки и загадки!"
    # Моника с вызовом
    imgf 34615
    m "С чего ты взяла, что я посещаю подобные мероприятия?!"
    # Линда ее перебивает
    linda "[monica_hotel_name], если ты занимаешь место руководителя в офисе Моники Бакфетт..."
    # Моника резко
    imgd 34616
    m "Я не Миссис Бакфетт!"
    linda "Я видела тебя в ее кресле!"
    m "Ты меня с ней перепутала!"
    m "Я [monica_hotel_name]!"
    # молча сверлят друг друга взглядами
    imgd 34617
    m "!!!"
    linda "..."
    # Линда прерывает паузу, говоря примирительно
    music Groove2_85
    imgf 34618
    linda "[monica_hotel_name], я не хочу с тобой спорить."
    linda "И я верю тебе..."
    m "Вот как?!" # удивленно
    linda "Да..."
    linda "Я поняла, что это ты была в кресле Бакфетт... Но я поняла, что ты - не Бакфетт..."
    # Моника ничего не понимая, удивленно
    imgd 34619
    m "Ты сама сейчас поняла, что сказала?"
    m "???"
    # Линда смеется дружелюбно
    linda "Я посмотрела фотографии настоящей Миссис Бакфетт..."
    m "И?.."
    linda "У нее грудь меньше, чем у тебя."
    linda "Так что я определила подмену. Хи-хи-хи!"
    m "!!!"
    img 34606
    mt "Какого черта?!"
    # если был секс с Адриано
    if monicaAdrianoEscortHotel4 > day:
        #
        $ notif(_("Адриано сказал, что попы у [monica_hotel_name] и у Моники разные."))
        #
        mt "Сначала этот никчемный Адриано что у меня попа больше, чем у Моники Бакфетт!"
        mt "Теперь эта овца!"
        mt "Почему они все говорят, что я отличаюсь от самой себя?!"
        mt "Это не так!"
        mt "Одни идиоты вокруг!"
        mt "!!!"
        #
    # Моника подозрительно
    imgf 34620
    m "Подмену? О какой подмене ты говоришь?"
    linda "Я поняла, что настоящая Моника Бакфетт наняла тебя, как своего двойника..."
    linda "Потому что ты на нее очень похожа, [monica_hotel_name]."
    linda "Наверняка, ты проводишь фотосессии вместо нее, посещаешь какие-то мероприятия, проводишь кастинги..."
    linda "В общем, делаешь то, на что у Миссис Бакфетт нет времени."
    # Моника в шоке
    img 34621 vpunch
    mt "!!!"
    # Линда продолжает свою "разоблачительную" речь
    imgd 34622
    linda "Я навела справки..."
    linda "Мне сказали, что настоящая Моника Бакфетт отдыхает сейчас на островах..."
    linda "Она устала от деловой активности и ей требуется время, чтобы восстановить свои силы."
    linda "Но для того, чтобы не было простоя в бизнесе..."
    linda "И чтобы больше заработать денег..."
    linda "Она решилась на кардинальную смену курса журнала."
    linda "И улетела отдыхать, оставив в кресле босса своего двойника..."
    img 34621
    mt "!!!"
    imgf 34623
    linda "Тебя, [monica_hotel_name], выбрали как ее двойника только из-за внешнего сходства..."
    linda "Вы и правда удивительно похожи!"
    linda "Скажи, ведь это ты снимаешься в этих откровенных фотосессиях для журнала?"
    linda "Настоящая Бакфетт ни за что не согласилась бы на подобное!"
    linda "Говорят, что она очень строгая леди!"
    # Моника в замешательстве
    imgd 34624
    m "Я... Кхм..."
    music Pyro_Flow
    imgd 34625
    mt "Вот черт!"
    mt "И что мне теперь делать?"
    mt "Продолжать настаивать на том, что я не имею отношения к работе в офисе?"
    mt "Или согласиться с ее версией?"
    music Stealth_Groover
    mt "Хмм... Удивительно, что ее версия поразительно схожа с тем, что обо мне думает мерзавец Биф!.."
    mt "У этих двух людишек, Линды и Бифа, похоже, есть нечто общее..."
    mt "А именно - отсутствие мозгов!"
    mt "!!!"
    # Линда продолжает говорить, делает это дружелюбно, без наездов
    music Groove2_85
    imgf 34626
    linda "[monica_hotel_name], знаешь, я прекрасно понимаю, почему ты работаешь в эскорте..."
    linda "Я слышала, что Миссис Бакфетт легко увольняет людей за малейшую оплошность."
    linda "Поэтому ты в любой момент можешь остаться без этой работы двойником... Соответственно, и без дохода..."
    linda "Работа в нашем ВИП-эскорте для тебя, как страховка. Я права?"
    # Моника продолжает молчать, не приняв решения, какой линии поведения придерживаться
    imgd 34627
    m "..."
    linda "Слушай, [monica_hotel_name]..."
    linda "В тот вечер, когда мы встретились с тобой в кабинете Бакфетт..."
    linda "Ты не подумай, я не обижаюсь на тебя за отказ."
    imgf 34628
    mt "Хммм... С трудом в это верится, сучка лицемерная!"
    imgd 34629
    linda "Я знаю, что Мэйсон договорился обо всем и дело было уже почти решено..."
    linda "Но оставалось получить согласие самой Моники Бакфетт..."
    linda "И я понимаю, что отказала мне не ты..."
    linda "Ты сделала это по приказу настоящей Бакфетт."
    linda "Наверное, она позвонила тебе или как-то вышла с тобой на связь..."
    linda "И приказала поступить именно таким образом."
    m "..."
    # Линда с интересом, внимательно глядя на Монику
    imgd 34630
    linda "Ты ведь общаешься с Миссис Бакфетт по рабочим моментам, [monica_hotel_name]?"
    linda "И, наверняка, лично знакома с ней..."
    # Моника задумчиво
    music Stealth_Groover
    imgf 34631
    mt "Моника, феерическая глупость овцы Линды тебе сейчас на руку!"
    mt "Хорошо, что она сделала такие выводы."
    mt "Пусть думает, что я являюсь двойником Моники Бакфетт!"
    mt "Все, что тебе нужно сделать - это подыграть ей."
    m "..."
    menu:
        "Сказать, что Моника общается с настоящей Бакфетт.":
            pass
    # Моника, натягивая притворную улыбку, говорит Линде
    # та внимательно ее слушает
    imgd 34632
    m "Да, Линда, ты права."
    m "Мы с Миссис Бакфетт поддерживаем связь, обсуждая некоторые моменты по работе в офисе..."
    linda "Я так и знала, что моя теория верна!"
    # Моника продолжает притворно ей улыбаться
    # Линда очень заинтересованно спрашивает
    music Groove2_85
    imgd 34635
    linda "[monica_hotel_name], скажи мне по секрету..."
    linda "Этот отказ на моем кастинге... Это был отказ со стороны настоящей Миссис Бакфетт?"
    m "Да..."
    # Линда уже крайне заинтересованно спрашивает
    linda "А почему она отказала?"
    linda "Она говорила тебе что-нибудь об этом?"
    # Моника начинает высокомерничать
    music Stealth_Groover
    imgf 34636
    m "Ну, как тебе сказать, Линда?.."
    m "Ты видела модель, Мелани, которая снимается в этом журнале?"
    m "Или посмотри на меня... Я тоже часто участвую в съемках..."
    m "Твои внешние данные, Линда, не соответствуют нашим."
    m "В качестве модели может выступать девушка только с яркой, запоминающей внешностью."
    m "У посредственных девушек нет никаких шансов попасть в фотостудию моего... То есть нашего журнала."
    # Линда немного расстроенно
    img 34637 vpunch
    linda "Миссис Бакфетт так и сказала?"
    m "Да, Линда."
    m "Она сказала, что у тебя не достаточно хорошие внешние данные для ее журнала..."
    # Линда начинает закидывать удочку
    music Groove2_85
    imgf 34626
    linda "Да, я понимаю, [monica_hotel_name]..."
    linda "Но предполагаю, что все это условно."
    m "В смысле?"
    linda "Я думаю, что, скорее всего, это просто каприз Миссис Бакфетт."
    linda "На самом деле у меня есть все шансы попасть на обложку ее журнала."
    imgd 34606
    mt "Самооценка просто зашкаливает..."
    mt "..."
    # если была фотосессия с Викторией
    if melanieAlexVictoriaSex2 == True:
        #
        $ notif(_("У Виктории была фотосессия с Алексом в офисе Моники."))
        #
        imgf 34638
        linda "Не так давно я видела кадры со съемки какой-то девочки в розовом платье..."
        linda "И под снимками было написано, что это работа фотографа Модного журнала."
        linda "Но ведь она совсем не соответствует стандартам... У нее далеко не модельная внешность."
        # Моника зло
        imgd 34625
        mt "Белобрысая сучка Виктория так не считает!"
        mt "!!!"
        #
    imgf 34639
    linda "[monica_hotel_name], я хотела спросить у тебя..."
    # Линда с надеждой спрашивает у Моники
    linda "Ты же можешь повлиять на Миссис Бакфетт, чтобы она согласилась меня взять?"
    linda "Ты же общаешься с ней..."
    music Power_Bots_Loop
    imgd 34640
    mt "Так вот ты чего хочешь от меня, лицемерая стерва?!"
    mt "Решила, что с моей помощью ты сделаешь себе карьеру модели?!"
    mt "!!!"
    # Моника продолжает строить из себя
    music Stealth_Groover
    imgf 34641
    m "Конечно, Моника Бакфетт меня слушает!"
    m "Ведь у меня изысканный вкус..."
    music Groove2_85
    linda "Глядя на тебя, любой поймет, что ты очень тонкая натура!"
    linda "И что у тебя очень хороший вкус!"
    linda "Поэтому я уверена, что настоящая Моника Бакфетт прислушивается к тебе!"
    mt "?!"
    imgd 34642
    linda "Так ты поговоришь с Миссис Бакфетт о моей кандидатуре, [monica_hotel_name]?"
    m "Ну не знаю, Линда..."
    m "Я не могу принимать такие серьезные решения, предварительно не обумав..."
    # Линда начинает к ней подлизываться
    music Hidden_Agenda
    linda "[monica_hotel_name], знаешь, когда ты впервые пришла в ВИП-эскорт..."
    #
    $ notif(_("У Моники всегда были плохие отношения с Линдой."))
    #
    linda "Я поняла, что ты очень добрая и хорошая."
    # Моника изображает удивление
    img 34643
    m "Правда?!"
#    music Power_Bots_Loop
    imgd 34644
    mt "Мерзкая лицемерка!"
    mt "!!!"
    imgf 34643
    linda "Да, [monica_hotel_name]. Это правда!"
    linda "Я сразу прониклась симпатией к тебе!"
    linda "Между прочим, я была против того ужасного кастинга, который тебе устроила наша администираторша!"
    linda "В отличие от Кэндис и Эбби!"
    imgd 34644
    mt "Как интересно..."
    mt "Неужели эта Линда думает, что может так легко обмануть меня?"
    mt "Если у нее это получается легко сделать с мужчинами, которые только и мечтают о всяких извращенствах..."
    mt "То с такой умной и проницательной женщиной, как Я, у нее этот фокус не пройдет!"
    imgf 34645
    m "..."
    m "А что Кэндис с Эбби? Они что-то говорили против меня?"
    # Линда продолжает с воодушевлением
    linda "Да, [monica_hotel_name]!"
    linda "Эти две стервы постоянно говорят про тебя всякие гадости!"
    if ep218_quests_escort_completed_day > 0:
        #
        $ notif(_("Кэндис и Эбби являются 'подругами' Моники."))
        #
    linda "Они мне сказали, что ты всех ненавидишь и считаешь себя лучше других!"
    linda "Называли тебя высокомерной сучкой и лгуньей!"
    m "..."
    imgd 34646
    linda "Я говорила им о том, что некрасиво так высказываться в твой адрес. Что это гнусная клевета!"
    linda "Они лишь смеялись в ответ. И еще меня назвали глупой."
    linda "В общем, они постоянно пытаются настроить меня и Миранду против тебя..." # с сожалением
    m "Миранда, это твоя подруга из эскорта?"
    linda "Да. И Миранда к тебе тоже очень хорошо относится..."
    #
    $ notif(_("У Моники всегда были плохие отношения с Мирандой."))
    #
    music Pyro_Flow
    img 34647 vpunch
    m "Миранда ко мне хорошо относится?!"
    m "Ты шутишь?!"
    # Линда с нарочитой искренностью
    music Groove2_85
    linda "Нет, [monica_hotel_name], какие тут могут быть шутки?!"
    linda "Мы часто с Мирандой говорим о том, что было бы здорово дружить с тобой!"
    linda "Жаль, что я только сейчас тебе решилась рассказать все..."
    linda "Нужно было сделать это в первый же день твоей работы в эскорте."
    linda "Мы давно бы уже были бы близкими подругами с тобой!"
    # Моника притворно улыбается
    music Stealth_Groover
    imgf 34631
    mt "О, Боги! Какой бурный поток лести!"
    mt "Я немного отвыкла от такого со времен..."
    mt "В общим, с тех времен, когда была сама собой и не была вынуждена притворяться своим же двойником!"
    # Линда услужливо
    imgd 34648
    linda "[monica_hotel_name], как тебе вино? Нравится?"
    linda "Если тебе не очень нравися, я могу принести другого вина."
    linda "У меня как раз есть бутылка прекрасного вина для особо дорогих мне гостей!"
    # Моника надменно
    m "Не нужно, Линда..."
    # Линда с милой улыбкой
    imgd 34649
    linda "Если вдруг передумаешь, я с радостью угощу тебя, [monica_hotel_name]!"
    # затемнение
    # спустя некоторое время, звонок в дверь, каблуки
    # смена кадра, холл
    # в холле стоят Линда и только что пришедшая Миранда, они шепчутся
    fadeblack
    sound snd_door_bell1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 34651
    w
    imgf 34650
    linda "Миранда, какого черта ты пришла?!"
    linda "Я же тебе говорила, что сама с ней буду договариваться!"
    miranda "Я решила, что могу тебе помочь, если что-то пойдет не так."
    miranda "Я же хочу тебя поддержать, по-дружески..."
    imgd 34652
    linda "Ну ладно, проходи."
    linda "Я как раз рассказывала ей, как мы хотим дружить с ней."
    miranda "Про меня тоже говорила?"
    linda "Да, говорила. В общем, все идет по плану, Миранда."
    miranda "Пошли, я тоже хочу с ней пообщаться!"
    # затемнение
    # Миранда заходит в гостиную и изображает удивление
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Hidden_Agenda
    imgfl 34653
    miranda "Ой, [monica_hotel_name], вот это сюрприз!"
    miranda "Привет! Рада тебя видеть!"
    # Миранда подходит к Монике и чмокает ее в щечку
    sound highheels_short_walk
    imgf 34654
    w
    imgd 34655
    sound kiss1
    m "!!!"
    sound2 highheels_short_walk
    imgf 34661
    w
    # Моника офигевает
    music Power_Bots_Loop
    imgd 34656
    mt "Мерзкая сучка Миранда собственной персоной!"
    mt "Она что, тоже собирается рассказывать мне, как она мечтает дружить со мной?!"
    mt "Ненавижу эту дрянь!"
    mt "!!!"
    # Миранда садится на диван рядом с Линдой и тоже начинает подлизываться к Монике
    music Groove2_85
    imgf 34657
    miranda "А я тут была недалеко по делам и решила зайти к Линде ненадолго."
    linda "Миранда, будешь вино?"
    miranda "Да, не откажусь."
    miranda "Сегодня был непростой день."
    miranda "Зато я неплохо заработала на одном денежном мешке!"
    imgd 34658
    miranda "Я таких тюфяков люблю."
    miranda "Возни с ними мало, а на чаевых можно заработать столько, как за несколько рабочих дней!"
    miranda "Хорошо, что он мой постоянный клиент!"
    miranda "А у вас как дела, девочки?"
    miranda "[monica_hotel_name], как ты сегодня отработала?"
    # Моника смотрит на нее зло
    music Stealth_Groover
    imgd 34659
    m "Не так хорошо по чаевым, как ты!"
    mt "Сучка!!!"
    mt "!!!"
    # Линда говорит Миранде
    music Groove2_85
    imgf 34660
    linda "Мы тут как раз говорили о работе..."
    linda "Я рассказывала, что хочу стать моделью и уйти из ВИП-эскорта."
    miranda "Я очень надеюсь, что у тебя это получится, Линда!"
    linda "Спасибо за поддержку, подруга."
    # Миранда говорит Монике
    imgd 34662
    miranda "Но до того, как Линда загорелась этой идеей с модельным бизнесом..."
    miranda "Мы планировали, что сместим администраторшу с ее насиженного места..."
    miranda "И что Линда станет главной в ВИП-эскорте!"
    # Моника удивленно смотрит на них
    if ep218_quests_escort_completed_day > 0:
        img 34625 vpunch
        mt "У меня дежавю?"
        #
        $ notif(_("Кэндис и Эбби тоже хотят сместить администраторшу. Эбби планирует занять ее место."))
        #
        mt "?!"
    imgf 34663
    m "Вы хотите сместить администраторшу?!"
    linda "Да, хотим."
    linda "Но так как я собираюсь уходить в модели, то я сначала вышвырну администраторшу из эскорта..."
    linda "Потом отдам ее место Миранде..."
    linda "И только после этого смогу спокойно строить карьеру модели."
    m "..."
    imgd 34664
    m "То есть, вы планируете это сделать уже в ближайшем будущем?"
    miranda "Да, именно!"
    music Hidden_Agenda
    miranda "Я стану главной и буду отдавать тебе, [monica_hotel_name], самых лучших клиентов!.. Раз Линда хочет уйти..."
    linda "Ты будешь хорошо зарабатывать, [monica_hotel_name]!"
    linda "И с клиентами будет только такой интим, который нравится именно тебе!"
    m "Даже так?!"
    # если была сцена мести Миранде с футфетишистом
    if monicaEscortRevengeGirl2 == True:
        #
        $ notif(_("Моника заставила Миранду облизывать ее ноги."))
        #
        imgd 34665
        linda "Да! Мне тут Миранда недавно говорила, что тебе нравится..."
    # если не было сцены мести Миранде
    else:
        #
        $ notif(_("Постоянный клиент Моники любит облизывать ее ноги."))
        #
        imgd 34665
        linda "Да! Мы тут с Мирандой недавно слышали, что тебе нравится..."
        #
    linda "Когда тебе целуют и облизывают ноги!"
    m "!!!"
    imgf 34666
    miranda "В общем, [monica_hotel_name], мы с Линдой предлагаем тебе..."
    miranda "Не оставаться больше в одиночестве, а присоединиться к нам."
    miranda "У нас уже намечен кое-какой план и, поверь, администраторша уже совсем скоро перестанет мозолить нам глаза!"
    linda "Мы познакомим тебя с классными и богатыми клиентами! А, главное, щедрыми!"
    imgd 34667
    linda "Кто знает, может ты сможешь с одним из них устроить свою личную жизнь!"
    linda "И тогда тебе не будет страшно, если Моника Бакфетт вдруг уволит тебя из-за какой-нибудь ерунды!"
    linda "У тебя будет финансовая стабильность!"
    miranda "Ну, что скажешь, [monica_hotel_name]?"
    # Моника делает вид, что сомневается
    music Stealth_Groover
    imgf 34628
    m "Даже не знаю, девочки..."
    m "Это так... Неожиданно..."
    m "А что за план у вас в отношении администраторши?"
    # Миранда ей заговорщицки подмигивает
    music Hidden_Agenda
    imgd 34668
    miranda "Мы тебя обязательно в него посвятим... Позже немного..."
    sound Jump1
    img 34669
    miranda "Мы должны быть уверены, что ты на нашей стороне."
    imgf 34670
    m "Звучит достаточно интересно..."
    m "..."
    linda "Если ты поговоришь с Миссис Бакфетт по поводу моей кандидатуры..."
    linda "Тогда мы сможем приступить к осуществлению нашего плана."
    img 34671
    linda "И все тебе расскажем. Да, Миранда?"
    miranda "Согласна, в этом случае мы точно будем уверены в том, что тебе можно доверять, [monica_hotel_name]."
    # Моника задумчиво
    music Stealth_Groover
    imgf 34672
    mt "Эти две овцы действительно думают, что мной так легко манипулировать?!"
    mt "Они думают, что я поверила в эти сказки про дружбу?!"
    mt "Они меня недооценивают!"
    mt "!!!"
    imgd 34673
    mt "Так, нужно подумать..."
    if ep218_quests_escort_completed_day > 0:
        mt "Мне не удалось узнать от Кэндис и Эбби подробностей плана по смещению администраторши..."
        mt "Возможно, они мне все расскажут скоро..."
        mt "Также возможно, что у них получится воплотить свой план в реальность раньше, чем это сделают Линда с Мирандой."
        mt "Тогда дружба с Линдой и Мирандой будет мне мешать."
        mt "..."
        imgf 34674
        mt "Но также вероятен другой исход..."
        mt "Линда и Миранда, эти две змеи, вышвырнут администраторшу быстрее..."
        mt "Тогда мне невыгодно будет оставаться подружкой Кэндис и Эбби..."
        mt "Черт!"
        mt "Как все непросто, Моника!"
        mt "Нужно принять какое-то решение!"
    mt "Хммм..."
#    music Hidden_Agenda
    imgd 34631
    mt "А что, если?.."
    mt "..."
    mt "Так! Что там эти две безмозглые сучки от меня хотят взамен на их дружбу?"
    mt "Чтобы я поговорила с Моникой Бакфетт?"
    mt "..."
    # бичность
    menu:
        "Согласиться помочь Линде." if monicaBitch == False: # низкая бичность
#            $ monicaLindaMirandaFriendship5 = day # Моника согласилась помочь Линде, без унижений своих новых подружек
            # Моника делает вид, что сомневается
            music Stealth_Groover
            imgf 34675
            m "Даже не знаю, как вам могу пообещать, девочки..."
            m "Линда, а вдруг Миссис Бакфетт не захочет менять своего решения?"
            linda "Я уверена, что Миссис Бакфетт прислушается к тебе, [monica_hotel_name]!"
            linda "Главное, попробуй сделать это при первой же возможности!"
            m "Но я не знаю, когда у меня появится эта возможность..."
            linda "Я готова подождать..."
            menu:
                "Дать согласие.":
                    pass
            imgd 34676
            m "Ну, так уж и быть, Линда."
            m "Я постараюсь переубедить Миссис Бакфетт."
            m "Хотя это будет непросто..."
            # счастливая Линда подскакивает и бежит обниматься с Моникой
            music Hidden_Agenda
            sound2 Jump2
            img 34677 hpunch
            linda "[monica_hotel_name]!"
            linda "Спасибо! Я так рада, что ты согласилась!"
            sound highheels_run2
            imgd 34678
            linda "Ты такая классная!!!"
            linda "Обожаю тебя!!!"
            # Миранда смотрит на них и, улыбаясь, пьет вино
            music Stealth_Groover
            imgf 34679
            m "Я рада, что побывала у тебя в гостях, Линда."
            m "Но мне пора идти. У меня еще дела."
            linda "Приходи ко мне почаще в гости, [monica_hotel_name]!"
            miranda "Как-нибудь и у меня соберемся, девочки, да?"
            # Моника притворно улыбается
            imgd 34680
            m "Да, обязательно..."
            sound highheels_short_walk
            imgf 34681
            w
            fadeblack
            sound snd_door_open1
            pause 1.5
            # уходит, затемнение
            return
        "Согласиться помочь Линде. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
            pass
        "Мне нужно время, чтобы подумать...":
            pass
#        "Мне нужно время, чтобы подумать... (Моника слишком приличная) (disabled)" if monicaBitch == False:
#            pass
    # Моника делает вид, что сомневается
    music Stealth_Groover
    imgf 34675
    m "Даже не знаю, как вам могу пообещать, девочки..."
    m "Линда, а вдруг Миссис Бакфетт не захочет менять своего решения?"
    linda "Я уверена, что Миссис Бакфетт прислушается к тебе, [monica_hotel_name]!"
    linda "Главное, попробуй сделать это при первой же возможности!"
    m "Но я не знаю, когда у меня появится эта возможность..."
    imgd 34676
    m "Я контактирую с ней не так часто... Только когда она мне звонит сама."
    m "И разговаривать с Миссис Бакфетт, скорее всего, придется не один раз..."
    m "Сразу она свое решение не изменит."
    linda "Я готова подождать, [monica_hotel_name]..."
    imgf 34682
    m "Вообще, чаще всего с Бакфетт общается Биф..."
    linda "Фу! Этот урод?!"
    m "Да, он урод!"
    linda "Он мне не понравился! Такой мерзкий тип!"
    m "А мне приходится терпеть его присутствие в офисе, хотя мне он тоже не нравится..."
    m "..."
    m "А если Миссис Бакфетт разозлится и уволит меня? Что я буду тогда делать?"
    music Hidden_Agenda
    imgd 34668
    miranda "Мы, как твои подруги, тебя поддержим, [monica_hotel_name]."
    miranda "Я познакомлю тебя с парочкой богатых клиентов."
    $ gallery_ep219_dialogues3_escort_5_loop_count = 0
label gallery_ep219_dialogues3_escort_5_loop:
    # Моника снова изображает сомнение
#    label video_test:
    music Stealth_Groover
    imgf 34683
    m "Все равно мне нужно еще подумать..."
    m "Возможно, я сразу дала бы свое согласие, но..."
    m "..."
    menu:
        "Я помню, как вы заставили меня раздеться, чтобы принять меня на работу.":
            # Моника злорадно
            label gallery_34719:
            music Stealth_Groover
            imgd 34684
            mt "Сейчас я этим сучкам припомню!.."
            mt "!!!"
            imgf 34685
            m "Я помню, как вы заставили меня раздеться, чтобы принять меня на работу..."
            m "Значит, вы не относились ко мне хорошо, раз так поступили?"
            sound Jump2
            img 34686 vpunch
            m "Поэтому я сомневаюсь, стоит ли мне соглашаться..."
            # Линда вскакивает с дивана
            music Hidden_Agenda
            sound2 Jump1
            img 34687 hpunch
            linda "Нет, [monica_hotel_name], мы никогда не относились к тебе плохо!"
            linda "Да, Миранда?"
            # Миранда тоже встает с дивана
            miranda "Всегда хорошо относились!"
            miranda "Как ты могда так подумать о нас, [monica_hotel_name]?"
            linda "Да и что тут такого, чтобы снять одежду?!"
            imgd 34688
            miranda "Да, что тут такого?! Хочешь, мы сделаем тоже самое?"
            linda "Мы с Мирандой прямо сейчас можем это сделать!"
            linda "Хочешь?"
            m "..."
            # коррапшн
#            $ menu_corruption = [monicaLindaMirandaFriendshipCorruptionRequired1, 0]
            menu:
                "Согласиться.":
#                    $ monicaLindaMirandaFriendship6 = day # Моника заставила раздеться Линду и Миранду в обмен на свое согласие
                    music Stealth_Groover
                    imgf 34689
                    m "Да, я этого хочу!"
                    m "!!!"
                    imgd 34690
                    linda "Если мы это сделаем, ты согласишься помочь мне?"
                    linda "И поговорить с Миссис Бакфетт?"
                    imgd 34691
                    m "Да, Линда, я поговорю с Миссис Бакфетт."
                    # Линда с Мирандой переглядываются заговорщицки
                    music Groove2_85
                    imgf 34692
                    w
                    imgd 34693
                    w
                    # начинают раздеваться, на пол летит лдежда и Линды и Миранды
                    imgf 34694
                    w
                    sound vjuh3
                    img 34695 vpunch
                    w
                    imgf 34696
                    w
                    sound vjuh3
                    img 34697 hpunch
                    w
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Hidden_Agenda
                    # обе стоят перед Моникой голые
                    imgfl 34698
                    w
                    # Моника злорадно смотрит на них
                    imgf 34699
                    miranda "[monica_hotel_name], видишь, как это просто?"
                    m "Вижу, Миранда..."
                    linda "Может, ты хочешь, чтобы мы еще что-нибудь сделали для тебя, [monica_hotel_name]?"
                    imgd 34700
                    linda "Хочешь, я тебе сделаю массаж?"
                    miranda "И я тоже могу сделать массаж!"
                    menu:
                        "Согласиться.":
                            pass
                    music Stealth_Groover
                    imgf 34672
                    m "Да, неплохая идея..."
                    mt "Две лицемерные мерзкие стервы!"
                    mt "Готовы пойти на все ради своих меркантильных интересов!"
                    mt "!!!"
                    # Линда указывает рукой на диван
                    imgd 34701
                    linda "Тогда тебе лучше лечь на диван, [monica_hotel_name]."
                    linda "Чтобы ты лучше расслабилась."
                    linda "И нам с Мирандой так намного удобнее будет."
                    # Моника встает, идет к дивану и ложится на него (не снимая одежды-?)
                    sound highheels_short_walk
                    imgf 34702
                    w
                    fadeblack
                    sound highheels_short_walk
                    pause 2.0
                    music Loved_Up
                    # голая Линда массирует ей плечи, гладит спину
                    # голая Миранда массирует ей поясницу, ноги
                    imgfl 34703
                    w
                    imgf 34704
                    m "Мммм..."
                    imgd 34705
                    w
                    imgf 34706
                    w
                    imgd 34707
                    w
                    imgd 34708
                    w
                    imgf 34709
                    m "Это и правда расслабляет..."
                    m "Миранда, немного активнее!"
                    imgd 34710
                    miranda "А так? Так тебе нравится, [monica_hotel_name]?"
                    imgd 34711
                    m "Да, вот так..."
                    imgf 34712
                    w
                    imgd 34713
                    w
                    sound Jump2
                    img 34714 hpunch
                    m "Так хорошо..."
                    imgf 34715
                    m "Линда, ты делаешь слишком сильно! Мне немного больно!"
                    imgd 34716
                    linda "Ой, [monica_hotel_name], я не специально! Сейчас не больно?"
                    imgf 34717
                    m "Сейчас лучше, Линда."
                    sound Jump1
                    imgd 34718
                    w
                    imgf 34745
                    w
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34719
                    w
                    #sound grabbing3
                    music2 v_Monica_Claire_Oiling2_2
                    imgf 34836
                    w
                    #sound grabbing7
                    imgd 34837
                    w
                    #sound grabbing3
                    imgd 34836
                    w
                    #sound grabbing7
                    imgd 34837
                    w
                    #sound grabbing3
                    imgd 34836
                    w
                    #sound grabbing7
                    imgd 34837
                    w
                    imgf 34838
                    w
                    imgd 34839
                    w
                    imgd 34838
                    w
                    imgd 34839
                    w
                    imgd 34838
                    w
                    imgd 34839
                    w
                    music2 stop
                    imgd 34840
                    ## вставка фразы Линды чтобы Моника перевернулась на спину
                    linda "[monica_hotel_name], а теперь повернись на спину."
                    linda "Хочу, чтобы ты максимально расслабилась..."
                    imgf 34720
                    w
                    ## мысли или ответ Моники
                    imgd 34722
                    mt "Эти глупые сучки готовы на все ради моего согласия!"
                    mt "Как это низко! Фи!"
                    mt "Но мне доставляет удовольствие унижать их..."
                    mt "Никчемные и безполезные существа!"
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34721
                    w
                    imgf 34723
                    w
                    imgd 34724
                    w
                    imgd 34725
                    w
                    imgf 34726
                    m "Мммм..."
                    music2 v_Monica_Claire_Oiling2_2
                    imgd 34727
                    w
                    imgd 34728
                    m "..."
                    imgd 34727
                    w
                    imgd 34728
                    w
                    imgd 34727
                    w
                    imgd 34728
                    w
                    imgf 34729
                    w
                    imgd 34751
                    w
                    imgd 34729
                    w
                    imgd 34751
                    w
                    imgd 34729
                    w
                    imgd 34751
                    w
                    imgd 34729
                    w
                    music2 stop
                    sound2 Jump1
                    img 34730 vpunch
                    w
                    imgd 34731
                    m "Достаточно!"
                    # массаж закончили, Моника поднимается с дивана
                    fadeblack 1.5
                    music Stealth_Groover
                    imgf 34732
                    m "Спасибо, девочки."
                    m "Это было приятно..."
                    # затемнение, шуршание одежды, каблуки
                    # смена кадра после затемнения
                    # Моника и ее новые подружки сидят в гостиной Линды на своих прежних местах
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Groove2_85
                    imgf 34657
                    linda "Ну что, [monica_hotel_name], ты приняла решение?"
                    m "..."
                    pass
                    $ gallery_ep219_dialogues3_escort_5_loop_count += 1
                    if gallery_ep219_dialogues3_escort_5_loop_count < 2:
                        jump gallery_ep219_dialogues3_escort_5_loop
                "Отказаться.":
                    imgd 34689
                    m "Хмм... Пожалуй, нет..."
                    jump gallery_ep219_dialogues3_escort_5_loop
            pass
        "Я помню, как Линда заставила меня работать ее реквизитом.":
            label gallery_34742:
            # Моника злорадно
            music Stealth_Groover
            imgd 34684
            mt "Сейчас я этим сучкам припомню!.."
            mt "!!!"
            imgf 34685
            m "Я помню, как Линда заставила меня работать ее реквизитом..."
            m "Значит, ты, Линда, не относились ко мне хорошо, раз так поступила?"
            m "И мне кажется, что Миранда знает об этом твоем поступке..."
            sound Jump2
            img 34686 vpunch
            m "Поэтому я сомневаюсь, стоит ли мне соглашаться..."
            # Линда вскакивает с дивана
            music Hidden_Agenda
            sound2 Jump1
            img 34687 hpunch
            linda "Нет, [monica_hotel_name], мы никогда не относились к тебе плохо!"
            linda "Да, Миранда?"
            # Миранда тоже встает с дивана
            miranda "Всегда хорошо относились!"
            miranda "Как ты могда так подумать о нас, [monica_hotel_name]?"
            linda "Да и что тут такого, чтобы побыть немного реквизитом?!"
            miranda "Да, что тут такого?! Это очень прикольно! Мы любим так пошутить!"
            imgd 34688
            linda "Мы с Мирандой прямо сейчас можем это сделать!"
            linda "Хочешь?"
            m "..."
            # коррапшн
#            $ menu_corruption = [monicaLindaMirandaFriendshipCorruptionRequired2, 0]
            menu:
                "Согласиться.":
#                    $ monicaLindaMirandaFriendship7 = day # Моника заставила Линду и Миранду стоять столиом в обмен на свое согласие
                    music Stealth_Groover
                    imgf 34689
                    m "Да, я этого хочу!"
                    m "!!!"
                    imgd 34690
                    linda "Если мы это сделаем, ты согласишься помочь мне?"
                    linda "И поговорить с Миссис Бакфетт?"
                    imgd 34691
                    m "Да, Линда, я поговорю с Миссис Бакфетт."
                    m "..."
                    m "Если вы перед тем, как притворяться столиками, разденетесь..."
                    # Линда с Мирандой переглядываются заговорщицки
                    music Groove2_85
                    imgf 34692
                    w
                    imgd 34693
                    w
                    # потом раздеваются, скидывая на пол одежду
                    imgf 34694
                    w
                    sound vjuh3
                    img 34695 vpunch
                    w
                    imgf 34696
                    w
                    sound vjuh3
                    img 34697 hpunch
                    w
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Hidden_Agenda
                    imgf 34698
                    w
                    # голые встают в позу столиков
                    # Моника злорадно смотрит на них
                    sound Jump2
                    imgd 34733
                    w
                    imgf 34734
                    w
                    imgd 34735
                    miranda "[monica_hotel_name], видишь, как это просто?"
                    m "Вижу, Миранда..."
                    linda "Может, ты хочешь, чтобы мы еще что-нибудь сделали для тебя, [monica_hotel_name]?"
                    linda "Хочешь, можешь сложить на мою спину ноги, если они устали?"
                    menu:
                        "Согласиться.":
                            pass
                    music Stealth_Groover
                    imgf 34672
                    m "Да, неплохая идея..."
                    mt "Две лицемерные мерзкие стервы!"
                    mt "Готовы пойти на все ради своих меркантильных интересов!"
                    mt "!!!"
                    # Моника надменно
                    ## решили обыграть, что Моника сядет на Линду, а ноги сложит на Миранду (соответственно фразы Моники в этом ключе)
                    imgd 34736
                    m "Вам нужно ближе подползти ко мне."
                    m "Я хочу посидеть на спине Линды."
                    linda "Да, конечно, [monica_hotel_name]..."
                    m "А свои ножки я сложу на Миранду. Мне так будет удобнее."
                    miranda "Без проблем, [monica_hotel_name]."
                    # голая Линда на четвереньках подползает ближе к Монике
                    # та складывает свои ноги на спину Линды
                    # сидит довольная
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34737
                    w
                    imgf 34738
                    w
                    sound Jump2
                    imgd 34739
                    m "Мммм..."
                    imgf 34740
                    w
                    imgd 34741
                    w
                    imgd 34742
                    w
                    imgf 34743
                    m "Можно и вина немного выпить, чтобы расслабиться..."
                    ## Миранду поменять на Линду
                    m "Линда, подай мне вино!"
                    # Миранда хочет встать
                    ## Линда не сможет встать, так как Моника сидит на ней - просто подаст бокал, так как стоит у стола
                    imgd 34744
                    w
                    imgf 34746
                    w
                    #m "Нет-нет-нет!"
                    #m "Ты ведь мой реквизит, тебе можно сделать это, оставаясь на коленях!"
                    # Миранда ползком приносит Монике вино со стола
                    sound vjuh3
                    imgd 34747
                    m "Спасибо..."
                    # Моника балдеет, сложив ноги на Линду, и делая глоток вина
                    imgd 34748
                    m "Как же хорошо..."
                    imgf 34749
                    w
                    fadeblack
                    sound snd_drinking_water
                    pause 2.0
                    music Stealth_Groover
                    # потом Моника поднимается с софы
                    imgf 34750
                    m "Спасибо, девочки."
                    m "Это было приятно..."
                    # затемнение, шуршание одежды, каблуки
                    # смена кадра после затемнения
                    # Моника и ее новые подружки сидят в гостиной Линды на своих прежних местах
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Groove2_85
                    imgf 34657
                    linda "Ну что, [monica_hotel_name], ты приняла решение?"
                    m "..."
                    pass
                    $ gallery_ep219_dialogues3_escort_5_loop_count += 1
                    if gallery_ep219_dialogues3_escort_5_loop_count < 2:
                        jump gallery_ep219_dialogues3_escort_5_loop
                "Отказаться.":
                    imgd 34689
                    m "Хмм... Пожалуй, нет..."
                    jump gallery_ep219_dialogues3_escort_5_loop
            pass
        "Я помню, как Линда обманула меня с чаевыми клиента Олафа. (disabled)" if monicaBiffInvestorDate5 == False and monicaBiffInvestorDate8 == False: # если это не было
            pass
        "Я помню, как Линда обманула меня с чаевыми клиента Олафа." if monicaBiffInvestorDate5 == True or monicaBiffInvestorDate8 == True:
        #if monicaBiffInvestorDate6 == True: # если это было
            # Моника злорадно
            label gallery_34763:
            music Stealth_Groover
            imgd 34684
            mt "Сейчас я этим сучкам припомню!.."
            mt "!!!"
            imgf 34685
            m "Я помню, как Линда обманула меня с чаевыми клиента Олафа..."
            m "Значит, ты, Линда, не относилась ко мне хорошо, раз так поступила?"
            m "И мне кажется, что Миранда знает об этом твоем поступке..."
            sound Jump2
            img 34686 vpunch
            m "Поэтому я сомневаюсь, стоит ли мне соглашаться..."
            # Линда вскакивает с дивана
            music Hidden_Agenda
            sound2 Jump1
            img 34687 hpunch
            linda "Нет, [monica_hotel_name], мы никогда не относились к тебе плохо!"
            linda "Да, Миранда?"
            # Миранда тоже встает с дивана
            miranda "Всегда хорошо относились!"
            miranda "Как ты могда так подумать о нас, [monica_hotel_name]?"
            linda "Хочешь, я сделаю все, что ты скажешь..."
            linda "Чтобы доказать тебе, что отношусь к тебе очень хорошо!"
            imgd 34688
            miranda "Да, я тоже!"
            linda "Хочешь?"
            m "..."
            # коррапшн
#            $ menu_corruption = [monicaLindaMirandaFriendshipCorruptionRequired3, 0]
            menu:
                "Согласиться.":
#                    $ monicaLindaMirandaFriendship8 = day # Моника заставила Линду и Миранду лизать ей грудь в обмен на свое согласие
                    music Stealth_Groover
                    imgf 34689
                    m "Да, я этого хочу!"
                    m "!!!"
                    imgd 34690
                    linda "Если мы это сделаем, ты согласишься помочь мне?"
                    linda "И поговорить с Миссис Бакфетт?"
                    imgd 34691
                    m "Да, Линда, я поговорю с Миссис Бакфетт."
                    m "..."
                    m "Раздевайтесь!"
                    # Линда с Мирандой переглядываются заговорщицки
                    music Groove2_85
                    imgf 34692
                    w
                    imgd 34693
                    w
                    # потом раздеваются, скидывая на пол одежду
                    imgf 34694
                    w
                    sound vjuh3
                    img 34695 vpunch
                    w
                    imgf 34696
                    w
                    sound vjuh3
                    img 34697 hpunch
                    w
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Hidden_Agenda
                    imgfl 34698
                    w
                    imgf 34699
                    w
                    # обе стоят перед Моникой голые
                    # Моника злорадно смотрит на них
                    imgd 34700
                    miranda "[monica_hotel_name], что нам нужно сделать?"
                    m "Хммм..."
                    menu:
                        "Приласкать груди Моники.":
                            pass
                    music Stealth_Groover
                    imgf 34672
                    m "Я хочу, чтобы вы целовали мою грудь..."
                    mt "Две лицемерные мерзкие стервы!"
                    mt "Готовы пойти на все ради своих меркантильных интересов!"
                    mt "!!!"
                    # Линда указывает рукой на диван
                    imgd 34701
                    linda "Тогда тебе лучше лечь на диван, [monica_hotel_name]."
                    linda "Чтобы ты лучше расслабилась."
                    linda "И нам с Мирандой так намного удобнее будет."
                    # Моника встает, идет к дивану и ложится на него (не снимая одежды-?)
                    # голая Линда проводит уками по груди Моники и приспускает платье
                    # голая Миранда наклоняется и елует соски Моники на онойгруди, а Линда - на второй
                    sound highheels_short_walk
                    imgf 34702
                    w
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34752
                    w
                    imgf 34753
                    w
                    imgd 34754
                    m "Мммм..."
                    imgd 34755
                    m "Это и правда расслабляет..."
                    imgf 34756
                    m "Миранда, немного активнее!"
                    miranda "..."
                    imgd 34757
                    w
                    sound vjuh3
                    img 34758 vpunch
                    w
                    sound lick3
                    imgf 34759
                    m "Да, вот так..."
                    m "Так хорошо..."
                    imgd 34760
                    m "Линда, ты тоже!"
                    linda "..."
                    sound lick3
                    imgd 34761
                    w
                    sound vjuh3
                    sound2 lick3
                    img 34762 vpunch
                    w
                    sound lick3
                    imgd 34763
                    m "Сейчас лучше, Линда."
                    sound lick3
                    imgf 34764
                    w
                    sound lick3
                    imgd 34765
                    m "Мммм..."
                    sound lick3
                    imgf 34766
                    m "Достаточно!"
                    # после окончания ласк, Моника поднимается с дивана
                    fadeblack 1.5
                    music Stealth_Groover
                    imgf 34767
                    m "Спасибо, девочки."
                    imgd 34790
                    m "Это было приятно..."
                    # затемнение, шуршание одежды, каблуки
                    # смена кадра после затемнения
                    # Моника и ее новые подружки сидят в гостиной Линды на своих прежних местах
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Groove2_85
                    imgf 34657
                    linda "Ну что, [monica_hotel_name], ты приняла решение?"
                    m "..."
                    pass
                    $ gallery_ep219_dialogues3_escort_5_loop_count += 1
                    if gallery_ep219_dialogues3_escort_5_loop_count < 2:
                        jump gallery_ep219_dialogues3_escort_5_loop
                "Отказаться.":
                    imgd 34689
                    m "Хмм... Пожалуй, нет..."
                    jump gallery_ep219_dialogues3_escort_5_loop
            pass
#        "Я помню, как Миранда подставила меня перед женой своего клиента. (disabled)" if monicaEscortAngryWife1 == False: # если это не было
#            pass
        "Я помню, как Миранда подставила меня перед женой своего клиента.":
        #if monicaEscortAngryWife1 == True: # если это было
            # Моника злорадно
            label gallery_34778:
            music Stealth_Groover
            imgd 34684
            mt "Сейчас я этим сучкам припомню!.."
            mt "!!!"
            imgf 34685
            m "Я помню, как Миранда подставила меня перед женой своего клиента..."
            m "Значит, ты, Миранда, не относилась ко мне хорошо, раз так поступила?"
            sound Jump2
            img 34686 vpunch
            m "И мне кажется, что Линда знает об этом твоем поступке..."
            m "Поэтому я сомневаюсь, стоит ли мне соглашаться..."
            # Миранда вскакивает с дивана
            music Hidden_Agenda
            sound2 Jump1
            img 34687 hpunch
            miranda "Нет, [monica_hotel_name], мы никогда не относились к тебе плохо!"
            miranda "Да, Линда?"
            # Линда тоже встает с дивана
            linda "Всегда хорошо относились!"
            linda "Как ты могда так подумать о нас, [monica_hotel_name]?"
            miranda "Хочешь, я сделаю все, что ты скажешь..."
            miranda "Чтобы доказать тебе, что отношусь к тебе очень хорошо!"
            imgd 34688
            linda "Да, я тоже!"
            miranda "Хочешь?"
            m "..."
            # коррапшн
#            $ menu_corruption = [monicaLindaMirandaFriendshipCorruptionRequired4, 0]
            menu:
                "Согласиться. (Extra version) (disabled)" if game.extra == False:
                    pass
                "Согласиться." if game.extra == True: # в экстру
#                    $ monicaLindaMirandaFriendship9 = day # Моника заставила Линду и Миранду облизывать ей ноги в обмен на свое согласие
                    music Stealth_Groover
                    imgf 34689
                    m "Да, я этого хочу!"
                    m "!!!"
                    imgd 34690
                    linda "Если мы это сделаем, ты согласишься помочь мне?"
                    linda "И поговорить с Миссис Бакфетт?"
                    imgd 34691
                    m "Да, Линда, я поговорю с Миссис Бакфетт."
                    m "..."
                    m "Раздевайтесь!"
                    # Линда с Мирандой переглядываются заговорщицки
                    music Groove2_85
                    imgf 34692
                    w
                    imgd 34693
                    w
                    # потом раздеваются, скидывая на пол одежду
                    imgf 34694
                    w
                    sound vjuh3
                    img 34695 vpunch
                    w
                    imgf 34696
                    w
                    sound vjuh3
                    img 34697 hpunch
                    w
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Hidden_Agenda
                    imgfl 34698
                    w
                    imgf 34699
                    w
                    # обе стоят перед Моникой голые
                    # Моника злорадно смотрит на них
                    imgd 34700
                    miranda "[monica_hotel_name], что нам нужно сделать?"
                    m "Хммм..."
                    menu:
                        "Целовать ноги Моники.":
                            pass
                    music Stealth_Groover
                    imgf 34672
                    m "Я хочу, чтобы вы целовали мои ноги..."
                    mt "Две лицемерные мерзкие стервы!"
                    mt "Готовы пойти на все ради своих меркантильных интересов!"
                    mt "!!!"
                    # Линда указывает рукой на диван
                    ## Моника останется на кушетке - там больше места (возле дивана стол мешает)
                    linda "Конечно, [monica_hotel_name], мы сделаем это с удовольствием."
                    miranda "Я знаю, что ты это любишь, и хочу, чтобы ты расслабилась."
                    # Моника встает, идет к дивану и ложится на него (не снимая одежды-?)
                    # голые Линда и Миранда сидят возле ног Моники и начинают целовать ступни
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34768
                    w
                    imgf 34769
                    w
                    imgd 34770
                    m "Мммм..."
                    imgf 34771
                    sound kiss1
                    w
                    sound2 kiss1
                    imgd 34772
                    w
                    sound lick3
                    imgd 34773
                    m "Это и правда расслабляет..."
                    sound kiss1
                    imgd 34772
                    w
                    sound kiss1
                    imgd 34771
                    w
                    sound kiss1
                    imgd 34772
                    w
                    sound lick3
                    imgd 34773
                    w
                    imgf 34774
                    m "Миранда, оближи мои пальчики!"
                    imgd 34775
                    sound kiss1
                    w
                    sound2 kiss1
                    imgd 34776
                    w
                    imgd 34775
                    sound kiss1
                    w
                    imgd 34776
                    sound kiss1
                    w
                    sound2 lick3
                    imgd 34777
                    miranda "Тебе нравится, [monica_hotel_name]?"
                    imgf 34779
                    m "Да, вот так..."
                    imgd 34778
                    m "Так хорошо..."
                    m "Линда, ты тоже! Облизывай мои пальчики!"
                    imgf 34780
                    w
                    sound lick3
                    imgd 34781
                    w
                    sound lick3
                    imgd 34780
                    w
                    sound lick3
                    imgd 34781
                    w
                    sound lick3
                    imgd 34780
                    w
                    sound lick3
                    imgd 34781
                    w
                    sound kiss1
                    imgd 34782
                    linda "Вот так, [monica_hotel_name]?"
                    imgf 34783
                    m "Да так, Линда."
                    imgd 34784
                    m "Мммм..."
                    imgf 34785
                    sound lick3
                    w
                    imgd 34786
                    sound kiss1
                    w
                    imgf 34787
                    m "Достаточно!"
                    # поцелую ног закончены, Моника поднимается с дивана
                    fadeblack 1.5
                    music Stealth_Groover
                    imgf 34788
                    m "Спасибо, девочки."
                    imgd 34789
                    m "Это было приятно..."
                    # затемнение, шуршание одежды, каблуки
                    # смена кадра после затемнения
                    # Моника и ее новые подружки сидят в гостиной Линды на своих прежних местах
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Groove2_85
                    imgf 34657
                    linda "Ну что, [monica_hotel_name], ты приняла решение?"
                    m "..."
                    pass
                    $ gallery_ep219_dialogues3_escort_5_loop_count += 1
                    if gallery_ep219_dialogues3_escort_5_loop_count < 2:
                        jump gallery_ep219_dialogues3_escort_5_loop
                "Отказаться.":
                    imgd 34689
                    m "Хмм... Пожалуй, нет..."
                    jump gallery_ep219_dialogues3_escort_5_loop
            pass
        "Я помню, как вы хотели заставить лизать ваши киски.":
            # Моника злорадно
            label gallery_34820:
            music Stealth_Groover
            imgd 34684
            mt "Сейчас я этим сучкам припомню!.."
            mt "!!!"
            imgf 34685
            m "Я помню, как вы хотели заставить лизать ваши киски..."
            m "Значит, вы не относились ко мне хорошо, раз так поступили?"
            sound Jump2
            img 34686 vpunch
            m "Поэтому я сомневаюсь, стоит ли мне соглашаться..."
            # Линда вскакивает с дивана
            music Hidden_Agenda
            sound2 Jump1
            img 34687 hpunch
            linda "Нет, [monica_hotel_name], мы никогда не относились к тебе плохо!"
            linda "Да, Миранда?"
            # Миранда тоже встает с дивана
            miranda "Всегда хорошо относились!"
            miranda "Как ты могда так подумать о нас, [monica_hotel_name]?"
            linda "Да и что тут такого, чтобы полизать киски друг другу?!"
            imgd 34688
            miranda "Да, что тут такого?! Хочешь, мы сделаем это прямо сейчас?"
            linda "Да! Хочешь?"
            m "..."
            # коррапшн
#            $ menu_corruption = [monicaLindaMirandaFriendshipCorruptionRequired5, 0]
            menu:
                "Согласиться.":
#                    $ monicaLindaMirandaFriendship10 = day # Моника заставила Линду и Миранду деласть ей ликинг в обмен на свое согласие
                    music Stealth_Groover
                    imgf 34689
                    m "Да, я этого хочу!"
                    m "!!!"
                    imgd 34690
                    linda "Если мы это сделаем, ты согласишься помочь мне?"
                    linda "И поговорить с Миссис Бакфетт?"
                    imgd 34691
                    m "Да, Линда, я поговорю с Миссис Бакфетт."
                    m "..."
                    m "Если вы перед тем, как ласкать друг другу киски, разденетесь..."
                    # Линда с Мирандой переглядываются заговорщицки
                    music Groove2_85
                    imgf 34692
                    w
                    imgd 34693
                    w
                    # потом раздеваются, скидывая на пол одежду
                    imgf 34694
                    w
                    sound vjuh3
                    img 34695 vpunch
                    w
                    imgf 34696
                    w
                    sound vjuh3
                    img 34697 hpunch
                    w
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Loved_Up
                    imgfl 34698
                    m "Теперь поцелуйтесь!"
                    # сначала Линда опускается на колени перед Мирандой и лижет у нее
                    imgf 34791
                    w
                    imgd 34792
                    w
                    sound kiss1
                    imgf 34793
                    w
                    sound lick3
                    imgd 34794
                    w
                    sound kiss1
                    imgd 34795
                    w
                    sound lick3
                    imgd 34794
                    w
                    sound kiss1
                    imgd 34793
                    w
                    imgf 34796
                    w
                    sound Jump1
                    img 34797 hpunch
                    miranda "Оооо..."
                    imgf 34798
                    w
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34799
                    w
                    imgf 34800
                    w
                    imgd 34801
                    w
                    imgf 34802
                    w
                    sound lick3
                    imgd 34803
                    w
                    sound lick3
                    imgd 34802
                    w
                    sound lick3
                    imgd 34803
                    w
                    sound lick3
                    imgd 34802
                    w
                    sound lick3
                    imgd 34803
                    w
                    sound lick3
                    imgd 34802
                    w
                    sound lick3
                    imgd 34803
                    w
                    imgf 34804
                    w
                    sound woman_moan11
                    imgd 34805
                    miranda "Мммм..."
                    # потом Миранда опускается на колени перед Линдой и лижет у нее
                    #fadeblack 1.5
                    #music Loved_Up
                    sound vjuh3
                    imgf 34793
                    w
                    sound lick3
                    imgd 34794
                    w
                    sound kiss1
                    imgd 34795
                    w
                    imgf 34844
                    w
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34806
                    w
                    imgf 34807
                    w
                    imgd 34808
                    w
                    imgf 34809
                    linda "Оххх!"
                    imgd 34810
                    w
                    sound woman_moan15
                    imgd 34811
                    linda "Да, как прикольно!"
                    imgf 34812
                    w
                    sound lick3
                    imgd 34813
                    w
                    sound lick3
                    imgd 34812
                    w
                    sound lick3
                    imgd 34813
                    w
                    sound lick3
                    imgd 34812
                    w
                    sound lick3
                    imgd 34813
                    w
                    sound lick3
                    imgd 34812
                    w
                    sound lick3
                    imgd 34813
                    linda "Оооо!"
                    # ласки прекратили, обе стоят перед Моникой голые
                    # Моника злорадно смотрит на них
                    fadeblack 1.5
                    music Hidden_Agenda
                    imgf 34699
                    miranda "[monica_hotel_name], видишь, как это просто?"
                    m "Вижу, Миранда..."
                    imgd 34700
                    linda "Может, ты хочешь, чтобы мы еще что-нибудь сделали для тебя, [monica_hotel_name]?"
                    linda "Хочешь, я и тебе полижу киску?"
                    miranda "И я тоже могу сделать это!"
                    menu:
                        "Согласиться.":
                            pass
                    music Stealth_Groover
                    imgf 34672
                    m "Да, неплохая идея..."
                    mt "Две лицемерные мерзкие стервы!"
                    mt "Готовы пойти на все ради своих меркантильных интересов!"
                    mt "!!!"
                    # Линда указывает рукой на диван
                    imgd 34701
                    linda "Тогда тебе лучше лечь на диван, [monica_hotel_name]."
                    linda "Чтобы ты лучше расслабилась."
                    linda "И нам с Мирандой так намного удобнее будет."
                    # Моника встает, идет к дивану и ложится на него (не снимая одежды-?)
                    sound highheels_short_walk
                    imgf 34702
                    w
                    # задирает платье и раздвигет ноги
                    # голые Линда и Миранда по очереди лижут киску Моники
                    # Моника смотрит на них со злорадством
                    fadeblack 1.5
                    music Stealth_Groover
                    imgfl 34814
                    w
                    imgf 34815
                    w
                    sound vjuh3
                    img 34816 hpunch
                    w
                    imgf 34841
                    w
                    sound Jump2
                    imgd 34842
                    w
                    imgf 34843
                    w
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 34817
                    w
                    imgf 34818
                    m "Мммм..."
                    imgd 34819
                    w
                    imgd 34820
                    m "Это и правда расслабляет..."
                    imgf 34821
                    m "Миранда, немного активнее!"
                    imgd 34822
                    w
                    sound lick3
                    imgd 34823
                    m "Да, вот так..."
                    sound lick3
                    imgd 34822
                    w
                    sound lick3
                    imgd 34823
                    w
                    sound lick3
                    imgd 34822
                    w
                    sound lick3
                    imgd 34823
                    w
                    sound lick3
                    imgd 34822
                    w
                    sound lick3
                    imgd 34823
                    w
                    imgf 34824
                    m "Так хорошо..."
                    imgd 34825
                    m "Линда, ты делаешь слишком сильно! Полегче!"
                    imgf 34826
                    w
                    sound lick3
                    imgd 34827
                    w
                    sound lick3
                    imgd 34826
                    w
                    sound lick3
                    imgd 34827
                    w
                    sound lick3
                    imgd 34826
                    w
                    sound lick3
                    imgd 34827
                    w
                    sound lick3
                    imgd 34826
                    w
                    sound lick3
                    imgd 34827
                    w
                    sound ahhh2
                    imgf 34828
                    m "Сейчас лучше, Линда."
                    sound ahhh6
                    imgd 34829
                    w
                    imgf 34830
                    w
                    sound ahhh8
                    imgd 34831
                    m "Мммм..."
                    imgd 34832
                    w
                    imgf 34833
                    m "Достаточно!"
                    # ликинг закончили, Моника поднимается с дивана
                    fadeblack 1.5
                    music Stealth_Groover
                    imgfl 34814
                    w
                    imgf 34834
                    m "Спасибо, девочки."
                    imgd 34835
                    m "Это было приятно..."
                    # затемнение, шуршание одежды, каблуки
                    # смена кадра после затемнения
                    # Моника и ее новые подружки сидят в гостиной Линды на своих прежних местах
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Groove2_85
                    imgf 34657
                    linda "Ну что, [monica_hotel_name], ты приняла решение?"
                    m "..."
                    pass
                    $ gallery_ep219_dialogues3_escort_5_loop_count += 1
                    if gallery_ep219_dialogues3_escort_5_loop_count < 2:
                        jump gallery_ep219_dialogues3_escort_5_loop
                "Отказаться.":
                    imgd 34689
                    m "Хмм... Пожалуй, нет..."
                    jump gallery_ep219_dialogues3_escort_5_loop
            pass
    # Моника снисходительно говорит
    music Stealth_Groover
    imgd 34676
    m "Ну, так уж и быть, Линда."
    m "Я постараюсь переубедить Миссис Бакфетт."
    m "Хотя это будет непросто..."
    # счастливая Линда лезет обниматься с Моникой
    music Hidden_Agenda
    sound2 Jump2
    img 34677 hpunch
    linda "[monica_hotel_name]!"
    linda "Спасибо! Я так рада, что ты согласилась!"
    sound highheels_run2
    img 34678
    linda "Ты такая классная!!!"
    linda "Обожаю тебя!!!"
    # Миранда смотрит на них, улыбаясь
    miranda "!!!"
    # Моника высокомерно
    music Stealth_Groover
    imgf 34679
    m "Я рада, что побывала у тебя в гостях, Линда."
    m "Но мне пора идти. У меня еще дела."
    linda "Приходи ко мне почаще в гости, [monica_hotel_name]!"
    miranda "Как-нибудь и у меня соберемся, девочки, да?"
    # Моника притворно улыбается
    imgd 34680
    m "Да, обязательно..."
    sound highheels_short_walk
    imgf 34681
    w
    fadeblack
    sound snd_door_open1
    pause 1.5
    # уходит, затемнение
    return
