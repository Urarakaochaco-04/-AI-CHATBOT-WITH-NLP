import tkinter as tk
from tkinter import scrolledtext
import wikipedia
import datetime
import sys
print(sys.executable)


# Function to fetch answer from Wikipedia
def get_answer(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your question is too broad. Try asking about: {e.options[0]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find an answer. Try asking something else."
    except Exception as e:
        return "Sorry, something went wrong."

# Function to save conversation
def save_to_file(user_msg, bot_msg):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] You: {user_msg}\n")
        file.write(f"[{timestamp}] Bot: {bot_msg}\n\n")

# GUI Chat Function
def start_chat():
    def send_message():
        user_msg = entry.get()
        if user_msg.strip() == "":
            return
        chat_window.config(state='normal')
        chat_window.insert(tk.END, "You: " + user_msg + "\n")

        bot_msg = get_answer(user_msg)
        chat_window.insert(tk.END, "Bot: " + bot_msg + "\n\n")
        chat_window.config(state='disabled')

        save_to_file(user_msg, bot_msg)
        entry.delete(0, tk.END)

    # GUI Layout
    root = tk.Tk()
    root.title("AI Chatbot (Answers + Save to File)")
    root.geometry("520x600")

    chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Arial", 11))
    chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(padx=10, pady=(0, 10), fill=tk.X)

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(padx=10, pady=(0, 10))

    root.mainloop()

# Start the chatbot
start_chat()
