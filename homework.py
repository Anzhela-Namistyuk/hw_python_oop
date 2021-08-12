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
        if date is not None:
            moment = dt.datetime.strptime(date, '%d.%m.%Y')
            self.date = moment.date()  # переводит строку в формат даты
        else:
            self.date = dt.date.today()  # записываем в свойство дату today()


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
        today_stats = 0
        today = dt.date.today()
        for record in self.records:
            if record.date == today:
                today_stats += record.amount
        return today_stats

    def get_week_stats(self) -> float:
        """
        Считать, сколько калорий получено
        или денег потрачено за последние 7 дней.
        """
        week_stats = 0
        today = dt.date.today()
        week_start = today - dt.timedelta(days=7)
        for record in self.records:
            if week_start <= record.date <= today:
                week_stats += record.amount
        return week_stats


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
        converter = {
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'rub': ('руб', 1)
        }
        spend_today = self.get_today_stats()
        cash_remain_rub = self.limit - spend_today
        name_currency, rate_currency = converter[currency]
        rest = round(abs(cash_remain_rub) / rate_currency, 2)
        if cash_remain_rub > 0:
            return f'На сегодня осталось {rest} {name_currency}'
        elif cash_remain_rub == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {rest} {name_currency}'


class CaloriesCalculator(Calculator):
    """Калькулятор калорий."""
    def get_calories_remained(self) -> str:
        """Возвращает ответ - остаток калорий на сегодня."""
        calories_today = self.get_today_stats()
        calories_remained = self.limit - calories_today
        if calories_today < self.limit:
            return 'Сегодня можно съесть что-нибудь ещё, но с общей' \
                   f' калорийностью не более {calories_remained} кКал'
        elif calories_today >= self.limit:
            return 'Хватит есть!'
