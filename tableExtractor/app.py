import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, redirect
import pandas as pd
import pdfplumber
import uuid

# Configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'Downloads')  # Ensures proper path handling
ALLOWED_EXTENSIONS = {'pdf'}  # Set is preferred

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = str(uuid.uuid4())  # Generate a unique secret key

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    # Check for a valid file extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_file(file_path):
    # Extract tables from the PDF file
    tables = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                table = pd.DataFrame(table)
                table.columns = table.iloc[0]  # Correctly assign column headers
                table.drop(0, inplace=True)  # Drop the first row (headers)
                tables.append(table)
    return tables

@app.route('/')
def home():
    return render_template('home.html')  # Corrected typo in 'render_template'

@app.route('/extract_table', methods=['POST'])
def extract_table():
    # Handle file upload
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract tables from the uploaded PDF
        tables = extract_file(file_path)

        # Save extracted tables to an Excel file
        output_excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'extracted_file.xlsx')
        with pd.ExcelWriter(output_excel_path) as writer:
            for i, df in enumerate(tables):
                df.to_excel(writer, sheet_name=f"Sheet{i + 1}", index=False)

        # Convert tables to HTML for display on the webpage
        tables_html = [df.to_html(index=False) for df in tables]

        return render_template('home.html', org_img_name=filename, tables=tables_html, ntables=len(tables))
    else:
        flash("Invalid file type. Please upload a PDF file.")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
