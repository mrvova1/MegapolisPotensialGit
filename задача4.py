def promocod(csv_f):
    '''
    Создает промокоды для товаров
    :param csv_f: Название таблицы из для которой хотим создать промокоды
    :return: product_promo.csv
    '''
    # Считывается таблица и на ее основе строится list
    product_list = open(csv_f).readlines()
    product_list_for_sum = [[i.split(';')[0], i.split(';')[1], i.split(';')[2], i.split(';')[3], i.split(';')[4][:-1]] for i in product_list[1:]]
    # Добавляем к каждому товару его промокод
    for obj in product_list_for_sum:
        obj.append(str(obj[1][:2] + obj[2].split('.')[0] + obj[1][:-3:-1] + obj[2].split('.')[1][::-1]).upper())
    # Записываем все в таблицу product_promo.csv
    product_list_writing = open('product_promo.csv', 'w')
    product_list_writing.write(product_list[0][:-1] + ';promocode' + '\n')
    for i in product_list_for_sum:
        product_list_writing.write(';'.join(i) + '\n')