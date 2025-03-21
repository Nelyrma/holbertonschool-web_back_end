-- Create  a stored procedure AddBonus
-- the procedure adds a new correction for a student
-- it takes 3 inputs
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT,

    -- check if the project already exists
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- create the project if it doesn't exist
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- add a new correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;//

DELIMITER ;