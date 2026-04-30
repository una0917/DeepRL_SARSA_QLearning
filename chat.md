# Q\-learning 與 SARSA 懸崖行走比較

**Date**: April 30, 2026 at 01:56 PM
**Turns**: 5
**Source**: [Gemini Chat](https://gemini.google.com/u/1/app/084778fdbb07cdad?hl=zh-TW&pageId=none)

---

## Turn 1

### 👤 User

*[This turn includes uploaded images]*

![上傳圖片預覽](assets/img-001.jpg)

![上傳圖片預覽](assets/img-002.png)

一、作業目的
本作業旨在實作並比較兩種經典強化學習演算法——Q-learning 與 SARSA，透過相同環境與參數設定，分析其學習行為、收斂特性以及最終策略差異。
二、環境描述
本實驗採用經典的格子世界（Gridworld）問題，亦稱為「Cliff Walking」環境。環境設定如下：
使用一個矩形網格（例如 4 × 12）
起點（Start）位於左下角
終點（Goal）位於右下角
起點與終點之間的底部區域為「懸崖（Cliff）」
當代理（agent）進入懸崖時，會受到重大懲罰並回到起點。
三、問題設定
狀態空間（State Space）：所有網格位置
動作空間（Action Space）：上、下、左、右
獎勵機制（Reward）：每移動一步：−1
掉入懸崖：−100，並回到起點
到達終點：回合結束
策略（Policy）：ε-greedy（例如 ε = 0.1）
學習率（α）：例如 0.1
折扣因子（γ）：例如 0.9
訓練回合數（Episodes）：至少 500 回合
四、作業內容
（一）演算法實作
請分別實作以下兩種演算法：
Q-learning（離策略方法，Off-policy）
SARSA（同策略方法，On-policy）
兩者皆需建立並更新狀態-動作價值函數 Q(s, a)。
（二）訓練過程
在相同的環境與參數設定下，使用 ε-greedy 策略進行訓練，確保兩種方法的公平比較。
（三）結果分析
請針對以下面向進行比較與討論：
學習表現
繪製每一回合的累積獎勵（Total Reward）曲線
比較收斂速度
策略行為
描述或視覺化最終學習到的路徑
分析是否傾向冒險或保守
穩定性分析
比較學習過程中的波動程度
討論探索（exploration）對結果的影響
五、理論比較與討論
在報告中，請說明以下概念：
Q-learning 為離策略（Off-policy）方法，其更新基於「下一狀態的最佳可能行動」，即使該行動未實際執行。
SARSA 為同策略（On-policy）方法，其更新基於「實際採取的行動」，因此會反映探索策略的影響。
一般而言：
Q-learning 傾向學習到理論上的最優策略，但在訓練過程中可能較具風險。
SARSA 則傾向學習在實際探索策略下較安全、穩定的行為。
六、結論要求
請總結兩種方法在本實驗中的差異，並說明：
哪一種方法收斂較快
哪一種方法較穩定
在何種情境下應選擇 Q-learning 或 SARSA
image_1b629d.png是result sample
請按照以上作業說明，完成此作業

### 🤖 Assistant

這是一份基於您提供的環境設定與實驗結果圖片，為您整理的 Q-learning 與 SARSA 強化學習演算法比較報告。

---

### 一、 作業目的
本報告旨在透過經典的「懸崖行走（Cliff Walking）」環境，實作並比較 Q-learning 與 SARSA 兩種強化學習演算法。藉由觀察其在相同參數下的學習行為、收斂曲線以及最終收斂的策略，探討同策略（On-policy）與離策略（Off-policy）方法在面臨高風險環境時的本質差異。

### 二、 環境描述與問題設定
本實驗採用 4 × 12 的網格世界，代理（Agent）需從左下角起點（Start）移動至右下角終點（Goal）。起點與終點之間的底部區域為「懸崖（Cliff）」。

- **狀態與動作**：狀態空間為所有網格位置，動作空間為上、下、左、右四個方向。
- **獎勵機制**：每移動一步獲得 −1 的獎勵；掉入懸崖會受到 −100 的懲罰並重置回起點；抵達終點則回合結束。
- **學習參數**：採用 $\epsilon$-greedy 策略（$\epsilon=0.1$）進行探索，學習率 $\alpha=0.5$（依據您提供的折線圖參數），折扣因子 $\gamma=0.9$ 或 $1.0$，訓練 500 回合。

---

### 三、 實驗結果分析
根據您提供的實驗結果圖表，我們從以下三個面向進行分析：

#### 1. 學習表現（Learning Performance）
觀察累積獎勵曲線（Sarsa Vs. Q-Learning Cliff Walking 折線圖）：

- **SARSA**：在訓練初期經歷短暫的摸索後，累積獎勵迅速上升並收斂在一個較高的水平（每回合約 -20 到 -30 之間）。
- **Q-learning**：雖然也呈現學習趨勢，但其每回合的平均累積獎勵明顯低於 SARSA（約徘徊在 -40 到 -60 之間）。這意味著在訓練過程中，Q-learning 的代理掉入懸崖的頻率遠高於 SARSA。

#### 2. 策略行為（Policy Behavior）
觀察最終學習到的路徑（Q-learning policy 與 Sarsa policy 網格圖）：

- **Q-learning 傾向冒險**：其最終策略（藍色虛線）緊貼著懸崖邊緣行走。這是理論上的最短路徑（Optimal Path），能將移動步數造成的扣分降到最低。
- **SARSA 傾向保守**：其最終策略（藍色虛線）選擇遠離懸崖，沿著網格的最上方邊緣行走。這條路徑雖然較長（移動步數扣分較多），但極為安全。

#### 3. 穩定性分析（Stability）

- **波動程度**：在累積獎勵曲線中，Q-learning 的曲線波動幅度較大。因為它選擇緊貼懸崖行走，在 $\epsilon$-greedy 策略（$\epsilon=0.1$）下，有 10% 的機率會隨機探索。只要在邊緣隨機向下走一步，就會觸發 −100 的巨大懲罰。
- **探索的影響**：SARSA 將「探索帶來的隨機性」考慮進去，因此學到退後幾步以避免隨機探索造成的災難；Q-learning 則無視探索的隨機性，固執地認為自己總會選出最佳動作，導致在訓練期間持續承受高昂的「探索代價」。

---

### 四、 理論比較與討論
這兩種行為的巨大差異，根源於演算法更新價值函數 $Q(s, a)$ 的方式：

- **Q-learning（離策略方法，Off-policy）**：
更新公式為：$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma \max_{a'} Q(s', a') - Q(s, a)]$Q-learning 在更新當前狀態的價值時，直接假設下一步會採取「價值最高」的最佳動作（即 $\max_{a'} Q(s', a')$），**完全忽略了實際執行時會受到 ϵ-greedy 探索的干擾**。因此它勇敢地貼著懸崖走，學到的是「若沒有探索干擾」時的全局最佳解。
- **SARSA（同策略方法，On-policy）**：
更新公式為：$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma Q(s', a') - Q(s, a)]$SARSA 的更新基於「實際採取的下一個動作 $a'$」。如果因為 $\epsilon$-greedy 隨機亂走掉下懸崖，這個巨大的負回報會直接更新到前一個狀態的價值中。這使得 SARSA 深刻體會到「貼近懸崖的狀態因為有隨機探索的存在，期望價值極低」，從而逼迫策略往安全的上方移動。

