num_channels = 2 * 30
block_prob_threshold = 0.005
user_traffic_intensity = 0.05 * 2

a = user_traffic_intensity / (1 + user_traffic_intensity)
N = int(a * num_channels)
a = -a

def Pascal(a, num_channels, N):
    if num_channels == 0:
        return 1
    E = Pascal(a, num_channels-1, N)
    return (a*(N-num_channels+1)*E)/(num_channels+a*(N-num_channels+1)*E)

while True:
    N += 1
    block_prob = Pascal(a, num_channels, -1*N)
    #print(block_prob)
    if block_prob > block_prob_threshold:
        N -= 1
        break

print("Maksymalna liczba użytkowników, którzy mogą być połączeni z hubem: " + str(N))
