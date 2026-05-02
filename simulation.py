import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 基本設定
# ----------------------------
NUM_PEOPLE = 100
INITIAL_INFECTED = 5
SPACE_SIZE = 100
STEP_SIZE = 2

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

# 描画準備
plt.figure(figsize=(8, 8))

for step in range(50):
    # ----------------------------
    # 人をランダムに動かす
    # ----------------------------
    x += np.random.uniform(-STEP_SIZE, STEP_SIZE, NUM_PEOPLE)
    y += np.random.uniform(-STEP_SIZE, STEP_SIZE, NUM_PEOPLE)

    x = np.clip(x, 0, SPACE_SIZE)
    y = np.clip(y, 0, SPACE_SIZE)

    # ----------------------------
    # 色を決める
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
    plt.clf()
    plt.scatter(x, y, c=colors)
    plt.xlim(0, SPACE_SIZE)
    plt.ylim(0, SPACE_SIZE)
    plt.title(f"Step: {step}")
    plt.pause(0.1)