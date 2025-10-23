#!/usr/bin/env python3
import sys

current = None
total = 0.0
count = 0

for line in sys.stdin:
    department, salary = line.strip().split(",")
    salary = float(salary)

    if current and department != current:
        avg_salary = total / count
        print(f"{current}\t{avg_salary:.2f}")

        total = 0.0
        count = 0

    current = department
    total += salary
    count += 1

if current:
    avg_salary = total / count
    print(f"{current}\t{avg_salary:.2f}")