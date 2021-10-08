#!/bin/sh

set -e

# Perform all actions as $POSTGRES_USER
export PGUSER="$POSTGRES_USER"

echo "Creating table"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<- 'EOSQL'
CREATE TABLE persons (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    company_name VARCHAR NOT NULL
);
EOSQL

echo "Populating table"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<- 'EOSQL'
INSERT INTO persons (id, first_name, last_name, company_name) VALUES (5, 'Taco', 'Fargo', 'Alpha Omega Upholstery');
INSERT INTO persons (id, first_name, last_name, company_name) VALUES (6, 'Frank', 'Shader', 'USDA');
INSERT INTO persons (id, first_name, last_name, company_name) VALUES (1, 'Pam', 'Trexler', 'Hampton, Hampton and McQuill');
INSERT INTO persons (id, first_name, last_name, company_name) VALUES (8, 'Paul', 'Badman', 'Paul Badman & Associates');
INSERT INTO persons (id, first_name, last_name, company_name) VALUES (9, 'Otto', 'Spring', 'The Chicken Sisters Restaurant');
EOSQL
