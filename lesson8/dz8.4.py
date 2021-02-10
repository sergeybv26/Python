if __name__ == '__main__':
    class Warehouse:
        pass

    class OfficeEquipment:
        def __init__(self, firmware, ser_number, paper_format):
            self.firmware = firmware
            self.ser_number = ser_number
            self.paper_format = paper_format

    class Printer(OfficeEquipment):
        def __init__(self, firmware, ser_number, paper_format, print_color):
            super().__init__(firmware, ser_number, paper_format)
            self.print_color = print_color

    class Scanner(OfficeEquipment):
        def __init__(self, firmware, ser_number, paper_format, type_scan):
            super().__init__(firmware, ser_number, paper_format)
            self.type_scan = type_scan

    class Xerox(OfficeEquipment):
        def __init__(self, firmware, ser_number, paper_format, copy_speed):
            super().__init__(firmware, ser_number, paper_format)
            self.copy_speed = copy_speed
