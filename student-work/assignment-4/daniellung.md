# Daniel Lung

Hi, my favorite coding language is python! I think this is the language I am most proficient in. 

## Example code
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()  # Replace with webdriver.Firefox() or other if needed
url = "https://www.opensecrets.org/races/outside-spending?cycle=2024&id=MTS1"
driver.get(url)

wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.ID, "DataTables_Table_1")))

data = []
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:  # Skip the header row
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 3:  # Ensure the row has the expected columns
        party = "Red" if "red" in cols[0].get_attribute("class") else "Blue" if "blue" in cols[0].get_attribute("class") else "Gray"
        committee = cols[0].text.strip()
        committee_type = cols[1].text.strip()
        total_spending = cols[2].text.strip()
        data.append([party, committee, committee_type, total_spending])

df = pd.DataFrame(data, columns=["Party", "Committee", "Type", "All 2024 Total"])
print(df)
df.to_csv("montana_senate_spending.csv", index=False)
driver.quit()
```

### Code explanation
This Python code is a web scraper that automatically fetches data from open secrets website about political campaign spending. In order to run it, you can save it in a pyscraper.py file and run it through the terminal with "python pyscraper.py". You also need to make sure you have some webdriver in the same folder. This code uses a chrome webdriver.