from datetime import datetime
import pickle

def history(q):
    """Вспомогательная функция для печати истории добавления
    новых данных"""
    for i in q:
        print (i)

class model():
    """Класс, содержащий информацию о марке автомобиля"""
    def __init__(self, name, country, factory, adress):
        """Функция инициализации класса"""
        self._country = country
        try:
            if name.isalpha():
                self._name = name
        except AttributeError:
            raise ExError("Неверный тип данных")
        self._factory = factory
        self._adress = adress
        self.queue = []

    def change_adress(self, street):
        return self.__change_adress(street)
    def __change_adress(self, street):
        """Функция, меняющая адрес"""
        self._adress = street
        self.queue.append("When: {0} ; Operation: change adress on {1}".format(datetime.today(), street))
    def __del__(self):
        """Функция, вызываемая при удалении, печатает страну-изготовителя"""
        print(self._country)

    @property
    def FactoryAdress(self):
        """Функция, объединяющая завод и адрес в одну переменную"""
        return self.factory + " " + self.adress

    @property
    def name(self):
        ''' Возвращает имя '''
        return self._name
    @name.setter
    def name(self, new_name):
        ''' Устанавливает новое имя '''
        self._name = new_name

class car():
    """Класс, содержащий информацию о конкретном автомобиле"""
    def __init__(self, name, model, year, colour, price):
        """Функция инициализации класса"""
        self._name = name
        self._model = model
        try:
            self._year = int(year)
        except ValueError:
            raise ExError("Неверный тип данных")
        self._colour = colour
        self._price = price
        self.queue = []

    def change_price(self, nw):
        return self.__change_price(nw)
    def __change_price(self, nw):
        """Функция, меняющая цену"""
        self._price = nw
        self.queue.append("When: {0} ; Operation: change price on {1}".format(datetime.today(), nw))
    def __del__(self):
        """Функция, вызываемая при удалении, печатает название модели"""
        print(self._model)

    @property
    def full_model(self):
        """Функция, объединяющая имя, модель и год производства
        в одну переменную"""
        return self._name + " " + self._model + " " + self._year

    @property
    def name(self):
        ''' Возвращает имя '''
        return self._name
    @name.setter
    def name(self, new_name):
        ''' Устанавливает новое имя '''
        self._name = new_name

class customer():
    """Класс, содержащий информацию о покупателе"""
    def __init__(self, name2, name1, name3, passport, city, age, sx):
        """Функция инициализации класса"""
        self._name2 = name2
        self._name1 = name1
        self._name3 = name3
        self._passport = passport
        self._city = city
        try:
            self._age = int(age)
        except ValueError:
            raise ExError("Неверный тип данных")
        self._sx = sx
        self.queue = []
    def change_passport(self, passport):
        return __change_passport(passport)
    def __change_passsport (self, passport):
        self._passport = passport
    def change_age(self, age):
        return self.__change_price(age)
    def __change_age (self, age):
        self._age = age
    def __del__(self):
        """Функция, вызываемая при удалении, печатает имя"""
        print(self._name1)
    @property
    def full_name(self):
        """Функция, объединяющая фамилию, имя и отчество в одну переменную,
        заменила соответствующий метод"""
        self.queue.append("When: {0} ; Operation: name set on {1}".format(datetime.today(), self._name2 + " " + self._name1 + " " + self._name3))
        return self._name2 + " " + self._name1 + " " + self._name3

    @property
    def passport(self):
        ''' Возвращает паспорт '''
        return self._passport
    @passport.setter
    def passport(self, new_passport):
        ''' Устанавливает новое имя '''
        self._passport = new_passport

class up_customer(customer):
    """Дочерний класс customer, добавляющий id покупателя и
    возможность обновлять кол-во покупок purchases"""
    def __init__ (self, name2, name1, name3, passport, city, age, sx, id, purchases):
        """Функция инициализации класса"""
        super().__init__(name2, name1, name3, passport, city, age, sx)
        self._id = id
        self._purchases = purchases
    def up_purchases (self, new_purch):
        """Функция, устанавливающая кол-во покупок клиента"""
        self._purchases = new_purch
    def __add__ (self, add):                                    # НОВЫЙ МЕТОД @@@@@@@@@@@@@@@@@@@@@@@@
        """Функция, увеличивающая кол-во покупок клиента"""
        self._purchases += add
    def change_id (self, new_id):
        """Функция, меняющая id клиента"""
        self._id = new_id

    @property
    def purchases(self):
        ''' Возвращает кол-во покупок '''
        return self._purchases

    @purchases.setter
    def purchases(self, new_purchases):
        ''' Устанавливает новое кол-во покупок '''
        self._purchases = new_purchases

class down_customer(customer):
    """Дочерний класс customer, добавляющий возможность увидеть
    полную информацию о клиенте, а также сменить имя"""
    def __init__ (self, name2, name1, name3, passport, city, age, sx):
        """Функция инициализации класса"""
        super().__init__(name2, name1, name3, passport, city, age, sx)
        self._info = [name1, passport, age, sx, city]
    def show_info (self):
        """Функция, показывающая полную информацию о клиенте"""
        print(" Name: {0}; \n Passport: {1}; \n Age: {2}; \n Sx: {3}; \n City: {4}".format(self._info[0], self._info[1], self._info[2], self._info[3], self._info[4]))
    def change_name1(self, name1):
        """Функция, меняющая имя клиента"""
        self._name1 = name1
        self._info[0] = name1
    def name213(self, name2, name1, name3):
        """Функция, меняющая полное имя клиента"""
        self._name2 = name2
        self._name1 = name1
        self._name3 = name3
        self._info[0] = name1
    def __del__(self):
        pass

    @property
    def purchases(self):
        ''' Возвращает кол-во покупок '''
        return self._purchases

    @purchases.setter
    def purchases(self, new_purchases):
        ''' Устанавливает новое кол-во покупок '''
        self._purchases = new_purchases

