from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout,QVBoxLayout,QPushButton,QTextEdit,QLabel,QSpinBox
from PyQt5.QtGui import QFont
import sys

#Κλάση του κυρίως παραθύρου
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Τίτλος του κυρίου παραθύρου
        self.setWindowTitle("Κρυπτογράφηση/Αποκρυπτογράφηση Καίσαρα")

        #Χρώμα του κυριώς παραθύρου σε rgb
        self.setStyleSheet("background-color: rgb(90, 90, 90);")

        #Mέγεθος κυρίου παραθύρου
        self.resize(800, 700)

        #Εικόνα εφαρμογής
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("63de39d13acc0b1d9c4fcedab763686e.jpg"))
        self.setWindowIcon(icon)


        #Όλα τα widgets του κύριου παραθύρου
        self.title = Title("Κρυπτογράφηση Καίσαρα")

        self.input = Input("Γράψε κείμενο, επέλλεξε shift και κρυπτογράφησε/αποκρυπτογράφησε το.")
        
        
        self.b1 = Button("Κρυπτογράφησε")
        self.b1.clicked.connect(self.getcipher) 
        
        self.shift = Shift(1,22)
        
        self.b2 = Button("Αποκρυπτογράφησε")
        self.b2.clicked.connect(self.getdecipher)
        
        self.output_e = Output("Κρυπτογραφημένο Κείμενο")
        self.output_d  = Output("Αποκρυπτογραφημένο Κείμενο")
        
        

        #Τα layouts του παραθύρου
        vertical = QVBoxLayout()
        vertical_2 = QVBoxLayout()
        horizontal_1 = QHBoxLayout()
        horizontal_2 = QHBoxLayout()
        
        #Το vertical είναι το parent των horizontal_1 & horizontal_2
        vertical.addLayout(vertical_2)
        vertical.addLayout(horizontal_1)
        vertical.addLayout(horizontal_2)
        
        #Προσθέτω τα widgets στα κατάλληλα layout
        vertical_2.addWidget(self.title)
        vertical_2.addWidget(self.input)
        horizontal_1.addWidget(self.b1,stretch=2)
        horizontal_1.addWidget(self.shift,stretch=0)
        horizontal_1.addWidget(self.b2,stretch=2)
        horizontal_2.addWidget(self.output_e)
        horizontal_2.addWidget(self.output_d)

        #Ορίζω το κεντρικό widget το οποίο είναι το parent όλων των layout & widget
        central_widget = QWidget()
        central_widget.setLayout(vertical)
        self.setCentralWidget(central_widget)

    def getcipher(self):   #μέθοδος που κάνει την κωδικοποίηση μέσω των γραφικών
    
        Entry=str(self.input.toPlainText())
        entry=int(self.shift.value())
        c=Cipher(Entry,entry)
        c.change()
        f=open('Cipher.txt','a',encoding='utf-8') #Κάθε κωδικποίηση γράφεται σε ένα αρχείο, σαν ιστορικό
        f.write(f'{Entry}==>{c}\n')
        f.close()
        self.output_e.setText(f'{Entry}==>{c}')
        
    

    def getdecipher(self):#Μέθοδος που κάνει την αποκωδικοποίηση μέσω των γραφικών
    
        Entry=str(self.input.toPlainText())
        entry=int(self.shift.value())
        c=Decipher(Entry,entry)
        c.change()
        f=open('Decipher.txt','a',encoding='utf-8')#Ομοίως σε άλλο αρχείο γράφει αυτά που αποκωδικοποιήθηκαν
        f.write(f'{Entry}==>{c}\n')
        f.close()
        self.output_d.setText(f'{Entry}==>{c}')

        


