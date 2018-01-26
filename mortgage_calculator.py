# Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

import matplotlib.pyplot as plt; plt.rcdefaults()
from collections import OrderedDict
import numpy as np

class Mortgage:
    '''
    def __init__(self):
        self.f_cost = 0 #flat_cost
        self.own_c_p = 0 #own contribution in %
        self.b_comm = 0 #bank_commision
        self.c_spread = 0 #credit_spread in %
        self.ref_rate = 0 #reference_rate in %
        self.years = 0 #number of years
        self.p_p_y = 12 #usually 12 payments per year
    '''
    def __init__(self):
        self.f_cost = 340000 #flat_cost
        self.own_c_p = 20 #own contribution in %
        self.b_comm = 2.5 #bank_commision
        self.c_spread = 2 #credit_spread in %
        self.ref_rate = 1.67 #reference_rate in %
        self.years = 35 #number of years
        self.p_p_y = 12 #usually 12 payments per year
    
    def credit_parameters(self):
        self.f_cost = float(raw_input('Set cost of the flat: '))
        self.own_c_p = float(raw_input('Set amount of your own contribution, in %: '))
        self.b_comm = float(raw_input('Set amount of bank commision, in %: '))
        self.years = int(raw_input('Set number of years: '))
        self.c_spread = float(raw_input('Set credit spread of your bank, in %: '))
        self.ref_rate = float(raw_input('Set reference rate in you country, in %: '))
        self.p_p_y = int(raw_input('Set number of instalments per year (usually is 12): '))
        
    def mortgage_calc(self):
        own_c = self.f_cost * self.own_c_p / 100
        self.credit_amount_nc = self.f_cost - own_c
        self.real_commision = self.credit_amount_nc * self.b_comm / 100 
        self.credit_cost = self.credit_amount_nc + self.real_commision
        self.payments_num = self.years * self.p_p_y # Number of payments
        self.i_p_y = self.c_spread + self.ref_rate #Interest per Year

    def mortgage_parameters(self):
        print ('BASIC DATA ABOUT MORTGAGE'.center(45 + 10, '-'))
        basic_data = OrderedDict([
                                ('Credit without bank commission', str(self.credit_amount_nc)),
                                ('Bank commision', str(self.real_commision)),
                                ('Credit cost with bank commission', str(self.credit_cost)),
                                ('Total number of payments', str(self.payments_num)),
                                ('Number of years', str(self.years)),
                                ('Total interest', str(self.i_p_y)+'%')
                                ])
        for k, v in basic_data.items():
            print (k.ljust(45, '.') + v.rjust(10))
        
    def loan_installment(self):
        self.q = 1 + (self.i_p_y/100 / self.p_p_y)
        self.loan_inst = (self.credit_cost*(self.q**self.payments_num)*(self.q-1))/((self.q**self.payments_num)-1)
        self.amount_to_pay = self.loan_inst * self.payments_num
        print ('FIXED INSTALLMENT CREDIT'.center(45 + 10, '-'))
        print ('Monthly loan installment: '.ljust(45, '-') + str(round(self.loan_inst,2)).rjust(10))
            
    def fixed_installment(self):
        self.capital=[]
        self.interest2 =[]
        capital_sum = 0
        self.interest_sum = 0
        self.interest = self.i_p_y/100/self.p_p_y
        for x in range(1,self.payments_num+1):
            self.capital_installment = (self.credit_cost*self.interest*(1+self.interest)**(x-1))/((1+self.interest)**self.payments_num-1)
            self.interest_installment = self.loan_inst - self.capital_installment
            self.capital.append(round(self.capital_installment,2))
            self.interest2.append(round(self.interest_installment,2))
            capital_sum += self.capital_installment
            self.interest_sum += self.interest_installment        
            
    def f_parameters(self):
        basic_data = OrderedDict([
                                ('First capital installment', str(round(self.capital[0],2))),
                                ('Fist interest installment', str(round(self.interest2[0],2))),
                                ('Total interest installment', str(round(self.interest_sum,2))),
                                ('Total amount to pay', str(round(self.amount_to_pay,2)))
                                ])
        for k, v in basic_data.items():
            print (k.ljust(45, '.') + v.rjust(10))

    def bar_chart_size(self):
        self.fig_size = plt.rcParams["figure.figsize"]
        self.fig_size[0] = 10
        self.fig_size[1] = 3
        plt.rcParams["figure.figsize"] = self.fig_size
        
    def bar_chart(self):
        cap = self.capital
        inter = self.interest2
        N = len(cap)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.6       # the width of the bars: can also be len(x) sequence
        p1 = plt.bar(ind, cap, width)
        p2 = plt.bar(ind, inter, width, bottom=cap)
        plt.show()

    def loan_d_installment(self):
        self.capital_d_inst = self.credit_cost / self.payments_num
        self.interest_d_inst = ((self.credit_cost-(1-1)*self.capital_d_inst)*self.i_p_y/100)/self.p_p_y
        self.amount_to_pay_d = self.capital_d_inst + self.interest_d_inst       
            
    def decreasing_installment(self):
        self.d_capital=[]
        self.d_interest2 =[]
        self.d_total = []
        d_capital_sum = 0
        d_interest_sum = 0
        d_total_sum = 0
        self.interest = self.i_p_y/100/self.p_p_y
        for x in range(1,self.payments_num+1):
            self.interest_d_installment = ((self.credit_cost-(x-1)*self.capital_d_inst)*self.i_p_y/100)/self.p_p_y
            self.capital_d_installment = self.capital_d_inst
            self.total_d_installment = self.interest_d_installment + self.capital_d_installment
            self.d_capital.append(round(self.capital_d_installment,2))
            self.d_interest2.append(round(self.interest_d_installment,2))
            self.d_total.append(round(self.total_d_installment,2))
            d_capital_sum += self.capital_d_installment
            d_interest_sum += self.interest_d_installment
            d_total_sum += self.total_d_installment
        print ('Total interest installments'.ljust(45, '-') + str(round(d_interest_sum,2)).rjust(10))
        print ('Total amount to pay'.ljust(45, '-') + str(round(d_total_sum,2)).rjust(10))

    def d_parameters(self):
        print ('DESCENDING INSTALLMENT CREDIT'.center(45 + 10, '-'))
        basic_data = OrderedDict([
                                ('Fist loan installment', str(round(self.amount_to_pay_d,2))),
                                ('Constant capital installment is', str(round(self.capital_d_inst,2))),
                                ('First decreassing interest installment is', str(round(self.interest_d_inst,2)))
                                 ])
        for k, v in basic_data.items():
            print (k.ljust(45, '.') + v.rjust(10))
        
    def bar_chart_d(self):
        cap = self.d_capital
        inter = self.d_interest2
        N = len(cap)
        ind = np.arange(N)# the x locations for the groups
        width = 0.6       # the width of the bars: can also be len(x) sequence
        p1 = plt.bar(ind, cap, width)
        p2 = plt.bar(ind, inter, width, bottom=cap)
        plt.show()

kredyt = Mortgage()
#kredyt.credit_parameters()
kredyt.mortgage_calc()
kredyt.mortgage_parameters()
kredyt.loan_installment()
kredyt.fixed_installment()
kredyt.f_parameters()
kredyt.bar_chart_size()
kredyt.bar_chart()
#kredyt.print_f_results()

kredyt.loan_d_installment()
kredyt.d_parameters()
kredyt.decreasing_installment()
kredyt.bar_chart_d()

import os
