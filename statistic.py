# Statistical Functions
def calculate_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result



def calculate_mean(numbers):
    total = calculate_sum(numbers)
    mean = total / len(numbers)
    return mean



def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data) if len(data) > 0 else 0



def var(x):
    n = len(x)
    m = sum(x)/n
    sigma=0
    for i in x:
        sigma += (i-m)**2
    return sigma/n



def cal_variance(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(num - mean)**2 for num in numbers]
    variance = calculate_mean(squared_diff)
    return variance



def calculate_standard_deviation(data):
    return calculate_variance(data) ** 0.5



def calculate_mode(data):
    # شمارش تعداد تکرارهای هر عنصر
    counts = {}
    for value in data:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    # یافتن عنصر با بیشترین تعداد تکرار
    max_count = max(counts.values())
    mode = [key for key, value in counts.items() if value == max_count]

    return mode



def calculate_median(data):
    sorted_data = bubble_sort(data.copy())  # ایجاد یک کپی از داده و مرتب‌سازی
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[(n // 2) - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data



def calculate_percentile(data, percentile):
    sorted_data = bubble_sort(data.copy())  # ایجاد یک کپی از داده و مرتب‌سازی
    n = len(sorted_data)
    
    index = (percentile / 100) * (n - 1)
    
    if index.is_integer():
        return sorted_data[int(index)]
    else:
        lower_index = int(index // 1)
        upper_index = lower_index + 1
        lower_value = sorted_data[lower_index]
        upper_value = sorted_data[upper_index]
        return lower_value + (index - lower_index) * (upper_value - lower_value)
    


def calculate_covariance(X, Y):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    n = len(X)
    
    covariance = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / (n - 1)
    return covariance




def calculate_correlation(X, Y):
    covariance = calculate_covariance(X, Y)
    std_dev_X = calculate_standard_deviation(X)
    std_dev_Y = calculate_standard_deviation(Y)
    
    correlation = covariance / (std_dev_X * std_dev_Y)
    return correlation



def find_max_min(numbers):
    if not numbers:
        return "لیست خالی است!"
    max_num = min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num



def calculate_range(numbers):
    if not numbers:
        return "لیست خالی است!"
    
    max_num, min_num = find_max_min(numbers)
    data_range = max_num - min_num
    return data_range



def normal_distribution_pdf(x, mean, std_dev):
    exponent = -((x - mean) ** 2) / (2 * std_dev ** 2)
    pdf = 1 / (std_dev * (2 * 3.14159) ** 0.5) * (2.71828 ** exponent)
    return pdf



def count_even_odd(numbers):
    even_count = odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
