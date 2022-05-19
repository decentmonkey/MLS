default mlsBardiFamilyV5Cynthia1 = 0 # Барди поговорил с Синтией по просьбе Оливии

## суббота утро, после разговора с Оливией

# доступно только при условии, что Барди разговаривал с Оливией (mlsBardiFamilyV5Olivia1 > 0)
# при клике на комнату Синтии
# Никаких автотрекеров! Это затянет сцену. Если игрок не кликает, а уходит, то вечером в субботу дверь закрыта (Синтии нет дома, она с Николь). дверь доступна для клика станет в воскресенье утром.
label ep05_dialogues6_family_cynthia_1:
    # Синтия сидит у себя в комнате с книжкой на кровати, подавленная и зажатая.
    bardi_t "А вот и наша грустная милашка..."
    bardi "Привет, Синтия." ##->#####inc
    #####inc bardi "Привет, сестренка."
    # Синтия смотрит на Барди с легкой наигранной улыбкой.
    cynthia "О, [mcname], привет. Как ты?"
    bardi "Да, хорошо все..."
    cynthia "Что-то случилось?"
    menu:
        "Нет ничего.":
            bardi_t "Пожалуй, я еще не готов к подобному мозговому штурму..."
            bardi "Нет, все окей."
            bardi "Просто хотел спросить, все ли у тебя в порядке?"
            cynthia "Да..."
            # Синтия растерянно смотрит по сторонам, после чего останавливается довольный взгляд на книге. Изобразите это в трех рендерах.
            cynthia "..."
            cynthia "Просто вот..."
            cynthia "В книгу окунулась."
            bardi_t "Мда... Не умеешь ты врать."
            bardi "И о чем книга?"
            # Синтия растерянно смотрит на книгу. После переводит неуверенный взгляд на Барди.
            cynthia "О любви! Это Лавкрафт."
            bardi "Ммм... Лавкрафт - идеальный выбор для ценителей этого жанра..."
            # Синти растерянно смотрит на обложку. Затем переводит взгляд на Барди.
            cynthia "Да... Тут есть скрытый смысл..."
            bardi "Ну хорошо, не буду отвлекать тебя."
            # Барди разворачивается и идет к выходу
            bardi_t "Да ну нафиг, пусть сами разбираются."
            bardi_t "Как-нибудь потом с ней поговорю..."
            # но Синтия окликает его
            cynthia "[mcname], подожди!.."
            # он снова поворачивается к ней, Синтия грустно
            cynthia "Дело в том, что... В общем..."
            pass
        "Все ли в порядке?":
            bardi "Да ничего... Просто ты выглядишь какой-то подавленной..."
            cynthia "Ой, да все в порядке."
            # Синтия растерянно смотрит по сторонам, после чего останавливается довольный взгляд на книге. Изобразите это в трех рендерах.
            cynthia "Просто вот..."
            cynthia "В книгу окунулась."
            bardi_t "Мда... Не умеешь ты врать."
            bardi "И о чем книга?"
            # Синтия растерянно смотрит на книгу. После переводит неуверенный взгляд на Барди.
            cynthia "О любви! Это Лавкрафт."
            bardi "Ммм... Лавкрафт - идеальный выбор для ценителей этого жанра..."
            # Синти растерянно смотрит на обложку, затем, переводит взгляд на Барди. В двух рендерах.
            cynthia "Да... Тут есть скрытый смысл..."
            bardi "Не умеешь ты врать, Синтия. Давай колись уже!"
            bardi "Я слышал ваш диалог с Оливией..."
            # Синтия смотрит на Барди возмущенно удивленным взглядом.
            cynthia "Ты все слышал?"
            bardi "Да, я проходил мимо и случайно застал вас за душещипательным разговором..."
            # Синтия расстроенно опускает взгляд вниз.
            bardi "Не молчи, Синтия. Я могу помочь советом, если ты расскажешь, в чем именно проблема." ##->#####inc
            #####inc bardi "Не молчи, сестренка. Я же твой брат и могу помочь советом, если ты расскажешь, в чем именно проблема."
            # Синтия поднимает глазки на Барди и смущенно и подавленно начинает.
            cynthia "Ну... Понимаешь..."
            cynthia "Между мной и Оливией что-то произошло..."
            bardi "Это я понял по вашему разговору. В чем контекст?"
            pass
    # Синтия снова отводит взгляд
    cynthia "Мне кажется, Оливия обиделась на меня..."
    bardi_t "Ну нихрена себе!"
    bardi_t "Эта сестрофилка ненавидит абсолютно все и вся! Но ни за что не тебя!"
    bardi_t "Боже... И как ты еще не поняла этой фигни, Синтия?!"
    bardi "С чего ты это взяла?"
    cynthia "Ну..."
    cynthia "Наше общение с ней стало намного холоднее после той ситуации..."
    cynthia "Когда мы поссорились с ней. Помнишь?"
    cynthia "Мне кажется, я зря на нее тогда так взъелась."
    cynthia "Оливия же просто переживала за меня. А по-другому показывать свои чувства она не умеет..."
    bardi_t "По-твоему, это ТЫ на нее взъелась?! Серьезно?!"
    # Синтия возмущенная и лицом и позой.
    cynthia "Хотя она и не должна была переживать! Ты же мне как брат!" ##->#####inc
    #####inc cynthia "Хотя она и не должна была переживать! Ты же наш брат!"
    cynthia "Зачем вообще переживать из-за этого?!"
    # Синтия снова подавленная.
    cynthia "Но я все равно не должна была портить с ней отношения."
    cynthia "Мы же с ней сестры, а я столько всего наговорила ей!.."
    cynthia "Я же не хотела с ней ссориться и не желала ей зла..."
    bardi_t "Фак... И что за детская хрень тут началась?"
    bardi_t "Ладно, [mcname], это, конечно, максимально тупо, но примерно этого ты и ожидал..."
    bardi_t "Первая - стерва, которой ее ЧСВшность не позволит прийти и на прямую разобраться..."
    bardi_t "А вторая - невинная душа, чувствующая свою вину. Которой быть и не должно!"
    bardi_t "Господи! Оливия должна извиниться за то, что заставляет Синтию так загоняться!"
    bardi_t "Ладно, сейчас мне нужно думать о том, как разрешить это недопонимание..."
    bardi_t "И вдолбить в голову Синтии, что ей загоняться нужно в последнюю очередь."
    # Синтия смотрит на Барди, она вроде и подавлена, но внимательно слушает его.
    bardi "Так, я вроде все понял..."
    bardi "Но мне кажется, что ты вообще не должна переживать по этому поводу."
    # Синтия вопросительно смотрит на Бари.
    cynthia "Это еще почему?"
    bardi "Потому что Оливия, наверняка, давно уже забила на ту ситуацию."
    bardi "А если и помнит, то тебя она винит в последнюю очередь."
    # Синтия возмущенно машет головой.
    cynthia "Ты ничего не понимаешь!.."
    bardi_t "Ну конечно! Как раз таки я вижу всю картину целиком, в отличие от тебя..."
    # Синтия подавленно смотрит на Барди.
    cynthia "Ты совсем не знаешь Оливию..."
    bardi_t "Ага... По-моему, в этом доме никто не знает эту сестрофилку лучше меня."
    bardi "Возможно, ты и права, Синтия..." ##->#####inc
    #####inc bardi "Возможно, ты и права, сестренка..."
    cynthia "Конечно, права!"
    cynthia "Знаешь какая Оливия обидчивая?!"
    # Синтия обиженно отводит взгляд и сидит обнимая колени.
    cynthia "Она, наверняка, уже сделала меня врагом народа!.."
    cynthia "И зачем я вообще так с ней обошлась?!"
    bardi "Да как?! Отстояла свои интересы?!"
    bardi "Это твое право! В этом совершенно нет твоей вины!.."
    # Синтия смотрит на Барди.
    cynthia "Я знаю... Но..."
    bardi "Уверен, Оливия считает также."
    # Синтия в той же позе хмуро и надув щеки смотрит в сторону.
    cynthia "Нет... Она не принимает никакого иного мнения, кроме своего!"
    bardi_t "Ну, тут я, пожалуй, с тобой соглашусь..."
    # Синтия смотрит на Барди грустненько, подавленно, чуть наклонив голову и положив щеку на колено.
    cynthia "Но я дорожу нашими отношениями."
    cynthia "Она класная на самом деле. Просто иногда ведет себя... Плохо!"
    bardi_t "Как сучка она себя ведет! Нужно называть вещи своими именами!"
    cynthia "И после той ситуации наши отношения стали намного холоднее..."
    # Синтия сидит в зажатой и обиженно-грустной позе, как и ее выражение лица.
    cynthia "Я словно чувствую ее обиду... И от этого мне очень грустно..."
    # Синтия закрывает лицо руками.
    cynthia "Я совершенно не знаю, что с этим делать..."
    bardi_t "Да нихрена! Все просто! Поцелуй ее, извинись и она засияет от счастья!.."
    bardi_t "И обкончается..."
    # Синтия с надеждой и тоской смотрит на Барди.
    cynthia "Что мне делать, [mcname]?"
    bardi_t "Да уж... Синтия уже конкретно себе накрутила там всякого..."
    menu:
        "Успокоить Синтию.":
            pass
    bardi "Ничего не делать."
    bardi "Я уверен, она так же как и ты хочет все исправить."
    bardi "Вам всего лишь стоит поговорить по душам."
    # Синтия обиженно отворачивается.
    cynthia "Думаешь, это вообще возможно с человеком вроде Оливии?!"
    bardi "Нет. Ни для кого это, пожалуй, невозможно..."
    bardi "Ни для кого, кроме тебя."
    # Синтия снова смотрит  на Барди. Выражение лица более или менее живое и теплое. Но поза все такая же зажатая.
    bardi "Она же любит тебя. Ты для нее любимая младшая сестренка."
    bardi_t "И предмет сексуальных фантазий, который страпонит ее на досуге."
    bardi_t "Но тебе это знать не обязательно..."
    # Синтия уже улыбается, легкой и искренней улыбкой, но слабо заметной.
    cynthia "Может, ты и прав... В конце концов, мы и правда помиримся..."
    # Синтия снова подавленная смотрит в сторону.
    cynthia "Но это произойдет потом. А я хочу сейчас."
    cynthia "А сейчас она холодная и не любит меня!.."
    # Синтия переводит взгляд на Барди.
    bardi "Боже! Меня бы она так не любила!"
    cynthia "Что?"
    bardi_t "Фак! Это должно было прозвучать только в мыслях..."
    bardi "Нет-нет, ничего..."
    # Синтия снова отводит взгляд.
    bardi_t "Так. Ну я уже не знаю, что делать с этой наивной глупой дурочкой..."
    bardi_t "Что еще можно сказать?"
    bardi_t "Ладно, видимо, надо менять тактику."
    bardi_t "Если никакой из моих вариантов не подходит, пусть Синтия сама что-нибудь придумает."
    # Барди подсаживается к Синтии, мы к ней ближе. Она смотрит на него. взгляд такой же тоскливый. сидит в позе типа лотоса
    bardi "Есть идеи дальнейшего развития событий?"
    # Синтия опускает голову.
    cynthia "Честно говоря, вообще ни одной идеи..."
    bardi "..."
    cynthia "Хотя, есть одна... Но, мне кажется, она провальная."
    bardi "А вот это уже интересно! Рассказывай."
    # Синтия смотрит на Барди. Взгляд нейтральный, ожидающий какой-либо критики ее решения.
    cynthia "Я думала купить ей какой-нибудь подарок в знак примирения..."
    bardi "?!"
    bardi_t "Да хрена с два эта стерва заслуживает хоть какой-нибудь подарок!"
    bardi_t "Да и не нужен он вообще!"
    bardi_t "Оливия спит и видит, как бы извиниться перед тобой!"
    bardi_t "А даже если бы это и было не так! Какой, мать твою, подарок заслуживает человек вроде Оливии?!"
    # Синтия обеспокоена. Поменяйте позу, сделайте ее чуть смущенной.
    cynthia "Ну?"
    bardi "Что?"
    cynthia "Ты чего так завис?.."
    bardi "Кхм... Я просто слегка задумался..."
    # Синтия улыбается. Она не прям радостная, но при этом заметна легкая улыбка на ее лице.
    bardi "Подарок это отличная идея."
    bardi "Не понимаю, почему ты хотела отказаться от этой мысли. Мне кажется, это будет идеально."
    # Синтия вновь слегка зажатая, позой и выражением лица показывает нерешительность.
    cynthia "Ну, с этим есть некоторые затруднения..."
    cynthia "С которыми, мне кажется, я не справлюсь..."
    bardi_t " Ох... И почему мне кажется, что это очередная головная боль для меня?"
    cynthia "Я совершенно не знаю, что можно было бы ей подарить."
    bardi "Как так?! Я думал, что раз вы очень близки, ты знаешь, что может ей понравится..."
    # Синтия смотрит на Барди с тоской.
    cynthia "Это так. Но, тем не менее, она всегда держится на расстоянии."
    cynthia "Я не знаю, как это описать. Я это просто чувствую..."
    # Синтия отводит взгляд.
    cynthia "Она не любит говорить о себе и своих увлечениях, кроме инсты."
    cynthia "Поэтому я даже не представляю, чему бы она могла обрадоваться..."
    bardi_t "Тебе! Голой и связанной на кровати!"
    bardi_t "Но вряд ли тебе стоит знать об этом..."
    bardi "И из-за этого ты считаешь, что идея провальная?"
    # Синтия смотрит на Барди жалобными глазами.
    cynthia "Ну, плохому подарку мало кто обрадуется..."
    bardi "По-моему, ты слишком загоняешься, Синтия."
    bardi "Самое важное, что ты проявишь к ней внимание. Думаю, она оценит именно это."
    cynthia "И тем не менее... Я хочу, чтобы этот подарок ей понравился."
    cynthia "Эх, вот бы кто-нибудь поговорил бы с ней и узнал..."
    bardi_t "О, нееет!.. Конечно же, этот кто-нибудь - это я!.."
    bardi_t "Твою мать!"
    bardi_t "Ну окей. По крайней мере, это не должно доставить хлопот."
    bardi_t "Я даже сейчас знаю, какой подарок был бы идеальным..."
    bardi_t "Оливия ничему так не обрадуется, как ношенным панталонам Синтии."
    bardi_t "Но об этом Синтии лучше не знать..."
    menu:
        "Предложить свою помощь Синтии.":
            pass
    bardi "Я тебя понял. Попробую что-нибудь выведать у Оливии."
    # Синтия смотрит на Барди радостная.
    cynthia "Правда?!"
    bardi "Ага."
    cynthia "Ой, как здорово!"
    cynthia "[mcname], а ты сможешь сделать это так, чтобы Оливия ни о чем не догадалась?"
    bardi "Думаю, да..."
    bardi_t "Нет. Я просто спрошу напрямую."
    # радостная Синтия обнимает Барди.
    cynthia "Ох, спасибо большое, [mcname]! Ты самый лучший!" ##->#####inc
    #####inc cynthia "Ох, спасибо большое, [mcname]! Ты лучший брат на свете!"
    bardi "Да без проблем..."
    bardi_t "Боже, как приятно... Это того стоит."
    # Синтия отстраняется от Барди и смотрит на него полная счастья
    cynthia "Ты узнаешь у нее, а потом мы вместе пойдем и выберем ей подарок, да?"
    bardi_t "Да, это явно того стоило. Думаю, это неплохо нас сблизит с Синтией..."
    bardi "Конечно, Синтия. С радостью составлю тебе компанию."
    # Синтия смотрит на Барди вся из себя довольная. Поза открытая, соответствующая.
    cynthia "Отлично! С первой проблемой мы разобрались!.."
    bardi_t "Таааак!.."
    bardi_t "А вот это мне уже не нравится!"
    bardi "Постой-постой! С первой?!"
    bardi "А есть еще?!"
    # Синтия смущенно отводит взгляд, поза зажатая. Кончики указательных пальцев тычут друг в друга, голова чуть отвернута, щеки слегка надуты.
    cynthia "Нууу..."
    cynthia "Тут такое дело..."
    # Синтия смотрит на Барди глазками снизу вверх. Не обиженная и смущенная, скорее неуверенная.
    cynthia "Мое финансовое состояние не располагает достаточными ресурсами..."
    bardi "Что?"
    cynthia "Мне чуть-чуть... Совсем немного... Не хватает денег..."
    bardi "И каково сейчас твое финансовое состояние? Сколько у тебя сейчас денег?"
    # Синтия падает на кровать рядом с Барди. изобразите это сексуальным ракурсом.
    cynthia "Нисколько."
    cynthia "Полный ноль."
    bardi_t "Фааак..."
    bardi_t "Собственно, чего же ты еще ожидал, [mcname]?!"
    bardi_t "Что в кои-то веки все будет легко? А вот хрен тебе!"
    bardi "А сколько тебе надо денег на подарок?"
    # Синтия невинными глазками смотрит на Барди
    cynthia "150 баксов."
    bardi_t "Сколько?! Ну нихрена себе!"
    bardi_t "Это еще что за суммы?!"
    bardi_t "А не слишком ли жирно для психованной сестрофилки?!"
    bardi "Мдаа... Деньги не маленькие..."
    # Синтия смотрит на него жалобным взглядом.
    cynthia "Да... Но мне нужно именно 150..."
    cynthia "Вот был бы у меня человек, который мог бы занять мне такую сумму..."
    bardi "Синтия, это не маленькие деньги. Мало кто займет тебе столько."
    cynthia "Наверное, только кто-то очень близкий..."
    cynthia "Думаю, у меня есть один такой человек..."
    bardi_t "Ой, а который уже час?! Засиделся я кажется!"
    bardi_t "Хрен там знает, на кого она намекает, но, надеюсь, ей не откажут..."
    # Барди собирается вставать с кровати.
    bardi "Ну, тут я могу только пожелать тебе удачи."
    bardi "Надеюсь, у тебя получится найти деньги."
    bardi "А с Оливией я поговорю..."
    # Синтия резко привстала и хватается за Барди усаживая его обратно на кровать и не давая встать.
    # Держит его за бедра. Выражение лица в отчаянии, чуть ли не ревет но наигранно. Максимально наигранно.
    cynthia "Ну [mcname]! Ты же понимаешь, что я говорю о тебе!" ##->#####inc
    #####inc cynthia "Ну братик! Ты же понимаешь, что я говорю о тебе!"
    cynthia "Мне же не к кому больше обратиться! У меня только ты!"
    bardi "У тебя есть Софи! И Дейзи с Николь! И Генри!" ##->#####inc
    #####inc bardi "У тебя есть мама! И Дейзи с Николь! И Генри!"
    cynthia "Ну [mcname]!!!"
    cynthia "Ну ты же не откажешь мне?!"
    bardi_t "Что угодно проси - помогу! Но денег на эту стерву Оливию не дам!"
    bardi "Синтия, да откуда у меня такие деньги?!"
    # Синтия утыкается лицом в бедра Барди близь паха.
    cynthia "Ну ты же работаешь!"
    bardi "И что?! Это не значит, что я миллионер!"
    cynthia "Ну помоги-и-и!"
    bardi_t "Фак! Хватит ерзать у моего члена! У меня уже вставать начинает!"
    bardi "Отпусти меня! Мне неудобно, Синтия!"
    cynthia "Ну [mcname]!!!"
    cynthia "Ну кто, если не ты, поможет мне?!" ##->#####inc
    #####inc cynthia "Ну кто, если не ты, поможет своей любимой младшей сестре?!"
    menu:
        "Согласиться помочь Синтии.":
            pass
    bardi_t "Твою же мать! "
    bardi "Ладно-ладно! Я найду деньги!"
    # Синтия вскакивает, Лицо сразу радостное. Руки на плечах Барди. Смотрит на него.
    cynthia "Правда?!"
    bardi "Да... Правда..."
    bardi_t "И почему именно я?! Почему именно я должен был встрять в это дерьмо?!"
    # Синтия обнимает Барди, на следующем рендере они валятся на кровать.
    # Итак, дорогие художники, делайте что хотите, но в этом моменте и в следующих до тех пор пока Барди не встанет с кровати, член читателя должен стоять!
    cynthia "[mcname]! Я тебя обожаю! Ты лучший!" ##->#####inc
    #####inc cynthia "Братик! Я тебя обожаю! Ты лучший!"
    bardi_t "Да-да... Спасибо..."
    bardi_t "Господин 'Вытащи меня из дерьма' снова в деле..."
    bardi_t "Черт! Ну вот с какого хрена я должен оплачивать подарок для этой стервы Оливии?!"
    bardi_t "?!?!"
    # Меняйте ракурс.
    bardi_t "Эх... В любом случае, бросить Синтию я не могу."
    bardi_t "Не хочу, чтобы Синтия думала, что не может на меня положиться..."
    bardi_t "Да, я делаю это ради нее."
    bardi_t "Синтия будет должна мне. Вот теперь уж точно!"
    bardi "Ну все-все! Хватит."
    # Барди и Синтия поднимаются и снова сидя на Кровати. Синтия смотрит на Барди с благодарностью, счастливая.
    # Синтия целует Барди в щеку. На следующем рендере отстраняется и смотрит на него.
    bardi_t "Оу! Ну ничего себе!"
    cynthia "Спасибо большое, [mcname]!"
    cynthia "Ты даже не представляешь, как для меня это важно!"
    bardi "Да без проблем. Обращайся в любое время. Я всегда рад помочь тебе."
    # Синти мило улыбается.
    cynthia "Спасибо! Ты лучший!"
    # Барди встал с кровати. Синтия сидит, возможно в другой позе, но так же улыбаясь смотрит на него.
    bardi "Ладно... Пойду узнаю, что могло бы понравиться Оливии..."
    bardi "И насчет денег подумаю."
    bardi "Как все будет готово, я скажу тебе, ладно?"
    cynthia "Хорошо! Еще раз спасибо!"
    # Бари разворачивается и идет к выходу. На следующем рендере Барди выходит из комнаты.
    bardi_t "Итак, что мы имеем?"
    bardi_t "Если вкратце, я в дерьме."
    bardi_t "Ну а если развернуто..."
    bardi_t "Какого хрена меня вообще в это втянули?! Оливия!.. Мать ее!.."
    bardi_t "Ладно, разберусь по ходу. Для начала стоит поговорить с этой стервой..."
    # смена кадра на холл (в холле, в движке, уже стоит Оливия)
    $ mlsBardiFamilyV5Cynthia1 = day # Барди поговорил с Синтией по просьбе Оливии
    # в квест-лог "Поговорить с Оливией насчет подарка."
    return

    # далее снова разговор с Оливией

