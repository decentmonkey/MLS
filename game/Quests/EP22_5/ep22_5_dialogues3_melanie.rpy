default melanieVictoriaInstructorDate1 = 0  # Мелани увидела на руках Виктории шрамы
default melanieVictoriaInstructorDate2 = 0  # у Мелани было DP с Алексом и фитнес-тренером

define v_Melanie_FitnessTrainer_Sex1_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex1_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex2_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex2_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex3_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex3_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex4_1_25_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"
define v_Melanie_FitnessTrainer_Sex4_1_sound_name = "v_Monica_RichRestaurant_Sex1_1_25"

default melanieFitnessTrainerAlex_cumzone = 0

#call ep22_5_dialogues3_melanie_1() # Мелани и Виктория в апартаментах Виктории
#call ep22_5_dialogues3_melanie_2() # кафе в трущобах, свидание с тренером, далее апартаменты Мелани и сцена с DP

# апартаменты Виктории
# Мелани и Виктория сидят на диванчике, на котором сидела Стефани
label ep22_5_dialogues3_melanie_1:
    # Виктория, как обычно, с самодовольной улыбочкой
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Тем временем..."))
    scene black_screen
    with Dissolve(1)
    sound snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 44527
    victoria "Ой, подружка Мелани, я так рада, что наша дружба становится все крепче и крепче!"
    victoria "Мне нравится, что мы теперь ходим вместе не только по магазинам..."
    victoria "Но и на тренировки в фитнес-зал!"
    victoria "Это так здорово! Да, подружка?"
    victoria "Тебе нравится дружить со мной?"
    # Мелани без эмоций смотрит на нее
    imgf 44528
    melanie "Очень нравится... Подружка..."
    # Виктория хихикает, поднимая руку к лицу, как обычно
    sound snd_woman_laugh3
    imgd 44529
    victoria "Хи-хи-хи!"
    # браслеты по ее руке сползают вниз и становится видно свежие следы от потертостей
    # Мелани опускает взгляд на эти шрамы на руке Виктории и ее брови удивленно поднимаются вверх
    music stop
    sound plastinka1b
    img 44530 hpunch
    melanie "?!"
    melanie "?!!?!"
    # Виктория прохихикалась и опускает руку, кладет к себе на колени
    # Виктория продолжает болтать, а Мелани пристально смотрит на ее шрамы, не отводя взгляда, Виктория этого не замечает
    music Groove2_85
    imgd 44531
    victoria "Подружка Мелани, я тут подумала, что нужно спросить у тебя..."
    victoria "Я часто тебе даю какие-то советы по-дружески..."
    victoria "Хотела спросить у тебя, ценишь ли ты мое искреннее, дружеское участие?"
    imgd 44532
    victoria "Ведь я делаю это из благих намерений. Я стараюсь ради тебя, подру..."
    # Мелани все это время рассматривает ее шрамы, потом перебивает Викторию на полуслове
    img 44533
    melanie "Что это за шрамы на твоих руках?"
    # Виктория резко смотрит на свои руки, потом на Мелани, выглядит расстерянной
    music Master_Disorder
    img 44534 vpunch
    victoria "!!!"
    # Мелани поднимает взгляд и вопросительно смотрит на Викторию
    imgd 44535
    melanie "Похоже, это следы от веревок или от наручников."
    # Виктория закрывает шрамы ладонью другой руки, на которой тоже видно шрамы
    imgd 44534
    w
    sound Jump2
    img 44536 hpunch
    w
    imgf 44537
    melanie "Виктория... Тебя что, связывали?"
    # Виктория резко прячет обе руки так, чтобы Мелани их не видела, она все еще выглядит расстерянной
    imgd 44536
    w
    sound vjuh3
    img 44556
    victoria "!!!"
    imgd 44538
    victoria "Ты... Кхм..."
    victoria "Я..."
    # потом берет себя в руки и выражение лица становится обычным, насмешливым
    sound Jump1
    img 43020
    victoria "..."
    imgd 44537
    melanie "???"
    imgf 44542
    victoria "!!!"
    music Hidden_Agenda
    imgd 44539
    victoria "Так, подружка Мелани."
    victoria "На чем мы там остановились?"
    # Мелани предпринимает попытку вывести ее на разговор
    music Master_Disorder
    melanie "Виктория, тебя кто-то принуждает ко всему этому?.."
    melanie "Скажи мне и я..."
    # Виктория демонстративно игнорит ее слова и перебивает
    music Groove2_85
    img 44540
    victoria "Ах, да! Мы говорили про мои дружеские советы. Хи-хи!"
    melanie "!!!"
    victoria "Я вижу, что ты очень ценишь мои советы, подружка..."
    victoria "И у меня для тебя есть еще один совет."
    victoria "Я могу тебе по-дружески кое-что подсказать..."
    victoria "Ты готова будешь делать так, как я тебе посоветую?.."
    # Мелани все еще в недоумении смотрит на Викторию
    imgf 44541
    melanie "..."
    imgd 44542
    victoria "Что молчишь, подружка Мелани?"
    victoria "Если ты считаешь, что я в чем-то заблуждаюсь, то ты всегда можешь сказать об этом."
    victoria "Мы ведь дружим и должны быть искренними друг с другом. Так ведь?"
    # Мелани косится на руки Виктории
    imgd 44543
    melanie "Да..."
    victoria "Готова последовать моему совету и в этот раз, подружка?"
    melanie "Готова..."
    # пристальный взгляд на Викторию, но та всячески игнорит
    melanie "..."
    # Виктория язвительно улыбается Мелани и говорит
    imgf 44544
    victoria "Ой, подружка, что-то у меня так устали мои ножки!.."
    victoria "Не могла бы ты помассировать их немного?"
    victoria "По-дружески..."
    imgd 44545
    melanie "..."
    menu:
        "Сделать, как говорит Виктория.":
            pass
    # Мелани встает с дивана, опускается на колени перед Викторией и начинает стягивать с нее сапог
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 44546
    melanie "?!"
    # стянув сапог, держит в руках ее ногу, а сама смотрит на ее руки, которые Виктория пытается спрятать
    imgf 44547
    w
    imgd 44548
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Master_Disorder
    imgf 44549
    melanie "?!?!"
    imgd 44557
    w
    # Виктория говорит ехидно Мелани
    music Groove2_85
    imgf 44550
    victoria "Тебе удобно, подружка Мелани?"
    melanie "..."
    imgd 44558
    melanie "Да... Удобно..."
    imgf 44559
    victoria "Я сейчас дам тебе несколько дружеских советов..."
    victoria "А потом мы вместе пойдем на шоппинг. Я помогу тебе подобрать новый наряд. Здорово, правда?!"
    melanie "Да..."
    # Виктория указывает пальцем на свою ногу
    imgd 44551
    victoria "Ты, подружка, пока будешь слушать мои советы..."
    victoria "Можешь помассировать мою ножку своим язычком."
    imgd 44552
    w
    sound lick3
    imgd 44553
    w
    # Мелани пристально смотрит на нее и выполняет
    imgd 44554
    sound snd_woman_laugh3
    victoria "Хи-хи-хи!"
    music Master_Disorder
    imgf 44555
    melanie "!!!"
    # затемнение
    $ melanieVictoriaInstructorDate1 = day # Мелани увидела на руках Виктории шрамы
    return

