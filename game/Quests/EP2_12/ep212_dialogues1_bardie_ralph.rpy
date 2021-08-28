# при условии, что у Барди достигнут максимальный уровень (8-?) и были сцены с одноклассником и не запущен ревендж-квест
# после уборки Барди ловит Монику

#call ep212_dialogues1_bardie_ralph1() # разговор с Барди с подвале
#call ep212_dialogues1_bardie_ralph2() # Моника думает после разговора с Барди
#call ep212_dialogues1_bardie_ralph3() # Моника 1-й раз приходит убираться в гостиную, меню
#call ep212_dialogues1_bardie_ralph4() # Моника убирается в трусиках Юлии
#call ep212_dialogues1_bardie_ralph5() # разговор с Барди после 1-й уборки
#call ep212_dialogues1_bardie_ralph6() # мысли Моники после ухода Барди
#call ep212_dialogues1_bardie_ralph7() # Моника 2-й раз приходит убираться в гостиную, мысли
#call ep212_dialogues1_bardie_ralph8() # Моника убирается в трусиках Бетти
#call ep212_dialogues1_bardie_ralph9() # разговор с Барди после 2-й уборки
#call ep212_dialogues1_bardie_ralph10() # мысли Моники после ухода Барди
#call ep212_dialogues1_bardie_ralph11() # Моника 3-й раз приходит убираться в гостиную
#call ep212_dialogues1_bardie_ralph12() # Моника убирается без трусиков
#call ep212_dialogues1_bardie_ralph13() # разговор с Барди после 3-й уборки
#call ep212_dialogues1_bardie_ralph14() # мысли Моники после ухода Барди

