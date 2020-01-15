import tkinter
import json
from play import play

#JSON open(users load in):
users_pw = []
users_name = []

with open("users.json") as users:
    users_data = json.load(users)
    for i in users_data:
        users_name.append(i["name"])
        users_pw.append(i["pw"])

#Functions:
def add_user(): #Add user
    if input1.get() and input2.get() is not "":
        data = {
            "name": input1.get(),
            "pw": input2.get()
        }
        users_data.append(data)
        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=4)
    else:
        pass
    input1.delete(0, "end")
    input2.delete(0, "end")


def remove(): #Remove user
    index = users_name.index(variable.get())
    del users_data[index]
    with open('users.json', 'w') as f:
        json.dump(users_data, f, indent=4)


def play_song(): #Play song, play function in play.py
    name = variable.get()
    index = users_name.index(variable.get())
    pw = users_pw[index]
    proxy = input3.get()
    album = input4.get()
    play(name, pw, proxy, album)



#GUI setup:
window = tkinter.Tk()
window.title("Tidal Bot")
window.geometry("400x120")
window.resizable(False, False)

#For optionMenu refresh:
newUser = tkinter.StringVar()


top_frame = tkinter.Frame(window, bg="white", width=600, height=30)
mid_frame = tkinter.Frame(window, bg="white", width=600, height=30)
mid2_frame = tkinter.Frame(window, bg="white", width=600, height=30)
bottom_frame = tkinter.Frame(window, bg="white", width=600, height=30)
top_frame.grid(row=1)
mid_frame.grid(row=2)
mid2_frame.grid(row=3)
bottom_frame.grid(row=4)
input1 = tkinter.Entry(top_frame, width=15, textvariable= newUser)
input2 = tkinter.Entry(top_frame, width=15)
input3 = tkinter.Entry(bottom_frame, width=20)
input4 = tkinter.Entry(bottom_frame, width=20)
add_user = tkinter.Button(top_frame, text="Add User", command=add_user)
remove = tkinter.Button(mid_frame, text="Remove User", command=remove)
play_song = tkinter.Button(mid_frame, text="Start Song", command=play_song, bg="green")
input1.grid(row=1, column=0, padx=10)
input2.grid(row=1, column=1, padx=10)
input3.grid(row=3, column=0, padx=10)
input4.grid(row=3, column=1, padx=10)
add_user.grid(row=1, column=2, padx=10)
remove.grid(row=2, column=0, padx=10)
play_song.grid(row=2, column=1, padx=10)
input1.insert(0, "Email")
input2.insert(0, "Password")
input3.insert(0, "Proxy")
input4.insert(0, "Album link")

#Users list:
variable = tkinter.StringVar()
variable.set("Users")  #default value


userList = tkinter.OptionMenu(mid2_frame, variable, *users_name)
userList.config(width=40)
userList.grid(row=3, column=1)

window.mainloop()


