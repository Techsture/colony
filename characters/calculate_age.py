import random
from numpy.random import choice

def calculate_age(force_adult):
  age_categories = [
      { 'category_name': 'Child', 'age_lower_bound': 0, 'age_upper_bound': 18 },
      { 'category_name': 'Young Adult', 'age_lower_bound': 19, 'age_upper_bound': 29 },
      { 'category_name': 'Adult', 'age_lower_bound': 30, 'age_upper_bound': 45 },
      { 'category_name': 'Middle Aged', 'age_lower_bound': 46, 'age_upper_bound': 64 },
      { 'category_name': 'Senior', 'age_lower_bound': 65, 'age_upper_bound': 79 },
      { 'category_name': 'Elderly', 'age_lower_bound': 80, 'age_upper_bound': 120 }
  ]
  age_category_weights = [
    0.05, # Child
    0.2,  # Young Adult
    0.5,  # Adult
    0.1,  # Middle Aged
    0.1,  # Senior
    0.05  # Elderly
  ]
  age_category_weights_forced_adult = [
    0.0,  # Child
    0.25, # Young Adult
    0.5,  # Adult
    0.1,  # Middle Aged
    0.1,  # Senior
    0.05  # Elderly
  ]
  if force_adult is True:
    age_category = choice(age_categories, p=age_category_weights_forced_adult)
  else:
    age_category = choice(age_categories, p=age_category_weights)
  age = random.randrange(age_category['age_lower_bound'], age_category['age_upper_bound'])
  return age, age_category['category_name']
