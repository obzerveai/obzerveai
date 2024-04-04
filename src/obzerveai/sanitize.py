import re
from monitor import track_usage

def redact_sensitive_info(text):
    # Regular expressions for sensitive information
    regex_patterns = {
        # 'names': r'\b[A-Z][a-z]+\b(?:\s[A-Z][a-z]+)*',
        # 'addresses': r'\d{1,5}\s\w+\s\w+\s\w+|\d{1,5}\s\w+\s\w+',
        'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone_numbers': r'\b(?:\d{3}[-.\s]??\d{3}[-.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-.\s]??\d{4}|\d{3}[-.\s]??\d{4})\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        "passport": r'^[a-zA-Z]{1}\d{8}$',
        "drivers_license": r'^[a-zA-Z]{1}\d{7}$',
        "date": r"\d(3[01]|[12][0-9]|0?[1-9])(\/|-)(1[0-2]|0?[1-9])\2([0-9]{2})?[0-9]{2}",
        'credit_cards': r'^\d{4}-\d{4}-\d{4}-\d{4}$',
        'health_info': r'\b\d{3}-\d{2}-\d{4}\b',  # Sample for medical record numbers
        # 'financial_info': r'\b(?:\d[ -]*?){13,16}\b'  # Sample for credit card or account numbers
    }
    
    redacted_text = text
    for category, pattern in regex_patterns.items():
        # if type(pattern) == list:
        #     for each_pattern in pattern:
        #         print(each_pattern)
        #         redacted_text = re.sub(each_pattern, '[REDACTED - {}]'.format(category), redacted_text)        
        # else:
            redacted_text = re.sub(pattern, '[REDACTED - {}]'.format(category), redacted_text)
    
    track_usage()
    return redacted_text
