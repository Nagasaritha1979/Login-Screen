from tkinter import *
from PIL import ImageTk, Image

win=Tk()
win.geometry('1000x700')
win.resizable(1,1)


def show():
    pass_word_entry.config(show="")
    toggle_btn.configure(bg='dark orange')
def hide():
    pass_word_entry.config(show="*")
#------------------Background Image  ----------------------------
back_ground= Image.open('autumn1.jpg')
back_ground=ImageTk.PhotoImage(back_ground,master=win)

back_label=Label(win,image=back_ground)
back_label.image=back_ground
back_label.pack(fill='both',expand='yes')

#--------------------  Login Frame ------------------------------

main_frame=Frame(win,bg='dark orange',width=800,height=500)
main_frame.place(x=100,y=100)

fore_ground_original= Image.open('nature1.jpg')
fore_ground=fore_ground_original.resize((400,400))
fore_ground=ImageTk.PhotoImage(fore_ground,master=win)

fore_label=Label(main_frame,image=fore_ground,bg='dark orange')
fore_label.image=fore_ground
fore_label.place(x=10,y=60)

login_text='LOGIN'
login_heading=Label(main_frame, text=login_text,font=("Arial",25),bg='dark orange',fg='black')
login_heading.place(x=500,y=20)

#------------------------User Name and Password ------------

usr_name_lbl=Label(main_frame,text='Username',bg='dark orange',fg='black',font=('Arial',15))
usr_name_lbl.place(x=420,y=150)

usr_name_entry=Entry(main_frame,highlightthickness=0,relief=FLAT,bg='dark orange',fg='black',font=("Arial",13),width=30)
usr_name_entry.place(x=450,y=180)

usr_name_line=Canvas(main_frame,width=200,height=2.0, bg='black',highlightthickness=0)
usr_name_line.place(x=450,y=200)


usr_icon_original= Image.open('orange_icon.jpg')
usr_icon=usr_icon_original.resize((25,25))
usr_icon=ImageTk.PhotoImage(usr_icon,master=win)

usr_icon_lbl=Label(main_frame,image=usr_icon,bg='dark orange')
usr_icon_lbl.image=usr_icon
usr_icon_lbl.place(x=420,y=175)


usr_name_entry.bind('<FocusIn>', lambda e: usr_name_line.configure(bg='white'))
usr_name_entry.bind('<FocusOut>', lambda e: usr_name_line.configure(bg='black'))

pass_word_lbl=Label(main_frame,text='Password', bg='dark orange',fg='black',font=("Arial",15))
pass_word_lbl.place(x=420,y=225)

pass_word_entry=Entry(main_frame,show='*',highlightthickness=0,relief=FLAT,bg='dark orange',fg='black',font=("Arial",13))
pass_word_entry.place(x=450,y=255)
pass_icon_original= Image.open('password_icon.png')
pass_icon=pass_icon_original.resize((25,25))
pass_icon=ImageTk.PhotoImage(pass_icon,master=win)

pass_icon_lbl=Label(main_frame,image=pass_icon,bg='dark orange')
pass_icon_lbl.image=pass_icon
pass_icon_lbl.place(x=420,y=255)

pass_word_line=Canvas(main_frame,width=200,height=2.0, bg='black',highlightthickness=0)
pass_word_line.place(x=450,y=280)

pass_word_entry.bind('<FocusIn>',lambda e: pass_word_line.configure(bg='white'))
pass_word_entry.bind('<FocusOut>',lambda e: pass_word_line.configure(bg='black'))

toggle_btn = Button(main_frame, text='Show Password', width=15,bg='dark orange',fg='white',cursor='hand2',activebackground='dark orange')
toggle_btn.place(x=670,y=270)
toggle_btn.bind("<ButtonPress>", lambda event:show())
toggle_btn.bind("<ButtonRelease>", lambda event:hide())


login_btn= Image.open('login_btn3.png')
photo=ImageTk.PhotoImage(login_btn,master=win)

login_btn_lbl=Button(main_frame,image=photo,bg='dark orange',activebackground='dark orange',cursor='hand2',bd=0)
login_btn_lbl.image=photo
login_btn_lbl.place(x=550,y=350)

forgot_pass_btn=Button(main_frame,text='Forgot Password ?',bd=0,font=("Arial",13), bg='dark orange',activebackground='dark orange',cursor='hand2')
forgot_pass_btn.place(x=530,y=395)

signup_account_btn=Button(main_frame,text='No Account yet ?',bd=0,font=("Arial",13),bg='dark orange',activebackground='dark orange',cursor='hand2')
signup_account_btn.place(x=500,y=435)

signup_btn_original= Image.open('signup_button.png')
signup_btn=signup_btn_original.resize((50,50))
photo=ImageTk.PhotoImage(signup_btn,master=win)

signup_btn_lbl=Button(main_frame,image=photo,bg='dark orange',activebackground='dark orange',cursor='hand2',bd=0)
signup_btn_lbl.image=photo
signup_btn_lbl.place(x=650,y=435)

win.mainloop()
