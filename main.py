from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Read the list of student IDs from an Excel file. You can also use a list of IDs directly.
student_ids = pd.read_excel('students_info.xlsx')['Roll No.'].tolist()

# Initialize the WebDriver (Make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # You can use other drivers like Firefox, Edge, etc.


# Function to scrape grade report for a student
def scrape_grade_report(student_id):
    # Navigate to the website
    driver.get('https://portals.au.edu.pk/auresult')

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'ctl00$AUContent$txt_regid')))

    # Find the input element and enter the student ID
    student_input = driver.find_element(By.NAME, 'ctl00$AUContent$txt_regid')
    student_input.clear()
    student_input.send_keys(student_id)

    # Find and click the "Search Result" button
    search_button = driver.find_element(By.ID, 'AUContent_btnShow')
    search_button.click()

    # Wait for the result to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'AUContent_lbl_gpa')))

    # Extract student's name
    name_element = driver.find_element(By.XPATH, '//table[@id="AUContent_DataList1"]/tbody/tr/td')
    name_text = name_element.text.split('\n')
    name = name_text[1].split(':')[1].strip()

    # Wait for the grade table to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'AUContent_GridView1')))

    # Extract grade report data
    rows = driver.find_elements(By.XPATH, '//table[@id="AUContent_GridView1"]/tbody/tr')
    grade_report = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_elements(By.TAG_NAME, 'td')
        course = cols[0].text
        credit_hours = cols[1].text
        grade = cols[2].text
        grade_report.append((course, credit_hours, grade))

    # Extract GPA
    gpa_element = driver.find_element(By.ID, 'AUContent_lbl_gpa')
    gpa = gpa_element.text.strip()

    return student_id, name, grade_report, gpa


# Data structure to hold the results
results = []

# Iterate over the list of student IDs and scrape the grade reports
for index, student_id in enumerate(student_ids):
    student_id, name, grade_report, gpa = scrape_grade_report(student_id)
    student_data = {
        'Sr#': index + 1,
        'ID': student_id,
        'Name': name
    }
    for i, (course, credit_hours, grade) in enumerate(grade_report):
        student_data[f'{course} [{credit_hours}Cr.Hr]'] = grade
    student_data['Gpa'] = gpa
    results.append(student_data)
    time.sleep(1)  # Sleep to avoid overloading the server

# Close the WebDriver
driver.quit()

# Create a DataFrame and save to Excel
df = pd.DataFrame(results)
cols = [col for col in df.columns if col != 'Gpa'] + ['Gpa']
df = df[cols]
df.to_excel('grade_reports.xlsx', index=False)

print('Grade reports saved to grade_reports.xlsx')
