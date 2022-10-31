from statistics import mean, stdev
from random import shuffle

drugTest = [7.1, 8.5, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [7.2, 7.9, 7.8, 7.7, 7.6, 7.5, 7.4, 7.3, 7.2, 7.1, 7.0]

print(mean(drugTest))

print(mean(placebo))

obs_diff = mean(drugTest) - mean(placebo)

combined = drugTest + placebo

num_samples = len(drugTest)

shuffle(combined)

new_drugTest = combined[:num_samples]

new_placebo = combined[num_samples:]

def trial():
    shuffle(combined)
    new_drugTest = combined[:num_samples]
    new_placebo = combined[num_samples:]
    return mean(new_drugTest) - mean(new_placebo)

n = 10000

print(sum([trial() > obs_diff for _ in range(n)]) / n)