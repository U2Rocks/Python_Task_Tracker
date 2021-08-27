import tkinter as tk

# task tracker application where people can organize tasks for the day


# function that clears tasks from the board
def clear_task_board():
    global default_board_task_text
    global default_board_time_text
    iterate_open_slots(0)
    default_board_task_text = "No Task Yet!"
    default_board_time_text = "No Time Yet!"
    task_1.config(text=default_board_task_text)
    time_1.config(text=default_board_time_text)
    task_2.config(text=default_board_task_text)
    time_2.config(text=default_board_time_text)
    task_3.config(text=default_board_task_text)
    time_3.config(text=default_board_time_text)
    task_4.config(text=default_board_task_text)
    time_4.config(text=default_board_time_text)
    task_5.config(text=default_board_task_text)
    time_5.config(text=default_board_time_text)
    task_6.config(text=default_board_task_text)
    time_6.config(text=default_board_time_text)
    task_7.config(text=default_board_task_text)
    time_7.config(text=default_board_time_text)
    task_8.config(text=default_board_task_text)
    time_8.config(text=default_board_time_text)
    task_9.config(text=default_board_task_text)
    time_9.config(text=default_board_time_text)
    task_10.config(text=default_board_task_text)
    time_10.config(text=default_board_time_text)
    task_11.config(text=default_board_task_text)
    time_11.config(text=default_board_time_text)
    task_12.config(text=default_board_task_text)
    time_12.config(text=default_board_time_text)
    pass


# function that removes top task and moves tasks up
def clear_top_task():
    default_board_task_text_temp = "No Task Yet!"
    default_board_time_text_temp = "No Time Yet!"
    # swap all task texts up one
    task_1.config(text=task_2.cget("text"))
    task_2.config(text=task_3.cget("text"))
    task_3.config(text=task_4.cget("text"))
    task_4.config(text=task_5.cget("text"))
    task_5.config(text=task_6.cget("text"))
    task_6.config(text=task_7.cget("text"))
    task_7.config(text=task_8.cget("text"))
    task_8.config(text=task_9.cget("text"))
    task_9.config(text=task_10.cget("text"))
    task_10.config(text=task_11.cget("text"))
    task_11.config(text=task_12.cget("text"))
    # swap all time texts up one
    time_1.config(text=time_2.cget("text"))
    time_2.config(text=time_3.cget("text"))
    time_3.config(text=time_4.cget("text"))
    time_4.config(text=time_5.cget("text"))
    time_5.config(text=time_6.cget("text"))
    time_6.config(text=time_7.cget("text"))
    time_7.config(text=time_8.cget("text"))
    time_8.config(text=time_9.cget("text"))
    time_9.config(text=time_10.cget("text"))
    time_10.config(text=time_11.cget("text"))
    time_11.config(text=time_12.cget("text"))
    # make row 12 blank after all of the texts are moved up
    task_12.config(text=default_board_task_text_temp)
    time_12.config(text=default_board_time_text_temp)
    # subtract one from label counter
    iterate_open_slots(2)
    pass

# function that iterates through a int variable to find an open task slot


def iterate_open_slots(number):
    global open_slot
    if number == 0:
        open_slot = int()
        open_slot = 0
    if number == 1:
        open_slot = open_slot + 1
        if open_slot > 11:
            open_slot = 11
    if number == 2:
        open_slot = open_slot - 1
        if open_slot < 0:
            open_slot = 0
    print(open_slot)


# function that clears entry boxes
def clear_entries():
    task_input.delete(0, 'end')
    task_input_time.delete(0, 'end')
    task_input.insert(0, "Enter A Task Here")
    task_input_time.insert(0, "Input An Amount of Minutes")


# function that stores entry values into temp variables and the number is used for reseting values
def store_temp_variables(number):
    global task_name
    global task_name_time
    global default_task_text
    global default_time_text
    global check_if_entry_error
    check_if_entry_error = False
    default_task_text = "Enter A Task Here"
    default_time_text = "Input An Amount of Minutes"
    task_name = task_input.get()
    task_name_time = task_input_time.get()
    task_name_check = check_if_entry_default()
    if task_name_check == False:
        print("False Name Check :O")
        task_name = "ERROR"
        task_name_time = "TIME ERROR"
        check_if_entry_error = True
    if number == 0:
        print("clear triggered")
        task_name = default_task_text
        task_name_time = default_time_text
        clear_entries()


# function that checks if entry boxes have been edited
def check_if_entry_default():
    if task_name == default_task_text or task_name_time == default_time_text:
        return False
    else:
        return True


# function that adds task to task tracking list
def add_task():
    store_temp_variables(1)
    if check_if_entry_error == True:
        return
    modify_label()
    store_temp_variables(0)
    iterate_open_slots(1)


