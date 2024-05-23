-- a script that lists all cities contained in the database hbtn_0d_usa.
SELECT c.id,state_id,c.name,s.name FROM cities c join states s ON c.state_id=s.id;
