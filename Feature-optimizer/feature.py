import numpy as np
import pandas as pd
import pygad
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def run_feature(df, target_column):

    df = df.copy()

    # 🔹 Encode categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    # 🔹 Split features and target
    X = df.drop(columns=[target_column]).values
    y = df[target_column].values

    num_features = X.shape[1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # 🔹 Fitness function
    def fitness_func(ga, solution, solution_idx):
        selected_indices = np.where(solution == 1)[0]
        # avoid empty feature set
        if len(selected_indices) == 0:
            return 0

        X_train_subset = X_train[:, selected_indices]
        X_test_subset = X_test[:, selected_indices]

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train_subset, y_train)

        predictions = model.predict(X_test_subset)
        accuracy = accuracy_score(y_test, predictions)

        return accuracy

    ga_instance = pygad.GA(
        num_generations=30,              
        num_parents_mating=5,
        fitness_func=fitness_func,
        sol_per_pop=12,
        num_genes=num_features,
        gene_type=int,
        gene_space=[0, 1],
        mutation_percent_genes=15
    )

    ga_instance.run()

    solution, solution_fitness, _ = ga_instance.best_solution()

    selected_features = np.where(solution == 1)[0]

    return selected_features, solution_fitness
