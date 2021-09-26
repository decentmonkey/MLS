
init python:
    import datetime

    # время старта текущей сессии игры = время последней проверки
    persistent.game_last_time = datetime.datetime.now()
    # общее время в игре в секундах
    if persistent.gametime is None:
        persistent.gametime = 0

    def show_gametime(st, at):
        # сколько прошло со времени последней проверки
        t = datetime.datetime.now()
        dt = t - persistent.game_last_time
        # запоминаем текущее время, как время последней проверки
        persistent.game_last_time = t
        # суммируем время в игре со временем с последней проверки
        persistent.gametime += dt.total_seconds() # в секундах
        # переводим секунды в часы, минуты, секунды
        minutes, seconds = divmod(int(persistent.gametime), 60)
        hours, minutes = divmod(minutes, 60)
        # переводим текст в изображение
        # с форматированием (добавлением нулей, если число не двузначное)
        img = Text("{size=80}{color=#dcdddcf9}{b}%0*d:%0*d" % (2, hours, 2, minutes))
        # на выходе изображение со временем
        return img, .1
init:
    # привязываем функцию к динамическому изображению,
    # чтобы счетчик тикал без обновления экранов
    image gametime = DynamicDisplayable(show_gametime)
screen scr_game_time(showw1 = "false"):

    # эту же строку можно добавить и в главное меню:
    add "gametime":
        align(.1, .26)
        if showw1 == "false":
            at up_down
