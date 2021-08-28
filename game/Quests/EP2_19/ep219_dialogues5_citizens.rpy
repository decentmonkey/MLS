default monicaCitizen4SlumsApartment1 = 0 # Моника в подъезде согласилась привести к себе незнакомца
default monicaCitizen4SlumsApartment2 = 0 # Моника согласилась оголить грудь и сделать минет незнакомцу
default monicaCitizen4SlumsApartment3 = 0 # Моника согласилась раздеться и раздвинуть ноги для незнакомца
default monicaCitizen4SlumsApartment4 = 0 # Моника согласилась привести к себе незнакомца, встретив его на улице
default monicaCitizen4SlumsApartment5 = 0 # клик на незнакомца на улице, квест активирован
default monicaCitizen4SlumsApartment6 = 0 # Моника согласилась на секс с незнакомцем

default monicaCitizen4Sex_cumzone = 0

define monicaCitizen4SexCorruptionRequired1 = 400 # Моника согласилась на предложение незнакомца и пошла с ним к себе домой
define monicaCitizen4SexCorruptionRequired2 = 450 # Моника согласилась сделать минет незнакомцу
define monicaCitizen4SexCorruptionRequired3 = 550 # Моника согласилась на секс с незнакомцем
define monicaCitizen4SexCorruptionRequired4 = 500 # Моника согласилась на ликинг с незнакомцем

define v_Monica_Citizen4_Blowjob2_1_sound_name = "v_Monica_Citizen4_Blowjob2_1"
define v_Monica_Citizen4_Licking1_1_25_sound_name = "v_Monica_Citizen4_Licking1_1"
define v_Monica_Citizen4_Sex1_1_sound_name = "v_Monica_Citizen4_Sex1_1"

#call ep219_dialogues5_citizens_1b() # при клике на незнакомца на улице
#call ep219_dialogues5_citizens_1() # сцена в подъезде с незнакомцем
#call ep219_dialogues5_citizens_1a() # с незнакомцем в квартире Моники
#call ep219_dialogues5_citizens_2() # разговор с незнакомцем на улице, если отказала в подъезде
#call ep219_dialogues5_citizens_3() # мысли Моники, если отказала незнакомцу в подъезде или выгнала из квартиры


# при условии, что Моника ранее соглашалась на минет незнакомцу
# при клике на него на улице
label ep219_dialogues5_citizens_1b:
    # не рендерить!
    music Groove2_85
    imgr Dial_Citizen_4_3
    citizen4 "Эй, детка!"
    citizen4 "Ты не хочешь доделать свою работу?"
    imgl Dial_begin35_22
    m "Какую еще работу?!"
    citizen4 "Которую прервала та двинутая баба в красном платье!"
    #
    $ notif(_("Перри увидела, что Моника делала незнакомцу минет на улице возле пилона."))
    #
    m "!!!" # зло
    citizen4 "Условия нашей сделки те же: отсасываешь у меня - получаешь $ 100."
    citizen4 "Ну что? Пошли!"
    # нагло берет ее за руку и тянет за собой
    music Stealth_Groover
    imgl Dial_begin35_16
#    m "Эй! Ты что делаешь?!"
    m "Я никуда с тобой не пойду!"
    m "!!!"
    # Моника резко выдергивает свою руку
    # зло на него смотрит
    mt "Я не могу себе этого позволить!"
    mt "Я еще не настолько опустилась!"
    mt "И, надеюсь, этого не произойдет НИКОГДА!"
    imgl Dial_begin35_17
#    m "НЕТ!!!"
    m "Я не собираюсь заключать никакие сделки!!!"
    m "Тем более, с тобой!!!"
    m "Чертов извращенец!"
    music Groove2_85
    imgl Dial_begin35_16
    imgr Dial_Citizen_4_4
    citizen4 "Ну и пошла ты!"
    citizen4 "Видимо, не так уж тебе нужны эти сто баксов..."
    # он уходит
    $ monicaCitizen4SlumsApartment5 = day # клик на незнакомца на улице, квест активирован
    return