# если игрок еще не поговорил с Оливией о подарке (2-й разговор с ней)
# при клике на комнату Синтии
label ep05_dialogues6_family_cynthia_2:
    # Синтия лежит на кровати и читает книгу
    cynthia "О, [mcname], привет!"
    bardi "Привет, Синтия."
    cynthia "Ну как? Все готово?"
    bardi "Говоря по правде, еще нет..."
    # Синтия чуть погрустнела.
    cynthia "Ясно..."
    bardi "Но скоро все будет, не переживай."
    # Синтия снова улыбается Барди.
    cynthia "Я знаю, я тебе верю."
    cynthia "Просто мне уже не терпится!.."
    bardi "Понимаю."
    bardi "Ну ладно. Как будет все сделано, я тебе сразу сообщу."
    cynthia "Хорошо. Я буду ждать."
    return

# если кликнуть на контакт Оливии в телефоне Барди
# при условии, что Барди согласился помочь Оливии и поговорить с Синтией, но еще не сделал этого
# if mlsBardiFamilyV5Olivia1 > 0 and mlsBardiFamilyV5Cynthia1 == 0
label ep05_dialogues6_family_cynthia_3:
    ## chat olivia
    ## не рендерить
    bardi "Привет :)"
    olivia "Ты уже поговорил с Синтией?"
    bardi "Еще нет. Как раз собираюсь заняться этим вопросом..."
    olivia "Какого хрена так долго?!"
    olivia "Давай скорее, я жду!"
    return

