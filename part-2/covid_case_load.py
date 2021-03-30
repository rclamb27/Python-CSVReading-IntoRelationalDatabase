#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-11-12
#rclamb27@csu.fullerton.edu
"""Takes Csv File and converts into  a relational database"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import asc
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from CovidCase import *

def main():
    """Takes death and cases per 10,000 and plots the two lines"""
    if len(sys.argv) < 3:
        print("Not enough arguments, Needs 3.")
        sys.exit()
    engine = create_engine('sqlite:///' + sys.argv[1])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    this_session = Session()
    population = [record.population for record in this_session.query
            (CovidCase.population).order_by(asc(CovidCase.date))]
    death = [record.deaths for record in this_session.query
            (CovidCase.deaths).order_by(asc(CovidCase.date))]
    cases = [record.covid_cases for record in this_session.query
            (CovidCase.covid_cases).order_by(asc(CovidCase.date))]
    dates = [record.date for record in this_session.query
            (CovidCase.date).order_by(asc(CovidCase.date))]
    this_session.commit()
    this_session.close()

    c_10k = []
    d_10k = []
    first = population[0]/10000
    for i in cases:
        c_10k.append(float(i/first))
    for i in death:
        d_10k.append(float(i/first))
    #print(c_10k)
    fig, ax = plt.subplots(figsize=(8, 8), constrained_layout=True)
    fig.suptitle('Cases and Deaths per 10,000', fontsize=25)
    ax.plot(dates, c_10k)
    line2 = ax.plot(dates, d_10k)
    plt.setp(line2, color='r')
    label_1 = mlines.Line2D([], [], color='blue', markersize=15,
              label='Covid Cases per 10,000')
    label_2 = mlines.Line2D([], [], color='red', markersize=15,
              label='Deaths per 10,000')
    ax.set(xlabel="Dates", ylabel="Amount per 10,000")
    ax.legend(title="Legend", handles=[label_1, label_2])
    fig.savefig(sys.argv[2])
    plt.close()

if __name__ == '__main__':
    """Calls main"""
    main()
