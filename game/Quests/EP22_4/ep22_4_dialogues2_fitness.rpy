default melanieVictoriaFitness1 = 0  # Мелани и Виктория посетили первое занятие в фитнес-зале

#call ep22_4_dialogues2_fitness_1() # разговор Мелани и Виктории на улице перед фитнес-залом
#call ep22_4_dialogues2_fitness_2() # фитнес
#call ep22_4_dialogues2_fitness_3() # разговор Мелани и Виктории на улице после фитнеса

# при условии, что секс-вечеринка у Мелани уже была
# перед входом в фитнес, у здания
# Мелани и Виктория
# Мелани в голубых шортах и желтой рубашке, Виктория в своем рабочем платье
label ep22_4_dialogues2_fitness_1:
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Тем временем...")) from _rcall_textonblack_87
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 43547
    victoria "Ой, подружка Мелани, я так рада, что мы с тобой вместе идем на фитнес!"
    victoria "Хорошие подружки должны все делать вместе."
    victoria "Не только встречаться на девичниках, но и устраивать совместный шоппинг..."
    victoria "Как мы с тобой сделали, чтобы выбрать тебе костюм."
    imgf 43548
    victoria "И на фитнес вместе теперь будем ходить!"
    victoria "Ты рада этому, подружка?"
    imgd 43549
    melanie "Очень..."
    imgf 43550
    victoria "Я знала, что тебе будет приятно заниматься спортом вместе со мной."
    victoria "И вместе с нашими новыми подружками."
    victoria "Кстати, ты, подружка, отлично справилась с выполнением моей просьбы..."
    victoria "На той вечеринке, когда Стефани была у тебя в гостях."
    victoria "Скоро Стефани тоже станет моей лучшей подружкой. Хи-хи-хи!"
    # если Мелани выключила камеру в самом начале сцены со Стефани
    if melanieVictoriaStephanieSwingerParty4 > 0:
        imgd 43551
        victoria "Кстати, подружка Мелани... Хотела сказать тебе..."
        victoria "Подружка Мелани сделала не очень хорошо, выключив камеру."
        victoria "Хоть я и осталась довольна, что она сняла для меня достаточно материала."
        #
    imgd 43552
    melanie "..."
    imgf 43553
    victoria "Я знаю, что ты не будешь ревновать меня к ней."
    victoria "Ты же хорошая подружка?"
    melanie "Я не буду ревновать..."
    melanie "Потому что я хорошая подружка."
    sound snd_woman_laugh3
    imgd 43554
    victoria "Хи-хи-хи!"
    victoria "Ну пошли скорее!"
    victoria "Занятие скоро начнется, а нам с тобой еще нужно переодеться."
    imgd 43555
    melanie "..."
    return