# вечером при клике на дом в трущобах Моники, когда Моника идет в свои апартаменты
label ep219_dialogues5_citizens_1:
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
    $ menu_corruption = [monicaCitizen4SexCorruptionRequired1, 0]
    menu:
        "Согласиться на его предложением.":
            $ monicaCitizen4SlumsApartment1 = day # Моника в подъезде согласилась привести к себе незнакомца
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
            return False
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
label ep219_dialogues5_citizens_1a:
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
            return False
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
    $ menu_corruption = [monicaCitizen4SexCorruptionRequired2, 0]
    menu:
        "Оголить грудь и сделать минет.":
            $ monicaCitizen4SlumsApartment2 = day # Моника согласилась оголить грудь и сделать минет незнакомцу
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
            sound anger2
            img 42813 hpunch
            m "Еще раз увижу тебя в своем подъезде - позвоню в полицию!"
            m "Чертов извращенец!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            return False
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
    # тут вспышка, типа его воспоминание
    # кадр из встречи с Перри, когда она застукала Монику за минетом
#    pause 0.7
#    hide screen photoshot_screen
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
    # новая вспышка - опять Перри, только уже якобы она в квартире Моники и стоит рядом с ним
    # Перри орет возмущенно
#    pause 0.7
#    hide screen photoshot_screen
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
    # вспышка - Перри сидит на куштке у Моники в апартаментах, м.б. задрав платье и раздвинув ноги, и довольно говорит
#    pause 0.7
#    hide screen photoshot_screen
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
            $ menu_corruption = [monicaCitizen4SexCorruptionRequired3, 0]
            menu:
                "Сделать, как он говорит.":
                    $ monicaCitizen4SlumsApartment6 = day # Моника согласилась на секс с незнакомцем
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
                    return False
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
                    $ monicaCitizen4Sex_cumzone = 1
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
                    $ monicaCitizen4Sex_cumzone = 2
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
                    $ monicaCitizen4Sex_cumzone = 3
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
            $ menu_corruption = [monicaCitizen4SexCorruptionRequired4, 0]
            menu:
                "Сделать, как он говорит.":
                    $ monicaCitizen4SlumsApartment3 = day # Моника согласилась раздеться и раздвинуть ноги для незнакомца
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
                    return False
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
            call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_82
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
    $ add_money(130.0)
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
    return True


