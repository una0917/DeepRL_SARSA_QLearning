import numpy as np
import matplotlib.pyplot as plt

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
        # 初始化 Q-table 為 0 (4 x 12 個狀態，每個狀態 4 個動作)
        self.q_table = np.zeros((4, 12, 4))
        
    def choose_action(self, state):
        # Epsilon-greedy 策略
        if np.random.rand() < self.epsilon:
            return np.random.randint(4) # 隨機探索
        else:
            r, c = state
            # 選擇 Q 值最大的動作，若有多個相同最大值則隨機挑一個
            q_values = self.q_table[r, c, :]
            max_q = np.max(q_values)
            actions = np.where(q_values == max_q)[0]
            return np.random.choice(actions)

class QLearningAgent(RLAgent):
    def update(self, state, action, reward, next_state, next_action, done):
        r, c = state
        nr, nc = next_state
        # Q-learning (Off-policy): 取下一狀態所有動作中的最大 Q 值
        target = reward if done else reward + self.gamma * np.max(self.q_table[nr, nc, :])
        self.q_table[r, c, action] += self.alpha * (target - self.q_table[r, c, action])

class SarsaAgent(RLAgent):
    def update(self, state, action, reward, next_state, next_action, done):
        r, c = state
        nr, nc = next_state
        # SARSA (On-policy): 取實際採取的下一動作之 Q 值
        target = reward if done else reward + self.gamma * self.q_table[nr, nc, next_action]
        self.q_table[r, c, action] += self.alpha * (target - self.q_table[r, c, action])

# ==========================================
# 3. 訓練與比較
# ==========================================
def train(agent_class, episodes=500, runs=50):
    all_rewards = np.zeros(episodes)
    
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
                
                # 更新 Q-table
                agent.update(state, action, reward, next_state, next_action, done)
                
                state = next_state
                action = next_action
                ep_reward += reward
                
            run_rewards.append(ep_reward)
        all_rewards += np.array(run_rewards)
        
    # 回傳多次跑完的平均值以平滑曲線
    return all_rewards / runs

if __name__ == "__main__":
    print("Training SARSA...")
    sarsa_rewards = train(SarsaAgent)
    
    print("Training Q-Learning...")
    q_rewards = train(QLearningAgent)

    # 繪製圖表
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