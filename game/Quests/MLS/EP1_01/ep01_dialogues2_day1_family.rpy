
#call ep01_dialogues2_day1_family_1() # комната Барди перед ужином
#call ep01_dialogues2_day1_family_1_1() # мысли при клике на кровать, если утро или день
#call ep01_dialogues2_day1_family_1_2() # мысли при клике на окно
#call ep01_dialogues2_day1_family_1_3() # мысли при клике на стол
#call ep01_dialogues2_day1_family_1_4() # мысли при клике на печатную машинку
#call ep01_dialogues2_day1_family_1_5() # при клике на лист в печатной машинке
#call ep01_dialogues2_day1_family_1_6() # мысли при клике на двери соседних комнат на втором этаже
#call ep01_dialogues2_day1_family_1_7() # мысли при клике на флипчарт (холл второго этажа)
#call ep01_dialogues2_day1_family_1_8() # мысли при клике на стол (холл второго этажа)
#call ep01_dialogues2_day1_family_1_9() # мысли при клике на картины (холл второго этажа)
#call ep01_dialogues2_day1_family_1_10() # мысли при клике на ТВ (первый этаж, гостиная)
#call ep01_dialogues2_day1_family_1_11() # мысли при клике на диван (первый этаж, гостиная)
#call ep01_dialogues2_day1_family_1_12() # мысли при клике на входную дверь (первый этаж, холл)
#call ep01_dialogues2_day1_family_1_13() # мысли при клике на унитаз (ванная комната)
#call ep01_dialogues2_day1_family_1_14() # мысли при клике на душ или ванную (ванная комната)
#call ep01_dialogues2_day1_family_1_15() # мысли при клике на любой предмет на кухне
#call ep01_dialogues2_day1_family_2() # кухня, ужин с семьей
#call ep01_dialogues2_day1_family_3() # комната Барди, вечер, клик на кровать (меню)
#call ep01_dialogues2_day1_family_4() # вечером на кухне, клик на Софи
#call ep01_dialogues2_day1_family_4_1() # повторный клик на Софи после разговора с ней
#call ep01_dialogues2_day1_family_5() # вечером в гостиной, клик на Генри
#call ep01_dialogues2_day1_family_6() # попытка зайти в комнату старшей Оливии вечером
#call ep01_dialogues2_day1_family_7() # попытка зайти в комнату младшей Синтии
#call ep01_dialogues2_day1_family_8() # комната Барди, при выборе пункта меню "Лечь спать"


label ep01_dialogues2_day1_family_1:
    # кадр на комнату Барди
    # звук шагов, звук открывающейся двери
    # на пол или на кровать падает рюкзак
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("СПУСТЯ ЧАС")) from _rcall_textonblack_2
    scene black_screen
    with Dissolve(1)
    imgfl scene_House_Street_Evening
    music night_ambience
    w
    music Dont_Close_Your_Eyes
    imgfl 900026
    bardi_t "Это и есть моя комната?!"
    imgf 900027
    bardi_t "Твою же мать!"
    sound Jump1
    img 900028 hpunch
    bardi_t "!!!"
    sound sneaks_1
    imgf 900029
    bardi_t "Надо валить отсюда как можно быстрее!.."
    bardi_t "!!!"
    # голос Софи из-за двери
    imgd 900030
    sophie "[mcname], милый, мой руки и спускайся на ужин. Мы все ждем тебя!"
    bardi "Иду!"
    # злой пинок по стулу, кровати или рюкзаку
    sound vjuh3
    imgd 900031
    w
    img 900032
    w
    sound snd_kick_fred1
    img 900033 vpunch
    bardi "!!!"
    img 900032
    w
    menu:
        "Пойти на кухню.":
#            jump ep01_dialogues2_day1_family_2
            return True
        "Позже, сначала осмотреться.":
            # уход на движок
            # игрок может побродить по комнате и дому
            # затем сам топает до кухни, след. сцена запускается при клике на локацию Кухня
            pass
    imgf 900034
    bardi_t "Думаю, ничего страшного, что им придется немного подождать меня..."
    return False

# в телефоне в Инсте можно сделать в аккаунте Барди один опубликованный (или сохраненный в галерее) пост
# фотка - селфи Барди на фоне вокзала, он показывает фак в камеру
# и текст:
# "Наконец-то, этот долгожданный день настал! Сегодня я оставляю это гребаное захолустье!"
# "Прощайте, деревенщины-одноклассники! Я уезжаю!"
# "Меня ждет новая, счастливая и богатая жизнь в огромном городе!"
# "Я поступлю в лучший колледж страны! Я смогу позволить себе ВСЕ!"
# "Крутые тачки, крутые девчонки, элитные ночные клубы и улетные вечеринки!.."
# "У меня все только начинается!"
# "Завидуйте мне, лузеры!"
# под постом коммент от Гарри "Сам ты лузер! Увижу - надеру тебе зад, ушлепок!"


