#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-11-12
#rclamb27@csu.fullerton.edu
"""takes it and puts it into an sql3"""
import sys
import csv
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from CovidCase import*
#all the imports give pylint an error
def main():
    """Main Function"""
    if len(sys.argv) < 3:
        print('Not Enough Arguments')
        sys.exit()
    engine = create_engine('sqlite:///' + sys.argv[2])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    this_session = Session()
    filename = sys.argv[1]
    with open(filename, 'r') as fh:
        reader = csv.reader(fh)
        for i in reader:
            year, month, day = map(int, i[2].split('-'))
            _c_ = CovidCase(i[0], i[1], date(year, month, day), int(i[3]),
                int(i[4]), int(i[5]))
            #print(_c_)
            this_session.add(_c_)
    this_session.commit()
    this_session.close()

if __name__ == '__main__':
    main()
