#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6 Файлы и исключения
print('6 Файлы и исключения')
# 6.1 Введение в файловый ввод и вывод
print('6.1 Введение в файловый ввод и вывод')
# Когда программе нужно сохранить данные для дальнейшего использования, она пишет эти данные в файл. Позднее их можно
# прочитать из файла.
# Программисты обычно называют процесс сохранения данных в файле записью данных в файл. Термин "файл вывода"
# используется для файла, в который данные сохраняются. Он имеет такое название, потому что программа помещает в него
# выходные данные. Процесс извлечения данных из файла называется чтением данных из файла. Когда порция данных
# считывается из файла, она копируется из файла в ОЗУ, где на нее ссылается переменная. Термин "файл ввода" используется
# для файла, из которого данные считываются. Он называется так потому, что программа извлекает входные данные из этого
# файла.
# Когда в программе используется файл, всегда требуется выполнить три шага.
# 1. Открыть файл. В процессе открытия файла создается связь между файлом и программой. Открытие файла вывода обычно
# создает файл на диске и позволяет программе записать в него данные. Открытие файла ввода позволяет программе прочитать
# данные из файла.
# 2. Обработать файл. На этом шаге данные либо записываются в файл (если это файл вывода), либо считываются из файла
# (если это файл ввода).
# 3. Закрыть файл. Когда программа закончила использовать файл, его нужно закрыть. Эта операция разрывает связь файла с
# программой.

# Типы файлов.
# Существует два типа файлов: текстовые и двоичные. Текстовый файл содержит данные, которые были закодированы в виде
# текста при помощи такой схемы кодирования, как ASCII или Юникод. Даже если файл содержит числа, они в файле хранятся
# как набор символов. В результате файл можно открыть и просмотреть в текстовом редакторе, таком как Блокнот. Двоичный
# файл содержит данные, которые не были преобразованы в текст. Данные, которые помещены в двоичный файл, предназначены
# только для чтения программой, и значит, такой файл невозможно просмотреть в текстовом редакторе.

# Методы доступа к файлам.
# Большинство языков программирования обеспечивает два разных способа получения доступа к данным, хранящимся в файле:
# последовательный доступ и прямой доступ. Во время работы с файлом с последовательным доступом происходит
# последовательное обращение к данным, с самого начала файла и до его конца. Если требуется прочитать порцию данных,
# которая размещена в конце файла, придется прочитать все данные, которые идут передней, - перескочить непосредственно к
# нужным данным не получится.
# Во время работы с файлом с прямым доступом (который также называется файлом с произвольным доступом) можно
# непосредственно перескочить к любой порции данных в файле, не читая данные, которые идут перед ней. Это подобно тому,
# как работает проигрыватель компакт-дисков или MP3-плеер. Можно прямиком перескочить к любой песне, которую нужно
# прослушать.

# Имена файлов и файловые объекты.
# Для того чтобы программа работала с файлом, находящимся на диске компьютера, она должна создать в оперативной памяти
# файловый объект. Файловый объект - это программный объект, который связан с определенным файлом и предоставляет
# программе методы для работы с этим файлом. В программе на файловый объект ссылается переменная.
# Она используется для осуществления любых операций, которые выполняются с файлом.

# Открытие файла.
# В Python функция open применяется для открытия файла. Она создает файловый объект и связывает его с файлом на диске.
# Вот общий формат применения функции open:
# файловая_переменная = open(имя_файла, режим)
# Здесь файловая_переменная - это имя переменной, которая ссылается на файловый объект; имя_файла - это строковый
# литерал, задающий имя файла; режим - это строковый литерал, задающий режим доступа (чтение, запись и т. д.), в котором
# файл будет открыт.
# Некоторые режимы доступа к файлам в Python
# Режим Описание
# 'r'   Открыть файл только для чтения. Файл не может быть изменен, в него нельзя записать
# 'w'   Открыть файл для записи. Если файл существует, то стереть содержимое. Если файл не существует, то создать
# 'a'   Открыть файл, в который будет выполнена запись. Все записываемые в файл данные будут добавлены в его конец.
#       Если файл не существует, то создать его
# Например, предположим, что файл customers.txt содержит данные о клиентах, и мы хотим его открыть для чтения. Вот
# пример вызова функции open:
# customer_file = open('customers.txt', 'r')
# Напомним, что при использовании режима 'w' на диске создается файл. Если при открытии файла с указанным именем он уже
# существует, то содержимое существующего файла будет удалено.