## мысли не рендерить!!
# комната Барди
# мысли при клике на кровать, если утро или день, вечером и ночью меню из лейбла ep01_dialogues2_day1_family_3
label ep01_dialogues2_day1_family_1_1:
    bardi_t "Мне еще рано ложиться спать."
    return False
# мысли при клике на окно
label ep01_dialogues2_day1_family_1_2:
    bardi_t "Может, сбежать отсюда? Вокзал, поезд..."
    bardi_t "И что дальше?"
    bardi_t "Отец меня не ждет, а больше мне некуда идти."
    return
# мысли при клике на стол
label ep01_dialogues2_day1_family_1_3:
    bardi_t "Здесь я буду делать домашние задания для колледжа."
    bardi_t "Черт! Колледж. Не хочу сейчас думать об этом."
    return
# мысли при клике на печатную машинку
label ep01_dialogues2_day1_family_1_4:
    bardi_t "А это еще что за древность?"
    bardi_t "Они мне вместо компа поставили ЭТО?!"
    return
# мысли при клике на лист в печатной машинке
label ep01_dialogues2_day1_family_1_5:
    bardi_t "Там что-то написано..."
    # можно сделать приближение к листу
    unknown_writer "Меня не покидают мысли о том, что я совершила ошибку."
    unknown_writer "Если бы я могла повернуть все назад, вернуться в прошлое..."
    unknown_writer "Я не стала бы вступать в эти болезненные отношения."
    unknown_writer "Я потеряла свою индивидуальность, я потеряла себя."
    unknown_writer "Я забыла, что такое быть любимой и желанной..."
    unknown_writer "К сожалению, сейчас уже ничего не изменишь."
    unknown_writer "Каждый день я вынуждена улыбаться и притворяться счастливой."
    unknown_writer "А на самом деле..."
    unknown_writer "Только ночь знает мои истинные чувства и переживания."
    # лист отдаляется
    bardi_t "Похоже на отрывок из какого-то дневника."
    bardi_t "Интересно, кто написал это?"
    return
# холл на втором этаже
# мысли при клике на двери соседних комнат
label ep01_dialogues2_day1_family_1_6:
    bardi_t "Эта дверь закрыта."
    return
# мысли при клике на флипчарт
label ep01_dialogues2_day1_family_1_7:
    bardi_t "Зачем эта хрень тут стоит?"
    bardi_t "Они устроили здесь свалку из ненужных вещей?"
    return
# мысли при клике на стол
label ep01_dialogues2_day1_family_1_8:
    bardi_t "Чей-то рабочий стол."
    bardi_t "Странно, что его поставили здесь, а не в комнате."
    return
# мысли при клике на картины
label ep01_dialogues2_day1_family_1_9:
    bardi_t "Какие-то дурацкие картины."
    return
# гостиная
# мысли при клике на ТВ
label ep01_dialogues2_day1_family_1_10:
    bardi_t "Я не хочу сейчас смотреть телек."
    return
# мысли при клике на диван
label ep01_dialogues2_day1_family_1_11:
    bardi_t "Здесь все такое старое. Когда они последний раз делали ремонт и меняли мебель?"
    return
# мысли при клике на входную дверь
label ep01_dialogues2_day1_family_1_12:
    bardi_t "Мне пока там нечего делать."
    return False
# ванная комната
# мысли при клике на унитаз
label ep01_dialogues2_day1_family_1_13:
    bardi_t "Я недавно отлил. Пока не хочу."
    return False
label ep01_dialogues2_day1_family_1_13a:
    bardi_t "Я предпочитаю душ."
    return False
# мысли при клике на душ или ванную
label ep01_dialogues2_day1_family_1_14:
    imgfl 910311
    bardi_t "В этом старом доме только один душ."
    bardi_t "Это не очень удобно."
label ep01_dialogues2_day1_family_1_14b:
    menu:
        "Принять душ.":
            # кадры стены душа и капли воды, как будто Барди смотрит
            # вид из глаз вниз, видно член
            music Adventures_of_the_Deaf_Dreamer
            music2 snd_shower3
            imgf 910312
            bardi_t "Совсем недавно я жил в доме, где у меня были собственный душ и туалет."
            bardi_t "А тут, по ходу, можно и в очередь попасть, если приспичит."
            bardi_t "Такие контрасты... Жесть."
            music2 stop
            $ mcShowerLastDay = day
        "Позже.":
            imgd 910311
            bardi_t "Я пока не хочу принимать душ."
            pass
    return