label ep212_dialogues1_bardie_ralph1:
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Sneaky_Snitch
    img 9672
    with fadelong
    bardie "Гувернантка, спустись вниз."
    bardie "Твой хозяин хочет поговорить с тобой"

    # В подвале спальня
    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 7456
    with fadelong
    w
    img 15808
    with fade
    m "Что тебе снова от меня надо?!"
    img 15809
    with diss
    bardie "Гувернантка, ты была хорошей и помогала хозяину."
    bardie "Теперь у хозяина хорошие оценки в колледже."
    m "!!!"
    img 15810
    with fade
    bardie "Еще гувернантка соблюдает правила дома и ходит без трусиков..."
    img 15811
    with diss
    mt "Мерзкая малявка!"
    mt "Я даже представить не могла что все это дойдет до такого!"
    img 15812
    with fade
    bardie "Также гувернантка помогла хозяину заставить Бетти тоже соблюдать правила дома."
    bardie "Хозяину это нравится."
    img 15823
    with diss
    bardie "Хозяин любит, когда в доме порядок и все соблюдают правила." # улыбается
    music Pyro_Flow
    img 15826
    with fade
    mt "Это мой дом! И я должна устанавливать порядки здесь!"
    mt "ТОЛЬКО Я!"
    mt "Ненавижу!!!"
    music Groove2_85
    img 15835
    with diss
    bardie "Однако, хозяин пока еще не доволен."
    img 15834
    with diss
    m "Что значит недоволен?!"
    m "Что тебе еще надо?!"
    music Sneaky_Snitch
    img 15825
    with fade
    bardie "Во-первых, хозяину не нравится все время проверять, соблюдает-ли гувернантка правила дома."
    bardie "Хозяин тратит слишком много времени на поддержание порядка."
    bardie "Хозяин должен издалека видеть, что гувернантка придерживается правил."
    img 15827
    with diss
    m "Что ты имеешь ввиду?!"
    img 15831
    with fade
    bardie "Твоя юбка."
    bardie "Хозяин заметил, что гувернантка не очень любит, когда хозяин заглядывает под нее."
    bardie "Хозяин думает о своих подопечных и заботится о них."
    bardie "Поэтому, хозяин решил что гувернантке будет лучше без этой юбки."
    img 15833
    with diss
    bardie "Так будет всегда видно, что гувернантка послушная."
    bardie "И хозяину не придется все время беспокоить ее, чтобы проверять это."
    music Power_Bots_Loop
    img 17597
    with hpunch
    m "ЧТООО?!"
    m "Ты хочешь, чтобы я ходила по дому голой?!"
    m "ЭТОГО НЕ БУДЕТ!"
    m "ДАЖЕ НЕ МЕЧТАЙ!!!"
    music Groove2_85
    img 15835
    with fade
    bardie "Хозяину не нравится, когда гувернантка поднимает на него голос!"
    bardie "Хозяин определяет правила этого дома!"
    bardie "А гувернантка должна соблюдать их!"
    img 17598
    with diss
    m "В аду я видела эту гребаную работу гувернанткой!"
    m "Ты знаешь, кто ты и кто я!!!"
    m "Как ты смеешь требовать от меня что-то подобное!"
    m "Ничтожная малявка!"
    music Sneaky_Snitch
    img 17599
    with fade
    bardie "Ты - моя игрушка!"
    bardie "И я делаю с тобой все что захочу!"
    music Power_Bots_Loop
    img 17600
    with diss
    m "НЕТ, МАЛЯВКА!!!"
    music Groove2_85
    img 17601
    with fade
    bardie "Да! Ты сама сказала мне это!"
    bardie "Там, в полицеском участке, ты сама сказала что ты моя игрушка!"
    bardie "Ты что, обманула меня?!"
    img 15830
    with diss
    m "!!!"
    img 17602
    with fade
    bardie "Если ты меня обманула, то я прямо сейчас пойду к Мистеру Маркусу!"
    bardie "И попрошу его выписать тебе штраф!"
    img 15826
    with diss
    mt "Дьявол!"
    mt "Он снова шантажирует меня!"
    mt "Как тебя угораздило влипнуть в это, Моника?"
    mt "Что какая-то мелкая малявка знает про Маркуса и командует мной в моем же доме!"
    mt "Мне хочется прихлопуть его!"
    mt "Этого мелкого недороска!"
    img 17603
    with diss
    bardie "Молчишь?!"
    bardie "Значит ты не моя игрушка?"
    # уходит
    sound man_steps
    img 7471
    with fade
    bardie "Тогда я иду к Мистеру Маркусу прямо сейчас!"
    music Master_Disorder
    img 9691
    with hpunch
    mt "Дьявол!"
    mt "Это конец!"
    img 17604
    with diss
    m "Стой! Подожди!!"
    bardie "Что тебе надо! Я не хочу разговаривать с тобой!"
    bardie "Ты обманула меня!"
    img 17605
    with fade
    m "Стой! Я... Я не обманывала тебя..."
    music Groove2_85
    img 7554
    with diss
    bardie "Да? Тогда скажи кто ты!"
    img 7555
    with fade
    mt "О БОЖЕ! Моника!"
    mt "Неужели тебе придется снова сказать это?!"
    img 9700
    with diss
    m "Я... Я твоя игрушка..."
    bardie "И?"
    m "И... И ты можешь делать со мной все что хочешь..."
    music Sneaky_Snitch
    img 9701
    with fade
    bardie "Так-то лучше, гувернантка!"
    bardie "Если ты хочешь, чтобы я тебя простил, то пообещай что не будешь забывать что ты моя игрушка!"
    music Power_Bots_Loop
    img 9702
    with diss
    mt "Я убью его! Я его точно убью..."
    music Groove2_85
    img 7533
    with fade
    m "Я... Обещаю что не буду забывать кто я..."
    bardie "???"
    m "Я... Обещаю что не буду забывать что я твоя игрушка... Хозяин..."
    img 7554
    with diss
    bardie "Так-то лучше!"
    bardie "И ты помнишь новые правила дома?"
    img 15815
    with fade
    mt "Черт! Я не хочу ходить по дому голой!"
    mt "Мне надо что-то придумать!"
    mt "Эта малявка настолько глуп, что такая умная как я должна легко обвести его вокруг пальца..."
    music Hidden_Agenda
    img 9688
    with diss
    m "Барди..."
    m "Дело в том, что в доме хозяин не только ты."
    m "Знаешь, здесь также есть Ральф, твой отец."
    m "И он явно не одобрит мой внешний вид..."
    m "И заставит снова одеться как обычно..."
    music Groove2_85
    img 9685
    with fade
    bardie "Ральф?"
    bardie "Ну да... Хм..."
    bardie "Точно!"
    bardie "Гувернантка, у меня есть поручение тебе!"
    img 9687
    with diss
    m "Какое еще поручение?!"
    mt "Что этот мелкий извращенец снова придумал?!"
    img 9686
    with fade
    bardie "Бетти надоедала мне."
    bardie "Постоянно ко мне придиралась."
    bardie "Сейчас, когда она стала послушной, мне стал мешать Ральф, мой отец."
    img 17606
    with diss
    bardie "Он контролирует мою учебу и сует свой нос в дела хозяина."
    bardie "Хозяину это не нравится. Это надо исправить."
    bardie "В этом доме все должна соблюдать правила."
    img 17607
    with fade
    m "И что ты собрался делать с этим?"
    music Sneaky_Snitch
    bardie "То же самое что и с Бетти!"
    m "В смысле?"
    img 17608
    with diss
    bardie "Ральф очень боится Бетти."
    bardie "Потому, если в моих руках будут кое-какие материалы, это поможет мне убрать его с моего пути."
    music Groove2_85
    m "Ты собрался шантажировать Бетти изменой Ральфу, а Ральфа изменой Бетти?"
    img 17609
    with fade
    m "Но откуда ты возьмешь эти материалы?"
    m "Ральф целыми днями сидит дома. Неужели он изменяет Бетти?"
    img 9697
    with diss
    bardie "По моим наблюдениям, Ральф периодически уезжает, чтобы встречаться со шлюхами."
    bardie "Он стал это делать после того, как доме появилась ты."
    music Pyro_Flow
    img 9677
    with fade
    mt "Этот мерзавец тратит на шлюх мои деньги!"
    mt "Которые должен был платить мне!"
    mt "Мерзавец! Ничтожество!"
    mt "Вся эта дурацкая семейка, которая захватила мой дом!"
    # Зло
    img 17610
    with diss
    m "Я думаю Бетти будет интересно узнать о его визитах!"
    music Groove2_85
    img 17611
    with fade
    bardie "Тише, гувернантка!"
    bardie "Бетти не должна ничего узнать!"
    bardie "Иначе я потеряю контроль над Ральфом, а гувернантку будет ждать штраф!"
    img 17612
    with diss
    m "!!!"
    m "Что-же, вперед! Иди, выводи его на чистую воду!"
    img 17613
    with fade
    bardie "Есть одна проблема..."
    m "Какая?"
    bardie "У меня нет необходимых материалов на Ральфа."
    img 17614
    with diss
    m "Такой шпион как ты, уверена, без труда достанет их!"
    img 17615
    with fade
    bardie "Все не так просто. Он мой отец."
    bardie "Поэтому он умеет заметать следы."
    music Stealth_Groover
    img 9703
    with diss
    m "Ну вот и отлично!"
    m "У тебя нет материалов, а значит нечем шантажировать Ральфа."
    m "Значит ходить голой мне запрещено."
    m "Все, ты закончил? Можешь идти!"
    music Sneaky_Snitch
    img 9705
    with fade
    bardie "К счастью, у меня есть красивая игрушка."
    bardie "Которая поможет мне добыть эти материалы!"
    img 9706
    with diss
    m "Какая игрушка?"
    bardie "Ты забыла? Ты! Ты моя игрушка!"
    music Groove2_85
    img 9702
    with fade
    m "!!!"
    img 7469
    with diss
    bardie "Ты обещала что не будешь этого забывать!"
    bardie "Быстро скажи кто ты!"
    img 7470
    with fade
    mt "!!!"
    m "Я... Я твоя игрушка..."
    m "!!!"
    m "Но если ты говоришь что не сможешь прошпионить за ним, то чего тогда ты ждешь от меня?"
    m "Я понятия не имею, куда он ходит и где встречается с кем-то!"
    img 7465
    with diss
    bardie "Мне не обязательно знать где ходит Ральф."
    bardie "Мне нужны материалы! И все!"
    img 7466
    with fade
    m "Но как ты их добудешь, если не знаешь где Ральф встречается с кем-то?"
    img 9692
    with diss
    bardie "Очень просто! Мне не надо их добывать!"
    bardie "Зачем их где-то добывать, если их можно просто сделать!"
    img 17616
    with diss
    m "Что ты имеешь ввиду?"
    music Sneaky_Snitch
    img 17617
    with fade
    bardie "Я имею ввиду мою игрушку, которая сделает эти материалы для хозяина."
    img 9683