# Указание места расположения файла.
# Когда в функцию open передается имя файла, которое в качестве аргумента не содержит путь, интерпретатор Python исходит
# из предположения, что место расположения файла такое же, что и у программы. Например, предположим, что программа
# расположена на компьютере, работающем под управлением Windows, в папке C:\Users\Documents\Python. Если программа
# выполняется, и она исполняет инструкцию:
# test_file = open('test.txt', 'w')
# то файл test.txt создается в той же папке. Если требуется открыть файл в другом месте расположения, можно указать путь
# и имя файла в аргументе, который передается в функцию open. Если указать путь в строковом литерале (в особенности на
# компьютере под управлением Windows), следует снабдить строковый литерал префиксом в виде буквы r. Вот пример:
# test_file = open(r'C:\Users\temp\test.txt', 'w')
# Эта инструкция создает файл test.txt в папке C:\Users\temp. Префикс r указывает на то, что строковый литерал является
# неформатированным. В результате этого интерпретатор Python рассматривает символы обратной косой черты как обычные
# символы. Без префикса r интерпретатор предположит, что символы обратной косой черты являются частью экранированных
# последовательностей, и произойдет ошибка.

# Запись данных в файл.
# Метод - это функция, которая принадлежит объекту и выполняет некоторую операцию с использованием этого объекта. После
# открытия файла для выполнения операций с файлом используются методы файлового объекта.
# Например, файловые объекты имеют метод write(), который применяется для записи данных в файл. Вот общий формат вызова
# метода write():
# файловая_переменная.write(строковое_значение)
# В данном формате файловая_переменная - это переменная, которая ссылается на файловый объект, строковое_значение -
# символьная последовательность, которая будет записана в файл. Файл должен быть открыт для записи (с использованием
# режима 'w' или 'a'), либо произойдет ошибка.
# После того как программа закончила работать с файлом, она должна закрыть его. Это действие разрывает связь программы с
# файлом. В некоторых системах невыполнение операции закрытия файла вывода может вызвать потерю данных. Это происходит
# потому, что данные, которые пишутся в файл, сначала пишутся в буфер, т. е. небольшую "область временного хранения" в
# оперативной памяти. Когда буфер полон, система пишет содержимое буфера в файл. Этот прием увеличивает
# производительность системы потому, что запись данных в оперативную память быстрее их записи на диск. Процесс закрытия
# файла вывода записывает любые несохраненные данные, которые остаются в буфере, в файл.
# В Python для закрытия файла применяется метод close() файлового объекта.
# В программе в файле file_write.py приведен законченный код на Python, который открывает файл вывода, пишет в него
# данные и затем его закрывает.

# Чтение данных из файла.
# Если файл был открыт для чтения (с помощью режима 'r'), то для чтения всего его содержимого в оперативную память
# применяют метод файлового объекта read(). При вызове метода read() он возвращает содержимое файла в качестве
# строкового значения. Например, в программе в файле file_read.py показано применение метода read() для чтения
# содержимого файла philosophers.txt, который мы создали ранее.
# В Python для чтения строкового значения из файла применяется метод readline(). (Строка файла представляет собой
# символьную последовательность, завершающуюся символом \n). Этот метод возвращает строку файла как символьную
# последовательность, включая \n. В программе в файле line_read.py показано применение метода readline() для построчного
# чтения содержимого файла philosophers.txt.
# Если последняя строка в файле не будет заканчиваться на \n, то метод readline() вернет символьную последовательность
# без \n.

# Конкатенация символа новой строки со строковым значением.
# В большинстве случаев записанные в файл значения данных являются не строковыми литералами, а значениями в оперативной
# памяти, на которые ссылаются переменные. Это будет в случае программы, которая предлагает пользователю ввести данные и
# затем записывает эти данные в файл. Когда программа записывает введенные пользователем данные в файл, обычно перед их
# записью необходимо в данные добавить, или конкатенировать, экранированную последовательность \n. В результате каждая
# порция данных записывается в отдельной строке файла. В программе в файле write_names.py показано, как это делается.

# Чтение строкового значения и удаление из него символа новой строки.
# Иногда возникают сложности из-за символа \n, который появляется в конце строковых значений, возвращаемых из метода
# readline().
# Символ \n отделяет сохраненные в файле значения друг от друга. Однако в ряде случаев возникает необходимость удалить
# \n из строкового значения после того, как оно прочитано из файла. В Python каждое значение со строковым типом имеет
# метод rstrip(), который удаляет, или "отсекает", определенные символы с конца строкового значения. (Имя метода
# rstrip() говорит о том, что он отсекает символы с правой стороны строкового значения.)
# Приведенный ниже фрагмент кода демонстрирует пример использования метода rstrip().
name = 'Джоанна Менчестер\n'
name = name.rstrip('\n')
# В программе в файле strip_newline.py представлен еще один пример кода, который читает и выводит на экран содержимое
# файла philosophers.txt. Здесь применяется метод rstrip() для удаления символа \n из прочитанных из файла строковых
# значений перед тем, как они будут выведены на экран. В результате этого дополнительные пустые строки в выводе не
# появляются.

