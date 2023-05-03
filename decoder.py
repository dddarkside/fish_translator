ERROR_SIGNAL = False
# coding: utf8

def transform(symbol):
    return chr(int(symbol,2))  #ord()


def error():
    global ERROR_SIGNAL
    ERROR_SIGNAL = True


def decode_unit(i, limit, symbol, code, end_signal):

    while code[i]!="б":
        i+=1

    while code[i]=="б" and i<limit:  #Все Б
        symbol += "1"
        i+=1

    while code[i]=="у" and i<limit:  #Все У
        symbol += "0"
        i+=1

    if code[i] != "л":
        error()

    #Концовка
    if i+2 < limit:
        if code[i:i+3] == "льк":
            end_signal = 1
            i+=3
            return [i,limit,symbol,code, end_signal]

        elif i+1 < limit:
            if code[i:i+2] == "ль":
                i+=2

        else:
            error()
            
    elif i+1 < limit:
        if code[i:i+2] == "ль":
            i+=2

    else:
        error()

    while code[i] == " " and i<limit:
        i+=1

    return [i,limit,symbol,code, end_signal]

def decode(code):
    i = 0
    limit = len(code)
    symbol = ""
    end_signal = 0
    translated = ""

    global ERROR_SIGNAL
    while i<limit and not ERROR_SIGNAL:
        i,limit,symbol,code,end_signal = decode_unit(i,limit,symbol,code,end_signal)

        if end_signal:
            translated += transform(symbol)
            symbol = ""
            end_signal = 0

    if symbol:
        translated += transform(symbol)
    return translated
   


# print(decode("бууууульк"))