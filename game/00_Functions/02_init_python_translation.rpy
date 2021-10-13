python early:
    #json.loads(renpy.file("language_dict.json").read())
    #language_dict2 = json.loads(renpy.file("language_dict2.json").read())
    #str1 = renpy.file("language_dict.json").read().replace('\r\n', '\n')
    #hash = hashlib.md5(str1).hexdigest()
    language_dict = {}
    language_dict_hash = "729657222"
    list_files = renpy.list_files()
    language_files_list = []
    for fileName in list_files:
        if fileName[-5:] == ".json":
            if "language_" in fileName:
                language_files_list.append(fileName)
    language_files_list.sort()
    for langFileName in language_files_list:
        languageFile = json.loads(renpy.file(str(langFileName)).read())
        for langLine in languageFile:
            language_dict[langLine] = languageFile[langLine]
    hash = zlib.crc32(json.dumps(language_dict))

#    for line in language_dict2:
#        language_dict[line] = language_dict2[line]
#    language_dict = renpy.file("language_dict.json").read()

#    open(config.basedir + "/game/update_data.json", "wb").write(str)
    def parse_tstr(str1):
        global item1
        result = re.findall(r'\[(.*?)\]', str1)
#        str1 = str1.replace("{c}", "{")
#        str1 = str1.replace("{/c}", "}")
#        str1 = str1.replace("{", "{c}")
#        str1 = str1.replace("}", "{/c}")
#        str1 = str1.replace("{c{/c}", "{c}")
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
#        global _preferences, language_fields, language_dict
#        lang = _preferences.language
#        if language_dict.has_key(s):
#            s = language_dict[s][language_fields[lang]]
#        return parse_tstr(s)
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
