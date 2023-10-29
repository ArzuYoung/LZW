from struct import unpack

# начальная длина словаря 256 - расширенная версия ASCII
init_dict_len = 256
dictionary = {_: chr(_) for _ in range(init_dict_len)}


def decode(data):
    # буфер, в который записываем что декодируем
    buffer = ""
    res = ""
    # актуальная длина словаря
    cur_dict_len = init_dict_len
    # проходимся по всем кодам в data
    for item in data:
        if item not in dictionary:
            dictionary[item] = buffer + (buffer[0])
        res += dictionary[item]

        if buffer != "":
            dictionary[cur_dict_len] = buffer + dictionary[item][0]
            cur_dict_len += 1

        buffer = dictionary[item]

    return res


def solve():
    # получаем файл, который будем декодировать
    print("Введите имя файла для распаковки: ")
    file_name = input()
    data = []
    with open(file_name + ".txt", 'rb') as f:
        # записываем в data содержимое файла, считываем по 2 символа,
        # пока не дойдем до 1-ого последнего, обозначающего конец файла
        while 1:
            x = f.read(2)
            if len(x) != 2:
                break

            # распаковываем и достаем код символа
            (x_, ) = unpack(">h", x)
            data.append(x_)

    res = decode(data)

    with open(file_name + "_decode.txt", "w") as f:
        # записываем результат в файл
        f.write(res)


if __name__ == '__main__':
    solve()
