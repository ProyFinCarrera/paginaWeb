#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File test_firebase.py:
#           1. Class for upload and download of data in the firebase account.
# -*- coding: utf-8 -*-
import myfirebase
import json
from datetime import datetime
import time
import random
import calendar
from uuid import getnode as get_mac
# Year, month, dat
# inicio = datetime(2019, 6, 1)
user = {
    1: "user1",
    2: "user2",
    3: "user3",
    4: "user4",
    5: "user5",
    6: "user6",
    7: "user7",
    8: "user8",
    9: "user9",
    10: "user10",
}
email = {
    1: "user1@gmail.com",
    2: "user2@gmail.com",
    3: "user3@gmail.com",
    4: "user4@gmail.com",
    5: "user5@gmail.com",
    6: "user6@gmail.com",
    7: "user7@gmail.com",
    8: "user8@gmail.com",
    9: "user9@gmail.com",
    10: "user10@gmail.com",
}

n_mac = {
    1: "60E3270178FB",
    2: "70E3450178FB",
    3: "80E3350178FB",
}
lastName = {
    1: "Pérez",
    2: "González",
    3: "Dorta",
    4: "Lemus",
}

work = {
    1: "Gerencia",
    2: "Administración",
    3: "Cocina",
    4: "Auxiliar Gerencia",
}

info = {
    1: "Eficiente",
    2: "Sale temprano los viernes",
    3: "Trabaja de noche",
    4: "Esta de Vacaciones",
}

r_mac = {
    1:{u"name": u"Device 1",u"mac": u"60E3270178FB"},
    2:{u"name": u"Puerta 2",u"mac": u"70E3450178FB"},
    3:{u"name": u"Puerta 5", u"mac": u"80E3350178FB"}
}


def my_mac():
    mac = get_mac()
    mac_aux = ''.join(('%012X' % mac)[i:i + 2]for i in range(0, 12, 2))
    return mac_aux


