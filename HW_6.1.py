####################
# Author: Kefa
# Date: 25.11
# system information
####################
from platform import python_version, architecture, processor


FILE_NAME = "Your system info.txt"


def py_v():
    """
    Указывает на версию Python, установленную в системе
    """
    return "Your python version: {}".format(python_version())


def proc():
    """
    Определяет процессор системы
    """
    return "Your processor: {}".format(processor())


def os_architecture():
    """
    Определяет разрядность операционной системы
    """
    bits, linkage = architecture()
    return bits


def write_to_text_file():
    """
    Запись всех данных о системе в файл
    """
    file = open(FILE_NAME, "w")
    file.write("Your system info:\n Python version: {} \n Your architecture: {} \n Your processor: {}".format(
            python_version(),
            os_architecture(),
            processor()
        )
    )
    file.close()
    print("All data about your system has been written to a file {}".format(FILE_NAME))


def file_read():
    """
    Вывод информации в файле
    """
    file = open(FILE_NAME, "r")
    data = file.read()
    file.close()
    print("Data from {}\n".format(FILE_NAME), data)


while True:  # Выбор операции
    u_ch = input(
        "\n\n"
        "Select operation and enter the letter : \n "
        "v- python version \n "
        "a- os architecture \n "
        "p- processor, \n "
        "w- write all data to a file \n "
        "r- read data from a file \n "
        "e- exit \n"
    )

    if u_ch == "e" or u_ch == "exit":
        break
    elif u_ch == "v":
        print(py_v())
    elif u_ch == "a":
        print(os_architecture())
    elif u_ch == "p":
        print(proc())
    elif u_ch == "w":
        write_to_text_file()
    elif u_ch == "r":
        file_read()
    else:
        print("Incorrect data specified")