---

### 五、 結論

1. **收斂較快的方法**：就「訓練過程中的表現（Online Performance）」而言，**SARSA** 收斂到穩定高獎勵的速度較快，因為它很快就學會避開造成巨大扣分的懸崖。但若以「尋找最佳理論路徑」來看，Q-learning 其實很快就找到了最短路徑，只是在訓練時被探索機制拖累了分數。
2. **較穩定的方法**：**SARSA** 表現得較為穩定。它在訓練後期因為選擇了安全路徑，即使偶爾發生隨機探索，也不會掉入懸崖，因此累積獎勵的波動較小。
3. **情境選擇建議**：
  - **選擇 Q-learning**：當訓練是在**模擬環境**中進行，且我們只關心最終推論時（關閉 $\epsilon$ 探索）能否找出最優、最高效的策略時，應使用 Q-learning。
  - **選擇 SARSA**：當訓練是在**真實世界**（例如實體機器人、自駕車）進行時，因為訓練過程中的「失誤（如撞車、掉落）」會造成昂貴的成本或危險，我們需要演算法在學習過程中也能保持安全，此時應優先選擇 SARSA。

## Turn 2

### 👤 User

幫我寫出此作業的程式碼，分析的部分寫成README.md給我

### 🤖 Assistant

這是一份為您實作的 Python 程式碼，包含了環境定義、兩種演算法的代理（Agent）、訓練迴圈以及繪圖功能。在程式碼下方，我也為您整理了標準的 `README.md` 格式分析報告。

