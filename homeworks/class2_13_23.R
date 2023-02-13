getwd()
# Exercise 1
# Consider a deck of 32 cards. Each card has a suit (Hearts, Spades, Clubs, Diamonds)
# and a value (Ace, King, Queen, Jack, 10, 9, 8, 7). A hand is a set of 5 cards drawn
# from this deck, regardless of the order of the cards drawn. Determine the number of hands:
# • comprising exactly 3 Hearts;
# • having exactly one king and exactly two Queens;
# • with at most 2 Kings.
choose(8, 3)
choose(24, 2)
choose(24, 2) * choose(8, 3)
# having exactly one king and exactly two Queens
choose(4, 1) * choose(4, 2) * choose(24, 2)
# with at most 2 Kings
choose(4, 0) * choose(28, 5) + choose(4, 1) * choose(24, 4) + choose(4, 2) * choose(20, 3)

# Exercise 2
# An assembly of 30 people wishes to elect a delegation of 4 people to represent
# them at a congress.
# a.	How many delegations can be formed in this way?
# b.	Alice and Bob can't stand each other and don't want to be both part of the delegation.
# How many possibilities are there?
# c.	Alice and Bob finally agree to work together if necessary. Nevertheless,
# the inseparable Camille and Dominique will only be part of the delegation if
# they are both chosen. How many different delegations can be formed under these conditions?

# a.	How many delegations can be formed in this way?
choose(30, 4)
# b.	Alice and Bob can't stand each other and don't want to be both part of the delegation.
# How many possibilities are there?
choose(28, 4) + choose(28, 3) + choose(28, 3)
choose(30, 4) - choose(28, 2)
# c.	Alice and Bob finally agree to work together if necessary. Nevertheless,
# the inseparable Camille and Dominique will only be part of the delegation if
# they are both chosen. How many different delegations can be formed under these conditions?
choose(28, 2) + choose(28, 4)

# Exercise 3
# You must hitch your reindeers Prancer, Quentin, Rudy and Jebediah, to your sled.
# They are hitched in single file. If Rudy and Prancer are not behind each other,
# they will refuse to move forward. In how many ways can you build your team?
#different orderings
choose(4, 2) + choose(4, 2)


# Exercise 4
# Calculate the sum
# 9C0 - 9C1 + 9C2 - 9C3 + 9C4 - 9C5 + 9C6 - 9C7 + 9C8 - 9C9 =
# SUMMATION (-1)^k * 9Ck
for (k in 0:9) {
  print((-1)^k * choose(9, k))
}

