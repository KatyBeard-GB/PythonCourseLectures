# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

slovar = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, 
          {" VIII ":"S007"}]
result = list()
for i in slovar:
    for k in i:
        result.append(i[k])
print(set(result))
# slovar.values() - получить все значения словаря
# slovar.keys() - получить все ключи