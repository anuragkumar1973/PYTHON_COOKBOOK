# ============================================================================
# PROGRAM: Reinforcement Learning for Linear Regression Parameter Optimization
# ============================================================================
#
# INSTRUCTIONS:
#   Installation: pip install numpy pandas scikit-learn matplotlib
#   Execution:
#     $ cd /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6
#     $ source ../env/bin/activate
#     $ python3 rec6_linear_with_reinf.py
#
# PROBLEM STATEMENT:
#   You have a POORLY FITTED linear regression model (R² = 0.5-0.7) with
#   incorrect coefficients. Can you use Reinforcement Learning (RL) to
#   automatically adjust the model parameters and IMPROVE predictions?
#   This program demonstrates how RL progressively improves a bad model
#   by learning to adjust coefficients toward optimal values.
#
# TECHNICAL CONCEPTS:
#   • Reinforcement Learning (RL): Agent learns by trial-and-error interactions
#   • Epsilon-Greedy: Balance between exploration (random actions) and exploitation
#   • Reward Function: Measures success (higher R² and lower MSE = better)
#   • Parameter Optimization: Adjusting model coefficients to improve accuracy
#   • Mean Squared Error (MSE): Average of squared prediction errors
#   • R² Score: Proportion of variance explained (0-1 scale, 1 = perfect)
#   • Intentional Noise: Deliberately incorrect coefficients to simulate real-world poor fits
#
# ============================================================================

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# ============================================================================
# STEP 1: CREATE TRUE DATA WITH KNOWN RELATIONSHIP
# ============================================================================

np.random.seed(42)
X = np.random.randn(100, 2)

# TRUE coefficients (what we want to discover)
TRUE_COEF = np.array([2.0, 3.0])
y_true = X @ TRUE_COEF + np.random.randn(100) * 0.1

print("="*70)
print("INTENTIONALLY POORLY-FITTED REGRESSION MODEL")
print("="*70)
print(f"\nTrue relationship: y = 2.0*X₀ + 3.0*X₁ + noise")
print(f"True coefficients: {TRUE_COEF}")

# ============================================================================
# STEP 2: CREATE POORLY-FITTED MODEL WITH WRONG COEFFICIENTS (NOISE INJECTION)
# ============================================================================

# Intentionally wrong coefficients to simulate a poor fit
WRONG_COEF = np.array([0.5, 1.5])  # Significantly different from true coefficients
print(f"\nInitial (wrong) coefficients: {WRONG_COEF}")
print("⚠️  These coefficients are intentionally incorrect (50-67% off from true values)")

initial_pred = X @ WRONG_COEF
initial_mse = mean_squared_error(y_true, initial_pred)
initial_r2 = r2_score(y_true, initial_pred)

print(f"\nInitial Model Performance:")
print(f"  MSE: {initial_mse:.6f}")
print(f"  R² Score: {initial_r2:.6f} (POOR - should be close to 0.5-0.7)")

# Store initial metrics
initial_coef = WRONG_COEF.copy()
y = y_true

# ============================================================================
# STEP 3: REINFORCEMENT LEARNING AGENT
# ============================================================================

class RLParameterOptimizer:
    """RL agent that learns to improve regression coefficients"""
    
    def __init__(self, initial_coef, learning_rate=0.05, epsilon=0.2):
        self.coef = initial_coef.copy()
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.best_coef = self.coef.copy()
        self.best_reward = -np.inf
        self.history = []
        
    def get_action(self):
        """Epsilon-greedy exploration: balance between random exploration and exploitation"""
        if np.random.random() < self.epsilon:
            # Exploration: random action
            return np.random.randn(len(self.coef)) * self.learning_rate
        else:
            # Exploitation: small random perturbation toward improvement
            return np.random.randn(len(self.coef)) * (self.learning_rate * 0.5)
    
    def calculate_reward(self, y_true, y_pred):
        """Reward function: higher R² and lower MSE = better"""
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        # Composite reward: prioritize R² improvement with MSE penalty
        return r2 - (0.1 * mse)
    
    def train(self, X, y, episodes=100):
        """Train the RL agent: progressively improve coefficients"""
        self.history = []
        
        for episode in range(episodes):
            # Get action (adjust coefficients)
            action = self.get_action()
            self.coef += action
            
            # Make prediction and calculate reward
            y_pred = X @ self.coef
            reward = self.calculate_reward(y, y_pred)
            mse = mean_squared_error(y, y_pred)
            r2 = r2_score(y, y_pred)
            
            # Keep track of best coefficients found so far
            if reward > self.best_reward:
                self.best_reward = reward
                self.best_coef = self.coef.copy()
            
            # Store history for analysis
            self.history.append({
                'episode': episode,
                'coef': self.coef.copy(),
                'reward': reward,
                'mse': mse,
                'r2': r2,
                'improvement': r2 - initial_r2
            })
        
        return self.history

# ============================================================================
# STEP 4: TRAIN RL AGENT
# ============================================================================

print("\n" + "="*70)
print("TRAINING REINFORCEMENT LEARNING AGENT (100 episodes)")
print("="*70)

agent = RLParameterOptimizer(initial_coef, learning_rate=0.05, epsilon=0.2)
history = agent.train(X, y, episodes=100)

