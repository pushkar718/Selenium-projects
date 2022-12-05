import random

def generator():
    first_name_options=['Test','Name','Qa','Dummy']
    last_name_options=['Test','Name','Qa','Dummy','Lead']
    final_name=random.choice(first_name_options)+' '+random.choice(last_name_options)
    print(final_name)