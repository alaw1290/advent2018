def insert_marble(marble_n, marbles, current_marble_index):
    marble_n_index = ((current_marble_index + 1) % len(marbles)) + 1
    marbles.insert(marble_n_index, marble_n)
    return marbles, marble_n_index

def get_points(marble_n, marbles, current_marble_index):
    marble_m_index = current_marble_index - 7
    if marble_m_index < 0:
        marble_m_index = len(marbles) + marble_m_index
    marble_m = marbles.pop(marble_m_index)
    return marbles, marble_m_index, marble_n + marble_m

def play_marbles(players, max_marble_n):
    marbles = [0]
    current_marble_index = 0
    current_player = 0
    player_scores = {i:0 for i in range(players)}
    for marble_n in range(1,max_marble_n+1):
        if marble_n % 23 == 0:
            marbles, current_marble_index, score = get_points(marble_n, marbles, current_marble_index)
            player_scores[current_player] += score
            # print(f"{current_player}: {marbles[current_marble_index]}:  {score}")
            
        else:
            marbles, current_marble_index = insert_marble(marble_n, marbles, current_marble_index)
        
        # print(f"{current_player}: {marbles[current_marble_index]}:  {marbles}")
        current_player = (current_player + 1) % players


    print(sorted([(player_scores[i],i) for i in player_scores])[-1])

if __name__ == '__main__':
    # play_marbles(9,25)
    # play_marbles(10,1618)
    # play_marbles(13,7999)
    # play_marbles(17,1104)
    # play_marbles(21,6111)
    # play_marbles(30,5807)
    play_marbles(403,71920)
    # play_marbles(403,71920*100)