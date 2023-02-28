from gooeypie import *

errors = {}

def validate_roll_no_inp(event, indicator):
    global errors
    if not event.widget.text.isdigit():
        indicator.text = '❎'
        errors["Roll Number"] = "Roll number must be a number."
        return
    indicator.text = '✅'
    errors.pop("Roll Number", 1)
    return


def validate_alpha_inp(event, indicator, label):
    global errors
    if not event.widget.text.isalpha():
        indicator.text = '❎'
        errors[label.text] = f"{label.text} must consist of letters only."
        return
    indicator.text = '✅'
    errors.pop(label.text, 1)
    return
    

def validate_grade_dd(event, indicator):
    global errors
    if not event.widget.selected:
        indicator.text = '❎'
        errors["Grade"] = "Please select a valid grade."
        return
    indicator.text = '✅'
    errors.pop("Grade", 1)
    return


def validate_marks_inp(event, indicator):
    global errors
    if not event.widget.text.isdigit():
        indicator.text = '❎'
        errors["Marks"] = "Marks must be a number."
        return
    elif not int(event.widget.text) <= 100:
        indicator.text = '❎'
        errors["Marks"] = "Marks should be less than or equal to 100."
        return
    indicator.text = '✅'
    errors.pop("Marks", 1)
    return


def validate_mobile_inp(event, indicator):
    global errors
    if not event.widget.text.isdigit():
        indicator.text = '❎'
        errors["Mobile"] = "Mobile Number must be a number."
        return
    elif not len(event.widget.text) == 10:
        indicator.text = '❎'
        errors["Mobile"] = "Mobile Number should have 10 digits."
        return
    indicator.text = '✅'
    errors.pop("Mobile", 1)
    return
    

def validate_submit(errors):
    if not all((roll_no_inp.text, name_inp.text, last_name_inp.text, grade_dd.selected, marks_inp.text, address_txt.text, mobile_inp.text)):
        app.alert("Error", "All fields are madatory", "error")
        return
    print(errors)    
    if messages := errors.values():
        error = "\n".join([message for message in messages])
        app.alert("Error", error, "error")
        return
    app.alert("Success", "Data saved successfully!", "info")
    


app = GooeyPieApp("Student Records")

# -------------------------------- New entry container widgets start--------------------------------------------------
new_entry_container = LabelContainer(app, 'Add New Records')

# Row 1
roll_no_lbl = Label(new_entry_container, "Roll No.")
roll_no_inp = Input(new_entry_container)
roll_no_inp_validator = Label(new_entry_container, "❎")
roll_no_inp.add_event_listener("change", lambda x: validate_roll_no_inp(x, roll_no_inp_validator))

name_lbl = Label(new_entry_container, "Name")
name_inp = Input(new_entry_container)
name_inp_validator = Label(new_entry_container, "❎")
name_inp.add_event_listener("change", lambda x: validate_alpha_inp(x, name_inp_validator, name_lbl))

last_name_lbl = Label(new_entry_container, "Last Name")
last_name_inp = Input(new_entry_container)
last_name_inp_validator = Label(new_entry_container, "❎")
last_name_inp.add_event_listener("change", lambda x: validate_alpha_inp(x, last_name_inp_validator, last_name_lbl))

# Row 2
grade_lbl = Label(new_entry_container, "Grade")
grade_dd = Dropdown(new_entry_container, ["", "A", "B", "C", "D", "F"])
grade_dd.width = 17
grade_dd_validator = Label(new_entry_container, "❎")
grade_dd.add_event_listener("select", lambda x: validate_grade_dd(x, grade_dd_validator))

marks_lbl = Label(new_entry_container, "Marks")
marks_inp = Input(new_entry_container)
marks_inp_validator = Label(new_entry_container, "❎")
marks_inp.add_event_listener("change", lambda x: validate_marks_inp(x, marks_inp_validator))

mobile_lbl = Label(new_entry_container, "Mobile")
mobile_inp = Input(new_entry_container)
mobile_inp_validator = Label(new_entry_container, "❎")
mobile_inp.add_event_listener("change", lambda x: validate_mobile_inp(x, mobile_inp_validator))

# Row 3
address_lbl = Label(new_entry_container, "Address")
address_txt = Textbox(new_entry_container, 10, 2)


# Row 4
save_btn = Button(new_entry_container, "Save", lambda x: validate_submit(errors))
# ------------------------------------------- New entry container widgets end --------------------------------------------------------

# ------------------------------------------- Table container widgets start ----------------------------------------------------------
table_container = LabelContainer(app, "Records")

# Row 1
records_tbl = Table(table_container, ["Roll No.", "Name", "Last Name", "Grade", "Marks", "Mobile Number", "Address"])
records_tbl.set_column_alignments('center', 'center', 'center', 'center', 'center', 'center', 'center')
records_tbl.set_column_widths(40, 40, 40, 40, 40, 40, 300)
records_tbl.height = 6


# ------------------------------------------- Table container widgets end ------------------------------------------------------------

