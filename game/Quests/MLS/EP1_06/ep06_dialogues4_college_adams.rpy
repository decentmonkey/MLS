define teacher_adams_t = Character(t_("Миссис Адамс"), who_color=c_orange, what_color=c_gray, what_italic=True) # училка инглиша Teacher5 Миссис Адамс, Mrs. Adams, thinking
define student_rose_t = Character(t_("Роуз"), who_color=c_pink, what_color=c_gray, what_italic=True) # одноклассница милая Роуз, Rose, thinking

# при клике на кабинет английского
# холл колледжа у двери кабинета
label ep06_dialogues4_college_adams_1:

    # Барди стоит у двери и рукой держится за ручку, в кабинет еще не зашел
    img 920000
    bardi "Вот черт! Я снова опоздал!.."
    # внезапно голос училки
    img 920001
    teacher_adams "Опаздываешь, [mcname]."
    # Барди смотрит в бок, видит рядом Миссис Адамс (observing-?)
    img 920002
    bardi_t "Вау... Эта Миссис Адамс клево выглядит..."
    # Барди быстро переводит взгляд на лицо преподавателя. Миссис Адамс мило улыбается прикрыв глаза.
    bardi "Кхм... Я... Я не опаздываю, просто задерживаюсь."
    # Миссис Адамс, поднимает указательный палец и говорит с некой наигранной строгостью
    img 920003
    teacher_adams "Задерживается преподаватель. Студенты - опаздывают."
    img 920002
    bardi "Значит, если преподаватель задерживается, то я не опоздаю, если приду раньше!"
    img 920003
    teacher_adams "Верно мыслишь... Но..."
    # Барди быстро открывает дверь, Адамс смотрит на него слегка удивленно, в той же позе.
    img 920002
    bardi "Никаких 'но'!"
    # звук двери
    # смена локации на кабинет английского
    # в классе сидят все студенты из группы Барди, кроме Сары (ее нет, она в спортзале)
    img 920004
    # Барди быстро заваливается в кабинет. Класс занят кто чем (Как это обычно бывает на парах, когда препода нет и все заняты своим делом)
    bardi "Успел!"
    # Миссис Адамс заходит за ним, С улыбкой машет в сторону его парты.
    img 920005
    teacher_adams "Садись уже на свое место, [mcname]..."
    #Затемнение
    #Просветление
    #Барди сидит на своем месте. Все ученики так же. Миссис Адамс с умным видом ходит между рядами с учебником.
    img 920006
    teacher_adams "*звуки какой-то однозначно безумно интересной лекции, которая проходит мимо ушей [mcname].*"
    img 920007
    # Барди в это время на нее пялится
    bardi_t "Интересно, у нее есть муж?.."
    img 920008
    #Миссис Адамс проходит мимо Барди. Заострите внимание на ее ногах.
    bardi_t "Да, наверняка есть... У такой-то красотки!.."
    bardi_t "Хмм... А сколько ей вообще лет?.."
    img 920010
    #Миссис адамс окидывает взглядом класс. Роуз подняла руку.
    teacher_adams "Итак, кто может дать ответ?"
    img 920009
    #Миссис Адамс смотрит на Роуз и указывает на нее рукой словно приглашая.
    teacher_adams "Да, Роуз?"
    img 920011
    #Роуз опускает руку и с умным видом отвечает.
    student_rose "Мне кажется, что..."
    student_rose "*звуки интереснейшего ответа на не менее интереснейший вопрос преподавателя, до которого [mcname] нет никакого дела.*"
    #Миссис Адамс сдержанно но очень мило и по доброму улыбается. Роуз довольная собой, но чуть смущенная смотрит на парту.
    teacher_adams "Отлично. Молодец, Роуз. Садись."
    student_rose "Спасибо, миссис Адамс."
    # Роуз садится
    teacher_adams "Продолжим..."
    #Затемнение
    #Просветление
    img 920012
    #Миссис адамс проходит перед Барди сверкая задницей, на которую Барди внимательно и усердно пялится крупным планом.
    img 920014
    teacher_adams "Я бы хотела услышать мнение [mcname] по этому поводу..."
    # Барди ее не слышит и не слушает
    img 920013
    #Воображение Барди играет на полную катушку. Раздеваем Миссис Адамс до трусов
    bardi_t "Какие трусики предпочитает миссис Адамс?.."
    bardi_t "..."
    # снимаем в фантазиях юбку
    bardi_t "Ееее!.."
    bardi_t "Отличная попка, миссис Адамс!"
    img 920015
    # в это время училка смотрит на Барди и повернулась к нему. поэтому крупный план спереди.
    teacher_adams_t "Боже... [mcname], как всегда, витает в облаках..." # мысли миссис Адамс
    img 920016
    teacher_adams_t "Совсем ведь не думает о своем будущем..."
    img 920015
    teacher_adams_t "Ладно... Я предполагала, что мне придется пойти на нечто подобное..."
    img 920018
    # Миссис Адамс наклоняется к лицу Барди
    teacher_adams "[mcname]?"
    #Барди резко поднимает взгляд на Миссис Адамс. Ее лицо нейтральное.
    #одной рукой обнимает себя за живот и в ее ладонь упирается локоть ее второй руки в кисти которой она держит закрытую книгу справа от ее лица.
    bardi_t "Что?.."
    bardi_t "Ох, вот черт!"
    bardi "Ах... Да... Кхм..."
    bardi "Я полностью с вами согласен, миссис Адамс."
    bardi "Эээ... Это действительно так. Мое мнение полностью совпадает с вашим!"
    img 920019
    teacher_adams_t "Правда?" # скептически
    #Звук звонка. Миссис Адамс переводит взгляд на других студентов.
    img 920020
    bardi "Ох... Ну, конечно, у меня была пара поправок относительно вопроса, о которых я хотел бы рассказать..."
    bardi "Но, как видите, занятие уже окончено... Очень жаль."
    img 920021
    #Миссис Адамс смотрит на Барди, Поза все та же, но на лице победительская ухмылочка.
    img 920022
    teacher_adams "Хорошо. Не буду задерживать остальных, все свободны."
    img 920023
    bardi_t "Остальных?"
    teacher_adams "Ну а тебя, [mcname], я с радостью выслушаю."
    bardi_t "О, нет! Вот я попал!.."
    #Миссис Адамс смотрит на Роуз. Роуз смотрит на Адамс озадаченно.
    teacher_adams "Роуз, останься пожалуйста тоже."
    #Затемнение.
    #Просветление.

    # в кабинете остаются миссис Адамс, Барди и Роуз, остальные студенты ушли
    #Барди стоит напротив Миссис Адамс. Роуз стоит рядом, так чтоб ее было видно.
    #Она в такой, зажатой позе, не очень понимает вообще что происходит.
    img 920024
    #Миссис Адамс в свою очередь стоит облокотившись к столу попой и скрестив руки на животе. (Обнимая себя за живот если будет понятнее.)  На ее лице ухмылка. (Больше добрая, чем подстебывающая.)
    teacher_adams "Ну? Мы тебя внимательно слушаем, [mcname]."
    bardi "Знаете, мне крайне неудобно занимать ваше внеурочное время, миссис Адамс."
    bardi "Я уверен, что у вас есть другие важные дела помимо того, чтобы возиться со..."
    img 920025
    #Миссис адамс закатывает глаза, после чего смотрит на барди с таким же лицом. Роуз переводит взгляд на Барди.
    teacher_adams "Ты слушал лекцию, [mcname]?"
    bardi "Естественно!"
    teacher_adams "Естественно нет?"
    img 920026
    #Нарисуйте на лице Роуз легкий смешок. Миссис адамс чуть нахмурилась. Поменяйте ее жестикуляцию. Просто расположение рук. Роуз смотрит вниз и прикрывает рот рукой.
    bardi "Естественно..."
    img 920027
    #Миссис Адамс нейтральная.
    teacher_adams "Почему?"
    bardi "Так вышло..."
    img 920028
    teacher_adams_t "Думаю, я отчетливо вижу причину..."
    img 920029
    #Миссис Адамс сексуально скрестила ноги все так же облокачиваясь, юбка чуть задралась.
    #Роуз вообще ничего не понимает
    teacher_adams "Внимание затмило что-то более интересное?"
    bardi_t "Черт!"
    bardi "Отчасти..."
    img 920030
    teacher_adams_t "Боже... Я, конечно, понимаю, что интересоваться подобным нормально в его возрасте... Но не в таких же количествах!.."
    teacher_adams_t "Хотя... Возможно, это и окажется ключом к его сознанию..."
    img 920031
    teacher_adams "Все с тобой понятно, [mcname]."
    img 920032
    #Миссис Адамс смотрит на Роуз. Та в свою очередь, смотрит на  препода в ответ.
    teacher_adams "Что насчет тебя, Роуз, ты молодец."
    teacher_adams "Я вижу, что ты усердно учишься и стараешься. Это очень похвально."
    img 920033
    #Роуз с улыбкой.
    student_rose "Спасибо, миссис Адамс! Рада, что оправдываю ваши ожидания!"
    img 920034
    teacher_adams "Как у вас движутся дела с проектом?"
    bardi_t "Ну неееет!.."
    img 920035
    student_rose "Все отлично, миссис Адамс!"
    student_rose "Мы уже заканчиваем писать вступление нашего эссе! Думаю, сегодня перейдем к основной части."
    img 920036
    #Барди смотрит на Роуз, та в какой-то нерешительности смотрит на него в ответ.
    bardi "Да?!"
    img 920037
    #Барди переводит взгляд на Миссис Адамс, которая смотрит на него хмуро и с недовольством.
    teacher_adams "..."
    bardi "Да!"
    bardi "Мы с Роуз очень плодотворно работаем над проектом!"
    img 920038
    #Миссис Адамс смотрит на Роуз теплым приятным взглядом. Поза такая же какая и была
    teacher_adams "Роуз, я тут подумала, может ты сменишь партнера для работы над проектом?"
    teacher_adams "Сара очень способная студентка. Она, как и ты, идет на высший балл."
    img 920024
    #Роуз смотрит на Барди с сочувствием.
    teacher_adams "Работать с ней тебе будет гораздо проще, так как у Сары есть интерес к учебе..." # смотрит на Роуз
    teacher_adams "В отличие от некоторых..." # переводит взгляд на Барди
    bardi_t "Ну ничего себе!"
    img 920039
    #Роуз смотрит на Миссис Адамс с извинительной улыбкой, слегка прищурившись и подняв руки на уровне груди ладонями в сторону Миссис Адамс. Сама Миссис Адамс невозмутима.
    student_rose "Эм... Спасибо, миссис Адамс, но мне комфортно с [mcname]..."
    student_rose "Он делает большой вклад в работу над нашим проектом!"
    bardi "?!?!"
    bardi_t "Черт... Вот теперь мне немного стыдно..."
    bardi_t "Нужно будет как-то отблагодарить Роуз за то, что пытается заступиться за меня..."
    img 920040
    #Роуз смотрит на Миссис Адамс слегка смущенно. Адамс улыбается.
    teacher_adams "Хорошо, я поняла тебя, Роуз."
    teacher_adams "Но я все еще переживаю... Поэтому запишу тебя на дополнительные занятия."
    img 920041
    teacher_adams "Будешь посещать их до тех пор, пока я не буду уверена, что ты действительно справляешься с проектом, ладно?"
    student_rose "Хорошо, миссис Адамс..."
    img 920042
    teacher_adams "Тогда не буду тебя больше задерживать, Роуз."
    img 920043
    student_rose "Спасибо, миссис Адамс. До свидания!"
    teacher_adams "До свидания."
    img 920044
    #Барди и роуз направляются в сторону выхода. На следующем рендере, когда Барди проходил мимо адамс, она кладет ему руку на плечо.
    bardi "До свидания, миссис Адамс!"
    img 920045
    teacher_adams "Нет-нет, [mcname]. С тобой мы еще побеседуем."
    bardi_t "Вот черт!"
    #Роуз открывает дверь и с сочувствующим взглядом оборачивается на Барди. На следующем рендере, она вышла из кабинета.
    img 920046
    #Барди оборачивается на Миссис Адамс. Она улыбается ему своей обычной улыбкой.
    teacher_adams "Давай перейдем сразу к делу, [mcname]."
    img 920047
    #Миссис Адамс слегка хмурая.
    teacher_adams "Ты же осознаешь, что такое отношение к учебе совершенно не подобает примерному студенту?"
    teacher_adams "К тому же, ты тянешь вниз Роуз."
    img 920048
    #Миссис Адамс отводит взгляд в сторону
    teacher_adams "Я, конечно, понимаю, почему она так заступается за тебя..."
    bardi "Потому что не может противостоять моей обаятельности?"
    img 920049
    teacher_adams "Именно..."
    bardi "Что?! Вы шутите, миссис Адамс?"
    bardi "Это было просто глупое предположение..."
    img 920050
    #Миссис Адамс смотрит на Барди с удивлением.
    teacher_adams_t "Так он даже и не догадывался... Мило..."
    img 920051
    teacher_adams_t "Хмм... Возможно, это даже пойдет нам на пользу..."
    img 920052
    #Сдержанный смешок в Миссис Адамс, который она прикрыла рукой.
    teacher_adams "Ладно, будем считать, что Роуз тебя просто пожалела..."
    bardi_t "Вот я идиот! Это же было очевидно!"
    bardi_t "Какая отличница в здравом уме согласится взять в проект кого-то вроде меня?"
    bardi "Я просто думал, что она просто... А оказывается..."
    teacher_adams "Да-да. Сказать по правде, я думала ты понимаешь, что ты ей не безразличен..."
    bardi "Теперь понимаю..."
    #Миссис Адамс нейтральная
    teacher_adams "И то, как ты относишься к ней и ее помощи - это очень некрасиво."
    teacher_adams "Роуз примерная и прилежная студентка. Уверена, она закончит колледж с отличием."
    teacher_adams "А ты сейчас - ее балласт, и попросту используешь ее. Ради собственной выгоды."
    teacher_adams "Такими темпами, ты запросто можешь запороть девочке диплом."
    #Миссис Адамс смотрит на Барди с сочувствием.
    bardi "И как мне теперь быть?"
    bardi "Если я влезу в этот проект со своей помощью, то конечный результат станет только хуже..."
    teacher_adams "Насчет этого я тоже хотела поговорить, [mcname]..."
    #Миссис Адамс снова хмурая. Она тычет в Барди рукой.
    teacher_adams "Мне крайне неприятно наблюдать за тем, как ты гробишь свою жизнь."
    teacher_adams "Ты совершенно не продвинешься в учебе. И что дальше?"
    bardi "У меня все под контролем, миссис Адамс. Все будет окей."
    #Миссис Адамс подходит к Барди и с  сочувствующим взглядом кладет руку ему на плечо.
    teacher_adams "[mcname], так нельзя. Я дорожу всеми своими студентами... И тобой в том числе."
    teacher_adams "Ты неглупый парень. Наоборот, очень способный."
    teacher_adams "Просто почему-то ты категорически не хочешь направить свой энтузиазм на учебу."
    teacher_adams "И когда-нибудь это может привести к негативным последствиям, а я этого не хочу."
    bardi_t "Ох, ничего себе!.."
    bardi_t "Неужели я вижу нормального преподавателя, действительно думающего о своих студентах?"
    bardi "Спасибо, миссис Адамс."
    bardi "Я обещаю, что придумаю, что делать с этим эссе..."
    bardi "Я не оставлю Роуз в этом деле одну. Так что можете не переживать."
    #Барди собирается уходить.
    teacher_adams "А тебе и не придется думать, [mcname]..."
    #Барди оборачивается на препода. Та в свою очередь стоит облокотившись к столу и смотрит на него милой улыбкой.
    bardi "В смысле?"
    teacher_adams "Я уже все придумала."
    teacher_adams "Я записала тебя на дополнительные занятия вместе с Роуз."
    teacher_adams "И права на отказ у тебя нет."
    bardi_t "Дополнительные занятия?!"
    bardi_t "Твою мать! У меня совсем нет времени на это! А как же моя подработка?!"
    bardi "Но, миссис Адамс!.. Я не могу!"
    bardi "Почему вы даже не спросили меня?.."
    #Миссис Адамс облокачиваясь о стол встала в какую-то сексуальную позу, и сексуально поправляет волосы.
    teacher_adams "Потому что я уверена, что отказать ты мне не сможешь, [mcname]."
    teacher_adams_t "Я уже знаю что пробудит твой энтузиазм..."
    bardi "Что?"
    #Миссис Адамс подмигивает Барди.
    teacher_adams "И да, у меня нет мужа..."
    bardi_t "Что?!"
    bardi_t "?!?!"
    bardi_t "Я что, говорил это вслух?! Да не может быть!"
    #Миссис Адамс смеется.
    teacher_adams "Судя по выражению твоего лица, я не ошиблась насчет твоих мыслей на занятиях по английскому..."
    bardi_t "Но как она догадалась?! Она что, умеет читать мысли?!"
    teacher_adams "Я хорошо понимаю людей, [mcname]..."
    #Миссис Адамс, сексуальное выражение лица и поза другая.
    teacher_adams "И сейчас я примерно представляю, как направить твой энтузиазм в нужное русло..."
    bardi "???"
    teacher_adams "Просто мне больно смотреть на то..."
    teacher_adams "Как студенты наплевательски относятся к своей учебе, а значит и к своему будущему..."
    #Барди подходит и стоит рядом с ней. Миссис адамс в сексуальной позе.
    teacher_adams "По моему предмету у тебя, к сожалению, все плохо..."
    teacher_adams "Но мне кажется, что правильный подход мог бы все улучшить."
    teacher_adams "Ты просто не представляешь, [mcname], сколько есть прекрасных произведений, которые ты упускаешь. В том числе и о любви."
    #Миссис Адамс все еще в той же позе, но раздвигает ноги и оборачивается лицом к барди.
    bardi_t "Мне кажется или она сейчас пытается намекнуть мне на что-то?.."
    teacher_adams "Я думаю попробовать новую методику с практическими занятиями..."
    bardi "С практическими занятиями?"
    teacher_adams "Именно. Что скажешь? Тебе интересно?"
    bardi_t "Ох, что-то подсказывает мне, что где-то здесь есть подвох... Или..."
    bardi_t "А вдруг нет?.."
    bardi "Нуу... Да, это звучит интересно..."
    #Миссис Адамс выпрямилась. Смотрит на Барди с ухмылкой.
    teacher_adams "И самое главное то, что ты ведь будешь не один..."
    teacher_adams "Мне кажется, вам с Роуз будет очень интересно работать над проектом вместе... Под моим наблюдением."
    teacher_adams "Думаю, вы могли бы многое друг о друге узнать... И это неплохо тебя с ней сблизит... Да и со мной в том числе..."
    #Миссис Адамс смотрит на Барди с победой в глазах. Она уверена что он сдался и полностью под ее контролем.
    bardi_t "Черт! Ладно, она умеет уговаривать..."
    bardi_t "А насчет подработки я что-нибудь придумаю..."
    bardi "Вы правы, миссис Адамс, у меня действительно есть проблемы с учебой. И решать их в одиночку было бы трудно..."
    bardi "Пара индивидуальных занятий мне явно не помешает."
    #Миссис Адамс. Сдержанная милая улыбка
    teacher_adams "Отлично! Рада, что мы с тобой нашли общий язык..."
    teacher_adams "Тогда как насчет понедельника? Приходи после учебы."
    teacher_adams "И да, я совсем забыла назначить время Роуз. Возьмешь ее с собой, ладно?"
    bardi "Ага... Без проблем."
    bardi "До свидания, миссис Адамс."
    teacher_adams "До свидания, [mcname]."
    #Барди разворачивается к двери.
    bardi_t "Ох... Ладно, посмотрим что из этого выйдет..."
    bardi_t "Надеюсь, это не превратится во что-то вроде спартанского курса миссис Брукс..."
    #Затемнение, звук двери
    #Просветление.
    #Барди выходит из класса, там его ждет роуз.
    # Она стоит облокотившись к стене и смотрит вверх. обе руки расслаблены и в них болтаясь свисает рюкзак.
    bardi "О, ты все еще тут?"
    #После этой фразы, роуз смотрит на Барди радостная. На следующем рендере она встает прямо и поправляет волосы. мило улыбается барди.
    student_rose "Ох, [mcname]... Я тебя уже заждалась!.."
    bardi_t "Боже... И как я мог не замечать ее чувств?.."
    bardi_t "После того, как об этом сказала миссис Адамс, это стало для меня очевидным..."
    bardi "Дааа... Меня, наконец-то, отпустили..."
    #Роуз смотрит на Барди с вопросительным сочувствием, тип спрашивая "Ну и на сколько все хреново?"
    student_rose "Ну и? Как все прошло?"
    bardi "Ну... Могло быть и хуже..."
    #Роуз хмурая и недовольная. Поза соответствующая.
    student_rose "Она пыталась тебя уговорить найти кого-то другого для работы над нашим проектом?"
    bardi_t "Так вот почему она ждала меня... Это настолько ее тревожит?"
    student_rose "Что бы миссис Адамс тебе не наговорила - не слушай ее!"
    #Роуз смотрит на дверь.
    student_rose "И вообще! Давай я сейчас пойду и поговорю с ней!"
    bardi "*сдержанный смешок*"
    #Роуз смотрит на Барди смущенно и все еще недовольно.
    student_rose "Что смешного? Я что-то не то сказала?!"
    bardi "Нет-нет... Просто... Это было очень мило..."
    #Роуз смотрит в сторону все так же смущенно, но это милое смущение. Позу с грозной и настойчивой, меняйте на зажатую.
    student_rose "Ты так считаешь?"
    bardi "Ага..."
    #Роуз снова хмурая, но по милому. Как злой недовольный котенок. Она смотрит на Барди.
    student_rose "А вот и нет! Я злая!"
    #Роуз отворачивается от Барди. Поза и лицо сдержанные.
    student_rose "Ну не вообще злая, а именно в этот момент..."
    bardi "И тем не менее, это было мило."
    #Роуз недовольно смотрит в сторону. Поза строгая, обиженная. (Стоит полубоком руки скрещены на животе.)
    student_rose "Нравится, когда я злюсь?"
    bardi "Совсем чуточку."
    #Роуз переводит недовольный взгляд на Барди, но на следующем рендере он становится лишь слегка обиженным. позу для следующего рендера тоже поменяйте.
    student_rose "Ну и что там было-то?.."
    bardi "Пошли, по дороге расскажу."
    #Роуз удивлена.
    student_rose "Куда пошли?"
    bardi "В лес."
    student_rose "Зачем?"
    bardi "Приставать к тебе буду. Зачем же еще?"
    #Роуз просто в шоке, отстраняется не много от Барди, чуть приподняла ногу и выставила руки так чтоб закрыться. Не страх, а шок, удивление.
    bardi "Да домой пойдем... Господи..."
    student_rose "К кому?"
    bardi_t "Боже... Это не лечится..."
    #Затемнение.
    #Просветление.
    #Барди и Роуз идут по улице (у ТЦ, мимо лотка с мороженым, за лотком стоит Бекки в своей обычной одежде, с сигаретой)
    # Барди не смотрит в сторону лотка с мороженным, увлечен разговором с Роуз
    # Бекки пока не показываем - отвернулась, наклонилась, что-то делает, что ее лица не видно
    # Роуз слегка зажатая смущенная и прочие прелести подросткового спектра эмоций.
    bardi "Роуз, ну хватит уже так переживать из-за миссис Адамс. Все же хорошо."
    student_rose "Да не переживаю я! И причем тут миссис Адамс?!"
    student_rose "Просто ты..."
    student_rose "Ты так выразился и я растерялась..."
    student_rose "Какой вообще лес?! Как можно было такое придумать?!"
    student_rose_t "О, Боже!.. Как же я могла так глупо повести себя?!"
    bardi "Ну прости... Это была просто глупая шутка."
    #Роуз смотрит на Барди обиженно.
    student_rose "Ладно... Что там было-то в итоге? О чем с тобой говорила миссис Адамс?"
    #Роуз смотрит на Барди, словно вдохновленно, с каким-то восхищением. Взгляд Барди сделайте чуть в сторону. Она в кадре, но мы смотрит не прямо на нее.
    bardi "Ну... Я записался на дополнительные занятия. Теперь мы будем ходить на них вместе..."
    #Барди фокусирует взгляд на роуз, на ее лице, А она в свою очередь тут же его отводит, словно смущенно.
    student_rose "Это круто..."
    bardi "Ага... Кстати, занятия будут по понедельникам. Миссис Адамс забыла тебе сказать об этом."
    student_rose "Спасибо..."
    #Роуз смотрит на Барди нейтрально.
    student_rose "А почему ты вообще согласился? Я думала тебе это не интересно..."
    bardi "А потому что нечего начинать наше эссе без меня! Ты уже и вступление написала!"
    student_rose "Да, я просто... Не думала, что тебе будет это интересно..."
    student_rose "Вот и решила сделать все сама..."
    #Роуз смотрит на Барди снова этими влюбленными глазами и вдохновленным лицом.
    bardi "А я думал, что мы вообще еще не начали! Я и не планировал всю работу взваливать на тебя!"
    bardi_t "Хоть это и не совсем то, что я планировал изначально..."
    bardi "Это ударило по моей гордости, Роуз... Тебе не стыдно?"
    #Роуз, хихикает
    student_rose "Стыжусь, прости..."
    bardi "Не прощу. Будешь должна."
    student_rose "Хорошо."
    #Роуз чуть смущенная.
    bardi "Роуз, с чего ты вообще взяла, что я хочу воспользоваться тобой и ничего не делать?"
    student_rose "Нууу... Я просто... Помочь хотела..."
    bardi_t "Мне действительно не стоило взваливать все на милашку Роуз. Я повел себя как законченный эгоист."
    #Барди фокусирует взгляд на лотке с мороженым
    bardi_t "Так... А вот и шанс для начала моего праведного пути..."
    menu:
        "Купить Роуз мороженое ($ 8).": # Если у Барди нет в кармане нужной суммы, то купить мороженое нельзя
            # минус 3 бакса у Барди
            bardi "Жарко, не думаешь?"
            #Роуз смотрит на Барди вопросительно.
            student_rose "Да, немного..."
            #Барди сворачивает к лавке с мороженым. Роуз чуть отстает потому что не понимает что он делает.
            student_rose "[mcname], ты куда?"
            bardi "Вершить великие дела! За мной!"
            #Барди и Роуз подходят к киоску с мороженым. Роуз счастливая и радостная.
            student_rose "О, точно! Мороженое!"
            #Роуз показывает пальцем на какое-то мороженное и смотрит на продавца.
            student_rose "Я буду такое!"
            # в этот момент Бекки поворачивается к ним и смотрит на Барди, расплываясь в улыбке
            bardi_t "?!"
            bardi_t "?!?!"
            becky "Отличный выбор, малышка!" # Бекки подмигивает Роуз
            # если была встреча с Бекки у ТЦ
            bardi_t "Бекки?!"
            bardi_t "Вот черт!"
            bardi_t "Она что, действительно тут продает мороженое?!"
            bardi_t "?!?!"
            bardi_t "Твою мать! Вот я попал!"
            bardi_t "Надеюсь, она ничего не скажет при Роуз!.."
            # Бекки переводит взгляд на Барди
            becky "А что выберет этот симпатичный парнишка?"
            bardi "Эээ... Мне то же самое, что выбрала она..."
            #Роуз подмигивает барди с ухмылкой. Бекки тем временем достает мороженое и поглядывает хитро на Барди.
            student_rose "Отличный выбор, [mcname]! У тебя есть вкус!"
            bardi "Просто доверился твоему."
            #Роуз самодовольно улыбается задрав нос.
            student_rose "Это было верное решение. Хи-хи."
            #Бекки держит в руках два рожка с мороженым и протягивает их барди с Роуз.
            becky "Пожалуйста, ваше мороженое. С вас 8 долларов."
            #Роуз полезла в сумку и ищет кошелек.
            student_rose "Да, сейчас..."
            # Барди, пока Роуз роется в сумке, кладет деньги на прилавок
            bardi "За двоих."
            # Бекки улыбается и протягивает Барди мороженое, подмигивает
            becky "Может, что-нибудь еще желаете, молодой человек, м?"
            bardi "Эээ... Нет-нет, спасибо..."
            bardi_t "Черт! Бекки, твою мать!"
            bardi_t "Она меня сейчас спалит перед Роуз!"
            bardi_t "Надо валить отсюда быстрее!.."
            #Роуз смотрит на Барди удивленно, с нотками страха.
            student_rose "Что, ты заплатил?! Но [mcname]! У меня есть деньги!"
            # Барди протягивает один рожок Роуз.
            bardi "Ой, не выделывайся, Роуз! Просто бери."
            #Роуз смущенно берет мороженку. и они отходят от этого места.
            # Бекки с улыбочкой машет вслед Барди и Роуз
            becky "Приходите еще. Буду очень рада вашему визиту..."
            student_rose "Спасибо! До свидания!"
            bardi_t "Уфф... Надеюсь, Роуз ничего не поняла..."
            #Роуз смотрит на Барди недовольно. Они уже отошли на достаточное расстояние
            student_rose "[mcname], мог бы и сразу сказать. что ты хочешь угостить меня!"
            student_rose "Я бы выбрала мороженое подешевле!"
            bardi "Хах! Ну все, теперь ты мой должник!"
            #Роуз посмеивается. легкий и сдержанный смешок.
            student_rose "Хи-хи... Хорошо!"
            #Роуз чуть смущенная.
            #Роуз прикрыв глаза целует Барди в щеку. Делает это резко чтоб Барди не успел опомниться.
            bardi_t "Воу! Ничего себе! Стесняшка Роуз?!"
            #Роуз очень смущенная идет рядом с Барди, пытаясь делать вид, словно ничего и не произошло.
            student_rose_t "О, Боже! Зачем я это сделала?!"
            student_rose_t "Что он теперь обо мне подумает?!"
            bardi "?!"
            #Роуз не смотрит на Барди, отводит глаза в сторону.
            student_rose "Мы рассчитались?"
            student_rose_t "Ой, что я несу?! Что за ужасное выражение?!"
            student_rose_t "Почему это прозвучало так, словно я проститутка?!"
            bardi "Не хочу считать это оплатой за мороженое, Роуз."
            bardi "Пусть это будет просто дружеский поцелуй, окей?"
            student_rose "Ладно..."
            student_rose_t "О, Боже! [mcname], ты шикарен!"
            #Роуз смотрит на Барди с наигранной злостью. Прошлое смущение еще не до конца прошло с ее лица.
            bardi "Так что ты мне все еще должна..."
            student_rose "[mcname]!"
            bardi "Да все-все! Шучу я..."
            #Затемнение
            pass
        "Не покупать.":
            bardi_t "Хотя, нет... Слишком уж дорого мне обойдется этот акт доброй воли."
            bardi_t "Перенесем это событие на другой день..."
            #Затемнение.
            pass
    #Просветление.
    #Барди и Роуз стоят у ее дома (входная дверь или крыльцо). смотрят друг на друга. У роуз на лице легкая приятная улыбка.
    bardi "Ну вот и все?"
    student_rose "Видимо..."
    bardi "Ладно, я пошел. Удачи."
    student_rose "И тебе..."
    #Барди разворачивается и собирается уходить.
    student_rose "Постой, [mcname]!"
    #Барди оборачивается, Роуз смотрит на него смущенно.
    bardi "Что такое? Что-то забыла?"
    student_rose "Нет, просто... Я подумала..."
    student_rose "Может пройдемся так же после дополнительных занятий в следующий раз?.."
    bardi "Оу... Почему бы и нет? Было весело."
    #Роуз повеселела. Позу сделайте соответствующую, но все еще сдержанную. Она все еще смущается.
    student_rose "Значит договорились?"
    bardi "Однозначно!"
    #Барди разворачивается и начинает уходить.
    bardi_t "Эти дополнительные занятия еще не начались, а все больше начинают мне нравиться..."
    bardi "Ладно, надеюсь это будет весело..."
    return

# !!в регулярный лейбл с Бекки вечером у ТЦ вставить if, если она продавала мороженое Барди и Роуз