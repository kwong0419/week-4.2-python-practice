from capitals import states
import random

# dictionary to map state names to their capitals
state_capital_dict = {state['name']: state['capital'] for state in states}

def play_game(states_list):
    score = 0
    total_questions = len(states_list)
    state_stats = {item['name']: {'correct': 0, 'incorrect': 0} for item in states_list}
    
    random.shuffle(states_list)

    print("Welcome to the State Capitals Game!")
    print(f"You'll be asked to identify the capital of {total_questions} states.")
    print("Let's begin!\n")

    for state in states_list:
        user_answer = input(f"What is the capital of {state['name']}? ").lower()
        correct_answer = state['capital'].lower()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
            state_stats[state['name']]['correct'] += 1
        else:
            print(f"Sorry, that is wrong. The correct answer is {state['capital']}.")
            state_stats[state['name']]['incorrect'] += 1

        print(f"Your current score: {score}/{total_questions}\n")

    print(f"Game over! Your final score is {score}/{total_questions}")
    return state_stats

def get_difficult_states(state_stats):
    return [{'name': state, 'capital': state_capital_dict[state]} 
            for state, _ in sorted(state_stats.items(), key=lambda x: x[1]['incorrect'], reverse=True)]

def main():
    while True:
        state_stats = play_game(states)
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
        
        focus_on_difficult = input("Would you like to focus on the states you found most difficult? (yes/no): ").strip().lower()
        
        if focus_on_difficult == 'yes':
            difficult_states = get_difficult_states(state_stats)
            states_to_play = difficult_states[:10]
        else:
            states_to_play = states

        state_stats = play_game(states_to_play)

if __name__ == "__main__":
    main()
