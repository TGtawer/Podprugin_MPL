import pandas as pd
import numpy as np
import random
from concurrent.futures import ProcessPoolExecutor

quan_files = 5
quan_elem = 50

def generate_file(file_num):
    data = {'category': [], 'value': []}
    for i in range(quan_elem):
        data['category'].append(random.choice(['A', 'B', 'C', 'D']))
        data['value'].append(round(random.uniform(1, 10), 2))
    
    df = pd.DataFrame(data)
    filename = f'output_{file_num}.csv'
    df.to_csv(filename, index=False)
    return filename

def process_file(filename):
    df = pd.read_csv(filename)
    results = []
    
    for category in ['A', 'B', 'C', 'D']:
        category_values = df[df['category'] == category]['value']
        median = float(np.median(category_values))
        std_dev = float(np.std(category_values))
        results.append({
            'category': category,
            'median': median,
            'std_deviation': std_dev
        })
    
    return results

def main():
    print("Генерация файлов...")
    filenames = [generate_file(i+1) for i in range(quan_files)]

    print("\nОбработка файлов...")
    all_results = []
    
    with ProcessPoolExecutor() as executor:
        results_list = list(executor.map(process_file, filenames))

    for i, results in enumerate(results_list):
        print(f"\nРезультаты для файла {i+1}:")
        for result in results:
            print(f"{result['category']}, {result['median']:.2f}, {result['std_deviation']:.2f}")
        all_results.append(results)
    
    print("\n\nМедиана медиан и отклонение:")
    
    category_medians = {'A': [], 'B': [], 'C': [], 'D': []}
    
    for results in all_results:
        for result in results:
            category_medians[result['category']].append(result['median'])
    
    final_results = []
    for category in ['A', 'B', 'C', 'D']:
        medians = category_medians[category]
        median_of_medians = float(np.median(medians))
        std_of_medians = float(np.std(medians))
        
        final_results.append({
            'category': category,
            'median_of_medians': median_of_medians,
            'std_of_medians': std_of_medians
        })
        
        print(f"{category}, {median_of_medians:.2f}, {std_of_medians:.2f}")
    
    result_df = pd.DataFrame(final_results)
    result_df.to_csv('final_results.csv', index=False)
    print("\nРезультаты сохранены в 'final_results.csv'")
    

if __name__ == "__main__":
    main()