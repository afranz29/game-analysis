import pandas as pd
import re
from collections import Counter

csv_path = r"D:\WindowsInvestigations\sysmon-overwatch-session.csv"
print("Reading Sysmon CSV...")
df = pd.read_csv(csv_path)

print(f"Total events: {len(df)}")
print("Event ID counts:")
print(df['Id'].value_counts())

# Let's parse the 'Message' column to see what images are involved
images = []
dlls_loaded = []
for msg in df['Message'].dropna():
    # Look for Image: ...
    image_match = re.search(r"Image:\s*(.+)", msg, re.IGNORECASE)
    if image_match:
        images.append(image_match.group(1).strip())
    
    # Look for ImageLoaded: ...
    loaded_match = re.search(r"ImageLoaded:\s*(.+)", msg, re.IGNORECASE)
    if loaded_match:
        dlls_loaded.append(loaded_match.group(1).strip())

print("\nTop 15 Images in events:")
print(Counter(images).most_common(15))

print("\nTop 15 Loaded DLLs:")
print(Counter(dlls_loaded).most_common(15))
