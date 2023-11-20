# задание 1



# import files
#
#
# def read_end(lines, file):
#     if not isinstance(lines, int) or lines <= 0:
#         print("Количество строк должно быть положительным целым числом.")
#         return
#
#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             all_lines = f.readlines()
#
#             for line in all_lines[-lines:]:
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"Файл '{file}' не найден.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#
# read_end(5, 'article.txt')



# задание 2



# import os
#
# def print_reps(directory):
#     for root, dirs, files in os.walk(directory):
#         print(f"Current Directory: {root}")
#
#         for file in files:
#             print(f"File: {file}")
#         for dir in dirs:
#             print(f"Subdirectory: {dir}")
#
#         print("\n")
#
# print_reps(r'C:\Users\Самат\Desktop\venv')



# задание 3


# def longest_words(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#             words = content.split()
#             max_length = max(len(word) for word in words)
#             longest_words_list = [word for word in words if len(word) == max_length]
#
#             if len(longest_words_list) == 1:
#                 print(f"The longest word is: {longest_words_list[0]}")
#             else:
#                 print(f"The longest words are: {', '.join(longest_words_list)}")
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# file_path = 'poem.txt'
# longest_words(file_path)


