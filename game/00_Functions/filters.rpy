init python:
    def check_filter(filter, data): #проверяет сходится-ли объект с фильтром filter (словарь)
        global scenes_data
        json_list_type = type(scenes_data["misc"]["list_type"])
        for var1 in filter:
            if data.has_key(var1) != True:
                return False
            flag1 = False
#            if type(data[var1]) is list or type(data[var1]) is tuple or str(type(data[var1])) == "<type 'list'>":
            if type(data[var1]) is list or type(data[var1]) == json_list_type or type(data[var1]) is tuple:
                for i in data[var1]:
                    if i == filter[var1]:
                        flag1 = True
                if flag1 == False:
                    return False
            else:
                if data[var1] != filter[var1]:
                    return False
        return True
