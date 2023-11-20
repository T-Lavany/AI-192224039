class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount
        self.visited_states = set()

    def solve(self):
        initial_state = (0, 0)
        if self._dfs(initial_state):
            print("Solution found:")
        else:
            print("No solution found.")

    def _dfs(self, current_state):
        if current_state[0] == self.target_amount or current_state[1] == self.target_amount:
            print(f"Reached target state: {current_state}")
            return True

        self.visited_states.add(current_state)

        # Fill jug 1
        next_state = (self.jug1_capacity, current_state[1])
        if next_state not in self.visited_states and self._dfs(next_state):
            print(f"Fill jug 1: {current_state} -> {next_state}")
            return True

        # Fill jug 2
        next_state = (current_state[0], self.jug2_capacity)
        if next_state not in self.visited_states and self._dfs(next_state):
            print(f"Fill jug 2: {current_state} -> {next_state}")
            return True

        # Pour water from jug 1 to jug 2
        pour_amount = min(current_state[0], self.jug2_capacity - current_state[1])
        next_state = (current_state[0] - pour_amount, current_state[1] + pour_amount)
        if next_state not in self.visited_states and self._dfs(next_state):
            print(f"Pour jug 1 to jug 2: {current_state} -> {next_state}")
            return True

        # Pour water from jug 2 to jug 1
        pour_amount = min(current_state[1], self.jug1_capacity - current_state[0])
        next_state = (current_state[0] + pour_amount, current_state[1] - pour_amount)
        if next_state not in self.visited_states and self._dfs(next_state):
            print(f"Pour jug 2 to jug 1: {current_state} -> {next_state}")
            return True

        # Empty jug 1
        next_state = (0, current_state[1])
        if next_state not in self.visited_states and self._dfs(next_state):
            print(f"Empty jug 1: {current_state} -> {next_state}")
            return True

        # Empty jug 2
        next_state = (current_state[0], 0)
        if next_state not in self.visited_states and self._dfs(next_state):
            print(f"Empty jug 2: {current_state} -> {next_state}")
            return True

        return False

# Example usage:
jug_problem = WaterJugProblem(jug1_capacity=4, jug2_capacity=3, target_amount=2)
jug_problem.solve()
