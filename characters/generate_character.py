#!/usr/bin/python

import random
import uuid

# Lists for character generation:
from calculate_age import calculate_age
from female_first_names import female_first_names
from genders import genders
from male_first_names import male_first_names
from relationships import relationships
from surnames import surnames

class Character:
  def __init__(self):
    self.character_id = uuid.uuid4().hex
    self.gender = random.choice(genders)
    if 'Male' in self.gender:
      self.first_name = random.choice(male_first_names)
    else:
      self.first_name = random.choice(female_first_names)
    self.age, self.age_category = calculate_age(force_adult=True)
    self.male_parent = None
    self.female_parent = None
    self.surname = random.choice(surnames)

  def print_information(self):
    print("Character ID: {}".format(self.character_id))
    print("Gender:       {}".format(self.gender))
    print("First Name:   {}".format(self.first_name))
    print("Last Name:    {}".format(self.surname))
    print("Age:          {}".format(self.age))
    print("Age Category: {}".format(self.age_category))


def main():
  character = Character()
  character.print_information()
  print('\n')


if __name__ == '__main__':
  main()
