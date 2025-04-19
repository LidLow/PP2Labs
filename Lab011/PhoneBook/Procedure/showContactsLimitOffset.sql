CREATE OR REPLACE FUNCTION showContactsLimitOffset(
    p_limit INT, 
    p_offset INT
)
RETURNS TABLE(first_name VARCHAR(50), last_name VARCHAR(50), phone_number VARCHAR(20)) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT c.first_name, c.last_name, c.phone_number
    FROM contacts c
    ORDER BY c.first_name ASC
    LIMIT p_limit OFFSET p_offset;
END;
$$;