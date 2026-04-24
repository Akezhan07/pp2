CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    INSERT INTO phonebook (name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (phone) DO UPDATE 
    SET name = EXCLUDED.name; 
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_many_contacts(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]+$' AND length(phones[i]) BETWEEN 7 AND 15 THEN
            INSERT INTO phonebook (name, phone) 
            VALUES (names[i], phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            RAISE NOTICE 'Invalid data: % - %', names[i], phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_contact_proc(identifier VARCHAR)
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE name = identifier OR phone = identifier;
END;
$$ LANGUAGE plpgsql;