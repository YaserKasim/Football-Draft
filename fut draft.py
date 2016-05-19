import time
import random

def pickFormation():
    formation = []
    random1 = random.randint(0,len(formation))
    formation.append([['gk'],['cb','cb','cb'],['lm','cm','cm','rm'],['cam'],['st','st']])
    formation.append([['gk'],['cb','cb','cb'],['lm','cm','cm','rm'],['lf','rf'],['st']])
    formation.append([['gk'],['cb','cb','cb'],['lm','cm','cm','rm'],['lf','st','rf']])
    formation.append([['gk'],['cb','cb','cb'],['lm','cdm','cdm','cam','rm'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm'],['lm','rm'],['cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm'],['lm','cm','cm','rm'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm','cdm'],['cam'],['cam','cam'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm','cdm',],['cam','cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm'],['lm','cm','cm','rm'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm'],['cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm'],['lf','rf'],['st']])

    numberOfFormations = 5
    listOfRandomItems = random.sample(formation,numberOfFormations)

    for formation in listOfRandomItems:
        strToPrint = []
        for row in formation [1:]:
             strToPrint.append(len(row))

        print(strToPrint)

    
        
    
pickFormation()  
