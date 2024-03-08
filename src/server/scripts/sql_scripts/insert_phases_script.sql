USE bulkcut_buddy_database;
DROP TABLE IF EXISTS phases;
CREATE TABLE phases (
    phase_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    phase_type TINYINT CHECK (phase_type IN (0, 1)),  -- 0 for cut, 1 for bulk
    start_date DATE,
    target_weight INT,
    target_date DATE,
    FOREIGN KEY (account_id) REFERENCES profile(account_id)
);