#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLabel,QRadioButton,QGroupBox,QHBoxLayout,QButtonGroup
from random import randint
from random import shuffle

points = 0

def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.hide()
    AnswerGroupBox.show()
    answer.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    ResultGroupBox.hide()
    AnswerGroupBox.hide()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


app = QApplication([])
my_win = QWidget()
my_win.resize(400,200)

my_win.setWindowTitle('Memory card')

answer = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')

AnswerGroupBox= QGroupBox()
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioGroupBox.setLayout(layout_1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnswerGroupBox)
layout_line3.addWidget(answer)
AnswerGroupBox.hide()
g_layout = QVBoxLayout()

ResultGroupBox = QGroupBox('Результат теста')
lb_Result_test = QLabel('?')
layout_res_test = QVBoxLayout()
layout_res_test.addWidget(lb_Result_test ,alignment =Qt.AlignHCenter)
ResultGroupBox.setLayout(layout_res_test)
layout_line2.addWidget( ResultGroupBox)
ResultGroupBox.hide()

g_layout.addLayout(layout_line1)
g_layout.addLayout(layout_line2)
g_layout.addLayout(layout_line3)

my_win.setLayout(g_layout)

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
layout_res.addWidget(lb_Result)
AnswerGroupBox.setLayout(layout_res)   
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer =right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)   
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)  
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    global points 
    if answers[0].isChecked():
        show_correct('Правильно!')
        points += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Не правильно!')

def next_question():
    my_win.cur_question += 1
    if my_win.cur_question >= len(questions_list):
        show_result_test()
        return None 
    q = questions_list[my_win.cur_question]   
    ask(q)


def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def show_result_test():
    global points
    my_win.cur_question = -1
    RadioGroupBox.hide()
    AnswerGroupBox.hide()
    ResultGroupBox.show()
    lb_Result_test.setText('Ваш результат- '+ str(points)+ ' из '+ str(len(questions_list)))
    answer.setText('Начать заново')
    points = 0





my_win.cur_question = -1

questions_list = []
questions_list.append(Question('Какой государственный язык Бразилии?','Португальский','Бразильский','Испанский','Немецкий'))
questions_list.append(Question('169/13 = ','13','14','12','11'))
questions_list.append(Question('Сколько длилась столетняя война?','116','100','120','119'))

next_question()

answer.clicked.connect(click_ok)

my_win.show()
app.exec()