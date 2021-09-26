define e = Character('Эйлин', color="#c8ffc8")
define r = Character('me', color="#c8ffc8")
define l = Character('mama', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
label sms_text:
    # чтобы текст смс запоминался при сохранениях
    $ sms_text = []
    # имя собеседника
    $ sms_nar = "Не определен"
    $ sms_on()
    $ sms_clear()
    pause 1
    #$l = Character('left', color="#c8ffc8")
    $ sms_clear()
    r "123"
    pause 2
    l "1231 111 123 456 1233"
    pause 3
    r "132 125 345 12 65 42 786 7883 67889 574 547547745 4746677777 777 7456456"
    pause 4
    r "177 982 233 986"
    pause 2
    l "126 673 711"
    pause 3
    r "132 333 331 523 134 654"
    pause 3
    l "565 456"
    pause 1
    # очистить
    $ sms_clear()
    pause 1.0
    # и спрятать экран смс
    $ sms_off()
    "The конец"
    return
# Игра начинается здесь:


label iphone:
    #jump sms_text
    $notes_text += "123\n321"
    $notes_text += "\nbla bla bla"
    $notes_text += "\n1111 111111 1111 111 111 11111 11 11111 1111 111 111 11111 11 111"
    $notes_text += "\n2222 222222 2222 222 222 22222 22 22222 2222 222 222 22222 22 222"
    $notes_text += "\n3333 333333 3333 333 333 33333 33 33333 3333 333 333 33333 33 333"
    $notes_text += "\n4444 444444 4444 444 444 44444 44 44444 4444 444 444 44444 44 444"
    show screen iphone_x
    pause

    hide screen iphone_x
    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
