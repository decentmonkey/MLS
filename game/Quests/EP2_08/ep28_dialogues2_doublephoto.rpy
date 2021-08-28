# Дом. Комната Барди. Разговор Барди и Бетти.
default monicaMadeDoublePhotoBetty = False
label dialogue_doublephoto_1:
    # Барди с телефоном в руках сидит на своей кровати, Бетти стоит в комнате Барди и недовольно кричит
    music Power_Bots_Loop
    img 15113
    with hpunch
    betty "Гувернантка!!!"
    # спустя несколько минут появляется Моникаg
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Groove2_85
    img 14579
    with fade
    mt "Она опять орет на весь дом..."
    mt "Что этой деревенщине снова от меня нужно?"
    img 14582
    with diss
    m "Да, миссис Робертс..."
    # Бетти и Моника стоят перед Барди, он сидит на кровати
    img 15115
    with fade
    betty "Гувернантка, я..."
    img 15116
    with diss
    betty "..."
    img 15117
    with fade
    bardie "Мне нужно проверить, насколько хорошо ты соблюдаешь правила этого дома и..."
    bardie "...сделать фото!"
    img 14589
    with diss
    mt "Он опять хочет фото?! Когда он уже отстанет от меня?!"
    img 15118
    with fade
    bardie "Давай, без лишних разговоров. Поднимай юбку!"
    # Моника зло смотрит на него
    music Power_Bots_Loop
    img 14592
    with diss
    m "Я не собираюсь фотографироваться с задранной юбкой!"
    m "Достаточно того, что ты при каждом удобном случае заглядываешь мне под юбку!"
    img 15119
    with diss
    mt "Мелкий озабоченный извращенец!"
    music Groove2_85
    img 15120
    with fade
    bardie "Гувернантка слишком много разговаривает!"
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    img 14592
    with diss
    m "..."
    # Барди с угрозой
    img 15121
    with fade
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    img 14594
    with diss
    mt "!!!"
    mt "Ненавижу эту малявку! И эту чокнутую деревенщину Бетти!"
    mt "Когда этот дом снова станет моим, я возьму ее к себе гувернанткой. Будет работать у меня за еду."
    mt "!!!"
    # Моника смотрит зло, Бетти все это время стоит с каменным лицом
    img 14588
    with fade
    m "Зачем тебе нужна эта фотография?"
    img 15122
    with diss
    bardie "Гувернантку это не касается! Поднимай юбку!"
    # Барди поднимает руку с телефоном, чтобы сделать фото
    mt "..."
    if monicaUnder != "Nude":
        img 14594
        with diss
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        sound highheels_run2
        img 14595
        with fade
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return False
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            sound highheels_run2
            img 14595
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return False
    # Моника, срипя зубами соглашается, поднимает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14598
    with fadelong
    w
    img 15123
    with diss
    w
    music Groove2_85
    img 15124
    with fade
    bardie "Хорошая гувернантка."
    # Барди фото не делает и смотрит на Бетти
    img 15125
    with diss
    bardie "Бетти?.."
    img 15126
    betty "!!!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15127
    with fadelong
    w
    img 15128
    with diss
    w
    img 15129
    with diss
    betty "Давай, быстрее!"
    betty "Только одно фото!"
    w
    call photoshop_flash() from _call_photoshop_flash_166
    w
    # Барди с довольным видом делает фотку
    img 15130
    with diss
    betty "Все?"
    bardie "Подождите, что-то не получилось фото. Ну-ка еще раз."
    w
    call photoshop_flash() from _call_photoshop_flash_167
    w
    # Барди делет еще несколько кадров
    img 15131
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_168
    w
    img 15132
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_169
    w
    img 15133
    with diss
    betty "Все! Хватит!"
    w
    call photoshop_flash() from _call_photoshop_flash_170
    w
    # Бетти опускает юбку, Моника следом за ней
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 14584
    with fadelong
    betty "Надеюсь, ты доволен?"
    img 14585
    with diss
    bardie "Очень! Вы обе доказали мне, что соблюдаете правила этого дома."
    bardie "..."
    img 14587
    with diss
    bardie "Моему однокласснику точно понравится!"
    # Бетти с Моникой офигевают
    music Power_Bots_Loop
    img 15134
    with hpunch
    mt "!!!"
    betty "!!!"
    # Бетти начинает орать, Моника зло смотрит
    img 15135
    with fade
    betty "ЧТООООО?!!"
    betty "Какому еще однокласснику?!"
    # Барди нагло
    music Groove2_85
    img 15136
    with diss
#    if ep28_monica_eric_meeting_completed == False:
    bardie "Ах да... Вы же еще не знакомы... Я скоро приглашу его в гости."
#    else:
#        bardie "Ах да... Ты еще с ним не знакома... В отличие от гувернантки."
    img 15119
    with diss
    mt "Он совсем обнаглел! Ненавижу эту малявку!"
    mt "И почему у этой деревенщины не хватает мозгов, чтобы приструнить его?!"
    music Power_Bots_Loop
    img 15137
    with fade
    betty "Нет!!! Не смей! Ты говорил, что это фото никто не увидит!"
    betty "!!!"
    music Groove2_85
    img 14587
    with diss
    bardie "Я так сказал?! Хм... Никто, кроме моего одноклассника."
    bardie "Аха-ха!"
    music Power_Bots_Loop
    img 15138
    with fade
    betty "Да как ты смеешь так обращаться со мной, порядочной женщиной?! Сопляк!"
    betty "Я - жена твоего отца! А ты собираешься показываеть фото, где я голая, да еще и с этой шлюхой, своему однокласснику!!!"
    img 15139
    with diss
    mt "Ненавижу эту семейку! Когда она будет моей гувернанткой, я ее уволю!"
    mt "!!!"
    music Groove2_85
    img 15140
    with fade
    bardie "Если ты и дальше будешь со мной так разговаривать, то женой моего отца ты будешь недолго..."
    bardie "Ты забыла, что у меня есть много фото, интересных фото...?"
    img 15141
    with diss
    bardie "И в интересной компании..."
    bardie "???"
    # Бетти смотрит испепеляющим взглядом, но молчит
    img 15142
    betty "!!!"
    img 15143
    with diss
    mt "Хм. Кто из нас после этого шлюха?"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15144
    with fade
    bardie "Вы на сегодня свободны. Можете идти."
    $ monicaMadeDoublePhotoBetty = True
    return


label dialogue_doublephoto_1a:
    betty "Гувернантка!!!"
    return False
