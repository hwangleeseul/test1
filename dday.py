import calendar
import datetime
import pickle
today = datetime.today()

#d1 = date(2019, 12, 10)
#d2 = date(2020, 5, 20)
#delta = d1 - d2
#print(delta.days)
#def dateList(base_date)
#    yy = int(base_date[:4])
#    mm = int(base_date[4:6])
#    dd = int(base_date[6:8])
    
#def working_days(start_dt,end_dt):
#    num_days = (end_dt - start_dt).days + 1

#from_date = int(input("기간입력: "))
#to_date = int(input("기간입력: "))

#holi_day = int(input("휴일입력: "))
class calculator_day:
    def __init__(self,start_dt,end_dt):
        self.start_dt = start_dt
        self.end_dt = end_dt
    def dday(self):
        num_days = (self.end_dt - self.start_dt).days + 1
        num_weeks = (num_days) // 7
        a = 0

        self.start_dt=input('기간입력: ')
        self.end_dt=input('기간입력: ')

        if self.end_dt.strftime('%a') == 'Sat':
            if self.end_dt.strftime('%a') != 'Sun':
                a = 1

        if self.end_dt.strftime('%a') =='Sun':
            if self.end_dt.strftime('%a') != 'Sat':
                a = 1

        if self.end_dt.strftime('%a') =='Sun':
            if self.end_dt.strftime('%a') not in ('Mon','Sun'):
                a = 2
        
        if self.end_dt.weekday() not in (0,6):
            if (self.end_dt.weekday()-self.end_dt.weekday()) >= 2:
                a = 2

        result = num_days - (num_weeks*2) - a 

        return result
myDay = calculator_day()
print(myDay.dday())
    #self.end_dt = datetime.date(2019,12,10)
    #self.end_dt = datetime.date(2020,5,20)

    #print(dday(self.end_dt,self.end_dt))

def dday(start_dt,end_dt):
        num_days = (end_dt - start_dt).days + 1
        num_weeks = (num_days) // 7
        a = 0

        if end_dt.strftime('%a') == 'Sat':
            if end_dt.strftime('%a') != 'Sun':
                a = 1

        if end_dt.strftime('%a') =='Sun':
            if end_dt.strftime('%a') != 'Sat':
                a = 1

        if end_dt.strftime('%a') =='Sun':
            if end_dt.strftime('%a') not in ('Mon','Sun'):
                a = 2
        
        if end_dt.weekday() not in (0,6):
            if (end_dt.weekday()-end_dt.weekday()) >= 2:
                a = 2

        dday = num_days - (num_weeks*2) - a 

        return dday


