define config.steam_appid = 1794470

init python:
    def steam_achievement(achName):
        if steamVersion != True:
            return
        achievement.grant(achName)
        achievement.sync()
        return

    def questHelp_achievement_check(questName):
        if steamVersion != True:
            return
        questHelp_achievements_list = {
            "house_10" : "ach18"
        }
        if questHelp_achievements_list.has_key(questName):
            achievement.grant(questHelp_achievements_list[questName])
            achievement.sync()
        return
















#