# function modify label
def modify_label():
    minute_modifier = " Minutes"
    if open_slot == 0:
        task_1.config(text=task_name)
        time_1.config(text=task_name_time + minute_modifier)
    if open_slot == 1:
        task_2.config(text=task_name)
        time_2.config(text=task_name_time + minute_modifier)
    if open_slot == 2:
        task_3.config(text=task_name)
        time_3.config(text=task_name_time + minute_modifier)
    if open_slot == 3:
        task_4.config(text=task_name)
        time_4.config(text=task_name_time + minute_modifier)
    if open_slot == 4:
        task_5.config(text=task_name)
        time_5.config(text=task_name_time + minute_modifier)
    if open_slot == 5:
        task_6.config(text=task_name)
        time_6.config(text=task_name_time + minute_modifier)
    if open_slot == 6:
        task_7.config(text=task_name)
        time_7.config(text=task_name_time + minute_modifier)
    if open_slot == 7:
        task_8.config(text=task_name)
        time_8.config(text=task_name_time + minute_modifier)
    if open_slot == 8:
        task_9.config(text=task_name)
        time_9.config(text=task_name_time + minute_modifier)
    if open_slot == 9:
        task_10.config(text=task_name)
        time_10.config(text=task_name_time + minute_modifier)
    if open_slot == 10:
        task_11.config(text=task_name)
        time_11.config(text=task_name_time + minute_modifier)
    if open_slot == 11:
        task_12.config(text=task_name)
        time_12.config(text=task_name_time + minute_modifier)


# setup base for tkinter app
root = tk.Tk()
root.title("Task Tracker Pro")
root.geometry('600x600')
root.minsize(600, 600)
root.maxsize(600, 600)
root.config(bg="#fc9403")


# initialize input box for tasks, amount of task time, clear button, and add task button
global task_input
global task_input_time
task_input = tk.Entry(root, width=20)
task_input.insert(0, 'Enter A Task Here')
task_input_time = tk.Entry(root, width=30)
task_input_time.insert(0, 'Input An Amount of Minutes')
task_add = tk.Button(root, text="Add Task", command=add_task)
task_clear = tk.Button(root, text="Clear All Tasks", command=clear_task_board)
task_frame = tk.Frame(root, bg="#7DBBC3")
remove_top_task = tk.Button(
    root, text="Remove Top Task", command=clear_top_task)

# create placeholder labels to test item frame
global task_1
global time_1
global task_2
global time_2
global task_3
global time_3
global task_4
global time_4
global task_5
global time_5
global task_6
global time_6
global task_7
global time_7
global task_8
global time_8
global task_9
global time_9
global task_10
global time_10
global task_11
global time_11
global task_12
global time_12
task_1 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_1 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_2 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_2 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_3 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_3 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_4 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_4 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_5 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_5 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_6 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_6 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_7 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_7 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_8 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_8 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_9 = tk.Label(task_frame, text="No Task Yet!", width=20,
                  padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_9 = tk.Label(task_frame, text="No Time Yet!",
                  width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_10 = tk.Label(task_frame, text="No Task Yet!", width=20,
                   padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_10 = tk.Label(task_frame, text="No Time Yet!",
                   width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_11 = tk.Label(task_frame, text="No Task Yet!", width=20,
                   padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_11 = tk.Label(task_frame, text="No Time Yet!",
                   width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")
task_12 = tk.Label(task_frame, text="No Task Yet!", width=20,
                   padx=10, pady=10, bg="#7DBBC3", font="Helvetica 11")
time_12 = tk.Label(task_frame, text="No Time Yet!",
                   width=20, padx=10, pady=10, bg="#DAEDBD", font="Helvetica 11")


# place items on a grid
task_input.grid(row=0, column=0, padx=10, pady=10)
task_input_time.grid(row=0, column=1, padx=10, pady=10)
task_add.grid(row=0, column=2, padx=10, pady=10)
task_clear.grid(row=0, column=3, padx=10, pady=10)
task_frame.grid(row=2, column=0, columnspan=4)
remove_top_task.grid(row=1, column=1, padx=10, pady=10)

# place labels onto the frame
task_1.grid(row=0, column=0)
time_1.grid(row=0, column=1)
task_2.grid(row=1, column=0)
time_2.grid(row=1, column=1)
task_3.grid(row=2, column=0)
time_3.grid(row=2, column=1)
task_4.grid(row=3, column=0)
time_4.grid(row=3, column=1)
task_5.grid(row=4, column=0)
time_5.grid(row=4, column=1)
task_6.grid(row=5, column=0)
time_6.grid(row=5, column=1)
task_7.grid(row=6, column=0)
time_7.grid(row=6, column=1)
task_8.grid(row=7, column=0)
time_8.grid(row=7, column=1)
task_9.grid(row=8, column=0)
time_9.grid(row=8, column=1)
task_10.grid(row=9, column=0)
time_10.grid(row=9, column=1)
task_11.grid(row=10, column=0)
time_11.grid(row=10, column=1)
task_12.grid(row=11, column=0)
time_12.grid(row=11, column=1)

# call root loop to start application
iterate_open_slots(0)
root.mainloop()
