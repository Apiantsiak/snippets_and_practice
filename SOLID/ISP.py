from abc import ABC, abstractmethod


class Machine:
    def print(self, document):
        raise NotImplemented

    def fax(self, document):
        raise NotImplemented

    def scan(self, document):
        raise NotImplemented


class MultiFunctionalPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        raise NotImplemented("Printer cannot scan!")


# Refactor according to ISP

class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Scaner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        pass


class Photocopier(Printer, Scaner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


# Combo class

class MultiFunctionalDevice(Printer, Fax, Scaner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


#  Pattern Decorator

class MultiFunctionalMachine(MultiFunctionalDevice):
    def __init__(self, printer, fax, scanner):
        self.printer = printer
        self.faxer = fax
        self.scaner = scanner

    def print(self, document):
        self.printer.print(document)

    def fax(self, document):
        self.faxer.fax(document)

    def scan(self, document):
        self.scaner.scan(document)
