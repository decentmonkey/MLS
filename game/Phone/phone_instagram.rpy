label phone_instagram1:
    $ phone_instagram_posts = [
        ["/images/Phone/insta/Feed_past.jpg", t_("Наконец-то, этот долгожданный день настал! Сегодня я оставляю это гребаное захолустье!")]
    ]
    return

label phone_instagram1_Olivia:
    $ phone_set_new("instagram")
    $ phone_instagram_posts = [
        ["/images/Phone/insta/Olivia_feed1.jpg", t_("Я не художник, но рисую свои мечты. Я не писатель, но пишу свою книгу жизни.")],
        ["/images/Phone/insta/Olivia_feed2.jpg", t_("Забудь о том, кто ты есть сейчас и стань тем, кем хочешь быть.")],
        ["/images/Phone/insta/Olivia_feed3.jpg", t_("Найти себя невозможно — себя можно только создать.")],
        ["/images/Phone/insta/Olivia_feed4.jpg", t_("Я в восторге от факта собственного существования!")],
        ["/images/Phone/insta/Olivia_feed5.jpg", t_("Всё самое лучшее случается неожиданно.")]
    ]
    return

label phone_instagram2:
    # init EP2
    $ phone_instagram_posts_multi = {
        "MC": {"caption": t_("BestBoy0398"), "img":"/images/contacts/Contacts_MC.png", "posts":[["/images/Phone/insta/Feed_past.jpg", t_("Наконец-то, этот долгожданный день настал! Сегодня я оставляю это гребаное захолустье!")]]},
        "Olivia": {"caption": t_("Olivia_Beauty21"), "img":"/images/contacts/Contacts_Olivia.png", "posts":[
            ["/images/Phone/insta/Olivia_feed1.jpg", t_("Я не художник, но рисую свои мечты. Я не писатель, но пишу свою книгу жизни.")],
            ["/images/Phone/insta/Olivia_feed2.jpg", t_("Забудь о том, кто ты есть сейчас и стань тем, кем хочешь быть.")],
            ["/images/Phone/insta/Olivia_feed3.jpg", t_("Найти себя невозможно — себя можно только создать.")],
            ["/images/Phone/insta/Olivia_feed4.jpg", t_("Я в восторге от факта собственного существования!")],
            ["/images/Phone/insta/Olivia_feed5.jpg", t_("Всё самое лучшее случается неожиданно.")]
        ]}
    }
    return

label phone_instagram3: # Emily
    $ phone_instagram_posts_multi["Emily"] = {"caption": t_("sunshine.emily"), "img":"/images/contacts/Contacts_Emily.png", "posts":[
            ["/images/Phone/insta/Emily_feed1.jpg", t_("Хорошенькая девушка может носить почти все или почти ничего.")],
            ["/images/Phone/insta/Emily_feed2.jpg", t_("Я красивая, добрая и милая. А злые и страшные мне просто завидуют.")],
            ["/images/Phone/insta/Emily_feed3.jpg", t_("Если мужчина поднял на вас руку, то пусть с этой рукой и коротает все оставшиеся ночи.")],
            ["/images/Phone/insta/Emily_feed4.jpg", t_("Девчонки, а у вас в шкафу тоже живет забавное существо по имени 'Нечего надеть'?")],
            ["/images/Phone/insta/Emily_feed5.jpg", t_("Так устала… Хочу шампанского, клубники, цветов и на ручки!")]
    ]}
    $ phone_instagram_new.append("Emily")
    return

