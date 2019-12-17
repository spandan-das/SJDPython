# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:21:59 2019

@author: Spandan Das
"""

questionbank ={
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}
            
#print("Question1=",questionbank["quiz"]["sport"]["q1"]["question"])
#print("Question2=",questionbank["quiz"]["maths"]["q1"]["question"])
#print("Question3=",questionbank["quiz"]["maths"]["q2"]["question"])
for key,value in questionbank.items():
    for subkey,subvalue in value.items():
        for sskey,ssvalue in subvalue.items():
            print(ssvalue["question"])
