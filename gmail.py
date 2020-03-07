
import smtplib
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import wget
import cv2


def send_email(SUBJECT, MESSAGE):
    try:
        tkinter.messagebox.showinfo("Message","Email sending process initiated.")
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender_email.get(),sender_pw.get() )
        message = 'Subject: {}\n\n{}'.format(SUBJECT, MESSAGE)
        server.sendmail(sender_email.get(), reciever_email.get(), message)
        server.quit()
        tkinter.messagebox.showinfo("Success!","Email sent Successfully.")
    except:
        tkinter.messagebox.showinfo("Error","Cannot send Email.")


def send_email_new():
    send_email(subject_variable.get(),message_variable.get())

def gmail_image():
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/New_Logo_Gmail.svg/1200px-New_Logo_Gmail.svg.png"
    local_image_filename = wget.download(image_url)
    print(local_image_filename)
    img = ImageTk.PhotoImage(Image.open(local_image_filename))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
        
    
    
    
root = Tk()
root.title("GUI : Email Sending Using Python")

root.geometry("1000x560")

root.configure(background = '#e6e5e5')
Tops = Frame(root,bg = '#e6e5e5',pady = 1, width =550, height = 50, relief = RIDGE)
Tops.grid(row=0,column=0)


sender_email = StringVar()
sender_pw = StringVar()
reciever_email = StringVar()

subject_variable = StringVar()
message_variable = StringVar()


Title_Label = Label(Tops,font=('Comic Sans MS',26,'bold'),text = "          Email Sending Using Python with GUI\t\t",bg= '#663300',fg='white',justify ="center")
Title_Label.grid(row=0,column=0)
MainFrame = Frame(root,bg = '#e6e5e5',pady = 2, width =200, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)

Label_2 =Label(MainFrame, font=('lato black', 17,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=0, column=0)

Label_1 =Label(MainFrame, font=('lato black', 19,'bold'), text=" Sender's Email : ",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=1, column=0,sticky=W)

Entry_1=Entry(MainFrame,font=('arial',12,'bold'),bd=2,fg="black",textvariable= sender_email, width=35,
justify=LEFT).grid(row=1,column=1)

Label_1 =Label(MainFrame, font=('lato black', 19,'bold'), text=" Sender's Password :",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=2, column=0,sticky=W)

Entry_1=Entry(MainFrame,font=('arial',12,'bold'),bd=2,fg="black",textvariable= sender_pw,show='*', width=35,
justify=LEFT).grid(row=2,column=1)

Label_2 =Label(MainFrame, font=('lato black', 17,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=3, column=0)
Label_2 =Label(MainFrame, font=('lato black', 17,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=4, column=0)

Label_2 =Label(MainFrame, font=('lato black', 19,'bold'), text=" Reciever's Email :",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=5, column=0,sticky=W)

Entry_2=Entry(MainFrame,font=('arial',12,'bold'),bd=2,fg="black",textvariable= reciever_email, width=35,
justify=LEFT).grid(row=5,column=1)


Label_2 =Label(MainFrame, font=('lato black', 19,'bold'), text=" Subject :",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=6, column=0,sticky=W)

Entry_2=Entry(MainFrame,font=('arial',12,'bold'),bd=2,fg="black",textvariable= subject_variable, width=70,
justify=LEFT).grid(row=6,column=1)

Label_2 =Label(MainFrame, font=('lato black', 19,'bold'), text=" Message :",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=7, column=0,sticky=W)

Label_9=Entry(MainFrame,font=('arial',12,'bold'),bd=2,fg="black",textvariable= message_variable, width=70,justify=LEFT).grid(row=7,column=1,sticky=E)

Label_2 =Label(MainFrame, font=('lato black', 17,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=8, column=0)
Label_2 =Label(MainFrame, font=('lato black', 17,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_2.grid(row=9, column=0)



Label_10 =Button(MainFrame, font=('arial', 20,'bold'), text="Send Email",padx=2,pady=2, bg="blue",fg = "white",command=send_email_new)
Label_10.grid(row=10, column=0,sticky=W)

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/New_Logo_Gmail.svg/1200px-New_Logo_Gmail.svg.png"
local_image_filename = wget.download(image_url)
print(local_image_filename)
img = cv2.imread(local_image_filename)
img = cv2.resize(img,(100,76))
cv2.imwrite('gmail.png',img)
img = ImageTk.PhotoImage(Image.open("gmail.png"))
panel = Label(MainFrame, image = img).grid(row=1,column=1,sticky=E)


root.mainloop()









