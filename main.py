def number_to_dargin(num):
    if num == 0:
        return "нуль"
    
    basic_numbers = {
        1: "ца", 2: "кIвел", 3: "хIябал", 4: "авъал", 5: "швал",
        6: "уриґал", 7: "верхIал", 8: "гахIал", 9: "урчIимал", 10: "вицIал"
    }
    
    teens = {
        11: "вицIну цара", 12: "вицIну кIвира", 13: "вицIну хIябра",
        14: "вицIну авра", 15: "вицIну шура", 16: "вицIну уриґра",
        17: "вицIну верхIра", 18: "вицIну гахIра", 19: "вицIну урчIимра"
    }
    
    tens = {
        20: "гъал", 30: "хIябцIали", 40: "авцIали", 50: "шуцIали",
        60: "уриґцIали", 70: "верхIцIали", 80: "гахIцIали", 90: "урчIимцIали"
    }
    
    hundreds = {
        100: "даршал", 200: "кIвидарш", 300: "хIябдарш", 400: "авдарш",
        500: "шударш", 600: "уриґдарш", 700: "верхIдарш", 
        800: "гахIдарш", 900: "урчIимдарш"
    }
    
    def convert_under_thousand(n):
        if n == 0:
            return ""
        parts = []
        if n >= 100:
            h = (n // 100) * 100
            parts.append(hundreds[h])
            n %= 100
        if n >= 20:
            t = (n // 10) * 10
            parts.append(tens[t])
            n %= 10
            if n:
                parts.append(basic_numbers[n])
        elif n >= 11:
            parts.append(teens[n])
        elif n >= 1:
            parts.append(basic_numbers[n])
        return "ну ".join(parts) if len(parts) > 1 else (parts[0] if parts else "")
    
    def convert_with_thousands(n):
        if n < 1000:
            return convert_under_thousand(n)
        parts = []
        if n >= 1_000_000:
            m = n // 1_000_000
            parts.append(
                "āзирна āзир" if m == 1 
                else convert_under_thousand(m) + " āзирна āзир"
            )
            n %= 1_000_000
        if n >= 1000:
            th = n // 1000
            if th == 1:
                parts.append("āзир" if n % 1000 == 0 else "āзиллим")
            else:
                parts.append(convert_under_thousand(th) + " āзиллим")
            n %= 1000
        if n:
            r = convert_under_thousand(n)
            if r:
                parts.append(r)
        return " ".join(parts)
    
    return convert_with_thousands(num)



num = int(input("ДелкIи лугIи").strip())

dargin_text = number_to_dargin(abs(num))
if num < 0:
    dargin_text = "тIярхI " + dargin_text

print(f"{num} -> {dargin_text}")
