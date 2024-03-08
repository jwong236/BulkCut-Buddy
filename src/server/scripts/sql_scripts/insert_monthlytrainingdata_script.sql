USE bulkcut_buddy_database;
DROP TABLE IF EXISTS monthlytrainingdata;
CREATE TABLE monthlytrainingdata (
    training_id INT AUTO_INCREMENT PRIMARY KEY,
    height INT,
    age INT,
    sex INT CHECK (sex IN (0, 1)),  -- 0 for woman, 1 for man
    phase_type INT CHECK (phase_type IN (0, 1)),  -- 0 for cut, 1 for bulk
    initial_weight INT,
    active_calories_burned INT,
    resting_calories_burned INT,
    steps INT,
    hours_of_sleep FLOAT,
    weight_change_rate FLOAT,
    daily_calorie_intake INT,
    daily_protein_intake INT,
    month_count INT,
    future_weight INT
);