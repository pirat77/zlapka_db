create or replace function zlapka.hash_relation(id1 integer, id2 integer)
returns varchar as
$$
begin
    if id1 < id2 then
        return concat(id2, '#', id1);
    end if;
    return concat(id1, '#', id2);
end;
$$ language plpgsql immutable;

CREATE OR REPLACE FUNCTION zlapka.check_unique_relation(id1 INTEGER, id2 INTEGER)
RETURNS INTEGER AS $body$
DECLARE
    retval INTEGER DEFAULT 0;
    searchedHash VARCHAR;
BEGIN
    if id1 is null OR id2 IS null then
        raise exception 'nulllll!!!!!!!!!!!!!!!!!!!!!!!!!111';
    end if;
    searchedHash := zlapka.hash_relation(id1, id2);
    SELECT COUNT(*) INTO retval FROM (
    SELECT * FROM zlapka.user_relations
    WHERE (SELECT zlapka.hash_relation(user_id_1, user_id_2)) LIKE searchedHash
    LIMIT 1
    ) AS pairs;
    RETURN retval;
END
$body$
LANGUAGE 'plpgsql';

create index relation_index ON zlapka.user_relations (zlapka.hash_relation(user_id_1, user_id_2));

alter table zlapka.user_relations add constraint
    different_values check (user_id_1 <> user_id_2);

ALTER TABLE zlapka.user_relations ADD CONSTRAINT unique_pair
    CHECK (zlapka.check_unique_relation(user_id_1, user_id_2) < 1);



