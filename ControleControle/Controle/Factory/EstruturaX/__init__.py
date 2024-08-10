

class EstruturaX:
    def __init__(self):
        self.__object_tables = [list(), list(), list(), list()]

    def get_pack_objeto(self, type_return, pos: int, object_name) -> list:
        if type_return == list:
            self.__object_tables[3].append(list())
            for x in self.__object_tables[pos]:
                for name in object_name:
                    if name in str(x):
                        self.__object_tables[3][0].append(x)
            for element in self.__object_tables[3][0]:
                for element_antigo in self.__object_tables[pos]:
                    if element == element_antigo: self.__object_tables[pos].remove(element)
            return self.__object_tables[3].pop()
        else:
            self.__object_tables[3].append(list())
            for x in self.__object_tables[pos]:
                if object_name in str(x):
                    self.__object_tables[3][0].append(x)
            for element in self.__object_tables[3][0]:
                for element_antigo in self.__object_tables[pos]:
                    if element == element_antigo: self.__object_tables[pos].remove(element)
            return self.__object_tables[3].pop()

    def remove_object_in_table(self, pos, object_name):
        for index, element in enumerate(self.__object_tables[pos]):
            if object_name in str(element): del self.__object_tables[pos][index]

    def addInTable(self, pos, object):
        self.__object_tables[pos].append(object)

    def getInTable(self, type_return, pos, object_name):
        if type_return == object:
            for index, element in enumerate(self.__object_tables[pos]):
                if object_name in str(element): return self.__object_tables[pos][index]
        elif type_return == list:
            self.__object_tables.append(list())
            for index, element in enumerate(self.__object_tables[pos]):
                if object_name in str(element): self.__object_tables[-1].append(self.__object_tables[pos][index])
            return self.__object_tables.pop()