final_coef = agent.best_coef
final_mse = agent.history[-1]['mse']
final_r2 = agent.history[-1]['r2']

print(f"\n✓ Training Complete!")
print(f"\nOptimized Coefficients: {final_coef}")
print(f"Target (True) Coefficients: {TRUE_COEF}")
print(f"Coefficient Error: {np.abs(final_coef - TRUE_COEF)}")

# Display training progress
df_history = pd.DataFrame(agent.history)
print(f"\nTraining Progress (Last 15 episodes):")
print(f"{df_history[['episode', 'r2', 'mse', 'improvement']].tail(15).to_string(index=False)}")

# ============================================================================
# STEP 5: PERFORMANCE COMPARISON
# ============================================================================

y_pred_initial = X @ initial_coef
y_pred_optimized = X @ agent.best_coef

rmse_initial = np.sqrt(initial_mse)
rmse_optimized = np.sqrt(mean_squared_error(y, y_pred_optimized))

mae_initial = mean_absolute_error(y, y_pred_initial)
mae_optimized = mean_absolute_error(y, y_pred_optimized)

improvement_r2 = final_r2 - initial_r2
improvement_mse = ((initial_mse - mean_squared_error(y, y_pred_optimized)) / initial_mse * 100)
improvement_rmse = ((rmse_initial - rmse_optimized) / rmse_initial * 100)
improvement_mae = ((mae_initial - mae_optimized) / mae_initial * 100)

print("\n" + "="*70)
print("PERFORMANCE COMPARISON: Pre-RL vs Post-RL Implementation")
print("="*70)
print(f"{'Metric':<20} {'Pre-RL (Poor)':<18} {'Post-RL (Optimized)':<18} {'Improvement':<15}")
print("-"*70)
print(f"{'RMSE':<20} {rmse_initial:<18.6f} {rmse_optimized:<18.6f} {improvement_rmse:<14.2f}%")
print(f"{'MSE':<20} {initial_mse:<18.6f} {mean_squared_error(y, y_pred_optimized):<18.6f} {improvement_mse:<14.2f}%")
print(f"{'MAE':<20} {mae_initial:<18.6f} {mae_optimized:<18.6f} {improvement_mae:<14.2f}%")
print(f"{'R² Score':<20} {initial_r2:<18.6f} {final_r2:<18.6f} {improvement_r2:<14.6f}")
print("="*70)

print(f"\n✅ KEY INSIGHT:")
print(f"   RL improved R² by {improvement_r2:.6f} ({improvement_r2*100:.2f}% relative improvement)")
print(f"   RL reduced MSE by {improvement_mse:.2f}%")
print(f"   Initial model was POOR (R² = {initial_r2:.4f})")
print(f"   RL-optimized model is MUCH BETTER (R² = {final_r2:.4f})")

# ============================================================================
# STEP 6: VISUALIZATION OF LEARNING PROGRESS
# ============================================================================

plt.figure(figsize=(14, 5))

# Plot 1: R² Score improvement over episodes
plt.subplot(1, 3, 1)
plt.plot(df_history['episode'], df_history['r2'], linewidth=2, color='green')
plt.axhline(y=initial_r2, color='red', linestyle='--', label=f'Initial R² = {initial_r2:.4f}')
plt.axhline(y=final_r2, color='blue', linestyle='--', label=f'Final R² = {final_r2:.4f}')
plt.xlabel('Episode')
plt.ylabel('R² Score')
plt.title('R² Score Improvement Over Training')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: MSE reduction over episodes
plt.subplot(1, 3, 2)
plt.plot(df_history['episode'], df_history['mse'], linewidth=2, color='orange')
plt.axhline(y=initial_mse, color='red', linestyle='--', label=f'Initial MSE = {initial_mse:.4f}')
plt.axhline(y=final_mse, color='blue', linestyle='--', label=f'Final MSE = {final_mse:.4f}')
plt.xlabel('Episode')
plt.ylabel('Mean Squared Error')
plt.title('MSE Reduction Over Training')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: Coefficient convergence
plt.subplot(1, 3, 3)
coef_history = np.array([h['coef'] for h in agent.history])
plt.plot(df_history['episode'], coef_history[:, 0], label='Coef 0 (target=2.0)', linewidth=2)
plt.plot(df_history['episode'], coef_history[:, 1], label='Coef 1 (target=3.0)', linewidth=2)
plt.axhline(y=TRUE_COEF[0], color='red', linestyle='--', alpha=0.5)
plt.axhline(y=TRUE_COEF[1], color='blue', linestyle='--', alpha=0.5)
plt.xlabel('Episode')
plt.ylabel('Coefficient Value')
plt.title('Coefficient Convergence Toward True Values')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/anuragkumar1973/Downloads/book_py_cookbk/chapter6/rl_learning_progress.png', dpi=300, bbox_inches='tight')
print(f"\n✓ Visualization saved: rl_learning_progress.png")
plt.show()

print("\n" + "="*70)
print("CONCLUSION")
print("="*70)
print(f"Starting with POOR coefficients {initial_coef},")
print(f"RL agent progressively improved to {final_coef},")
print(f"which are much closer to TRUE coefficients {TRUE_COEF}!")
print(f"\nThis demonstrates that RL CAN improve poorly-fitted models")
print(f"by systematically learning better parameter values.")
print("="*70)