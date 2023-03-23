import sqlite3
import os
import json
import csv

# Path to Chrome's history database file
history_db = os.path.expanduser('/Users/elainezhao/Documents/Robin_Stock/new/Untitled/mysite/playground/History')

# Connect to the database
conn = sqlite3.connect(history_db)
cursor = conn.cursor()

# SQL query to retrieve the browsing history
query = 'SELECT title, url, last_visit_time FROM urls ORDER BY last_visit_time DESC'

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the database connection
conn.close()

with open('history.json', 'w', encoding='utf-8') as f:
    json.dump(results, f)

with open('history.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'URL', 'Last Visit Time'])
    for result in results:
        writer.writerow(result)



#
