init python:
    secret_objects_opened = []
    def open_secret_object(obj_name):
        if obj_name not in secret_objects_opened:
            secret_objects_opened.append(obj_name)
            notif(t__("Секретный предмет найден!"))
            renpy.play("Sounds/level_up.ogg", channel="sound")
        return
