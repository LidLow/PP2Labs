CREATE OR REPLACE PROCEDURE updateOrInsert(p_first_name TEXT, p_last_name TEXT, p_phone_number TEXT)
LANGUAGE plpgsql

AS $$
BEGIN
    UPDATE contacts
    SET phone_number = p_phone_number
    WHERE first_name = p_first_name
    OR last_name = p_last_name;

    IF NOT FOUND THEN
        INSERT INTO contacts(first_name, last_name, phone_number)
        VALUES (p_first_name, p_last_name, p_phone_number);
    END IF;
END;
$$;