import tkinter as tk
import json
from random import sample
from tkinter import messagebox
from os.path import exists

# Sample data to simulate the JSON file with questions and answers
sample_questions = {
    "questions": [
        {
            "keyword": "glioma",
            "question": "What is a glioma?",
            "answer": "A glioma is a type of tumor that occurs in the brain and spinal cord."
        },
        {
            "keyword": "glioma",
            "question": "What are the symptoms of a glioma?",
            "answer": "Symptoms can include headaches, nausea, vomiting, seizures, and changes in personality or mental function."
        },
        {
            "keyword": "glioma",
            "question": "How is a glioma diagnosed?",
            "answer": "Diagnosis may involve neurological exams, MRI, CT scans, and sometimes a biopsy."
        },
        {
            "keyword": "glioma",
            "question": "What are the treatment options for glioma?",
            "answer": "Treatment can include surgery, radiation therapy, chemotherapy, targeted therapy, and experimental clinical trials."
        },
        {
            "keyword": "glioma",
            "question": "What is the prognosis for someone with a glioma?",
            "answer": "Prognosis depends on the type, size, and location of the tumor, as well as the patient's age and overall health."
        },
        {
            "keyword": "glioma",
            "question": "Can gliomas be cured?",
            "answer": "Some gliomas may be managed or removed through surgery, but a cure depends on the individual case and tumor type."
        },
        {
            "keyword": "glioma",
            "question": "What is the difference between a glioma and glioblastoma?",
            "answer": "Glioblastoma is a type of glioma and is considered the most aggressive form, characterized by rapid growth and a tendency to spread within the brain."
        },
        # For testing purposes
    ]
}

# Ensure that the questions.json file exists
def check_json_file():
    if not exists('questions.json'):
        save_sample_questions_to_json()

# Function to save the sample questions to a JSON file
def save_sample_questions_to_json():
    with open('questions.json', 'w') as f:
        json.dump(sample_questions, f)

# Save the sample questions to a JSON file
# save_sample_questions_to_json()
check_json_file()


# Function to load questions from a JSON file
def load_questions_from_json():
    with open('questions.json', 'r') as f:
        return json.load(f)

# Function to filter questions by keyword and return a random subset of them
def get_random_questions(keyword, number_of_questions):
    questions = load_questions_from_json()['questions']
    filtered_questions = [q for q in questions if q['keyword'].lower() == keyword.lower()]
    return sample(filtered_questions, min(len(filtered_questions), number_of_questions))

# Function to create the GUI.
def create_gui():
    window = tk.Tk()
    window.title("Radiology Question Generation")

    keyword_label = tk.Label(window, text="Enter a keyword:")
    keyword_label.pack()
    keyword_entry = tk.Entry(window)
    keyword_entry.pack()

    number_label = tk.Label(window, text="Enter the number of questions you wish to generate (1-10):")
    number_label.pack()
    number_entry = tk.Entry(window)
    number_entry.pack()

    questions_frame = tk.Frame(window)
    questions_frame.pack()

    # Function to reveal the answer when the corresponding button is clicked.
    def reveal_answer(answer_button, answer_label, answer):
        answer_label.config(text=answer)  # Set the text of the label to the answer
        answer_button.config(state='disabled')  # Disable the button

    # Function to update the display with questions when the user inputs keyword and number.
    def update_questions_display():
        # Get the user input from the entries.
        keyword = keyword_entry.get()
        try:
            # Ensure that the number of questions is an integer.
            number_of_questions = int(number_entry.get())
        except ValueError:
            # If not an integer, do nothing.
            return

        # Ensure the number of questions is within the allowed range.
        if 1 <= number_of_questions <= 10:
            
            # Clear any existing questions from the frame.
            for widget in questions_frame.winfo_children():
                widget.destroy()
                
            # Retrieve a subset of questions based on the keyword.
            questions = get_random_questions(keyword, number_of_questions)
            
            if not questions:
                messagebox.showinfo("Info", "No questions found for the given keyword.")
                return

            # Loop through the questions and create widgets for each.
            for question in questions:
                question_label = tk.Label(questions_frame, text=question['question'])
                question_label.pack()

                # Label for the answer, initially empty.
                answer_label = tk.Label(questions_frame, text="", bg='blue')
                answer_label.pack()

                # Here we create the button and immediately pass it to the lambda using default arguments
                answer_button = tk.Button(questions_frame, text="Show Answer")
                answer_button.config(command=lambda btn=answer_button, lbl=answer_label, ans=question['answer']: reveal_answer(btn, lbl, ans))
                answer_button.pack()
        else:
            messagebox.showerror("Error", "Number of questions must be between 1 and 10.")
            return

    # Button to generate the questions based on user input.
    generate_button = tk.Button(window, text="Generate Questions", command=update_questions_display)
    generate_button.pack()

    # Start the main loop of the application.
    window.mainloop()

# Run the GUI function.
create_gui()