# день, кафе в трущобах, где было свидание Моники и Юлии
label ep22_5_dialogues3_melanie_2:
    # тем временем
    # Мелани в новом аутфите заходит в эту забегаловку, останавливается и осматривается
    # на лице выражение брезгливости
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Тем временем..."))
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 2.0
    music m80s_Things
    imgfl 44560
    w
    imgf 44561
    melanie "!!!"
    # у посетителей, которые сидят за столиками, отваливается челюсть, все в шоке смотрят на нее
    imgd 44562
    w
    sound oooh2
    img 44563 hpunch
    cafe_visitor2 "Это же модель Мелани!"
    cafe_visitor2 "Вот это да!!!"
    imgf 44564
    w
    # один из них (тот, который в свитере) встает и подбегает к ней
    imgd 44565
    cafe_visitor1 "П-простите, в-вы М-мелани?!"
    imgd 44566
    melanie "..."
    sound Jump1
    img 44567 vpunch
    cafe_visitor1 "М-модель?!"
    cafe_visitor1 "А м-можно ваш автограф? П-пожалуйста!"
    # Мелани с выражением лица а-ля как надоела эта вся рутина с поклонниками
    imgf 44568
    melanie "Можно..."
    # не показываем, как дает автограф, кадр в это время на баристу, которая в шоке смотрит на Мелани
    imgd 44569
    cafe_barista "Охренеееть!"
    cafe_barista "Интересно, что она забыла в нашей забегаловке?!"
    cafe_barista "Явно не на ужин сюда пришла, ха-ха!"
    cafe_barista "А вырядилась-то как! Со съемок что-ли сбежала?"
    # кадр на Мелани, довольный поклонник отходит от нее
    imgf 44570
    cafe_visitor1 "С-спасибо, М-мелани!"
    imgd 44571
    cafe_visitor1 "В-вы такая к-красивая!!! Спасибо!!!"
    # Мелани снова оглядывается, не обращая внимания на поклонника
    # из-за одного из столиков ей машет рукой фитнес-тренер, широко улыбаясь, он измазан кетчупом
    music stop
    sound plastinka1b
    img 44572 hpunch
    fitness_instructor "Я тут!"
    fitness_instructor "Иди сюда!"
    # Мелани смотрит на него, как на насекомое, медлит
    music ZigZag
    imgd 44573
    melanie "!!!"
    melanie "!!!!"
    imgf 44574
    sound2 wow
    w
    imgd 44575
    sound highheels_short_walk
    w
    # потом направляется к его столику и садится за него
    # на тарелке перед ним лежит бургер (как в Шайни-хол)
    # посетители с завистью смотрят на инструктора и Мелани
    fadeblack 1.5
    music Groove2_85
    imgfl 44576
    fitness_instructor "Привет, Мелани!"
    melanie "Здравствуй..."
    fitness_instructor "Здорово, что ты предложила сходить на свидание!"
    fitness_instructor "Я так офигел, когда твоя подружка передала мне, что ты запала на меня!"
    melanie "!!!"
    imgf 44578
    fitness_instructor "Я чуть в штаны от радости не наложил!"
    fitness_instructor "Кому из друзей расскажу - не поверят! Ха!"
    fitness_instructor "Пусть обзавидуются мне, лузеры!"
    img 44577
    melanie "!!!"
    # подходит официантка, она же бариста
    sound highheels_short_walk
    imgf 44579
    cafe_barista "Добрый день! Что будете заказывать?"
    fitness_instructor "О! Бургер бери!"
    # Мелани брезгливо смотрит на тренера и не глядя на официантку отвечает
    imgd 44580
    melanie "Нет, спасибо... Я ничего не буду заказывать здесь..."
    imgd 44581
    cafe_barista "Окей. Если что-то понадобится - позовите меня."
    # официантка отходит и оборачивается, пялясь на Мелани
    sound highheels_short_walk
    imgf 44582
    w
    sound vjuh3
    imgd 44583
    w
    imgf 44584
    fitness_instructor "А чего ты не хочешь заказывать еду?"
    fitness_instructor "Бери! Я угощаю!"
    imgd 44585
    melanie "Спасибо, не надо... Я не ем фастфуд."
    fitness_instructor "Так и я не ем! Я же на спорте, ха!"
    fitness_instructor "Но раз в месяц можно себя побаловать!"
    fitness_instructor "Тем более, у меня сегодня такой повод - свидание с тобой!"
    imgd 44586
    fitness_instructor "Устроим себе праздник живота, а?"
    fitness_instructor "Потом пара пробежек в парке и как-будто бы и не было никакого бургера с колой!"
    fitness_instructor "Ну так что, уговорил я тебя, а?"
    imgd 44587
    melanie "На что?"
    sound vjuh3
    img 44588
    fitness_instructor "На бургер с колой, ха!"
    imgd 44589
    w
    imgf 44590
    melanie "Нет."
    imgd 44591
    fitness_instructor "Эээх, зря!.."
    # Мелани пристально смотрит на него нечитаемым взглядом
    # тот сидит жует с довольной рожей
    # потом резко перестает жевать и смотрит на Мелани
    imgf 44592
    w
    sound eating_toastie
    imgd 44593
    w
    img 44594
    w
    imgd 44595
    fitness_instructor "Ой, я это!.. Забыл совсем!"
    # торопливо вытирает руку об свою футболку и тянет ее Мелани
    imgd 44596
    fitness_instructor "Меня зовут Эд! А то мы так и не познакомились."
    sound vjuh3
    img 44599 vpunch
    w
    sound Jump2
    img 44597
    fitness_instructor "Но ты можешь называть меня Тедди! Мне нравится, когда девушки меня так называют!"
    music Power_Bots_Loop
    img 44598 hpunch
    melanie "!!!"
    # Мелани смотрит на его руку и игнорирует рукопожатие
    # с трудом натягивает на лицо полуулыбку
    imgd 44600
    melanie "Рада познакомиться с тобой, Тедди..."
    # ему по фигу, он убирает руку и продолжает жевать
    music Groove2_85
    imgf 44601
    fitness_instructor "А я-то как рад!"
    fitness_instructor "Сижу, смотрю на тебя и не верю, что такая крутая девушка, как ты..."
    # она его перебивает
    melanie "Почему ты выбрал для нашей встречи именно это место?"
    # он с придурковатым выражением лица
    fitness_instructor "Так я тут недалко, в парке, бегал."
    fitness_instructor "Я каждый день бегаю в этом парке."
    imgd 44602
    fitness_instructor "Мне там нравится. Тем более, он недалеко от моего дома."
    fitness_instructor "Хочешь, будем бегать со мной вместе?"
    fitness_instructor "Тебе стопудово понравится! Классный парк!"
    imgd 44603
    melanie "Спасибо, я подумаю..."
    # снова подходит официантка
    sound highheels_short_walk
    imgf 44604
    cafe_barista "Может быть, вы выбрали что-нибудь?"
    # Мелани снова не глядя в ее сторону
    melanie "Нет."
    # официантка поворачивается к инструктору
    imgd 44605
    cafe_barista "А вам принести еще чего-нибудь?"
    imgd 44606
    fitness_instructor "Не-а."
    imgf 44607
    sound highheels_short_walk
    cafe_barista "Окей, как хотите."
    # официантка отходит
    fadeblack 1.5
    music Groove2_85
    imgf 44608
    fitness_instructor "Слушай, Мелани!"
    fitness_instructor "Если не хочешь бургер, давай я угощу тебя шавермой!"
    fitness_instructor "Тут недалеко, за углом, продается лучшая шаверма в городе!"
    imgd 44609
    sound kiss2
    w
    img 44610
    fitness_instructor "Пальчики оближешь!"
    # Мелани в шоке смотрит на него
    imgd 44611
    melanie "Шаверма?!"
    imgf 44612
    fitness_instructor "Да! Пойдем? Прямо там, на улице, и съедим по шаверме!"
    fitness_instructor "Заодно с Джеком тебя познакомлю! Такой классный парень! Он тебе понравится!"
    melanie "!!!"
    fitness_instructor "Или можно пойти в парк! Сядем на лавочку и поедим, а?!"
    fitness_instructor "Мне кажется, я круто придумал!"
    fitness_instructor "Устроим романтическое свидание!"
    # Мелани снова с трудом изображает улыбку
    music Hidden_Agenda
    imgd 44613
    melanie "Я... Давай, в следующий раз?"
    melanie "Я планировала, что мы сегодня..."
    music Groove2_85
    fitness_instructor "А хочешь, я проведу для тебя персональную тренировку?"
    melanie "???"
    fitness_instructor "Ты не взяла свой костюм для йоги?"
    melanie "Нет..."
    imgd 44614
    fitness_instructor "Ну и ладно! В этом костюмчике тоже можно тренироваться!"
    sound wow
    imgd 44615
    w
    imgf 44616
    fitness_instructor "Пошли, позанимаемся йогой в парке, а?"
    fitness_instructor "Я помогу тебе расслабиться, а то какая-то напряженная вся."
    fitness_instructor "Волнуешься что-ли, как пройдет свидание со мной?!"
    fitness_instructor "Да ты не переживай! Круто выглядишь, я тоже красавчик!.."
    fitness_instructor "Сейчас я доем и пойдем гулять."
    # Мелани с обреченным видом
    imgd 44617
    melanie "Тедди..."
    fitness_instructor "Угу... Чего?"
    melanie "..."
    menu:
        "Следовать советам Виктории.":
            pass
    # Мелани с видимым трудом выговаривает
    music Master_Disorder
    imgf 44618
    melanie "Я тут подумала..."
    melanie "Почему бы мне не пригласить такого..."
    melanie "Такого красавчика, как ты, к себе..."
    melanie "К себе в гости."
    # он удивленно смотрит на нее
    music stop
    sound plastinka1b
    img 44619 hpunch
    fitness_instructor "К тебе?"
    imgd 44620
    melanie "Ко мне..." # обреченно
    music Groove2_85
    fitness_instructor "Ааа! Я врубился!"
    fitness_instructor "Ты забыла свой костюм для йоги дома!"
    fitness_instructor "И поэтому хочешь, чтобы я провел тебе персональную тренировку не в парке, как я предлагаю..."
    fitness_instructor "А у тебя дома! Правильно, да?"
    imgf 44621
    melanie "..."
    melanie "Да, Тедди."
    # он глупо хихикает
    imgd 44622
    fitness_instructor "Тедди не только красавчик. Тедди еще и умный парень, ха!"
    music Master_Disorder
    imgd 44623
    melanie "Да... И мне это..."
    melanie "Мне это очень нравится."
    music Groove2_85
    fitness_instructor "Хи-хи-хи!"
    fitness_instructor "Да, я такой! Крутой перец!"
    fitness_instructor "Може, все-таки сначала по шаверме, а?"
    imgd 44624
    melanie "Нет-нет... У меня не так много времени."
    melanie "Мне нужно успеть провести тренировку до... До вечера."
    # он торопливо встает из-за стола
    sound Jump1
    img 44625 vpunch
    fitness_instructor "Понял! Не дурак!"
    fitness_instructor "Я сейчас быстро расплачусь и поедем к тебе!"
    # уходит
    # Мелани остается за столиком одна, на лице буря эмоций из отвращения, ненависти, злости
    sound man_steps
    imgf 44626
    melanie "!!!"
    music Master_Disorder
    img 44627
    melanie "!!!!"
    melanie "!!!!!!"
    # теренер возвращается и встает рядом с Мелани, тянет ей свою руку
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgf 44628
    fitness_instructor "Ну что, погнали?!"
    imgd 44629
    w
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    # затемнение, звук мотора
    # смена кадра на квартиру Мелани
    # она заходит в гостиную, тренер идет следом за ней и пялится на ее попу
    fadeblack 1.5
    music ZigZag
    sound2 highheels_short_walk
    imgfl 44630
    melanie "Чувствуй себя, как дома... Тедди."
    imgf 44631
    w
    sound wow
    imgd 44632
    w
    sound man_steps
    imgf 44633
    fitness_instructor "Ага. А нормальная такая у тебя хата!"
    fitness_instructor "У меня квартира раза в три меньше!"
    fitness_instructor "За сколько арендуешь?"
    melanie "Это мои апартаменты."
    imgd 44634
    fitness_instructor "О, ну да. Ты, наверное, зарабатываешь кругленькую сумму, да?"
    fitness_instructor "Сколько у тебя выходит в год? Миллион, наверное? Или даже два!"
    imgd 44635
    melanie "Неважно."
    music Groove2_85
    imgd 44636
    fitness_instructor "Ну ладно, не хочешь - не говори."
    fitness_instructor "Но офигеть, какая ты крутая!"
    fitness_instructor "Мои коллеги о таких клиентках, как ты, даже мечтать не смеют..."
    fitness_instructor "А я тут бац! И приехал в гости к самой модели Мелани, ха!"
    img 44637
    melanie "!!!"
    menu:
        "Следовать советам Виктории.":
            pass
    # Мелани направляется к своей спальне
    music Master_Disorder
    imgf 44638
    melanie "Тедди..."
    melanie "Как я тебе уже говорила, у меня мало времени."
    melanie "Мне нужно успеть до вечера... Провести тренировку с тобой."
    music Groove2_85
    fitness_instructor "Ага, я помню."
    fitness_instructor "Приступим?"
    sound highheels_short_walk
    imgd 44639
    melanie "Да, давай начнем..."
    fitness_instructor "Ну тогда переодевайся в свой костюм для йоги. Я тебя жду здесь."
    # Мелани идет в спальню, затемнение
    # спястя 5 минут
    # кадр на гостиную, инструктор ждет Мелани и ходит по гостиной, разминаясь перед тренировкой
    # голос из-за двери спальни
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Ready_and_Waiting
    imgf 44640
    w
    sound vjuh3
    imgd 44641
    w
    imgf 44642
    melanie "Тедди?"
    sound Jump1
    img 44643
    # он резко поворачивает голову в сторону спальни
    fitness_instructor "Ты готова, Мелани?"
    imgd 44644
    melanie "Я думаю, что нам лучше провести тренировку тут."
    melanie "Так будет гораздо удобнее."
    melanie "Иди сюда."
    # он идет в сторону спальни
    # затемнение
    # смена кадра на спальню
    # тренер заходит и у него от удивления открывается рот
    # он во все глаза пялится на Мелани
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Loved_Up
    imgf 44645
    sound2 wow
    w
    img 44646 vpunch
    w
    sound Jump2
    img 44647 hpunch
    fitness_instructor "ОГО!!!"
    # она стоит голая и с ненавистью смотрит на камеру на прикроватной тумбе
    music Master_Disorder
    imgf 44649
    melanie "!!!"
    imgd 44648
    w
    # смена кадра
    # приемная в офисе Дика
    # Виктория сидит на своем рабочем месте и смотрит в монитор, довольно хихикая
    sound snd_woman_laugh3
    imgf 19023
    victoria "Хи-хи-хи!"
    # затемнение
    # смена кадра на спальню Мелани
    # она поворачивается к тренеру, тот стоит в шоке
    fadeblack 1.5
    music Loved_Up
    imgf 44650
    melanie "..."
    menu:
        "Продолжать следовать советам Виктории.":
            pass
    # Мелани равнодушно
    imgd 44651
    melanie "На кровати гораздо удобнее заниматься йогой. Не так-ли, Тедди?"
    imgd 44652
    fitness_instructor "Ага, да... К-конечно, уд-добнее..."
    fitness_instructor "А ты?.."
    # Мелани лезет на кровать
    sound barefoot_walk2
    imgf 44653
    melanie "Мне будет удобно делать это без костюма для йоги..."
    imgd 44654
    fitness_instructor "Я... А мне... Кхм!"
    sound vjuh3
    img 44655 vpunch
    w
    # Мелани соблазнительно ложится на живот, косится на камеру
    imgd 44656
    w
    imgf 44657
    melanie "Думаю, что тебе тоже одежда будет мешать..."
    melanie "Если так - сними ее."
    # тренер в ступоре смотрит на округлости Мелани
    imgd 44658
    fitness_instructor "Офигеееть!"
    img 44659
    fitness_instructor "Я сейчас, Мелани! Пару секунд!"
    # он быстро скидывает с себя одежду
    sound snd_fabric1
    imgd 44660
    w
    imgf 44661
    fitness_instructor "Все! Я готов к тренировке!"
    # Мелани зло смотрит на камеру
    melanie "Иди ко мне..."
    melanie "Помоги мне расслабиться... Тедди."
    # тренер лезет на кровать и начинает лапать попу Мелани
    sound Jump2
    imgd 44662
    fitness_instructor "Да, Мелани, ты слишком напряжена."
    fitness_instructor "Тебе нужно расслабиться."
    fitness_instructor "Сейчас я помогу тебе."
    imgf 44663
    fitness_instructor "Раздвинь немного ноги в стороны, Мелани."
    fitness_instructor "Так я более эффективно смогу тебе помочь..."
    imgd 44664
    melanie "..."
    menu:
        "Раздвинуть ноги.":
            pass
    # Мелани раздвигает ноги
    # тренер кладет ладони на ее ягодицы и разводит их в стороны
    imgf 44665
    w
    sound vjuh3
    imgd 44666
    w
    imgf 44667
    w
    sound Jump1
    imgd 44668
    w
    imgd 44667
    fitness_instructor "Ууууф..."
    sound Jump1
    imgd 44668
    fitness_instructor "Ты все еще очень напряжена, Мелани."
    sound Jump1
    imgd 44669
    fitness_instructor "Сейчас я помассирую тебя немного и мы приступим к тренировке."
    # рассматривает и трогает пальцем ее дырочки, сует палец то в киску, то в попу
    sound Jump1
    imgd 44668
    w
    sound Jump1
    imgd 44669
    w
    imgd 44670
    fitness_instructor "Вот тааак... Хорошо..."
    sound chpok5
    imgd 44671
    w
    imgd 44670
    w
    sound chpok5
    imgd 44671
    fitness_instructor "Я вижу, как ты расслабляешься все больше и больше."
    imgd 44670
    w
    sound chpok5
    imgd 44672
    fitness_instructor "Сейчас мы поработаем с твоими мышцами, Мелани."
    imgf 44673
    fitness_instructor "После этой тренировки ты почувствуешь легкость во всем теле."
    fitness_instructor "И тебе захочется повторять наши персональные тренировки снова и снова."
    imgd 44674
    fitness_instructor "Ооох..."
    # он пристраивает член к киске Мелани
    imgf 44675
    fitness_instructor "Сейчас я помассирую тебя немного по-другому."
    sound drkanje5
    imgd 44676
    fitness_instructor "Это будет более эффективный массаж, чем руками."
    fitness_instructor "Ты ведь хочешь этого, Мелани?"
    imgd 44677
    melanie "..."
    menu:
        "Следовать советам Виктории.":
            pass
    # Мелани зло смотрит в камеру
    imgf 44678
    melanie "Да, я с нашей первой встречи в фитнес-зале..."
    melanie "Мечтала об этом..."
    melanie "Помассируй меня, как следует, тренер..."
    # он приподнимает немного ее попу и направляет член на киску
    # водит головкой между ног Мелани
    imgd 44679
    fitness_instructor "Ооо... Круто как..."
    fitness_instructor "Мне нравится тренировать тебя, Мелани!"
    # вводит член в киску
    sound chpok6
    img 44680 hpunch
    fitness_instructor "Ееее!"
    fitness_instructor "Тедди проник в киску модели Мелани!"

    imgf 44681
    w
    # video
    # 1
    # v_Melanie_FitnessTrainer_Sex1_1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex1_1= Movie(play="video/v_Melanie_FitnessTrainer_Sex1_1.mkv")
    show videov_Melanie_FitnessTrainer_Sex1_1
    with fade
    fitness_instructor "Рррр!.. Охренительно!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44682
    w
    # 2
    # v_Melanie_FitnessTrainer_Sex1_2_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex1_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex1_2_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex1_2_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex1_2_25
    with fade
    fitness_instructor "Тебе нравится, Мелани, а?"
    wclean
    melanie "Да."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44683
    w
    # 3
    # v_Melanie_FitnessTrainer_Sex1_6
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex1_6= Movie(play="video/v_Melanie_FitnessTrainer_Sex1_6.mkv")
    show videov_Melanie_FitnessTrainer_Sex1_6
    with fade
    fitness_instructor "Я буду твоим тигром!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # он начинает двигаться в ней, а Мелани смотрит в камеру
    imgf 44684
    w
    # 4
    # v_Melanie_FitnessTrainer_Sex1_3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex1_3= Movie(play="video/v_Melanie_FitnessTrainer_Sex1_3.mkv")
    show videov_Melanie_FitnessTrainer_Sex1_3
    with fade
    fitness_instructor "Мммм, кайфово-то как!"
    wclean
    fitness_instructor "Меня так надолго не хватит, Мелани."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44685
    w
    # 5
    # v_Melanie_FitnessTrainer_Sex1_5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex1_5= Movie(play="video/v_Melanie_FitnessTrainer_Sex1_5.mkv")
    show videov_Melanie_FitnessTrainer_Sex1_5
    with fade
    fitness_instructor "МММММ... Дааа!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # 6
    # v_Melanie_FitnessTrainer_Sex1_4_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex1_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex1_4_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex1_4_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex1_4_25
    with fade
    fitness_instructor "Давай ты будешь сверху!"
    wclean
    fitness_instructor "Хочу смотреть на тебя, Мелани!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # смена кадра
    # приемная в офисе Дика
    # Виктория сидит на своем рабочем месте и трогает свою киску
    imgf 18935
    w
    music Master_Disorder
    imgd 43505
    w
    imgf 19036
    victoria "Сегодня у подружки отличная тренировка."
    imgd 44746
    victoria "Стефани было бы интересно посмотреть на это. Хи-хи!"
    # затемнение
    # смена кадра на спальню Мелани
    # тренер лежит на спине, Мелани двигается на нем сверху
    # он тискает ее груди, лапает за бедра
    fadeblack 1.5
    music Loved_Up

    imgf 44686
    w
    # video
    # 1
    # v_Melanie_FitnessTrainer_Sex2_1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex2_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex2_1_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex2_1_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex2_1_25
    with fade
    fitness_instructor "Поверить не могу, что меня трахает модель с обложки журнала!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # 2
    # v_Melanie_FitnessTrainer_Sex2_4
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex2_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex2_4= Movie(play="video/v_Melanie_FitnessTrainer_Sex2_4.mkv")
    show videov_Melanie_FitnessTrainer_Sex2_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44687
    w
    sound drkanje5
    imgd 44688
    w
    sound Jump1
    imgd 44687
    w
    # 3
    # v_Melanie_FitnessTrainer_Sex2_3_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex2_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex2_3_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex2_3_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex2_3_25
    with fade
    fitness_instructor "О, сделай так еще раз!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44689
    w
    # 4
    # v_Melanie_FitnessTrainer_Sex2_2
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex2_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex2_2= Movie(play="video/v_Melanie_FitnessTrainer_Sex2_2.mkv")
    show videov_Melanie_FitnessTrainer_Sex2_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44690
    w
    # 5
    # v_Melanie_FitnessTrainer_Sex2_6_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex2_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex2_6_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex2_6_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex2_6_25
    with fade
    fitness_instructor "Такая секс-бомба потекла по Тедди, да!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # 6
    # v_Melanie_FitnessTrainer_Sex2_5
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex2_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex2_5= Movie(play="video/v_Melanie_FitnessTrainer_Sex2_5.mkv")
    show videov_Melanie_FitnessTrainer_Sex2_5
    with fade
    fitness_instructor "Она не могла не запасть на такого крутого тренера, как я, ха!"
    wclean
    fitness_instructor "Дааа!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44691
    w
    # раздается хлопок дверью, пришел Алекс
    # Мелани перестает двигаться и замирает на тренере, она в афиге
    sound snd_door_open1
    img 44692 vpunch
    alex_photograph "Милая, я дома!"
    melanie "!!!"
    alex_photograph "Мне позвонила Виктория и передала, что ты для меня приготовила сюрприз."
    alex_photograph "И чтобы я пришел домой пораньше."
    music stop
    sound plastinka1b
    img 44693 hpunch
    melanie "!!!!"
    music Master_Disorder
    alex_photograph "Милая, ты где?"
    # Алекс заходит в спальню и видит Мелани с тренером, она так и продолжает сидеть на нем
    # тренер глупо улыбается
    sound snd_door_open1
    imgd 44694
    fitness_instructor "Гы! А это кто?"
    # Алекс в шоке
    alex_photograph "?!?!?!"
    alex_photograph "Мелани?!"
    melanie "Алекс?!"
    img 44695
    alex_photograph "Что это такое, Мелани?!"
    alex_photograph "Объясни мне, что тут происходит?!"
    # Мелани отворачивается от Алекса и смотрит в камеру
    sound Jump2
    img 44696 hpunch
    melanie "!!!"
    # смена кадра на приемную в офисе Дика
    # Виктория хихикает
    imgf 18970
    w
    imgd 19029
    sound snd_woman_laugh3
    victoria "Так гораздо интереснее!"
    victoria "Импровизируй, подружка Мелани!"
    victoria "Хи-хи-хи!"
    # ласкает себя
    # затемнение
    # смена кадра на спальню Мелани, она также сидит на теренере
    # Алекс возмущенно
    fadeblack 1.5
    music Power_Bots_Loop
    imgd 44697
    alex_photograph "Мелани, что ты творишь?!"
    alex_photograph "Зачем ты так поступаешь со мной?!"
    melanie "..."
    imgd 44698
    alex_photograph "Одно дело твои игры, а другое - любовник в постели!"
    alex_photograph "И после этого ты говоришь о нашей свадьбе?!"
    alex_photograph "Как ты себе представляешь это?!"
    imgd 44699
    w
    sound vjuh3
    imgd 44700
    w
    # тренер теряет интерес к Алексу и водит рукой по бедру Мелани, рассматривает ее
    # кадр на Викторию
    music Master_Disorder
    imgf 18970
    w
    imgd 19029
    victoria "Ну давай, подружка!"
    victoria "Ты ведь знаешь, что я расстроюсь, если Алекс уйдет..."
    # кадр на Мелани
    imgf 44701
    melanie "..."
    menu:
        "Успокоить Алекса.":
            pass
    # Мелани игриво улыбается Алексу
    music Hidden_Agenda
    sound2 Jump2
    imgd 44702
    melanie "Алекс..."
    melanie "Это и есть мой сюрприз для тебя, о котором тебе сказали по телефону."
    music Power_Bots_Loop
    img 44703 vpunch
    alex_photograph "Вот ЭТО сюрприз?!"
    alex_photograph "Я прихожу к свой любимой девушке, а ее трахает незнакомый мужик!"
    alex_photograph "Это, по-твоему, сюрприз?!"
    music Hidden_Agenda
    imgd 44704
    melanie "Да, Алекс. Я очень хочу поиграть с тобой..."
    melanie "И очень ждала тебя."
    # Алекс зло
    img 44705
    alex_photograph "Ждала меня?!"
    imgd 44706
    melanie "Да, Алекс..."
    alex_photograph "Для чего?!"
    melanie "Ох, Алекс..."
    melanie "Я хочу поиграть с тобой, как мы это любим делать..."
    alex_photograph "Поиграть, как мы любим?"
    alex_photograph "А где другая девушка, если поиграть?"
    music Loved_Up
    imgf 44707
    melanie "Алекс, мне так понравилось, как было в прошлый раз со Стефани..."
    imgd 44708
    melanie "Я часто вспоминаю ту вечеринку..."
    sound Jump1
    imgd 44709
    melanie "Вспоминаю, как ты и Джон одновременно овладели ее телом..."
    imgd 44708
    w
    imgd 44710
    melanie "И меня так возбуждает это. Мммм..."
    # Мелани делает движения бедрами на тренере
    imgf 44711
    fitness_instructor "Ооох, сделай так еще разочек, Мелани."
    imgd 44708
    w
    sound Jump1
    imgd 44709
    melanie "Мммм..."
    imgd 44708
    # она повторяет движение
    # тренер кладет руку ей на груди и мнет их
    fitness_instructor "Ееее..."
    # Мелани изображает возбуждение, прикрывая глаза и облизывая губы
    imgd 44712
    melanie "Мммм... Даа..."

    imgf 44713
    w
    # video
    # 1
    # v_Melanie_FitnessTrainer_Sex3_1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex3_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex3_1_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex3_1_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex3_1_25
    with fade
    melanie "Алекс, я так возбуждаюсь от мысли о том..."
    melanie "Что ты сейчас войдешь в мою попу..."
    wclean
    melanie "В то время как внутри моей киски член другого мужчины!.."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # тренер продолжает лапать Мелани и качает ее бедра на своем члене
    imgf 44715
    w
    # 2
    # v_Melanie_FitnessTrainer_Sex3_2_25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex3_2_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex3_2_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex3_2_25
    with fade
    fitness_instructor "Ууууф, как круто!"
    wclean
    fitness_instructor "Как ты возбуждена, Мелани..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44714
    w
    # 3
    # v_Melanie_FitnessTrainer_Sex3_3
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex3_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex3_3= Movie(play="video/v_Melanie_FitnessTrainer_Sex3_3.mkv")
    show videov_Melanie_FitnessTrainer_Sex3_3
    with fade
    melanie "Да! Я так завожусь от этой мысли!"
    wclean
    melanie "Так хочу этого!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    # Алекс растерянно смотрит на происходящее

    imgf 44716
    alex_photograph "Мелани, но ты мне никогда не разрешала делать это туда..."
    # 4
    # v_Melanie_FitnessTrainer_Sex3_4_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex3_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex3_4_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex3_4_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex3_4_25
    with fade
    melanie "Алекс, иди сюда скорее!"
    melanie "Сегодня я хочу этого больше всего на свете!"
    alex_photograph "..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # потом залипает взглядом на попе Мелани
    imgf 44717
    alex_photograph "..."
    # она видит его взгляд и проводит рукой по своим ягодицам
    sound snd_slap1
    img 44718 hpunch
    melanie "Алекс, ты же не откажешь мне? Я ведь так ждала тебя!"
    sound vjuh3
    img 44719
    w
    imgf 44720
    alex_photograph "Нуу... Ты что, правда так хочешь этого?"
    imgd 44721
    melanie "Да-да! Войди же в меня, Алекс!"
    melanie "!!!"
    # Алекс смотрит на ее попу и начинает раздеваться
    imgd 44722
    w
    # смена кадра на приемную в офисе Дика
    # Виктория радостно
    music Master_Disorder
    imgf 18935
    w
    imgd 19032
    victoria "Ох, как подружка Мелани умеет изображать страсть!"
    victoria "Какая старательная и хорошая подружка!"
    # ласкает себя
    # затемнение
    # смена кадра на спальню Мелани
    # голый Алекс уже лезет на постель к Мелани
    # трогает попу Мелани
    fadeblack 1.5
    music Loved_Up
    imgfl 44723
    melanie "О, да, Алекс! Сделай это скорее!"
    melanie "Я так возбуждена! Я так хочу тебя!"
    melanie "Быстрее, Алекс!"
    # Алекс пристраивается членом к ее попе
    imgf 44724
    alex_photograph "Да, милая. Сейчас..."
    alex_photograph "Ты и правда так возбуждена..."
    alex_photograph "Ты такая страстная..."
    imgd 44725
    w
    imgd 44726
    alex_photograph "Я не могу тебе отказать, милая... Просто не в силах отказать."
    alex_photograph "Я так люблю тебя..."
    # Алекс вводит свой член в попу Мелани
    imgf 44727
    w
    sound chpok6
    img 44728 hpunch
    w
    music Loved_Up2
    img 44729
    melanie "Аааа!"
    melanie "Даааа!!!"
    # тренер довольно улыбается и двигает бедрами, продолжая лапать Мелани за грудь
    imgf 44730
    fitness_instructor "Ооо, кайф! Как же круто!"
    melanie "Мммммм!!!"

    imgf 44731
    w
    # video
    # 1
    # v_Melanie_FitnessTrainer_Sex4_2_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex4_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_2_25= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_2_25.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_2_25
    with fade
    alex_photograph "Оооох..."
    wclean
    melanie "Даааа... Продолжай таааак..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # 2
    # v_Melanie_FitnessTrainer_Sex4_1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Melanie_FitnessTrainer_Sex4_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_1= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_1.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_1
    with fade
    melanie "Аааах!!!"
    wclean
    alex_photograph "Мммм..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44732
    w
    imgd 44733
    w
    # 3
    # v_Melanie_FitnessTrainer_Sex4_5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_5= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_5.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_5
    with fade
    melanie "Мпфааа!!!"
    wclean
    alex_photograph "Ааааа!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 44734
    w
    # 4
    # v_Melanie_FitnessTrainer_Sex4_6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_6= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_6.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_6
    with fade
    fitness_instructor "Вот это тренировка! Да!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    # Мелани кончает первой (ну, или делает вид)
    imgf 44735
    w
    # 5
    # v_Melanie_FitnessTrainer_Sex4_3
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_3= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_3.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_3
    with fade
    melanie "Я не могу больше сдерживаться!"
    wclean
    melanie "ОООООО!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # 6
    # v_Melanie_FitnessTrainer_Sex4_4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_4= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_4.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_4
    with fade
    melanie "Кончаю!"
    wclean
    melanie "ООООО!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 44735
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    melanie "ОООООООО!!!"
    img 44736
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound snd_melanie_cum
    w
    # 7
    # v_Melanie_FitnessTrainer_Sex4_7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Melanie_FitnessTrainer_Sex4_7= Movie(play="video/v_Melanie_FitnessTrainer_Sex4_7.mkv")
    show videov_Melanie_FitnessTrainer_Sex4_7
    with fade
    alex_photograph "И я сейчас кончуууу!!!"
    wclean
    fitness_instructor "Да-да! Я тоже!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    menu:
        "Кончить внутрь Мелани.":
            $ melanieFitnessTrainerAlex_cumzone = 1
            img 44738
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            imgd 44739
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            img 44737
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            fitness_instructor "Ррррр!"
            fitness_instructor "Оооох..."
            fitness_instructor "ДАААААА!!!"
            imgd 44739
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            melanie "Ммммм..."
            img 44740
            sound chpok5
            w
            pass
        "Кончить на Мелани.":
            $ melanieFitnessTrainerAlex_cumzone = 2
            img 44737
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            fitness_instructor "Ррррр!"
            fitness_instructor "Оооох..."
            img 44743
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            fitness_instructor "ДАААААА!!!"
            img 44744
            sound chpok5
            w
            img 44738
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            img 44741
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            alex_photograph "ААААААААА!!!"
            img 44742
            sound chpok5
            melanie "Ммммм..."
            pass
    # Мелани, вся в сперме, смотрит на камеру
    fadeblack
    sound man_steps
    pause 2.0
    music Master_Disorder
    imgfl 44745
    melanie "!!!"
    # затемнение
    # смена кадра на приемную в офисе Дика
    # Виктория кончает
    music Loved_Up
    imgf 19037
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan6
    victoria "Мммм..."
    victoria "Ааааа!"
    victoria "АААААААА!!!"
    # потом расслаблено откидывается в кресле
    imgf 44748
    victoria "Отличная работа, подружка Мелани..."
    victoria "Хи-хи-хи!"
    # затемнение
    $ melanieVictoriaInstructorDate2 = day # у Мелани было DP с Алексом и фитнес-тренером
    return
