# Passcheck: Password Generator & Strength Checker

#### Video Demo:  **[Link]()**

#### Description:

This project, **Passcheck**, is a command-line utility built in Python designed to enhance digital security by providing both a robust password generator and a comprehensive password strength checker.

**Key Features:**

* **Password Generation (`gen` mode):**
    * Generates strong, random passwords of a specified length.
    * Allows users to select which character types to include (uppercase, lowercase, digits, special characters) to customize complexity.
    * Ensures that generated passwords meet the selected criteria, making them suitable for various security requirements.

* **Password Strength Checking (`check` mode):**
    * Evaluates the strength of user-provided passwords against a set of predefined criteria.
    * Classifies passwords into "Low," "Medium," or "High" strength categories.
    * Provides a numerical score (out of 7) for a quick strength overview.
    * Offers actionable feedback and suggestions to the user on how to improve their password's security (e.g., "Add an uppercase letter," "Make it longer").
    * Includes a crucial check against a list of common and easily guessable words, flagging such passwords as "Low Strength" immediately.

**How to Use:**

1.  **Save the files:** Ensure `project.py` and `test_project.py` are in the same directory.
2.  **Run the program:**
    ```bash
    python project.py
    ```
3.  **Choose an option:**
    * Enter `gen` to generate a new password. You'll be prompted for a desired length.
    * Enter `check` to check the strength of a password you provide.
    * Enter `quit` to exit the program.


