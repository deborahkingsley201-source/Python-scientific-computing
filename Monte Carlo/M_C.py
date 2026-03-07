import copy
import random

class Hat:
    """
    Manages a collection of items for random sampling.
    """
    def __init__(self, **balls):
        self.contents = []
        # Populate the hat based on color and count
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        """
        Removes and returns a random selection of balls.
        If num exceeds total, returns all balls.
        """
        num = min(num, len(self.contents))
        drawn = random.sample(self.contents, num)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Runs the Monte Carlo simulation to find the probability 
    of drawing a specific set of balls.
    """
    count_success = 0
    
    for _ in range(num_experiments):
        # Create a fresh copy of the hat for each trial
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        # Convert drawn list to a frequency dictionary
        drawn_dict = {}
        for ball in drawn:
            drawn_dict[ball] = drawn_dict.get(ball, 0) + 1
        
        # Check if the draw meets all 'expected' criteria
        success = True
        for color, count in expected_balls.items():
            if drawn_dict.get(color, 0) < count:
                success = False
                break
        
        if success:
            count_success += 1
        
    return count_success / num_experiments

# --- Example Professional Execution ---
# Scenario: 6 Black, 4 Red, 3 Green balls. 
# Probability of getting at least 2 Red and 1 Green in 5 draws.
test_hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=test_hat, 
    expected_balls={"red": 2, "green": 1}, 
    num_balls_drawn=5, 
    num_experiments=2000
)

print(f"Calculated Probability: {probability:.4f}")
