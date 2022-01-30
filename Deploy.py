from tkinter import *
from tkinter import filedialog as fd
from Response_Prediction import response
from Lungs_Prediction import predict_image

BG_GRAY = "#ABB2B9"
BG_COLOR = "#141414"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# ChatBot class
class ChatBot:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    
    # helper function to keep the window active
    def run(self):
        self.window.mainloop()

    
    # helper function to setup the main window
    def _setup_main_window(self):
        self.window.title("Covi hates COVID")
        self.window.resizable(width = False, height = False)
        self.window.configure(width = 500, height = 580, bg = BG_COLOR)

        # head label
        header = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, text = "Covi on Duty", font = FONT_BOLD, pady = 10)
        header.place(relwidth = 1)

        line = Label(self.window, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        
        # text widget
        self.text_widget = Text(self.window, width = 25, height = 2, bg = BG_COLOR, fg = TEXT_COLOR, font = FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor = "arrow", state = DISABLED)

        # scrollbar = Scrollbar(self.window)
        # scrollbar.place(relheight = 1, relx = 0.96)
        # scrollbar.configure(command = self.text_widget.yview)
        
        bottom_label = Label(self.window, bg = BG_GRAY, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg = "#0d0d0d", fg = TEXT_COLOR, font = FONT)
        self.msg_entry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text = "Send", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = lambda: self._on_enter_pressed(None))
        send_button.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")


    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state = DISABLED)

        token, res = response(msg)

        if token == "lungs":
            img_path = fd.askopenfilename()
            res = predict_image(img_path)
            
        msg2 = f"Covi: {res}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state = DISABLED)
        
        self.text_widget.see(END)

# Driver code
if __name__ == "__main__":
    app = ChatBot()
    app.run()
