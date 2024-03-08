USE bulkcut_buddy_database;
DROP TABLE IF EXISTS weeklyprojections;
CREATE TABLE weeklyprojections (
    weekly_projection_id INT AUTO_INCREMENT PRIMARY KEY,
    daily_entry_id INT NOT NULL,
    projected_weight INT,
    week_count INT,
    FOREIGN KEY (daily_entry_id) REFERENCES dailyentries(daily_entry_id)
);