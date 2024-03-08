USE bulkcut_buddy_database;

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE dailyentries;
TRUNCATE TABLE monthlyprojections;
TRUNCATE TABLE monthlytrainingdata;
TRUNCATE TABLE phases;
TRUNCATE TABLE profile;
TRUNCATE TABLE weeklyprojections;
TRUNCATE TABLE weeklytrainingdata;

SET FOREIGN_KEY_CHECKS = 1;
