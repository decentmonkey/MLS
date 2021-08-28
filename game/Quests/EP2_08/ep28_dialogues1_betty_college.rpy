default monicaShowedPussyToBardiePhoto1 = False
default dialogue_betty_teacher_1_flag = False
# Дом. Комната Барди. Разговор Барди и Бетти.
label dialogue_betty_college_0_1:
    # Бетти стоит в комнате Барди и недовольно
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Вечер...")) from _call_textonblack_43
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 14566
    with fadelong
    betty "Чего тебе надо? Зачем ты меня звал?"
    # Барди лежит на кровати и смотрит на Бетти с улыбочкой
    music Sneaky_Snitch
    img 14567
    with diss
    bardie "Мне нужно проверить, соблюдаешь ли ты правила этого дома..."
    img 14568
    with fade
    betty_t "Как же меня этот сопляк достал со своими глупостями! Пусть проверяет... и отстанет уже от меня."
    # подходит к Бетти и задирает ей юбку, заглядывает под нее. Бетти без трусиков. Барди довольно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14569
    with fadelong
    w
    img 14570
    with diss
    w
    img 14571
    with diss
    w
    music Sneaky_Snitch
    img 14572
    with fade
    bardie "Хорошо. Я вижу, что ты соблюдаешь правила. Позови гувернантку. Я давно не проверял ее."
    # Бетти недовольно
    music Power_Bots_Loop
    img 14573
    with diss
    betty "Тебе надо - ты и зови. Мне нет дела до твоих глупостей."
    img 14574
    with fade
    bardie "Я сказал тебе, чтобы ты позвала гувернантку..."
    bardie "Или ты решила, что меня не надо слушаться? Ты забыла, что у меня есть парочка очень интересных фото с тобой и тренером?"
    # Бетти поворачивается к Барди, зло смотрит на него
    music Groove2_85
    img 14575
    with diss
    betty_t "Когда же ты уже отстанешь от меня?!"
    betty_t "!!!"
    # Барди с серьезной миной
    img 14576
    with fade
    bardie "Ну? Я жду!"
    img 14577
    with diss
    betty "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    img 14578
    with fadelong
    with hpunch
    betty "Гувернантка! Гувернантка!!!"
    # спустя несколько минут появляется Моника, Барди возле Моники
    # с лица
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Power_Bots_Loop
    img 14579
    with fadelong
    mt "Эта деревенщина не знает, что так орать на весь дом - неприлично..."
    mt "Что на этот раз?.. Эта Бетти с этим малявкой. Я уже даже не знаю, чего ожидать от них."
    mt "Когда же они все уже исчезнут из моего дома?.."
    # со спины
    music Hidden_Agenda
    img 14580
    with fade
    m "Да, миссис Робертс..."
    # Бетти, не поворачиваясь к Монике
    # Барди идет к кровата
    music Groove2_85
    img 14582
    with diss
    betty "Гувернантка, я тебя позвала, чтобы..."
    img 14583
    with diss
    betty "..."
    # Барди прыгает на кровать
    sound Jump1
    img 14581
    with diss
    w
    img 14584
    with fade
    betty "Хм. Барди, что ты там хотел? Давай, быстрее.!"
    music Sneaky_Snitch
    img 14585
    with diss
    bardie "Мне нужно проверить, насколько хорошо вы соблюдаете правила этого дома и..."
    img 14586
    with diss
    betty "И?"
    img 14587
    with diss
    bardie "... и запечатлеть это на свой телефон!"
    # Барди поворачивается к Монике и говорит
    img 14588
    with fade
    bardie "Начнем с тебя. Ты же хорошая гувернантка? Ты соблюдаешь правила?"
    # Моника в шоке, смотрит на него, как на больного
    music Power_Bots_Loop
    img 14589
    mt "Он совсем обнаглел!!!"
    mt "Эта малявка требует от меня, Моники Бакфетт, чтобы я согласилась задрать юбку!"
    mt "Задрать юбку перед каким-то малявкой, который будет снимать это на телефон! Который поселился в МОЕМ доме!!!"
    mt "!!!"
    img 14590
    with fade
    m "Я не буду делать этого! Да как ты смеешь?! В обязанности гувернантки не входит позировать в голом виде перед камерой!"
    music Groove2_85
    img 14591
    with diss
    bardie "А в обязанности хорошей гувернантки - входит. Ты же хорошая гувернантка?"
    # Моника смотрит зло
    img 14592
    m "!!!"
    img 14593
    with fade
    bardie "Или ты не соблюдаешь правила этого дома и хочешь получить штраф?"
    bardie "???"
    # Моника думает
    if monicaUnder != "Nude":
        music Hidden_Agenda
        img 14594
        with fade
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        # Моника убегает
        sound highheels_run2
        music Groove2_85
        img 14595
        with diss
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return False
    img 14594
    with diss
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            # Моника убегает
            sound highheels_run2
            music Groove2_85
            img 14595
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return False
    img 14596
    with diss
    m "!!!"
    # Моника, срипя зубами соглашается, поднимает юбку, Барди фото не делает и смотрит на Бетти
    $ monicaShowedPussyToBardiePhoto1 = True
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 14597
    with fadelong
    w
    img 14598
    with diss
    w
    img 14599
    with fade
    bardie "Бетти, а ты чего ждешь? Я хочу запечатлеть на фото вас вдвоем. Поднимай юбку!"
    # Бетти офигевает и начинает ор-р-р-рать
    music Power_Bots_Loop
    img 14600
    with hpunch
    betty "Если эта шлюха готова поднять юбку перед любым, даже перед моим приемным сыном..."
    betty "То я на такое никогда не соглашусь!"
    music Groove2_85
    img 14601
    with diss
    betty "!!!"
    # Бетти уходит, Моника продолжает держать юбку и смотрит ей вслед
    sound highheels_run2
    img 14602
    with fade
    betty "Я порядочная замужняя женщина и ты не смеешь требовать от меня такого!" #высокомерно
    bardie "Стой! Я с тобой еще не договорил! Ты куда?" # в этом же арте
    # кадр меняется на Барди
    music Sneaky_Snitch
    img 14603
    with diss
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return True

label dialogue_betty_college_0_1b:
    mt "Вот малявка!"
    return

# Дом. Спальня. Разговор Барди и Бетти.
label dialogue_betty_college_1:
    # Барди разговаривает нагло, отдает приказ
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Утро...")) from _call_textonblack_44
    scene black_screen
    with Dissolve(1)
    music Sneaky_Snitch
    img 14604
    with fadelong
    w
    img 14605
    with diss
    bardie "Сегодня мой преподаватель вызывает к себе родителей..."
    # Бетти вопросительно
    img 14606
    with diss
    betty "???"
    # Поворачивается
    music Groove2_85
    img 14607
    with fade
    betty "А я здесь причем?"
    betty "Иди к Ральфу, скажи ему об этом."
    img 14608
    with diss
    bardie "Ты же моя приемная мать. Ты и сходишь в колледж. Отцу не обязательно об этом знать."
    bardie "У меня там небольшие проблемы: меня могут отчислить. Я хочу, чтобы ты уладила этот вопрос."
    img 14609
    with fade
    betty "В смысле, 'ты хочешь'?! Почему я должна идти в колледж и вообще тратить свое время на это?"
    img 14610
    with diss
    bardie "Потому что отцу не обязательно знать не только о том, что у меня проблемы в колледже, но и еще кое о чем..."
    bardie "О чем мы оба с тобой знаем."
    # Бетти зло смотрит
    img 14611
    betty "!!!"
    img 14612
    with fade
    bardie "Вот поэтому сегодня именно ТЫ пойдешь в колледж и сделаешь так, чтобы меня не отчислили!"
    # Бетти раздражена назойливостью Барди
    img 14613
    with diss
    betty_t "Чего эта малявка пристала ко мне?! Как бы поскорее отвязаться от него?"
    img 14614
    with diss
    betty "Это твои проблемы, разбирайся с этим сам!"
    img 14615
    with fade
    bardie "Это наша общая проблема! Так же, как и проблема того, что ты трахаешься со всеми подряд!"
    # Бетти, кипя от злости
    img 14616
    betty "!!!"
    img 14617
    with diss
    betty "Вообще-то, я верная жена! Не смей говорить обо мне такое!"
    # Барди в ответ смеется
    img 14618
    with fade
    bardie "Если хочешь, чтобы отец и дальше думал, что ты верная жена, делай, что я тебе говорю."
    bardie "И только попробуй не уладить вопрос моего отчисления. Тебе же хуже будет!"
    # Бетти убийственным взглядом смотрит на него и уходит
    img 14619
    betty "!!!"
    img 14620
    with fade
    bardie_t "Мне нужно будет убедиться, что она все сделает правильно. Надо за ней проследить!"
    return

