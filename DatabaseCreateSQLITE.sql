



-- klimapi.main.locations definition

-- Drop table

-
- DROP TABLE klimapi.main.locations;

CREATE TABLE locations (
	id INTEGER NOT NULL,
	name VARCHAR NOT NULL,
	info VARCHAR,
	CONSTRAINT LOCATIONS_PK PRIMARY KEY (id)
);


-- klimapi.main.measurements definition

-- Drop table

-- DROP TABLE klimapi.main.measurements;

CREATE TABLE measurements (
	id integer PRIMARY KEY ,
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

CREATE TABLE sensors (
	id INTEGER NOT NULL,
	name VARCHAR,
	info VARCHAR,
	location_id INTEGER,
	CONSTRAINT SENSORS_PK PRIMARY KEY (id)
);