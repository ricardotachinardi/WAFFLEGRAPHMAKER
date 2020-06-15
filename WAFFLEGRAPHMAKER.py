import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Function to get inputs from the GUI and then create the graph
def create_graph():

    plt.cla()
    frame1 = tk.Frame(window)

    # Getting inputs
    values_input = ent_1.get().split(', ')
    # Transform str input in float
    for i in range(len(values_input)):
        values_input[i] = float(values_input[i])

    names_input = ent_2.get().split(', ')

    colors_input = ent_3.get().split(', ')

    icons_input = ent_4.get().split(', ')
    
    xmargin_input = ent_5.get().split(', ')

    ymargin_input = ent_6.get().split(', ')


    # Create list from values_input and names_input, needed to plot in pywaffle 
    if names_input == None or names_input == ['']:
        data = values_input
    else:
        data = {}
        for i in range(len(values_input)):
            data[names_input[i]] = values_input[i]


    # Create list from colors_input, needed to plot in pywaffle
    colors_values = []
    for i in range(len(colors_input)):
        colors_values.append(colors_input[i])


    # Default values
    if icons_input == ['']:
        icons_input = None

    if xmargin_input == ['']:
        xmargin = 0.15
    else:
        xmargin = float(xmargin_input[0])
        
    if ymargin_input == ['']:
        ymargin = 0.15
    else:
        ymargin = float(ymargin_input[0])

    # Plot the graph 
    fig = plt.figure(
        FigureClass=Waffle, 
        rows=10, 
        values=data, 
        colors=colors_values,
        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.2), 'ncol': len(data), 'framealpha': 0},
        interval_ratio_x = xmargin,
        interval_ratio_y = ymargin,
        icons = icons_input
    )
    # Set-up the graph in the GUI
    canvas = FigureCanvasTkAgg(fig, frame1)

    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)

    toolbar = NavigationToolbar2Tk(canvas, frame1)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)
    frame1.grid(row=8, column = 1, columnspan=2)
# Set-up the window
window = tk.Tk()
window.title("Waffle Graph Maker")
window.resizable(width=True, height=True)

# Create the Tkinter labels and entries
lbl_1 = tk.Label(master=window, text="values:")
ent_1 = tk.Entry(master=window, width=20)

lbl_2 = tk.Label(master=window, text="legend (default = None):")
ent_2 = tk.Entry(master=window, width=20)

lbl_3 = tk.Label(master=window, text="color name or HEX:")
ent_3 = tk.Entry(master=window, width=20)

lbl_4 = tk.Label(master=window, text="icons (default = None):")
ent_4 = tk.Entry(master=window, width=20)

lbl_5 = tk.Label(master=window, text="x spacing (default = 0.15):")
ent_5 = tk.Entry(master=window, width=20)

lbl_6 = tk.Label(master=window, text="y spacing (default = 0.15):")
ent_6 = tk.Entry(master=window, width=20)


# Create the Graph Maker button and result display Label
btn = tk.Button(
    master=window,
    text="GENERATE",
    command=create_graph
)


# Set-up the layout using the .grid() geometry manager
lbl_1.grid(row =1, column=1, sticky='W')
ent_1.grid(row =1, column=2, sticky='W')

ent_2.grid(row =2, column=2, sticky='W')
lbl_2.grid(row =2, column=1, sticky='W')

lbl_3.grid(row =3, column=1, sticky='W')
ent_3.grid(row =3, column=2, sticky='W')

lbl_4.grid(row =4, column=1, sticky='W')
ent_4.grid(row =4, column=2, sticky='W')

lbl_5.grid(row =5, column=1, sticky='W')
ent_5.grid(row =5, column=2, sticky='W')

lbl_6.grid(row =6, column=1, sticky='W')
ent_6.grid(row =6, column=2, sticky='W')

btn.grid(row=7, column=1, columnspan=2, sticky='N')


# Run the application
window.mainloop()
