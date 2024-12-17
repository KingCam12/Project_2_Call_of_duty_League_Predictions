
def interactive_matchup_tool():
    print("\nWelcome to the Team Matchup Prediction Tool!")
    available_teams = cleaned_data['Current Team'].unique()

    # Display all available teams
    print("\nAvailable Teams:")
    for idx, team in enumerate(available_teams):
        print(f"{idx + 1}. {team}")

    while True:
        try:
            # Input Team A
            team_a_input = input("\nEnter the number for Team A: ").strip()
            if not team_a_input.isdigit() or int(team_a_input) not in range(1, len(available_teams) + 1):
                print("Invalid input. Please enter a valid team number for Team A.")
                continue
            team_a_input = int(team_a_input) - 1

            # Input Team B
            team_b_input = input("Enter the number for Team B: ").strip()
            if not team_b_input.isdigit() or int(team_b_input) not in range(1, len(available_teams) + 1):
                print("Invalid input. Please enter a valid team number for Team B.")
                continue
            team_b_input = int(team_b_input) - 1

            if team_a_input == team_b_input:
                print("Team A and Team B cannot be the same. Please try again.")
                continue

            # Get team names
            team_a = available_teams[team_a_input]
            team_b = available_teams[team_b_input]

            # Predict the matchup
            predict_matchup(team_a, team_b)

            # Option to continue or exit
            cont = input("\nWould you like to compare another matchup? (yes/no): ").strip().lower()
            if cont == 'no':
                print("Thank you for using the prediction tool. Goodbye!")
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")