label ep01_dialogues2_day1_family_1_14a:
    bardi_t "В этом старом доме только один душ."
    bardi_t "Это не очень удобно."
    return
# кухня
# при клике на любой предмет
label ep01_dialogues2_day1_family_1_15:
    if introKitchen1Day == day:
        return
    bardi_t "Какая маленькая кухня. Не то что в новом доме отца."
    $ remove_hook()
    return


label ep01_dialogues2_day1_family_2:
    # кухня
    # вся сцена проигрывается так, что мы смотрим глазами Барди
    # на столе перед каждым тарелки, столовые приборы и стаканы с соком
    # одно место за столом свободно, стоит пустой стул для Барди
    # за столом сидят Софи, ее муж Генри и две сестры - старшая Оливия и младшая Синтия
    # Софи и Синтия мило улыбаются Барди
    # Генри бросает в его сторону равнодушный взгляд и снова принимается за еду
    # Оливия отрывается от своего телефона и смотрит зло на Барди
    music Visions_Of_Plenty
    sound2 sneaks_1
    imgfl 900000
    w
    sound snd_eating
    imgf 900001
    w
    sound sneaks_1
    imgd 900002
    w
    imgd 900003
    olivia "Наконец-то, ты притащил свою задницу сюда, придурок!"
    olivia "Какого черта мы должны ждать тебя?!"
    imgd 900004
    bardi_t "Вот так встреча..."
    bardi "Эм... Ну я..."
    # Софи делает ей замечание
    img 900005
    sophie "Оливия! Что за выражения?!"
    # Софи поворачивается к Барди, машет на Оливию рукой и улыбаясь говорит
    imgf 900006
    sophie "[mcname], не обращай на нее внимания! Она всегда такая колючая..."
    # младшая Синтия тоже сердито говорит Оливии
    imgd 900007
    cynthia "Он наш гость! Зачем ты так?!"
    # Оливия с презрением фыркает
    olivia "Пфф!!!"
    # Синтия с милой улыбкой говорит Барди
    imgf 900008
    cynthia "Я очень рада, что ты теперь будешь жить у нас, [mcname]."
    imgd 900009
    bardi "Угу... Я тоже."
    imgd 900008
    w
    # Софи говорит ему, мило улыбаясь
    imgf 900010
    sound snd_eating
    sophie "[mcname], милый, я тоже рада, что твой отец решил вернуть тебя в твой родной город. И что ты теперь будешь жить с нами."
    sophie "Все равно та комната, в которой ты теперь будешь жить, уже много лет стоит пустая."
    sophie "И моим девочкам будет веселее, что у них появился такой милый сосед. Надеюсь, вы подружитесь."
    # Оливия зло косится на Барди
    imgd 900011
    olivia "Еще чего!"
    # Софи не обращает внимания на дочь и продолжает разговаривать с Барди
    imgf 900012
    sophie "А в городе... Ну что тебе там делать одному, когда отец постоянно пропадает на работе?"
    imgd 900013
    sophie "Зато здесь ты можешь спокойно общаться с друзьями и вообще весело проводить время."
    imgd 900012
    bardi "..."
    # муж Софи Генри говорит равнодушно
    imgf 900014
    henry "[mcname], я вчера разговаривал с директором колледжа..."
    henry "Твои документы уже приняли и ты зачислен к ним."
    henry "Так что завтра у тебя начинаются занятия."
    # и Генри снова теряет интерес к происходящему
    imgd 900015
    sophie "В этом колледже учатся многие из твоих бывших одноклассников. Здорово, правда?!"
    sophie "Ты, наверное, очень скучал по ним, милый?"
    imgd 900016
    bardi "Угу... Очень..."
    imgd 900017
    sophie "Синтия учится на курсе на год младше твоего. Так что будете ходить в колледж вместе."
    # Синтия мило улыбается Барди
    imgf 900008
    cynthia "Скажи, прикольно, [mcname]?! Мы не только соседи по комнатам, но и учимся в одном колледже!"
    # Барди угрюмо
    imgd 900009
    bardi_t "Чему эта дурочка Синтия так радуется?!"
    bardi_t "Меня тошнит от одной мысли о колледже!"
    imgf 900018
    sophie "[mcname], милый, занятия в колледже начинаются завтра в 9 утра..."
    # Генри равнодушно бросает
    imgd 900019
    henry "Но сначала не забудь зайти в приемную директора."
    henry "Тебе нужно подписать какие-то документы."
    imgd 900020
    bardi "Угу."
    imgd 900018
    sophie "Я приготовлю тебе на завтрак сэндвичи... Ты любишь сэндвичи, [mcname]?"
    imgd 900020
    bardi "Да, Софи."
    # кадр на Синтию - мило улыбается Барди
    imgf 900021
    cynthia "..."
    bardi_t "Хм... Ну окей... Вроде, Синтия и правда мне рада."
    # кадр на Оливию - пялится в свой смартфон
    imgd 900022
    olivia "У этой страшной дуры лайков больше, чем у меня! Какого черта?!"
    bardi_t "Чего не скажешь про Оливию!"
    bardi_t "Вообще ее не узнаю... Обозвала меня придурком и залипла в своем телефоне..."
    # кадр на Генри - он с безразличным видом ужинает
    imgf 900023
    henry "..."
    bardi_t "Этого Генри вообще интересует, что происходит? Он всегда такой безучастный?"
    bardi_t "И что Софи в нем нашла? Не понимаю."
    imgd 900024
    bardi_t "..."
    bardi_t "Все! С меня на сегодня хватит милого общения с моими соседями!"
    bardi_t "Не хочу больше никого видеть..."
    # Барди кладет вилку на стол и встает
    sound snd_plates1
    imgf 900025
    bardi "Я устал. Пойду спать."
    # Софи улыбается ему
    sophie "Да, конечно, [mcname]."
    bardi "Спасибо за ужин, Софи."
    # смена кадра на комнату Барди
    return

