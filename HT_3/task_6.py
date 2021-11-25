"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > виводимо тільки цифри, починаючи з кінця
"""

def handle_line(s):
    if len(s) < 30:
        print(sum(int(i) for i in s if i.isdigit()))
        print(''.join(i for i in s if not i.isdigit()))
    elif len(s) > 50:
        print(''.join(i for i in s if i.isdigit())[::-1])
    else:
        print(len(s))
        print(len(''.join(i for i in s if not i.isdigit())))
        print(len(''.join(i for i in s if i.isdigit())))


handle_line("f98neroi4nr0c3n30i")
handle_line("f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe0")
handle_line("f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345")
