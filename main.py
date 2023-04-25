import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui_v2 import Ui_Form
import numpy as np
import random


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_START.clicked.connect(self.start)
        self.doubleSpinBox_allC.valueChanged.connect(self.update_sum)
        self.doubleSpinBox_allD.valueChanged.connect(self.update_sum)
        self.doubleSpinBox_kD.valueChanged.connect(self.update_sum)
        self.doubleSpinBox_kC.valueChanged.connect(self.update_sum)
        self.doubleSpinBox_kDC.valueChanged.connect(self.update_sum)

    def start(self):
        print("mleczny start")
        self.initialize_data()

    def initialize_data(self):
        M = self.spinBox_Mrows.value()
        N = self.spinBox_Nrows.value()
        CA_states = np.zeros((M + 1, N + 1), dtype=int)
        CA_strat = np.zeros((M + 1, N + 1), dtype=int)
        CA_actions = np.ones((M + 1, N + 1), dtype=int)
        CA_kD_strat = np.full((M+1, N+1), -1, dtype=int)
        CA_kC_strat = np.full((M+1, N+1), -1, dtype=int)
        CA_kDC_strat = np.full((M+1, N+1), -1, dtype=int)
        Group_8_0s = np.zeros((M + 1, N + 1), dtype=int)
        Group_8_1s = np.zeros((M + 1, N + 1), dtype=int)
        if self.checkBox_debug.isChecked() \
                and self.checkBox_read_CA_state_deb.isChecked() \
                and self.checkBox_read_CA_strat_deb.isChecked():
            print("______________wez tu napisz kod___________________")
            # tu trzeba zrobic wczytywanie danych z plików txt do naszych tablic
        else:
            for i in range(1, M + 1):
                for j in range(1, N + 1):
                    x = random.uniform(0, 1)
                    if x <= self.doubleSpinBox_p_init_C.value():
                        CA_states[i][j] += 1
                    else:
                        CA_states[i][j] += 0
        if self.checkBox_debug.isChecked():
            self.print_1(CA_states)
        b1 = self.doubleSpinBox_allC.value()
        b2 = b1 + self.doubleSpinBox_allD.value()
        b3 = b2 + self.doubleSpinBox_kD.value()
        b4 = b3 + self.doubleSpinBox_kC.value()
        b5 = b4 + self.doubleSpinBox_kDC.value()
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                x = random.uniform(0, 1)
                if x <= b1:
                    CA_strat[i][j] += 1
                    break
                if x <= b2:
                    CA_strat[i][j] += 0
                    break
                if x <= b3:
                    CA_strat[i][j] += 2
                    y = random.randint(self.spinBox_min.value(), self.spinBox_max.value())
                    CA_kD_strat[i][j] += y
                    break
                if x <= b4:
                    CA_strat[i][j] += 3
                    y = random.randint(self.spinBox_min.value(), self.spinBox_max.value())
                    CA_kC_strat[i][j] += y
                    break
                CA_strat[i][j] += 4
                y = random.randint(self.spinBox_min.value(), self.spinBox_max.value())
                CA_kDC_strat[i][j] = y
            # tu idk o co mu chodzi, ale chyba bez tego niżej
            # else:
            #     continue
            # break

        if self.checkBox_debug.isChecked():
            self.print_2(CA_strat, CA_kD_strat, CA_kC_strat, CA_kDC_strat)
        Agent_glob_ID = np.zeros((M + 1, N + 1), dtype=int)
        Agent_i_j_ID = np.zeros((M*N, 2), dtype=int)
        Agent_neighbors = np.zeros((M*N, 8), dtype=int)

        if self.checkBox_debug.isChecked():
            self.print_3(Agent_glob_ID, Agent_i_j_ID, Agent_neighbors)
        # utworzenie tablic strategii???
        kD = np.zeros((8, 8), dtype=int)
        kC = np.zeros((8, 8), dtype=int)
        kDC = np.zeros((8, 8), dtype=int)
        if self.checkBox_debug.isChecked():
            self.print_4(kD, kC, kDC)

    def update_sum(self):
        suma = self.doubleSpinBox_allC.value() + self.doubleSpinBox_allD.value() + self.doubleSpinBox_kD.value() + \
               self.doubleSpinBox_kC.value() + self.doubleSpinBox_kDC.value()
        if suma > 1.0:
            sender = self.sender()
            sender.setValue(sender.value() - (suma - 1.0))

    def print_1(self, CA_states):
        print("iterat = 0")
        print(f"CA_states\n{CA_states}")

    def print_2(self, CA_strat, CA_kD_strat, CA_kC_strat, CA_kDC_strat):
        print(f"CA_strat\n{CA_strat}\n")
        print(f"CA_kD_strat\n{CA_kD_strat}\n")
        print(f"CA_kC_strat\n{CA_kC_strat}\n")
        print(f"CA_kDC_strat\n{CA_kDC_strat}\n")

    def print_3(self, Agent_glob_ID, Agent_i_j_ID, Agent_neighbors):
        print(f"Agent_glob_ID\n{Agent_glob_ID}\n")
        print(f"Agent_i_j_ID\n{Agent_i_j_ID}\n")
        print(f"Agent_neighbors\n{Agent_neighbors}\n")

    def print_4(self, kD, kC, kDC):
        print(f"kD\n{kD}\n")
        print(f"kC\n{kC}\n")
        print(f"kDC\n{kDC}\n")

    def STATISTIC_0(self):
        # tutaj giga obliczenia XD
        pass

    def STATISTIC_a(self):
        # tutaj giga obliczenia XD
        pass

    def STATISTIC_b(self):
        # tutaj giga obliczenia XD
        pass

    def main(self):
        for i in range(1, self.spinBox_num_of_iter):
            num_of_strat_chahge = 0
            self.STATISTIC_0()
            self.STATISTIC_a()
            self.STATISTIC_b()
            # zapisz wyniki do "results_a.txt"
            # zapisz wyniki do "results_b.txt"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
