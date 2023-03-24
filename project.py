# Importing all the required libraries
from converter import convert_SpeechToText
import speech_recognition as sr
from tkinter import*  # This imports all the modules of the tkinter library
import pyaudio


# This title of project will be displayed at the top of the GUI : We are calling our project the Hearing Assistant
project_title = "Hearing-Assistant"
# This is our file which will we keep a log of all the previous conversations
saved_text_file = "./saved.txt"

# Our GUI will have an icon at the top, we are setting the path of this here. This icon is an image
# of a hearing assistant
try:
    icon_path = "./favicon.ico"
except:
    print('The Favicon is missing')
# Setting the font parameters, we will primarily be using these parameters throughout the GUI
selected_font = "Times"
font_buttons = "Verdana"
selected_fontSize = 20


# Initializing our speaker output to an empty string
speaker_output = ""
try:
    # If we have an existing saved text file we will open it and set the output of the speaker to
    # our existing text.
    save_txt = open(saved_text_file, "r", encoding='utf-8')
    speaker_output = save_txt.read()
    save_txt.close()
except FileNotFoundError:
    # Incase the file is not found, it means that there are no previous conversatiions, thus,
    # we will keep the speaker output as empty initially.
    fi_le = open(saved_text_file, "w+", encoding="utf-8")

# -------------------------This is the function that gets called when we click the record button----------------------------------


def recorder():
    # defining the speaker output
    global speaker_output
    try:
        # Clearing the frame
        for widget in DisplayFrame.winfo_children():
            widget.destroy()
    except:
        pass
    speaker_output += '\n'  # This moves it to the next line
    speaker_output += str(convert_SpeechToText())
    # capture and show text
    textFrame = LabelFrame(DisplayFrame, font=(
        selected_font, selected_fontSize), text="Conversion Output")
    textFrame.pack(fill="both", expand=True)
    showText = frame_Scroll(textFrame)
    Text = Label(showText.scrollable_frame, padx=10, pady=5,
                 justify=LEFT, font=(selected_font, selected_fontSize), text=speaker_output)
    Text.pack(fill="both", expand=True)
    showText.pack(fill="both", expand=True)


class frame_Scroll(Frame):
    def __init__(self, container, *args, **kwargs):
        # Setting the constructor
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        # Creating a scrollbar and setting it's orientation to vertical
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview
                              )
        self.scrollable_frame = Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")
                                       )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def helpingframe(option):
    frame = Toplevel()
    # Setting the title of the frame as "Hearing Assistant"
    frame.title(project_title)
    try:
        frame.iconbitmap(icon_path)
    except:
        print('The Favicon is Missing ')
    # Setting the dimensions of the frame
    frame.geometry("720x480")
    # setting the specifications for the help option
    if option == 'help':
        # Creating Frame for help
        defaultFrame = Frame(frame)
        defaultFrame.pack(fill="both", expand=True, padx=1, pady=1)
        # This will create the widgets isnide the help section. We will have two widgets here : help and about.
        frame_top = LabelFrame(defaultFrame, bd=2, width=480, height=300, padx=50,
                               pady=50, relief=RIDGE, bg="grey", fg="white", text="Help")
        # Placing the help widget inside the frame
        frame_top.pack(fill="both", expand=True)
        # Setting the text of the help section with our pre defined font values
        text_help = Label(frame_top, bg="grey", fg="white",
                          font=(selected_font, selected_fontSize), text="Hi this is the help section")
        # Placing the text
        text_help.pack(fill="both", expand=True, padx=5, pady=5)
    # setting the specifications for the about option now
    if option == 'about':
        # Creating frame for about now as before
        defaultFrame = Frame(frame)
        # Placing the frane
        defaultFrame.pack(fill="both", expand=True, padx=1, pady=1)
        # Creating the widget inside the frame
        frame_top = LabelFrame(defaultFrame, bd=2, width=480, height=300, padx=50,
                               pady=50, relief=RIDGE, bg="grey", fg="white", text="About Section")
        # Placing the frame
        frame_top.pack(fill="both", expand=True)
        # Setting the text for "about"
        text_about = Label(frame_top, fg="white", bg="grey",
                           font=(selected_font, selected_fontSize), text="Hi this a hearing assistant. Thanks!")
        # Placing the text
        text_about.pack(fill="both", expand=True, padx=5, pady=5)


if __name__ == '__main__':
    # Initializing the tkinter root
    root = Tk()
    # Setting the ttitle of the root as "Hearing Assistant"
    root.title(project_title)
    # Same try-catch block as before
    try:
        root.iconbitmap(icon_path)
    except:
        print('Favicon is Missing')
    # Setting the dimensions of the GUI. This can be adjusted as required. For now, we have set comparitively larger dimensions for better
    # visulaization.
    root.geometry("1200x800")
    # Using the Menu widget in the GUI
    bar_menu = Menu(root)
    # Setting the tearoff=0 at declaration of help menu
    help_menu = Menu(bar_menu, tearoff=0)
    # The help meny will have two commands : Help and about. Adding help first
    help_menu.add_command(label="Help Index",
                          command=lambda: helpingframe('help'))
    # Now adding the about secttion
    help_menu.add_command(
        label="About...", command=lambda: helpingframe('about'))
    # Adding the menu seperator
    help_menu.add_separator()
    # Adding the exit button and setting it's command as the quit command. The root.quit closes
    # the GUI
    help_menu.add_command(label="Exit", command=root.quit)
    bar_menu.add_cascade(label="Help", menu=help_menu)
# Creating the base frame here
frame_default = Frame(root)
frame_default.pack(fill="both", expand=True, padx=5, pady=5)
# Creatting the widgets inside the default frame
frame_top = Frame(frame_default, bd=2, width=480, height=300,
                  padx=10, pady=10, relief=RAISED, bg="black")
# Adding(packing) the frame now
frame_top.pack(fill="both", expand=True)
frame_main = Frame(frame_top)
# Adding the frame
frame_main.pack(fill="both", expand=True)
# Creating the widgets inside the main frame
# The display frame is the basic frame that will contain the speech to text output
DisplayFrame = Frame(frame_main, bd=5, width=720, height=360,
                     padx=2, relief=RAISED, bg="yellow")
# Placing the display frame
DisplayFrame.pack(fill="both", expand=True)
# Creating the button frame, the button frame will contain two buttons : Record Voice and Exit.
frame_button = Frame(frame_main, bd=5, width=720, height=80,
                     padx=2, relief=RAISED, bg="cyan")
# Placing the button frame
frame_button.pack(fill="both", expand=True)
# Creating the record button and setting it's command as the recorder function
button_record = Button(frame_button, text="Record Voice",
                       padx=20, pady=20, command=recorder, fg="black", bg="white", relief=RAISED, font=(font_buttons, 16, "bold"))
# Placing the record button.
button_record.pack(side=LEFT, padx=30, pady=10)
# Creating the quit button and setting it's command to root.quit()
button_quit = Button(frame_button, text="Exit",
                     padx=20, pady=20, command=root.quit,
                     fg="black", bg="white", relief=RAISED, font=(font_buttons, 16, "bold"))
# Placing the quit button
button_quit.pack(side=RIGHT, padx=30, pady=10)

root.config(menu=bar_menu)
root.mainloop()
