import sqlite3
import os

# Path to Chrome's cookies database file
cookies_db = os.path.expanduser('/Users/elainezhao/Documents/Robin_Stock/new/Untitled/mysite/playground/Cookies')

# Connect to the database
conn = sqlite3.connect(cookies_db)
cursor = conn.cursor()

# SQL query to retrieve cookie data
query = 'SELECT name, value, host_key, path, expires_utc FROM cookies'

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Close the database connection
conn.close()

# Filter the results to include only cookies that contain shopping cart information
shopping_cart_cookies = [result for result in results if 'cart' in result[0] or 'basket' in result[0]]

# Filter the results to include only cookies that are used for advertising
advertising_cookies = [result for result in results if 'ad' in result[0] or 'tracker' in result[0]]

# Filter the results to include only cookies that are used for analytics
analytics_cookies = [result for result in results if 'analytics' in result[0] or 'tracking' in result[0]]