#    with diss
    m "Ты имеешь ввиду - Меня?!"
    img 9674
    with fade
    bardie "Ну конечно!"
    bardie "Так даже лучше!"
    bardie "Хозяину не придется нигде бегать и ничего искать."
    bardie "Моя ручная гувернантка соблазнит Ральфа и сделает необходимый хозяину материал!"
    img 9676
    with diss
    m "Ты... Ты решил подложить меня под Ральфа?!"
    bardie "Конечно! Ты ведь моя игрушка!"
    bardie "Я делаю с тобой все что хочу!"
    music Power_Bots_Loop
    img 9680
#    with diss
    m "ТЫ..."
    m "ТЫ... ТЫ..."
    music Sneaky_Snitch
    bardie "Моя игрушка хочет что-то сказать мне?"
    img 9691
    with fade
    m "!!!"
    img 9686
    with diss
    bardie "Да, и я вовсе не требую от тебя заниматься с ним сексом."
    bardie "Достаточно поцелуя."
    bardie "При этом он должен трогать тебя за попу."
    img 9689
    with diss
    bardie "И ее должно быть хорошо видно."
    bardie "Я не люблю, когда другие трогают мои игрушки..."
    bardie "Но я готов потерпеть это один раз..."
    img 17618
    with fade
    m "!!!"
    bardie "Гувернантка хорошо поняла распоряжение хозяина?"
    m "!!!"
    bardie "Я не слышу..."
    img 7462
    with diss
    m "Да, гувернантка поняла хозяина вполне хорошо..."
    music Groove2_85
    img 9709
    with fade
    mt "Не могу поверить!"
    mt "Мне придется соблазнять этого отвратительного Ральфа!"
    mt "Только такая провинциальная дура как Бетти может жить с этим старым неудачником!"
    mt "И мне, Монике Бакфетт..."
    img 9691
    with diss
    mt "Самой богатой и влиятельной леди этого города..."
    mt "Приходится соблазнять это ничтожество, по приказу какого-то сопляка..."
    mt "БОЖЕ, Моника!"
    img 7522
    with diss
    mt "Как могло до этого дойти!"
    mt "..."
    mt "Кстати, о Бетти..."
    img 7468
    with fade
    m "А что насчет Бетти?"
    m "Как мне соблазнять Ральфа, если Бетти все время следит за мной?"
    m "Она и так подозревает меня что я пришла в дом, чтобы соблазнить Ральфа."
    music Sneaky_Snitch
    img 7594
    with diss
    bardie "Бетти уже стала больше доверять тебе и не так следит за тобой как раньше."
    bardie "Ты ведь заметила, что тебе [необязательно убираться в доме ежедневно]?"
    bardie "Поэтому ты легко соблазнишь Ральфа у Бетти под носом!"
    img 7600
    with diss
    bardie "Но не вздумай допустить того, чтобы она заметила тебя."
    bardie "Тогда весь план рухнет и Бетти перестанет слушаться хозяина."
    bardie "В таком случае гувернантку ждет штраф у Мистера Маркуса."
    music Groove2_85
    img 7601
    with fade
    m "!!!"
    m "Как мне соблазнять его?"
    m "Я не умею этого делать!"
    img 7592
    with diss
    bardie "Моника Бакфетт не умеет соблазнять мужчин?"
    img 7553
    with fade
    m "Я делала это когда-то давно. Один раз..."
    m "Мужчины всегда сами пытались соблазнить меня..."
    music Sneaky_Snitch
    img 7459
    with diss
    bardie "Тебе стоило бы научиться этому!"
    bardie "Это может быть полезный навык для моей игрушки!"
    bardie "Так она сможет принести больше пользы хозяину!"
    music Power_Bots_Loop
    img 9677
    with diss
    mt "Малявка!!!"
    music Sneaky_Snitch
    img 9699
    with fade
    bardie "Возможно я дам тебе шанс потренироваться на мне..."
    bardie "Но только после Ральфа!"
    bardie "Сейчас на это нет времени!"
    bardie "Это будет сделать не сложно."
    img 7554
    with diss
    bardie "Просто убирайся в гостиной, когда он сидит там."
    bardie "Нагибайся пониже, чтобы было видно что у тебя под юбкой."
    bardie "И Ральф сам к тебе пристанет."
    img 7587
    with diss
    bardie "Я видел это в кино..."
    bardie "Там это никогда не занимает много времени."
    img 7589
    with fade
    mt "Догадываюсь что это за кино..."
    # уходит
    bardie "Я жду результатов от гувернантки."
    bardie "Не затягивай с моим приказом!"
    return

