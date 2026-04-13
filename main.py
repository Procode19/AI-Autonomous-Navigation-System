from src.simulation import Simulation
from src.path_planning import a_star
from src.perception import get_obstacles
from src.navigation import get_next_move
import time

def main():
    # Initialize simulation
    sim = Simulation()

    print("Starting Autonomous Navigation...")

    # Main loop (Sense → Plan → Act)
    while not sim.is_goal_reached():

        # 🔹 Step 1: Perception (detect obstacles dynamically)
        obstacles = get_obstacles(sim.grid)
        print("Detected obstacles:", obstacles)

        # 🔹 Step 2: Path Planning (recalculate path every step)
        path = a_star(sim.grid, sim.robot_pos, sim.goal)
        print("Replanned path:", path)

        if not path:
            print("No path found to the goal!")
            break

        # 🔹 Step 3: Navigation (move one step)
        next_pos = get_next_move(path)

        if next_pos:
            sim.update_robot(next_pos)
            sim.draw()
            time.sleep(0.3)  # smoother + faster

    # Final result
    if sim.is_goal_reached():
        print("✅ Goal reached successfully!")
    else:
        print("❌ Failed to reach goal.")

    # Keep window open
    time.sleep(2)
    sim.close()

if __name__ == "__main__":
    main()