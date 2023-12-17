def str_full2half(input_string):
    '''
       將中文全形符號轉換成半形，便於比對及處理
    '''

    fullwidth_chars = "，。！？`「」："
    halfwidth_chars = ",.!?'[]:"
    # === generate transform table ===
    translation_table = str.maketrans(fullwidth_chars, halfwidth_chars)

    result_string = input_string.translate(translation_table)

    return result_string
