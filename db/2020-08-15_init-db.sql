CREATE TABLE persons (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    company_name VARCHAR NOT NULL
);


CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL,
    coordinate GEOMETRY NOT NULL,
    creation_time TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (person_id) REFERENCES person(id)
);
CREATE INDEX coordinate_idx ON locations (coordinate);
CREATE INDEX creation_time_idx ON locations (creation_time);
