# Hadoop MapReduce Exercises

Collection of MapReduce exercises demonstrating distributed data processing with Hadoop on Azure HDInsight.

## 📋 Overview

This repository contains practical exercises for learning Hadoop MapReduce using Python streaming. The exercises process employee data to calculate statistics using the MapReduce paradigm.

## 🎯 Exercises

### 1. Average Salary by Department
**Location:** `Exercices/salaires_moyens_par_departement/`

Calculates the average salary for each department using MapReduce.

**Files:**
- `employees_mean_salary_mapper.py` - Mapper: extracts department and salary
- `employees_mean_salary_reducer.py` - Reducer: calculates average salary per department
- `hdfs_command_line.txt` - Hadoop streaming command for Azure HDInsight

**Algorithm:**
1. **Map phase:** Read CSV, emit `(department, salary)` pairs
2. **Shuffle phase:** Group all salaries by department
3. **Reduce phase:** Calculate average for each department

### 2. Average Experience by Department
**Location:** `Exercices/experience_moyenne_par_département/`

Calculates the average years of experience for each department.

**Files:**
- `employees_mean_experience_mapper.py` - Mapper: extracts department and experience
- `employees_mean_experience_reducer.py` - Reducer: calculates average experience per department

## 📊 Dataset

**File:** `Exercices/employees.csv`

**Structure:**
```csv
employee_id,name,age,department,salary,experience_years
1,John Doe,30,IT,65000,5
2,Jane Smith,28,HR,55000,3
...
```

**Columns:**
- `employee_id` - Unique identifier
- `name` - Employee name
- `age` - Employee age
- `department` - Department (IT, HR, Sales, Marketing, Finance, R&D)
- `salary` - Annual salary
- `experience_years` - Years of professional experience

**Size:** 10,000+ employee records

## 🚀 Running the Exercises

### Local Testing (Linux/Mac)

Test the MapReduce logic locally using pipes:

```bash
# Test salary calculation
cat Exercices/employees.csv | \
  python Exercices/salaires_moyens_par_departement/employees_mean_salary_mapper.py | \
  sort | \
  python Exercices/salaires_moyens_par_departement/employees_mean_salary_reducer.py

# Test experience calculation
cat Exercices/employees.csv | \
  python Exercices/experience_moyenne_par_département/employees_mean_experience_mapper.py | \
  sort | \
  python Exercices/experience_moyenne_par_département/employees_mean_experience_reducer.py
```

### Azure HDInsight Deployment

1. **Upload files to Azure Blob Storage:**
```bash
az storage blob upload --account-name YOUR_STORAGE --container-name YOUR_CONTAINER \
  --name data/employees.csv --file Exercices/employees.csv

az storage blob upload --account-name YOUR_STORAGE --container-name YOUR_CONTAINER \
  --name data/employees_mapper.py --file Exercices/salaires_moyens_par_departement/employees_mean_salary_mapper.py

az storage blob upload --account-name YOUR_STORAGE --container-name YOUR_CONTAINER \
  --name data/employees_reducer.py --file Exercices/salaires_moyens_par_departement/employees_mean_salary_reducer.py
```

2. **Run Hadoop streaming job:**

See `hdfs_command_line.txt` files for complete commands. Replace placeholders with your Azure storage details.

## 🛠️ Technologies

- **Hadoop Streaming** - MapReduce with non-Java languages
- **Python 3** - Mapper/Reducer implementation
- **Azure HDInsight** - Managed Hadoop cloud service
- **Azure Blob Storage (WASBS)** - Distributed file storage

## 📚 MapReduce Concepts Demonstrated

- **Mapper:** Data transformation and emission of key-value pairs
- **Reducer:** Aggregation and computation on grouped data
- **Streaming:** Using stdin/stdout for data flow
- **Distributed Processing:** Parallel execution across cluster nodes

## 🎓 Learning Objectives

- Understand MapReduce programming model
- Implement mappers and reducers in Python
- Deploy jobs to cloud infrastructure (Azure)
- Process large datasets distributively
- Calculate aggregations (average, sum, count)

## 📝 License

MIT License - Feel free to use for educational purposes

## 🤝 Contributing

This is an educational project. Feel free to fork and experiment with different MapReduce algorithms!

## 📧 Contact

For questions or suggestions, feel free to open an issue.