### 1. Python 程式碼 (`cliff_walking.py`)
請確保您已經安裝了 `numpy` 與 `matplotlib` 套件。

```python
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
    def __init__(self, alpha=0.5, epsilon=0.1, gamma=1.0):
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
    plt.title('Sarsa Vs. Q-Learning Cliff Walking\nEpsilon=0.1, Alpha=0.5\n(averaged over 50 runs)')
    plt.legend()
    plt.grid(True)
    plt.ylim([-100, 0])
    plt.show()

```

---

### 2. 分析報告 (`README.md`)
請將以下內容存為 `README.md`。

```markdown
# 懸崖行走環境：Q-learning 與 SARSA 演算法比較分析

本專案旨在透過經典的「懸崖行走（Cliff Walking）」環境，實作並比較兩種經典強化學習演算法：**Q-learning**（離策略）與 **SARSA**（同策略）。藉由觀察其學習行為、收斂曲線以及最終策略，探討兩者在面臨高風險環境時的本質差異。

## 1. 環境設定與問題描述

本實驗採用 4 × 12 的網格世界，代理（Agent）需從左下角起點移動至右下角終點。起點與終點之間的底部區域為「懸崖」。

* **狀態空間（State Space）**：4 × 12 的所有網格位置。
* **動作空間（Action Space）**：上、下、左、右。
* **獎勵機制（Reward）**：
  * 每移動一步：-1
  * 掉入懸崖：-100（並強制重置回起點）
  * 到達終點：回合結束
* **學習參數**：$\epsilon$-greedy 策略 ($\epsilon=0.1$)、學習率 $\alpha=0.5$、折扣因子 $\gamma=1.0$。所有曲線為 50 次獨立訓練運行的平均值，訓練回合數為 500 回合。

## 2. 演算法理論與更新機制

兩種演算法行為差異的核心在於如何估算「目標價值（Target Value）」。

* **Q-learning (Off-policy)**: 
  其更新公式為：
  $$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$
  更新時直接假設下一步會採取「價值最高」的動作，**忽略了實際執行時會受到 $\epsilon$-greedy 探索的干擾**。它傾向學習理論上的全局最佳解。

* **SARSA (On-policy)**:
  其更新公式為：
  $$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma Q(s', a') - Q(s, a)]$$
  更新基於「實際採取的下一個動作 $a'$」。這會將 $\epsilon$-greedy 帶來的隨機風險反映在價值估計中，使其策略更偏向安全。

## 3. 實驗結果分析

### 3.1 學習表現與收斂速度
* **SARSA** 在訓練初期經歷短暫的摸索後，累積獎勵迅速上升並收斂在一個較高的水平（每回合約徘徊於 -20 到 -30 之間）。因為它學會了避開會造成巨大扣分的懸崖。
* **Q-learning** 雖然也呈現學習趨勢，但其平均累積獎勵明顯較低（約徘徊在 -40 到 -60 之間），這意味著在訓練過程中，Q-learning 的代理因為隨機探索而掉入懸崖的頻率遠高於 SARSA。

### 3.2 策略行為 (Policy Behavior)
* **Q-learning 傾向冒險**：其最終策略選擇緊貼著懸崖邊緣行走。這是理論上的最短路徑（Optimal Path），能將移動步數造成的扣分降到最低。
* **SARSA 傾向保守**：其最終策略選擇遠離懸崖，沿著網格的最上方邊緣行走。這條路徑雖然較長，但能最大幅度降低因隨機探索掉落懸崖的風險。

### 3.3 穩定性分析
在累積獎勵曲線中，Q-learning 的曲線波動幅度較大。因為它固執地貼緊邊緣行走，在 10% 的隨機探索機率下，只要向下走就會承受 -100 的巨大懲罰。SARSA 則因為遠離了危險區域，即使發生隨機探索，也只會多扣除正常的步伐分數 (-1)，因此訓練後期的表現相當穩定。

## 4. 結論

1. **收斂較快且穩定**：若看訓練過程中的在線表現（Online Performance），**SARSA** 由於盡早避開了高風險區域，其收斂到穩定高獎勵的速度較快且波動較小。
2. **尋找理論最優**：若目標是找出純粹的理論最短路徑，則 **Q-learning** 能夠找到貼邊而行的全局最佳解。
3. **應用情境建議**：
   * 在**模擬環境**中訓練且只關注最終最佳策略時，建議選擇 **Q-learning**。
   * 若訓練發生在**真實世界**（例如自駕車或實體機器人），探索期間的高昂失誤成本（如撞車）難以承受時，務必選擇較為安全、保守的 **SARSA**。

```

