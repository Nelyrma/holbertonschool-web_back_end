-- Create a trigger that decreases the quantity of an item
-- After adding an new order

DELIMITER //

CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_id = NEW.item_id;
END //

DELIMITER ;
