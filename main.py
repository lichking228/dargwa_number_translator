def number_to_dargin(num: int) -> str:
    if num == 0:
        return "нуль"

    UNITS_BASE = {1:"ца",2:"кIвел",3:"хIябал",4:"авъал",5:"швал",
                  6:"уриґал",7:"верхIал",8:"гахIал",9:"урчIимал"}
    UNITS_COMP = {1:"цара",2:"кIвира",3:"хIябра",4:"авра",5:"шура",
                  6:"уриґра",7:"верхIра",8:"гахIра",9:"урчIимра"}
    TEENS = {11:"вицIну цара",12:"вицIну кIвира",13:"вицIну хIябра",
             14:"вицIну авра",15:"вицIну шура",16:"вицIну уриґра",
             17:"вицIну верхIра",18:"вицIну гахIра",19:"вицIну урчIимра"}
    TENS_BASE = {20:"гъал",30:"хIябцIали",40:"авцIали",50:"шуцIали",
                 60:"уриґцIали",70:"верхIцIали",80:"гахIцIали",90:"урчIимцIали"}
    TENS_COMP = {20:"гъану",30:"хIябцIанну",40:"авцIанну",50:"шуцIанну",
                 60:"уриґцIанну",70:"верхIцIанну",80:"гахIцIанну",90:"урчIимцIанну"}
    HUNDREDS_BASE = {100:"даршал",200:"кIвидарш",300:"хIябдарш",400:"авдарш",
                     500:"шударш",600:"уриґдарш",700:"верхIдарш",
                     800:"гахIдарш",900:"урчIимдарш"}

    def hundred_word(h: int, tail: bool) -> str:
        if h == 100:
            return "даршлим" if tail else "даршал"
        return HUNDREDS_BASE[h] + ("лим" if tail else "")

    def under_thousand(n: int) -> str:
        if n == 0:
            return ""
        parts = []
        if n >= 100:
            h_val = (n // 100) * 100
            parts.append(hundred_word(h_val, n % 100 != 0))
            n %= 100
        if n >= 20:
            t = (n // 10) * 10
            parts.append(TENS_BASE[t] if n % 10 == 0 else TENS_COMP[t])
            n %= 10
            if n:
                parts.append(UNITS_COMP[n])
        elif n >= 11:
            parts.append(TEENS[n])
        elif n >= 1:
            parts.append(UNITS_BASE[n])
        return " ".join(parts)

    def with_thousands(n: int) -> str:
        if n < 1000:
            return under_thousand(n)
        parts = []
        if n >= 1_000_000:
            m = n // 1_000_000
            parts.append("āзирна āзир" if m == 1 else f"{under_thousand(m)} āзирна āзир")
            n %= 1_000_000
        if n >= 1000:
            th = n // 1000
            rem = n % 1000
            if th == 1:
                parts.append("āзир" if rem == 0 else "āзиллим")
            else:
                parts.append(f"{under_thousand(th)} {'āзир' if rem == 0 else 'āзиллим'}")
            n = rem
        if n:
            parts.append(under_thousand(n))
        return " ".join(parts)

    text = with_thousands(abs(num))
    if num < 0:
        text = "тIярхI " + text
    return text

if __name__ == "__main__":
    try:
        num = int(input("Введите целое число: ").strip())
    except ValueError:
        print("Ошибка: введите корректное целое число.")