# Дозапись данных в существующий файл.
# Когда для открытия файла вывода используется режим 'w', и файл с указанным именем уже на диске существует, имеющийся
# файл будет удален, и будет создан новый пустой файл с тем же именем. Иногда есть необходимость оставить существующий
# файл и добавить в его текущее содержимое новые данные. В этом случае новые данные дописываются в конец данных, которые
# уже имеются в файле.
# В Python режим 'a' используется для открытия файла вывода в режиме дозаписи, то есть:
# - если файл уже существует, то он не будет стерт; если файл отсутствует, он будет создан;
# - когда данные пишутся в файл, они будут дописываться в конец текущего содержимого файла.
# Например, допустим, что файл friends.txt содержит приведенные ниже имена, при этом каждое имя расположено на отдельной
# строке:

# Запись и чтение числовых данных.
# Строковые значения могут записываться в файл непосредственно методом write(), однако числа перед их записью должны
# быть преобразованы в строковый тип. Python имеет встроенную функцию str, которая преобразует значение в строковый тип.
# В программе в файле write_numbers.py приведен пример использования функции str для преобразования числового значения в
# строковое и записи получившегося строкового значения в файл.


# 6.2 Применение циклов для обработки файлов
print('6.2 Применение циклов для обработки файлов')
# Файлы обычно содержат большие объемы данных, и в программах, как правило, применяется цикл, в котором обрабатываются
# данные, хранящиеся в файле.
# В некоторых программах используются файлы для хранения лишь незначительных объемов данных. Вместе с тем файлы, как
# правило, предназначены для хранения больших коллекций данных. Когда в программе используется файл для записи или
# чтения большого объема данных, то, как правило, задействуется цикл. Например, взгляните на программу в файле
# write_sales.py. Она получает от пользователя суммы продаж за несколько дней и записывает эти суммы в файл sales.txt.
# Пользователь задает количество дней, за которые ему нужно ввести данные о продажах. В демонстрационном выполнении
# программы пользователь вводит суммы продаж за пять дней.

# Чтение файла в цикле и обнаружение конца файла.
# Довольно часто программа должна читать содержимое файла, не зная количества хранящихся в файле значений.
# В Python метод readline() возвращает пустое строковое значение (''), когда он пытается прочитать за пределами конца
# файла. Это позволяет написать цикл while, который определяет, когда был достигнут конец файла.

# Применение цикла for для чтения строк.
# Язык Python позволяет писать цикл for, автоматически читающий строки в файле без проверки какого-либо особого условия,
# которое сигнализирует о конце файла. Этот цикл не требует операции первичного чтения и автоматически останавливается,
# когда достигнут конец файла. Когда требуется просто последовательно прочитать все строки файла, этот подход проще и
# изящнее, чем написание цикла while, который явным образом выполняет проверку условия конца файла. Вот общий формат
# такого цикла:
# for переменная in файловый_объект:
#   инструкция
#   инструкция
#   ...
# В данном формате переменная - это имя переменной, файловый_объект - это переменная, которая ссылается на файловый
# объект. Данный цикл будет выполнять одну итерацию для каждой строки в файле. Во время первой итерации цикла переменная
# будет ссылаться на первую строку в файле (как на символьную последовательность), во время второй итерации она будет
# ссылаться на вторую строку и т. д. В программе в файле read_sales2.py продемонстрирована работа этого цикла. Здесь
# читаются и показываются все значения из файла sales.txt.


# 6.3 Обработка записей
print('6.3 Обработка записей')
# Сохраненные в файле данные часто организованы в виде записей. Запись - это полный набор данных об объекте, а поле -
# это отдельная порция данных в записи.
# Когда данные пишутся в файл, они часто организованы в виде записей и полей. Запись - это полный набор данных, который
# описывает один объект данных, поле - это отдельная порция данных в записи.

# Добавление и вывод записей на экран.

# Изменение записей.
# Во время работы с файлом с последовательным доступом приходится копировать весь файл всякий раз, когда изменяется одно
# значение в нем. Как можно предположить, этот подход неэффективен, в особенности если файл большой. Более подходящим
# подходом к работе с крупными объемами данных является использование базы данных.