# ------------------------------------------- Delete container widgets start ------------------------------------------------------------

delete_container = LabelContainer(app, "Delete Record")

delete_roll_no_lbl = Label(delete_container, "Roll No.")
delete_roll_no_inp = Input(delete_container)
delete_roll_no_inp_validator = Label(delete_container, "❎")
delete_roll_no_inp.add_event_listener("change", lambda x: validate_roll_no_inp(x, delete_roll_no_inp_validator))

delete_btn = Button(delete_container, "Delete", None)
# ------------------------------------------- Delete container widgets end ------------------------------------------------------------

# ------------------------------------------- Show container widgets start ------------------------------------------------------------

show_container = LabelContainer(app, "Show")

show_roll_no_lbl = Label(show_container, "Roll No.")
show_roll_no_inp = Input(show_container)
show_roll_no_inp_validator = Label(show_container, "❎")
show_roll_no_inp.add_event_listener("change", lambda x: validate_roll_no_inp(x, show_roll_no_inp_validator))

show_btn = Button(show_container, "Show marks", None)
# ------------------------------------------- Show container widgets end ------------------------------------------------------------


# --------------------------------------- Grid ----------------------------------------------
app.set_grid(5, 3)

app.add(new_entry_container, 1, 1, row_span=3, fill=True, stretch=True)

v_sep = Separator(app, "vertical")
app.add(v_sep, 1, 2, row_span=3, fill=True, stretch=True)

app.add(delete_container, 1, 3, fill=True, align="right", stretch=True)

app.add(show_container, 3, 3, fill=True, align="right", stretch=True)

h_sep = Separator(app, "horizontal")
app.add(h_sep, 4, 1, column_span=3, fill=True, stretch=True)


app.add(table_container, 5, 1, column_span=3, fill=True, stretch=True)


# --------------------------------------New Entry Container --------------------------------
new_entry_container.set_grid(4, 9)


new_entry_container.add(roll_no_lbl, 1, 1)
new_entry_container.add(roll_no_inp, 1, 2, margins=["auto", 0, "auto", 0])
new_entry_container.add(roll_no_inp_validator, 1, 3, margins=["auto", 0, "auto", 0])


new_entry_container.add(name_lbl, 1, 4, margins=["auto", 0, "auto", 50])
new_entry_container.add(name_inp, 1, 5, margins=["auto", 0, "auto", 0])
new_entry_container.add(name_inp_validator, 1, 6, margins=["auto", 0, "auto", 0])


new_entry_container.add(last_name_lbl, 1, 7, margins=["auto", 0, "auto", 50])
new_entry_container.add(last_name_inp, 1, 8, margins=["auto", 0, "auto", 0])
new_entry_container.add(last_name_inp_validator, 1, 9, margins=["auto", 10, "auto", 0])


new_entry_container.add(grade_lbl, 2, 1)
new_entry_container.add(grade_dd, 2, 2, margins=["auto", 0, "auto", 0])
new_entry_container.add(grade_dd_validator, 2, 3, margins=["auto", 0, "auto", 0])


new_entry_container.add(marks_lbl, 2, 4, margins=["auto", 0, "auto", 50])
new_entry_container.add(marks_inp, 2, 5, margins=["auto", 0, "auto", 0])
new_entry_container.add(marks_inp_validator, 2, 6, margins=["auto", 0, "auto", 0])


new_entry_container.add(mobile_lbl, 2, 7, margins=["auto", 0, "auto", 50])
new_entry_container.add(mobile_inp, 2, 8, margins=["auto", 0, "auto", 0])
new_entry_container.add(mobile_inp_validator, 2, 9, margins=["auto", 10, "auto", 0])


new_entry_container.add(address_lbl, 3, 1)
new_entry_container.add(address_txt, 3, 2, column_span=8, fill=True, margins=["auto", 0, "auto", 0])


new_entry_container.add(save_btn, 4, 5, fill=True)


# ---------------------------------------- Table Container --------------------------------
table_container.set_grid(1, 1)
table_container.add(records_tbl, 1, 1, fill=True)

# ---------------------------------------- Delete Container ----------------------------------
delete_container.set_grid(1, 4)
delete_container.add(delete_roll_no_lbl, 1, 1, fill=True)
delete_container.add(delete_roll_no_inp, 1, 2, margins=["auto", 0, "auto", 0], fill=True)
delete_container.add(delete_roll_no_inp_validator, 1, 3, margins=["auto", 0, "auto", 0], fill=True)

delete_container.add(delete_btn, 1, 4, fill=True)

# ---------------------------------------- Show Container ----------------------------------
show_container.set_grid(1, 4)
show_container.add(show_roll_no_lbl, 1, 1, fill=True)
show_container.add(show_roll_no_inp, 1, 2, margins=["auto", 0, "auto", 0], fill=True)
show_container.add(show_roll_no_inp_validator, 1, 3, margins=["auto", 0, "auto", 0], fill=True)

show_container.add(show_btn, 1, 4, fill=True)

if __name__ == "__main__":
    app.run()