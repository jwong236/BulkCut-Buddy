USE bulkcut_buddy_database;
DROP TABLE IF EXISTS dailyentries;
CREATE TABLE dailyentries (
    daily_entry_id INT AUTO_INCREMENT PRIMARY KEY,
    phase_id INT NOT NULL,
    date DATE,
    current_weight INT,
    active_calories_burned INT,
    resting_calories_burned INT,
    steps INT,
    hours_of_sleep FLOAT,
    daily_calorie_intake INT,
    daily_protein_intake INT,
    FOREIGN KEY (phase_id) REFERENCES phases(phase_id)
);