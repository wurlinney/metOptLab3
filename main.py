import sympy as sp

# Переменные и множители Лагранжа
x, y, l1, l2 = sp.symbols('x y l1 l2', real=True)

# Целевая функция
f = x**2 + 3*y**2

# Ограничения
g1 = x**2 + y**2 - 1
g2 = (x - 1)**2 + (y - 1)**2 - 2

# Уравнения стационарности (градиент Лагранжиана = 0)
# L = f + l1*g1 + l2*g2
eq1 = sp.diff(f, x) + l1 * sp.diff(g1, x) + l2 * sp.diff(g2, x)  # dL/dx = 0
eq2 = sp.diff(f, y) + l1 * sp.diff(g1, y) + l2 * sp.diff(g2, y)  # dL/dy = 0

# Ограничения (g1 = 0, g2 = 0)
eq3 = g1
eq4 = g2

# Решаем систему уравнений
solutions = sp.solve((eq1, eq2, eq3, eq4), (x, y, l1, l2), dict=True)

print("Найденные стационарные точки (x, y) и множители Лагранжа (l1, l2):")
for sol in solutions:
    x_val = sp.simplify(sol[x])
    y_val = sp.simplify(sol[y])
    l1_val = sp.simplify(sol[l1])
    l2_val = sp.simplify(sol[l2])
    f_val = sp.simplify(f.subs({x: x_val, y: y_val}))
    print(f"x = {x_val}, y = {y_val}, l1 = {l1_val}, l2 = {l2_val}, f(x,y) = {f_val}")

# Определим минимум/максимум по значению f
print("\nКлассификация по значению функции:")
values = []
for sol in solutions:
    x_val = sp.simplify(sol[x])
    y_val = sp.simplify(sol[y])
    f_exact = sp.simplify(f.subs({x: x_val, y: y_val}))  # точное выражение
    f_num = sp.N(f_exact)  # численное значение только для сортировки
    values.append((f_num, f_exact, x_val, y_val))

# Сортировка по численному значению f
values_sorted = sorted(values, key=lambda t: t[0])

for i, (f_num, f_exact, x_val, y_val) in enumerate(values_sorted):
    kind = "минимум" if i == 0 else "максимум"
    print(f"{kind}: f = {f_exact}, при x = {x_val}, y = {y_val}")
