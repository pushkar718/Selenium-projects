import random

def generator():
    first_name_options=['Test','Name','Qa','Dummy','Lorem','Ipsum','Lead','John','Robert','Michael','William','David','Richard','Charles','Joseph','Linda','Barbara','Elizabeth','Jennifer','Maria','Susan','Thompson','White','Lopez','Lee','Gonzalez','Harris','Clark','Lewis','Robinson','Sanchez','Wright','King','Scott','Green','Baker']
    last_name_options=['Test','Name','Qa','Dummy','Lead','Lorem','Ipsum','Linda','Barbara','Elizabeth','Jennifer','Maria','Susan','Garcia','Rodriguez','Wilson','Martinez','Anderson','Taylor','Thomas','Hernandez','Moore','Martin','Jackson','Thompson','White','Lopez','Lee','Gonzalez','Harris','Clark','Lewis','Robinson','Walker','Perez']
    final_name=random.choice(first_name_options)+' '+random.choice(last_name_options)
    return final_name