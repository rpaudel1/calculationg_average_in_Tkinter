# This program uses a GUI to get three test
# scores and display their average.

import tkinter as tk
class TestAverage:
    def __init__(self):
        # Create the main window.
        self.__main_window = tk.Tk()
        self.__main_window.title('String_Var')
        self.__main_window.geometry('250x200')
        self.create_widgets()
        # Start the main loop.
        tk.mainloop()
    def create_widgets(self):
        # Create the five frames.
        self.__test1_frame = tk.Frame(self.__main_window)
        self.__test2_frame = tk.Frame(self.__main_window)
        self.__test3_frame = tk.Frame(self.__main_window)
        self.__average_frame = tk.Frame(self.__main_window)
        self.__button_frame = tk.Frame(self.__main_window)

        # Create and pack the widgets for test 1.
        self.__test1_label = tk.Label(self.__test1_frame,
                text = 'Enter the score for test 1:')
        self.__test1_entry = tk.Entry(self.__test1_frame, width = 10)
        self.__test1_label.pack(side = 'left')
        self.__test1_entry.pack(side = 'left')
        #pack the first frame
        self.__test1_frame.pack()
        
        # Create and pack the widgets for test 2.
        self.__test2_label = tk.Label(self.__test2_frame,
                text = 'Enter the score for test 2:')
        self.__test2_entry = tk.Entry(self.__test2_frame, width = 10)
        self.__test2_label.pack(side = 'left')
        self.__test2_entry.pack(side = 'left')
        self.__test2_frame.pack()

        # Create and pack the widgets for test 3.
        self.__test3_label = tk.Label(self.__test3_frame,
                                      text='Enter the score for test 3:')
        self.__test3_entry = tk.Entry(self.__test3_frame, width=10)
        self.__test3_label.pack(side = 'left')
        self.__test3_entry.pack(side = 'left')
        self.__test3_frame.pack()
        
        # Create and pack the widgets for the average.
        self.__result_label = tk.Label(self.__average_frame,
                                    text = 'The Average is:', fg = 'green')
        self.__avg = tk.StringVar() # an instance of StrinVar class
        self.__avg_label = tk.Label(self.__average_frame, textvariable = self.__avg)
        self.__result_label.pack(side = 'left')
        self.__avg_label.pack(side = 'left')
        self.__average_frame.pack()

        # Create and pack the button widgets.
        self.__calc_button = tk.Button(self.__button_frame, text = 'Calculate', fg = 'green',
            bg = 'yellow', command = self.__calc_average)
        self.__quit_button = tk.Button(self.__button_frame, text = 'Quit', fg = 'white',
            bg = 'red', command = self.__main_window.destroy)
        self.__calc_button.pack(side = 'left')
        self.__quit_button.pack(side = 'left')
        # Pack button frame
        self.__button_frame.pack()
        # The calc_avg method is the callback function for
        # the calc_button widget.

    def __calc_average(self):
        # Get the three test scores and store them
        # in variables.
        self.__test1 = float(self.__test1_entry.get())
        self.__test2 = float(self.__test2_entry.get())
        self.__test3 = float(self.__test3_entry.get())
        # Calculate the average.
        self.__average = round(((self.__test1 + self.__test2 + self.__test3) / 3.0), 2)
        # Update the avg_label widget by storing
        # the value of self.average in the StringVar
        # object referenced by avg.
        self.__avg.set(str(self.__average))

# Create an instance of the TestAvg class.
test_avg = TestAverage()

                                     
