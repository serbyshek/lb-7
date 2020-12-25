#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, содержащие введенное с клавиатуры слово.

if __name__ == '__main__':
    with open('text.txt', 'r', encoding="utf8") as f:
        text = f.read().upper()

    text = text.replace("!", ".")
    text = text.replace("?", ".")

    sentences = text.split(".")

    c = input('Введите слово которое желаете найти').upper()

    for sentence in sentences:
        if c in sentence:
            print(sentence)