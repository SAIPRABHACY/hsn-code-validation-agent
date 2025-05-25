import pandas as pd

# Load Excel data
def load_hsn_data(file_path):
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()  
    df['HSNCode'] = df['HSNCode'].astype(str).str.strip()
    df.set_index('HSNCode', inplace=True)
    return df['Description'].to_dict()


# Validation function
def validate_hsn_code(code, hsn_dict):
    code = code.strip()
    if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
        return {"code": code, "status": "Invalid format"}
    if code in hsn_dict:
        return {"code": code, "status": "Valid", "description": hsn_dict[code]}
    else:
        return {"code": code, "status": "Invalid - Not Found"}

# Run  validation
if __name__ == "__main__":
    hsn_file = "HSN_SAC.xlsx"  
    hsn_dict = load_hsn_data(hsn_file)
    
    codes_to_check = ["01", "0101", "01011010", "9999", "01AB"]

    for code in codes_to_check:
        result = validate_hsn_code(code, hsn_dict)
        print(result)