# Удаление записей.
# Во время работы с файлом с последовательным доступом приходится копировать весь файл всякий раз, когда удаляется одно
# значение из файла. Как уже упоминалось ранее, этот подход неэффективен, в особенности если файл объемный. Существуют
# другие, более продвинутые методы, в частности работа с файлами с прямым доступом, которые намного эффективнее.


# 6.4 Исключения
print('6.4 Исключения')
# Исключение - это ошибка, которая происходит во время работы программы, приводящая к ее внезапному останову. Для
# корректной обработки исключений используется инструкция try/except.
# Исключение - это ошибка, которая происходит во время работы программы. В большинстве случаев исключение приводит к
# внезапному останову программы. Например, взгляните на программу в файле division.py. Она получает от пользователя два
# числа и делит первое число на второе. Однако в демонстрационном выполнении программы произошло исключение, потому что
# в качестве второго числа пользователь ввел 0. (Деление на 0 вызывает исключение, потому что оно математически
# невозможно.)
# Длинное сообщение об ошибке, показанное в демонстрационном выполнении, называется отчетом об обратной трассировке.
# Обратная трассировка предоставляет информацию относительно одного или нескольких номеров строк, которые вызвали
# исключение. (Когда исключение происходит, программисты говорят, что исключение было вызвано, или "поднято".) Последняя
# строка сообщения об ошибке показывает название вызванного исключения (ZeroDivisionError - ошибка деления на ноль) и
# краткое описание ошибки, которая привела к вызову исключения (division by zero, т. е. деление на ноль).
# Возникновение многих исключений можно предотвратить, тщательно продумывая свою программу. Например, программа в файле
# division2.py показывает, как деление на 0 может быть предотвращено простой инструкцией if. Вместо того чтобы допустить
# возникновение исключения, программа проверяет значение переменной num2 и показывает сообщение об ошибке, если ее
# значение равно 0. Это пример корректного предотвращения исключения.
# Однако некоторых исключений невозможно избежать независимо от того, насколько тщательно написана программа.
# Язык Python, как и большинство современных языков программирования, позволяет писать программный код, который
# откликается на вызванные исключения и препятствует внезапному аварийному останову программы. Такой программный код
# называется обработчиком исключений и пишется при помощи инструкции try/except. Существует несколько способов написания
# инструкции try/except, но приведенный ниже общий формат показывает самый простой ее вариант:
# try:
#   инструкция
#   инструкция
#   ...
# except ИмяИсключения:
#   инструкция
#   инструкция
#   ...
# В начале данной инструкции стоит ключевое слово try, сопровождаемое двоеточием. Затем идет блок кода, который мы будем
# называть группой try. Она состоит из одной или нескольких инструкций, которые потенциально могут вызвать исключение.
# После группы try идет выражение except. Оно начинается с ключевого слова except, за которым необязательно может
# следовать имя исключения с двоеточием. Начиная со следующей строки, располагается блок инструкций, который мы будем
# именовать обработчиком.
# Во время исполнения инструкции try/except начинают исполняться инструкции в группе try. Ниже описывается, что
# происходит далее.
# - Если инструкция в группе try вызывает исключение, которое задано в выражении except ИмяИсключения, то выполняется
# обработчик, который расположен сразу после выражения except. Затем программа возобновляет выполнение инструкцией,
# которая идет сразу после инструкции try/except.
# - Если инструкция в группе try вызывает исключение, которое не задано в выражении except ИмяИсключения, то программа
# остановится и выведет сообщение об ошибке в отчете об обратной трассировке.
# - Если инструкции в группе try выполняются, не вызывая исключения, то любые выражения except и обработчики в данной
# инструкции пропускаются, и программа возобновляет исполнение инструкцией, которая идет сразу после инструкции
# try/except.
# В программе в файле gross_pay2.py показано, как пишется инструкция try/except с целью корректного отклика на
# исключение ValueError.
# Программа в файле display_file.py использует обработку исключения; она получает от пользователя имя файла и затем
# показывает содержимое файла. Программа работает при условии, если пользователь вводит имя существующего файла. Однако
# исключение будет вызвано, если указанного пользователем файла нет. Именно это и произошло в демонстрационном
# выполнении программы.
# В программе в файле display_file2.py показано, как при помощи инструкции try/except, которая корректно откликается на
# исключение IOError, можно изменить программу в файле display_file.py. Допустим, что в демонстрационном выполнении
# плохой_файл.txt не существует.