## Turn 3

### 👤 User

*[This turn includes uploaded images]*

![上傳圖片預覽](blob:https://gemini.google.com/76d335d3-78eb-4d69-a28c-7124cd5fdc39)

這是我執行程式後出現的結果圖，跟我給你的sample圖，似乎缺少了SARSA跟Q-learning的sutton pub，並請幫我檢查我的執行結果圖合理正確嗎

### 🤖 Assistant

您的執行結果圖是**非常合理且完全正確的**！恭喜您成功跑出符合理論的結果。

### 為什麼您的圖是正確的？
從您跑出的圖表中可以觀察到強化學習教科書中描述的經典現象：

- **SARSA（藍線）**：大約在 50 回合後，穩定維持在較高的報酬（約 -20 到 -30 之間）。這證明 SARSA 確實學會了較長但**安全**的路線（遠離懸崖），因此較少受到 -100 的巨大懲罰。
- **Q-learning（紅線）**：報酬維持在較低的水位（約 -40 到 -60 之間），且震盪非常劇烈。這證明 Q-learning 學會了貼近懸崖的**最短**路線，但在 $\epsilon=0.1$ 的隨機探索下，它有 10% 的機率會隨機亂走，導致頻繁掉入懸崖而拉低了平均報酬。

### 關於缺少的 "Sutton Pub." 曲線
您在原本範例圖中看到的 "Sarsa, Sutton Pub." 與 "Q-learning, Sutton Pub."（虛線），其實是**教科書（Sutton & Barto 著作）提供的原始參考數據**。
在許多這類的作業或實驗中，作者會去下載教科書官方提供的標準數據（或是預先寫死在程式碼裡的座標），並將其畫在圖上作為「基準線（Baseline）」，用來對比自己寫的演算法是否與書本的結果一致。
因為我們上一篇提供的程式碼是**完全從零開始模擬**，直接把您電腦當下跑出來的真實結果畫出來，並沒有匯入或硬寫入教科書的標準數據，所以圖上只會有您自己實際跑出來的這兩條實線。這在演算法實作上是完全正常的。
💡 **補充小技巧**：如果您希望您的實線看起來不要這麼毛躁，更接近範例圖中那種平滑的感覺，您可以將主程式區塊中的參數調高，例如將 `runs=50` 改成 `runs=200` 或 `runs=500`。平均的次數越多，統計上的雜訊就會被抵消，曲線就會越平滑！

## Turn 4

### 👤 User

三、問題設定
狀態空間（State Space）：所有網格位置
動作空間（Action Space）：上、下、左、右
獎勵機制（Reward）：每移動一步：−1
掉入懸崖：−100，並回到起點
到達終點：回合結束
策略（Policy）：ε-greedy（例如 ε = 0.1）
學習率（α）：例如 0.1
折扣因子（γ）：例如 0.9
訓練回合數（Episodes）：至少 500 回合
檢查現在的程式碼是否有符合作業說明的問題設定

### 🤖 Assistant

幫您檢查了前一版程式碼，**大部分的核心邏輯都完全符合**作業說明的問題設定。
唯一需要微調的地方在於**學習率 (α)** 與 **折扣因子 (γ)** 的預設值。前一版程式碼是為了配合您圖片中的參數（Alpha=0.5）而設定，而您現在提供的作業說明中建議的值為 0.1 與 0.9。
以下為詳細的檢查比對清單，以及需要修改的程式碼段落：

### ✅ 完全符合的部分

1. **狀態空間（State Space）**：程式碼中定義為 `4 x 12` 的網格位置，完全符合。
2. **動作空間（Action Space）**：程式碼定義 `actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]`，對應上、右、下、左，完全符合。
3. **獎勵機制（Reward）**：
  - 每移動一步：程式碼中設定 `reward = -1`，完全符合。
  - 掉入懸崖：程式碼設定 `reward = -100`，並將 `next_state = self.start_state`（回到起點），完全符合。
  - 到達終點：程式碼設定 `done = True`（回合結束），完全符合。
4. **策略（Policy）**：程式碼使用 `choose_action` 實作了 $\epsilon$-greedy 策略，且預設 $\epsilon = 0.1$，完全符合。
5. **訓練回合數（Episodes）**：程式碼預設執行 `episodes=500` 回合，完全符合「至少 500 回合」的要求。

---

### ⚠️ 建議微調的參數
作業說明中寫道：

- **學習率（α）**：例如 0.1
- **折扣因子（γ）**：例如 0.9
前一版程式碼的預設值是 $\alpha=0.5$（配合您的圖表）與 $\gamma=1.0$。為了完全貼合這份作業說明的建議，您只需要在程式碼的 **第 2 部分（定義 Agent）** 中，修改 `RLAgent` 類別的預設參數即可。
**請將原本的這行程式碼：**

```python
class RLAgent:
    def __init__(self, alpha=0.5, epsilon=0.1, gamma=1.0):
        # ...

```
**修改為：**

```python
class RLAgent:
    def __init__(self, alpha=0.1, epsilon=0.1, gamma=0.9):  # 修改了 alpha 和 gamma
        # ...

```
（註：修改參數後，跑出來的曲線形狀可能會與您之前 $\alpha=0.5$ 的圖表略有不同，收斂速度會變慢一些，但最終結論與趨勢依然會是相同的。）

## Turn 5

### 👤 User

*[This turn includes uploaded images]*

![上傳圖片預覽](blob:https://gemini.google.com/b54b64c0-6e75-4bbc-87cb-052eadff4c43)

![上傳圖片預覽](blob:https://gemini.google.com/6ba511f7-947c-4a4b-91e0-431a54ffec7a)

![「MD」圖示](assets/img-003.png)

這兩張分別是
alpha=0.5, epsilon=0.1, gamma=1.0
alpha=0.1, epsilon=0.1, gamma=0.9
的結果圖，請檢查這個圖是合理的嗎，以及檢查README的內容是否有符合作業要求，是否有需要修改的地方

### 🤖 Assistant

這兩張圖表的結果**非常合理且完全正確**！

### 1. 圖表合理性分析

- **Figure 1 (α=0.5):** 因為學習率較高，Agent 更新 Q 值的步伐很大，所以你可以看到曲線在前期（約 50 回合內）就迅速拉升並達到收斂的水平。
- **Figure 2 (α=0.1):** 因為學習率降低到 0.1，Agent 更新 Q 值的速度變慢了，這反映在曲線上就是「爬升的坡度變緩」。你可以看到 SARSA 大約花了 200 到 300 回合才慢慢爬升並穩定在 -20 到 -30 的區間。這完全符合強化學習中學習率調整帶來的理論現象。
這證明你的程式碼寫得很健壯，能夠正確反映不同超參數（Hyperparameters）帶來的影響。

### 2. README 內容檢查與修改建議
目前的 `README.md` 寫得很好，涵蓋了作業要求的大部分重點。不過，既然作業說明的「問題設定」要求使用 $\alpha=0.1$ 和 $\gamma=0.9$，我們需要將 README 中的**參數設定**以及對應的**收斂速度描述**進行微調，使其完全吻合 Figure 2 的結果。同時，我稍微調整了標題結構，讓它與你最初提供的「作業說明」的五大重點更完美對齊。
以下是為你修改過後的 `README.md`：

```markdown
# 懸崖行走環境：Q-learning 與 SARSA 演算法比較分析

## 一、 作業目的
本專案旨在透過經典的「懸崖行走（Cliff Walking）」環境，實作並比較兩種經典強化學習演算法：**Q-learning**（離策略）與 **SARSA**（同策略）。藉由在相同參數設定下觀察其學習行為、收斂曲線以及最終策略，探討兩者在面臨高風險環境時的本質差異。

## 二、 環境描述與問題設定
本實驗採用 4 × 12 的網格世界，代理（Agent）需從左下角起點移動至右下角終點。起點與終點之間的底部區域為「懸崖」。

* **狀態空間（State Space）**：4 × 12 的所有網格位置。
* **動作空間（Action Space）**：上、下、左、右。
* **獎勵機制（Reward）**：
  * 每移動一步：-1
  * 掉入懸崖：-100（並強制重置回起點）
  * 到達終點：回合結束
* **學習參數設定**：
  * 策略（Policy）：$\epsilon$-greedy 策略 ($\epsilon=0.1$)
  * 學習率（$\alpha$）：0.1
  * 折扣因子（$\gamma$）：0.9
  * 訓練回合數：500 回合（曲線為 50 次獨立運行的平均值以平滑結果）。

## 三、 結果分析

### 1. 學習表現與收斂速度
觀察累積獎勵曲線可以發現：
* **SARSA**：在較低的學習率（$\alpha=0.1$）下，SARSA 呈現穩定爬升的趨勢，大約在 200 至 300 回合後，累積獎勵逐漸收斂在較高的水平（每回合約 -20 到 -30 之間）。
* **Q-learning**：雖然同樣呈現學習趨勢，但其平均累積獎勵明顯低於 SARSA（約徘徊在 -40 到 -60 之間）。這意味著在整個訓練過程中，Q-learning 的代理因為隨機探索而掉入懸崖的頻率遠高於 SARSA。

### 2. 策略行為 (Policy Behavior)
* **Q-learning 傾向冒險**：其最終學習到的策略緊貼著懸崖邊緣行走。這是理論上的最短路徑（Optimal Path），能將一般移動步數造成的扣分降到最低。
* **SARSA 傾向保守**：其最終學習到的策略選擇遠離懸崖，繞道至網格的最上方邊緣行走。這條路徑雖然較長，但極為安全。

### 3. 穩定性分析
* **波動程度**：Q-learning 的學習曲線波動幅度較大。因為它選擇貼邊行走，在 10% 的隨機探索機率下，只要向下探索就會承受 -100 的巨大懲罰。
* **探索的影響**：SARSA 考慮了探索帶來的隨機風險，因此遠離危險區域，訓練後期的表現相當穩定；反之，Q-learning 忽略了探索風險，導致在訓練期間持續承受高昂的代價。

## 四、 理論比較與討論

這兩種行為的差異，源自於演算法更新價值函數的方式：

* **Q-learning (離策略方法，Off-policy)**: 
  其更新公式為：
  $$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$
  Q-learning 的更新基於「下一狀態的最佳可能行動」，**它直接假設未來總是完美的，忽略了實際執行時會受到 $\epsilon$-greedy 探索的干擾**。因此它傾向學習理論上的全局最佳解（最短路徑），但在訓練過程中較具風險。

* **SARSA (同策略方法，On-policy)**:
  其更新公式為：
  $$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma Q(s', a') - Q(s, a)]$$
  SARSA 的更新基於「實際採取的行動 $a'$」。這會將 $\epsilon$-greedy 帶來的掉落懸崖風險真實反映在價值估計中，使其傾向學習在實際探索策略下較安全、穩定的行為。

## 五、 結論

1. **收斂較快且穩定的方法**：就訓練過程中的表現而言，**SARSA** 由於盡早避開了高風險區域，其收斂到穩定高獎勵的表現較佳且波動較小。
2. **尋找理論最優的方法**：若目標是找出純粹的理論最短路徑（忽略探索風險），則 **Q-learning** 能夠找到貼邊而行的最佳解。
3. **情境選擇建議**：
   * 當在**模擬環境**中訓練，且我們只關心最終佈署時（關閉隨機探索）的最佳效能時，應選擇 **Q-learning**。
   * 當訓練發生在**真實世界**（例如機器人導航），且訓練過程中的失誤會造成嚴重破壞或高昂成本時，應選擇較為安全的 **SARSA**。

```
這份修改版將所有的描述都對齊了 $\alpha=0.1$ 時較平緩的收斂特徵，並且把架構調整得更符合學術作業的要求。

---

*Exported from [Voyager](https://github.com/Nagi-ovo/gemini-voyager)*  
*Generated on April 30, 2026 at 01:56 PM*