# фитнес
# Мелани и Виктория заходят, их встречает тренер
label ep22_4_dialogues2_fitness_2:
    # он жадно осматривает Мелани с головы до ног, Викторию как-будто и не замечает
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 43560
    fitness_instructor "Добрый день, девочки!"
    fitness_instructor "Я ваш фитнес-инструктор."
    # Мелани равнодушно смотрит на него
    melanie "Добрый день."
    imgf 43561
    fitness_instructor "Добро пожаловать на наше занятие!"
    fitness_instructor "Надеюсь, вам понравится и вы хорошо и с пользой проведете время."
    imgd 43562
    fitness_instructor "И обязательно вернетесь к нам! И не один раз!"
    # Виктория любезничает с ним
    music Hidden_Agenda
    imgd 43563
    victoria "Ой, приятно с вами познакомиться!"
    victoria "Я уверена, что мы станем вашими постоянными клиентками!"
    victoria "Меня зовут Виктория."
    imgd 43564
    victoria "А это моя подружка Мелани."
    # тренер пожирает Мелани глазами, она равнодушно смотрит в сторону
    music Groove2_85
    imgf 43565
    fitness_instructor "Мне очень приятно!"
    melanie "Взаимно..."
    sound vjuh3
    imgd 43566
    fitness_instructor "Девочки, проходите в раздевалку."
    fitness_instructor "Она находится вон там." # указывает рукой
    fitness_instructor "И через 10 минут я жду вас в этом зале."
    # Виктория, флиртуя
    sound highheels_short_walk
    imgf 43567
    victoria "Хорошо. Мы скоро вернемся. Хи-хи-хи!"
    # он смотрит на Мелани, игноря попытки Виктории
    # она это видит и недовольно косится на Мелани
    music ZigZag
    imgd 43568
    sound2 wow
    w
    imgd 43569
    w
    img 43570
    victoria "!!!"
    # Мелани и Виктория идут в раздевалку, тренер смотрит Мелани вслед
    # затемнение, каблуки
    # смена кадра на раздевалку
    # там, как обычно, тусят Стефани и Ребекка, они переодеваются
    # Виктория подбегает к ним
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 43571
    victoria "Девочки, мы пришли!"
    # чмокает их в щечку по очереди
    sound highheels_short_walk
    imgf 43572
    rebecca "Привет, Виктория!" # дружелюбно
    imgd 43573
    sound kiss1
    w
    sound highheels_short_walk
    imgf 43574
    sound2 kiss1
    stephanie "Привет..." # прохладно
    imgd 43575
    victoria "Я так рада, что мы снова встретились!"
    victoria "Так здорово, что мы теперь будем ходить на занятия вместе! Правда?!"
    rebecca "Да, это будет прикольно!"
    # к ним подходит Мелани
    # Стефани сама идет к Мелани и чмокает ее в щечку
    sound highheels_short_walk
    imgf 43576
    w
    imgd 43577
    stephanie "Мелани, привет!"
    imgf 43578
    sound kiss1
    w
    # отстранясь, смотрит на ее губы и улыбается
    imgd 43579
    stephanie "Рада видеть тебя..."
    victoria "!!!"
    # Мелани, как всегда, с равнодушным видом
    imgd 43580
    melanie "Привет."
    # Виктория пристально смотрит на то, как Стефани любезничает с Мелани
    ##Можно поставить пожалуйста эмоции Виктории чуть выше
    ## после фразы Стефани "Рада видеть тебя"
    # Ребекка встревает в разговор и Стефани отходит от Мелани
    imgf 43582
    rebecca "Привет! Здорово, что вы теперь с нами!"
    rebecca "Будет веселее! Да, Стефани?"
    stephanie "Да, Ребекка."
    imgd 43581
    sound kiss1
    w
    imgf 43583
    rebecca "Переодевайтесь, девочки! Занятие скоро начнется!"
    # Мелани и Виктория отходят к шкафчикам
    # Мелани начинает раздеваться с непроницаемым выражением лица
    # Виктория ехидно на нее оглядывает и тоже начинает снимать платье
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Hidden_Agenda
    imgfl 43584
    victoria "Подружка Мелани, хорошо, что мы купили тебе костюм для фитнеса."
    victoria "Мне кажется, что тебе в нем будет очень удобно заниматься."
    music Master_Disorder
    imgf 43585
    melanie "Да... Очень..."
    music Groove2_85
    sound2 vjuh3
    imgd 43586
    victoria "Я, как твоя лучшая подружка, тебе посоветовала самый лучший вариант."
    melanie "Да, подружка."
    victoria "Мне нравится ходить с тобой на шоппинг и выбирать тебе костюмы."
    victoria "Думаю, из меня получился бы отличный стилист. Да, подружка?"
    imgd 43587
    melanie "Да."
    imgf 43588
    victoria "Заодно и у меня появляются обновки. Хи-хи-хи!"
    music Master_Disorder
    imgd 43589
    melanie "!!!"
    # затемнение, шуршание одежды
    # Мелани и Виктория переоделись
    # Стефани и Ребекка в афиге смотрят на костюм Мелани
    fadeblack
    sound snd_fabric1
    pause 2.0
    music ZigZag
    imgfl 43590
    w
    imgf 43591
    sound oooh4
    w
    sound2 oooh1
    imgd 43592
    rebecca "Ого! Круто!!"
    # Стефани смотрит скорее с вожделением
    imgf 43593
    stephanie "Мелани, ты, как всегда, на высоте."
    imgd 43594
    stephanie "Потрясно!"
    sound oooh4
    imgd 43595
    w
    # Виктория ехидно улыбается
    imgf 43596
    victoria "Девочки, прикольный костюм я посоветовала купить Медани?"
    imgd 43597
    rebecca "О да! Отпад!"
    imgf 43598
    w
    sound snd_woman_laugh3
    imgd 43599
    victoria "Хи-хи-хи!"
    # затемнение
    # девочки выходят в зал
    # тренер смотрит на Мелани, не замечая никого, у него шок
    fadeblack
    sound snd_walk_barefoot
    pause 1.5
    music Groove2_85
    imgfl 43600
    w
    imgf 43601
    w
    sound wow
    img 43602 hpunch
    fitness_instructor "Оооо!"
    imgd 43603
    fitness_instructor "Я..."
