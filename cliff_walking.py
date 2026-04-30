import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ==========================================
# 1. 定義環境 (Cliff Walking Environment)
# ==========================================
class CliffWalkingEnv:
    def __init__(self):
        self.rows = 4
        self.cols = 12
        self.start_state = (3, 0)
        self.goal_state = (3, 11)
        self.state = self.start_state
        
        # 動作定義: 0:上, 1:右, 2:下, 3:左
        self.actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action_idx):
        action = self.actions[action_idx]
        next_r = self.state[0] + action[0]
        next_c = self.state[1] + action[1]

        # 邊界處理
        next_r = max(0, min(self.rows - 1, next_r))
        next_c = max(0, min(self.cols - 1, next_c))
        next_state = (next_r, next_c)

        # 判斷是否掉入懸崖 (Cliff)
        if next_r == 3 and 1 <= next_c <= 10:
            reward = -100
            next_state = self.start_state
            done = False
        # 判斷是否抵達終點 (Goal)
        elif next_state == self.goal_state:
            reward = -1
            done = True
        # 正常移動
        else:
            reward = -1
            done = False

        self.state = next_state
        return next_state, reward, done

# ==========================================
# 2. 定義 Agent (Q-learning 與 SARSA)
# ==========================================
class RLAgent:
    def __init__(self, alpha=0.1, epsilon=0.1, gamma=0.9):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.q_table = np.zeros((4, 12, 4))
        
    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(4)
        else:
            r, c = state
            q_values = self.q_table[r, c, :]
            max_q = np.max(q_values)
            actions = np.where(q_values == max_q)[0]
            return np.random.choice(actions)

    def get_greedy_action(self, state):
        # 繪圖時取最佳動作 (不帶 epsilon 探索)
        r, c = state
        q_values = self.q_table[r, c, :]
        max_q = np.max(q_values)
        actions = np.where(q_values == max_q)[0]
        return np.random.choice(actions)

class QLearningAgent(RLAgent):
    def update(self, state, action, reward, next_state, next_action, done):
        r, c = state
        nr, nc = next_state
        target = reward if done else reward + self.gamma * np.max(self.q_table[nr, nc, :])
        self.q_table[r, c, action] += self.alpha * (target - self.q_table[r, c, action])

class SarsaAgent(RLAgent):
    def update(self, state, action, reward, next_state, next_action, done):
        r, c = state
        nr, nc = next_state
        target = reward if done else reward + self.gamma * self.q_table[nr, nc, next_action]
        self.q_table[r, c, action] += self.alpha * (target - self.q_table[r, c, action])

