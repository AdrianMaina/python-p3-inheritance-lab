#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        # Initialize base User with first and last name
        super().__init__(first_name, last_name)
        # Each student starts with an empty knowledge list
        self.knowledge = []

    def learn(self, fact):
        """
        Add a new fact (string) to the student's knowledge list.
        """
        self.knowledge.append(fact)
