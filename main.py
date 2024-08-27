from datetime import datetime


class ShowTime:

    NB_BITS = 4
    NB_HEXA_DIGITS_IN_DICT_HEXACODES_BY_DIGITS = 5
    hexacodes_by_digits = {
        "0": 0xF999F,
        "1": 0x11111,
        "2": 0xF1F8F,
        "3": 0xF1F1F,
        "4": 0x99F11,
        "5": 0xF8F1F,
        "6": 0xF8F9F,
        "7": 0xF1111,
        "8": 0xF9F9F,
        "9": 0xF9F1F
    }
    bin_code_two_points = "01010"

    def __init__(self, time=datetime.now()):
        self._time = time

    @property
    def time(self):
        return self._time

    def get_bin_code_list_by_hexa_code(self, hexa_code):
        bin_code = self.get_bin_code_by_hexa_code(hexa_code)
        bin_code_list_by_hexa_code = [bin_code[i:i + self.NB_BITS] for i in range(0, len(bin_code), self.NB_BITS)]
        return bin_code_list_by_hexa_code

    def get_bin_code_by_hexa_code(self, hexa_code):
        # on transforme en code binaire et on enlève les 2 lettres au début
        bin_code = bin(hexa_code)[2::]
        normal_length = self.NB_HEXA_DIGITS_IN_DICT_HEXACODES_BY_DIGITS * self.NB_BITS
        # on rajoute des "0" au début de "bin_code" dans cas où le 1er code hexa de "bin_code"
        # commence par des 0, ces "0" ayant été supprimés automatiquement par la fonction "bin"
        bin_code_by_hexa_code = f"{bin_code:>0{normal_length}}"
        return bin_code_by_hexa_code

    def get_bin_code_list_by_digit(self, digit):
        hexacodes_by_digits = self.hexacodes_by_digits[digit]
        bin_code_list_by_hexa_code = self.get_bin_code_list_by_hexa_code(hexacodes_by_digits)
        return bin_code_list_by_hexa_code

    def get_bin_code_lists_by_digits(self):
        bin_code_lists_by_digits = [self.get_bin_code_list_by_digit(digit) for digit in str(self.time.hour)]
        bin_code_lists_by_digits.append(list(self.bin_code_two_points))
        bin_code_lists_by_digits.extend(self.get_bin_code_list_by_digit(digit) for digit in self.time.strftime("%M"))
        return bin_code_lists_by_digits

    def show_in_command_line(self):
        bin_code_lists_by_digits = self.get_bin_code_lists_by_digits()
        formatted_bin_code_lists_by_digits = list(zip(*bin_code_lists_by_digits))
        separator = "  "
        drawing = ""
        white_spaces = ""

        if self.time.hour < 10:
            white_spaces = " " * self.NB_BITS + separator

        for bin_code_list in formatted_bin_code_lists_by_digits:
            bin_code = white_spaces + separator.join(bin_code_list)
            drawing += bin_code.replace("1", "#").replace("0", " ") + "\n"

        print(drawing)


if __name__ == '__main__':

    date_time_list = [
        datetime(2024, 10, 10, 10, 26, 36),
        datetime(2024, 10, 10, 22, 56, 36),
        datetime(2024, 10, 10, 1, 57, 36),
        datetime(2024, 10, 10, 1, 58, 36),
        datetime(2024, 10, 10, 1, 4, 36)
    ]

    for one_date_time in date_time_list:
        show_time = ShowTime(one_date_time)
        show_time.show_in_command_line()

    show_time = ShowTime()
    show_time.show_in_command_line()