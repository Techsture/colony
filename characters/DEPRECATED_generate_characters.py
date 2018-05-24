#!/usr/bin/python

import random

# Lists for character generation:
from calculate_age import calculate_age
from female_first_names import female_first_names
from genders import genders
from male_first_names import male_first_names
from relationships import relationships
from surnames import surnames

CHARACTER_LIST = []

class Character:
  def __init__(self, character_id, number_of_adult_males, number_of_childbearing_adult_females):
    self.character_id = character_id
    self.gender = random.choice(genders)
    if 'Male' in self.gender:
      self.first_name = random.choice(male_first_names)
    else:
      self.first_name = random.choice(female_first_names)
    if number_of_adult_males < 1 or number_of_childbearing_adult_females < 1:
      self.age, self.age_category = calculate_age(force_adult=True) 
    else:
      self.age, self.age_category = calculate_age(force_adult=False)
    self.male_parent = None
    self.female_parent = None
    if 'Child' in self.age_category:
      while self.male_parent is None \
      or self.male_parent.age_category is 'Child' \
      or self.male_parent.age_category is 'Senior' \
      or self.male_parent.age_category is 'Elderly' \
      or self.male_parent.age - self.age < 15 \
      or self.male_parent.gender is 'Female':
        self.male_parent = random.choice(CHARACTER_LIST)
        self.surname = self.male_parent.surname
      while self.female_parent is None \
      or self.female_parent.age_category is 'Child' \
      or self.female_parent.age_category is 'Senior' \
      or self.female_parent.age_category is 'Elderly' \
      or self.female_parent.age - self.age < 15 \
      or self.female_parent.gender is 'Male':
        self.female_parent = random.choice(CHARACTER_LIST)
    else:
      self.surname = random.choice(surnames)

  def print_information(self):
    print("Character ID: {}".format(self.character_id))
    print("Gender:       {}".format(self.gender))
    print("First Name:   {}".format(self.first_name))
    print("Last Name:    {}".format(self.surname))
    print("Age:          {}".format(self.age))
    print("Age Category: {}".format(self.age_category))
    if self.male_parent is not None:
      print("Parents:      {} {} & {} {}".format( 
        self.male_parent.first_name, 
        self.male_parent.surname,
        self.female_parent.first_name, 
        self.female_parent.surname
        ))
    else:
      print("Parents:      None")


def main():
  number_of_characters = 3
  id_iterator = 0
  number_of_adult_males = 0
  number_of_childbearing_adult_females = 0
  for character in range(number_of_characters):
    id_iterator += 1
    for generated_character in CHARACTER_LIST:
      if generated_character.gender is 'Male' and generated_character.age >= 19 and generated_character.age <= 64:
        number_of_adult_males += 1
      if generated_character.gender is 'Female' and generated_character.age >= 19 and generated_character.age <= 64:
        number_of_childbearing_adult_females += 1
    character = Character(id_iterator, number_of_adult_males, number_of_childbearing_adult_females)
    CHARACTER_LIST.append(character)
  for character in CHARACTER_LIST:
    character.print_information()
    print('\n')


if __name__ == '__main__':
  main()
