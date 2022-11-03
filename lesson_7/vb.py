# #ints = []
# try:
#     f = open('vbn')
# expect FileNotFoundError:
#     print('ну, типо проигрыш')
# else:
#     try:
#         for line in f:
#             ints.append(int(line))
#     except ValueError:
#         print("Тут не число, пшёл вон")
#     else: # если ошибок нет
#         print(ints)
#     finally: # ваще всегда
#         f.close()
#         print('Я закрываю фийл')