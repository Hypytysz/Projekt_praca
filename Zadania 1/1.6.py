# Spłaszczanie list


def splaczanie_listy(_2d_list):
    splaszczona = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                splaszczona.append(item)
                if type(item) is list:
                    splaszczona.remove(item)
                    for i in item:
                        splaszczona.append(i)
        else:
            print(element)
            splaszczona.append(element)
    print("Splaczona lista: ", splaszczona)


oryginalna = [[1, 2], [3, 4, [5, 6]]]
splaczanie_listy(oryginalna)
print("Oryginalna lista: ", oryginalna)
