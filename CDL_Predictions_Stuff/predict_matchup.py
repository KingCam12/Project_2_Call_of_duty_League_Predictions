def predict_matchup(team_a, team_b):
    try:
        # Extract average stats for Team A and Team B
        team_a_stats = cleaned_data[cleaned_data['Current Team'] == team_a][features].mean()
        team_b_stats = cleaned_data[cleaned_data['Current Team'] == team_b][features].mean()

        # Calculate stat differences
        stat_diffs = pd.DataFrame([team_a_stats - team_b_stats], columns=features)

        # Predict outcomes
        probabilities = model.predict_proba(stat_diffs)[0]  # Probabilities for [Team B Wins, Team A Wins]
        prediction = model.predict(stat_diffs)[0]

        # Display results
        print("\n--- Matchup Prediction Results ---")
        print(f"Team A: {team_a}")
        print(f"Team B: {team_b}")
        print(f"Predicted Winner: {'Team A' if prediction == 1 else 'Team B'}")
        print("\nCategory Win Probabilities:")
        print(f"  Overall KD: {probabilities[1]:.2%} chance Team A wins")
        print(f"  Search Destroy KD: {probabilities[1]:.2%} chance Team A wins")
        print(f"  Control KD: {probabilities[1]:.2%} chance Team A wins")
        print(f"  Hardpoint KD: {probabilities[1]:.2%} chance Team A wins")
    except Exception as e:
        print(f"An error occurred during prediction: {e}")