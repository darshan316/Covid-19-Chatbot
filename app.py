from tkinter import *
from chat import get_response, bot_name

# Updated color scheme
BG_COLOR = "#1c1c1c"
TEXT_COLOR = "#FFFFFF"
ENTRY_BG_COLOR = "#333333"
BUTTON_BG_COLOR = "#4CAF50"
BUTTON_TEXT_COLOR = "#FFFFFF"
HEAD_COLOR = "#2E8B57"
DIVIDER_COLOR = "#4CAF50"

FONT = "Verdana 12"
FONT_BOLD = "Verdana 12 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("CovidBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=500, height=600, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=HEAD_COLOR, fg=TEXT_COLOR,
                           text="CovidBot", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # divider
        line = Label(self.window, width=450, bg=DIVIDER_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=10, pady=10, wrap=WORD)
        self.text_widget.place(relheight=0.75, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, font=FONT, bd=2, relief=FLAT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, bg=BUTTON_BG_COLOR,
                             fg=BUTTON_TEXT_COLOR, activebackground=BUTTON_BG_COLOR, activeforeground=BUTTON_TEXT_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        send_button.configure(relief=FLAT)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
