from tkinter import Tk,Entry,Label,W,E,StringVar,IntVar,END
from tkmacosx import Button
import sqlite3

root = Tk()
root.title("Address Book")
# root.geometry("400x400")
#Databases

# Create a Database or connect to already exist
conn =sqlite3.connect('address_book.db')

# Create a cursor it is like sender and receiver of data to database 
c = conn.cursor()

#create table 
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )
# """)

def save():
    # Create a Database or connect to already exist
    conn =sqlite3.connect('address_book.db')

    # Create a cursor it is like sender and receiver of data to database 
    c = conn.cursor()  

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode

    WHERE oid = :oid""",
    {
        "first":f_name_editor.get(),
        "last":l_name_editor.get(),
        "address":address_editor.get(),
        "city": city_editor.get(),
        "state":state_editor.get(),
        "zipcode":zipcode_editor.get(),
        "oid":record_id
    })

    #commit change
    conn.commit()

    #close connection 
    conn.close() 

    editor.destroy()   
    


#create function to delete record
def delete():
    # Create a Database or connect to already exist
    conn =sqlite3.connect('address_book.db')

    # Create a cursor it is like sender and receiver of data to database 
    c = conn.cursor()   

    c.execute("DELETE from addresses WHERE oid=" + delete_box.get()) 

    delete_box.delete(0,END)

    #commit change
    conn.commit()

    #close connection 
    conn.close()   

# create function to update record

def update():
    global editor
    editor = Tk()
    editor.title("Edit Record")
    # Create a Database or connect to already exist
    conn =sqlite3.connect('address_book.db')

    # Create a cursor it is like sender and receiver of data to database 
    c = conn.cursor()

    record_id = delete_box.get()
    #Queary the database
    c.execute("SELECT * FROM addresses WHERE oid="+record_id)
    records = c.fetchall()

    #create global variable for text boxname
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    #create text box
    f_name_editor = Entry(editor,width=30)
    f_name_editor.grid(row=1,column=1,padx=20)

    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=2,column=1,padx=20)

    address_editor = Entry(editor,width=30)
    address_editor.grid(row=3,column=1,padx=20)

    city_editor = Entry(editor,width=30)
    city_editor.grid(row=4,column=1,padx=20)

    state_editor = Entry(editor,width=30)
    state_editor.grid(row=5,column=1,padx=20)

    zipcode_editor = Entry(editor,width=30)
    zipcode_editor.grid(row=6,column=1,padx=20)

    # delete_box = Entry(editor,width=30)
    # delete_box.grid(row=9,column=1,padx=20)

    #create text box label

    address_bar_label = Label(editor,text="Edit Record",font=("Calibra",30,"bold"))
    address_bar_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

    f_name_label = Label(editor,text="First Name")
    f_name_label.grid(row = 1,column=0,padx=20,pady=10,stick=W)

    l_name_label = Label(editor,text="Last Name")
    l_name_label.grid(row = 2,column=0,padx=20,pady=10,stick=W)

    address_label = Label(editor,text="Address")
    address_label.grid(row = 3,column=0,padx=20,pady=10,stick=W)

    city_label = Label(editor,text="City")
    city_label.grid(row = 4,column=0,padx=20,pady=10,stick=W)

    state_label = Label(editor,text="State")
    state_label.grid(row = 5,column=0,padx=20,pady=10,stick=W)

    zipcode_label = Label(editor,text="Zip Code")
    zipcode_label.grid(row = 6,column=0,padx=20,pady=10,stick=W)

    # Loop through result
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    save_btn = Button(editor,text="Save",padx=10,pady=10,takefocus=0,command=save)
    save_btn.grid(row=7,column=0,padx=10,pady=10,columnspan=2)
  
#create submit function for database
def submit():
    # Create a Database or connect to already exist
    conn =sqlite3.connect('address_book.db')

    # Create a cursor it is like sender and receiver of data to database 
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })

    #commit change
    conn.commit()

    #close connection 
    conn.close()    

    # Clear text box
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#create Query function for database
def query():
    # Create a Database or connect to already exist
    conn =sqlite3.connect('address_book.db')

    # Create a cursor it is like sender and receiver of data to database 
    c = conn.cursor()

    #Queary the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    
    print_records = ""
    for record in records:
        print_records += str(record[0]) +" "+ str(record[1]) + " " + "\t" + str(record[6])+ "\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)

    #commit change
    conn.commit()

    #close connection 
    conn.close() 


#create text box
f_name = Entry(root,width=30)
f_name.grid(row=1,column=1,padx=20)

l_name = Entry(root,width=30)
l_name.grid(row=2,column=1,padx=20)

address = Entry(root,width=30)
address.grid(row=3,column=1,padx=20)

city = Entry(root,width=30)
city.grid(row=4,column=1,padx=20)

state = Entry(root,width=30)
state.grid(row=5,column=1,padx=20)

zipcode = Entry(root,width=30)
zipcode.grid(row=6,column=1,padx=20)

delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,padx=20)

#create text box label

address_bar_label = Label(root,text="Address Book",font=("Calibra",30,"bold"))
address_bar_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

f_name_label = Label(root,text="First Name")
f_name_label.grid(row = 1,column=0,padx=20,pady=10,stick=W)

l_name_label = Label(root,text="Last Name")
l_name_label.grid(row = 2,column=0,padx=20,pady=10,stick=W)

address_label = Label(root,text="Address")
address_label.grid(row = 3,column=0,padx=20,pady=10,stick=W)

city_label = Label(root,text="City")
city_label.grid(row = 4,column=0,padx=20,pady=10,stick=W)

state_label = Label(root,text="State")
state_label.grid(row = 5,column=0,padx=20,pady=10,stick=W)

zipcode_label = Label(root,text="Zip Code")
zipcode_label.grid(row = 6,column=0,padx=20,pady=10,stick=W)

delete_box_label = Label(root,text="Select Record")
delete_box_label.grid(row=9,column=0,padx=20,sticky=W)

# submit button

submit_btn = Button(root,text="Submit",padx=10,pady=10,activebackground=("cyan","blue"),takefocus=0,command=submit)
submit_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=20,ipadx=100)

# Create a query Button
query_btn = Button(root,text="Query",padx=10,pady=10,takefocus=0,command=query)
query_btn.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#create delete button
delete_btn = Button(root,text="Delete record",padx=10,pady=10,takefocus=0,command=delete)
delete_btn.grid(row=10,column=1,padx=10,pady=10,ipadx=50)

# create an update button
update_btn = Button(root,text="Edit record",padx=10,pady=10,takefocus=0,command=update)
update_btn.grid(row=10,column=0,padx=10,pady=10,sticky=E,ipadx=70)

#commit change
conn.commit()

#close connection 
conn.close()

root.mainloop()
