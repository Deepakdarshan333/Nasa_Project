CREATE DATABASE nasa_neo;
USE nasa_neo;

CREATE TABLE neo_asteroids (
    id VARCHAR(50),
    neo_reference_id VARCHAR(50),
    name VARCHAR(100),
    absolute_magnitude_h FLOAT,
    estimated_diameter_min_km FLOAT,
    estimated_diameter_max_km FLOAT,
    is_potentially_hazardous_asteroid BOOLEAN,
    close_approach_date DATE,
    relative_velocity_kmph FLOAT,
    astronomical FLOAT,
    miss_distance_km FLOAT,
    miss_distance_lunar FLOAT,
    orbiting_body VARCHAR(50)
);

USE nasa_neo;
SELECT COUNT(*) FROM neo_asteroids;

SELECT COUNT(*) AS total_asteroids FROM neo_asteroids;

SELECT name, close_approach_date, relative_velocity_kmph, miss_distance_km
FROM neo_asteroids
WHERE is_potentially_hazardous_asteroid = TRUE
ORDER BY close_approach_date ASC;

SELECT close_approach_date, COUNT(*) AS asteroid_count
FROM neo_asteroids
GROUP BY close_approach_date
ORDER BY close_approach_date;

SELECT name, miss_distance_lunar, close_approach_date
FROM neo_asteroids
WHERE miss_distance_lunar < 1
ORDER BY miss_distance_lunar ASC;

SELECT name, estimated_diameter_max_km, is_potentially_hazardous_asteroid
FROM neo_asteroids
WHERE estimated_diameter_max_km > 1
  AND is_potentially_hazardous_asteroid = TRUE
ORDER BY estimated_diameter_max_km DESC;

SELECT orbiting_body, COUNT(*) AS total_asteroids
FROM neo_asteroids
GROUP BY orbiting_body;
