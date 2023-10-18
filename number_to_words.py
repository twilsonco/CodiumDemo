import unittest

def Problem017(num):

    l1000 = ["", "thousand", "m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non", "dec"]
    os = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    ts = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hs = "hundred"

    def IntToStr(n):
        n = int(n)
        s = ""
        lt = int(log10(n) / log10(1000))
        for l in range(lt, -1, -1):
            d = n // 1000 ** l
            h = d // 100
            t = d % 100
            o = d % 10
            if h > 0:
                s += " ".join([os[h], hs])
                if t > 0 or o > 0:
                    s += " and "
            if t > 19:
                t = t // 10
                s += ts[t]
                if o > 0:
                    s += "-" + os[o]
            elif t > 9:
                t -= 10
                s += teens[t]
            elif t > 0:
                s += os[t]
            s += " " + l1000[l] + ("illion" if l > 1 else "") + (" " if l > 0 else "")
            n = n % 1000 ** l

        return s

    return IntToStr(num)


