-- Create a stored procedure that computes and store the average score for a student
-- An average score can be a decimal
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- compute the average score
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;

    -- update the average_score row in the table users
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END //

DELIMITER ;