# ==========================================
# 3. 繪製策略圖 (Policy Visualization)
# ==========================================
def draw_policy(agent, title):
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    
    # 畫網格線
    ax.set_xticks(np.arange(13))
    ax.set_yticks(np.arange(5))
    ax.grid(color='black', linestyle='-', linewidth=1.5)
    
    # 翻轉 Y 軸，讓 (0,0) 在左上角，(3,0) 在左下角
    ax.invert_yaxis()
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_title(title, fontsize=16, pad=15)

    # 標示 Start, Goal 與 Cliff
    cliff_rect = patches.Rectangle((1, 3), 10, 1, facecolor='#a9d4ee', edgecolor='black')
    ax.add_patch(cliff_rect)
    ax.text(6, 3.5, 'Cliff', ha='center', va='center', fontsize=14, color='black')
    
    # Start & Goal (特別標註藍色向上箭頭與向下箭頭以符合範例)
    ax.text(0.6, 3.5, 'Start', ha='center', va='center', fontsize=12)
    ax.arrow(0.2, 3.8, 0, -0.4, head_width=0.15, head_length=0.15, fc='#0072b2', ec='#0072b2', width=0.03)
    ax.text(11.5, 3.5, 'Goal', ha='center', va='center', fontsize=12)

    # 動作繪圖參數
    # 0:上 (-y), 1:右 (+x), 2:下 (+y), 3:左 (-x)
    arrow_dx = [0, 0.4, 0, -0.4]
    arrow_dy = [-0.4, 0, 0.4, 0]

    # 畫出每個格子的最佳策略箭頭
    for r in range(4):
        for c in range(12):
            # 懸崖跟終點不畫箭頭
            if (r == 3 and 1 <= c <= 10) or (r == 3 and c == 11):
                continue
            
            best_action = agent.get_greedy_action((r, c))
            cx, cy = c + 0.5, r + 0.5
            
            # Start 格子的箭頭已經特製，跳過
            if r == 3 and c == 0:
                continue
                
            dx = arrow_dx[best_action]
            dy = arrow_dy[best_action]
            
            ax.arrow(cx - dx/2, cy - dy/2, dx, dy, head_width=0.12, head_length=0.15, fc='black', ec='black')

    # 尋找並畫出貪婪路徑 (藍色虛線)
    path_x = [0.5]
    path_y = [3.5]
    curr_state = (3, 0)
    
    steps = 0
    while curr_state != (3, 11) and steps < 50: # 防呆機制，避免無窮迴圈
        action = agent.get_greedy_action(curr_state)
        # 更新狀態
        if action == 0: curr_state = (max(0, curr_state[0]-1), curr_state[1])
        elif action == 1: curr_state = (curr_state[0], min(11, curr_state[1]+1))
        elif action == 2: curr_state = (min(3, curr_state[0]+1), curr_state[1])
        elif action == 3: curr_state = (curr_state[0], max(0, curr_state[1]-1))
        
        path_x.append(curr_state[1] + 0.5)
        path_y.append(curr_state[0] + 0.5)
        
        # 掉下懸崖中斷畫線
        if curr_state[0] == 3 and 1 <= curr_state[1] <= 10:
            break
        steps += 1

    ax.plot(path_x, path_y, color='#0072b2', linestyle='--', linewidth=3, zorder=1)

    plt.tight_layout()
    plt.show()

# ==========================================
# 4. 訓練與比較主程式
# ==========================================
def train(agent_class, episodes=500, runs=50):
    all_rewards = np.zeros(episodes)
    best_agent = None
    
    for run in range(runs):
        env = CliffWalkingEnv()
        agent = agent_class()
        run_rewards = []
        
        for ep in range(episodes):
            state = env.reset()
            action = agent.choose_action(state)
            ep_reward = 0
            done = False
            
            while not done:
                next_state, reward, done = env.step(action)
                next_action = agent.choose_action(next_state)
                
                agent.update(state, action, reward, next_state, next_action, done)
                
                state = next_state
                action = next_action
                ep_reward += reward
                
            run_rewards.append(ep_reward)
        all_rewards += np.array(run_rewards)
        
        # 保留最後一次 run 的 agent 用來畫策略圖
        if run == runs - 1:
            best_agent = agent
            
    return all_rewards / runs, best_agent

if __name__ == "__main__":
    print("Training Q-Learning...")
    q_rewards, trained_q_agent = train(QLearningAgent)
    
    print("Training SARSA...")
    sarsa_rewards, trained_sarsa_agent = train(SarsaAgent)

    # 1. 繪製報酬曲線 (Curve)
    plt.figure(figsize=(10, 6))
    plt.plot(sarsa_rewards, label='Sarsa', color='#17becf')
    plt.plot(q_rewards, label='Q-learning', color='#d62728')
    plt.xlabel('Episodes')
    plt.ylabel('Reward Sum for Episode')
    plt.title('Sarsa Vs. Q-Learning Cliff Walking\nEpsilon=0.1, Alpha=0.1\n(averaged over 50 runs)')
    plt.legend()
    plt.grid(True)
    plt.ylim([-100, 0])
    plt.show()

    # 2. 繪製最終策略圖 (Policy Grid)
    draw_policy(trained_q_agent, "Q-learning policy")
    draw_policy(trained_sarsa_agent, "Sarsa policy")