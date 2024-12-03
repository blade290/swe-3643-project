from src.calculator_logic.calculation_logic import *


def test_CalculateMean_ValidList_ReturnsMean():
    #preq-UNIT-TEST-4
    input_list = "9\r\n6\r\n8\r\n5\r\n7"
    expected = 7.0
    actual = calculate_mean(input_list).result
    assert actual == expected


def test_CalculateMean_EmptyList_ReturnsError():
    #preq-UNIT-TEST-4
    input_list = ""
    expected = 'No numbers detected. One value per line.'
    actual = str(calculate_mean(input_list).error)
    assert actual == expected


def test_CalculateMean_MultipleValues_ReturnsError():
    #preq-UNIT-TEST-4
    input_list = "9 6\r\n3 4\r\n66"
    expected = 'Multiple values detected. One value per line.'
    actual = str(calculate_mean(input_list).error)
    assert actual == expected


def test_CalculateMean_NonNumeric_ReturnsError():
    #preq-UNIT-TEST-4
    input_list = "96\r\n34b\r\n66"
    expected = 'Non-numeric value detected. One value per line.'
    actual = str(calculate_mean(input_list).error)
    assert actual == expected


def test_SampleStandardDeviation_ValidList_ReturnsStandardDeviation():
    #preq-UNIT-TEST-2
    input_list = "9\r\n6\r\n8\r\n5\r\n7\r\n"
    expected = 1.5811388300841898
    actual = calculate_sample_standard_deviation(input_list).result
    assert actual == expected


def test_SampleStandardDeviation_EmptyList_ReturnsError():
    # preq-UNIT-TEST-2
    input_list = ""
    expected = 'No numbers detected. One value per line.'
    actual = str(calculate_sample_standard_deviation(input_list).error)
    assert actual == expected


def test_SampleStandardDeviation_NonNumeric_ReturnsError():
    # preq-UNIT-TEST-2
    input_list = "96\r\n34b\r\n66"
    expected = 'Non-numeric value detected. One value per line.'
    actual = str(calculate_sample_standard_deviation(input_list).error)
    assert actual == expected


def test_SampleStandardDeviation_MultipleValues_ReturnsError():
    # preq-UNIT-TEST-2
    input_list = "9 6\r\n3 4\r\n66"
    expected = 'Multiple values detected. One value per line.'
    actual = str(calculate_sample_standard_deviation(input_list).error)
    assert actual == expected

def test_PopulationStandardDeviation_ValidList_ReturnsPopulationStandardDeviation():
    # preq-UNIT-TEST-3
    input_list = "9\r\n6\r\n8\r\n5\r\n7\r\n"
    expected = 1.4142135623730951
    actual = calculate_population_standard_deviation(input_list).result
    assert actual == expected


def test_PopulationStandardDeviation_EmptyList_ReturnsError():
    # preq-UNIT-TEST-3
    input_list = ""
    expected = 'No numbers detected. One value per line.'
    actual = str(calculate_population_standard_deviation(input_list).error)
    assert actual == expected

def test_PopulationStandardDeviation_NonNumeric_ReturnsError():
    # preq-UNIT-TEST-3
    input_list = "96\r\n34b\r\n66"
    expected = 'Non-numeric value detected. One value per line.'
    actual = str(calculate_population_standard_deviation(input_list).error)
    assert actual == expected

def test_PopulationStandardDeviation_MultipleValues_ReturnsError():
    # preq-UNIT-TEST-3
    input_list = "9 6\r\n3 4\r\n66"
    expected = 'Multiple values detected. One value per line.'
    actual = str(calculate_population_standard_deviation(input_list).error)
    assert actual == expected

def test_PopulationStandardDeviation_OneValue_ReturnsError():
    # preq-UNIT-TEST-3
    input_list = "9"
    expected = 'One number detected. Two or more numbers required.'
    actual = str(calculate_population_standard_deviation(input_list).error)
    assert actual == expected

def test_ZScore_ValidInput_ReturnsZScore():
    #preq-UNIT-TEST-5
    input_list = "11.5,7,1.5811388300841898"
    expected = 2.846049894151541
    actual = calculate_zscore(input_list).result
    assert actual == expected

def test_ZScore_EmptyInput_ReturnsError():
    #preq-UNIT-TEST-5
    input_list = ""
    expected = 'No Values detected. Format is \"value,mean,standard_deviation\" on one line.'
    actual = str(calculate_zscore(input_list).error)
    assert actual == expected

def test_Zscore_MissingParameters_ReturnsError():
    # preq-UNIT-TEST-5
    input_list = "9,3,"
    expected = 'Format is \"value,mean,standard_deviation\" on one line.'
    actual = str(calculate_zscore(input_list).error)
    assert actual == expected

def test_ZScore_MultipleLines_ReturnsError():
    # preq-UNIT-TEST-5
    input_list = "33,\r\n34,\r\n1"
    expected = 'Multiple lines detected. Format is \"value,mean,standard_deviation\" on one line.'
    actual = str(calculate_zscore(input_list).error)
    assert actual == expected

