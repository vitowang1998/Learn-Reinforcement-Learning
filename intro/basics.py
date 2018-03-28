# History about Reinforcement Learning

# Theory about deep learning and reinforcement learning are formed in 1970s/1980s.
# Reinforcement Learning is different from supervised/unsupervised learning.


# SupervisedLearning general model
class SupervisedLearning
    '''
    fit(X, Y) takes an sample X from  input and tries to predict X to fit target Y
    vars:
        X: The current sample from input
        Y: The target sample
    requires: valid X, Y
    time: O(1)
    '''
    def fit(X, Y):

    '''
    predict(X) predicts a Y based on the sample input(x)
    vars:
        X: The current sample from input
    requires: valid X
    time: O(1)
    '''
    def predict(X):



# UnsupervisedLearning general model
class UnsupervisedLearning

    def fix(X):

    def transform(X):

    

# RL, on the other hand, has a much bigger interface.
# It takes the entire environment instead of several training parameters X and
#     Y as the parameter.

# RL can be used in psychology and predicting animal behavior.

# SL focuses on increase performance and lower the cost. 
# Unlike SL and UL, RL focuses on getting a message back from the environment, 
#     and this process should be autometic.
# In SL, labels need to be manually added so that the algorithm can be trained, 
#     but in RL, we train the algorithm based on the feedback from the environment. 



# Terminologies
# 1. Agent: The object that lives in the environment. The object into which we 
#           are trying to code AI.
# 2. Environment: The place, whether virtual or real, in which the agent lives.
# 3. State: DIfferent combinations of the factor parameters of the environment. 
#           State only involves the information that the agent can sense.
# 4. Rewards: The feedback from the environment. Positive reward should be given
#             if AI performs expectedly, otherwise, negative reward
#             should be given.
# 5. SAR Triples: abbe. of State, Action, Reward.



