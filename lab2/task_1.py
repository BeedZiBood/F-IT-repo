money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

num_of_month = 0
delta = spend - salary
while money_capital > delta:
    money_capital -= delta
    num_of_month += 1
    spend *= (1 + increase)
    delta = spend - salary

print("Количество месяцев, которое можно протянуть без долгов:", num_of_month)
