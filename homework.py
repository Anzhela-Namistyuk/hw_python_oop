import datetime as dt
from typing import Optional


"""Калькулятор для подсчёта денег и калорий."""


class Record:
    """
    Создание записей: amount - потраченые деньги/ количество килокалорий
    comment - коментарий, date - дата создания записи.
    """
    def __init__(self, amount: float, comment: str = 'траты',
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()  # записываем в свойство дату today()
        else:
            moment = dt.datetime.strptime(date, '%d.%m.%Y')
            self.date = moment.date()  # переводит строку в формат даты


class Calculator:
    """
    Родительский класс - калькулятор.
    Принимает один аргумент - лимит трат/калорий.
    """
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, record: Record) -> None:
        """
        Сохранят новую запись о расходах
        или о приёме пищи.
        """
        self.records.append(record)

    def get_today_stats(self) -> float:
        """
        Считать, сколько калорий получено
        или денег потрачено сегодня.
        """
        today = dt.date.today()
        return sum(record.amount for record in self.records
                   if record.date == today)

    def get_week_stats(self) -> float:
        """
        Считать, сколько калорий получено
        или денег потрачено за последние 7 дней.
        """
        today = dt.date.today()
        week_start = today - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                   if week_start <= record.date <= today)

    def get_today_remained(self) -> float:
        """Возвращает остаток денег/ каллорий."""
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    """Денежный калькулятор."""
    USD_RATE = 73.67
    EURO_RATE = 86.45

    def get_today_cash_remained(self, currency: str) -> str:
        """
        Принимать на вход обозначение валюты: одну из строк "rub", "usd"
        или "eur" и возвращает он сообщение о состоянии дневного баланса
        в этой валюте, округляя сумму до двух знаков после запятой.
        """
        cash_remain_rub = self.get_today_remained()
        if cash_remain_rub == 0:
            return 'Денег нет, держись'
        converter = {
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'rub': ('руб', 1)
        }
        name_currency, rate_currency = converter[currency]
        rest = round(abs(cash_remain_rub) / rate_currency, 2)
        if cash_remain_rub > 0:
            return f'На сегодня осталось {rest} {name_currency}'
        else:
            return f'Денег нет, держись: твой долг - {rest} {name_currency}'


class CaloriesCalculator(Calculator):
    """Калькулятор калорий."""
    def get_calories_remained(self) -> str:
        """Возвращает ответ - остаток калорий на сегодня."""
        calories_remained = self.get_today_remained()
        if calories_remained <= 0:
            return 'Хватит есть!'
        else:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {calories_remained} кКал')
