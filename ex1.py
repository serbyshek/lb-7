#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text1.txt', 'r', encoding="utf8") as f:
        text1 = f.read()

    # Заменить символы конца предложения.
    text1 = text1.replace("!", ".")
    text1 = text1.replace("?", ".")

    # Удалить все многоточия.
    while ".." in text1:
        text1 = text1.replace("..", ".")

    # Разбить текст на предложения.
    sentences = text1.split(".")

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            print("{}.".format(sentence))