create table location
(
    location_id serial  not null
        constraint location_pk
            primary key,
    name        varchar not null,
    geo_tag     integer[]
);

alter table location
    owner to postgres;

create unique index location_location_id_uindex
    on location (location_id);

create table organization
(
    organization_id serial  not null
        constraint organization_pk
            primary key,
    name            varchar not null
);

alter table organization
    owner to postgres;

create unique index organization_organization_id_uindex
    on organization (organization_id);

create table advertisement
(
    advertisement_id serial  not null
        constraint advertisement_pk
            primary key,
    information      varchar not null,
    target           varchar not null,
    picture          varchar,
    launch           date    not null,
    duration         integer,
    organization_id  integer not null
        constraint advertisement_fk
            references organization
            on update cascade
);

alter table advertisement
    owner to postgres;

create unique index advertisement_advertisement_id_uindex
    on advertisement (advertisement_id);

create table event_category
(
    category_id serial  not null
        constraint event_category_pk
            primary key,
    name        varchar not null
);

alter table event_category
    owner to postgres;

create table event
(
    event_id              serial  not null
        constraint event_pk
            primary key,
    name                  varchar not null,
    description           varchar not null,
    max_participant       integer,
    date                  date    not null,
    duration              integer not null,
    public                boolean not null,
    event_category_id     integer not null
        constraint event_event_category_category_id_fk
            references event_category
            on update cascade,
    event_location_id     integer
        constraint event_location_location_id_fk
            references location
            on update cascade,
    event_organization_id integer
        constraint event_organization_organization_id_fk
            references organization
            on update cascade
);

alter table event
    owner to postgres;

create unique index event_event_id_uindex
    on event (event_id);

create unique index event_category_category_id_uindex
    on event_category (category_id);

create table user_category
(
    category_id serial  not null
        constraint user_category_pk
            primary key,
    name        varchar not null
);

alter table user_category
    owner to postgres;

create unique index user_category_category_id_uindex
    on user_category (category_id);

create table "group"
(
    group_id serial  not null
        constraint group_pk
            primary key,
    name     varchar not null,
    public   boolean
);

alter table "group"
    owner to postgres;

create unique index group_group_id_uindex
    on "group" (group_id);

create table preference
(
    preference_id serial  not null
        constraint preference_pk
            primary key,
    name          varchar not null
);

alter table preference
    owner to postgres;

create unique index preference_preference_id_uindex
    on preference (preference_id);

create table users
(
    user_id          serial  not null
        constraint user_pk
            primary key,
    first_name       varchar not null,
    last_name        varchar not null,
    description      varchar,
    photo            varchar,
    email            varchar not null,
    user_location_id integer
        constraint user_location_location_id
            references location
            on update cascade,
    user_category_id integer not null
        constraint user_user_category_category_id_fk
            references user_category
            on update cascade
);

alter table users
    owner to postgres;

create unique index user_user_id_uindex
    on users (user_id);

create table user_preference
(
    id            serial  not null
        constraint user_preference_pk
            primary key,
    preference_id integer not null
        constraint user_preference_preference_preference_id_fk
            references preference
            on update cascade,
    user_id       integer not null
        constraint user_preference_user_user_id_fk
            references users
            on update cascade
);

alter table user_preference
    owner to postgres;

create unique index user_preference_id_uindex
    on user_preference (id);

create table user_group
(
    id       serial  not null
        constraint user_group_pk
            primary key,
    group_id integer not null
        constraint user_group_group_group_id_fk
            references "group"
            on update cascade,
    user_id  integer not null
        constraint user_group_user_user_id_fk
            references users
            on update cascade
);

alter table user_group
    owner to postgres;

create unique index user_group_id_uindex
    on user_group (id);

create table message
(
    message_id serial  not null
        constraint message_pk
            primary key,
    title      varchar,
    content    varchar not null,
    photo      varchar,
    group_id   integer not null
        constraint message_group_group_id_fk
            references "group"
            on update cascade,
    user_id    integer not null
        constraint message_user_user_id_fk
            references users
            on update cascade
);

alter table message
    owner to postgres;

create unique index message_message_id_uindex
    on message (message_id);

create type u_relation as enum (
    'USER1_BLOCKED_USER2',
    'USER2_BLOCKED_USER1',
    'USER1_INVITED_USER2',
    'USER2_INVITED_USER1',
    'USER1_ACCEPTED_USER2',
    'USER2_ACCEPTED_USER1');

create table user_relations
(
    id        serial  not null
        constraint user_relations_pk
            primary key,
    status    u_relation not null,
    user_id_1 integer not null
        constraint user_relations_user_user_id_fk
            references users
            on update cascade,
    user_id_2 integer not null
        constraint user_relations_user_user_id_fk_2
            references users
            on update cascade
);

alter table user_relations
    owner to postgres;

create unique index user_relations_id_uindex
    on user_relations (id);

create index uid1 ON user_relations (user_id_1);
create index uid2 ON user_relations (user_id_2);

CREATE OR REPLACE FUNCTION check_unique_relation(IN id1 INTEGER, IN id2 INTEGER)
RETURNS INTEGER AS $body$
DECLARE retval INTEGER DEFAULT 0;
BEGIN
SELECT COUNT(*) INTO retval FROM (
  SELECT * FROM user_relations WHERE user_id_1 = id1 AND user_id_2 = id2
  UNION ALL
  SELECT * FROM user_relations WHERE user_id_1 = id2 AND user_id_2 = id1
) AS pairs;
RETURN retval;
END
$body$
LANGUAGE 'plpgsql';

ALTER TABLE user_relations ADD CONSTRAINT unique_pair
    CHECK (check_unique_relation(user_id_1, user_id_2) < 1);

alter table user_relations add constraint check (user_id_1 <> user_id_2);

create table voucher
(
    voucher_id serial  not null
        constraint voucher_pk
            primary key,
    type       varchar not null,
    value      integer,
    user_id    integer not null
        constraint voucher_user_user_id_fk
            references users
            on update cascade
);

alter table voucher
    owner to postgres;

create unique index voucher_voucher_id_uindex
    on voucher (voucher_id);

create table user_organization
(
    id              serial  not null
        constraint user_organization_pk
            primary key,
    role            varchar,
    organization_id integer not null
        constraint user_organization_organization_organization_id_fk
            references organization
            on update cascade,
    user_id         integer not null
        constraint user_organization_user_user_id_fk
            references users
            on update cascade
);

alter table user_organization
    owner to postgres;

create unique index user_organization_id_uindex
    on user_organization (id);

create table user_event
(
    id       serial  not null
        constraint user_event_pk
            primary key
        constraint user_event_event_event_id_fk
            references event
            on update cascade
        constraint user_event_user_user_id_fk
            references users
            on update cascade,
    event_id integer not null,
    user_id  integer not null
);

alter table user_event
    owner to postgres;

create unique index user_event_id_uindex
    on user_event (id);

create table ticket
(
    ticket_id     serial  not null
        constraint ticket_pk
            primary key,
    price         integer,
    event_id      integer not null
        constraint ticket_event_event_id_fk
            references event
            on update cascade,
    user_event_id integer
        constraint ticket_user_event_id_fk
            references user_event
            on update cascade
);

alter table ticket
    owner to postgres;

create unique index ticket_ticket_id_uindex
    on ticket (ticket_id);

