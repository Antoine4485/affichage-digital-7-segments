from datetime import datetime


class ShowTime:

    __NB_BITS = 4
    __bin_codes_by_digits = {
        "0": ["1111", "1001", "1001", "1001", "1111"],
        "1": ["0001", "0001", "0001", "0001", "0001"],
        "2": ["1111", "0001", "1111", "1000", "1111"],
        "3": ["1111", "0001", "1111", "0001", "1111"],
        "4": ["1001", "1001", "1111", "0001", "0001"],
        "5": ["1111", "1000", "1111", "0001", "1111"],
        "6": ["1000", "1000", "1111", "1001", "1111"],
        "7": ["1111", "0001", "0001", "0001", "0001"],
        "8": ["1111", "1001", "1111", "1001", "1111"],
        "9": ["1111", "1001", "1111", "0001", "0001"]
    }
    __bin_code_two_points = "01010"

    def __init__(self, time=datetime.now()):
        self.__time = time

    def __get_bin_code_lists_by_digits(self):
        bin_code_lists_by_digits = [self.__bin_codes_by_digits[digit] for digit in str(self.__time.hour)]
        bin_code_lists_by_digits.append(list(self.__bin_code_two_points))
        bin_code_lists_by_digits.extend(self.__bin_codes_by_digits[digit] for digit in self.__time.strftime("%M"))
        return bin_code_lists_by_digits

    def digital_time(self):
        bin_code_lists_by_digits = self.__get_bin_code_lists_by_digits()
        formatted_bin_code_lists_by_digits = list(zip(*bin_code_lists_by_digits))
        separator = "  "
        drawing = ""
        white_spaces = ""

        if self.__time.hour < 10:
            white_spaces = " " * self.__NB_BITS + separator

        for bin_code_list in formatted_bin_code_lists_by_digits:
            bin_code = white_spaces + separator.join(bin_code_list)
            drawing += bin_code.replace("1", "#").replace("0", " ") + "\n"

        print(drawing)


if __name__ == '__main__':

    # date_time_list = [
    #     datetime(2024, 10, 10, 10, 23, 36),
    #     datetime(2024, 10, 10, 14, 56, 36),
    #     datetime(2024, 10, 10, 8, 57, 36),
    #     datetime(2024, 10, 10, 0, 59, 36),
    # ]
    #
    # for one_date_time in date_time_list:
    #     show_time = ShowTime(one_date_time)
    #     show_time.digital_time()

    show_time = ShowTime()
    show_time.digital_time()