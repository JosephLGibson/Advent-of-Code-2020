from d_23_parse import input_parse

def get_next_cup(pos):
	return (pos - 2) % 9 + 1

cups = input_parse()
successor = [0 for _ in range(len(cups) + 1)]
for pos in range(len(cups) - 1):
	successor[cups[pos]] = cups[pos + 1]
successor[cups[-1]] = cups[0]

current_cup = cups[0]
for _ in range(100):
	removed_cups = [successor[current_cup]]
	for _ in range(2):
		removed_cups.append(successor[removed_cups[-1]])
	successor[current_cup] = successor[removed_cups[-1]]
	destination_cup = get_next_cup(current_cup)
	while destination_cup in removed_cups:
		destination_cup = get_next_cup(destination_cup)
	after = successor[destination_cup]
	successor[destination_cup] = removed_cups[0]
	successor[removed_cups[2]] = after
	current_cup = successor[current_cup]

output = ""
current_cup = successor[1]
while current_cup != 1:
	output += str(current_cup)
	current_cup = successor[current_cup]
print(output)