CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL,
    coordinate GEOMETRY NOT NULL,
    creation_time TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX coordinate_idx ON locations (coordinate);
CREATE INDEX creation_time_idx ON locations (creation_time);