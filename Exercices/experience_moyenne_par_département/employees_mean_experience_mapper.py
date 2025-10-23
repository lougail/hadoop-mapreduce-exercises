#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    employee_id, name, age, department, salary, experience_years = line.split(",")
    print(f"{department}, {salary}")