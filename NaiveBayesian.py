import pandas as pd

# Load Excel data directly
df = pd.read_excel(r'C:\Users\Dell\OneDrive\Desktop\data.xlsx')
data = df.to_dict(orient='records')

# Calculate prior probability
def calculate_prior(data, target_value):
    count = sum(1 for item in data if item['play'].lower() == target_value.lower())
    return count / len(data)

# Calculate likelihood with Laplace smoothing
def calculate_likelihood(data, feature_value, feature_name, target_value):
    count_feature_and_target = sum(
        1 for item in data 
        if str(item[feature_name]).lower() == feature_value.lower() and item['play'].lower() == target_value.lower()
    )
    count_target = sum(1 for item in data if item['play'].lower() == target_value.lower())
    unique_vals = len(set(item[feature_name] for item in data))
    return (count_feature_and_target + 1) / (count_target + unique_vals)

# Prediction function
def predict(data, input_data):
    prior_yes = calculate_prior(data, 'yes')
    prior_no = calculate_prior(data, 'no')

    prob_yes = prior_yes
    prob_no = prior_no

    for feature, value in input_data.items():
        prob_yes *= calculate_likelihood(data, value, feature, 'yes')
        prob_no *= calculate_likelihood(data, value, feature, 'no')

    return 'yes' if prob_yes > prob_no else 'no'

# User input
print("Enter weather conditions:")
outlook = input("Outlook (sunny / overcast / rainy): ").strip().lower()
temperature = input("Temperature (hot / mild / cool): ").strip().lower()
humidity = input("Humidity (high / normal): ").strip().lower()
wind = input("Wind (weak / strong): ").strip().lower()

input_data = {
    'outlook': outlook,
    'temperature': temperature,
    'humidity': humidity,
    'wind': wind
}

prediction = predict(data, input_data)
print(f"Prediction for {input_data}: Will play? → {prediction}")


# data = [
# ['Yes', 'No', 'Yes'],
# ['No', 'Yes', 'Yes'],
# ['Yes', 'Yes', 'Yes'],
# ['No', 'No', 'No'],
# ['Yes', 'No', 'Yes'],
# ['No', 'No', 'Yes'],
# ['Yes', 'No', 'Yes'],
# ['Yes', 'No', 'No'],
# ['No', 'Yes', 'Yes'],
# ['No', 'Yes', 'No'],
# ]
# from collections import defaultdict
# # Count classes
# yes = sum(1 for row in data if row[2] == 'Yes')
# no = len(data) - yes
# total = yes + no
# # Feature counts
# counts = {
# 'Covid': {'Yes': defaultdict(int), 'No': defaultdict(int)},
# 'Flu': {'Yes': defaultdict(int), 'No': defaultdict(int)}
# }
# for row in data:
# covid, flu, fever = row
# counts['Covid'][fever][covid] += 1
# counts['Flu'][fever][flu] += 1
# def predict(covid, flu):
# # Prior probabilities
# p_yes = yes / total
# p_no = no / total
# # Likelihoods without smoothing
# try:
# covid_yes = counts['Covid']['Yes'][covid] / yes
# flu_yes = counts['Flu']['Yes'][flu] / yes
# p_yes *= covid_yes * flu_yes
# except ZeroDivisionError:
# p_yes = 0
# try:
# covid_no = counts['Covid']['No'][covid] / no
# flu_no = counts['Flu']['No'][flu] / no
# p_no *= covid_no * flu_no
# except ZeroDivisionError:
# p_no = 0
# print(f"\nInput: Covid={covid}, Flu={flu}")
# print(f"P(Fever=Yes): {p_yes:.5f}")
# print(f"P(Fever=No): {p_no:.5f}")
# return 'Yes' if p_yes > p_no else 'No'
# # Tests
# print("Predicted Fever:", predict('Yes', 'Yes')) # Expected: Yes
