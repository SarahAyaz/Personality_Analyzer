from tkinter import *
from tkinter import PhotoImage
import random

winGeometry="1600x700+0+0"
winHeading="PERSONALITY ANALYZER"
option1="Yes"
option2="No"
Bttnheight=1
Bttnwidth=10
fontType="Maiandra"
fontStyle="bold"
HeadingSize=18
BttnSize=14
TextSize=11
bgColor="White"
fgColor="Purple"
PicHeight=250
PicWidth=300
backgroundImage="background.png"
button_bg="lightPink"

#Start quiz on button click
def start():
    global winGeometry
    global window
    global fontType
    global HeadingSize
#    window.destroy()
    win1=Toplevel()
    background_image= PhotoImage(file=backgroundImage)
    background_label = Label(win1, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    win1.title('Personality Analyzer')
    win1.geometry(winGeometry)
    heading=Label(win1,text=winHeading, relief=RAISED, fg=fgColor ,bg=bgColor,height=2,width=40, font=(fontType,HeadingSize,fontStyle))
    heading.pack()
    window=win1
#    bottom = Frame(window)
#    bottom.pack(side=BOTTOM, expand=True)
#    Q = Button(window, text ="Quit", fg="yellow",bg="Green", height=Bttnheight, width=Bttnwidth, command =  QuitApp)
#    Q.pack(in_=bottom, side=LEFT)
#    Q.config(font=(fontType,BttnSize))
    GenQues()
    window.mainloop()
    
#Quit application on button click
def QuitApp():
    global window
    mainWin.destroy()

#Generating questions
def GenQues():
    global personality
    global questionsPerWindow
    global fileAnswer
    global countfileAnswer
    global r
    global window
    global radiobtns
    global Bttnheight
    global Bttnwidth
    global fontType
    global BttnSize
    global TextSize
    global R3
    global R4
    QuesFile = open("Questions//"+personalities[personality], "r+")
    AnsFile=open("Answers//"+personalities[personality], "r+")
    ques = QuesFile.read();
    ans =AnsFile.read();
    questions=(ques.split('#'))
    answers=(ans.split('#'))
    ques1Index=random.randrange(9)
    question1=Label(window,text=questions[ques1Index])
    fileAnswer[countfileAnswer]=answers[ques1Index]
    countfileAnswer+=1
    question1.pack()
    question1.config(font=(fontType,TextSize,fontStyle), bg=bgColor, fg=fgColor)
    R1=Radiobutton(window,text=option1, variable=r[radiobtns], value="yes", command=selected1)
    R2=Radiobutton(window, text=option2, variable=r[radiobtns], value="no", command=selected1)
    R1.pack()
    R2.pack()
    R1.config(font=(fontType,TextSize,fontStyle), bg=bgColor, fg=fgColor)
    R2.config(font=(fontType,TextSize,fontStyle), bg=bgColor, fg=fgColor)
    questionsPerWindow+=1
    r[radiobtns].set(None)
    radiobtns+=1
    ques2Index=random.randrange(9)
    while ques2Index==ques1Index:
        ques2Index=random.randrange(9)
    question2=Label(window,text=questions[ques2Index])
    fileAnswer[countfileAnswer]=answers[ques2Index]
    countfileAnswer+=1
    question2.pack()
    question2.config(font=(fontType,TextSize,fontStyle), bg=bgColor, fg=fgColor)
    R3=Radiobutton(window, text=option1, variable=r[radiobtns], state=DISABLED, value="yes", command=selected2)
    R4=Radiobutton(window,text=option2,variable=r[radiobtns], state=DISABLED, value="no", command=selected2)
    R3.pack()
    R4.pack()
    R3.config(font=(fontType,TextSize,fontStyle), bg=bgColor, fg=fgColor)
    R4.config(font=(fontType,TextSize,fontStyle), bg=bgColor, fg=fgColor)
    questionsPerWindow+=1
    r[radiobtns].set(None)
    radiobtns+=1
    #Create a new window after every 6 questions
    if (questionsPerWindow%6)==0:
        #Create description window after all 30 questions
        if questionsPerWindow==30:
            top = Frame(window)
#            bottom = Frame(window)
            top.pack(side=TOP)
#            bottom.pack(side=BOTTOM, expand=True)
            B = Button(window, text ="Next", relief=RAISED, fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command =  EvalPersonality)
            B.pack(in_=top, side=RIGHT)
            B.config(font=(fontType,BttnSize,fontStyle))
            Q = Button(window, text ="Quit", relief=RAISED, fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command =  QuitApp)
            Q.pack(in_=top, side=LEFT)
            Q.config(font=(fontType,BttnSize,fontStyle))
        else:
            top = Frame(window)
#            bottom = Frame(window)
            top.pack(side=TOP)
#            bottom.pack(side=BOTTOM, expand=True)
            B = Button(window, text ="Next", relief=RAISED, fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command =  New_Window)
            B.pack(in_=top, side=RIGHT)
            B.config(font=(fontType,BttnSize,fontStyle))
            Q = Button(window, text ="Quit", relief=RAISED, fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command =  QuitApp)
            Q.pack(in_=top, side=LEFT)
            Q.config(font=(fontType,BttnSize,fontStyle))

#Creating window2
def New_Window():
    global winGeometry
    global window
    global fontType
    global HeadingSize
#    window.destroy()
    new_win=Toplevel()
    background_image= PhotoImage(file=backgroundImage)
    background_label = Label(new_win, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    new_win.title('Personality Analyzer')
    new_win.geometry(winGeometry)
    heading=Label(new_win,text=winHeading, relief=RAISED, fg=fgColor,bg=bgColor,height=2,width=40, font=(fontType,HeadingSize,fontStyle))
    heading.pack()
    window=new_win
#    bottom = Frame(window)
#    bottom.pack(side=BOTTOM, expand=True)
#    Q = Button(window, text ="Quit", fg="yellow",bg="Green", height=Bttnheight, width=Bttnwidth, command =  QuitApp)
#    Q.pack(in_=bottom, side=LEFT)
#    Q.config(font=(fontType,BttnSize))
    GenQues()
    window.mainloop()

#Evaluate Personality
def EvalPersonality():
    global validAnswers
    global userAnswer
    global fileAnswer
    global personality
    global description
    global types
    global window
    personality=0
    for i in range(types):
#        description+=userAnswer[i]
        if userAnswer[i]==fileAnswer[i]:
            validAnswers+=1
            if validAnswers==2:
                DescFile=open("Descriptions//"+personalities[personality], "r+")
                description+=DescFile.read()
        if i!=0 and i%2==0:
            personality+=1
            validAnswers=0
    if description=="":
        description+="You have not taken the quiz honestly. Sorry! The system can't generate your result."
    DescWindow()

#Creating final description window
def DescWindow():
    #Creating New Window on Button Click!!
    global winGeometry
    global fontType
    global HeadingSize
    global TextSize
    global window
#    window.destroy()
    win=Toplevel()
    background_image= PhotoImage(file=backgroundImage)
    background_label = Label(win, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    win.title('Personality Analyzer')
    win.geometry(winGeometry)
    heading=Label(win,text=winHeading, relief=RAISED, fg=fgColor, bg=bgColor, height=1, width=40, font=(fontType,HeadingSize,fontStyle))
    heading.pack()
    result=Label(win,text="Your Result: ", fg=fgColor, bg=bgColor, height=2, width=30, font=(fontType,14,fontStyle))
    result.pack()
    txt_frm = Frame(win, width=600, height=300)
    txt_frm.pack()
    txt_frm.grid_propagate(False)
    txt_frm.grid_rowconfigure(0, weight=1)
    txt_frm.grid_columnconfigure(0, weight=1)
    txt = Text(txt_frm, borderwidth=3)
    txt.config(font=(fontType, TextSize), undo=True, wrap=WORD)
    txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    txt.insert(END,description)
    txt.configure(state=DISABLED)
    scrollb = Scrollbar(txt_frm, command=txt.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')
    txt['yscrollcommand'] = scrollb.set
    Q = Button(win, text ="Quit", relief=RAISED, fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command =  QuitApp)
    Q.pack()
    Q.config(font=(fontType,BttnSize,fontStyle))
    window=win
    window.mainloop()

#Collecting answers of selected radiobuttons
def selected1():
    global r
    global radioans
    global userAnswer
    global countuserAnswer
    global R3
    global R4
    R3.config(state=NORMAL)
    R4.config(state=NORMAL)
    userAnswer[countuserAnswer]=r[radioans].get()
    radioans+=1
    countuserAnswer+=1
    
def selected2():
    global personality
    global r
    global radioans
    global questionsPerWindow
    global userAnswer
    global countuserAnswer
    userAnswer[countuserAnswer]=r[radioans].get()
    radioans+=1
    countuserAnswer+=1
    personality+=1
    if (questionsPerWindow%6)!=0:
        GenQues() 

#Creating main window
mainWin=Tk()
background_image= PhotoImage(file=backgroundImage)
background_label = Label(mainWin, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
mainWin.title('Personality Analyzer')
mainWin.geometry(winGeometry)
heading=Label(mainWin,text=winHeading,relief=RAISED, fg=fgColor,bg=bgColor ,height=2,width=40, font=(fontType,HeadingSize,fontStyle))
heading.pack()

window=mainWin

#Top frames
blank1=Frame(window)
blank1.pack(side=TOP)
first = Frame(window)
first.pack(side=TOP)
second=Frame(window)
second.pack(side=TOP)
#blank2=Frame(window)
#blank2.pack(side=TOP)
third=Frame(window)
third.pack(side=TOP)
forth=Frame(window)
forth.pack(side=TOP)
#blank3=Frame(window)
#blank3.pack(side=TOP)

blank_label1=Label(mainWin).pack(in_=blank1)

label1_image=PhotoImage(file="clock.png")
time_image=Label(mainWin, image=label1_image, height=PicHeight, width=PicWidth).pack(in_=first, side=LEFT)
time=Label(mainWin, font=(fontType,TextSize,fontStyle), fg=fgColor, bg=bgColor, text="This application analyze your persnality in less than 15 minutes.").pack(in_=second, side=LEFT)

label2_image=PhotoImage(file="honest.png")
honest_image=Label(mainWin, image=label2_image, height=PicHeight, width=PicWidth).pack(in_=first, side=RIGHT)
honest=Label(mainWin, font=(fontType,TextSize,fontStyle), fg=fgColor, bg=bgColor, text="Please, be honest while you are selecting the answers.").pack(in_=second, side=RIGHT)

#blank_label2=Label(mainWin).pack(in_=blank2)

label3_image=PhotoImage(file="privacy.png")
privacy_image=Label(mainWin, image=label3_image, height=PicHeight, width=PicWidth).pack(in_=third, side=LEFT)
privacy=Label(mainWin, font=(fontType,TextSize,fontStyle), fg=fgColor, bg=bgColor, text="Your personality description will not be shared anywhere.").pack(in_=forth, side=LEFT)

label4_image=PhotoImage(file="uncheck.png")
uncheck_image=Label(mainWin, image=label4_image, height=PicHeight, width=PicWidth).pack(in_=third, side=RIGHT)
uncheck=Label(mainWin, font=(fontType,TextSize,fontStyle), fg=fgColor, bg=bgColor, text="DO NOT leave any answer unselected and DO NOT change your answer.").pack(in_=forth, side=RIGHT)

#blank_label3=Label(mainWin).pack(in_=blank3)

#Bottom frames
bottom = Frame(window)
bottom.pack(side=BOTTOM)
B = Button(window, text ="Start", relief=RAISED, fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command= start)
B.pack(in_=bottom, side=RIGHT)
B.config(font=(fontType,BttnSize,fontStyle))
Q = Button(window, text ="Quit", relief=RAISED,  fg=fgColor, bg=button_bg, height=Bttnheight, width=Bttnwidth, command =  QuitApp)
Q.pack(in_=bottom, side=LEFT)
Q.config(font=(fontType,BttnSize,fontStyle))

#initialization
types=30
personalities=["Anxiety.txt","Femininity.txt","Flexibility.txt","Independance.txt","Intellectual Efficiency.txt",
"Leadership.txt","Managerial Potential.txt","Responsibility.txt","Self Acceptance.txt","Self Control.txt","Sociability.txt",
"Tolerance.txt","Tough Mindedness.txt","Well-being.txt","Work Orientation.txt"]
description=""
userAnswer=["" for i in range(types)]
R3=Radiobutton()
R4=Radiobutton()
r=[StringVar() for i in range(types)]
fileAnswer=["" for i in range(types)]
#counters
validAnswers=0
personality=0
questionsPerWindow=0
radiobtns=0
radioans=0
countfileAnswer=0
countuserAnswer=0
 
mainWin.mainloop()