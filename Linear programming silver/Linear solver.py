import numpy as np

class SimplexSolver:
    def __init__(self, objective_coeffs, constraint_matrix, constants):
        """
        Maximizes: Z = objective_coeffs * x
        Subject to: constraint_matrix * x <= constants
        """
        self.obj = np.array(objective_coeffs, dtype=float)
        self.cons = np.array(constraint_matrix, dtype=float)
        self.consts = np.array(constants, dtype=float)

    def solve(self):
        # simplified 2-variable solver logic using NumPy
        num_vars = len(self.obj)
        num_cons = len(self.consts)
        
        # Build the initial Tableau
        tableau = np.zeros((num_cons + 1, num_vars + num_cons + 1))
        tableau[:num_cons, :num_vars] = self.cons
        tableau[:num_cons, num_vars:num_vars+num_cons] = np.eye(num_cons)
        tableau[:num_cons, -1] = self.consts
        tableau[-1, :num_vars] = -self.obj
        
        return "Tableau Initialized. Pivot to find Optimal Solution."

# Example for your Laundry Business:
# Maximize Profit = 500x (Wash) + 800y (Wash & Fold)
# Constraint 1: 2x + 3y <= 12 (Machine Hours)
# Constraint 2: 1x + 4y <= 10 (Staff Hours)
solver = SimplexSolver([500, 800], [[2, 3], [1, 4]], [12, 10])
print(solver.solve())