# в движке
label ep01_dialogues2_day1_family_3:
    # комната Барди, вечер
    # свободное перемещение по комнате и дому, если игрок кликает на кровать, то возникает меню
    # при клике на кровать
    menu:
        "Лечь спать.":
            bardi_t "Уже поздно. Я сегодня очень устал и хочу спать."
            return True
#            jump ep01_dialogues2_day1_family_8
        "Позже, я пока не устал.":
            # игрок может побродить по комнате и дому
            pass
    bardi_t "Я пока не хочу спать..."
    return False

label ep01_dialogues2_day1_family_3a:
    menu:
        "Ждать до полудня." if day_time_idx == 0:
            return 1
        "Ждать до вечера." if day_time_idx <= 1:
            return 2
        "Ждать до ночи." if day_time_idx <= 2:
            return 3
        "Лечь спать до утра." if day_time_idx <= 3:
            return 4
        "Уйти.":
            return 0
    return

label ep01_dialogues2_day1_family_4:
    # Барди зашел вечером на кухню, Софи стоит у столешницы и что-то делает (например, моет посуду)
    # клик на Софи
    # она поворачивается к нему и улыбается
    music Little_Tomcat
    imgf 900035
    sophie "[mcname]? Я думала, ты уже лег спать."
    imgd 900036
    bardi "Да, я как раз собираюсь..."
    imgd 900035
    sophie "Хорошо, милый. Тебе нужно выспаться - завтра рано вставать."
    sophie "Я тебя разбужу утром."
    imgd 900036
    bardi "Окей, Софи. Спасибо."
    return

label ep01_dialogues2_day1_family_4_1:
    # если повторный клик после этого диалога
    music Little_Tomcat
    imgf 900035
    sophie "Ты еще что-то хотел, милый?"
    imgd 900036
    bardi "Нет, Софи. Спокойной ночи."
    imgd 900035
    sophie "Спокойной ночи, [mcname]."
    return

label ep01_dialogues2_day1_family_5:
    # Барди зашел вечером в гостиную, Генри сидит с банкой или бутылкой пива и смотрит телек
    # клик на Генри
    # он поворачивается к Барди
    music Adventures_of_the_Deaf_Dreamer
    imgf 900037
    henry "[mcname], ты еще не спишь?"
    henry "Будешь пиво?"
    imgd 900038
    bardi "Нет, Генри. Как-нибудь в следующий раз."
    imgd 900037
    henry "Ладно. Мне больше достанется, хе-хе."
    # Генри отворачивается и снова утыкается в телек
    sound snd_drinking_water
    imgd 900039
    bardi_t "После пива он становится более дружелюбным."
    bardi_t "Если это можно так назвать..."
    return

label ep01_dialogues2_day1_family_6:
    # Барди пытается зайти в комнату старшей Оливии
    # клик на ее дверь
    sound snd_door_knock
    imgf 900040
    olivia "Кто там?"
    olivia "Мам, это ты? Я не хочу сейчас разговаривать..."
    olivia "И вообще, я занята и мне некогда!"
    bardi_t "Чем эта Оливия там занимается, что не может открыть дверь?.."
    call refresh_scene_fade() from _rcall_refresh_scene_fade
    return False

