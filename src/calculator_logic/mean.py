from src.calculator_logic.calculation_result import CalculationResult


def calculate_mean(num_list):
    result = CalculationResult()
    if len(num_list) == 0:
        result.error = "Value Error"
        return result
    amount = 0
    total = 0
    for num in num_list:
        amount += 1
        total += num
    result.result = total / num
    result.is_success = True
    result.operation =