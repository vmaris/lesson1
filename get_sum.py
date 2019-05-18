def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    get_sum = f'{one} {delimiter} {two}'
    # завершение функцииб возвращает результат
    return get_sum
    # OR return str(one+delimiter+two)

one1 = "Learn"
two1 = "python"

print(get_sum(one1, two1, '-'))
title = get_sum(one1,two1)
print(title.upper())