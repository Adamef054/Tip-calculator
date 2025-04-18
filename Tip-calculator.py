# Tip calculator

bill = float(input('What is the total bill?: '))
tip = int(input('What is the percentage tip would you like to give? 10, 12, or 15?: '))
people = int(input('How many people are you to split the bill?: '))

total_with_tip = ((tip / 100) * bill + bill) / people

print(f'Total for each person: {total_with_tip}')