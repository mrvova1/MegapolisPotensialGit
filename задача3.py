cat = input()
while cat != 'молоко':
    # Считывается таблица и на ее основе строится list
    product_list = open('products.csv').readlines()
    product_list_for_sum = [
        [i.split(';')[0], i.split(';')[1], i.split(';')[2], float(i.split(';')[3]), float(i.split(';')[4])] for i in
        product_list[1:]]
    list_sort = []
    # Задаются переменные, которые будут хранить в себе самое маленькое кол-во купленной продукции, категорию и список данных этого товара
    sum0 = 10 ** 100
    best_score = 0
    for obj in product_list_for_sum:
        if obj[0] == cat and obj[-1] < sum0:
            sum0 = obj[-1]
            best_score = obj
    if best_score == 0:
        print('Такой категории не существует в нашей БД')
    else:
        print(f'В категории: {best_score[0]} товар: {best_score[1]} был куплен {best_score[-1]} раз')
    cat = input()
