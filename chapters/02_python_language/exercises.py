# -- Exercises --#
# Exercise 1: Functions


def calc(x, y, operation="+"):
    if operation == "+":
        return x + y
    elif operation == "*":
        return x * y
    elif operation == "-":
        return x - y
    else:
        return "Error: invalid operation"


print(calc(4, 5, "*"))  # → 20
print(calc(3, 5))  # → 8 (par défaut "+")
print(calc(10, 2, "-"))  # → 8
print(calc(1, 2, "hello"))  # → "Error: invalid operation"


# Exercise 2: Functions + list + loop
def dedup_adjacent(seq):
    """Réduit les doublons adjacents: [1,2,2,3,2] -> [1,2,3,2]."""
    result = []
    first = True
    last = None
    for item in seq:
        if first or item != last:
            result.append(item)
            last = item
            first = False
    return result


def dedup_all(seq):
    """Supprime tous les doublons en conservant l'ordre: [1,2,2,3,2] -> [1,2,3]."""
    seen = {}
    result = []
    for item in seq:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result


# Exercise 3 File I/O (compter les mots d'UN fichier)
import re

_WORD_RE = re.compile(r"\w+", re.UNICODE)


def count_words_in_text(text):
    counts = {}
    for w in _WORD_RE.findall(text):
        w = w.lower()
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts


def count_words_in_file(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    return count_words_in_text(text)


# Exercise 4: OOP


class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = int(years_of_service)

    def salary(self):
        return 1500 + 100 * self.years_of_service


class Manager(Employee):
    def salary(self):
        return 2500 + 120 * self.years_of_service


def build_employee_db():
    return {
        "lucy": Employee("lucy", 3),
        "john": Employee("john", 1),
        "julie": Manager("julie", 10),
        "paul": Manager("paul", 3),
    }


def payroll_rows(db):
    rows = []
    for name in db:
        rows.append((name, db[name].salary()))
    # tri alphabétique par nom sans libs externes
    rows.sort(key=lambda x: x[0].lower())
    return rows


def print_payroll_table(db):
    rows = payroll_rows(db)
    name_w = len("name")
    sal_w = len("salary")
    for n, s in rows:
        if len(n) > name_w:
            name_w = len(n)
        if len(str(s)) > sal_w:
            sal_w = len(str(s))

    print("name".ljust(name_w), " ", "salary".rjust(sal_w), sep="")
    print("-" * name_w, " ", "-" * sal_w, sep="")
    for n, s in rows:
        print(n.ljust(name_w), " ", str(s).rjust(sal_w), sep="")


# Démo rapide si lancé seul
if __name__ == "__main__":
    # 2.16.1
    print(calc(4, 5, "*"))  # 20
    print(calc(3, 5))  # 8
    print(calc(1, 2, "x"))  # Error: invalid operation

    # 2.16.2
    print(dedup_adjacent([1, 2, 2, 3, 2]))  # [1, 2, 3, 2]
    print(dedup_all([1, 2, 2, 3, 2]))  # [1, 2, 3]

    # 2.16.3.1
    # print(count_words_in_file("license.txt"))

    # 2.16.4
    db = build_employee_db()
    print_payroll_table(db)
