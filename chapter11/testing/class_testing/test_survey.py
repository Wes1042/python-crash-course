import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self): # << method from unittest (you pre set it)
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English' , 'Spanish', 'JavaScript']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    """
    Pseudo code:
    Store a index variable from out setup array and use it to test
    make sure our index is in the responses array
    """

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
    """
    Pseudo code:
    create a for loop that stored every preset variable from the setup function
    store every variable in the instance that was created
    check to see if every index of our variable is in reponses.
    """

unittest.main()
