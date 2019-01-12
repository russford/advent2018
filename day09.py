class Node (object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left if left else self
        self.right = right if right else self

    def insert_after (self, val):
        n2 = Node(val, self, self.right)
        n2.right.left = n2
        n2.left.right = n2
        return n2

    def remove (self):
        self.left.right = self.right
        self.right.left = self.left

    def print (self):
        n = self
        while True:
            print ("{},".format(n.value), end =" ")
            n = n.right
            if n == self:
                print ()
                break

def play_game (players, max_marble):
    scores = [0] * players
    marbles = Node(0)
    curr_marble = marbles
    for curr_value in range(1, max_marble+1):
        if curr_value % 23:
            curr_marble = curr_marble.right
            curr_marble = curr_marble.insert_after(curr_value)
        else:
            scores[curr_value % players] += curr_value
            for i in range(7):
                curr_marble = curr_marble.left
            scores[curr_value % players] += curr_marble.value
            curr_marble.remove()
            curr_marble = curr_marble.right
        # print (curr_value % players+1, curr_marble.value, end="\t")
        # marbles.print()

    print(players, max_marble, scores.index(max(scores)), max(scores))

# play_game(9, 25)
# play_game(10, 1618)
# play_game(13, 7999)
# play_game(17, 1104)
# play_game(21, 6111)
# play_game(30, 5807)

play_game (411, 71170)
play_game (411, 7117000)
