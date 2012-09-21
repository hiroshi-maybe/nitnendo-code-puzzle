def decode_morse(str):
    chars=str.split()
    result=""
    morse_dic = {"iI":"A", "Iiii":"B", "IiIi":"C", "Iii":"D", "i":"E", "iiIi":"F", "IIi":"G", "iiii":"H", "ii":"I"
                  , "iIII":"J", "IiI":"K", "iIii":"L", "II":"M", "Ii":"N", "III":"O", "iIIi":"P", "IIiI":"Q"
                  , "iIi":"R", "iii":"S", "I":"T", "iiI":"U", "iiiI":"V", "iII":"W", "IiiI":"X", "IiII":"Y", "IIii":"Z"}
    for char in chars:
        result+=morse_dic[char]
    return result