#    sound wow
    img 43604 vpunch
    fitness_instructor "Кхм..."
    # Мелани с каменным лицом проходит мимо него, Виктория следом с ехидной улыбочкой
    imgf 43605
    melanie "..."
    imgd 43607
    w
    # Стефани смотрит на тренера, прищурившись, ревниво
    music stop
    sound plastinka1b
    img 43608 hpunch
    w
    img 43606
    stephanie "!!!"
    # он замечает это и перестает пялиться на Мелани
    music Groove2_85
    imgf 43609
    fitness_instructor "Девочки, занимайте свои места..."
    fitness_instructor "Начинаем!"
    # Мелани занимается в переднем ряду рядом со Стефани (Мелани на месте Моники)
    # Ребекка с Викторией сзади (Виктория на месте Бетти)
    # во время занятия Стефани периодически бросает на Мелани заинтересованные взгляды, как и Ребекка
    # показываем немного, как каждая из девочек занимается
    # тренер к ним по очереди подходит
    # к Виктории (помогая ей, бросает взгляды на попу Мелани)
    fadeblack
    sound snd_walk_barefoot
    pause 1.5
    music Ready_and_Waiting
    imgfl 43610
    w
    imgf 43611
    w
    imgd 43612
    w
    imgf 43613
    w
    imgd 43614
    w
    imgf 43615
    w
    imgd 43616
    w
    imgf 43617
    w
    imgd 43618
    w
    imgd 43619
    w
    imgf 43620
    w
    imgd 43621
    w
    imgf 43622
    w
    imgd 43623
    w
    imgd 43624
    w
    imgf 43625
    w
    imgd 43626
    w
    imgf 43627
    sound wow
    w
    imgd 43628
    w
    imgd 43629
    w
    imgd 43630
    w
    imgf 43631
    w
    imgd 43632
    w
    imgd 43633
    w
    imgf 43634
    w
    imgd 43635
    w
    imgf 43636
    w
    imgd 43637
    w
    imgd 43638
    w
    imgf 43639
    w
    imgd 43640
    w
    sound man_steps
    imgf 43641
    fitness_instructor "Делай вот так, Виктория, выгибай ногу сильнее."
    victoria "Вот так?"
    sound Jump1
    img 43642
    fitness_instructor "Да, так. Еще сильнее."
    fitness_instructor "Я помогу тебе, надо только немного поддержать..."
    imgd 43643
    victoria "Ой, мне так больно!"
    imgf 43644
    fitness_instructor "Терпи, сейчас все пройдет. Я желаю, чтобы ты добилась результатов."
    fitness_instructor "Доверься мне, Виктория."
    ###Тут нужно будет добавить фразы, так как сделала что она упала
    sound snd_bodyfall
    img 43645 hpunch
    sound2 snd_woman_pain1
    victoria "Ай! Как больно!"
    music stop
    sound plastinka1b
    img 43646 vpunch
    fitness_instructor "!!!"
    music Groove2_85
    fitness_instructor "Виктория, ты в порядке?"
    fitness_instructor "Давай, я тебе помогу."
    imgf 43647
    stephanie "Она что, на ногах устоять не может?"
    stephanie "Какого черта она вообще сюда пришла тогда?!"
    imgd 43648
    melanie "..."
    imgf 43649
    fitness_instructor "Виктория, я приношу свои извинения..."
    imgd 43650
    victoria "Ой, не беспокойтесь! Все хорошо! Я просто потеряла равновесие..."
    imgd 43649
    fitness_instructor "Это все из-за вашей растяжки... Над ней нужно еще поработать."
    fitness_instructor "Несколько занятий и все будет в порядке."
    fitness_instructor "Ну что? Продолжим?"
    victoria "С удовольствием!"
    fadeblack 1.5
    music Ready_and_Waiting
    imgf 43651
    w
    imgd 43652
    victoria "Теперь получается?"
    fitness_instructor "Да, Виктория, ты молодец."
    fitness_instructor "Я вижу в тебе потенциал."
    imgf 43653
    w
    imgd 43654
    w
    imgf 43655
    w
    imgd 43656
    w
    imgf 43657
    w
    imgd 43658
    w
    # к Ребекке
    imgf 43659
    w
    imgd 43660
    w
    imgf 43661
    fitness_instructor "Ребекка, тебе надо держать корпус ровнее..."
    rebecca "Так?"
    imgd 43662
    fitness_instructor "Еще немного..."
    sound Jump1
    imgd 43663
    rebecca "Так лучше?"
    fitness_instructor "Да, у тебя с каждым разом получается все лучше."