label ep212_dialogues1_bardie_ralph2:
    # Моника думает
    music stop
    img black_screen
    pause 1.5
    music Groove2_85
    img 15844
    with fadelong
    mt "Дьявол!"
    mt "Этот малявка совсем обнаглел!"
    mt "Ральф..."
    img 15845
    with fade
    mt "Какого черта я должна соблазнять старого уродливого неудачника!"
    mt "..."
    music Stealth_Groover
    img 15846
    with diss
    mt "Хотя... Возможно, если я соблазню его..."
    mt "Тогда я смогу занять место Бетти в этом доме."
    mt "Отправить эту малявку домой к его родной матери."
    mt "И вернуть себе дом..."
    img 9698
    with fade
    mt "Точно, Моника!"
    mt "Как тебе это не пришло в голову сразу?!"
    mt "Ну все, держитесь!"
#    $ log1 = t_("Соблазнить Ральфа.")
#    $ log1 = t_("Барди хочет, чтобы я соблазнила Ральфа и сделала для него материалы... Но, может быть, это мой шанс вернуть назад свой дом?")
    return

label ep212_dialogues1_bardie_ralph3: # Моника приходит убираться в гостиную
    # не рендерить
    if monicaBardieRalphSeducingStage == 1:
        $ menu_corruption = [ep212_seduce_ralph1]
    if monicaBardieRalphSeducingStage == 2:
        $ menu_corruption = [ep212_seduce_ralph2]
    if monicaBardieRalphSeducingStage == 3:
        $ menu_corruption = [ep212_seduce_ralph4]
    menu:
        "Соблазнять Ральфа.":
            return True
        "Убираться как обычно.":
            return False
#    menu:
#        "Убираться на виду Ральфа в трусиках Юлии.":
#            pass
#        "Убираться на виду Ральфа в трусиках Бетти.":
#            pass
#        "Убираться на виду Ральфа без трусиков":
#            pass

label ep212_dialogues1_bardie_ralph3a: # Моника приходит убираться в гостиную в первый раз
    mt "Вот и Ральф..."
    mt "Легкая жертва для такой красивой девушки как я..."
    mt "Уверена, что он никогда не сталкивался с красотой, подобной моей..."
    mt "И даже не подозревает, как он уязвим и жалок..."
    mt "Я специально скрывала свою женственность, чтобы он не вздумал ко мне приближаться!"
    mt "Но теперь он - моя жертва!"
    mt "И я верну назад этот дом!"

    # если нет трусиков или одеты трусики Бетти
    if monicaUnder == "Nude":
        mt "Однако, не думаю что стоит делать это без трусиков."
        return False
    if monicaBettyPanties == True:
        mt "Однако, не думаю что стоит делать это в трусиках Бетти."
        mt "Для такого как он будет достаточно надеть [трусики Юлии]..."
        mt "[Они в прачечной около бассейна.]"
        mt "Сделаю это в следующую уборку."
        return False
    #
    return True


label ep212_dialogues1_bardie_ralph4: # Моника убирается в трусиках Юлии
    # не рендерить
    music stop high
    scene black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda high
    img 23765
    with fadelong
    mt "Мистер Робертс, разрешите мне убрать в этой комнате?"
    ralph "Конечно, Моника. Можешь убираться."

label ep212_dialogues1_bardie_ralph4a: # Моника убирается в трусиках Юлии
    # Ральф уперся в книгу и не замечает Монику
    if obj_name == "Chair3":
        img 23766
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23767
        with diss
        mt "Он смотрит или нет?"

    if obj_name == "Chair4":
        img 23768
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23769
        with diss
        mt "Ну же!"

    if obj_name == "Sofa":
        img 23770
        with fade
        mt "Мистер Робертс, я протру и здесь тоже!"
        $ cleaning_sound()
        img 23771
        with diss
        ralph "Да, Моника. Протирай везде..."

    if obj_name == "TableLamp1":
        img 23772
        with fade
        $ cleaning_sound()
        mt "Он что, даже не смотрит?!"
    return

label ep212_dialogues1_bardie_ralph4b:
    img black_screen
    with diss
    pause 1.5
    $ cleaning_sound()
    img 23773
    with diss
    w
    $ cleaning_sound()
    img 23774
    with fade
    w
    $ cleaning_sound()
    img 23775
    with diss
    mt "Я не понимаю..."

    $ restore_music()
    # Конец
    music Groove2_85
    sound highheels_short_walk
    img 23776
    with fade
    mt "Мистер Робертс, я закончила уборку здесь..."
    ralph "Да, Моника, конечно. Можешь продолжать уборку в других комнатах."

    img 23777
    with diss
    sound highheels_short_walk
    mt "Как же так?"
    mt "Я вертелась перед ним все время, а он даже не оторвался от своей дурацкой книги!"
    mt "Что за жалкий представитель мужской фауны?"

    return

label ep212_dialogues1_bardie_ralph5: # После уборки
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Sneaky_Snitch
    img 9672
    with fadelong
    bardie "Гувернантка, спустись вниз."
    bardie "Твой хозяин хочет поговорить с тобой"

    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Sneaky_Snitch
    img 7458
    with fade
    bardie "Ну что, ты соблазнила его?"
    bardie "Когда вы будете целоваться?"
    bardie "Я уже приготовил свой телефон, чтобы снять это!"
    music Groove2_85
    img 9700
    with diss
    m "Я... Нет, у меня пока не получилось сделать это..."
    img 9685
    with fade
    bardie "Как это?"
    bardie "Ты делала что я говорил тебе?"
    img 9675
    with diss
    m "Да, я убиралась и наклонялась перед ним..."
    img 9686
    with fade
    bardie "И что, он увидел твою киску и ничего не сделал?"
    img 17619
    with diss
    m "Он не видел ее..."
    bardie "Почему это?!"
    m "Я делала это... в трусиках Юлии..."
    img 7533
    with fade
    bardie "Ты нарушила правила дома?!"
    img 7534
    with diss
    m "Я решила что так будет проще соблазнить его..."
    music Sneaky_Snitch
    img 7536
    with fade
    bardie "Трусиками Юлии? Ха-ха!"
    bardie "Тогда уж возьми трусики Бетти..."
    img 7537
    with diss
    bardie "А лучше вообще без трусиков!"
    bardie "Чтобы не нарушать правила дома."
    music Groove2_85
    img 7586
    with fade
    mt "Я не собираюсь делать это без трусиков!"
    # уходит
    bardie "Я жду, гувернантка..."
    return