# если Барди согласился помочь Оливии и поговорить с Синтией, поговорил, но с Оливией второго разговора еще не было
# if mlsBardiFamilyV5Olivia1 > 0 and mlsBardiFamilyV5Cynthia1 > 0 and mlsBardiFamilyV5Olivia2 == 0
label ep05_dialogues6_family_cynthia_4:
    ## chat olivia
    ## не рендерить
    bardi "Привет, Оливия!"
    olivia "Ну? Какие новости?"
    bardi "Я пообщался с Синтией. Скоро расскажу тебе все."
    olivia "Давай скорее, я жду!"
    return

# если кликнуть на контакт Синтии в телефоне Барди
# при условии, что Барди уже поговорил с ней по просьбе Оливии
# if mlsBardiFamilyV5Cynthia1 > 0
label ep05_dialogues6_family_cynthia_5:
    ## chat cynthia
    ## не рендерить
    bardi "Привет, Синтия."
    cynthia "Привет! :)"
    cynthia "Как дела? Все готово?"
    bardi "Еще нет..."
    bardi "Но скоро все будет, не переживай."
    cynthia "Мне уже не терпится! :)"
    bardi "Как будет все сделано, я тебе сразу сообщу."
    cynthia "Хорошо. Жду."
    cynthia "Спасибо тебе за помощь, [mcname]!"
    cynthia "Ты лучший! :)"
    return

# если кликнуть на контакт Оливии в телефоне Барди
# при условии, что все разговоры состоялись
# if mlsBardiFamilyV5Olivia1 > 0 and mlsBardiFamilyV5Cynthia1 > 0 and mlsBardiFamilyV5Olivia2 > 0
label ep05_dialogues6_family_cynthia_6:
    ## chat olivia
    ## не рендерить
    bardi "Привет, Оливия! Как дела?"
    olivia "Привет. Ты уже нашел деньги для подарка?"
    bardi "Воу! Не так быстро!"
    bardi "Нашла миллионера!"
    bardi "Мне еще надо обдумать, как все это провернуть..."
    olivia "Сообщи, как все уладишь."
    olivia "Я жду."
    bardi "Вас понял, госпожа."
    olivia "Да пошел ты!"
    return
