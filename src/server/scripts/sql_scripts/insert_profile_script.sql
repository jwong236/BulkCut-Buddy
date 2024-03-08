USE bulkcut_buddy_database;
DROP TABLE IF EXISTS profile;
CREATE TABLE profile (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    height INT,
    age INT,
    sex TINYINT CHECK (sex IN (0, 1))  -- 0 for woman, 1 for man
);