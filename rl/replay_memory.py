import numpy as np
from collections import deque


class ReplayMemory(object):

    '''
    The replay memory used for random minibatch training
    '''

    def __init__(self, env_spec):
        self.env_spec = env_spec
        self.memory_keys = [
            'states', 'actions', 'rewards', 'next_states', 'terminals']
        self.memory = {k: [] for k in self.memory_keys}
        self.state = None

    def reset_state(self, init_state):
        '''
        reset the state of ReplayMemory per episode env.reset()
        '''
        self.state = init_state

    def one_hot_action(self, action):
        action_arr = np.zeros(self.env_spec['action_dim'])
        action_arr[action] = 1
        return action_arr

    def add_exp(self, action, reward, next_state, terminal):
        '''
        after the env.step(a) that returns s', r,
        using the previously stored state for the s,
        form an experience tuple <s, a, r, s'>
        '''
        self.memory['states'].append(self.state)
        self.memory['actions'].append(self.one_hot_action(action))
        self.memory['rewards'].append(reward)
        self.memory['next_states'].append(next_state)
        self.memory['terminals'].append(int(terminal))
        self.state = next_state

    def _get_exp(self, exp_name, inds):
        return np.array([self.memory[exp_name][i] for i in inds])

    def get_exp(self, inds):
        # change to get by indices en-masse
        # pick it up directly by dict, so no need to transpose
        return {k: self._get_exp(k, inds) for k in self.memory_keys}

    def size(self):
        return len(self.memory['rewards'])

    def rand_minibatch(self, size):
        '''
        get a minibatch of random exp for training
        '''
        memory_size = self.size()
        if memory_size <= size:
            # to prevent repetition and initial overfitting
            rand_inds = np.random.permutation(memory_size)
        else:
            rand_inds = np.random.randint(
                memory_size, size=size)
        minibatch = self.get_exp(rand_inds)
        return minibatch