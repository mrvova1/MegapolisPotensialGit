# Считывается таблица и на ее основе строится list
product_list = open('products.csv').readlines()
product_list_for_sum = [[i.split(';')[0], i.split(';')[1], i.split(';')[2], float(i.split(';')[3]), float(i.split(';')[4])] for i in product_list[1:]]
# Задаем список и словарь, в которых будут хранится данные в виде {Category: Count} и [Category, Count]
hash_dict = {}
hash_list = []
# Если нужен список ПРОДУКТОВ с наименьшей продоваемостью, с ключом в виде котегории:
# Заполняем список
for obj in product_list_for_sum:
    hash_list.append([obj[0], obj[-1]])
# Сортируем по второму парамметру (по числу покупок)
hash_list = sorted(hash_list, key=lambda x: x[1])
# Выводим получившийся список
print('\n'.join([', '.join([i[0], str(i[1])]) for i in hash_list[:10]]))
# Если нужен список КАТЕГОРИЙ с наименьшей продоваемостью, с ключом в виде котегории:
# # Заполняем словарь
# for obj in product_list_for_sum:
#     if obj[0] not in hash_dict:
#         hash_dict[obj[0]] = obj[-1]
#     else:
#         hash_dict[obj[0]] += obj[-1]
# # На основе словоря заполняем список
# for key in hash_dict.keys():
#     hash_list.append([key, hash_dict[key]])
# # Выводим получившийся список
# print('\n'.join([', '.join([i[0], str(i[1])]) for i in hash_list[:10]]))