# Дом. Второй этаж. Бетти, выйдя из комнаты Барди.
label dialogue_betty_college_1_1:
    # не рендерить!
    betty_t "Как этот сопляк смеет так со мной разговаривать?!"
    betty_t "Теперь мне придется идти в колледж и решать его проблемы. Как-будто у меня более важных дел нет!"
    return

label dialogue_betty_college_1_1a0:
    betty "Нет времени на это..."
    return False

label dialogue_betty_college_1_1a:
# мысли Бетти
    # не рендерить!
    # если перемещение не на ту локацию
    betty_t "Мне нужно идти в колледж, иначе Барди от меня не отвяжется."
    if bettyCollegeDay < 2:
        betty_t "По-моему, колледж находится где-то недалеко от дома."
    return
label dialogue_betty_college_1_1b:
    # если вышла со школы и хочет снова туда зайти
    betty_t "Сегодня мне там больше нечего делать. Мне надо идти домой."
    return
label dialogue_betty_college_1_1c:
    # смотрит на Барди
    betty_t "Ненавижу это сопляка! Как он смеет командовать в моем доме?"
    return
label dialogue_betty_college_1_1d:
    # говорит с Барди
    betty_t "Я не хочу разговаривать с ним. Иначе опять начнет приставать со своими глупостями."
    return
label dialogue_betty_college_1_1e:
    # смотрит на Ральфа
    betty_t "Он даже не представляет, как ему повезло с такой порядочной и умной женой, как я."
    return
label dialogue_betty_college_1_1f:
    # говорит с Ральфом
    betty_t "О чем мне с ним говорить? Сейчас опять начнет нудеть о своей работе. Как-будто мне это интересно."
    return
label dialogue_betty_college_1_1g:
    # смотрит на Монику
    betty_t "Нужно внимательнее следить за этой гувернанткой. Какая-то она подозрительная."
    return
label dialogue_betty_college_1_1h:
    # говорит с Моникой
    betty "Гувернантка, ты недостаточно тщательно оттираешь пятно на ковре. За столько дней могла бы уже очистить его."
    return
label dialogue_betty_college_1_1i:
    # смотрит на дом
    betty_t "Я всегда мечтала быть хозяйкой в таком большом и красивом доме. Теперь он мой!"
    return False
label dialogue_betty_college_1_1j:
    # внутри дома
    betty_t "Мне нравится дизайн этого дома. Тот, кто это все делал, явно обладает изысканным вкусом... Не то, что моя гувернантка!"
    return
label dialogue_betty_college_1_1k:
    # смотрит на учителя
    betty_t "Мистер Эдвардс... Надеюсь, мне без труда удастся с ним договориться. Он просто не сможет отказать такой порядочной женщине, как я."
    return
label dialogue_betty_college_1_1l:
    # осматривает школьный класс, окна
    betty_t "Панорамные окна в классе? Сомнительное решение. Какой-нибудь сопляк вполне может вывалиться оттуда."
    return
label dialogue_betty_college_1_1m:
    # осматривает школьный класс, шкаф с книгами
    betty_t "Книги - это, конечно, хорошо... Но очень скучно. Есть множество более интересных вещей."
    return
label dialogue_betty_college_1_1n:
    # осматривает школьный класс, доска
    betty_t "Какие-то сложные математические формулы... Как в этом вообще что-то можно понять?"
    return
label dialogue_betty_college_1_1o:
    # осматривает школьный класс, карта
    betty_t "Какая оригинальная карта мира. На ней вообще не понятно, какая страна, где находится."
    return
label dialogue_betty_college_1_1p:
    # осматривает школьный класс, парты
    betty_t "Я за такими партами тоже когда-то училась. Вернее, делала вид, что училась. Учеба - это так неинтересно."
    return
label dialogue_betty_college_1_1r:
    # осматривает школьный класс, формулы на стене (картины)
    betty_t "Как в этом вообще можно разбираться?"
    return
label dialogue_betty_college_1_1s:
    # смотрит на колледж (глазик)
    betty_t "Всегда не любила учиться. У меня только одно желание, когда вижу колледж - поскорее уйти отсюда."
    return


# Двор школы. Бетти
label dialogue_betty_college_1_1_2:
    # не рендерить!
    # смотрит на колледж
    betty_t "Надеюсь, разговор с учителем этого сопляка не займет много времени. Надо быстрее решить эту проблему, и он, наконец, от меня отвяжется."
    return

# Колледж. Кабинет учителя. Разговор Бетти с учителем. Барди, подглядывает, стоя за дверью кабинета.
label dialogue_betty_teacher_1:
    # Бетти садится напротив учителя, который сидит за учительским столом. Бетти с улыбкой
    if dialogue_betty_teacher_1_flag == False:
        music Groove2_85
        img 14735
        with fadelong
        w
        img 14741
        with diss
        w
        img 14742
        with fade
        w
        img 14736
        with diss
        w
        sound highheels_short_walk
        img 14743
        with fade
        w

        music stop
        img black_screen
        with diss
        pause 2.0
        music Groove2_85
        img 14737
        with fadelong
        betty "Добрый день, мистер..."
        # учитель с серьезным лицом
        img 14738
        with diss
        teacher "...Эдвардс. Добрый день. Я так понимаю, вы - мать Барди?"
        img 14739
        with fade
        betty "Да, мистер Эдвардс. Барди сказал, что у него какие-то проблемы..."
        img 14740
        with diss
        teacher "У Барди серьезные проблемы с успеваемостью. У него много прогулов и много не сданных зачетов."
        teacher "Я неоднократно пытался проводить с ним разъяснительные беседы, но безуспешно."
        teacher "К сожалению, я вынужден вам сообщить, что я сейчас готовлю документы на отчисление Барди для передачи директору."
        img 14744
        with fade
        betty "Мистер Эдвардс, документы еще находятся у вас? Я могу их посмотреть?"
        img 14745
        with diss
        teacher "Да, конечно. Я вас пригласил сегодня именно для этого. Вот личный файл Барди, можете ознакомиться."
        # Учитель дает Бетти папку с документами, та их просматривает, сосредоточенно думая. Учитель в это время пялится на ее грудь
        img 14746
        with vpunch
        betty_t "Этот мелкий сопляк совсем не бывает в колледже!"
        betty_t "Если мне удастся уговорить учителя притормозить это дело, у меня появится отличная возможность приструнить его..."
        img 14747
        with diss
        w
        img 14748
        with diss
        betty_t "В противном случае, Барди мне вообще никакой жизни не даст. Я итак его уже видеть не могу."
        betty_t "Интересно, как мне уговорить этого мистера Эдвардса? Может, попросить денег у Ральфа? Скажу, что для колледжа..."
        # Бетти поднимает взгляд на учителя, тот продолжает пялиться на нее. Бетти уже без улыбки, с серьезным выражением лица
        img 14749
        with fade
        betty "Мистер Эдвардс, я вижу, что у Барди совсем все плохо с учебой. Этот сорванец и правда в последнее время совсем отбился от рук."
        betty "Возможно, мы с вами как-то сможем уладить этот вопрос? Я могла бы оказать спонсорскую помощь колледжу. Купить мел для доски, например."
        betty "Я обещаю, что поговорю с Барди. Этот сопл... Барди больше не будет прогуливать занятия и сдаст все зачеты."
        sound Jump2
        img 14750
        teacher "..."
        img 14751
        with fade
        betty "Мистер Эдвардс?"
        # учитель, наконец, отрывает взгляд от ее груди.
        img 14752
        with diss
        teacher "А? Что?"
        img 14753
        with fade
        betty "Я говорю, что готова поговорить с Барди и он будет себя хорошо вести..."
        img 14754
        with diss
        teacher "..."
        img 14755
        with fade
        teacher "Ну... Я даже не знаю... Документы уже подготовлены."
        teacher "Боюсь, что ничего уже нельзя изменить."
        # Барди подглядывает через приоткрытую дверь, переживает
        music Sneaky_Snitch
        img 14756
        with fade
        bardie_t "Черт!"
        bardie_t "..."
        bardie_t "Эта деревенщина не сможет договориться с преподом. Надо было гувернантку посылать к нему."
        # Бетти продолжает уговаривать учителя
        music Groove2_85
        img 14757
        with diss
        betty "Личный файл Барди все еще находится у вас. Значит, именно от вас зависит, дойдут ли документы до директора."
        betty "Что я могу сделать для того, чтобы Барди остался в колледже?"
        # препод снова залипает на груди Бетти, задумчиво
        img 14758
        with diss
        teacher "Хм. Я вижу, что вы искренне переживаете за сына, Миссис Робертс."
        # Бетти расплывается в улыбке
        img 14759
        with diss
        betty_t "Ненавижу этого сопляка!"
        img 14760
        with fade
        teacher "Возможно, я смогу что-нибудь придумать. Это будет непросто... Ведь, помимо меня, и другие учителя в курсе ситуации с Барди."
        teacher "Мне придется как-то аргументировать то, что я изменил свое решение..."
        img 14761
        with diss
        betty "Мистер Эдвардс, я понимаю, что это сложный процесс. Если я смогу чем-то вам помочь, то я буду только рада."
        # тут Бетти случайно роняет паку Барди на пол
        img 14762
        with vpunch
        #sound папка падает на пол
        sound down7
        betty "Oй!"
        img 14763
        with diss
        w
        # наклоняется за ней, поворачивает голову и видит, что учитель сидит с внушительным стояком
        img 14764
        with diss
        w
        sound Jump1
        img 14765
        with diss
        betty "!!!"
        # Бетти зависает на этом зрелище, но тут же берет себя в руки, выпрямляется. Глаза у нее заблестели, но она делает вид, что ничего не видела
        #video teacher dick up
        img black_screen
        with diss
        sound erection1
        scene black
        image videov_Teacher_Betty_DickUp_1 = Movie(play="video/v_Teacher_Betty_DickUp_1.mkv", fps=30, loop=False, image="/images/Slides/v_Teacher_Betty_DickUp_1_stop.jpg")
        show videov_Teacher_Betty_DickUp_1
