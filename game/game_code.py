import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow import Ui_MainWindow
import random
import pymorphy2


class MyWidget(QMainWindow, Ui_MainWindow):
    def restart(self):
        self.tips.setText('Нажмите START для начала игры')
        self.levels = [(100, [1, 3], [0, 2], 10),
                       (500, [5, 10], [4, 6], 100),
                       (10000, [10, 50], [10, 30], 1000),
                       (1000000, [50, 100], [40, 60], 10000),
                       (1000000000, [100, 1000], [90, 600], 100000)]
        self.items = ['урон', 'сила', 'аптечка', 'None']
        self.lvl = 0
        self.udari = 0
        self.heals = 0
        self.sila = 10
        with open('main_scene_text', 'r') as main_scene_text:
            main_scene_text = main_scene_text.read()
        self.main_scene.setPlainText(main_scene_text)
        self.btn.setText('START')
        self.btn.clicked.connect(self.fight)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.funcss = {'Вылечиться': self.heal, 'Показать статистику': self.stats,
                       'Силы до следующего уровня': self.next_lvl}
        self.funcs.addItems(list(self.funcss.keys()))
        self.funcs.activated[str].connect(self.onActivated)
        self.restart()

    def onActivated(self, el):
        self.funcss[el]()

    def info(self):
        if self.sila >= 1000000000:
            QMessageBox.about(self, 'Information', 'Producer: Timerkhan Giniyatyllin\n' +
                              'Writer: Irek Valeev')

    def fight(self):
        self.tips.setText(
            'Нажимайте FIGHT для нанесения ударов. '
            'Набирая силу, вы будете подниматься по уровням. '
            'Вас также могут атаковать противники')
        self.btn.setText('FIGHT')
        dmg_to_enemy = random.randint(self.levels[self.lvl][1][0], self.levels[self.lvl][1][1])
        dmg_to_me = random.randint(self.levels[self.lvl][2][0], self.levels[self.lvl][2][1])
        self.sila += (dmg_to_enemy - dmg_to_me)
        self.hp.setProperty("value", self.sila)
        morph = pymorphy2.MorphAnalyzer()
        word = morph.parse('сила')[0]
        self.main_scene.appendPlainText('+' + str(dmg_to_enemy) + ' '
                                        + word.make_agree_with_number(dmg_to_enemy).word + '.')
        self.main_scene.appendPlainText('-' + str(dmg_to_me) + ' '
                                        + word.make_agree_with_number(dmg_to_me).word + '.')
        self.udari += 1
        if self.udari % self.levels[self.lvl][3] == 0:
            a = self.items[random.randint(0, len(self.items) - 1)]
            self.main_scene.appendPlainText('Воодушевление. Вы нашли сундук с припасами...')
            if a == 'урон':
                self.levels[self.lvl][1][0] *= 2
                self.levels[self.lvl][1][1] *= 2
                self.main_scene.appendPlainText('Ваш урон повысился вдвое')
            elif a == 'сила':
                self.sila += random.randint(self.levels[self.lvl][1][0], self.levels[self.lvl][1][1]) * 2
                self.main_scene.appendPlainText('Ваша сила увеличилась вдвое')
            elif a == 'None':
                self.main_scene.appendPlainText('Сегодня не ваш день...')
                self.levels[self.lvl][2][0] *= 2
                self.levels[self.lvl][2][0] *= 2
                self.main_scene.appendPlainText('Урон противников увелисился вдвое')
            else:
                self.main_scene.appendPlainText('+1 аптечка')
                self.heals += 1
        if self.sila >= self.levels[self.lvl][0]:
            self.lvl += 1
            QMessageBox.about(self, 'New level', 'Вы перешли на новый уровень!')
            self.hp.setProperty('maximum', self.levels[self.lvl][0])
        if self.sila <= 0:
            message = QMessageBox.question(self, 'Game Over', 'Это же не конец?...',
                                           QMessageBox.Yes | QMessageBox.Cancel)
            if message == QMessageBox.Yes:
                self.restart()
            else:
                self.close()

    def heal(self):
        if self.heals > 0:
            t = random.randint(self.levels[self.lvl][1][0], self.levels[self.lvl][1][1])
            self.sila += t
            self.heals -= 1
            self.hp.setProperty("value", self.sila)
            self.main_scene.appendPlainText('Вы получили ' + str(t) + ' '
                                            + self.comment.make_agree_with_number(t).word + ' силы.')
        else:
            QMessageBox.about(self, 'Ошибка', 'Аптечки закончились')

    def stats(self):
        a = 'Сила: ' + str(self.sila) + '\n' + 'Уровень: ' + str(self.lvl) + '\n' + 'Кол-во аптечек: ' + str(
            self.heals) + '\n' + 'Кол-во наносимого урона: ' + 'случайное число из ' + str(self.levels[self.lvl][1])

        QMessageBox.about(self, 'Статистика', a)

    def next_lvl(self):
        QMessageBox.about(self, 'Силы до следующего уровня',
                          'Силы до следующего уровня: ' +
                          str(self.levels[self.lvl][0] - self.sila))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
