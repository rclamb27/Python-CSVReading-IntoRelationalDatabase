#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-11-12
#rclamb27@csu.fullerton.edu
"""CovidCase"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
#the imports is causing pylint to go crazy
Base = declarative_base()

class CovidCase(Base):
    """Class CovidCase"""
    __tablename__ = 'covid_cases'
    id = Column(Integer, primary_key=True)
    state = Column(String)
    date = Column(Date)
    covid_cases = Column(Integer)
    deaths = Column(Integer)
    population = Column(Integer)
    def __init__(self, county, state, date, covid_cases, deaths, population):
        """Initilization of Class"""
        self.county = county
        self.state = state
        self.date = date
        self.covid_cases = covid_cases
        self.deaths = deaths
        self.population = population
    
