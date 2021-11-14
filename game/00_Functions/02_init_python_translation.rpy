#python early:
init python:
    language_dict = {}
    list_files = renpy.list_files()
    language_files_list = []
    for fileName in list_files:
        if fileName[-5:] == ".json":
            if "language_" in fileName:
                language_files_list.append(fileName)
    language_files_list.sort()
    language_flag1 = False
    language_count1 = 0
    language_count_all = 0
    for langFileName in language_files_list:
        languageFile = json.loads(renpy.file(str(langFileName)).read())
        if language_flag1 == False:
            language_dict = languageFile
            hash1 = hashlib.md5(renpy.file(str(langFileName)).read()).hexdigest()
            language_count_all = len(language_dict)
            language_count1 = len(language_dict)
            language_flag1 = True
        else:
            for langLine in languageFile:
                language_dict[langLine] = languageFile[langLine]
            language_count_all += len(languageFile)

    language_dict_len = len(language_dict)
    if persistent.lang_suffixes is None or persistent.lang_count != language_dict_len:
        language_completed_list = [0]*(max(language_fields.values())+1)
        for lang_line_key, lang_line in language_dict.items():
            for lang_key, lang_value in language_fields.items():
                if lang_line[lang_value] != "":
                    language_completed_list[lang_value] += 1
        lang_suffixes = {}
        for lang_key in language_fields:
            if language_completed_list[language_fields[lang_key]] != language_dict_len:
                lang_suffixes[lang_key] = " (" + str(int(float(language_completed_list[language_fields[lang_key]]) / float(language_dict_len)*100)) + "%)"
            else:
                lang_suffixes[lang_key] = ""
        persistent.lang_suffixes = lang_suffixes
        persistent.lang_count = language_dict_len
    languageFile = False

    def parse_tstr(str1):
        global item1
        result = re.findall(r'\[(.*?)\]', str1)
        for var1 in result:
            var2 = var1
            translateVarFlag = False
            if var2[-2:] == "!t":
                var2 = var2[:-2]
                translateVarFlag = True
            if globals().has_key(var2):
                if translateVarFlag == True:
                    str1 = str1.replace("[" + var1 + "]", str(t__((globals()[var2]))))
                else:
                    str1 = str1.replace("[" + var1 + "]", str(globals()[var2]))
            else:
                if translateVarFlag == True:
                    str1 = str1.replace("[" + var1 + "]", "{c}" + t__(var2) + "{/c}")
                else:
                    str1 = str1.replace("[" + var1 + "]", "{c}" + var2 + "{/c}")
        return str1
    def t_(s):
        return s
    def t__(s):
        global _preferences, language_fields, language_dict
        lang = _preferences.language
        if language_fields.has_key(lang) == False:
            lang = "english"
        st = s
        if language_dict.has_key(s):
            st = language_dict[s][language_fields[lang]]
            if st == "":
                st = language_dict[s][language_fields["english"]]
                if st == "":
                    st = s
            st = st.split("#")[0]
        return parse_tstr(st)

    def ts__(s):
        global _preferences, language_fields, language_dict
        lang = _preferences.language
        st = s
        if language_dict.has_key(s):
            st = language_dict[s][language_fields[lang]]
            if st == "":
                st = language_dict[s][language_fields["english"]]
                if st == "":
                    st = s
            st = st.split("#")[0]
        return parse_tstr(st)

    def t___(s):
        global _preferences, language_fields, language_dict
        s = re.sub(r'(\n\s*)', " ", s)
        lang = _preferences.language
        if language_fields.has_key(lang) == False:
            lang = "english"
        st = s
        if language_dict.has_key(s):
            st = language_dict[s][language_fields[lang]]
            if st == "":
                st = language_dict[s][language_fields["english"]]
                if st == "":
                    st = s
            st = st.split("#")[0]

        st = parse_tstr(st)
        st = st.replace(" ", " ")
        st = re.sub("\!\s{1,}", "!\n", st)
        st = re.sub("\?\s{1,}", "?\n", st)
        st = re.sub("\.\s{1,}", ".\n", st)
        st = re.sub("Mr\.\\n", "Mr. ", st)
        st = re.sub("Mrs\.\\n", "Mrs. ", st)
        st = re.sub("Ms\.\\n", "Ms. ", st)
        return st
