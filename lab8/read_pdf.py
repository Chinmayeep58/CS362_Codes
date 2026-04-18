import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pypdf
except ImportError:
    install('pypdf')
    import pypdf

reader = pypdf.PdfReader('LAB_8_Qustions.pdf')
print("--- LAB_8_Qustions.pdf ---")
for page in reader.pages:
    print(page.extract_text())

print("\n--- CS302_Lab8.pdf ---")
try:
    reader2 = pypdf.PdfReader('CS302_Lab8.pdf')
    for page in reader2.pages:
        print(page.extract_text())
except Exception as e:
    print("Could not read CS302_Lab8.pdf:", e)