label ep212_dialogues1_bardie_ralph6: # autorun
    # не рендерить
    mt "Надоедливая малявка!"
    mt "Когда же я наконец избавлюсь от него!"
    return


label ep212_dialogues1_bardie_ralph7: # Моника приходит убираться в гостиную 2-ой раз
    # не рендерить
    mt "Вот и Ральф..."
    mt "Похоже он слепой, как крот, раз не обратил внимание на меня в прошлый раз..."
    mt "Но, в трусиках Бетти, он меня явно заметит."
    mt "У него нет никаких шансов устоять против меня..."

    if monicaBettyPanties != True:
        # если нет трусиков или одеты трусики Юлии
        mt "Мне надо будет [надеть трусики Бетти]."
        mt "Сделаю это в следующую уборку."
        return False
    #
    return True

label ep212_dialogues1_bardie_ralph8: # Моника убирается в трусиках Бетти
    # не рендерить
    music stop high
    scene black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda high
    img 23778
    with fadelong
    mt "Мистер Робертс, разрешите мне убрать в этой комнате?"
    ralph "Конечно, Моника. Можешь убираться."

label ep212_dialogues1_bardie_ralph8a:
    $ monicaBettyPantiesOverlayId = monicaBettyPantiesId - 1
    if obj_name == "Chair3":
        img 23779 #over1, over2, over3, over4
        overlay 23779 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        mt "Трусики Бетти должны сработать..."
        $ cleaning_sound()
        img 23780
        with diss
        w

    if obj_name == "Chair4":
        img 23781 #over1, over2, over3, over4
        overlay 23781 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23782
        with diss
        mt "Смотрит он или нет?"
        img 23783 #over1, over2, over3, over4
        overlay 23783 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        w

    if obj_name == "Sofa":
        $ cleaning_sound()
        img 23786 #over1, over2, over3, over4
        overlay 23786 monicaBettyPantiesOverlayId
        with fade
        m "Мистер Робертс, скажите, здесь тоже на протирать в этот раз?"
        $ cleaning_sound()
        img 23785
        with diss
        ralph "Да, Моника протирай везде и тщательно..."
        img 23784 #over1 over2 over3 over4
        overlay 23784 monicaBettyPantiesOverlayId
        with diss
        w

    if obj_name == "TableLamp1":
        img 23789 #over1, over2, over3, over4
        overlay 23789 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23787 # over1, over2, over3, over4
        overlay 23787 monicaBettyPantiesOverlayId
        with diss
        w
        $ cleaning_sound()
        img 23788
        with diss
        mt "Он что, не смотрит?!"
    return

label ep212_dialogues1_bardie_ralph8b:
    img black_screen
    with diss
    pause 1.5
    $ cleaning_sound()
    img 23790 # over1, over2, over3, over4
    overlay 23790 monicaBettyPantiesOverlayId
    with fade
    w
    $ cleaning_sound()
    img 23791
    with diss
    w
    $ cleaning_sound()
    img 23792 #over1, over2, over3, over4
    overlay 23792 monicaBettyPantiesOverlayId
    with diss
    mt "Да он совсем обнаглел?!"
    mt "Как можно не смотреть на то что перед ним?!"

    $ menu_corruption = [ep212_seduce_ralph3]
    menu:
        "Убираться перед Ральфом.":
            pass
        "Закончить уборку.":
            return False
    # подходит к Ральфу
    sound highheels_short_walk
    img 23793
    with fade
    m "Мистер Робертс, разрешите я здесь тоже протру, я вижу пыль..."
    ralph "Да, Моника, конечно, можешь протирать..."

    $ cleaning_sound()
    img 23794
    with diss
    w
    $ cleaning_sound()
    img 23795 #over1, over2, over3, over4
    overlay 23795 monicaBettyPantiesOverlayId
    with fade
    w
    $ cleaning_sound()
    img 23796 #iover1, over2, over3, over4
    overlay 23796 monicaBettyPantiesOverlayId
    with diss
    mt "Он что, снова пялится в свою книгу, а не на меня?!"
    $ restore_music()
    music Groove2_85
    img 23797
    with diss
    mt "Да как он смеет?!"
    mt "Как такое вообще возможно?!"
    mt "Перед ним самая красивая девушка этого города!"
    mt "Он что, импотент?!"

label ep212_dialogues1_bardie_ralph8c:
    sound highheels_short_walk
    music Groove2_85
    img 23776
    with fade
    mt "Мистер Робертс, я закончила уборку здесь..."
    ralph "Да, Моника, конечно. Можешь продолжать уборку в других комнатах."
    return True


label ep212_dialogues1_bardie_ralph9: # После второй уборки
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Sneaky_Snitch
    img 9672
    with fadelong
    bardie "Гувернантка, спустись вниз."
    bardie "Твой хозяин хочет поговорить с тобой"

    # в подвале
    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 15809
    with fadelong
    w
    img 15813
    with fade
    bardie "Ну что, гувернантка, у тебя получилось?"
    # Моника зло и обиженно
    img 15812
    with diss
    m "Нет! Он импотент, он даже не смотрит на меня!"
    img 15811
    with diss
    mt "Как такое вообще возможно?! Я не понимаю!!!"
    img 15812
    with fade
    bardie "Ты показала ему свою киску?"
    img 15830
#    with diss
    m "Да, я показала ему!"
    m "Видимо у него нет члена, раз он никак не реагирует на меня!"
    m "Это жалкое бесполое существо, не имеющее вкуса!"
    img 15835
    with fade
    bardie "Странно, у них с Бетти регулярный секс."
    bardie "Я знаю это, я подглядывал за ними."
    bardie "Ральф все время просит это у Бетти, а она дает ему только когда он это заслужит."
    img 17620
    with diss
    bardie "Ты уверена что показала ему свою киску?"
    img 15834
