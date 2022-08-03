import random
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
from os.path import expanduser



class MainWindow(QWidget):

    def __init__(self):
        self.Interface()

    def Interface(self):
        super().__init__()  # Iniciliazes the main page
        self.setWindowIcon(QIcon('cadeado.png'))  # defining window icon
        self.setWindowTitle('Password Generator')  # defining window title
        self.setGeometry(150, 150, 500, 500)  # defining screen size
        self.setFixedSize(self.size())  # desabilitando a mudança de tamanho da janela (pois ao abrir a janela, o usuário poderia mudar as dimnsões da mesma manualmente)
        self.background = QLabel(self)
        self.background.setPixmap((QPixmap('cadeado.png')).scaled(580,550))  # defining background image

        text_title = QLabel('Password Generator', self)
        text_title.setFont(QFont('Times New Roman',35))
        text_title.move(70, 50)

        texto_number_of_characters = QLabel('Number of Characters', self)
        texto_number_of_characters.setFont(QFont('Arial', 10))
        # texto_nome.setStyleSheet("border: 1px solid black;")
        texto_number_of_characters.move(175, 160)

        self.box_text_number_of_characters = QLineEdit(self)
        self.box_text_number_of_characters.setPlaceholderText('N° de caracteres')
        self.box_text_number_of_characters.setStyleSheet(''' border: 4px solid black; border-radius: 10px; 
                                                               padding: 0 6px;   background: rgb(255,255,255) ;
                                                               min-width: 8em; selection-background-color: darkgray;''')
        self.box_text_number_of_characters.move(175,190)

        text_number_passwords = QLabel('Number of Generated Passwords', self)
        text_number_passwords.setFont(QFont('Arial', 10))
        text_number_passwords.move(175,240)

        self.box_text_number_of_passwords = QLineEdit(self)
        self.box_text_number_of_passwords.setPlaceholderText('N° de senhas')
        self.box_text_number_of_passwords.setStyleSheet(''' border: 4px solid black; border-radius: 10px; 
                                                               padding: 0 6px;   background: rgb(255,255,255) ;
                                                               min-width: 8em; selection-background-color: darkgray;''') #solid gray
        self.box_text_number_of_passwords.move(175,260)

        self.save_checkbox = QCheckBox('Especial Characters', self)  # Caixa de marcação
        self.save_checkbox.move(175, 300)
        # self.save_checkbox.setStyleSheet('''background-color: rgb(150,150,150); border-style:inset; border-width: 4px;
        #                                                             border-radius: 10px;
        #                                                             border-color: black;
        #                                                             min-width: 5em;
        #                                                             padding: 6px;''')
        # self.save_checkbox.clicked.connect(self.sem_especiais)

        button = QPushButton('Generate Passwords', self)
        button.move(180,350)
        button.setStyleSheet('''background-color: rgb(150,150,150); border-style:inset; border-width: 4px;
                                                                    border-radius: 10px;
                                                                    border-color: black;
                                                                    min-width: 5em;
                                                                    padding: 6px;''')
        button_about = QPushButton('Sobre', self)
        button_about.setStyleSheet('''background-color: rgb(250,250,250); border-style:inset; border-width: 2px;
                                                                   border-radius: 10px;
                                                                   border-color: black;
                                                                   min-width: 3em;
                                                                   padding: 6px;''')
        button_about.move(420, 450)
        button_about.clicked.connect(self.sobre)

        button.clicked.connect(self.check_string)
        # button.clicked.connect(self.confirmar_dados)
        # button.clicked.connect(self.close)

        self.show()


    def check_string(self):
        if self.box_text_number_of_characters.text() in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*?/\?' or self.box_text_number_of_passwords.text() in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*?/\?':
           attention_alert = QMessageBox.information(self, 'ATTENTION','You put words insted of numbers, try again with integers numbers.')
        else:
            self.confirmar_dados()


    def confirmar_dados(self):
        # if self.box_text_number_of_characters.text() == float(self.box_text_number_of_characters.text()) or self.caixa_de_texto_cpf.text() == float(self.caixa_de_texto_cpf.text()):
        self.box_text_number_of_characters_int = int(self.box_text_number_of_characters.text())
        self.box_text_number_of_passwords_int = int(self.box_text_number_of_passwords.text())
        # else:
        #     pass
        confirmacao = QMessageBox.question(self, 'ATENÇÃO', f'''N° de caracteres: {self.box_text_number_of_characters_int}
N° de senhas: {self.box_text_number_of_passwords_int}''', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

        if confirmacao == QMessageBox.StandardButton.Yes and self.save_checkbox.isChecked():
            lower_case = 'abcdefghijklmnopqrstuvwxyz'
            upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            symbols = '@#$%&*?/\?'

            self.generate_password = lower_case + upper_case + numbers + symbols
            self.length_for_password = self.box_text_number_of_characters_int
            self.password_list = []
            arquivo = open('SENHAS_GERADAS.txt', 'w')
            for i in range(self.box_text_number_of_passwords_int):
                password = ''.join(random.sample(self.generate_password, self.length_for_password))
                self.password_list.append(password)
                arquivo.write(f'Senha {i}: {self.password_list[i]} \n')
                arquivo.write('*********************\n')
            arquivo.close
            # # print(self.password_list)
            self.interface_senhas()
        elif confirmacao == QMessageBox.StandardButton.Yes and not self.save_checkbox.isChecked():
            lower_case = 'abcdefghijklmnopqrstuvwxyz'
            upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'

            self.generate_password = lower_case + upper_case + numbers
            self.length_for_password = self.box_text_number_of_characters_int
            self.password_list = []
            arquivo = open('GENERATED_PASSWORDS.txt', 'w')
            for i in range(self.box_text_number_of_passwords_int):
                password = ''.join(random.sample(self.generate_password, self.length_for_password))
                self.password_list.append(password)
                arquivo.write(f'Password {i}: {self.password_list[i]} \n')
                arquivo.write('*********************\n')
            arquivo.close
            # # print(self.password_list)
            self.interface_senhas()
        else:
            self.Interface()

    def interface_senhas(self):
        super().__init__()  # Inicializa a página
        self.setWindowIcon(QIcon('cadeado.png'))  # definindo o icone da janela
        self.setWindowTitle('Generated Passwords')  # definindo um título para a janela
        self.setGeometry(150, 150, 500, 500)  # definindo o tamanho da tela
        self.setFixedSize(self.size())  # desabilitando a mudança de tamanho da janela (pois ao abrir a janela, o usuário poderia mudar as dimnsões da mesma manualmente)
        # self.setStyleSheet('background-color: rgb(200,200,200)') #definindo a cor de fundo da tela
        self.background = QLabel(self)
        self.background.setPixmap((QPixmap('cadeado.png')).scaled(580,550))
        texto_titulo = QLabel('Senhas Geradas', self)
        texto_titulo.setFont(QFont('Times New Roman', 25))
        texto_titulo.move(150, 30)
        height = 100
        #height_button = 80
        count = 1
        for number in range(len(self.password_list)):
            length = 195
            self.box_text = QLineEdit(self)
            self.box_text.setText(f'{self.password_list[number]}') #Como setar o texto sem o placeholdertext
            self.box_text.setReadOnly(True)
            self.box_text.move(length,height)
            self.box_text.setStyleSheet(''' border: 2px solid gray; border-radius: 10px;
                                                        padding: 0 6px;   background: rgb(200,200,200) ;
                                                        min-width: 8em; selection-background-color: darkgray;''')
            self.box_text_password = QLabel(f'Password {count}:' ,self)
            self.box_text_password.setFont(QFont('Times New Roman',12))
            self.box_text_password.move(110,height)
            # botao_copia_cola = QPushButton('', self)
            # botao_copia_cola.setIcon(QIcon('copiar_colar.png'))
            # botao_copia_cola.setStyleSheet('background-color: rgb(255,255,255); border-color: black')
            # botao_copia_cola.setGeometry(100, 100, 30, 30)
            # botao_copia_cola.move(length + 150, height_button)
            # botao_copia_cola.clicked.connect(self.copiar_colar)
            height += 40
            # height_button += 45
            count += 1

        button_leave = QPushButton('Sair',self)
        button_leave.clicked.connect(self.sair)
        button_leave.move(300,430)
        button_leave.setStyleSheet('''background-color: rgb(150,150,150); border-style:inset; border-width: 4px;
                                                                border-radius: 10px;
                                                                border-color: black;
                                                                min-width: 5em;
                                                                padding: 6px;''')
        button_back = QPushButton('Voltar', self)
        button_back.move(80, 430)
        button_back.setStyleSheet('''background-color: rgb(150,150,150); border-style:inset; border-width: 4px;
                                                                            border-radius: 10px;
                                                                            border-color: black;
                                                                            min-width: 5em;
                                                                            padding: 6px;''')

        button_back.clicked.connect(self.Interface)
        button_back.clicked.connect(self.close)


        self.show()

    def sobre(self):
        sobre = QMessageBox.information(self, 'Solutions C.A', '''
    Powered By: Barbosa, R.D .
    All Rights Reserverd''')  # Definindo mensagem de informação

    def sair(self):
        aviso = QMessageBox.information(self, 'Solutions C.A', '''If a large number of passwords are generated,
        a file "GENERATED PASSWORDS.txt" was generated with all the generated passwords on directory where the code is located.''')
        sys.exit(qt.exec())


qt = QApplication(sys.argv)
app = MainWindow()
sys.exit(qt.exec())


