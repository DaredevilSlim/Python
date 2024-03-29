#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа сохраняет последовательность, состоящую из длительностей видеоклипов, в файле video_times.txt.
def main():
    # Получить количество видеоклипов в проекте.
    num_videos = int(input('Сколько видеоклипов в проекте? '))
    # Открыть файл для записи длительностей видеоклипов.
    video_file = open('video_times.txt', 'w')
    # Получить длительность каждого видеоклипа и записать его в файл.
    print('Введите длительность каждого видеоклипа.')
    for count in range(1, num_videos + 1):
        run_time = float(input(f'Видеоклип No {count}: '))
        video_file.write(f'{run_time}\n')
    # Закрыть файл.
    video_file.close()
    print('Времена сохранены в video_times.txt.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
