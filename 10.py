# 提示使用者輸入生日月份與日期
BirthdayMonth = int(input('請輸入生日月份(1-12)：'))
BirthdayDate = int(input('請輸入生日日期(1-31)：'))

# 檢查月份是否輸入正確
if BirthdayMonth >= 1 and BirthdayMonth <= 12:

# 檢查日期是否輸入正確
 if BirthdayDate >= 1 and BirthdayDate <= 31:

    # 魔羯座12/22~01/19
    if (BirthdayMonth == 12 and BirthdayDate >= 22) or (BirthdayMonth == 1 and BirthdayDate <= 19):
      st.write('魔羯座12/22~01/19')
      st.write('優點:領導組織、傳統、成熟穩重、目標遠大、堅持理想')
      st.write('缺點:工作狂、不知變通、老成世故、易孤獨、功利主義')

    # 水瓶座01/20~02/18
    if (BirthdayMonth == 1 and BirthdayDate >= 20) or (BirthdayMonth == 2 and BirthdayDate <= 18):
      st.write('水瓶座01/20~02/18')
      st.write('優點:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義')
      st.write('缺點:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸')

    # 雙魚座02/19~03/20
    if (BirthdayMonth == 2 and BirthdayDate >= 19) or (BirthdayMonth == 3 and BirthdayDate <= 20):
      st.write('雙魚座02/19~03/20')
      st.write('優點:想像力強、具有同情心、藝術特質、浪漫多情')
      st.write('缺點:不切實際、多愁善感、只說不做、易受傷、軟弱')

    # 牡羊座03/21~04/19
    if (BirthdayMonth == 3 and BirthdayDate >= 21) or (BirthdayMonth == 4 and BirthdayDate <= 19):
      st.write('牡羊座03/21~04/19')
      st.write('優點:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快')
      st.write('缺點:好戰、不服輸、沒耐性、自我、暴躁、衝動、尖酸刻薄')

    # 金牛座04/20~05/20
    if (BirthdayMonth == 4 and BirthdayDate >= 20) or (BirthdayMonth == 5 and BirthdayDate <= 20):
      st.write('金牛座04/20~05/20')
      st.write('優點:值得信賴、有主見、意志堅定、熱情、友善、有耐心')
      st.write('缺點:易沒安全感、重視物質、固執倔強、懶惰、自我放縱、易怒')

    # 雙子座05/21~06/21
    if (BirthdayMonth == 5 and BirthdayDate >= 21) or (BirthdayMonth == 6 and BirthdayDate <= 21):
      st.write('雙子座05/21~06/21')
      st.write('優點:聰明、反應快、擅溝通、博學、好奇心強、學習力強')
      st.write('缺點:善變、雙重性格、缺乏耐性、狡猾、不可靠、不專心')

    # 巨蟹座06/22~07/22
    if (BirthdayMonth == 6 and BirthdayDate >= 22) or (BirthdayMonth == 7 and BirthdayDate <= 22):
      st.write('巨蟹座06/22~07/22')
      st.write('優點:溫柔、感性、保護家人、收藏家、敏感、同情心')
      st.write('缺點:情緒化、沒安全感、自私、被動、沉溺回憶')

    # 獅子座07/23~08/22
    if (BirthdayMonth == 7 and BirthdayDate >= 23) or (BirthdayMonth == 8 and BirthdayDate <= 22):
      st.write('獅子座07/23~08/22')
      st.write('優點:自信、創造、領導、表演、熱心助人、表達')
      st.write('缺點:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人')

    # 處女座08/23~09/22
    if (BirthdayMonth == 8 and BirthdayDate >= 23) or (BirthdayMonth == 9 and BirthdayDate <= 22):
      st.write('處女座08/23~09/22')
      st.write('優點:組織分析、謹慎、穩定、負責、擅思考、注重養生')
      st.write('缺點:嘮叨、神經質、潔癖、狡猾、挑剔、缺乏遠見')

    # 天秤座09/23~10/23
    if (BirthdayMonth == 9 and BirthdayDate >= 23) or (BirthdayMonth == 10 and BirthdayDate <= 23):
      st.write('天秤座09/23~10/23')
      st.write('優點:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心')
      st.write('缺點:猶豫不決、依賴、善辯、注重外在、懶惰散漫')

    # 天蠍座10/24~11/22
    if (BirthdayMonth == 10 and BirthdayDate >= 24) or (BirthdayMonth == 11 and BirthdayDate <= 22):
      st.write('天蠍座10/24~11/22')
      st.write('優點:持續力強、權威、迎接挑戰、愛恨分明、敏感')
      st.write('缺點:多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖')

    # 射手座11/23~12/21
    if (BirthdayMonth == 11 and BirthdayDate >= 23) or (BirthdayMonth == 12 and BirthdayDate <= 21):
      st.write('射手座11/23~12/21')
      st.write('優點:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強')
      st.write('缺點:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅')
