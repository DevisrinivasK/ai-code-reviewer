from flask import Flask, request, render_template
import test5
import test7
import test8

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Error Fixer
@app.route('/fix-errors', methods=['GET', 'POST'])
def fix_errors():
    if request.method == 'POST':
        code = request.form['code']
        language = request.form['language']
        corrected_code, error_report, error_count = test5.fix_code(code, language)
        return render_template('fix_errors.html', 
                             code=code,  # Pass original code back
                             result=corrected_code, 
                             report=error_report, 
                             error_count=error_count, 
                             language=language)
    return render_template('fix_errors.html', code=None, result=None, report=None, error_count=None)

# Optimizer
@app.route('/optimize', methods=['GET', 'POST'])
def optimize():
    if request.method == 'POST':
        code = request.form['code']
        language = request.form['language']
        optimized_code, debug_info, exec_time, opt_level = test7.optimize_code(code, language)
        return render_template('optimize.html', 
                             code=code,  # Pass original code back
                             result=optimized_code, 
                             report=debug_info, 
                             exec_time=exec_time, 
                             opt_level=opt_level, 
                             language=language)
    return render_template('optimize.html', code=None, result=None, report=None, exec_time=None, opt_level=None)

# Plagiarism Checker
@app.route('/check-plagiarism', methods=['GET', 'POST'])
def check_plagiarism():
    if request.method == 'POST':
        code = request.form['code']
        language = request.form['language']
        cleaned_code, debug_info, plagiarism_score = test8.check_plagiarism_and_fix(code, language)
        return render_template('plagiarism.html', 
                             code=code,  # Pass original code back
                             result=cleaned_code, 
                             report=debug_info, 
                             score=plagiarism_score, 
                             language=language)
    return render_template('plagiarism.html', code=None, result=None, report=None, score=None)

if __name__ == '__main__':
    app.run(debug=True)