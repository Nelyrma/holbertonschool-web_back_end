-- script that creates an index idx_name_first
-- the index is created on the table names and the first letter of name
CREATE INDEX idx_name_first ON names (name(1));