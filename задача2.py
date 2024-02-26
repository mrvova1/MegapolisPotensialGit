# Считывается таблица и на ее основе строится list
product_list = open('products.csv').readlines()
product_list_for_sum = [[i.split(';')[0], i.split(';')[1], i.split(';')[2], float(i.split(';')[3]), float(i.split(';')[4])] for i in product_list[1:]]
list_sort = []
# Сортируется список
for obj in product_list_for_sum:
    for prov in list_sort:
        if prov[0] > obj[0]:
            list_sort = list_sort[:list_sort.index(prov)] + [obj] + list_sort[list_sort.index(prov):]
            break
    if obj not in list_sort:
        list_sort.append(obj)
# list_sort - отсортированная таблица products.csv
# Отсортированный список заливается обратно в таблицу
product_list_writing = open('products.csv', 'w')
product_list_writing.write(product_list[0][:-1] + '\n')
for i in list_sort:
    product_list_writing.write(';'.join([str(ii) for ii in i]) + '\n')
# Задаются переменные, которые будут хранить в себе самую большую цену, категорию и список данных этого товара
sum0 = 0
cat = list_sort[0][0]
best_score = 0
for obj in list_sort:
    if obj[0] == cat and obj[-2] > sum0:
        sum0 = obj[-2]
        best_score = obj
print(f'В категории: {best_score[0]} самый дорогой товар: {best_score[1]} его цена за единицу товара составляет {best_score[-2]}')