label ep01_dialogues2_day1_family_7:
    # Барди пытается зайти в комнату младшей Синтии
    # клик на ее дверь
    # дверь приоткрывается и выглядывает приветливая мордашка Синтии
#    if steamVersion == True:
#        sound snd_door_locked1
#        pause 1.0
#        call ep01_dialogues2_day1_family_1_6()
#        return False
    sound snd_door_open1
    fadeblack 1.5
    music Little_Tomcat
    imgf 900042
    cynthia "[mcname]? Ты пришел пожелать мне спокойной ночи?"
    imgd 900043
    bardi "Ммм... Да."
    bardi "Спокойной ночи, Синтия."
    imgd 900042
    cynthia "Это так мило с твоей стороны, [mcname]."
    imgd 900041
    cynthia "И тебе спокойной ночи. Завтра увидимся."
    # улыбается ему
    # дверь закрывается
    sound snd_door_close1
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_4
    return False

# при выборе пункта меню "Лечь спать"
label ep01_dialogues2_day1_family_8:
    # ночь
    # комната Барди, темнота
    # тиканье часов
    fadeblack
    music2 Jail_Clock
    pause 3.0
    music Right_Now_Vocal
    imgfl 900044
    bardi_t "Помню, однажды я лежал ночью в своей комнате и слушал, как мои родители ругались в гостиной..."
    bardi_t "Мама плакала и кричала, что отец променял нас на какую-то блондинистую шлюху..."
    bardi_t "Потом хлопнула входная дверь и стало тихо... Только тиканье часов... Как сейчас..."
    bardi_t "И мне было страшно. За маму, за отца. За нашу семью, которая в итоге распалась."
    imgf 900045
    bardi_t "Ненавижу тиканье часов."
    bardi_t "..."
    bardi_t "Возможно, для кого-то мой выбор, с кем из родителей остаться после их развода, покажется странным. Я выбрал отца."
    bardi_t "Хотя, он никогда не проявлял ко мне теплых отцовских чувств."
    bardi_t "Но я его единственный сын и он в состоянии обеспечить мне блестящее будущее..."
    bardi_t "Так и должно было быть. Все шло по плану: я поступил в лучший колледж в стране..."
    imgd 900046
    bardi_t "Но потом..."
    bardi_t "Потом появилась та лживая стерва! Из-за нее я теперь здесь, в глухой дыре!"
    # тиканье часов продолжается
    imgd 900044
    bardi_t "..."
    bardi_t "Думаю, Софи и правда рада, что я теперь буду жить у них."
    bardi_t "И ее дочь Синтия тоже..."
    bardi_t "Они обе кажутся очень дружелюбными и милыми..."
    bardi_t "Чего не скажешь об Оливии!.."
    # стук в дверь
    music2 stop
    sound snd_door_knock
    imgd 900030
    music stop
    bardi_t "???"
    # дверь приоткрывается, заходит Софи
    music Little_Tomcat
    imgf 900047
    sophie "[mcname], милый, ты уже спишь?"
    imgd 900048
    bardi "Нет еще, Софи..."
    imgd 900047
    sophie "Переживаешь из-за колледжа?"
    imgd 900048
    bardi "Вот еще! Нисколько!"
    # она садится на край его кровати
#    sound snd_walk_barefoot
    imgf 900049
    w
    imgd 900050
    sophie "Не переживай, [mcname]. Уверена, что все пройдет отлично."
    # она прикасается к его волосам и гладит его по голове
    imgd 900053
    bardi "..."
    # Софи задумчиво
    imgf 900051
    sophie "Когда ты со своим отцом уезжал из нашего городка..."
    sophie "Ты был совсем юным подростком."
    imgd 900052
    sophie "А сейчас ты кажешься таким взрослым..."
    sophie "Ты так изменился за это время, [mcname]."
    sophie_t "Стал такой высокий и такой... Хорошенький..."
    imgd 900051
    sophie_t "И очень похож на своего отца в юности."
    # она снова улыбается и еще раз проводит рукой по его волосам
    imgd 900050
    sophie "Не переживай, [mcname]. Все будет хорошо."
    imgd 900053
    bardi "Угу..."
    imgd 900054
    sophie "Спокойной ночи, милый..."
    bardi "Спокойной ночи, Софи."
    # Софи уходит
    fadeblack 2.0
    music stop
    music2 Jail_Clock
    imgf 900044
    w
    imgd 900045
    w
    # комната, тиканье часов
    music2 stop
    return
