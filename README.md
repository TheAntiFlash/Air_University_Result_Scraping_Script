# Air University Result Scraper

This script scrapes semester grade reports for students from [https://portals.au.edu.pk/auresult/](https://portals.au.edu.pk/auresult/#) and exports the data into an Excel file. The script uses Selenium for web automation and pandas for data manipulation and export.

## Requirements

- Python 3.x
- Selenium
- pandas
- Chrome WebDriver (or the appropriate driver for your browser)

## Installation

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Required Packages**: Install the necessary Python packages using pip.
    ```bash
    pip install selenium pandas
    ```

3. **Download WebDriver**: Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory that is in your system's PATH. Alternatively, you can specify the path to the WebDriver executable in the script.

## Usage

1. **Prepare Your List of Student IDs**: Modify the `student_ids` list in the script to include the student IDs you want to scrape.
    ```python
    student_ids = ['123456', '234567', '345678']  # Add your student IDs here
    ```

2. **Run the Script**: run it using Python.
    ```bash
    python main.py
    ```

3. **Output**: The script will save the grade reports in an Excel file named `grade_reports.xlsx` in the same directory.

## Script Details

### scrape_grades.py

This script performs the following steps:

1. **Initialize the WebDriver**: Sets up the Selenium WebDriver for Chrome.

2. **Define Function to Scrape Grade Report**:
    - Navigates to the specified website.
    - Inputs the student ID and clicks the "Search Result" button.
    - Extracts the student's name, grade report, and GPA.
    - Returns the extracted data.

3. **Iterate Over Student IDs**:
    - Iterates over the list of student IDs.
    - Calls the scraping function for each student ID.
    - Collects the data into a list of dictionaries.

4. **Save Data to Excel**:
    - Converts the collected data into a pandas DataFrame.
    - Reorders the columns to move the GPA column to the end.
    - Saves the DataFrame to an Excel file.

## Example

Here is an example of how to modify the script with your own list of student IDs:

```python
# List of student IDs
student_ids = ['111111', '222222', '333333']  # Replace with your actual student IDs

# The rest of the script remains unchanged
