default bettyEricBardiesroom = False  # Бетти согласилась задрать юбку при Эрике


# прачечная (когда Моника вышла из дома)
label ep210_dialogues3_bardie_erik_betty_1:
    # темный экран "тем временем"
    # открывается дверь прачечной, в дверном проеме стоит Бетти
    # в прачечной стоит Эрик, спиной к двери, штаны приспущены и дрочит
    # шкафчики он закрывает своей тушкой, их не видно (показываем его сначала сзади, а потом его спереди, как будто из шкафчика, и Бетти стоит сзади)
    # Бетти возмущенно
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_52
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    img 16079
    with fadelong
    sound drkanje5
    w
    img 16080
    with fade
    sound drkanje5
    w
#    music Power_Bots_Loop
    img 16081
    with diss
    sound drkanje5
    betty "Это что еще такое?!"
    betty "Ты что тут делаешь?!"
    betty "!!!"
    # Эрик подпрыгивает от неожиданности, поворачивается к ней, пытается прикрыться
    # можно брать ассет, где он кончает в кулачок в других артах, но изменить что он закрывает рукой свой стручок )
    sound plastinka1b
    music stop
    img 16082
    with hpunch
    eric "Я... Ну... Эээ..."
    music Power_Bots_Loop
    img 16083
    with fade
    betty "А ну-ка иди сюда, паршивец!!!"
    betty "Я сейчас устрою тебе и этому малявке!!!"
    music Groove2_85
    img 16084
    with diss
    sound Jump2
    betty "Устроили непонятно что в моем доме!!!"
    betty "Я это вам просто так не оставлю!"
    # Бетти хватает его за ухо и тащит из прачечной
    img 16085
    with fade
    eric "А-а-а-а-а!"
    # он не успевает натянуть штаны и пытается удержать их рукой
    music stop
    img black_screen
    with diss
    pause 1.5
    sound highheels_run2
    pause 1.5
    return

label ep210_dialogues3_bardie_erik_betty_1a:
    # Моника комментирует
    mt "Мне показалось или здесь был какой-то звук?"
    mt "Кажется, кричала Бетти. Интересно на кого?"
    return

# комната Барди
label ep210_dialogues3_bardie_erik_betty_2:
    # Бетти затаскивает Эрика, который пытается одной рукой уержать свои расстегнутые штаны, в комнату Барди
    # Барди стоит у окна спиной, но поворчивается когда они заходят
    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16012
    with fadelong
    bardie "Эй, что случилось?"
    img 16013
    with fade
    betty "Ты у него спрашиваешь что случилось?! Я скажу тебе!"
    betty "Я нашла твоего друга в прачечной!"
    img 16078
    with diss
    w
    music Power_Bots_Loop
    img 16014
    with fade
    betty "Он залез в шкафчик с моим бельем!!!"
    betty "Он дергал свой... Свой отросток! И делал это на МОИ трусики!!!"
    # Бетти злится, орет и продолжает держать Эрика за ухо
    music Groove2_85
    img 16015
    with diss
    betty "Я не хочу больше видеть этого сопляка-извращенца в моем доме!"
    betty "Я порядочная женщина и живу в этом доме со своим мужем!"
    img 16016
    with diss
    betty "И я не потерплю, что какая-то малявка приходит сюда..."
    betty "И делает непотребства на белье супруги Ральфа!"
    # Барди смотрит на Эрика удивленно
    img 16017
    with fade
    bardie "Что он делал?"
    bardie "Дрочил что-ли? На ее трусы?"
    img 16018
    with diss
    eric "Нууу..."
    # Барди смеется и говорит Бетти
    img 16019
    with fade
    bardie "Тебе-то какое дело? Они тебе не нужны, все равно ты их не носишь!"
    bardie "Аха-ха!"
    # Бетти бомбит
    music Power_Bots_Loop
    img 16020
    with diss
    betty "Я не вижу здесь ничего смешного!!!"
    betty "!!!"
    betty "Еще раз такое повторится, я расскажу маме этого сопляка, что он тут творит!"
    # Барди опять смеется
    music Groove2_85
    img 16021
    with fade
    bardie "Расскажешь его маме?! Аха-ха!!!"
    img 16022
    with diss
    betty "!!!"
    betty "Ничего смешного я тут не вижу!"
    img 16023
    with fade
    bardie "..." # видно, что что-то задумывает
    music Marty_Gots_a_Plan
    bardie "Вообще-то..."
    # потом Барди делает вид, что недоволен поведением одноклассника
    img 16024
    with diss
    bardie "Эй, чувак! Это же белье моей приемной мамы..."
    bardie "А я ее очень люблю и очень уважаю!"
    # Бетти отпускает Эрика и удивленно смотрит на Барди
    sound Jump1
    img 16025
    with fade
    betty "???"
    bardie "Все, Эрик! Ты больше не можешь приходить ко мне домой!"
    # Эрик взволнованно
    music Groove2_85
    img 16026
    with diss
    eric "Нет, не надо! Барди, я могу..."
    eric "Домашку еще поделать тебе могу! Как в прошлый раз, помнишь?"
    eric "Еще напишу для тебя сочинение по литературе! Ты за это получишь высший балл по колледжу!"
    # Барди делает вид, что сомневается
    music Marty_Gots_a_Plan
    img 16027
    with fade
    bardie "Домашку? Ну, помню..."
    img 16028
    with diss
    eric "..."
    eric "Только я хочу, как и в прошлый раз... Посмотреть... Ну ты понял..."
    img 16029
    with fade
    bardie "..."
    bardie "Два месяца домашки!"
    bardie "И годовое тестирование по математике!!!"
    img 16030
    with diss
    eric "Месяц домашки, если просто посмотрю!"
    img 16031
    with diss
    bardie "Месяц домашки и годовое тестирование по математике!"
    # Бетти смотрит на них с подозрением
    music Groove2_85
    img 16032
    with fade
    betty "На что ты собрался смотреть, сопляк?"
