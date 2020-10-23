create schema analitics;

create or replace view analitics.event_limits as
select e.event_id as event_id, count(ue.user_id) as entries, e.max_participant
from zlapka.event as e
left join zlapka.user_event as ue
on e.event_id = ue.event_id
group by e.event_id;

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

create or replace function analitics.local_events(checkedCity int)
    returns table (
                    distance int,
                    event_id int,
                    event_name varchar,
                    free_slots int
                  )
    as  $$
        begin
            return query (
                    select sl.distance_to_city as distance, e.event_id, e.name as event_name, (el.max_participant-el.entries)::int as free_slots
                    from analitics.surrounding_locations as sl
                    join zlapka.event as e
                        on e.event_location_id=sl.location_id
                    join analitics.event_limits as el
                        on e.event_id=el.event_id
                    where sl.city_id=checkedCity and (el.max_participant-el.entries)>0
                    order by distance asc
                    );
        end;
    $$ language plpgsql;
    