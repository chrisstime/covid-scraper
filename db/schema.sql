DROP TABLE IF EXISTS cases_by_loc;
DROP TABLE IF EXISTS cases_by_age;
DROP TABLE IF EXISTS cases_by_infection_source;
CREATE TABLE cases_by_loc (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  notification_date DATETIME NOT NULL,
  postcode INTEGER,
  local_health_district_code TEXT,
  local_health_district TEXT,
  local_gov_area_code INTEGER,
  local_gov_area TEXT
);
CREATE TABLE cases_by_age (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  notification_date DATETIME NOT NULL,
  age_group TEXT
);
CREATE TABLE cases_by_infection_source (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  notification_date DATETIME,
  source_of_infection TEXT
);