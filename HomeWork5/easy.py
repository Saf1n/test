__author__ = 'Сафин Ильшат'

# coding: utf-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#создание папок
import os
import shutil

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')


#удаление папок


def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(dir_path):
    print(os.getcwd())
#dir_path = os.getcwd()


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')

