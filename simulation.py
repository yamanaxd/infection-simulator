import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 基本設定
# ----------------------------
NUM_PEOPLE = 100
INITIAL_INFECTED = 5
SPACE_SIZE = 100

# ----------------------------
# 人の位置をランダムに作る
# ----------------------------
x = np.random.uniform(0, SPACE_SIZE, NUM_PEOPLE)
y = np.random.uniform(0, SPACE_SIZE, NUM_PEOPLE)

# ----------------------------
# 状態を作る
# 0 = healthy
# 1 = infected
# 2 = recovered
# ----------------------------
state = np.zeros(NUM_PEOPLE, dtype=int)

# 最初の5人を感染者にする
infected_indices = np.random.choice(NUM_PEOPLE, INITIAL_INFECTED, replace=False)
state[infected_indices] = 1

# ----------------------------
# 色を決める
# healthy -> blue
# infected -> red
# recovered -> green
# ----------------------------
colors = []
for s in state:
    if s == 0:
        colors.append("blue")
    elif s == 1:
        colors.append("red")
    else:
        colors.append("green")

# ----------------------------
# 描画
# ----------------------------
plt.figure(figsize=(8, 8))
plt.scatter(x, y, c=colors)
plt.xlim(0, SPACE_SIZE)
plt.ylim(0, SPACE_SIZE)
plt.title("Day 1: Initial State of Infection Simulation")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()