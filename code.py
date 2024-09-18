import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to load and detect file type, then display the head of the data
def load_and_display_file():
    file_path = filedialog.askopenfilename(title="Select File", filetypes=[("All Files", "*.*")])
    
    if not file_path:
        messagebox.showwarning("No file selected", "Please select a file!")
        return
    
    # Check the file type
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
        print("CSV file detected:")
        print(data.head())
        
    elif file_path.endswith('.tsv'):
        data = pd.read_csv(file_path, sep='\t')
        print("TSV file detected:")
        print(data.head())
        
    elif file_path.endswith('.fastq'):
        print("FASTQ file detected:")
        records = SeqIO.parse(file_path, 'fastq')
        for i, record in enumerate(records):
            if i >= 5:  # Limit to 5 sequences for the head
                break
            print(f"ID: {record.id}")
            print(f"Sequence: {record.seq}")
            print(f"Description: {record.description}")
            print(f"Quality: {record.letter_annotations['phred_quality']}\n")
    else:
        messagebox.showwarning("Unknown file type", "Unsupported file type. Please select a CSV, TSV, or FASTQ file.")

# Create the GUI window
def create_gui():
    window = tk.Tk()
    window.title("Drag and Drop File Loader")
    window.geometry("400x200")
    
    # Label and button for file selection
    label = tk.Label(window, text="Please drag and drop or select a file", pady=20)
    label.pack()
    
    load_button = tk.Button(window, text="Select File", command=load_and_display_file, width=20, pady=10)
    load_button.pack()
    
    # Start the Tkinter loop
    window.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
