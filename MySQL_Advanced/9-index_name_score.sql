-- Create an index on the table names
CREATE idx_name_first_score ON names (name(1), score);