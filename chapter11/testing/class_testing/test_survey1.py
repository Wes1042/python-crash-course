import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) # using 
        my_survey.store_response("English")

        self.assertIn('English', my_survey.responses)
    """
    Pseudo code:
    set a variable that can be used to send a question to the survey class
    create a instance of our question as my_survey 
    Store a varible to that instance
    Make sure the variable was successfully stored in the survey instance.
    """

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        question = "What language fi you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English' , 'Spanish', 'JavaScript']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)

    """
    Pseudo code:
    set a variable for question
    use that variable to create an isntace from our importet file
    store 3 seperate variables in an array
    create a for loop that stores every variable at a time 
    create a for loop that checks if the responses were stored
    correctly
    """

unittest.main()
