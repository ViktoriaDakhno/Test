# import random

# file = open("Lesson1.txt", 'w')
#
# for i in range(1, 100):
#     n = random.randint(100, 1000)
#     s = str(n) + '\n'
#     file.write(s)
# file.close()

# file = open("Lesson1.txt", 'r')
#
# for line in file:
#     print(line, end='')

# file1 = open('even_numbers.txt', 'w')
# file2 = open('odd_numbers.txt', 'w')
#
# numbers = int(input("How many numbers do you want: "))
#
# def anyNumer(n):
#     even = n % 2
#     if even == 0:
#         file1.write(str(n) + "\n")
#     else:
#         file2.write(str(n) + "\n")
#
# for i in range(numbers):
#     n = int(input("Enter a number: "))
#     anyNumer(n)
#
# file1.close()
# file2.close()
#
# def sortNum():
#
#     fileRead = open("numbers.txt", "r")
#
#     if not fileRead:
#         print("File not found")
#         fileRead.close()
#         return
#
#     fileLarge = open("large_even.txt", 'w')
#     fileSmall = open("small_odd.txt", 'w')
#     fileOther = open("other_numbers.txt", 'w')
#
#     lines = fileRead.readlines()
#
#     if not lines in fileRead:
#         fileRead.close()
#
#     numbers = []
#     for line in lines:
#         num = line.split()
#         for i in num:
#             numbers.append(int(i))
#
#     numbers.sort()
#
#     for i in range(0, len(numbers)):
#         if int(numbers[i]) % 2 == 0 and int(numbers[i]) > 50:
#             fileLarge.write(str(numbers[i]) + "\n")
#         elif int(numbers[i]) % 2 != 0 and int(numbers[i]) < 20:
#             fileSmall.write(str(numbers[i]) + "\n")
#         else:
#             fileOther.write(str(numbers[i]) + "\n")
#
#     return numbers
# print(sortNum())

#Перше домашнє завдання
#
# numbers = int(input("Enter how many numbers do u want: "))
#
# if numbers < 0:
#     print("Sorry, try again")
#
# file1 = open("multiples_of_3.txt","w")
# file2 = open("multiples_of_5.txt","w")
# file3 = open("multiples_of_3_and_5.txt","w")
# file4 = open("other_numbers.txt","w")
#
# def anyNums():
#
#     for n in range(numbers):
#         num = int(input("Enter a number: "))
#         if num % 3 == 0:
#             file1.write(str(num) + "\n")
#         elif num % 5 == 0:
#             file2.write(str(num) + "\n")
#         elif num % 3 == 0 and num % 5 == 0:
#             file3.write(str(num) + "\n")
#         else:
#             file4.write(str(num) + "\n")
#
# anyNums()
#
# file1.close()
# file2.close()
# file3.close()
# file4.close()






