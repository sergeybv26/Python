if __name__ == '__main__':
    class OwnError(Exception):
        def __init__(self, txt):
            self.txt = txt

    class Warehouse:
        def __init__(self):
            self.equipment_dict = {}

        def add_in_warehouse(self, equipment):
            self.equipment_dict.setdefault(equipment.type_eq_name(), []).append(equipment)

        def moving(self, type_equipment):
            if self.equipment_dict[type_equipment]:
                self.equipment_dict.setdefault(type_equipment).pop(0)

    class OfficeEquipment:
        def __init__(self, firmware, ser_number, paper_format):
            self.firmware = firmware
            self.ser_number = ser_number
            self.paper_format = paper_format
            self.type_eq = self.__class__.__name__

        def type_eq_name(self):
            return f'{self.type_eq}'

        def __repr__(self):
            return f'Производитель: {self.firmware}, серийный номер: {self.ser_number}, формат бумаги: {self.paper_format}'

    class Printer(OfficeEquipment):
        def __init__(self, firmware, ser_number, paper_format, print_color):
            try:
                if not ser_number.isdigit():
                    raise OwnError('Не верный серийный номер. Серийный номер должен состоять из цифр')
            except OwnError as err:
                print(err)
            else:
                super().__init__(firmware, ser_number, paper_format)
                self.print_color = print_color

    class Scanner(OfficeEquipment):
        def __init__(self, firmware, ser_number, paper_format, type_scan):
            try:
                if not ser_number.isdigit():
                    raise OwnError('Не верный серийный номер. Серийный номер должен состоять из цифр')
            except OwnError as err:
                print(err)
            else:
                super().__init__(firmware, ser_number, paper_format)
                self.type_scan = type_scan

    class Xerox(OfficeEquipment):
        def __init__(self, firmware, ser_number, paper_format, copy_speed):
            try:
                if not ser_number.isdigit():
                    raise OwnError('Не верный серийный номер. Серийный номер должен состоять из цифр')
            except OwnError as err:
                print(err)
            else:
                super().__init__(firmware, ser_number, paper_format)
                self.copy_speed = copy_speed

    warehouse = Warehouse()
    printer = Printer('Canon', '123456789', 'A3', 'wb')
    warehouse.add_in_warehouse(printer)
    printer = Printer('HP', '956423', 'A4', 'color')
    warehouse.add_in_warehouse(printer)
    scanner = Scanner('Canon', '124563', 'A4', 'планшетный')
    warehouse.add_in_warehouse(scanner)
    xerox = Xerox('Xerox', '453135', 'A4', 40)
    warehouse.add_in_warehouse(xerox)

    print(warehouse.equipment_dict)

    warehouse.moving('Printer')
    print(warehouse.equipment_dict)

    printer = Printer('Canon', '12a54sd', 'A3', 'wb')
