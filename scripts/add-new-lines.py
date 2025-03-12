# This script adds 4 blank lines after each paragraph that starts with "E)" or "e)"
# It's used to format savindi's questionnaires

from docx import Document

def add_spaces_after_e(input_file, output_file):
    try:
        doc = Document(input_file)
        paragraphs = doc.paragraphs

        for i in range(len(paragraphs)):
            text = paragraphs[i].text.strip()
            
            # Check if the paragraph starts with "E)" or "e)"
            if text.startswith("E)") or text.startswith("e)") or text.startswith("E.") or text.startswith("e."):
                # Add 4 blank lines after the current paragraph
                for _ in range(4):
                    paragraphs[i+1].insert_paragraph_before("")

        doc.save(output_file)
        print(f"Successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the function
input_file = "file.docx"  # Make sure your input file is in .docx format
output_file = "output.docx"

add_spaces_after_e(input_file, output_file)


