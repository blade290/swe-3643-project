from flask import Flask, render_template, request, redirect, url_for
from src.calculator_logic import calculation_logic
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', operation='Enter values below and select an operation', input_box_content='')

@app.route('/sample_standard_deviation', methods=['POST', 'GET'])
def sample_standard_deviation():
    input_box_content = request.form.get('input_box_content')
    calculation = calculation_logic.calculate_sample_standard_deviation(input_box_content)
    if calculation.is_success:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,input_box_content=input_box_content)
    else:
        return redirect(url_for('error_handling', error_message=calculation.error, input_box_content=input_box_content))

@app.route('/population_standard_deviation', methods=['POST', 'GET'])
def population_standard_deviation():
    input_box_content = request.form.get('input_box_content')
    calculation = calculation_logic.calculate_population_standard_deviation(input_box_content)
    if calculation.is_success:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,input_box_content=input_box_content)
    else:
        return redirect(url_for('error_handling', error_message=calculation.error, input_box_content=input_box_content))

@app.route('/mean', methods=['POST', 'GET'])
def mean():
    input_box_content = request.form.get('input_box_content')
    calculation = calculation_logic.calculate_mean(input_box_content)
    if calculation.is_success:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,input_box_content=input_box_content)
    else:
        return redirect(url_for('error_handling', error_message=calculation.error, input_box_content=input_box_content))

@app.route('/z_score', methods=['POST', 'GET'])
def z_score():
    input_box_content = request.form.get('input_box_content')
    calculation = calculation_logic.calculate_zscore(input_box_content)
    if calculation.is_success:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation, input_box_content=input_box_content)
    else:
        return redirect(url_for('error_handling', error_message=calculation.error, input_box_content=input_box_content))

@app.route('/single_linear_regression', methods=['POST', 'GET'])
def single_linear_regression():
    input_box_content = request.form.get('input_box_content')
    calculation = calculation_logic.calculate_single_linear_regression(input_box_content)
    if calculation.is_success:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,input_box_content=input_box_content)
    else:
        return redirect(url_for('error_handling', error_message=calculation.error, input_box_content=input_box_content))

@app.route('/y_prediction', methods=['POST', 'GET'])
def y_prediction():
    input_box_content = request.form.get('input_box_content')
    calculation = calculation_logic.calculate_y_prediction(input_box_content)
    if calculation.is_success:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,input_box_content=input_box_content)
    else:
        return redirect(url_for('error_handling', error_message=calculation.error, input_box_content=input_box_content))

@app.route('/error_handling', methods=['POST', 'GET'])
def error_handling():
    input_box_content = request.args.get('input_box_content')
    error_message = request.args.get('error_message')
    return render_template('index.html', error_message=error_message, input_box_content=input_box_content)
