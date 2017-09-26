from datetime import datetime


def search(file_name, string):
    """
    функция ищет все байтовые подстроки в файле
    :param file_name: имя файла - str
    :param string: искомая строка - bytes
    :return: При наличии подстроки в файле  печатает "Yes" и точку первого вхождения
    """

    start = datetime.now()
    with open(file_name, 'rb') as f:
        # print('\n',data[1000:1010])
        lenght = 0
        for i in f.readlines():
            if string in i:
                pos = lenght+i.find(string)
                print('Yes')
                print('Позиция от начала файла', pos)
            lenght += len(i)
    end = datetime.now()
    print(end - start,'\n')

search('file_image.jpg',b'\x08\x08\x08\t\x08\x0c\t\t\x0c\x11')

# ________________________________test____________________________________

# with open('file_image.jpg', 'rb') as f:
#     print(f.read()[1000:1010])

# with open('file_image.jpg', 'rb') as f:
#     print(f.read()[12385:12395])
