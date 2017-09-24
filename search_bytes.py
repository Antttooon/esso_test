from datetime import datetime


def search(file_name, string):
    """
    функция ищет байтовую подстроку в файле
    :param file_name: имя файла - str
    :param string: искомая строка - bytes
    :return: При наличии подстроки в файле  печатает "Yes" и точку первого вхождения
    """

    start = datetime.now()
    with open(file_name, 'rb') as f:
        data = f.read()
        # print('\n',data[1000:1010])
        if string in data:
            print('Yes')
            print(data.find(string))
    end = datetime.now()
    print(end - start,'\n')

search('file_image.jpg',b'\x08\x08\x08\t\x08\x0c\t\t\x0c\x11') 