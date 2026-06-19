import os
from pyspark import SparkConf, SparkContext

def main():
    conf = SparkConf().setAppName("EmployeeProcessing").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")

    # 1. Load data and filter header
    raw_rdd = sc.textFile("employees.csv")
    header = raw_rdd.first()
    data_rdd = raw_rdd.filter(lambda line: line != header)
    
    # Parse to tuples: (id, name, department, salary)
    emp_rdd = data_rdd.map(lambda line: line.split(',')) \
                      .map(lambda parts: (int(parts[0]), parts[1], parts[2], int(parts[3])))
    emp_rdd.cache()

    print("\n" + "="*50)
    print("1. EMPLOYEES SORTED BY SALARY (DESCENDING)")
    print("="*50)
    sorted_emp = emp_rdd.sortBy(lambda x: x[3], ascending=False).collect()
    for emp in sorted_emp:
        print(f"ID: {emp[0]} | Name: {emp[1]} | Dept: {emp[2]} | Salary: {emp[3]}")

    print("\n" + "="*50)
    print("2. TOTAL SALARY BY DEPARTMENT")
    print("="*50)
    dept_salary_rdd = emp_rdd.map(lambda x: (x[2], x[3])).reduceByKey(lambda a, b: a + b)
    for dept, total in dept_salary_rdd.collect():
        print(f"Department: {dept:<10} | Total Salary: {total}")

    print("\n" + "="*50)
    print("3. SAVING TOP 3 HIGHEST-PAID EMPLOYEES TO FILE...")
    print("="*50)
    top_3_emps = emp_rdd.takeOrdered(3, key=lambda x: -x[3])
    top_3_strings = [f"{emp[0]},{emp[1]},{emp[2]},{emp[3]}" for emp in top_3_emps]
    
    output_dir = "output/top_highest_paid"
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
        
    sc.parallelize(top_3_strings).coalesce(1).saveAsTextFile(output_dir)
    print(f"Success! Top 3 employees saved inside directory: '{output_dir}/'")
    print("="*50 + "\n")

    sc.stop()

if __name__ == "__main__":
    main()