from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,
    QHBoxLayout,QVBoxLayout,
    QGroupBox,QButtonGroup,QRadioButton,
    QPushButton,QLabel)
from random import randint,shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('холм','pagorek','bugor','kopcow','helm'))
questions_list.append(Question('деревня','wioska','woiska','woinstva','wilena'))
questions_list.append(Question('город','miasto','miejsce','grad','gurat'))
questions_list.append(Question('ель','swierk','sosna','cholka','picea'))
app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
rbnt_1 = QRadioButton('Вариант 1')
rbnt_2 = QRadioButton('Вариант 2')
rbnt_3 = QRadioButton('Вариант 3')
rbnt_4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbnt_1)
RadioGroup.addButton(rbnt_2)
RadioGroup.addButton(rbnt_3)
RadioGroup.addButton(rbnt_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbnt_1)
layout_ans2.addWidget(rbnt_2)
layout_ans3.addWidget(rbnt_3)
layout_ans3.addWidget(rbnt_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment = Qt.AlignHCenter,stretch = 2)
AnsGroupBox.setLayout(layout_res)
Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()
Layout_line1.addWidget(lb_Question,alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
Layout_line2.addWidget(RadioGroupBox)
Layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
Layout_line3.addStretch(1)
Layout_line3.addWidget(btn_OK,stretch = 2)
Layout_line3.addStretch(1)
Layout_card = QVBoxLayout()
Layout_card.addLayout(Layout_line1,stretch = 2)
Layout_card.addLayout(Layout_line2,stretch = 8)
Layout_card.addStretch(1)
Layout_card.addLayout(Layout_line3,stretch = 1)
Layout_card.addStretch(1)
Layout_card.setSpacing(5)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbnt_1.setChecked(False)
    rbnt_2.setChecked(False)
    rbnt_3.setChecked(False)
    rbnt_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbnt_1,rbnt_2,rbnt_3,rbnt_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Наверно!')
def next_question():
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
window = QWidget()    
window.setLayout(Layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK)
next_question()
window.resize(400,300)
window.show()
app.exec()