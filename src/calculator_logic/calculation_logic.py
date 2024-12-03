import re

from src.calculator_logic.calculation_result import CalculationResult
import math


def is_float(string):
    pattern = r"^-?\d+(\.\d+)?$"
    match = re.match(pattern, string)
    return bool(match)

def calculate_mean(num_list):
    # preq-LOGIC-5
    try:
        num_list = num_list.split('\r\n')
        for num in num_list:
            num.strip()
        while '' in num_list:
            num_list.remove('')
        if not num_list:
            raise ValueError("No numbers detected. One value per line.")
        for num in num_list:
            if len(num.split(' ')) > 1:
                raise ValueError("Multiple values detected. One value per line.")
            if not is_float(num):
                raise ValueError("Non-numeric value detected. One value per line.")
        for i in range(len(num_list)):
            num_list[i] = float(num_list[i])
        mean = sum(num_list) / len(num_list)
        return CalculationResult(mean, True, "Mean", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def calculate_sample_standard_deviation(num_list):
    #preq-LOGIC-3
    try:
        num_list = num_list.split('\r\n')
        for num in num_list:
            num.strip()
        while '' in num_list:
            num_list.remove('')
        if not num_list:
            raise ValueError("No numbers detected. One value per line.")
        for num in num_list:
            if len(num.split(' ')) > 1:
                raise ValueError("Multiple values detected. One value per line.")
            if not is_float(num):
                raise ValueError("Non-numeric value detected. One value per line.")
        for i in range(len(num_list)):
            num_list[i] = float(num_list[i])
        mean = sum(num_list) / len(num_list)
        sample_variance = sum(pow((i - mean), 2) for i in num_list) / (len(num_list)-1)
        sample_standard_deviation = math.sqrt(sample_variance)
        return CalculationResult(sample_standard_deviation, True, "Standard Deviation", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def calculate_population_standard_deviation(num_list):
    #preq-LOGIC-4
    try:
        num_list = num_list.split('\r\n')
        for num in num_list:
            num.strip()
        while '' in num_list:
            num_list.remove('')
        if not num_list:
            raise ValueError("No numbers detected. One value per line.")
        for num in num_list:
            if len(num.split(' ')) > 1:
                raise ValueError("Multiple values detected. One value per line.")
            if not is_float(num):
                raise ValueError("Non-numeric value detected. One value per line.")
        if len(num_list) == 1:
            raise ValueError("One number detected. Two or more numbers required.")
        for i in range(len(num_list)):
            num_list[i] = float(num_list[i])
        mean = sum(num_list) / len(num_list)
        population_variance = sum(pow((i - mean), 2) for i in num_list) / len(num_list)
        population_standard_deviation = math.sqrt(population_variance)
        return CalculationResult(population_standard_deviation, True, "Population Standard Deviation", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)

def calculate_zscore(input_list):
    #preq-LOGIC-6
    try:
        input_list = input_list.split('\r\n')
        while '' in input_list:
            input_list.remove('')
        if len(input_list) == 0:
            raise ValueError("No Values detected. Format is \"value,mean,standard_deviation\" on one line.")
        elif len(input_list) > 1:
            raise ValueError("Multiple lines detected. Format is \"value,mean,standard_deviation\" on one line.")
        input_list = input_list[0].split(',')
        while '' in input_list:
            input_list.remove('')
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            check = input_list[i].split(' ')
            if len(check) > 1:
                raise ValueError("Multiple values detected. Format is \"value,mean,standard_deviation\" on one line.")
            if not is_float(input_list[i]):
                raise ValueError("Non-numeric value detected. Format is \"value,mean,standard_deviation\" on one line.")
        if not len(input_list) == 3:
            raise ValueError("Format is \"value,mean,standard_deviation\" on one line.")
        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])
        value = input_list[0]
        mean = input_list[1]
        standard_deviation = input_list[2]
        if standard_deviation == 0:
            raise ValueError("Division by Zero. Standard Deviation cannot be zero.")
        zscore = (value - mean) / standard_deviation
        return CalculationResult(zscore, True, "ZScore", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)

def calculate_single_linear_regression(input_list):
    #preq-LOGIC-7
    try:
        input_list = input_list.split('\r\n')
        while '' in input_list:
            input_list.remove('')
        if len(input_list) == 0:
            raise ValueError("Empty list. Format is one \"x,y\" pair per line.")
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.match(r"^-?\d+(?:\.\d+)?, ?-?\d+(?:\.\d+)?$", input_list[i]):
                raise ValueError("Invalid Format. Format is one \"x,y\" pair per line.")
        x_values = []
        y_values = []
        for xypair in input_list:
            pair = xypair.split(',')
            x_values.append(float(pair[0]))
            y_values.append(float(pair[1]))
        if len(input_list) == 1:
            raise ValueError("One pair detected. Multiple pairs needed. Format is one \"x,y\" pair per line.")
        numerator = 0
        denominator = 0
        x_mean = sum(x_values) / len(x_values)
        y_mean = sum(y_values) / len(y_values)
        for x,y in zip(x_values, y_values):
            numerator += (x - x_mean) * (y - y_mean)
            denominator += (x - x_mean) ** 2
        slope = numerator / denominator
        intercept = y_mean - slope * x_mean
        equation = f'y = {round(slope,10)}x + {round(intercept,10)}'
        return CalculationResult(equation, True, "Single Linear Regression", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)

def calculate_y_prediction(input_list):
    #preq-LOGIC-8
    try:
        input_list = input_list.split('\r\n')
        while '' in input_list:
            input_list.remove('')
        if len(input_list) == 0:
            raise ValueError("Empty input. Format is \"x, m, b\" on one line.")
        if len(input_list) > 1:
            raise ValueError("Multiple lines detected. Format is \"x, m, b\" on one line.")
        input_list = input_list[0].split(',')
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.match(r"^-?\d+(?:\.\d+)?$", input_list[i]):
                raise ValueError("Non-Numbers detected. Format is \"x, m, b\" on one line.")
        if len(input_list) != 3:
            raise ValueError("Missing Value(s). Format is \"x, m, b\" on one line.")
        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])
        y_value = (input_list[0] * input_list[1]) + input_list[2]
        result = f'y = {y_value}'
        return CalculationResult(result, True, "Y Prediction", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)