#    fitness_instructor "Теперь расслабься..."
    imgd 43664
    fitness_instructor "Вот так... Молодец!"
    imgf 43665
    w
    imgd 43666
    w
    imgf 43667
    w
    imgd 43668
    w
    imgf 43669
    w
    imgd 43670
    w
    imgd 43671
    w
    imgd 43672
    w
    # к Стефани (Виктория посматривает на них подозрительно)
    imgf 43673
    w
    imgd 43674
    w
    imgd 43675
    w
    imgf 43676
    w
    imgd 43677
    w
    imgf 43678
    w
    imgd 43679
    w
    imgf 43680
    fitness_instructor "Хорошо, молодец, Стефани."
    fitness_instructor "У тебя отлично получается."
    stephanie "Да, я стараюсь."
    imgd 43681
    fitness_instructor "Постарайся больше выгибать спинку, Стефани..."
    stephanie "Вот так?"
    imgf 43682
    fitness_instructor "Умничка. Теперь еще немного... Еще-еще..."
    fitness_instructor "Давай я тебе помогу."
    stephanie "Да, хорошо."
    imgd 43683
    w
    imgd 43684
    fitness_instructor "Молодец, Стефани."
    fitness_instructor "Продолжай в том же духе. Я пока помогу другим девочкам."
    imgf 43685
    w
    imgd 43686
    w
    imgf 43687
    w
    imgd 43688
    w
    imgd 43689
    w
    # к Мелани (на них все пялятся, а он пожирает взглядом прелести Мелани)
    imgf 43690
    w
    imgd 43691
    fitness_instructor "Мелани, ты слишком напряжена, ты чувствуешь это?"
    fitness_instructor "Тебе надо расслабиться. Я помогу."
    sound Jump2
    img 43692 vpunch
    fitness_instructor "Вот так. Молодец, Мелани."
    melanie "..."
    imgd 43693
    fitness_instructor "Теперь тяни ножку, тяни сильнее..."
    sound Jump1
    img 43694
    fitness_instructor "Тебе не больно?"
    melanie "Немного."
    imgf 43695
    fitness_instructor "Я помогу тебе, Мелани..."
    fitness_instructor "У тебя получается, ты чувствуешь?"
    melanie "Да, чувствую."
    imgd 43696
    fitness_instructor "Теперь тянись, тянись как можешь..."
    imgf 43697
    w
    imgd 43698
    fitness_instructor "Вот так, хорошо..."
    imgd 43699
    fitness_instructor "Давай, Мелани, ты можешь еще, я знаю."
    imgf 43700
    w
    # Виктория ехидно смотрит на Стефани, та ревниво на тренера, который помогает Мелани
    # Виктория ехидно улыбается
    # затемнение
    fadeblack 1.5
    music Groove2_85
    imgf 43701
    fitness_instructor "Девочки, на сегодня все!"
    # Ребекка и Виктория улыбаются ему, Мелани равнодушна, Стефани прситально на него смотрит
    fitness_instructor "Вы все молодцы!"
    fitness_instructor "Я очень доволен вашими результатами!"
    imgd 43702
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    sound snd_walk_barefoot
    imgf 43703
    w
    # все девочки идут в раздевалку, Стефани позади них и немного задерживается возле тренера, смотрит на него, флиртуя
    imgd 43704
    stephanie "..."
    # Виктория в это время, пока ее никто не видит, с любопытством выглядывает в зал
    sound vjuh3
    img 43705 vpunch
    victoria "???"
    # если у Стефани с тренером секс
    if stephanieFitnessJustSex == True:
        #
        $ notif(_("Фитнес-тренер любовник Стефани."))
        #
        music Loved_Up
        imgf 43706
        fitness_instructor "Стефани, я так соскучился по тебе..."
        stephanie "Тихо ты! Нас могут услышать!"
        sound Jump2
        img 43707 hpunch
        fitness_instructor "Ну и пусть! Твой Тигр готов провести для тебя персональную тренировку!"
        # он трогает Стефани за попу
        stephanie "Ну хватит! Я не хочу, чтобы кто-то знал!"
        # Виктория злорадно
        music Master_Disorder
        imgf 43708
        victoria "Ага! Вот я и узнала твой секретик, подружка Стефани!"
        victoria "Хи-хи-хи!"
        music Loved_Up
        imgd 43709
        fitness_instructor "Ты останешься?"
        stephanie "Да. А сейчас убери руки!"
        imgf 43710
        fitness_instructor "Я жду тебя здесь. Рррр!"
        imgd 43711
        stephanie "Ха-ха! Я приду, когда девочки уйдут."
        sound snd_walk_barefoot
        imgf 43714
        w
        #
    else:
        #
        $ notif(_("Стефани флиртует с фитнес-тренером."))
        #
        music Loved_Up
        imgf 43706
        fitness_instructor "Стефани, ты такая красивая..."
        stephanie "Без тебя знаю!"
        sound Jump2
        img 43712 hpunch
        fitness_instructor "Задержишься, когда все уйдут?"
        fitness_instructor "Я хочу провести для тебя персональную тренировку!"
        # он прикасается к руке Стефани или кладет руку ей на талию
        imgd 43713
        stephanie "Убери руку!"
        stephanie "Никаких персональных тренировок! Пока что... Я еще думаю..."
        # Виктория злорадно
        music Master_Disorder
        imgd 43708
        victoria "Ага! Вот я и узнала твой секретик, подружка Стефани!"
        victoria "Хи-хи-хи!"
        music Loved_Up
        imgf 43714
        sound2 snd_walk_barefoot
        fitness_instructor "Я готов ждать тебя столько, сколько нужно!"
        imgd 43715
        fitness_instructor "Тебе понравятся мои персональные тренировки, Стефани!"
        imgd 43716
        stephanie "Ха-ха-ха!"
        #
    fadeblack 1.5
    music Groove2_85
    # Виктория прячется обратно в раздевалку, чтоб Стефани ее не заметила
    # Стефани уходит в раздевалку
    # затемнение
    # все девочки стоят в раздевалке
    # Виктория восторженно
    imgf 43717
    victoria "Ой, девочки!"
    victoria "Такое волшебное чувство! Я так расслабилась!"
    victoria "Такая легкость во всем теле!"
    rebecca "Тебе понравилось занятие, Виктория?"
    img 43718
    victoria "Да! Я в восторге, девочки!"
    victoria "Обязательно приду снова!"
    imgf 43719
    stephanie "А тебе понравилось, Мелани?"
    imgd 43720
    melanie "Да, это действительно расслабляет..."
    music Hidden_Agenda
    imgf 43721
    victoria "Еще немного и мы с подружкой Мелани станем спортивными и подтянутыми, как вы, девочки!"
    victoria "Ой, не могу! Вы такие красотки!"
    imgd 43722
    rebecca "Спасибо, Виктория. Ты такая милая!"
    # Стефани бросает на Виктория недружелюбный взгляд
    stephanie "..."
    # потом обращается к Мелани
    music Groove2_85
    imgf 43723
    stephanie "Мелани, будет круто, если ты продолжишь заниматься с нами."
    imgd 43724
    melanie "Я приду, почему нет?"
    melanie "По крайней мере, здесь нет сумасшедших поклонников и папарацци..."
    stephanie "Да, именно поэтому в этот зал просто так не попадают..."
    sound Jump1
    img 43725
    stephanie "Посторонние люди..." # смотрит недовольно на Викторию
    # Виктория это видит, но стоит и мило ей улыбается
    music Hidden_Agenda
    imgd 43726
    victoria "Стефани, я так рада, что ты смогла пригласить меня и мою подружку Мелани!"
    victoria "Теперь мы будем заниматься все вместе!"
    victoria "Так здорово!!!"
    imgf 43727
    stephanie "Да. Прикольно."
    rebecca "Я тоже очень рада!"
    # затемнение, шуршание одежды
    # они все переоделись, чмокают друг друга в щечку на прощание
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgf 43728
    rebecca "Нам нужно будет как-нибудь встретиться всем вместе!"
    rebecca "Мне так понравилось у тебя на девичнике, Виктория!"
    img 43729
    melanie "!!!" # зло
    victoria "Обязательно встретимся, девочки!"
    victoria "Совсем скоро! И мою лучшую подружку Монику обязательно пригласим!"
    sound highheels_short_walk
    imgf 43730
    sound2 kiss1
    victoria "Пока, подружки! До встречи!"
    imgd 43731
    sound kiss1
    w
    imgf 43732
    sound kiss1
    stephanie "Пока, девочки."
    imgd 43733
    sound kiss1
    rebecca "Пока-пока! Скоро увидимся!"
    melanie "Пока..."
    sound highheels_short_walk
    imgf 43734
    w
    # затемнение, каблуки
    # Мелани и Виктория идут мимо тренера на выход из зала
    # он пялится на Мелани
    fadeblack 1.5
    music Groove2_85
    imgf 43735
    fitness_instructor "Девочки, вы молодцы!"
    fitness_instructor "Жду вас на следующем занятии!"
    victoria "Мы обязательно придем! Я просто в восторге!"
    music Hidden_Agenda
    imgd 43736
    victoria "Вы так здорово проводите тренировку!"
    victoria "Сразу видно - настоящий мастер своего дела!"
    music Groove2_85
    imgd 43737
    fitness_instructor "Спасибо, Виктория."
    fitness_instructor "Пока, девочки!"
    imgf 43738
    sound highheels_short_walk
    victoria "До свидания!"
    melanie "До встречи..."
    sound2 wow
    imgd 43739
    w
    fadeblack
    sound highheels_short_walk
    pause 2.0
    # они выходят, тренер смотрит Мелани вслед
    $ melanieVictoriaFitness1 = day # Мелани и Виктория посетили первое занятие в фитнес-зале
    return

# Мелани и Виктория вышли из фитнес-зала и стоят у здания
label ep22_4_dialogues2_fitness_3:
    music Groove2_85
    imgfl 43556
    victoria "Тебе понравилось занятие, подружка Мелани?"
    melanie "..."
    melanie "Да, неплохо..."
    victoria "А тренер тебе понравился?"
    melanie "Нет."
    # Виктория с фальшивой озабоченностью
    music Hidden_Agenda
    imgf 43557
    victoria "Странно..."
    victoria "Я была уверена, что тебе понравится такой мужчина, как тренер..."
    # Мелани подозрительно смотрит на нее
    melanie "Почему ты меня об этом спрашиваешь?"
    # Виктория ехидно
    imgd 43558
    victoria "Я немного позже все тебе расскажу, подружка Мелани."
    victoria "Пусть пока это останется моим маленьким секретиком!"
    victoria "Хи-хи-хи!"
    img 43559
    melanie "!!!"
    return
