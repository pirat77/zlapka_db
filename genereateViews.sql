create or replace view analitics.event_limits as
select e.event_id as event_id, count(ue.user_id) as entries, e.max_participant
from zlapka.event as e
join zlapka.user_event as ue
on e.event_id = ue.event_id
group by e.event_id;