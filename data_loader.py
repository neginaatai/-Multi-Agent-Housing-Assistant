# this file is created to fetch and process data before using in LLM


import sqlite3
from typing import List, Dict

def load_housing_data() -> List[Dict]:
    """Load housing resources from SQLite database"""
    try:
        conn = sqlite3.connect('data/housing_resources.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT NAME, ADDRESS, ZIP_CODE, PHONE, 
                   RESOURCE_TYPE, SERVICES 
            FROM HOUSING_RESOURCES
        """)
        
        resources = cursor.fetchall()
        
        # Convert to list of dictionaries
        housing_data = []
        for resource in resources:
            housing_data.append({
                'name': resource[0],
                'address': resource[1],
                'zip_code': resource[2],
                'phone': resource[3],
                'resource_type': resource[4],
                'services': resource[5]
            })
        
        conn.close()
        return housing_data
    except Exception as e:
        print(f" Error loading data: {e}")
        return []

def format_resource(resource: Dict) -> str:
    """Format a resource as text"""
    return f"""
Resource: {resource['name']}
Address: {resource['address']}, Chicago, IL {resource['zip_code']}
Phone: {resource['phone']}
Type: {resource['resource_type']}
Services: {resource['services']}
"""

if __name__ == "__main__":
    # Test it
    data = load_housing_data()
    print(f" Loaded {len(data)} resources")
    if data:
        print("\nFirst resource:")
        print(format_resource(data[0]))
    else:
        print(" No data loaded. Check your database.")