class TestFirebase:
    def __init__(self, register_this_moth,
                 register_this_week,
                 register_this_day,
                 today=datetime.now()):
        self.__db = myfirebase.MyFirebase()
        self.__today = today
        self.__register_this_moth = register_this_moth
        self.__register_this_week = register_this_week
        self.__register_this_day = register_this_day
        self.__cont_up = 0
        self.__amount_day = 10

    def getCont(self):
        return self.__cont_up

    def register_divice(self):
        for i in r_mac:
            self.__db.upload_testMac(r_mac.get(i))

    def register_new_user(self, c_user):
        for x in range(c_user):
            op_user = random.randint(1, 10)
            em = email.get(op_user)
            fn = user.get(op_user)
            ln = lastName.get(random.randint(1, 4))
            wp = work.get(random.randint(1, 4))
            otI = info.get(random.randint(1, 4))

            up_data = {
                u'emailId': em,
                u'firstName': fn,
                u'lastName': ln,
                u'workPosition': wp,
                u'otherInfo': otI
            }
            self.__db.upload_testUser(up_data)

    def run(self):
        self.register_this_date(self.__register_this_day, self.__today)
        amount_week = self.__register_this_week - self.__register_this_day
        self.register_week_without_this_date(amount_week, self.__today)
        amount_moth = self.__register_this_moth - self.__register_this_week
        self.register_this_month__without_this_week(
            amount_moth, self.__today)

    def register_this_month__without_this_week(self, amount, this_week):
        n_amount = amount
        start_moth = this_week.replace(day=1)
        after_moth = start_moth
        num_week = this_week.isocalendar()[1]
        while n_amount > 0:
            if start_moth != -1:
                if num_week != start_moth.isocalendar()[1]:
                    r = random.randint(0, n_amount)
                    n_amount = n_amount - r
                    after_moth = start_moth
                    self.register_this_week(r, start_moth)
                start_moth = self.next_week_of_mouth(start_moth)
            else:
                self.register_this_week(n_amount, after_moth)
                n_amount = 0
                # print(start_moth)

    def register_week_without_this_date(self, amount, this_date):
        n_amount = amount
        date_monday = self.start_of_this_week(this_date)
        next_day = date_monday.day
        next_date = date_monday.replace(day=next_day)
        last_day = self.last_day_mouth(date_monday)
        end_day = self.end_of_this_week(this_date).day
        while n_amount > 0:
            if this_date.day != next_date.day:
                r = random.randint(0, n_amount)
                self.register_this_date(r, next_date)
                n_amount = n_amount - r
            next_day += 1
            if((next_day <= last_day) & (next_day <= end_day)):
                date_monday = next_date
                next_date = next_date.replace(day=next_day)
            else:
                self.register_this_date(n_amount, next_date)
                n_amount = 0

    def last_day_mouth(self, date):
        return calendar.monthrange(date.year, date.month)[1]

    def _json_registre(self, date):
        # n_m = my_mac()
        n_m = n_mac.get(random.randint(1, 3))
        h = random.randint(0, 23)
        m = random.randint(0, 59)
        date = date.replace(hour=h, minute=m)
        up_data = {
            u'timeStamps': time.mktime(date.timetuple()),
            u'day': int(date.strftime('%d')),
            u'month': int(date.strftime('%m')),
            u'nameMonth': date.strftime('%B'),
            u'nameDay': date.strftime('%A'),
            u'year': int(date.strftime('%Y')),
            u'hour': int(date.strftime('%H')),
            u'minute': int(date.strftime('%M')),
            u'mac': n_m
        }
        op = random.randint(1, 10)
        up_data[u'emailId'] = email.get(op)
        up_data[u'firstName'] = user.get(op)
        # send data
        self.__cont_up += 1
        self.__db.upload_date_test(up_data)
        # print(up_data)
        return up_data

    def register_this_date(self, amount, this_date):
        for i in range(amount):
            self._json_registre(this_date)
        # print(self._json_registre(date))

    def end_of_this_week(self, this_date):
        date = this_date
        next_month = date.month
        next_day = date.day + 1
        last_day = self.last_day_mouth(this_date)
        while((next_day < last_day) &
              (6 != date.weekday()) &
              (date.month == next_month)):
            date = date.replace(day=next_day)
            next_month = date.month
            next_day += 1
        return date

    def start_of_this_week(self, this_date):
        date = this_date
        next_month = date.month
        next_day = date.day - 1
        while((next_day > 1) &
                (0 != date.weekday()) &
                (date.month == next_month)):
            date = date.replace(day=next_day)
            next_month = date.month
            next_day -= 1
        return date

    def register_this_week(self, amount, this_week):
        n_amount = amount
        date_monday = self.start_of_this_week(this_week)
        next_day = date_monday.day
        next_date = date_monday.replace(day=next_day)
        last_day = self.last_day_mouth(date_monday)
        end_day = self.end_of_this_week(this_week).day
        while n_amount > 0:
            r = random.randint(0, n_amount)
            self.register_this_date(r, next_date)
            n_amount = n_amount - r
            next_day += 1
            if((next_day <= last_day) & (next_day <= end_day)):
                date_monday = next_date
                next_date = next_date.replace(day=next_day)
            else:
                self.register_this_date(n_amount, next_date)
                n_amount = 0

    def next_week_of_mouth(self, date):
        end = self.end_of_this_week(date)
        n_day = end.day + 1
        last_day = self.last_day_mouth(date)
        if last_day >= n_day:
            next_week = end.replace(day=n_day)
            return next_week
        else:
            return -1

    def register_this_month(self, amount, this_week):
        n_amount = amount
        start_moth = this_week.replace(day=1)
        after_moth = start_moth
        # num_week = self.__today.isocalendar()[1]
        while n_amount > 0:

            if start_moth != -1:
                r = random.randint(0, n_amount)
                n_amount = n_amount - r
                after_moth = start_moth
                self.register_this_week(r, start_moth)
                start_moth = self.next_week_of_mouth(start_moth)
            else:
                self.register_this_week(n_amount, after_moth)
                n_amount = 0
                # print(start_moth)


if __name__ == '__main__':
    aux = TestFirebase(100, 30, 10)
    date = datetime(2019, 6, 27)
    #aux.register_this_date(5,date)
    # print(aux.next_week_of_mouth(date))
    aux.register_new_user(20)
    aux.register_divice()
    aux.run()

    # print(aux.getCont())
    # print(aux._start_of_this_week())
