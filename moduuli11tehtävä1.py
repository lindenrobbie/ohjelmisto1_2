class Release:
    def __init__(self, name):
        self.name = name

    def print_details(self):
        print(f'\nJulkaisun nimi: {self.name}')


class Book(Release):
    def __init__(self, name, bookauthor, pagecount):
        super().__init__(name)
        self.bookauthor = bookauthor
        self.pagecount = pagecount

    def print_details(self):
        print(f'\nKirjan nimi: {self.name}\nKirjan tekijä: {self.bookauthor}\nSivuja: {self.pagecount}')

class Paper(Release):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_details(self):
        print(f'\nLehden nimi: {self.name}\nLehden päätoimittaja: {self.editor}')


pieces = []

pieces.append(Paper('Aku Ankka', 'Aki Hyyppä'))
pieces.append(Book('Hytti n:o 6', 'Rosa Liksom', 200))

for piece in pieces:
    piece.print_details()