#    with fade
    m "Да!"
    img 17621
    with diss
    bardie "Покажи мне ее..."
    img 17622
    with fade
    m "Что показать?"
    bardie "То что ты показывала ему..."
    m "Это вовсе необязательно!"
    img 17623
    with diss
    bardie "Это обязательно!"
    bardie "Покажи мне, покажи как ты соблюдаешь правила дома!"
    # Обиженно
    img 17624
    with diss
    m "!!!"
    bardie "Я жду!"
    m "!!!"
    # показывает (все варианты трусиков Бетти)
    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_fabric1
    pause 1.0
    music Loved_Up
#    img 15819
#    with fadelong
#    w
#    img 15820
#    with fade
    $ monicaBettyPantiesOverlayId = monicaBettyPantiesId - 1
    img 17625
    overlay 17625 monicaBettyPantiesOverlayId
    with fadelong
    w
    # возвращает юбку как было
    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_fabric1
    pause 1.0
    music Sneaky_Snitch
    img 15835
    with fadelong
    bardie "Ты должна была идти без трусиков и показать Ральфу свою киску!"
    bardie "Это бы сработало! Я видел это в кино!"
    music Groove2_85
    img 15830
    with hpunch
    m "Нет! Я не буду показывать свою голую попу какому-то старикашке!"

    music Power_Bots_Loop
    img 10287
    with fadelong
    bardie "Ты плохая гувернантка!"
    bardie "Ты нарушаешь правила и будешь наказана!"

    img 10288
    with diss
    bardie "Не испытывай моего терпения и быстро ложись для получения наказания!"

    music Groove2_85
    img 10289
    with fade
    w
    img 10290
    with fade
    w
    img 10291
    with fade
    w
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #governess
            img 10292
            with diss
            w
            img 10293
            with diss
            w
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10295
            with diss
            w
            img 10294
            with diss
            w
            img 10305
            with diss
            w
    #
        if monicaBettyPantiesId == 2:
            img 10296
            with diss
            w
            img 10297
            with diss
            w
            img 10306
            with diss
            w
    #
        if monicaBettyPantiesId == 3:
            img 10299
            with diss
            w
            img 10298
            with diss
            w
            img 10307
            with diss
            w
    #
        if monicaBettyPantiesId == 4:
            img 10300
            with diss
            w
            img 10301
            with diss
            w
            img 10308
            with diss
            w
    #
        if monicaBettyPantiesId == 5:
            img 10303
            with diss
            w
            img 10302
            with diss
            w
            img 10304
            with diss
            w

    #
    img 10309
    with fade
    w
    img 10310
    with fade
    w
    img 10311
    with fade
    w
    img 10312
    with fade
    w
    img 10313
    with fade
    w
    img 10314
    with fade
    w
    img 10315
    with fade
    w
    img 10316
    with fade
    w
    img 10317
    with fade
    w
    img 10318
    with fade
    w
    img 10319
    with fade
    w
    # не рендерить (видео наказания)

label ep212_dialogues1_bardie_ralph9_loop1:
    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_1 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_1.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_1
    bardie "Получай!"
    wclean
    stop music

    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_2 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_2.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_2
    bardie "Получай!"
    bardie "Нерадивая гувернантка!"
    bardie "Я научу тебя соблюдать правила дома!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_3 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_3.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_3
    bardie "Плохая гувернантка! Плохая!"
    wclean
#    stop music
#    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
#    scene black
#    image videov_Basement_Bardie_Monica_Spanking_1_4 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_4.mkv", fps=30)
#    show videov_Basement_Bardie_Monica_Spanking_1_4
#    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_5 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_5.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_5
    bardie "Плохая гувернантка нарушает правила дома!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_6 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_6.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_6
    bardie "Ходит по дому в трусиках!"
    bardie "Получай!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_7 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_7.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_7
    bardie "Будет гувернантка слушаться хозяина?"
    bardie "Будет гувернантка соблазнять моего отца голой попой?"
    bardie "Покажет гувернантка Ральфу свою киску?"
    wclean
    stop music

    music Power_Bots_Loop
    menu:
        "Отпусти меня немедленно, малявка!":
            img 10320
            with fade
            m "Отпусти меня немедленно, малявка!"
            jump ep212_dialogues1_bardie_ralph9_loop1
        "Я поняла! Я буду слушаться хозяина!":
            pass

    music Groove2_85
    img 10321
    with fade
    m "Да, я покажу Ральфу свою киску!"
    m "Я буду хорошей гувернанткой!"
    m "Пожалуйста, хватит!"


    # рендерить (взять арты после наказания, где Моника держится за красную попу)
    music Groove2_85
    img 17630
    with fade
    bardie "Мне надоело ждать!"
    bardie "В следющую же уборку ты пойдешь к Ральфу и покажешь ему все что у тебя есть!"
    bardie "Ты поняла своего хозяина?!"
    img 17631
    with diss
    m "Да, я поняла..."
    bardie "Ты дашь ему хорошенько рассмотреть тебя!"
    img 17632
    with diss
    bardie "Ты должна его соблазнить!"
    bardie "Хозяину нужен этот материал!"
    # уходит
    img 10325
    with fade
    sound man_steps
    bardie "Пока можешь быть свободна, гувернантка."
    bardie "Но помни что твой хозяин ждет результатов!"
    return

label ep212_dialogues1_bardie_ralph10: #autorun
    # не рендерить
    music stop
    music Stealth_Groover
    mt "Это отвратительно!"
    mt "Этот малявка снова отшлепал меня!"
    mt "..."
    mt "Похоже, мне придется идти к Ральфу без трусиков."
    mt "По другому не получится."
    mt "Но мне придется пойти на такую жертву, чтобы избавиться от Барди и вернуть свой дом!"
    return


