import json
# writeF = open('file.json', 'w', encoding='utf-8')
# # writeF.write('true')
# content = [None, True, (1, 2, 3), [1, 2, 3], 'hello', 'Привет']
# json.dump(content, writeF, ensure_ascii=False)
# writeF.close()
#
# readF = open('file.json', 'r', encoding='utf-8')
# # print(readF.read())
# # print(type(readF.read()))
# print(json.load(readF))
# readF.close()
# 1 задача
# readF = open('filr.txt', 'r', encoding='utf-8')
# content = readF.readlines()
#
# print(content)
#
# d = {}
# for record in content:
#     splited = record.split(': ')
#     d[splited[0]] = splited[1].rstrip()
# print(d)
# readF.close
#
# f = open('file.json', 'w', encoding='utf-8')
# json.dump(d, f, ensure_ascii=False)
# f.close()
# 2 задача
import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.json())['iss_position']
print(f'Широта: {data[\''']})