class employee():
    """Класс, содержащий информацию о сотруднике"""
    def __init__(self, name2, name1, name3, experience, salary):
        """Функция инициализации класса"""
        self._name2 = name2
        self._name1 = name1
        self._name3 = name3
        self._experience = experience
        try:
            if int(salary) < 80000:
                self._salary = salary
            else:
                self._salary = 80000
        except ValueError:
            raise ExError("Неверный тип данных")
        self._queue = []
        self.number = 0
    def change_salary(self, salary):
        return self.__change_price(salary)
    def __change_salary(self, salary):
        self._salary = salary
    #def name213(self):
    #    "Функция, объединяющая фамилию, имя и отчество в одну переменную"""
    #    self.full_name = self.name2 + " " + self.name1 + " " + self.name3
    #    self.queue.append("When: {0} ; Operation: name set on {1}".format(datetime.today(), self.full_name))
    def __del__(self):
        """Функция, вызываемая при удалении, печатает имя"""
        pass
        #print(self._name1)
    @property
    def full_name(self):
        """Функция, объединяющая фамилию, имя и отчество в одну переменную,
        заменила соответствующий метод"""
        return self._name2 + " " + self._name1 + " " + self._name3

    @property
    def salary(self):
        ''' Возвращает размер зарплаты '''
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        ''' Устанавливает новый размер зарплаты '''
        self._salary = new_salary

class car_sale():
    """Класс, содержащий информацию о продаже атвомобиля"""
    def __init__(self, date, employee, car):
        """Функция инициализации класса"""
        self._date = date
        self._employee = employee
        self._car = car
        self.queue = []
    def salary_bonus(self, bonus):
        return self.__salary_bonus(bonus)
    def __salary_bonus (self, bonus):
        """Функция назначающая бонус работнику"""
        try:
            if int(bonus) < 2000:
                self._bonus = bonus
            else:
                self._bonus = 2000
        except ValueError:
            raise ExError("Неверный тип данных")
        self.queue.append("When: {0} ; Operation: set bonus on {1}".format(datetime.today(), self._bonus))

    def __add__(self, bonus):                       # НОВЫЙ МЕТОД @@@@@@@@@@@@@@@@@@@@@@@@
        """Функция, увеличивающая бонус работника"""
        self._bonus += bonus

    def __sub__(self, bonus):                       # НОВЫЙ МЕТОД @@@@@@@@@@@@@@@@@@@@@@@@
        """Функция, уменьшающая бонус работника"""
        self._bonus -= bonus

    def __del__(self):
        """Функция, вызываемая при удалении, печатает
        название проданной машины"""
        print(self._car)

    @property
    def CarDate(self):
        """Функция, объединяющая машину и дату в одну переменную"""
        return self._car + " " + self._date

    @property
    def date(self):
        ''' Возвращает дату '''
        return self._date

    @date.setter
    def date(self, new_date):
        ''' Устанавливает новую дату '''
        self._date = new_date


class ExError(Exception):
    ''' Класс исключений для класса '''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class EmployeeDatabase(object):
    def __init__(self):
        self.filename = 'employee.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database() #full name experience salary
        except:
            self.save_database()

    number = property(lambda self: self.database[self.index].number)
    full_name = property(lambda self: self.database[self.index].full_name)
    experience = property(lambda self: self.database[self.index].experience)
    salary = property(lambda self: self.database[self.index].salary)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]
    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]
    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]
    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed
    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed
    def add_account(self, data):
        data = data.split()
        emp = employee (data[0], data[1], data[2], data[3], data[4])
        if len(self.database) == 0:
            self.database[1] = [emp.full_name, emp._experience, emp._salary]
        else:
            self.database[list(self.database.keys())[-1]+1] = [emp.full_name, emp._experience, emp._salary]
        self.save_database()
    def get_account_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]
    def delete_account(self, number):
        account = self.get_account_by_number(number)
        if not account:
            raise ValueError('value does not exist')
        del self.database[number]
        self.save_database()
    def change_salary(self, number, salary):
        account = self.get_account_by_number(number)
        if not account:
            raise ValueError('value does not exist')
        account[-1] = salary
        self.save_database()


class EmployeeTerm(object):
    def __init__(self):
        self.employee_database = EmployeeDatabase()
    def printDB(self):
        d = list(self.employee_database.database.keys())
        for account in self.employee_database:
            print('account number: {0}; salary: {1}; named: {2}'.format(d[0],\
 account[-1], account[0]))
            d.pop(0)
    def run(self):
        choice  = 0
        choices = {
            1: lambda: self.printDB(),
            2: lambda: self.employee_database.add_account(input( \
                'enter data: ')),
            3: lambda: self.employee_database.delete_account(int(input( \
                'enter number: '))),
            4: lambda: self.employee_database.change_salary(int(input( \
                'enter number: ')), int(input('enter salary: ')))
        }
        while (choice != 5):
            print()
            print('1. print database')
            print('2. add account')
            print('3. delete account')
            print('4. change salary')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()


if __name__ == "__main__":
    EmployeeTerm().run()

