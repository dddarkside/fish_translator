def bin2bloop(bin_code):
    answer = ""
    limit = len(bin_code)

    i = 0
    while True:

        while bin_code[i]=='1':      #б
            answer += 'б'
            i+=1
            if i == limit:
                return answer + "льк"
                
        while bin_code[i]=='0':      #у
            answer += 'у'
            i+=1
            if i == limit:
                return answer + "льк"
                
        if bin_code[i]=='1':         #ль
            answer += 'ль '


def encode(text):
    code = ""

    for sym in text:
        bin_code = format(ord(sym),'b')
        code += "\n" + bin2bloop(bin_code)

    return code


# print(encode('\t'))