import os


class Progressbar(object):
    def __init__(self, charakter='#'):
        self.max_value = 100
        self.start_value = 0
        self.charakter = charakter
        self.value = 0
        self.value_percent = 0
        self.percent_bar_size = 0
        self.bar_size = 0
        self.message = ''

    def set_message(self, message):
        self.message = message
        self.step_to(self.value)

    def step_to(self, step):
        self.value = step - 1
        self.update()

    def update(self, n=1):
        self.calculate_size()
        self.value = self.value + n

        if self.value > self.max_value:
            print()
            raise ValueError(
                "current value '{0}' is higher then max value {1}".format(
                    self.value, self.max_value)
            )

        if self.value < self.start_value:
            self.value = self.start_value

        print(self.create_message(), end='')
        print(self.create_bar(), end='')
        print(self.create_percent_bar(), end='\r')

        if self.value == self.max_value:
            print()

    def create_message(self):
        max_line = int(self.console_width - self.bar_size -
                       self.percent_bar_size)

        return "{0:<{max_line}.{max_line}}".format(
            self.message, max_line=max_line
        )

    def create_percent_bar(self):
        return ' {percent:<3}%'.format(percent=self.value)

    def create_bar(self):
        bar = self.charakter * int(self.value * self.bar_size / self.max_value)

        return "[{0:{bar_size}}]".format(
            bar, bar_size=self.bar_size
        )

    def calculate_size(self):
        self.console_width = int(os.popen('stty size', 'r').read().split()[1])
        self.bar_size = int(self.console_width / 3)
        self.percent_bar_size = len(self.create_percent_bar()) + 2


def example():
    import time

    bar = Progressbar()
    for i in range(0, 100):
        time.sleep(0.02)
        bar.update()

    bar.step_to(0)
    time.sleep(2)

    bar.step_to(40)
    time.sleep(2)

    bar.set_message('This is a message')
    time.sleep(3)
    bar.set_message('New Message arrived')
    time.sleep(3)

    bar.step_to(80)
    time.sleep(4)

    bar.step_to(100)


if __name__ == '__main__':
    example()
