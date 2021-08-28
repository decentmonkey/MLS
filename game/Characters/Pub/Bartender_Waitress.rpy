label bartenderWaitressProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = t_("Жена бармена. Лапает меня, пока Джо не видит.")
        pass
    if char_data["level"] == 3:
        $ progress_character_name = t_("Эшли")
        help "Прогресс [progress_character_name] максимален, ждите следующих обновлений игры!"
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = t_("Work in progress...")
    return
