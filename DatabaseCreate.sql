



-- klimapi.main.locations definition

-- Drop table

-
- DROP TABLE klimapi.main.locations;

CREATE TABLE klimapi.main.locations (
	id INTEGER NOT NULL,
	name VARCHAR NOT NULL,
	info VARCHAR,
	CONSTRAINT LOCATIONS_PK PRIMARY KEY (id)
);


CREATE SEQUENCE klimapi.main.seq_measurement_id START 1;
-- klimapi.main.measurements definition

-- Drop table

-- DROP TABLE klimapi.main.measurements;

CREATE TABLE klimapi.main.measurements (
	id integer PRIMARY KEY DEFAULT NEXTVAL('seq_measurement_id'),
	"timestamp" TIMESTAMP NOT NULL,
	sensor_id INTEGER NOT NULL,
	temperature_celsius FLOAT,
	humidity FLOAT,
	location_id INTEGER--,
	--CONSTRAINT MEASUREMENTS_PK PRIMARY KEY (id)
);

-- klimapi.main.sensors definition

-- Drop table

-- DROP TABLE klimapi.main.sensors;

CREATE TABLE klimapi.main.sensors (
	id INTEGER NOT NULL,
	name VARCHAR,
	info VARCHAR,
	location_id INTEGER,
	CONSTRAINT SENSORS_PK PRIMARY KEY (id)
);