#    music Sneaky_Snitch
    img 16033
    with diss
    bardie "На тебя..."
    bardie "Ты сейчас покажешь, как ты соблюдаешь правила этого дома. А мы с Эриком посмотрим."
    # Бетти опять бомбит
    music Power_Bots_Loop
    img 16034
    with hpunch
    betty "ЧТОООО?!"
    betty "Да ты охренел!!!"
    betty "Я порядочная женщина и ни за что не стану..."
    # Барди перебивает
    music Groove2_85
    img 16035
    with fade
    bardie "Да-да-да... Ты 'порядочная женщина' и что там еще?"
    bardie "А, ты еще и 'верная жена'..."
    bardie "По крайне мере, мой отец так думает. Пока что..."
    # Бетти стоит руки в боки и смотрит на Барди зло
    img 16036
    with diss
    betty "Я!"
    betty "Не буду!"
    betty "Этого делать!"
    # Барди с мерзкой улыбочкой берет в руки телефон и смотрит вопросительно на нее
    img 16037
    with fade
    bardie "Ты уверена?"
    music Power_Bots_Loop
    img 16038
    with diss
    betty "Ненавижу!!!"
    betty "Мерзкая малявка!!!"
    music Groove2_85
    img 16039
    with diss
    menu:
        "Сделать, как требует Барди.":
            $ bettyEricBardiesroom = True # Бетти согласилась задрать юбку при Эрике
            pass
        "Послать малявку и уйти.":
            img 16040
            with fade
            betty_t "Этот малявка думает, что может вытворять любую глупость, которая взбредет ему голову..."
            betty_t "Ну уж нет! И ничего он мне за это не сделает!"
            music Power_Bots_Loop
            img 16041
            with diss
            betty "Да пошел ты к черту со своими правилами!"
            betty "Я не буду этого делать!"
            betty "!!!"
            music stop
            img black_screen
            with diss
            sound highheels_short_walk
            pause 2.0
            # уходит (поставить флаг, показывала или нет)
            return False
    # Бетти злобно смотрит на Барди
    img 16042
    with fade
    bardie "..." # Прищурившись, типа попробуй не послушайся
    img 16022
    with diss
    betty "Ладно..."
    betty "Я..."
    betty "Я сделаю это..."
    betty "Только быстро!"
    betty "Подниму платье и сразу опущу!"
    img 16043
    with diss
    betty "На этом все! Только на секунду, не больше!" # строго
    betty "!!!"
    # Барди с улыбочкой
    img 16044
    with fade
    bardie "Боюсь, мне придется наказать тебя."
    bardie "Ты споришь с хозяином дома и не хочешь слушаться его приказов."
    # Бетти смотрит на него зло
    img 16045
    with diss
    betty "!!!"
    bardie "Ну, я жду! Быстро в угол и снимай платье!"
    music Power_Bots_Loop
    img 16046
    with fade
    betty "Да как ты смеешь?! При своем друге!!!"
    betty "Я не буду ничего делать при нем!"
    music Groove2_85
    img 16047
    with diss
    sound keyboard
    bardie "Будешь..."
    # Барди нажимает что-то в телефоне
    # Бетти пугается, хватает его за руку
    sound Jump2
    img 16048
    with diss
    betty "Хорошо! Я сделаю, что нужно...."
    betty "Только не прикасаться ко мне!"
    # поворачивается к Эрику
    music Power_Bots_Loop
    img 16049
    with diss
    betty "Ты понял?!"
    # Эрик молча смотрит на нее как маньяк и кивает, что понял
    music Sneaky_Snitch
    img 16050
    with fade
    eric "Ага..."
    # кадр меняется. Бетти стоит в углу. в одном шарфике. зло смотрит на малявок
    # Эрик смотрит на нее и говорит Барди
    music stop
    img black_screen
    with diss
    pause 2.0
    sound snd_fabric1
    music Loved_Up
    img 16051
    with fade
    w
    img 16052
    with diss
    eric "Чувак, я согласен... Два месяца домашки и годовое тестирование."
    # Барди радостно
    music Sneaky_Snitch
    img 16053
    with fade
    bardie "Серьезно?! Точно?!"
    img 16054
    with diss
    eric "Ага..."
    img 16055
    with diss
    bardie "По рукам!"
    # Барди обращается к Бетти
    music Groove2_85
    img 16056
    with fade
    bardie "Сядь на кровать и раздвинь ноги шире!"
    # Бетти возмущенно
    img 16057
    with diss
    betty "Нет!"
    betty "!!!"
    img 16058
    with fade
    sound keyboard
    bardie "Ты снова не хочешь исполнять приказов хозяина дома?"
    # Барди снова показывает ей свой телефон и нажимает на экран
    bardie "Или мне это показалось, м?"
    # Бетти зло смотрит на него
    music Power_Bots_Loop
    img 16059
    with diss
    betty_t "Ненавижу!"
    betty_t "!!!"
    # кадр меняется. Бетти сидит на кровати, откинувшись назад. широко раздвинув ноги
    # Эрик рассматривает ее в упор, потом мнется, смотрит на Барди, потом на Бетти
    # потом резко подается вперед и присасывается к ее киске (как в сцене с Моникой)
    # Бетти
    music stop
    img black_screen
    with diss
    pause 2.0
    sound snd_fabric1
    music Loved_Up
    img 16060
    with fadelong
    w
    img 16061
    with fade
    w
    img 16062
    with diss
    w
    music Turbo_Tornado
    img 22057
    with diss
    w
    sound Jump2
    ###zvuk licking
    img 16063
    with hpunch
    betty "ААААА!!!"
    betty "Что ты делаешь?! Не смей!!!"
    img 16064
    with diss
    betty "Мелкий извращенец!"
    betty "БАРДИ!!!"
    betty "!!!"
    img 16065
    with diss
    w
    # Барди смотрит на это и офигевает
