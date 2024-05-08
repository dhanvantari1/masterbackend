"""
Error messages for user management.
Author: Dhanvantari Yeole
Date: 27th April 2024
"""

# Error messages for user management
USER_CREATED_SUCCESSFULLY = "User created successfully."
OTP_SENT = "OTP sent"
OTP_RESEND_LIMIT_REACHED = "OTP resend limit reached, account locked until"
INVALID_CONTEXT = "Invalid context"
INVALID_TOKEN = "Invalid token"
OTP_SENT_TO_MOBILE = "OTP sent to mobile number"
INVALID_PHONE_NUMBER = "Invalid Phone number"
PHONE_NUMBER_NOT_FOUND = "Phone number not found"
ACCOUNT_LOCKED = "Your account is locked until"
PASSWORD_CHANGED_SUCCESSFULLY = "Password changed successfully"
INVALID_OR_EXPIRED_OTP = "Invalid or expired OTP"
USER_NOT_FOUND = "User not found"
INVALID_USERNAME_OR_PASSWORD = "Invalid username or password"
LOGIN_SUCCESSFUL = "Login successful"
VERIFICATION_CODE_SENT = "Verification code sent on phone"
ACCOUNT_LOCKED_RETRY_LATER = "Account locked. Please try again after"
INVALID_PASSWORD = "Invalid password"
INVALID_USERNAME = "Invalid username"
USERNAME_PASSWORD_REQUIRED = "Username and password are required"
USER_DELETED_SUCCESSFULLY = "User deleted successfully."
DATA_UPDATED_SUCCESSFULLY = "Data updated successfully."
USER_ID_REQUIRED = "User id is required."
RECORD_DELETED_SUCCESSFULLY = "record deleted successfully."
RECORD_UPDATED_SUCCESSFULLY = "record updated successfully"
RECORD_NOT_CREATED = "record not created"
RECORD_CREATED_SUCCESSFULLY = "record created successfully"
NO_RECORDS_FOUND = "No records found."
RECORD_FETCHED_SUCCESSFULLY = "Record fetched successfully"
REQUESTED_RECORD_NOT_FOUND = "The requested record not found."
INVALID_ENTITY = "Invalid entity"
PASSWORD_RESET_CODE = "Your password reset code is:"
VERIFICATION_CODE = "Your verification code is:"
REFERENCE_NUMBER_DATA_FETCHED = "Reference number data fetched successfully."
STATE_COMMODITY_MODE_NOT_FOUND = "State or Commodity or Mode not found."
JRF_DELETED_SUCCESSFULLY = "JRF and associated JRFDetails deleted successfully."
JRF_UPDATED_SUCCESSFULLY = "JRF updated successfully."
NO_DATA_TO_CREATE = "No data to create."
JRFDETAILS_NOT_FOUND = "JRFDetails not found."
JRF_NOT_FOUND = "JRF id not found."
JRF_FETCHED_SUCCESSFULLY = "jrf and jrfdetail fetched successfully."
JRFDETAILS_CREATED_SUCCESSFULLY = "JRFDetails created successfully."
JRF_CREATED_SUCCESSFULLY = "JRF created successfully."
REFERENCE_NUMBER_REQUIRED = "Reference number is required."

DATA_NOT_FOUND = "Data not found"
DATA_FOUND_SUCCESSFULLY = "Data found successfully"
RECORD_ID_NOT_PROVIDED = "Record ID not provided"
ENTITY_ID_NOT_PROVIDED = "Entity ID not provided"
MODEL_NOT_FOUND = "Model not found"
# General error messages
UNEXPECTED_ERROR = "An unexpected error occurred"

DATA_RETRIVED = "Data retrieved successfully."
COMPANY_NAME_REQUIRED = "Company name is required."
No_DATA_DELETE = "No data to delete."
NO_DATA_UPDATE = "No data to update."
NO_REFERNCE_NUMBER = "No reference number provided."
ERROR_SAMPLE_INWARD_NOT_FOUND = "Sample Inward not found"
SAMPLE_INWARD_CREATED_SUCCESSFULLY = "Sample Inward a created successfully."
SAMPLE_INWARD_DETAILS_CREATED_SUCCESSFULLY = "Sample Inward Details created successfully."
SAMPLE_INWARD_SET_CREATED_SUCCESSFULLY = "Sample Inward Set created successfully."
SAMPLE_INWARD_UPDATED_SUCCESSFULLY = "Sample Inward updated successfully."
SAMPLE_INWARD_DETAIL_UPDATED_SUCCESSFULLY = "Sample Inward Detail updated successfully."
SAMPLE_INWARD_DELETED_SUCCESSFULLY = "Sample Inward deleted successfully."
SAMPLE_INWARD_DETAILS_UPDATED_SUCCESSFULLY = "Sample Inward Details updated successfully."
ERROR_SAMPLE_INWARD_NOT_FOUND= "Sample Inward not found"
NO_DATA_TO_CREATE = "No data provided for Sample Inward Set creation"

messages = {
    "create": {
        "basis": "Basis created successfully",
        "commodity": "Commodity created successfully",
        "standard": "Standards created successfully",
        "parameter": "Parameter created successfully",
        "commodity_group": "Commodity Group created successfully",
        "tenant_master": "Tenant Master created successfully",
        "commodity_specs": "Commodity Specs created successfully",
        # Add more models as needed
    },
    "delete": {
        "basis": "Basis deleted successfully",
        "commodity": "Commodity deleted successfully",
        "standard": "Standards deleted successfully",
        "parameter": "Parameter deleted successfully",
        "commodity_group": "Commodity Group deleted successfully",
        "tenant_master": "Tenant Master deleted successfully",
        "commodity_specs": "Commodity Specs deleted successfully",
        # Add more models as needed
    },
    "update": {
        "basis": "Basis updated successfully",
        "commodity": "Commodity updated successfully",
        "standard": "Standards updated successfully",
        "parameter": "Parameter updated successfully",
        "commodity_group": "Commodity Group updated successfully",
        "tenant_master": "Tenant Master updated successfully",
        "commodity_specs": "Commodity Specs updated successfully",
        # Add more models as needed
    },
    "fetch": {
        "basis": "Basis fetched successfully",
        "commodity": "Commodity fetched successfully",
        "standard": "Standards fetched successfully",
        "parameter": "Parameter fetched successfully",
        "commodity_group": "Commodity Group fetched successfully",
        "tenant_master": "Tenant Master fetched successfully",
        "commodity_specs": "Commodity Specs fetched successfully",
        # Add more models as needed
    },
    

    "not_found": {
        "basis": "Basis not found",
        "commodity": "Commodity not found",
        "standard": "Standards not found",
        "parameter": "Parameter not found",
        "commodity_group": "Commodity Group not found",
        "tenant_master": "Tenant Master not found",
        "commodity_specs": "Commodity Specs not found",
        # Add more models as needed
    },

    "not_created":{
        "basis": "Basis not created",
        "commodity": "Commodity not created",   
        "standard": "Standards not created",
        "parameter": "Parameter not created",
        "commodity_group": "Commodity Group not created",
        "tenant_master": "Tenant Master not created",
        "commodity_specs": "Commodity Specs not created",
        # Add more models as needed

    }

}