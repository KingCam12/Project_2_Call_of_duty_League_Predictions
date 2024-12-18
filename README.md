# **Team Matchup Prediction Tool**

## **Overview**
The **Team Matchup Prediction Tool** predicts the outcome of Call of Duty League matchups based on team stats, such as **Overall KD**, **Search Destroy KD**, **Control KD**, and **Hardpoint KD**. This interactive tool lets users input two teams, compare their performance metrics, and calculate the likelihood of each team winning.
### Project Overview
The Team Matchup Prediction Tool is designed to provide data-driven insights into match outcomes in the Call of Duty League (CDL). 
By leveraging advanced machine learning models, the tool predicts the
likelihood of a team winning based on key performance metrics, including:
Overall KD, Search Destroy KD, Control KD, Hardpoint KD
### Why Predictions Matter
Sports Betting:
Accurate predictions are critical for bettors looking to make informed decisions. 
Traditional sports betting markets are increasingly incorporating eSports, and CDL predictions provide a competitive edge.
By analyzing team performance data, this tool helps bettors identify favorable odds and reduce the risks of their wagers.
---
## **Features**
- Predicts the winner of a matchup based on trained machine learning models.
- Provides **win probabilities** for each KD category:
  - Overall KD
  - Search Destroy KD
  - Control KD
  - Hardpoint KD
- Interactive interface for easy team selection.
- Supports multiple comparisons in a single session.

---

## **Requirements**
To run the project, you need:
- Python 3.7 or higher
- The following Python libraries:
  - `pandas`
  - `numpy`
  - `joblib`
  - `scikit-learn`

---

## **Setup Instructions**

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd team-matchup-prediction-tool
---

# Example Usage
```
Welcome to the Team Matchup Prediction Tool!

Available Teams:
1. ATL FaZe
2. Optic Texas
3. LA Thieves
4. VAN Surge

Enter the number for Team A: 1
Enter the number for Team B: 2

--- Matchup Prediction Results ---
Team A: ATL FaZe
Team B: Optic Texas
Predicted Winner: Team A

Category Win Probabilities:
  Overall KD: 65.32% chance Team A wins
  Search Destroy KD: 65.32% chance Team A wins
  Control KD: 65.32% chance Team A wins
  Hardpoint KD: 65.32% chance Team A wins

Would you like to compare another matchup? (yes/no): no
Thank you for using the prediction tool. Goodbye!
```
---
# Training the Model
If you want to retrain the model:

Use the real_game_data.csv dataset or your own matchups data.
Train the model using a Random Forest or Logistic Regression:
python
Copy code
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

### Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

### Save the model
dump(model, 'model_combined.pkl')
---


Here’s the README in Markdown format:

markdown
Copy code
# **Team Matchup Prediction Tool**

## **Overview**
The **Team Matchup Prediction Tool** predicts the outcome of Call of Duty League matchups based on team stats, such as **Overall KD**, **Search Destroy KD**, **Control KD**, and **Hardpoint KD**. This interactive tool lets users input two teams, compare their performance metrics, and calculate the likelihood of each team winning.

## **Features**
- Predicts the winner of a matchup based on trained machine learning models.
- Provides **win probabilities** for each KD category:
  - Overall KD
  - Search Destroy KD
  - Control KD
  - Hardpoint KD
- Interactive interface for easy team selection.
- Supports multiple comparisons in a single session.

---

## **Requirements**
To run the project, you need:
- Python 3.7 or higher
- The following Python libraries:
  - `pandas`
  - `numpy`
  - `joblib`
  - `scikit-learn`

---

## **Setup Instructions**

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd team-matchup-prediction-tool
Install Dependencies: Install the required libraries using pip:

bash
Copy code
pip install pandas numpy joblib scikit-learn
Prepare the Files:

Place the following files in the project directory:
Cleaned_Team_Data.csv: Contains the cleaned team stats.
model_combined.pkl: The trained machine learning model.
How to Use
Run the Tool: Execute the Python script in your terminal:

bash
Copy code
python team_matchup_tool.py
Interactive Menu:

The tool displays a numbered list of available teams.
Input the numbers corresponding to Team A and Team B to compare them.
Output:

The predicted winner.
Win probabilities for each KD category.
Repeat or Exit:

You can compare additional matchups or exit by typing no.
Example Usage
```
bash
Copy code
Welcome to the Team Matchup Prediction Tool!

Available Teams:
1. ATL FaZe
2. Optic Texas
3. LA Thieves
4. VAN Surge

Enter the number for Team A: 1
Enter the number for Team B: 2

--- Matchup Prediction Results ---
Team A: ATL FaZe
Team B: Optic Texas
Predicted Winner: Team A

Category Win Probabilities:
  Overall KD: 65.32% chance Team A wins
  Search Destroy KD: 65.32% chance Team A wins
  Control KD: 65.32% chance Team A wins
  Hardpoint KD: 65.32% chance Team A wins

Would you like to compare another matchup? (yes/no): no
Thank you for using the prediction tool. Goodbye!
Files in the Project
team_matchup_tool.py: The main script for running the interactive prediction tool.
Cleaned_Team_Data.csv: Contains team stats used for predictions.
model_combined.pkl: The pre-trained machine learning model.
Training the Model
If you want to retrain the model:

Use the real_game_data.csv dataset or your own matchups data.
Train the model using a Random Forest or Logistic Regression:
python
Copy code
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
```

## Train the model
```
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```

## Save the model
```
dump(model, 'model_combined.pkl')
```
## Results
![output](https://github.com/user-attachments/assets/2de477d2-d19a-4a48-8065-9408896d1c42)
![output 2](https://github.com/user-attachments/assets/831093c2-e1c5-4a47-896c-ae159c2a4439)
![features](https://github.com/user-attachments/assets/0d60279f-ddb5-47a2-9542-3e142edc2468)

# Future Enhancements
Deploy the tool as a web app using Flask or Streamlit.
Add graphical visualizations for win probabilities.
Include match-specific factors like maps and player performance.

## **References**

This project relies on data and insights gathered from the following sources:

1. **Call of Duty Overview**:  
   General information about the Call of Duty franchise, including its history and gameplay details.  
   [Call of Duty - Wikipedia](https://en.wikipedia.org/wiki/Call_of_Duty)

2. **CDL Pick'ems**:  
   Official CDL Pick'ems competition for predicting match winners in the 2025 season.  
   [CDL Pick'ems - Major 1 Predictions](https://pickem.callofdutyleague.com/predictions/2025/major1)

3. **Call of Duty League Stats**:  
   Official stats for the CDL season, including team and player performance metrics.  
   [CDL Stats - Official Site](https://www.callofdutyleague.com/en-us/stats?tab=entire-season)

4. **COD League Player Stats**:  
   Comprehensive player statistics for detailed performance analysis.  
   [COD League Stats - Player Stats](https://www.codleaguestats.com/player-stats)