#    music Groove2_85
    img 16066
    with fade
    bardie "Эй! Ты чего творишь?!"
    bardie "Это же моя приемная мать!!!"
    # Эрик продолжает еще сильнее
    img 16067
    with diss
    bardie "Эй! Чувак! Ты меня слышишь?!"
    # Эрик отстраняется от ее киски, хватается за свой член и убегает из комнаты
    # Бетти возмущается
    sound plastinka1b
    music stop
    img 16068
    with diss
    w
    music Turbo_Tornado
    img 16069
    with fade
    sound snd_runaway
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    sound snd_fabric1
    music Power_Bots_Loop
    img 16070
    with hpunch
    betty "Безобразие!"
    betty "!!!"
    betty "Как ты мог такое позволить?!"
    img 16071
    with fade
    betty "Я твоя приемная мать! А ты заставляешь меня раздеваться перед этим... Этим сопляком-извращенцем!!!"
    betty "И ради чего?! Ради какой-то домашки!!!"
    betty "!!!"
    # Барди смотрит на нее
    music Groove2_85
    img 16072
    with diss
    bardie_t "Черт! Этот придурок Эрик совсем уже головой поехал."
    bardie_t "Ладно к моей гувернантке своим языком полез между ног..."
    bardie_t "Но эта дура Бетти - моя приемная мать..."
    bardie_t "Как-то стремно получилось..."
    music Power_Bots_Loop
    img 16073
    with fade
    betty "Я порядочная женщина, я не потерплю такого отношения к себе!"
    betty "!!!"
    # Барди отмахивается от Бетти
    music Groove2_85
    img 16074
    with diss
    bardie "Бетти, я не рассчитывал, что так будет и..." # Барди чешет репу
    img 16075
    with fade
    betty "Это тебе так не сойдет с рук!"
    img 16076
    with diss
    bardie "Ладно..."
    bardie "Давай это... Короче, просто забудем об этом."
#    music Power_Bots_Loop
    img 16077
    with fade
    betty "Мерзкая малявка!" # Бетти убегает
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    return


#################### в v0.11 #########################
# для разговора с Фредом Мелани придет во двор дома Моники
# ее там увидят все обитатели дома, включая Барди
# проработать, как Мелани выйдет на Фреда (игра будет за Мелани)
# Мелани выходит на Фреда, чтобы выяснить что-то про Викторию
# он взамен просит что-то, но Мелани ему отказывает
# тогда он говорит, давай тогда Миссис Бакфетт это сделает
#
# Фред должен принести компромат
# на встречу приходит он, а за ним приходит Виктория
# он говорит, что Виктория пообещала ему секс с Мелани, если он встанет на ее сторону
# поэтому он
