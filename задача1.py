# Считывается таблица и записывается в виде списка
product_list = open('products.csv').readlines()
product_list_for_sum = [[i.split(';')[0], i.split(';')[1], i.split(';')[2], float(i.split(';')[3]), float(i.split(';')[4])] for i in product_list[1:]]
# К каждому списку продукта добавляется значение total
list_for_writing = [[str(s) for s in i]+[str(i[-2]*i[-1])] for i in product_list_for_sum]
# Список записывается в файл
product_list_writing = open('products_new.csv', 'w')
product_list_writing.write(product_list[0][:-1] + ';total' + '\n')
for i in list_for_writing:
    product_list_writing.write(';'.join(i) + '\n')