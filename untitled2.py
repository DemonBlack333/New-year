# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oJDDlPRu9RyuoAWgvvm_CitvafX3B-BD
"""

class Human:
  
  def __init__ (self, name, surname, age, city):
    self._name = name
    self._surname = surname
    self._age = age
    self._city = city
def info(self):
  print("Name:", self._name, "\nLast name:", self._surname, "\nAge:", self._age, "\nCity:", self._city)

class Santa(Human):

  def __init__(self, name, surname, age, city, Location, Gift):
  
    self._Location = Location
    self._Gift = Gift
    Human.__init__(self, age, city, name, surname)

  def info(self):
    print("Name:",self._name, "\nLast name:", self._surname)
    print("Class:", self._Location,"\nScores:", self._Gift)