# Обработка многочисленных исключений.
# Во многих случаях программный код внутри группы try способен вызывать более одного типа исключений. Тогда необходимо
# написать выражение except для каждого типа исключения, которое вы хотите обработать. Например, программа в файле
# sales_report1.py читает содержимое файла с именем sales_data.txt. Каждая строка в файле содержит объем продаж в
# течение одного месяца, и файл имеет несколько строк. Вот содержимое файла:
# 24987.62
# 26978.97
# 32589.45
# 31978.47
# 22781.76
# 29871.44
# Программа в файле sales_report1.py читает все числа из файла и добавляет их в накапливающую переменную.

# Использование одного выражения except для отлавливания всех исключений.
# Иногда может возникнуть необходимость написать инструкцию try/except, которая просто отлавливает любое исключение,
# вызванное внутри группы try, независимо от типа исключения, и откликается одинаковым образом. Этого можно добиться,
# если в инструкции try/except написать одно выражение except, которое не задает конкретный тип исключения. В программе
# в файле sales_report2.py показан соответствующий пример.

# Вывод заданного по умолчанию сообщения об ошибке при возникновении исключения.
# Когда исключение вызвано, в оперативной памяти создается объект-исключение. Он обычно содержит заданное по умолчанию
# сообщение об ошибке, имеющее отношение к исключению. (Фактически это такое же сообщение об ошибке, которое вы видите
# на экране в конце отчета об обратной трассировке, когда исключение остается необработанным.) При написании выражения
# except можно присвоить объект-исключение переменной:
# except ValueError as err:
# Данное выражение except отлавливает исключения ValueError. Выражение, которое появляется после выражения except,
# указывает, что мы присваиваем объект-исключение переменной err. (В имени err нет ничего особенного. Это просто имя,
# которое мы выбрали для примеров. Можно использовать любое имя по своему выбору.) После этого в обработчике исключений
# можно передать переменную err в функцию print для вывода заданного по умолчанию сообщения об ошибке, которое Python
# предусматривает для этого типа ошибки.
# В программе в файле gross_pay3.py представлен пример, как это сделать.
# Если для отлавливания всех исключений, которые вызываются в выражении except, требуется иметь всего одно выражение
# except, то можно определить Exception как тип. В программе в файле sales_report3.py показан пример.

# Выражение else.
# Инструкция try/except может иметь необязательное выражение else, которое появляется после всех выражений except. Вот
# общий формат инструкции try/except с выражением else:
# try:
#   инструкция
#   инструкция
#   ...
# except ИмяИсключения:
#   инструкция
#   инструкция
#   ...
# else:
#   инструкция
#   инструкция
#   ...
# Блок инструкций после выражения else называется группой else. Инструкции в группе else исполняются после инструкций в
# группе try, только в случае если ни одно исключение не было вызвано. Если исключение вызвано, то группа esle
# пропускается. В программе в файле sales_report4.py показан пример.

# Выражение finally.
# Инструкция try/except может иметь необязательное выражение finally, которое должно появляться после всех выражений
# except. Вот общий формат инструкции try/except с выражением finally:
# try:
#   инструкция
#   инструкция
#   ...
# except ИмяИсключения:
#   инструкция
#   инструкция
#   ...
# finally:
#   инструкция
#   инструкция
#   ...
# Блок инструкций, который появляется после выражения finally, называется группой finally. Инструкции в группе finally
# всегда исполняются после инструкций в группе try и после того, как любые обработчики исключений исполнились.
# Инструкции в группе finally исполняются независимо от того, произошло исключение или нет. Цель группы finally
# состоит в том, чтобы выполнять операции очистки, такие как закрытие файлов или других ресурсов. Любой программный код,
# который написан в группе finally, будет всегда исполняться, даже если группа try вызовет исключение.

# Что если исключение не обработано?
# Необработанное исключение приведет к останову программы. Существуют две возможные ситуации, когда вызванное исключение
# остается необработанным. Первая заключается в том, что инструкция try/except не содержит выражения except, задающие
# исключение правильного типа. Вторая возможная ситуация складывается, когда исключения вызываются за пределами группы
# try. В любом случае исключение приводит к останову программы.
# В программе Python может произойти целый ряд исключений других типов. Во время разработки инструкций try/except узнать
# об исключениях, которые вам придется обрабатывать, можно, обратившись к документации Python. Она дает подробную
# информацию о каждом возможном исключении и типах ошибок, которые могут заставить их произойти.
# Еще один способ узнать об исключениях, которые могут произойти в программе, заключается в экспериментировании.
# К примеру, можно запустить программу и преднамеренно выполнить действия, которые вызовут ошибки. Наблюдая за
# выводимыми в отчете об обратной трассировке сообщениями об ошибках, можно увидеть имена вызванных исключений. И тогда
# можно написать выражения except для обработки этих исключений.