#Οι κλάσεις των widget
class Button(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.setFont(QFont("Arial",12))


class Input(QTextEdit):
    def __init__(self,text):
        super().__init__()
        self.setPlaceholderText(text)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setFont(QFont("Arial",12))
        

class Output(QTextEdit):
    def __init__(self,text):
        super().__init__()
        self.setPlaceholderText(text)
        self.setReadOnly(True)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setFont(QFont("Arial",12))

class Title(QLabel):
    def __init__(self,text):
        super().__init__()
        self.setText(text)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial",30))
        
        

class Shift(QSpinBox):
    def __init__(self,minimum,maximum):
        super().__init__()
        self.setMinimum(minimum)
        self.setMaximum(maximum)
        self.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.setFont(QFont("Arial",12))


import string
#Κώδικας για Κωδικοποίηση/Αποκωδηκοποίηση
class Cipher:                                   
    def __init__(self,text,move):           #κλάση που κάνει την κωδικοποίηση
        self.string=text
        self.fr=[]
        self.move=move
        self.dict_lower={'ά':'α','έ':'ε','ό':'ο','ί':'ι','ύ':'υ','ώ':'ω','ή':'η','ς':'σ','ϊ':'ι','ϋ':'υ','ΐ':'ι','ΰ':'υ'}  #
        self.dict_upper={'Ά':'Α','Έ':'Ε','Ί':'Ι','Ύ':'Υ','Ώ':'Ω','Ό':'Ο','Ή':'Η','ΐ':'ι','ΰ':'υ'}
        self.list_others=[i for i in string.punctuation] # μέσω του Library string φτιάχνουμε λίστα με τά σύμβολα
        self.list=[chr(n) for n in range(945,970)]      #short list με τα μικρά γράμματα της αλφαβήτου μέσω των κωδικών τους στο Ubicode
        self.list_upper = [i.upper() for i in self.list] 
        self.list_upper = self.list_upper +self.list_upper #Προσθέτουμε την λίστα στον εαυτό της ώστε να μπορει η προσθήκη της μετατόπισης να μην ξεπερνάει τα όρια της λίστας
        self.list=self.list+self.list
        self.l=[]
        self.kyes_lower=self.dict_lower.keys()
        self.kyes_upper=self.dict_upper.keys()
        self.list_eng=[chr(l) for l in range(97, 123)] #short list με αγγλικούς χαρακτήρες μικρούς απο Unicode
        self.list_eng_upper=[chr(m) for m in range(65, 91)] #short list με αγγλικούς χαρακτήρες κεγαλαίους απο Unicode
        self.list_eng=self.list_eng+self.list_eng
        self.list_eng_upper=self.list_eng_upper+self.list_eng_upper

    def change(self): #Μέθοδος που ελένχει τι τύπος, και σε ποιά λίστα ανήκει ο κάθε χαρακτήρας , τον αλλάζει αν χρειάζεται, και μετατοπίζει τους χαρκτήρες οπου είναι αναγκαίο
        for i in self.string: #Μετατρέπει σε λίστα το Text
            self.l.append(i)
        for i in self.l:    #Αν έχει τόνο ή διαλυτικά , του τα αφαιρεί
            if i in self.kyes_lower:                    
                self.l[self.l.index(i)]=self.dict_lower[i]        
            elif i in self.kyes_upper:
                self.l[self.l.index(i)]=self.dict_upper[i]
        for i in self.l:  #Μετατοπίζει τα γράμματα ανάλογα με το αν είναι κεφαλαία,μικρά,αγγλικά,ελληνικά
            if i in self.list_upper:
                ins=self.list_upper.index(i)
                mo=ins+self.move
                self.fr.append(self.list_upper[mo])
            elif i in self.list_eng_upper:
                ins = self.list_eng_upper.index(i) 
                mo = ins + self.move
                self.fr.append(self.list_eng_upper[mo])
            elif i != ' ':
                if i in self.list_others: #Άν έιναι σύμβολο ένας χαρακτήρας τον αφήνει ίδιο 
                    self.fr.append(i) 
                elif i in self.list_eng:
                    b=self.list_eng.index(i)
                    g=b+self.move
                    self.fr.append(self.list_eng[g])
                elif i in self.list:
                    b=self.list.index(i)
                    g=b+self.move
                    self.fr.append(self.list[g])
                else:# Άν δεν έιναι τίποτα απο τα προηγούμενα ο χαρακτήρας(άρα αριθμός) τον προσθέτει ίδιο
                    self.fr.append(i)
            elif i == ' ': #Το κενό το προσθέτει όπως είναι
                self.fr.append(' ')

    def __str__(self):
        return ''.join(self.fr)


class Decipher:#Ομοίως με την κλάση Cipher λειτουργεί η Decipher
    def __init__(self,text,move):
        self.string=text
        self.move=move
        self.fe=[]
        self.dict_lower={'ά':'α','έ':'ε','ό':'ο','ί':'ι','ύ':'υ','ώ':'ω','ή':'η','ς':'σ','ϊ':'ι','ϋ':'υ','ΐ':'ι','ΰ':'υ'}
        self.dict_upper={'Ά':'Α','Έ':'Ε','Ί':'Ι','Ύ':'Υ','Ώ':'Ω','Ό':'Ο','Ή':'Η','Ϊ':'Ι','Ϋ':'Υ'}
        self.list_others=[i for i in string.punctuation]
        self.list=[chr(n) for n in range(945,970)]
        self.list_upper = []
        self.list_upper = [i.upper() for i in self.list]
        self.list_upper = self.list_upper +self.list_upper
        self.list=self.list+self.list
        self.l=[]
        self.kyes_lower=self.dict_lower.keys()
        self.kyes_upper=self.dict_upper.keys()
        self.list_eng=[chr(l) for l in range(97, 123)]
        self.list_eng_upper=[chr(m) for m in range(65, 91)]
        self.list_eng=self.list_eng+self.list_eng
        self.list_eng_upper=self.list_eng_upper+self.list_eng_upper

    def change(self):
        
        for i in self.string:
            self.l.append(i)
        for i in self.l:
            if i in self.kyes_lower:
                self.l[self.l.index(i)]=self.dict_lower[i]        
            elif i in self.kyes_upper:
                self.l[self.l.index(i)]=self.dict_upper[i]
        for i in self.l:
            if i in self.list_upper :
                ins = self.list_upper.index(i) + 25
                mo = ins - self.move
                self.fe.append(self.list_upper[mo])
            elif i in self.list_eng_upper:
                ins = self.list_eng_upper.index(i) + 26
                mo = ins - self.move
                self.fe.append(self.list_eng_upper[mo])
            elif i != ' ':
                if i in self.list_others:
                    self.fe.append(i) 
                elif i in self.list_eng:
                    b=self.list_eng.index(i)+26
                    g=b-self.move
                    self.fe.append(self.list_eng[g])
                elif i in self.list:
                    b=self.list.index(i)+25
                    g=b-self.move
                    self.fe.append(self.list[g]) 
                else:
                    self.fe.append(i)
            elif i== ' ':
                self.fe.append(' ')
            
    def __str__(self):
        return ''.join(self.fe)
        
    

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())