# если Моника отказала незнакомцу в подъезде
# при клике на него на улице
label ep219_dialogues5_citizens_2:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19038
    citizen4 "Эй, детка!"
    citizen4 "Ты решила воспользоваться моим предложением и доделать свою работу?"
    m "!!!" # молчит зло
    imgf 13371
    citizen4 "Условия нашей сделки те же: отсасываешь у меня - получаешь $ 100."
    sound Jump2
    img 42978 hpunch
    citizen4 "Ну что? Пошли!"
    # нагло берет ее за руку и тянет за собой
    music Pyro_Flow
    img 42979
    m "Эй! Ты что делаешь?!"
    m "!!!"
    # Моника выдергивает свою руку
    sound Jump1
    img 42980 vpunch
    m "Я никуда с тобой не собираюсь идти за сто баксов!"
    music Groove2_85
    imgd 10579
    citizen4 "Окей. 130 баксов и ты мне отсасываешь."
    img 10580
    m "Черт!"
    m "!!!"
    # corruption
    $ menu_corruption = [monicaCitizen4SexCorruptionRequired1, 0]
    menu:
        "Согласиться на его предложение.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                music Groove2_85
                imgf 40334
                mt "Хммм..."
                mt "Я могу заработать на этом никчемном придурке $ 130."
                mt "Но мне некуда его вести! А здесь я это делать не собираюсь!"
                mt "С меня хватило прошлого раза, когда я встретила гребаную Перри!"
                #
                $ notif(t_("Монике некуда вести клиентов."))
                #
                # Моника резко выдергивает свою руку
                imgd 10578
                m "Нет!"
                m "Мне некуда тебя вести!"
                imgd 13378
                citizen4 "Видимо, не так уж тебе нужны эти деньги..."
                citizen4 "Окей, найду себе более сговорчивую шлюху!"
                return False
            # если арендует квартиру у Джека
            $ monicaCitizen4SlumsApartment4 = day # Моника согласилась привести к себе незнакомца, встретив его на улице
            pass
        "Отказаться!":
            # Моника зло на него смотрит
            music Pyro_Flow
            imgf 40344
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            # Моника резко выдергивает свою руку
            imgd 10572
            m "НЕТ!!!"
            m "Я не собираюсь заключать никакие сделки!!!"
            m "Тем более, с тобой!!!"
            m "Чертов извращенец!"
            music Groove2_85
            imgd 10579
            citizen4 "Видимо, не так уж тебе нужны эти деньги..."
            citizen4 "Окей, найду себе более сговорчивую шлюху!"
            return False
    # Моника в сомнениях смотрит на него
    music Pyro_Flow
    imgf 40334
    mt "Вот дьявол!"
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."
    #
    $ notif(_("Моника должна выплачивать Перри долг."))
    imgd 19174
    mt "Еще я должна выплачивать долг этой мерзкой извращенке Перри!"
    #
    # выглядывает мамочка
    music Master_Disorder
    img 24343 vpunch
    mt "И эта старая карга следит за мной..."
    img 24344
    #
    music Groove2_85
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 40333
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    imgf 40333
    mt "Моника, что же делать?"
    mt "Этот кретин сказал, что он заплатит $ 130..."
    mt "Хммм..."
    mt "В прошлый раз гребаная Перри застукала меня с этим никчемным неудачником..."
    mt "И я ничего не заработала из-за нее!"
    imgd 42981
    mt "Хотя мне пришлось брать его отвратительный член в свой рот!"
    mt "!!!"
    mt "Если я соглашусь сейчас на его предложение, то никто не сможет мне помешать сделать ему..."
    mt "В общем, доделать это извращенство и получить, наконец-то, мои $ 130!"
    # Моника со злостью вырывает руку
    ## может строчку где она говорит отпусти меня убрать, так как ранее был
    ## комментрарий, что она выдергивает руку в начале и я там уже сделала это
    ## и поэтому здесь он ее уже не держит
    music Stealth_Groover
    imgd 19039
    m "Не смей больше прикасаться ко мне!"
    m "С проститутками в борделе будешь так обращаться!"
    m "Я тебе не какая-то там падшая особа!"
    # он смотрит на нее, еходно улыбаясь
    music Groove2_85
    imgf 10575
    citizen4 "Да? Ха-ха!"
    citizen4 "Ну окей, как скажешь."
    citizen4 "Только пошли уже скорее!"
    citizen4 "У меня уже яйца пухнут!"
    return True
#    jump ep219_dialogues5_citizens_1a


# мысли Моники, если отказала незнакомцу в подъезде или выгнала его из своего дома
label ep219_dialogues5_citizens_3:
    # Моника стоит злая у себя в апартаментах
    music Pyro_Flow
    imgf 42976
    mt "Какой кошмар!"
    mt "Этот никчемный отброс общества сказал, что все знают о моем способе заработка!!!"
    mt "Черт! Этого быть не может!"
    mt "Моника, как ты могла допустить, чтобы о тебе говорили такое?!"
    mt "Если и дальше так пойдет, ты про тебя будут думать как про одну из тех падших женщин!.."
    mt "Которые стоят рядом со старой грымзой на улице!!!"
    mt "..."
    imgd 42977
    mt "Но нет, такого никогда не будет!"
    mt "Никто так не посмеет подумать!"
    mt "Любой видит что перед ним стоит Леди, а не какая-то шлюха!"
    mt "!!!"
    return
