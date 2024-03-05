# import random

class ProjectIdeasGenerator:
    def __init__(self):
        # List of project ideas to be randomly selected
        self.project_ideas = [
            "Create a task management app",
            "Build a weather forecast application",
            "Develop a simple chatbot",
            "Design a personal finance tracker",
            "Implement a URL shortener",
            "Build a note-taking application",
            "Create a basic e-commerce website",
            "Develop a password manager",
            "Build a recipe sharing platform",
            "Implement a file encryption tool",
        ]

    def get_random_project_idea(self):
        # Select a random project idea from the list
        return random.choice(self.project_ideas)

if __name__ == "__main__":
    # Create an instance of the ProjectIdeasGenerator class
    idea_generator = ProjectIdeasGenerator()
    
    # Get a random project idea and print it
    random_idea = idea_generator.get_random_project_idea()
    print("Your Random Project Idea:")
    print(random_idea)
