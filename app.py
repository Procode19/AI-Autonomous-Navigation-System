import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

from src.simulation import Simulation
from src.path_planning import a_star
from src.navigation import get_next_move

st.set_page_config(layout="wide")
st.title("🚗 AI Autonomous Navigation (Visual Simulator)")

# ---------------- STATE ----------------
if "sim" not in st.session_state:
    st.session_state.sim = Simulation()
    st.session_state.running = False
    st.session_state.path = []

sim = st.session_state.sim

# ---------------- CONTROLS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶ Start"):
        st.session_state.running = True

with col2:
    if st.button("⏸ Stop"):
        st.session_state.running = False

with col3:
    if st.button("🔄 Reset"):
        st.session_state.sim = Simulation()
        st.session_state.running = False
        st.session_state.path = []

# ---------------- GRID CLICK INPUT ----------------
st.subheader("🖱 Click to Add Obstacle")
click_x = st.number_input("X", 0, sim.grid_size - 1, 0)
click_y = st.number_input("Y", 0, sim.grid_size - 1, 0)

if st.button("Add Obstacle"):
    if (click_x, click_y) != sim.robot_pos and (click_x, click_y) != sim.goal:
        sim.grid[click_y][click_x] = 1

# ---------------- DRAW FUNCTION ----------------
def draw_grid(sim, path):
    grid = np.array(sim.grid)

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap="gray_r")

    # Draw path
    if path:
        px = [p[0] for p in path]
        py = [p[1] for p in path]
        ax.plot(px, py)

    # Draw robot (red)
    ax.scatter(sim.robot_pos[0], sim.robot_pos[1])

    # Draw goal (green)
    ax.scatter(sim.goal[0], sim.goal[1])

    ax.set_xticks(range(sim.grid_size))
    ax.set_yticks(range(sim.grid_size))
    ax.grid(True)

    return fig

# ---------------- SIMULATION LOOP ----------------
frame = st.empty()

if st.session_state.running:

    while not sim.is_goal_reached() and st.session_state.running:

        # Replan path
        path = a_star(sim.grid, sim.robot_pos, sim.goal)
        st.session_state.path = path

        if not path:
            st.error("No path found!")
            break

        # Move robot
        next_pos = get_next_move(path)
        if next_pos:
            sim.update_robot(next_pos)

        # Draw updated frame
        fig = draw_grid(sim, path)
        frame.pyplot(fig)

        time.sleep(0.3)

    if sim.is_goal_reached():
        st.success("✅ Goal Reached!")