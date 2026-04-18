import pypdf

def extract_to_file(pdf_path, txt_path):
    with open(txt_path, 'a', encoding='utf-8') as f:
        f.write(f"\n--- {pdf_path} ---\n")
        try:
            reader = pypdf.PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                f.write(f"\nPage {i+1}:\n")
                f.write(page.extract_text() or "")
        except Exception as e:
            f.write(f"Error reading {pdf_path}: {e}\n")

txt_file = 'lab9_content.txt'
# clear file first
open(txt_file, 'w', encoding='utf-8').close()

extract_to_file('lab_9.pdf', txt_file)
extract_to_file('Lab_9_Qustions.pdf', txt_file)
