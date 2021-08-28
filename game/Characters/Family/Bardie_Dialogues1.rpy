label bardieDialogue1:
    if cloth != "Governess":
        mt "Я не хочу разговаривать с ним в таком виде."
        mt "Мне надо переодеться!"
        return
    #render+
    #Моника говорит с Барди в его комнате
    music Hidden_Agenda
    img 5798
#    imgr Dial_Bardie_1
    bardie "Я тебя сюда устроил, помнишь?"
    bardie "Ты мне должна!"
    img 5799
#    imgl Dial_begin37_2
    m "Я тебе ничего не должна, мальчик!"
    m "Веди себя вежливо по отношению ко старшим!"

    music Power_Bots_Loop
    img 5800
#    imgr Dial_Bardie_2
    bardie "Ах ты так!"
    bardie_t "Ну она у меня попляшет!"

    $ monicaBardieOffended1 = True

    music casualMusic
    return

label bardie_comment4:
    #render+
    #Барди у лестницы, stairs
    $ store_music()
    music Marty_Gots_a_Plan
    img 6056
    with fade
    bardie "Эй! Гувернантка!"
    bardie "Покажи что у тебя под юбкой!"
    img 6057
    m "С какой стати я буду это делать?!"
    img 6058
    bardie "Ты там что-то прячешь! Ты что-то украла!"
    music Pyro_Flow
    img 6059
    m "Я ничего не украла, малявка!"
    m "Как ты смеешь обвинять меня?!"
    img 6060
    bardie "Тогда докажи! Подними юбку!"
    img 6061
    m "Я не собираюсь ничего доказывать тебе, малявка!"
    m "Прочь с дороги!"
#    if bardieHeardAboutMarcus == True:
#        call EP22_Quests_Bardie1()
    $ restore_music()
    $ remove_hook(label="bardie_catch_monica_at_stairs_onetime")

    return True
