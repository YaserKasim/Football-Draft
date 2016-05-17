import time
import random

def pickFormation():
    generateRandomFormations
    formation = []
    
    

    formation.append([['gk'],['cb','cb','cb',],['lw','cm','cm','rw',],['cam'],['st','st']])
    formation.append([['gk'],['cb','cb','cb'],['lw','cm','cm','rw'],['lw','rw'],['st']])
    formation.append([['gk'],['cb','cb','cb'],['lw','cm','cm','rw'],['lw','st','rw']])
    formation.append([['gk'],['cb','cb','cb'],['cdm','cm'],['lm','cam','rm'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm'],['lw','rw'],['cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm'],['lw','cm','cm','rw'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm'],['cam'],['cam','cam'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm',],['cam','cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm'],['lw','cm','cm','rw'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm'],['cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm',],['lw','rw'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm',],['lw','st','rw',]])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm',],['lw','cf','rw',],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['lw','cm','cm','rw',],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['lw','cm','rw',],['cam','cam'],['st']])
    formation.append([['gk'],['lb','cb','cb','cb','rb',],['cm','cm',],['cam',],['st','st',]])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm',],['lw','rw'],['st']])
    formation.append([['gk'],['lb','cb','cb','cb','rb'],['cm','cm',],['lw','st','rw',]])
    formation.append([['gk'],['lb','cb','cb','cb','rb'],['cm','cm','cm',],['st','st',]])

    strToPrint = []
    
    for row in formation[4][1:]:

        strToPrint.append(len(row))
    print(strToPrint)
    
                          
    
    
    
    
 
    
    
    
    
    
pickFormation()   
