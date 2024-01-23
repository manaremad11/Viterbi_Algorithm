# transitional probabilities
p_s_s = 0.8
p_s_r = 0.2
p_r_s = 0.4
p_r_r = 0.6

# initial probabilities
p_s = 0.6
p_r = 0.4

# emission probabilities
p_s_h = 0.8
p_s_g = 0.2
p_r_h = 0.4
p_r_g = 0.6

# sequence example
moods = ['G', 'G', 'H', 'H', 'H', 'H', 'G']
probabilities = []
weather = []
if moods[0] == 'H':
    # we have two cases, either it's sunny and he's happy, or rainy and he's happy
    probabilities.append((p_s * p_s_h, p_r * p_r_h))
else:
    # we have two cases, either it's sunny and he's grumpy, or rainy and he's grumpy
    probabilities.append((p_s * p_s_g, p_r * p_r_g))

for i in range(1, len(moods)):
    # first prob in the pair represents yesterday was sunny, second one it was rainy
    yesterday_sunny, yesterday_rainy = probabilities[-1]
    if moods[i] == 'H':
        today_sunny = max(yesterday_sunny * p_s_s * p_s_h, yesterday_rainy * p_r_s * p_s_h)
        today_rainy = max(yesterday_sunny * p_s_r * p_r_h, yesterday_rainy * p_r_r * p_r_h)
        probabilities.append((today_sunny, today_rainy))
    else:
        today_sunny = max(yesterday_sunny * p_s_s * p_s_g, yesterday_rainy * p_r_s * p_s_g)
        today_rainy = max(yesterday_sunny * p_s_r * p_r_g, yesterday_rainy * p_r_r * p_r_g)
        probabilities.append((today_sunny, today_rainy))

for p in probabilities:
    if p[0] > p[1]:
        weather.append('S')
    else:
        weather.append('R')
print("Wheather sequence is: ", weather)
