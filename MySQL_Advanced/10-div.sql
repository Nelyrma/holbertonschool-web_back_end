-- create a function SafeDiv that divides the first by the second number
-- return 0 if the second number is equal to 0
DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN (a / b);
    END IF;
END;//

DELIMITER ;