#        with fadelong
        wclean

#       img 14766
#        with diss
        betty "..."
        $ dialogue_betty_teacher_1_flag = True

    music stop
    img black_screen
    with diss
    pause 2.0
    music Hidden_Agenda
    img 14767
    with fade
    betty "Так на чем мы остановились, мистер Эдвардс?.."
    # учитель догадался, что она его спалила, и принимает решение развести Бетти на "помощь"
    img 14768
    with diss
    teacher "На том, что вы могли бы мне помочь в этом непростом деле."
    # Бетти воодушевленно
    img 14769
    with fade
    betty "Да, конечно. Я буду рада помочь вам. Что мне нужно будет сделать?"
    img 14770
    with diss
    teacher "..."
    # учитель встает со стула, поправляет ширинку и пристально смотрит на Бетти. Бетти сидит на стуле и не может оторвать взгляд от его стояка, который прямо перед ее лицом
    music Loved_Up
    img 14771
    with fadelong
    w
    img 14772
    with diss
    betty "М-м-мистер Эд-д-двардс... Я н-не совсем вас п-п-понимаю..."
    img 14773
    with fade
    betty_t "Вот черт. Что же мне делать?"
    betty_t "Так, стоп! Я же замужняя женщина и верная жена."
    betty_t "Тем более, я разговариваю с учителем Барди! Я не должна так смотреть на то, что у него в штанах!"
    # Бетти поднимает взгляд от ширинки препода и смотрит ему в глаза. Говорит возмущенно
    music Groove2_85
    img 14774
    with fade
    betty "Мистер Эдвардс! Я замужем! Как вы можете предлагать мне подобное?!"
    img 14775
    with diss
    teacher "Вы же сами предложили мне помощь, миссис Робертс... Это очень помогло бы мне..."
    # Бетти снова уставилась на его стояк
    img 14776
    with diss
    teacher "Тем более, я не прошу о многом. Вы могли бы просто приласкать его рукой. У меня так давно не было никого."
    teacher "А вы такая красивая, миссис Робертс, что я просто не в силах держать себя в руках."
    # учитель медленно начинает расстегивать ремень
    sound snd_zip
    img 14777
    with fade
    betty_t "..."
    betty_t "Я не должна этого делать! Что вообще себе позволяет этот мистер Эдвардс?!"
    # учитель расстегивает молнию на брюках, Бетти не в силах отвести взгляд
    img 14781
    with diss
    betty_t "С другой стороны..."
    betty_t "Хм... Если я просто потрогаю его, это же не будет считаться изменой?"
    img 14782
    with fade
    betty "М-мистер Эд-двардс, если об этом кто-нибудь узнает..."
    img 14783
    with diss
    teacher "Миссис Робертс, это не в моих интересах, чтобы кто-либо узнал о нашей с вами договоренности."
    teacher "Я в виде исключения предлагаю вам единственный из всех возможных способов решить эту проблему с вашим сыном."
    teacher "Для этого вам достаточно просто протянуть руку..."
    # препод достает свой стояк
    music Loved_Up
    sound Jump1
    img 14784
    with diss
    teacher "... и немного погладить его."
    img 14785
    with diss
    betty "!!!"
    img 14786
    with diss
    menu:
        "Убежать.":
            music Groove2_85
            betty "Я не буду этого делать!!!"
            return False
        "Постараться убедить учителя не делать этого":
            music Hidden_Agenda
            img 14787
            with fade
            betty "Мистер Эдвардс, я никогда себе не позволяю такого с другими мужчинами. Только с мужем..."
        "Поддаться давлению со стороны учителя":
            music Hidden_Agenda
            img 14788
            with fade
            betty "Мистер Эдвардс, я, конечно, не совсем уверена. Это единственный способ?"
            betty_t "У него просто каменный стояк. Если я к нему притронусь... Так интересно ощутить его."
    music Loved_Up
    img 14789
    with fade
    teacher "Это единственный способ, миссис Робертс. Просто прикоснитесь ко мне."
    # Бетти протягивает руку и замирает буквально в сантиметре от члена
    music Hidden_Agenda
    img 14790
    with diss
    betty_t "Что я делаю? Это так неправильно..."
    betty_t "Я просто потрогаю его и вопрос с Барди будет решен. Я делаю это не ради своего удовольствия!"
    # препод берет ее за запястье и притягивает ее руку к своему члену, Бетти прикасается к нему пальцами
    img 14791
    with diss
    w
    img 14792
    with diss
    betty_t "Ммм... Он и правда каменный. И такой горячий..."
    img 14793
    with fade
    betty "Мистер Эдвардс, я... мне... это так неправильно..."
    music Loved_Up
    img 14794
    with diss
    teacher "Вы уже делаете это, миссис Робертс. Еще совсем немного. Сожмите его своей ручкой."
    # препод убирает свою руку, Бетти обхватывает его член рукой
    img 14795
    with fade
    betty_t "Ооо! У этого мистера Эдвардса просто отличный член. Интересно, какой он на вкус?"
    betty_t "!!!"
    betty_t "О боже! О чем я думаю?!"
    # Бетти медленно начинает дрочить ему
    img 14796
    with diss
    sound drkanje5
    teacher "Да, так! У вас отлично получается, миссис Робертс! Быстрее!"
    # Бетти пристально смотрит на член и старается с удвоенной силой
    # Барди все видит и слышит. Волнение на его лице сменяется злорадной ухмылкой. Он достает свой смартфон и делает фото.
    music Sneaky_Snitch
    img 14797
    with fadelong
    bardie_t "Офигеть! Бетти даже в колледже умудрилась подержать чужой член в руке!"
    bardie_t "!!!"
    bardie_t "Может, будет какое-то продолжение?"

    # Бетти продолжает усердно работать рукой, не отрывая глаз от члена учителя
    img 14798
    with diss
    sound drkanje5
    w
    music Loved_Up2
    img 14799
    with fade
    sound drkanje5
    teacher "Ооо, миссис Робертс... Да, так! Еще..."
    teacher "Ммм... Еще быстрее!"
    #видео teacher_betty_handjob
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_1 = Movie(play="video/v_Teacher_Betty_HandJob_1_1.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_1
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
        scene black
        image videov_Teacher_Betty_HandJob_1_2 = Movie(play="video/v_Teacher_Betty_HandJob_1_2.mkv", fps=30)
        show videov_Teacher_Betty_HandJob_1_2
        wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_3 = Movie(play="video/v_Teacher_Betty_HandJob_1_3.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_4 = Movie(play="video/v_Teacher_Betty_HandJob_1_4.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_4
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
        scene black
        image videov_Teacher_Betty_HandJob_1_5 = Movie(play="video/v_Teacher_Betty_HandJob_1_5.mkv", fps=30)
        show videov_Teacher_Betty_HandJob_1_5
        wclean

    #препод со стоном кончает на личный файл Барди, который на столе, попадает и Бетти на руку
    stop music
    music stop
    music Loved_Up2
    sound bulk1
    img 14800
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "ООООООООО!!!"
    sound man_moan18
#    sound bulk1
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
    w

    # препод крайне доволен, надевает обратно брюки и садится за стол, а Бетти, изображая из себя оскорбленную невинность, вытирает руку

    # sound звук падающей спермы на папку (вввиухх...)
    sound hlup2
    music Groove2_85
    img 14801
    betty "Вы испачкали документы Барди, мистер Эдвардс."
    img 14802
    with fade
    teacher "Ничего страшного, миссис Робертс. Директор все равно этого не заметит."
    # Бетти в шоке, учитель с улыбочкой
    img 14803
    with diss
    betty "В смысле?! Мы же с вами договорились, что эти документы не дойдут до директора!"
    img 14804
    with fade
    teacher "Миссис Робертс, в моих силах пока только притормозить это дело."
    img 14805
    with diss
    betty "???"
    img 14807
    with fade
    teacher "Но если вы еще раз посетите меня на днях, то, возможно, я смогу закрыть этот вопрос."
    # Бетти удивленно
    img 14808
    betty "Еще раз?!"
    img 14809
    with diss
    teacher "Именно. Мне может снова потребоваться ваша помощь."
    # Барди злорадно ухмыляется за дверью
    music Sneaky_Snitch
    img 14806
    with fade
    bardie_t "!!!"
    bardie_t "Отлично! Нужно будет дождаться продолжения!"
    # Барди убегает, Бетти, сидя напротив учителя, пристально смотрит на него
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14810
    with fadelong
    betty_t "Из-за этого сопляка мне придется тащиться сюда снова. Он теперь в долгу передо мной. Нужно только окончательно уговорить учителя."
    img 14811
    with diss
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И, надеюсь, мы с вами закроем этот вопрос."
    img 14812
    with fade
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return True

# Двор школы. Бетти, выйдя из кабинета учителя
label dialogue_betty_college_1_1_3:
    # не рендерить!
    betty_t "По-моему, у меня отлично получилось убедить учителя не отчислять этого сопляка."
    betty_t "Почти получилось. Еще одна встреча - и дело сделано."
    return

# Дом. Двор. Спустя некоторое время Бетти возвращается домой и во дворе дома сталкивается с Барди.
label dialogue_betty_college_2:
    sound ball4
    # Барди делает вид, что ничего не знает, спрашивает Бетти
    music Groove2_85
    img 14621
    with fadelong
    bardie "Ну как? Надеюсь, ты все уладила?"
    # Бетти смотрит возмущенно
    img 14622
    with diss
    betty "Ты хоть видел свои оценки?! Ты думаешь так просто решить этот вопрос, если ты вообще не бываешь в колледже?!"
    # Барди строго
    img 14623
    with fade
    bardie "То есть у тебя не получилось договориться с учителем?"
    bardie "..."
    bardie "Я так и знал, что тебе ничего нельзя поручить..."
    music Power_Bots_Loop
    img 14624
    with diss
    betty "Ты как со мной разговариваешь, сопляк! Почему это мне ничего нельзя поручить?! Я почти договорилась с ним!"
    # Барди заинтересованно
    music Groove2_85
    img 14625
    with fade
    bardie "Что значит 'почти'?"
    # Бетти растерянно смотрит на Барди
    img 14626
    with diss
    betty "..."
    img 14627
    with diss
    betty_t "Черт!.."
    betty_t "Вот пристал! Я что, должна отчитываться перед ним?!"
    # отводит взгляд в сторону, Барди вопросительно смотрит на нее
    img 14628
    with fade
    bardie "Ну?"
    img 14629
    with diss
    bardie_t "Давай, соображай быстрее. Даже соврать нормально не может..."
    music Hidden_Agenda
    img 14630
    with diss
    betty "Мы... Хм..."
    betty "..."
    # Бетти поворачивается к Барди, с уверенным видом заявляет
    img 14631
    with fade
    betty "Мы с мистером Эдвардсом обсуждаем, на каких условиях нам договариваться!"
    betty "!!!"
    # Барди с сарказмом и мерзкой улыбочкой
    music Groove2_85
    img 14632
    with fade
    bardie "И чего учитель хочет?"
    img 14633
    with diss
    betty "..."
    img 14634
    with fade
    betty "А это не твое дело, сопляк!"
    betty "Как только учитель согласится не выкидывать тебя из колледжа, я тебе об этом скажу!"
    betty "А теперь отойди! У меня нет времени на тебя!"
    img 14635
    with diss
    betty "!!!"
    # Бетти уходит, Барди, все с той же улыбочкой
    music Sneaky_Snitch
    img 14636
    with fade
    bardie_t "Ну-ну. Я прослежу, как ты дальше будешь 'договариваться' с ним."
    bardie_t "Мастер переговоров. Аха-ха!"
    return

# Дом. Двор. Если Бетти убежала от учителя.
label dialogue_betty_college_2_1:
    # Барди делает вид, что ничего не знает, спрашивает Бетти
    music Groove2_85
    img 14625
    with fadelong
    bardie "Ну как? Надеюсь, ты все уладила?"
    # Бетти смотрит возмущенно
    img 14638
    with diss
    betty "Ты хоть видел свои оценки?! Ты думаешь так просто решить этот вопрос, если ты вообще не бываешь в колледже?!"
    # Барди строго
    img 14629
    with fade
    bardie "То есть у тебя не получилось договориться с учителем?"
    bardie "..."
    bardie "Я так и знал, что тебе ничего нельзя поручить..."
    # Бетти орет
    music Power_Bots_Loop
    img 14634
    with fade
    betty "Ты как со мной разговариваешь, сопляк!"
    betty "Я не буду решать твои проблемы в колледже!"
    betty "Разбирайся с этим сам!"
    img 14636
    with diss
    betty "А теперь отойди! У меня нет времени на тебя!"
    betty "!!!"
    # Бетти уходит, Барди ей вслед
    img 14640
    with diss
    bardie "Стой! Я с тобой еще не договорил! Ты куда?"
    # кадр меняется на Барди
    music Sneaky_Snitch
    img 14641
    with fade
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return

# Дом. Второй этаж.
label dialogue_betty_college_3:
    # Бетти нахмуренно смотрит на себя в зеркало
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14655
    with fadelong
    betty_t "!!!"
    betty_t "Как же меня достал этот мерзкий мальчишка со своими глупостями! Не могу его больше видеть!"
    betty_t "Скорее бы закрыть вопрос с его отчислением. Надеюсь, тогда он отстанет от меня!"
    music Hidden_Agenda
    img 14656
    with diss
    betty_t "..."
    # с улыбкой
    img 14657
    with diss
    betty_t "Хм... А у меня сегодня хорошо получилось уговорить учителя насчет документов этого сопляка..."
    betty_t "Я не только порядочная, но еще и умная женщина. Ральфу очень повезло, что у него такая жена, как я!"
    return

# Двор школы. Бетти
label dialogue_betty_college_1_1_4:
    # не рендерить!
    betty_t "Надеюсь, сегодня я смогу с мистером Эдвардсом закрыть вопрос отчисления этого сопляка."
    return

# Колледж. Кабинет учителя. Барди снова прячется за приоткрытой дверью кабинета.
label dialogue_betty_teacher_2:
    # Бетти сидит напротив учителя, как в прошлый раз. Говорит с улыбкой
    music Groove2_85
    img 14778
    with fadelong
    w
    sound highheels_short_walk
    img 14779
    with diss
    w
    img 14780
    with fade
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    # учитель тоже улыбается
#    img 14813
    img 14815
    with diss
    teacher "Рад вас видеть снова, миссис Робертс. Документы Барди все еще у меня."
    img 14814
    with fade
    betty "Спасибо. Я надеюсь, что мы с вами закроем сегодня этот вопрос?"
    img 14815
    with diss
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    img 14816
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    img 14817
    with diss
    betty_t "Почему мне, порядочной женщине, приходится заниматься подобными вещами из-за какого-то малявки?!"
    betty_t "Мне снова придется работать рукой? Что ж, в прошлый раз это помогло..."
    betty_t "Но только рукой! На большее я не соглашусь, это уже будет изменой! А я замужняя женщина!"
    img 14818
    with diss
    teacher "..."
    img 14819
    with diss
    betty "Мистер Эдвардс?"
    img 14820
    with fade
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди?"
    # Бетти растерянно
    music Hidden_Agenda
    img 14821
    with diss
    betty "???"
    betty "Я... Я думала, что мы просто повторим нашу прошлую встречу..."
    music Loved_Up
    img 14822
    with fade
    teacher "Я просто потрогаю ее и все. У вас такая красивая грудь!"
    img 14823
    with diss
    betty "..."
    img 14824
    with diss
    menu:
        "Не делать этого. Я порядочная замужняя женщина. Я же пришла сюда, чтобы удовлетворить его только рукой...":
            music Groove2_85
            img 14825
            with fade
            betty "Мистер Эдвардс, я порядочная замужняя женщина. Как вы себе это представляете?"
        "Почему нет? Он же просто потрогает мою грудь.":
            img 14826
            with fade
            betty "Мистер Эдвардс, я не против, если вы только потрогаете ее. Не более того!"
    img 14827
    with diss
    teacher "Миссис Робертс, я просто теряю голову от вашей красоты! Позвольте мне прикоснуться к вам. Хотя бы один раз."
    # Бетти встает со стула, приспускает платье и оголяет грудь. Учитель встает, обходит свой стол и подходит к ней
    # Барди подглядывает через приоткрытую дверь, делает фото
    music Sneaky_Snitch
    img 14828
    with fadelong
    bardie_t "!!!"
    bardie_t "Сегодня в моей коллекции прибавятся отличные фотки с Бетти! Жаль, отец пока не может оценить их."
    # учитель берет в ладонь грудь Бетти, приподнимает ее, сжимает
    music Loved_Up
    img 14829
    with fade
    w
    img 14830
    with diss
    w
    #видео teacher_betty_titsgrooping
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_v.ogg"
    scene black
    image videov_Teacher_Betty_TitsGrooping_1_1 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_1.mkv", fps=30)
    show videov_Teacher_Betty_TitsGrooping_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_2.ogg"
    scene black
    image videov_Teacher_Betty_TitsGrooping_1_2 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_2.mkv", fps=30)
    show videov_Teacher_Betty_TitsGrooping_1_2
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_3.ogg"
        scene black
        image videov_Teacher_Betty_TitsGrooping_1_3 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_3.mkv", fps=30)
        show videov_Teacher_Betty_TitsGrooping_1_3
        wclean
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_4.ogg"
        scene black
        image videov_Teacher_Betty_TitsGrooping_1_4 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_4.mkv", fps=30)
        show videov_Teacher_Betty_TitsGrooping_1_4
        wclean

    img 14831
    with diss
    w
    img 14832
    with diss
    betty "Ох. Мистер Эдвардс. Достаточно." # ахххх
    img 14833
    with diss
    betty_t "Ммм, это так приятно..."
    img 14834
    with fade
    teacher "Миссис Робертс, я хочу поцеловать ее."
    img 14835
    with diss
    betty "Нет, нет. Мы об этом не договаривались." # возмущенно (но ахх)
    # учитель не слушает ее, целует ее соски
    img 14836
    with fade
    betty "Ох! Ооо!"
    #sound поцелуй груди
    sound kiss1
    img 14839
    with diss
    w
    img 14840
    with diss
    w
    #sound поцелуй груди
    music Loved_Up
    sound kiss1
    img 14838
    with diss
    betty_t "Мне нужно остановить это немедленно. Ммм... Иначе одной рукой я не обойдусь сегодня."
    betty_t "Я порядочная и замужняя женщина! Я не могу себе позволить большего!"
    # Бетти отталкивает препода, неуверенно
    img 14841
    with fade
    betty "Мистер Эдвардс! Давайте, сделаем все, как в прошлый раз и я пойду. У меня мало времени."
    sound snd_zip
    img 14842
    with diss
    teacher "Как скажете. Но вам же это нравится, миссис Робертс. Зачем вы сопротивляетесь?"
    # учитель расстегивает ремень и ширинку, достает член, Бетти смотрит на его стояк
    sound Jump1
    img 14843
    with diss
    teacher "Возьмите его в руку, миссис Робертс."
    img 14844
    with diss
    betty "..."
    # Бетти подходит к преподу ближе и гладит его член
    img 14845
    with fade
    betty_t "Ммм... Какой же он... Ммм..."
    betty_t "Так! Мне надо держать себя в руках и не забывать о том, что я замужем."
    img 14846
    with diss
    teacher "Давайте, миссис Робертс, смелее. Прикоснитесь к нему губами."
    img 14847
    with diss
    betty "Губами?!"
    img 14848
    with diss
    menu:
        "Как он мог предложить мне такое?! Я порядочная женщина!":
            img 14849
            with fade
            betty "Мистер Эдвардс, я не могу на такое согласиться. Я порядочная женщина."
        "Мне совсем неинтересно, какой он на вкус!!!":
            img 14850
            with fade
            betty "Мистер Эдвардс, вам не достаточно нравится, как я делаю это рукой и вы хотите большего?"
    img 14851
    with diss
    teacher "Миссис Робертс, просто поцелуйте его. Неужели он вам не нравится?"
    img 14852
    with diss
    betty_t "Черт!!! Мне неинтересно... Мне неинтересно..."
    img 14853
    with diss
    teacher "Всего один поцелуй..."
    img 14854
    with diss
    betty "Только один!"
    # Бетти опускается на колени перед преподом, смотрит на член
    img 14855
    with fade
    betty_t "Что я творю?"
    betty_t "..."
    betty_t "Я просто прикоснусь к нему губами... и языком. Я делаю это не ради себя!"
    # Бетти прикасается к члену учителя губами, потом проводит языком по головке
    img 14858
    with diss
    w
    img 14856
    with diss
    w
    img 14859
    with diss
    betty_t "Ммм... Ну и что, что он оказался таким вкусным..."
    # и еще раз языком по стволу и по головке
    # видео betty teacher licking
    img black_screen
    with diss
    pause 1.5
    music stop
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_1 = Movie(play="video/v_Teacher_Betty_DickLicking_1_1.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_2 = Movie(play="video/v_Teacher_Betty_DickLicking_1_2.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_3 = Movie(play="video/v_Teacher_Betty_DickLicking_1_3.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_3
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
        scene black
        image videov_Teacher_Betty_DickLicking_1_4 = Movie(play="video/v_Teacher_Betty_DickLicking_1_4.mkv", fps=30)
        show videov_Teacher_Betty_DickLicking_1_4
        wclean
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
        scene black
        image videov_Teacher_Betty_DickLicking_1_5 = Movie(play="video/v_Teacher_Betty_DickLicking_1_5.mkv", fps=30)
        show videov_Teacher_Betty_DickLicking_1_5
        wclean

    img 14860
    with diss
    w
    img 14861
    with diss
    w
    img 14862
    with diss
    betty "Мистер Эдвардс, я... думаю, что... достаточно..."
    # а сама облизывает его
    img 14863
    with diss
    teacher "Еще немного, миссис Робертс. Обхватите его губами."
    # Бетти обхватывает губами головку и насаживается головой на член
    stop music
    music Loved_Up2
    img 14865
    with diss
    w
    sound Jump2
    img 14864
    show screen photoshot_screen()
#    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "Ооо, да!"
    img 14866
    with diss
    betty_t "!!!"
    # Бетти запускает свою руку под платье, в трусики (платье поднимает, трусики красные)
    # audio из видео
    img 14867
    with diss
    betty "Ммммфмммффф..."
    # Бетти старательно делает минет преподу, а Барди делает фото
    img 14868
    with diss
    w
    # видео betty teacher blowjob
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_1 = Movie(play="video/v_Teacher_Betty_Blowjob_1_1.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_1
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
        scene black
        image videov_Teacher_Betty_Blowjob_1_2 = Movie(play="video/v_Teacher_Betty_Blowjob_1_2.mkv", fps=30)
        show videov_Teacher_Betty_Blowjob_1_2
        wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_3 = Movie(play="video/v_Teacher_Betty_Blowjob_1_3.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_4 = Movie(play="video/v_Teacher_Betty_Blowjob_1_4.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_4
    wclean
    music Sneaky_Snitch
    img 14857
    with fadelong
    bardie_t "В прошлый раз подрочила, сегодня отсосала... Как она старается, чтобы меня не отчислили!"
    bardie_t "Аха-ха!"
    bardie_t "!!!"
    # Бетти продолжает работать ртом
    music Loved_Up2
    img 14869
    with fade
    teacher "Ммм... Как же чертовски хорошо! Еще, быстрее!"
    img 14870
    with diss
    betty "Ммммфмммффф..."
    # препод со стоном кончает на ее лицо
    img 14871
    with diss
    w
    img 14872
    with diss
    w
    img 14873
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    img 14874
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "Ооо, дааааааа!"
    sound man_moan18
    # Бетти делает еще несколько движений своей рукой у себя в трусиках и кончает следом за ним
    img 14875
    with diss
    w
    img 14876
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan14
    betty "ООООООООО!!!"
    # препод крайне доволен (уже одет)
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14877
    with fadelong
    teacher "Миссис Робертс, это было великолепно. Думаю, нам с вами нужно будет еще раз встретиться, чтобы закрепить нашу договоренность."
    # смотрит на него снизу вверх, вся в сперме
    img 14878
    with diss
    betty "Еще раз?"
    img 14879
    with fade
    teacher "Именно. Еще раз и я закрою этот вопрос с отчислением Барди."
    # Барди злорадно ухмыляется за дверью
    music Sneaky_Snitch
    img 14880
    with fade
    bardie_t "!!!"
    bardie_t "Отлично!"

    # Барди убегает, Бетти, сидя на полу перед учителем
    sound snd_runaway
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14881
    with fadelong
    betty_t "Еще один визит к преподавателю и этот сопляк у меня в руках! Не могу дождаться, чтобы, наконец, поставить его на место."
    img 14882
    with diss
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И мы закрепим с вами нашу договоренность."
    img 14883
    with fade
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return True

# Двор школы. Бетти, выйдя из кабинета учителя
label dialogue_betty_college_1_1_5:
    # не рендерить!
    betty_t "Еще один визит к преподавателю и этот сопляк у меня в руках! Не могу дождаться, чтобы, наконец, поставить его на место."
    return

# Дом. Двор. Спустя некоторое время Бетти возвращается домой и во дворе дома сталкивается с Барди.
label dialogue_betty_college_4:
    sound ball4
    # Барди снова делает вид, что не знает ничего
    music Sneaky_Snitch
    img 14637
    with fadelong
    bardie "Ну как? Есть хорошие новости для меня?"
    # Бетти высокомерно
    music Groove2_85
    img 14638
    with fade
    betty "Ты думашь, что серьезные дела так быстро решаются?!"
    betty "Я же тебе сказала, что сообщу тебе! А пока отстань от меня!"
    img 14639
    with diss
    betty_t "Сопляк!"
    betty_t "!!!"
    # Бетти уходит, Барди хихикает злорадно
    sound highheels_run2
    img 14640
    with fade
    w
    music Sneaky_Snitch
    img 14641
    with diss
    bardie_t "Надо придумать, как 'отблагодарить' ее. Не зря же она так старательно договаривается с учителем."
    # задумчиво
    img 14642
    with diss
    bardie_t "Хм... У меня есть неплохая идея..."
    return

# Двор школы. Бетти
label dialogue_betty_college_1_1_6:
    # не рендерить!
    betty_t "Сегодня я выйду отсюда с хорошими новостями для сопляка. Наконец-то, я сделаю это."
    return

# Колледж. Кабинет учителя. Барди, как обычно, прячется за приоткрытой дверью кабинета.
label dialogue_betty_teacher_3:
    # Бетти сидит напротив учителя, как в прошлый раз. Бетти с улыбкой
    music Groove2_85
    img 14884
    with fadelong
    w
    img 14885
    with diss
    w
    sound highheels_short_walk
    img 14886
    with diss
    w
    img 14737
    with fade
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    img 14887
    with diss
    teacher "Рад вас видеть снова, миссис Робертс."
    img 14739
    with fade
    betty "Я надеюсь, что мы с вами закроем сегодня вопрос отчисления Барди с колледжа?"
    img 14888
    with diss
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    img 14816
    with diss
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    img 14817
    with diss
    betty_t "Сегодня нельзя соглашаться на большее! Достаточно было прошлого раза..."
    betty_t "Я не собираюсь изменять своему мужу!"
    img 14818
    with fade
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди, как в прошлый раз?"
    img 14890
    with diss
    betty "???"
    img 14889
    with fade
    betty "Я... Да. Только как в прошлый раз, не более того!"
    img 14758
    with diss
    teacher "Миссис Робертс, ну конечно! Вам не о чем переживать!"
    # Бетти встает, приспускает платье и оголяет грудь. Учитель подходит к ней, берет в ладонь грудь Бетти, целует соски
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14830
    with fadelong
    w
    img 14832
    with diss
    w
    #sound целует грудь Бетти
    sound kiss1
    img 14891
    with diss
    sound ahhh1
    betty_t "Ммм, как же хорошо..."
    img 14892
    with diss
    betty "Ох. Мистер Эдвардс."
    img 14893
    with fade
    teacher "Миссис Робертс, я сниму с вас платье? Оно мешает мне рассмотреть вашу красоту."
    # Бетти растерянно
    img 14894
    betty "Вы хотите снять с меня платье?!"
    img 14895
    with diss
    menu:
        "Это все закончится сексом. Я не должна делать этого! Я порядочная женщина...":
            img 14896
            with fade
            betty "Мистер Эдвардс, вы забыли, что я порядочная женщина? Достаточно моей голой груди."
        "Он хочет приласкать меня. Это же просто ласки, а не измена? Я же порядочная женщина...":
            img 14897
            with fade
            betty "Мистер Эдвардс, вам не достаточно моей голой груди и вы хотите большего?"
    img 14898
    with diss
    teacher "Миссис Робертс, я ничего такого не собираюсь делать. Просто приласкаю вас немного."
    teacher "Вы же в прошлый раз сделали мне приятно, теперь я хочу сделать так, чтобы и вам было хорошо."
    # Бетти возмущенно
    music Power_Bots_Loop
    img 14899
    with hpunch
    betty "Нет, Мистер Эдвардс! Вы - преподаватель. Как вы вообще можете предлагать мне такое?!"
    betty "Мне, замужней женщине!"
    music Groove2_85
    img 14900
    with fade
    teacher "Миссис Робертс, вы такая заботливая мать, так искренне переживаете за вашего сына..."
    teacher "Я предлагаю вам единственный из всех возможных способов окончательно решить вопрос об учебе Барди."
    teacher "Если вы сейчас откажетесь, то я буду вынужден передать документы Барди директору."
    teacher "И тогда ничего нельзя уже будет исправить. Подумайте хорошо, прежде чем отказывать мне."
    # Бетти пристально смотрит на препода, сомневается
    img 14901
    with diss
    betty "..."
    # принимает решение
    img 14902
    with fade
    betty "Ну ладно, мистер Эдвардс... Только быстро!"
    # Бетти раздевается до трусиков, учитель гладит ее рукой через трусики
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 14903
    with fadelong
    sound Jump1
    w
    img 14904
    with diss
    sound chpok3
    w
    #sound ах
    sound ahhh12
    img 14905
    with diss
    betty "Ах!"
    betty_t "О, как же приятно!"
    img 14906
    with diss
    w
    img 14907
    with diss
    sound chpok3
    w
    # учитель подводит ее к столу, нагибает над ним и снимает с нее трусики, второй рукой расстегивает свою ширинку
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 14917
    with fadelong
    sound Jump1
    w
    img 14918
    with diss
    betty "Ммм..."
    # продолжает рукой ласкать ее киску, а потом входит в нее пальцами
    #sound чавк
    sound chmok2
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w


    img 14921
    with diss
    w
    img 14924
    with diss
    sound ahhh12
    betty "Ооо... М-мистер Эд-двардс... Ммм..."
    img 14922
    with diss
    betty_t "Ох, черт! Как же хорошо! Но я должна остановить его!"
    img 14923
    with diss
    betty "М-мистер Эд-двардс, я... дум-маю, что... д-достаточно..."
    # учитель продолжает водить рукой туда-сюда
    img 14925
    with diss
    teacher "Еще немного, миссис Робертс. Раздвиньте ножки пошире."
    # учитель убирает пальцы, берет в руки свой член, нацеливается в киску Бетти и входит в нее
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up2
    img 14910
    with fadelong
    sound chmok2
    w
    #видео teacher betty sex 1
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_1 = Movie(play="video/v_Teacher_Betty_Sex_1_1.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_2 = Movie(play="video/v_Teacher_Betty_Sex_1_2.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_3 = Movie(play="video/v_Teacher_Betty_Sex_1_3.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_4 = Movie(play="video/v_Teacher_Betty_Sex_1_4.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_4
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_5 = Movie(play="video/v_Teacher_Betty_Sex_1_5.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_5
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_6 = Movie(play="video/v_Teacher_Betty_Sex_1_6.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_6
    wclean

    img 14911
    with diss
    w
    img 14912
    with diss
    w
    img 14913
    with diss
    betty "Ааааах!"
    img 14914
    with diss
    w
    img 14915
    with diss
    teacher "Ооооо..."
    img 14916
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_171
    w
    call photoshop_flash() from _call_photoshop_flash_172
    w
    # Барди злорадно ухмыляется за дверью и делает несколько кадров
    img 14908
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_173
    w
    bardie_t "!!!"
    bardie_t "Отлично! Теперь она от меня никуда не денется!"
    img 14909
    with fade
    # препод "любит" Бетти на столе, потом они перемещаются на пол, Бетти садится сверху
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 14926
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_1 = Movie(play="video/v_Teacher_Betty_Sex_2_1.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_2 = Movie(play="video/v_Teacher_Betty_Sex_2_2.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_3 = Movie(play="video/v_Teacher_Betty_Sex_2_3.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_4 = Movie(play="video/v_Teacher_Betty_Sex_2_4.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_4
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_5 = Movie(play="video/v_Teacher_Betty_Sex_2_5.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_5
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_6 = Movie(play="video/v_Teacher_Betty_Sex_2_6.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_6
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_7 = Movie(play="video/v_Teacher_Betty_Sex_2_7.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_7
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_8 = Movie(play="video/v_Teacher_Betty_Sex_2_8.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_8
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_9 = Movie(play="video/v_Teacher_Betty_Sex_2_9.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_9
    wclean
    music Loved_Up2
    img 14927
    with diss
    teacher "Ммммммм..."
    img 14928
    with diss
    betty "Только не кончайте в меня, мистер Эдвардс!"
    # Бетти двигается на учителе и через некоторое время кончает
    img 14929
    with diss
    w
    img 14930
    with diss
    w
    img 14931
    with diss
    w
    img 14932
    #sound бетти кончает
    sound woman_moan14
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "ООООООООО!!!"
    # препод вынимает из нее член и со стоном кончает на ее грудь
    img 14933
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 14934
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    teacher "Ооо, дааааааа!"
    img 14938
    with diss
    w
    # препод крайне доволен, лежит на полу, Бетти сидит на учителе, недоверчиво смотрит на него
    music Groove2_85
    img 14935
    with fade
    teacher "Миссис Робертс, это было великолепно. Считайте, что вопрос с отчислением Барди закрыт."
    # Бетти недоверчиво
    img 14936
    with diss
    betty "Это точно?"
    img 14937
    with fade
    teacher "Да, мы с вами только что закрепили нашу договоренность."
    # Барди делает еще фото и убегает, радостный
    music Sneaky_Snitch
    img 14939
    with fadelong
    w
    call photoshop_flash() from _call_photoshop_flash_174
    w
    # Бетти встает и одевается, препод тоже
    music stop
    img black_screen
    with diss
    sound snd_runaway
    pause 2.0
    music Groove2_85
    img 14940
    with fadelong
    sound snd_zip
    teacher "Если вдруг у Барди снова начнутся проблемы с учебой, я вам сразу же позвоню, миссис Робертс."
    img 14941
    with diss
    betty_t "Отлично! Я сделала то, чего хотел этот сопляк. С меня хватит!"
    betty_t "Теперь он не посмеет требовать от меня своих глупостей!"
    img 14942
    with fade
    betty "Хорошо, мистер Эдвардс. Было приятно сотрудничать с вами."
    img 14943
    with diss
    teacher "Всегда к вашим услугам, миссис Робертс."
    return True

# Двор школы. Бетти, выйдя из кабинета учителя
label dialogue_betty_college_1_1_7:
    # не рендерить!
    betty_t "Сейчас я устрою этому сопляку! Я покажу ему, кто хозяин в этом доме!"
    return

# Дом. Двор. Бетти возвращается домой и видит во дворе, как Барди играет с мячом.
label dialogue_betty_college_5:
    sound ball4
    # Барди снова делает вид, что не замечает ее. Бетти стоит, руки в боки и зовет его
    music Groove2_85
    img 14643
    with fadelong
    betty "Эй, ты! Иди сюда!"
    # Барди к ней подходит и, делая вид, что ничего не знает, вопросительно смотрит на нее
    # Барди держит мяч
    sound Jump1
    img 14644
    with fade
    bardie "???"
    bardie "Что?"
    # Бетти ему высокомерно
    img 14645
    with diss
    betty "Я договорилась с твоим преподавателем. Это было непросто, но я смогла его убедить не отчислять тебя из колледжа."
    betty "Он очень не хотел оставлять тебя. Мне пришлось три раза посетить его и, в итоге, я смогла его уговорить."
    # Барди продолжает молча смотреть на нее, но уже едва сдерживает улыбку
    img 14646
    with diss
    bardie "..."
    img 14647
    with fade
    betty "Я сделала то, о чем ты меня попросил. Но хочу сразу тебя предупредить, что я в любой момент могу позвонить мистеру Эдвардсу..."
    # Бетти с угрозой
    img 14648
    with diss
    betty "... и он выкинет твою задницу из колледжа!"
    betty "!!!"
    betty "Поэтому с этого дня ты перестаешь строить из себя здесь хозяина и командовать мною! Если будешь хорошо себя вести, то с твоей учебой все будет в порядке."
    # Бетти с торжествующей улыбкой на лице
    img 14649
    with fade
    betty_t "Вот ты и попался, мелкий сопляк! Попробуй теперь покомандовать в моем доме!"
    img 14650
    with diss
    bardie "..."
    # На это Барди, не выдерживая, злорадно хохочет
    img 14651
    with fade
    bardie "Аха-ха!!! Ты это серьезно сейчас?!"
    bardie "!!!"
    bardie "Жду тебя через пять минут в своей комнате! И не задерживайся!"
    bardie "Аха-ха!!!"
    # Барди уходит, Бетти в недоумении
    img 14652
    with diss
    betty_t "???"
    sound snd_runaway
    img 14653
    with fade
    betty_t "Что еще этому мерзкому мальчишке нужно от меня?"
    betty_t "Почему я, такая порядочная и умная женщина, должна терпеть такое в своем же доме?!"
    betty_t "!!!"
    betty_t "Он, наверное, не понял, что он больше здесь не хозяин. Хм, что ж... Пойду к нему, объясню ему еще раз, более доходчиво!"
    # Бетти с уверенным видом уходит
    sound highheels_run2
    img 14654
    with diss
    w
    return

# Дом. Комната Барди.
label dialogue_betty_college_6:
    # Барди стоит возле своего стола и улыбается, Бетти заходит к нему в комнату, возмущается
    music Groove2_85
    img 15072
    with fadelong
    betty "Ты, наверное, не понял, о чем я тебе говорила! Ты почему со мной так разговариваешь?!"
    betty "!!!"
    # Барди с улыбочкой указывает рукой на свой ноут
    music Sneaky_Snitch
    img 15073
    with fade
    bardie "Я позвал тебя, чтобы ты посмотрела мою коллекцию фотографий. За последние дни я сделал несколько очень интересных фоток."
    img 15074
    with diss
    betty "???"
    betty "Что за глупости?! Какое мне дело до твоих дурацких коллекций?"
    img 15075
    with fade
    bardie "Я уверен, что тебе понравится... Посмотри."
    # Бетти подходит к его столу и заглядывает в ноут, видит на фото себя с учителем и офигевает
    #sound звук клавиши
    sound keyboard
    img 15076
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15077
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15078
    with diss
    betty "!!!"
    #sound звук клавиши
    sound keyboard
    img 15079
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15114
    with diss
    betty "ЧТО! ЭТО! ТАКОЕ?!"
    # Бетти бомбит
    music Power_Bots_Loop
    img 15080
    with fade
    betty "Ты что делаешь, сволочь!!!"
    betty "Я порядочная женщина! Что это за фотографии?!"
    betty "Как ты смеешь, мерзкий сопляк?! Я это сделала для тебя, а ты!.. Ты!!!"
    # Барди спокойно отвечает
    music Groove2_85
    img 15081
    with diss
    bardie "Я не просил тебя трахаться с ним. Ты даже в моем колледже нашла член, за который можно подержаться."
    bardie "На этих фото доказательство очередной измены моему отцу. Попробуй только сделать что-нибудь не так..."
    img 15082
    with diss
    bardie "..."
    bardie "Нууу, например, не слушаться меня... Эти фото сразу же увидит твой муж. И с того момента он станет уже твоим 'бывшем мужем'."
    # Бетти кипит от злости
    music Power_Bots_Loop
    img 15083
    betty_t "!!!"
    betty_t "Ненавижу! Да как он смеет?!"
    # Бетти смотрит на Барди убийственным взглядом
    img 15084
    with diss
    betty_t "Этот сопляк шпионил за мной! Он это все специально подстроил!"
    betty_t "!!!"
    music Hidden_Agenda
    img 15085
    with fade
    betty_t "Но я не могу позволить, чтобы Ральф увидел эти фотографии! Даже несмотря на то, что я это делала для его сына!"
    betty_t "..."
    # Бетти, злая, складывает руки на груди и спрашивает Барди
    music Groove2_85
    img 15086
    with diss
    betty "Чего тебе надо от меня?"
    img 15087
    with diss
    betty_t "Ненавижу этого сопляка!"
    img 15088
    with fade
    bardie "Так-то лучше."
    bardie "Помнишь, я хотел тебя сфотографировать с задранной юбкой? Ты мне отказала тогда..."
    bardie "Так вот..."
    # Бетти снова начинает орать
    music Power_Bots_Loop
    img 15089
    with fade
    betty "Да ты совсем охренел!"
    betty "НЕТ!"
    img 15090
    with diss
    betty "Ни за что!!! Я не буду фотографироваться так!"
    betty "!!!"
    # Барди с мерзкой улыбочкой
    music Groove2_85
    img 15091
    bardie "???"
    img 15092
    with diss
    bardie "Ты хорошо подумала?"
    img  15093
    with fade
    betty "..."
    # Барди показывает свой смартфон
    img 15094
    with diss
    bardie "Копии твоих фотографий с учителем есть у меня в телефоне. Отправить их отцу - вопрос нескольких секунд."
    img 15095
    betty "Ты не сделаешь этого!"
#    img 15096
    img 15097
    with diss
    bardie "Я уже делаю это."
    betty "!!!"
    # делает вид, что отправляет фотки, Бетти не выдерживает
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15098
    with fade
    betty "Хорошо, твоя взяла... Я согласна... Но только одно фото и ты обещаешь, что никому его не покажешь!"
    betty "..."
    img 15099
    bardie "Естественно, не покажу. Это только для меня..."
    img 15100
    with diss
    bardie_t "... и моего одноклассника."
    bardie_t "Теперь он мне точно поверит!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку, она в трусиках
    img 15101
    betty "Давай, быстрее!"
    # Барди ничего не делает и смотрит на нее вопросительно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15102
    with fadelong
    w
    img 15103
    with diss
    bardie "..."
    music Groove2_85
    img 15104
    with fade
    bardie "Во-первых, почему ты в трусах?"
    # Бетти опускает юбку, смотрит возмущенно и зло, но молчит
    img 15105
    with diss
    bardie "Ты забыла, что должна соблюдать правила этого дома? Снимай их, быстро!"
    bardie "Во-вторых, позови гувернантку. Я хочу сфотографировать вас вдвоем."
    # Бетти опять бомбит
    music Power_Bots_Loop
    img 15106
    betty "Я не собираюсь фотографироваться с этой шлюхой!"
    betty "!!!"
    music Groove2_85
    img 15107
    with diss
    bardie "Ты сейчас снимешь свои трусы и позовешь гувернантку! Я жду!"
    # Барди садится на свою кровать и демонстративно показывает Бетти свой телефон. Бетти кипит от злости, но подчиняется
    img 15108
    with diss
    w
    sound Jump1
    img 14581
    with diss
    w
    img 15109
    with diss
    w
    img 15110
    with fade
    betty_t "Ненавижу этого сопляка!"
    # Бетти отворачивается от Барди, со злостью снимает трусики
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 15111
    with fadelong
    w
    img 15112
    with diss
    betty "!!!"
    # Бетти с напряженным лицом зовет Монику
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 15113
    with hpunch
    betty "Гувернантка!!! Иди сюда!"
    # Барди самодовольно ухмыляется
    return

label dialogue_betty_college_7_cloth:
    mt "Мне лучше не идти туда в таком виде."
    return

# Комната Барди. Он наказывает Бетти. Та стоит голая в углу.
label dialogue_betty_college_8:
    bardie "Я крайне недоволен тем, как ты себя ведешь!" # строго
    betty "???"
    bardie "Ты отказалась решить мою проблему в колледже!"
    betty "..."
    menu:
        "Промолчать.":   #отказ проходить квест с учителем
            betty_t "Пусть сам разбирается со своими проблемами..."
            return False
        "Согласиться сходить в колледж.":   # квест с Бетти и учителем продолжается
            betty_t "Черт! Он теперь не отстанет от меня!"
            betty_t "Проще согласиться."
            betty "Я не забыла..."
            betty "Просто мне было некогда этим заниматься."
            betty "Я схожу в колледж и поговорю с учителем."
    return True







#
