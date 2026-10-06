CREATE DATABASE IF NOT EXISTS RoadFlow;
USE RoadFlow;

CREATE TABLE IF NOT EXISTS camera (	
    camera_id INT,
    trafikverket_id VARCHAR(50) UNIQUE NOT NULL,
    camera_name VARCHAR(60),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    
    PRIMARY KEY(camera_id)
);

CREATE TABLE IF NOT EXISTS data_gap (
	gap_id INT AUTO_INCREMENT PRIMARY KEY,
    camera_id INT NOT NULL,
    gap_start DATETIME NOT NULL,
    gap_end DATETIME,
    reason VARCHAR(50),
    
	FOREIGN KEY (camera_id) REFERENCES camera(camera_id)
);

CREATE TABLE IF NOT EXISTS photo (
	photo_id INT AUTO_INCREMENT PRIMARY KEY,
    camera_id INT NOT NULL,
    photo_time DATETIME NOT NULL,
    original_filepath VARCHAR(255),
	
    FOREIGN KEY (camera_id) REFERENCES camera(camera_id)
);

CREATE TABLE IF NOT EXISTS analysis (
	analysis_id INT AUTO_INCREMENT PRIMARY KEY,
    photo_id INT NOT NULL,
	detected_vehicles INT,
    analyzed_filepath VARCHAR(255),
	
	FOREIGN KEY (photo_id) REFERENCES photo(photo_id)
);


CREATE TABLE IF NOT EXISTS detection(
	detection_id INT AUTO_INCREMENT PRIMARY KEY,
    analysis_id INT NOT NULL,
	vehicle_class VARCHAR(50),
    detection_confidence DECIMAL(5,4),
    bounding_x1 DECIMAL(10,2),
    bounding_y1 DECIMAL(10,2),
    bounding_x2 DECIMAL(10,2),
	bounding_y2 DECIMAL(10,2),

	FOREIGN KEY (analysis_id) REFERENCES analysis(analysis_id)
);