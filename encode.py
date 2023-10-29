from struct import pack

# начальная длина словаря 256 - расширенная версия ASCII
init_dict_len = 256
dictionary = {chr(_): _ for _ in range(init_dict_len)}


def compress(data):
    # буфер в который будет складывать новые символы
    buffer = ""
    res = []
    # актуальная длина словаря (пригодится при добавлении новых слов)
    cur_dict_len = init_dict_len
    # проходимся по всем символам исходного текста
    for item in data:
        new_word = buffer + item
        if new_word in dictionary:
            buffer = new_word

        # если мы накнулись на неизвестную комбинацию, то добавляем ее в словарь и увеличиваем длину словаря,
        # а содержимое буфера кодируем и добавляем в ответ
        else:
            res.append(dictionary[buffer])
            dictionary[new_word] = cur_dict_len
            cur_dict_len += 1
            buffer = item

    # добавляем последнее слово в ответ
    if buffer in dictionary:
        res.append(dictionary[buffer])

    return res


def solve():
    # получаем наш файл, который надо сжать
    print("Введите имя файла для сжатия: ")
    file_name = input()
    with open(file_name + ".txt", 'r') as f:
        # записываем в data содержимое файла
        data = f.read()
    # Передаем содержимое файла в функцию сжатия
    comp_res = compress(data)

    with open(file_name + "_lzw.txt", "wb") as rf:
        for r in comp_res:
            # записываем результат в типе int и порядке байт big-endian (порядок от старшего байта к младшему)
            rf.write(pack('>h', int(r)))


if __name__ == '__main__':
    solve()