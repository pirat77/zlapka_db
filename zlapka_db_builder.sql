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
            primary key
        constraint advertisement_fk
            references organization
            on update cascade,
    information      varchar not null,
    target           varchar not null,
    picture          bytea,
    launch           date    not null,
    duration         integer
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
    event_id        serial  not null
        constraint event_pk
            primary key
        constraint event_event_category_category_id_fk
            references event_category
            on update cascade
        constraint event_location_location_id_fk
            references location
            on update cascade
        constraint event_organization_organization_id_fk
            references organization
            on update cascade,
    name            varchar not null,
    description     varchar not null,
    max_participant integer,
    date            date    not null,
    duration        integer not null,
    public          boolean not null
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

create table "user"
(
    user_id     serial  not null
        constraint user_pk
            primary key
        constraint user_location_location_id_fk
            references location
            on update cascade
        constraint user_user_category_category_id_fk
            references user_category
            on update cascade,
    first_name  varchar not null,
    last_name   varchar not null,
    description varchar,
    photo       bytea,
    email       varchar not null
);

alter table "user"
    owner to postgres;

create unique index user_user_id_uindex
    on "user" (user_id);

create table user_preference
(
    id serial not null
        constraint user_preference_pk
            primary key
        constraint user_preference_preference_preference_id_fk
            references preference
            on update cascade
        constraint user_preference_user_user_id_fk
            references "user"
            on update cascade
);

alter table user_preference
    owner to postgres;

create unique index user_preference_id_uindex
    on user_preference (id);

create table user_group
(
    id serial not null
        constraint user_group_pk
            primary key
        constraint user_group_group_group_id_fk
            references "group"
            on update cascade
        constraint user_group_user_user_id_fk
            references "user"
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
            primary key
        constraint message_group_group_id_fk
            references "group"
            on update cascade
        constraint message_user_user_id_fk
            references "user"
            on update cascade,
    title      varchar,
    content    varchar not null,
    photo      bytea
);

alter table message
    owner to postgres;

create unique index message_message_id_uindex
    on message (message_id);

create table user_relations
(
    id     serial  not null
        constraint user_relations_pk
            primary key
        constraint user_relations_user_user_id_fk
            references "user"
            on update cascade
        constraint user_relations_user_user_id_fk_2
            references "user"
            on update cascade,
    status varchar not null
);

alter table user_relations
    owner to postgres;

create unique index user_relations_id_uindex
    on user_relations (id);

create table voucher
(
    voucher_id serial  not null
        constraint voucher_pk
            primary key
        constraint voucher_user_user_id_fk
            references "user"
            on update cascade,
    type       varchar not null,
    value      integer
);

alter table voucher
    owner to postgres;

create unique index voucher_voucher_id_uindex
    on voucher (voucher_id);

create table user_organization
(
    id   serial not null
        constraint user_organization_pk
            primary key
        constraint user_organization_organization_organization_id_fk
            references organization
            on update cascade
        constraint user_organization_user_user_id_fk
            references "user"
            on update cascade,
    role varchar
);

alter table user_organization
    owner to postgres;

create unique index user_organization_id_uindex
    on user_organization (id);

create table user_event
(
    id serial not null
        constraint user_event_pk
            primary key
        constraint user_event_event_event_id_fk
            references event
            on update cascade
        constraint user_event_user_user_id_fk
            references "user"
            on update cascade
);

alter table user_event
    owner to postgres;

create unique index user_event_id_uindex
    on user_event (id);

create table ticket
(
    ticket_id serial not null
        constraint ticket_pk
            primary key
        constraint ticket_event_event_id_fk
            references event
            on update cascade
        constraint ticket_user_event_id_fk
            references user_event
            on update cascade,
    price     integer
);

alter table ticket
    owner to postgres;

create unique index ticket_ticket_id_uindex
    on ticket (ticket_id);


