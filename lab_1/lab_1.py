import pandas
import random

quan_elem = 50
quan_files = 5

def get_generated_file(quan_elem_into_data):
    data = {'category': [], 'value' : []}
    for i in range(quan_elem_into_data):
        data['category'].append(['A', 'B', 'C', 'D'][random.randrange(4)])
        data['value'].append(round(random.uniform(1, 10), 2))
    df = pandas.DataFrame(data)
    print(df)
    return df

def get_median(arr):
    sum = 0
    for elem in arr:
        sum += elem
    return round(sum / len(arr), 2)

def get_proc_file(quan_elem_into_data, file):
    df_csv = pandas.read_csv(file)
    category_dict = {'A' : [], 'B' : [], 'C' : [], 'D' : []}
    for i in range(quan_elem_into_data):
        category_dict[f'{df_csv['category'][i]}'].append(df_csv['value'][i])

    median_dict = {
        'A' : get_median(category_dict['A']),
        'B' : get_median(category_dict['B']),
        'C' : get_median(category_dict['C']),
        'D' : get_median(category_dict['D'])
    }

    new_data = {'category': df_csv['category'], 'median' : [], 'deviation' : []}
    for i in range(quan_elem_into_data):
        new_data['median'].append(median_dict[new_data['category'][i]])
        new_data['deviation'].append(abs(new_data['median'][i] - df_csv['value'][i]))
    df = pandas.DataFrame(new_data)
    print(df)

    median_of_medians = 0
    for key in median_dict:
        median_of_medians += median_dict[key]
    median_of_medians = round(median_of_medians / len(median_dict.keys()), 2)

    final_data = {'category': df_csv['category'], 'median_of_medians' : [], 'deviation_of_medians' : []}
    for i in range(quan_elem_into_data):
        final_data['median_of_medians'].append(median_of_medians)
        final_data['deviation_of_medians'].append(abs(new_data['median'][i] - median_of_medians))
    df = pandas.DataFrame(final_data)
    print(df)
    df.to_csv(file, index=False)

for i in range(quan_files):
    get_generated_file(50).to_csv(f'output_{i + 1}.csv', index=False)
    get_proc_file(50, f'output_{i + 1}.csv')


