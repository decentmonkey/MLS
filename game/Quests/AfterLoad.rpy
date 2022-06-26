label process_afterload:
    $ debugShowImageName = False

    call questHelp_init() from _rcall_questHelp_init
    call phone_backgrounds_init() from _rcall_phone_backgrounds_init_1
    call ep13_update_init() from _rcall_ep13_update_init
    return
