CREATE OR REPLACE FUNCTION search_contacts_pattern(pattern TEXT)
RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR) AS $$
BEGIN 
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || pattern || '%'
        OR p.phone LIKE '%' || pattern || '%';
END;
$$LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$LANGUAGE plpgsql;