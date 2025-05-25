# hsn-code-validation-agent
An intelligent agent to validate HSN (Harmonized System Nomenclature) codes using Python and Excel, built as part of an internship task.
This project is built for an internship assignment that validates HSN (Harmonized System Nomenclature) codes based on a master dataset using Python.

## 📌 Project Description

HSN codes classify goods in international trade. This tool reads a master Excel file (`HSN_Master_Data.xlsx`) and validates whether a given HSN code:
- Is in the correct format (2, 4, 6, or 8 numeric digits).
- Exists in the dataset.
- Returns the description if valid.
## 🔧 Requirements

- Python 3.x
- pandas
- openpyxl

## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
    pip install pandas openpyxl
3. Run the script:
   
## 🧪 Sample Output

{'code': '01', 'status': 'Valid', 'description': 'LIVE ANIMALS'}
{'code': '0101', 'status': 'Valid', 'description': 'LIVE HORSES, ASSES, MULES AND HINNIES.'}
{'code': '01011010', 'status': 'Valid', 'description': 'LIVE HORSES, ASSES, MULES AND HINNIES PURE-BRED BREEDING ANIMALS HORSES'}
{'code': '9999', 'status': 'Invalid - Not Found'}
{'code': '01AB', 'status': 'Invalid format'}