label ep212_dialogues1_bardie_ralph11: # Моника приходит убираться в гостиную 3-ий раз
    # не рендерить
    music Groove2_85
    sound highheels_short_walk
    img 23799
    with fadelong
    mt "Вот и Ральф..."
    mt "Этот гребаный импотент."
    img 23798
    with fade
    mt "Мне придется пойти на крайнюю меру, чтобы соблазнить его..."
    mt "Но это того стоит!"
    mt "Вот-вот я верну себе этот дом и избавлюсь от надоедливой малявки!"
    img 23800
    with diss
    mt "Похоже он слепой, как крот, раз не обратил внимание на меня в прошлый раз..."
    mt "Но, без трусиков, он меня явно заметит."
    mt "У него нет никаких шансов устоять против моих женственных форм..."

    # если одеты любые трусики
    if monicaUnder != "Nude":
        mt "Мне надо будет [придти без трусиков]."
        mt "Сделаю это в следующую уборку."
        return False
    #
    return True

label ep212_dialogues1_bardie_ralph12: # Моника убирается без трусиков
    # не рендерить
    music stop
    scene black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda high
    img 23801
    with fadelong
    mt "Мистер Робертс, разрешите мне убрать в этой комнате?"
    ralph "Конечно, Моника. Можешь убираться."
    return

label ep212_dialogues1_bardie_ralph12a:
    music Loved_Up high
    if obj_name == "Chair3":
        $ imgArr = [23802, 23803, 23804]

    if obj_name == "Chair4":
        $ imgArr = [23805, 23806, 23807]

    if obj_name == "Sofa":
        $ imgArr = [23808, 23809, 23810]

    if obj_name == "TableLamp1":
        $ imgArr = [23811, 23812, 23813]

    if monicaBardieRalphSeducingCleaningItemsCount == 4:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        mt "Ну что, Моника..."
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Ты задействовала самое сильное оружие, которое у тебя есть..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        w

    if monicaBardieRalphSeducingCleaningItemsCount == 3:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        w
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Ни один мужчина в мире не устоит перед таким..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        w
    if monicaBardieRalphSeducingCleaningItemsCount == 2:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        mt "Черт! Не могу поверить что я делаю это..."
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Соблазняю свой голой попой какого-то старикашку..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        mt "В своем совственном доме!"
        mt "Ужас!"
    if monicaBardieRalphSeducingCleaningItemsCount == 1:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        w
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Но мне надо сделать это!"
        mt "Я в шаге от того чтобы вернуть мой дом назад..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        w
    return

label ep212_dialogues1_bardie_ralph12b:
    # autorun
    mt "Мне надо привлечь его внимание..."
    return False

label ep212_dialogues1_bardie_ralph12c:
    music stop high
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda high
    img 23814
    with fade
    m "Мистер Робертс, скажите, здесь тоже протирать?"
    ralph "Да, Моника, протирай везде..."
    img 23815
    with diss
    w
    img 23816
    with fade
    w
    $ restore_music()
    music Groove2_85
    img 23817
    with diss
    mt "Дьявол! Он даже не смотрит!"
    mt "Не смотрит на то, что ему показывает самая чуть-ли ни самая красивая девушка в этом мире!"
    mt "Сама Моника Бакфетт соблазняет его!"
    mt "А он не смотрит! Урод!"
    $ menu_corruption = [ep212_seduce_ralph5]
    menu:
        "Убираться перед Ральфом.":
            pass
        "Закончить уборку.":
            return False
    # подходит к Ральфу
    music Hidden_Agenda
    sound highheels_short_walk
    img 23818
    with fade
    m "Мистер Робертс, разрешите я здесь тоже протру, я вижу пыль..."
    ralph "Да, Моника, конечно, можешь протирать..."
    mt "Мне надо во что бы то ни стало заставить его посмотреть на меня!"

    img 23819
    with diss
    m "Спасибо, Мистер Робертс!"

    music Loved_Up
    img 23820
    with fade
    m "Скажите, здесь тоже протирать?"
    ralph "Да, Моника, протирай..."

    img 23821
    with diss
    m "А здесь?"
    img 23822
    with diss
    ralph "Да..."

    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 23823
    with fade
    m "И здесь тоже протирать?"
    img 23824
    with diss
    ralph "Да, Моника, протирай везде..."

    img 23825
    with fade
    w

    # Задевает книгу, она падает
    sound Jump2
    img 23826
    with diss
    w
    sound Jump1
    img 23827 #diss
    with diss
    w
    sound down10
    img 23828
    with diss
    # звук падения
    w
    m "Ой, Мистер Робертс, простите! Я случайно..."
    # поднимает книгу, показывая попу

    sound swish
    img 23829
    with fade
    # звук кладущегося дустера (которым протирает)
    w
    img 23830
    with diss
    m "Позвольте, я подниму Вашу книгу!"
    img 23831
    with diss
    mt "Он у меня почти в руках!"

    img 23832
    with fade
    w
    music stop
    img 23833
    with diss
    sound snd_boot1
    # звук наступает на ногу
    w
    sound scream_steve
    img 23834
    with vpunch
    # звук ральф кричит ай!
    w

    # дает ее
    music Loved_Up
