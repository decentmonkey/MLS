label process_afterload:
    call questHelp_init() from _rcall_questHelp_init
    call phone_backgrounds_init()
    call ep13_update_init() from _rcall_ep13_update_init
    return
