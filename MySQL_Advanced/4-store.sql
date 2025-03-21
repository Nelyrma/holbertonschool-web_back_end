-- Script that creates a trigger that decrease
-- the quantity of an item after adding a new order
-- Create the trigger
DELIMITER //

CREATE TRIGGER decrease AFTER INSERT
ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;//

DELIMITER ;