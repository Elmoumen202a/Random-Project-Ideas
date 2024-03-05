import unittest
from main import ProjectIdeasGenerator

class TestProjectIdeasGenerator(unittest.TestCase):
    def test_get_random_project_idea(self):
        # Create an instance of the ProjectIdeasGenerator class
        idea_generator = ProjectIdeasGenerator()
        
        # Get a random project idea
        idea = idea_generator.get_random_project_idea()
        
        # Check if the generated idea is in the list of project ideas
        self.assertTrue(idea in idea_generator.project_ideas)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
