create schema analitics;

create or replace view analitics.event_limits as
select e.event_id as event_id, count(ue.user_id) as entries, e.max_participant
from zlapka.event as e
join zlapka.user_event as ue
on e.event_id = ue.event_id
group by e.event_id;

create or replace function analitics.distance(location1 int[], location2 int[])
    returns integer
    as $$
        begin
            return sqrt((location1[1] - location2[1])^2+(location1[2]-location2[2])^2);
        end;
    $$ language plpgsql;

create or replace function analitics.distance(location1 int[], location2 int[])
    returns integer
    as $$
        begin
            return sqrt((location1[1] - location2[1])^2+(location1[2]-location2[2])^2);
        end;
    $$ language plpgsql;

create or replace view analitics.surrounding_locations as
select c.city_id, c.name as closes_city, l.location_id, l.name as venue,
       analitics.distance(l.geo_tag,  c.geotag)
        as distance_to_city
from zlapka.location as l
join zlapka.city as c
on analitics.distance(l.geo_tag,  c.geotag)<10
order by distance_to_city ASC;
