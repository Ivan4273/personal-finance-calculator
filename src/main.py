"""
Калькулятор личных финансов.
Консольное приложение для учёта доходов и расходов.
"""

from datetime import datetime


class FinanceCalculator:
    """Класс для управления доходами и расходами."""

    def __init__(self):
        """Инициализация: пустой список операций."""
        self.operations = []

    def add_income(self, amount, category, date):
        """Добавить доход."""
        self.operations.append({
            'type': 'income',
            'amount': amount,
            'category': category,
            'date': date
        })
        print(f"✅ Доход добавлен: {amount} руб., категория \"{category}\"")

    def add_expense(self, amount, category, date):
        """Добавить расход."""
        self.operations.append({
            'type': 'expense',
            'amount': amount,
            'category': category,
            'date': date
        })
        print(f"✅ Расход добавлен: {amount} руб., категория \"{category}\"")

    def get_balance(self):
        """Текущий баланс (доходы − расходы)."""
        income = sum(op['amount'] for op in self.operations if op['type'] == 'income')
        expense = sum(op['amount'] for op in self.operations if op['type'] == 'expense')
        return income - expense

    def show_all_operations(self):
        """Показать список всех операций."""
        if not self.operations:
            print("📭 Операций пока нет.")
            return

        print("\n📋 Список операций:")
        print("-" * 60)
        for i, op in enumerate(self.operations, 1):
            sign = "+" if op['type'] == 'income' else "−"
            print(f"{i}. [{op['date']}] {sign}{op['amount']} руб. — {op['category']}")
        print("-" * 60)

    def show_balance(self):
        """Показать баланс."""
        balance = self.get_balance()
        if balance > 0:
            print(f"💰 Баланс: +{balance} руб. (профицит)")
        elif balance < 0:
            print(f"💸 Баланс: {balance} руб. (дефицит)")
        else:
            print(f"⚖️  Баланс: {balance} руб.")


def read_amount():
    """Запросить у пользователя сумму (с валидацией)."""
    while True:
        try:
            amount = float(input("Введите сумму: "))
            if amount <= 0:
                print("⚠️  Сумма должна быть положительной.")
                continue
            return amount
        except ValueError:
            print("⚠️  Введите число, например: 1500")


def read_date():
    """Запросить дату с валидацией формата ДД.ММ.ГГГГ."""
    while True:
        date_str = input("Введите дату (ДД.ММ.ГГГГ): ")
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
            return date_str
        except ValueError:
            print("⚠️  Неверный формат. Пример: 01.10.2026")


def print_menu():
    """Показать главное меню."""
    print("\n" + "=" * 40)
    print("=== Калькулятор личных финансов ===")
    print("=" * 40)
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Показать все операции")
    print("4. Показать баланс")
    print("0. Выход")
    print("=" * 40)


def main():
    """Главная функция: цикл меню."""
    calc = FinanceCalculator()

    print("Добро пожаловать в Калькулятор личных финансов!")

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            amount = read_amount()
            category = input("Введите категорию: ").strip() or "Без категории"
            date = read_date()
            calc.add_income(amount, category, date)

        elif choice == '2':
            amount = read_amount()
            category = input("Введите категорию: ").strip() or "Без категории"
            date = read_date()
            calc.add_expense(amount, category, date)

        elif choice == '3':
            calc.show_all_operations()

        elif choice == '4':
            calc.show_balance()

        elif choice == '0':
            print("👋 До свидания!")
            break

        else:
            print("⚠️  Неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main()