def test_ZScore_NonNumeric_ReturnsError():
    # preq-UNIT-TEST-5
    input_list = "9,34b,66"
    expected = 'Non-numeric value detected. Format is \"value,mean,standard_deviation\" on one line.'
    actual = str(calculate_zscore(input_list).error)
    assert actual == expected

def test_ZScore_MultipleValues_ReturnsError():
    # preq-UNIT-TEST-5
    input_list = "33 4, 32, 2"
    expected = 'Multiple values detected. Format is \"value,mean,standard_deviation\" on one line.'
    actual = str(calculate_zscore(input_list).error)
    assert actual == expected

def test_ZScore_StandardDeviationZero_ReturnsError():
    # preq-UNIT-TEST-5
    input_list = "33, 34, 0"
    expected = 'Division by Zero. Standard Deviation cannot be zero.'
    actual = str(calculate_zscore(input_list).error)
    assert actual == expected

def test_LinearRegression_ValidInput_ReturnsFormula():
    #preq-UNIT-TEST-6
    input_list = "1.47,52.21\r\n\r\n1.5,53.12\r\n\r\n1.52,54.48\r\n\r\n1.55,55.84\r\n\r\n1.57,57.2\r\n\r\n1.6,58.57\r\n\r\n1.63,59.93\r\n\r\n1.65,61.29\r\n\r\n1.68,63.11\r\n\r\n1.7,64.47\r\n\r\n1.73,66.28\r\n\r\n1.75,68.1\r\n\r\n1.78,69.92\r\n\r\n1.8,72.19\r\n\r\n1.83,74.46"
    expected = 'y = 61.2721865421x + -39.0619559188'
    actual = calculate_single_linear_regression(input_list).result
    assert actual == expected

def test_LinearRegression_EmptyInput_ReturnsError():
    #preq-UNIT-TEST-6
    input_list = ""
    expected = 'Empty list. Format is one \"x,y\" pair per line.'
    actual = str(calculate_single_linear_regression(input_list).error)
    assert actual == expected

def test_LinearRegression_NonNumeric_ReturnsError():
    #preq-UNIT-TEST-6
    input_list = "1.47,5.5\r\n1.56,6.65\r\n1.28,3.4\r\n1h8,10.2h"
    expected = 'Invalid Format. Format is one \"x,y\" pair per line.'
    actual = str(calculate_single_linear_regression(input_list).error)
    assert actual == expected

def test_LinearRegression_MultipleValues_ReturnsError():
    #preq-UNIT-TEST-6
    input_list = "1.47, 5.5\r\n1.56,6.65 3.6\r\n1.28,2 3.4\r\n1.8,10.2"
    expected = 'Invalid Format. Format is one \"x,y\" pair per line.'
    actual = str(calculate_single_linear_regression(input_list).error)
    assert actual == expected

def test_LinearRegression_SpacesAndCommasToIgnore_ReturnsFormula():
    #preq-UNIT-TEST-6
    input_list = "1.47, 5.5\r\n 1.56,6.65\r\n1.28, 3.4\r\n1.8,10.2 "
    expected = 'y = 13.1394101877x + -13.6329490617'
    actual = calculate_single_linear_regression(input_list).result
    assert actual == expected

def test_LinearRegression_OneCoordinatePair_ReturnsError():
    #preq-UNIT-TEST-6
    input_list = "1.5,3.6\r\n"
    expected = 'One pair detected. Multiple pairs needed. Format is one \"x,y\" pair per line.'
    actual = str(calculate_single_linear_regression(input_list).error)
    assert actual == expected

def test_PredictY_ValidInput_ReturnsPrediction():
    #preq-UNIT-TEST-7
    input_list = "1.535, 61.272186542107434, -39.061955918838656\r\n"
    expected = 'y = 54.990850423296244'
    actual = calculate_y_prediction(input_list).result
    assert actual == expected

def test_PredictY_EmptyInput_ReturnsError():
    #preq-UNIT-TEST-7
    input_list = ""
    expected = 'Empty input. Format is \"x, m, b\" on one line.'
    actual = str(calculate_y_prediction(input_list).error)
    assert actual == expected

def test_PredictY_MultipleLines_ReturnsError():
    #preq-UNIT-TEST-7
    input_list = "1.535, \r\n61.272186542107434, \r\n-39.061955918838656\r\n"
    expected = 'Multiple lines detected. Format is \"x, m, b\" on one line.'
    actual = str(calculate_y_prediction(input_list).error)
    assert actual == expected

def test_PredictY_NonNumeric_ReturnsError():
    #preq-UNIT-TEST-7
    input_list = "1.535, e61.272186542107434, -39.061955918838656"
    expected = 'Non-Numbers detected. Format is \"x, m, b\" on one line.'
    actual = str(calculate_y_prediction(input_list).error)
    assert actual == expected

def test_PredictY_MissingValues_ReturnsError():
    #preq-UNIT-TEST-7
    input_list = "1.535, 61.272186542107434"
    expected = 'Missing Value(s). Format is \"x, m, b\" on one line.'
    actual = str(calculate_y_prediction(input_list).error)
    assert actual == expected