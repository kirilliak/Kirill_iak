def total_salary(path):
    total_salary = 0
    num_developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
            
            average_salary = total_salary / num_developers
            return total_salary, average_salary
        
    except FileNotFoundError:
        return None, "Файл не знайдено."
    except Exception as e:
        return None, f"Сталася помилка: {e}"

def main():
    path = "path/to/salary_file.txt"
    total, result = total_salary(path)
    
    if total is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()

