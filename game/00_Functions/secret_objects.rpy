init python:
    def open_secret_object(obj_name):
        if persistent.secret_objects is None:
            persistent.secret_objects = []
        if obj_name not in persistent.secret_objects:
            persistent.secret_objects.append(obj_name)
            notif(t__("Секретный предмет найден!"))
            renpy.play("Sounds/level_up.ogg", channel="sound")
        return