#    music Groove2_85
    img 23835
    with fade
    m "Вот, Мистер Робертс, Ваша книга..."

    # Ральф встает
    # рендерить
    img 23836
    with diss
    ralph "Моника, мне надо с тобой поговорить..."
    music Stealth_Groover
    img 23837
    with diss
    mt "Все! Я сделала это!"
    mt "Он, наконец-то, обратил внимание на меня!"
    mt "Теперь ему никуда не деться, он мой!"
    mt "У него нет никаких шансов соскочить с моего крючка!"

    music Groove2_85
    img 23838
    with fade
    ralph "Моника, ты меня слышишь?"
    # улыбается заискивающе
    m "А? Да, Мистер Робертс, я Вас слушаю..."

    # строго
    img 23839
    with diss
    ralph "Моника, я давно заметил, что ты пытаешься обратить мое внимание на себя."
    ralph "С самого начала, как только ты начала работу здесь, ты проявляла интерес ко мне."
    img 23840
    with fade
    mt "Что? С самого начала?"
    mt "Это неправда!"

    img 23841
    with diss
    ralph "Бетти предупреждала меня об этом."
    ralph "Да и это, в общем, неудивительно."
    ralph "Такая молодая девушка как ты, без хорошего дохода."
    ralph "Конечно такой роскошный дом произведет на тебя впечатление."
    ralph "И ты попытаешься воспользоваться своими внешними данными, чтобы остаться здесь в качестве хозяйки."

    img 23842
    with fade
    mt "Что он имеет ввиду?"
    mt "Это он так пытается сказать что от меня без ума?!"

    img 23843
    with diss
    ralph "Я заверил Бетти что ты хорошая девушка и не станешь вести себя как все..."
    ralph "Однако, я ошибся..."
    ralph "И из всех способов, соблазнить хозяина дома, ты выбрала самый вульгарный..."
    ralph "Сначала ты пыталась соблазнить меня видом моих трусиков."
    mt "!!!"
    ralph "Затем решила использовать трусики Бетти..."
    music stop
    sound plastinka1b
    img 23845
    with hpunch
    mt "ЧТО?! ОН УЗНАЛ ИХ?!"

    music Groove2_85
    img 23844
    with fade
    ralph "У тебя на лице удивление?"
    ralph "Да, я узнал их."
    ralph "Я очень люблю все то, что носит Бетти."
    ralph "И для меня удивительно, как гувернантка позволила себе одеть белье супруги своего работодателя."
    img 23846
    with diss
    m "!!!"
    img 23847
    with fade
    ralph "Конечно ты сделала это без спроса, но сделала всего один раз."
    ralph "Посчитаем это досадным недоразумением..."
    ralph "Я могу понять то, что тобой двжут корыстные мотивы."
    ralph "И ради них ты готова пойти на то, чтобы демонстрировать себя без всякого стыда..."
    ralph "Я знаю что моральные устои современных девушек, твоего возраста, далеки от тех идеалов к которым я привык..."
    ralph "Однако, я бы не хотел терпеть это в своем доме..."
    img 23848
    with diss
    m "!!!"
    img 23849
    with fade
    ralph "Давай ты мне пообещаешь, что больше не будешь так делать."
    ralph "И мы вместе забудем о том что здесь только что было..."
    ralph "Ты согласна со мной?"
    mt "!!!"
    # стоит потупившись
    music Hidden_Agenda
    img 23850
    with diss
    m "Да, Мистер Робертс... Я согласна..."
    ralph "Я не скажу об этом Бетти..."
    ralph "Я боюсь ее реакции на подобные вещи..."
    # сжимается (есть поза в артах рука на голове)
    img 23851
    with fade
    ralph "Ты ведь знаешь, что Бетти такая строгая..."
    ralph "Скорее всего, учитывая какого она мнения о тебе, тебе придется быть уволеной отсюда..."
    music Pyro_Flow
    img 23852
    with diss
    mt "Я никогда не чувствовала себя так глупо!!!"
    mt "Моника, какой кошмар!"
    mt "Тебя отчитывают за аморальное поведение в своем же собственном доме!"
    mt "Как до такого могло дойти?!"
    mt "Я не могу поверить что нахожусь здесь!"
    mt "Мне хочется провалиться сквозь землю..."
    music Groove2_85
    img 23853
    with fade
    m "Да, Мистер Робертс... Я поняла..."
    m "Простите, Мистер Робертс... Такого больше не повториться..."
    img 23854
    with diss
    ralph "Хорошо, Моника. Можешь быть свободна."
    sound highheels_short_walk
    img 23855
    with fade
    m "Спасибо, Мистер Робертс..."
    return True



label ep212_dialogues1_bardie_ralph13: # После третьей уборки
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Sneaky_Snitch
    img 9672
    with fadelong
    bardie "Гувернантка, спустись вниз."
    bardie "Твой хозяин хочет поговорить с тобой"

    # в подвале
    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 7536
    with fadelong
    bardie "Ну что, гувернантка, у тебя получилось?"
    # Моника зло и обиженно
    img 7523
    with fade
    m "Нет!"
    m "Я сделала все как ты сказал!"
    m "Ральф отчитал меня и пригрозил сказать об этом Бетти!"
    m "Я не была в более глупой ситуации за всю мою жизнь!"
    m "Это все из-за тебя, Барди!"
    music Sneaky_Snitch
    img 7525
    with diss
    bardie "Странно, а в кино у гувернантки все получилось..."
    bardie "Она наклонилась без трусиков и после этого начался секс..."
    music Groove2_85
    img 7531
    with fade
    m "Я представляю что это было за кино, Барди!"
    m "В реальной жизни это происходит не так, как в кино, которое ты все время смотришь!"
    img 7533
    with diss
    bardie "Гувернантка, хозяину надо подумать..."
    bardie "Я придумаю для тебя способ залезть Ралью в штаны..."
    img 7522
    with diss
    m "!!!"
    # уходит
    sound man_steps
    img 7586
    with fade
    bardie "Я скоро сообщу тебе что надо делать..."
    bardie "Пока можешь быть свободна!"
#    help "Продолжение квеста в следующем обновлении."
    return

label ep212_dialogues1_bardie_ralph14: # autorun
    # не рендерить
    mt "Не могу поверить что у меня не сработало!"
    mt "Меня отчитали как какую-то шлюху!"
    mt "Я не шлюха, которая пыталась переспать с хозяином, чтобы занять место жены!"
    mt "Я... Я лишь хотела восстановить справедливость!"
    mt "Если бы этот никчемный старикашка только знал кого он отчитывает!"
    mt "Мерзавец!"
    mt "Бесполезный, никчемный неудачник!"
    return
