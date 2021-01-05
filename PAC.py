import tkinter as tk
from tkinter import IntVar


# create container frame

class ContainerFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        self.title("PaC Time Calculator v1.0")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame_list = [PACFrame]
        self.frames = {}

        for F in frame_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PACFrame")

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
            frame = self.frames[page_name]
            frame.grid()

# create PACFrame


class PACFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # assign total time variable to 0 as placeholder value
        # assign total time text variable to total time variable
        self.total_time = 0
        self.total_time_text = IntVar()
        self.total_time_text.set(self.total_time)

        calculate_button = tk.Button(self, text="Calculate", command=self.calculate_time)

        labels = {
            "frame label": tk.Label(self, text="Puzzles and Conquests Time Calculator V1.0"),
            "1 min": tk.Label(self, text="1 min:"),
            "5 min": tk.Label(self, text="5 min:"),
            "10 min": tk.Label(self, text="10 min:"),
            "15 min": tk.Label(self, text="15 min"),
            "30 min": tk.Label(self, text="30 min:"),
            "60 min": tk.Label(self, text="60 min:"),
            "3 hr": tk.Label(self, text="3 hr:"),
            "8 hr": tk.Label(self, text="8 hr:"),
            "24 hr": tk.Label(self, text="24 hr:"),
            "total time": tk.Label(self, text="# of days:"),
            "calculated time": tk.Label(self, textvariable=self.total_time_text)
        }

        self.entries = {
            "1 min": tk.Entry(self),
            "5 min": tk.Entry(self),
            "10 min": tk.Entry(self),
            "15 min": tk.Entry(self),
            "30 min": tk.Entry(self),
            "60 min": tk.Entry(self),
            "3 hr": tk.Entry(self),
            "8 hr": tk.Entry(self),
            "24 hr": tk.Entry(self)
        }

        labels["frame label"].grid(row=0, column=0, columnspan=9)
        labels["1 min"].grid(row=1, column=0)
        labels["5 min"].grid(row=2, column=0)
        labels["10 min"].grid(row=3, column=0)
        labels["15 min"].grid(row=4, column=0)
        labels["30 min"].grid(row=5, column=0)
        labels["60 min"].grid(row=6, column=0)
        labels["3 hr"].grid(row=1, column=3)
        labels["8 hr"].grid(row=2, column=3)
        labels["24 hr"].grid(row=3, column=3)
        labels["total time"].grid(row=9, column=4, columnspan=2)
        labels["calculated time"].grid(row=9, column=8)

        self.entries["1 min"].grid(row=1, column=1)
        self.entries["5 min"].grid(row=2, column=1)
        self.entries["10 min"].grid(row=3, column=1)
        self.entries["15 min"].grid(row=4, column=1)
        self.entries["30 min"].grid(row=5, column=1)
        self.entries["60 min"].grid(row=6, column=1)
        self.entries["3 hr"].grid(row=1, column=4)
        self.entries["8 hr"].grid(row=2, column=4)
        self.entries["24 hr"].grid(row=3, column=4)

        calculate_button.grid(row=9, column=0, columnspan=2)

    def calculate_time(self):
        # set total_time
        total_time = 0
        index = 0
        # get each entry and convert to total minutes
        entry_gets = {
            "1 min": self.entries["1 min"].get(),
            "5 min": (int(self.entries["5 min"].get()) * 5),
            "10 min": (int(self.entries["10 min"].get()) * 10),
            "15 min": (int(self.entries["15 min"].get()) * 15),
            "30 min": (int(self.entries["30 min"].get()) * 30),
            "60 min": (int(self.entries["60 min"].get()) * 60),
            "3 hr": (int(self.entries["3 hr"].get()) * 180),
            "8 hr": (int(self.entries["8 hr"].get()) * 480),
            "24 hr": (int(self.entries["24 hr"].get()) * 1440),
        }

        # sum up time
        while index != len(entry_gets):
            total_time += int(list(entry_gets.values())[index])
            index += 1
            # print(total_time)

        # convert time to hours than days, rounded out
        total_time = (total_time / 60)
        total_time = (total_time / 24)
        total_time = round(total_time, 2)
        # print(str(total_time))
        self.total_time_text.set(total_time)


def main():
    root = ContainerFrame()
    root.mainloop()


if __name__ == "__main__":
    main()
