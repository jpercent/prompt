begin;

create schema if not exists conversations;

create table if not exists conversations.users(
  user_id int not null,
  meta_data varchar(1024),
  primary key(user_id)
);

create table if not exists conversations.questions(
  question_id int not null,
  version int not null,
  question varchar(255) not null unique,
  primary key(question_id, version)
);

create table if not exists conversations.answers(
  answer_id int not null,
  user_id int not null,
  question_id int not null,
  question_version int not null,
  answer varchar(1024),
  primary key(answer_id),
  foreign key (user_id) references conversations.users(user_id)
    on delete restrict
    on update restrict,
  foreign key (question_id, question_version) references conversations.questions(question_id, version)
    on delete restrict
    on update restrict
);

insert into conversations.users(user_id, meta_data) values (0, 'name: "James Percent", address: "15 Island Ave", title: "Falconer"');
insert into conversations.users(user_id, meta_data) values(1, 'name: "James1"');
insert into conversations.users(user_id, meta_data) values(2, 'name: "James2"');
insert into conversations.users(user_id, meta_data) values(3, 'name: "James3"');

insert into conversations.questions(question_id, version, question) values (0, 0, 'Hey, what did you do today');
insert into conversations.questions(question_id, version, question) values (0, 1, 'Hi, what did you do this fine day');
insert into conversations.questions(question_id, version, question) values (0, 2, 'Hello, what did you do today');
insert into conversations.questions(question_id, version, question) values (1, 0, 'Hello, what did you do yesterday');
insert into conversations.questions(question_id, version, question) values (1, 1, 'Heya, what did you do yesterday');

insert into conversations.answers(answer_id, question_id, question_version, user_id, answer) values(0, 0, 0, 0, 'Rude question');
insert into conversations.answers(answer_id, question_id, question_version, user_id, answer) values(1, 0, 0, 1, 'Be polite');
insert into conversations.answers(answer_id, question_id, question_version, user_id, answer) values(2, 0, 1, 0, 'Still rude question');
insert into conversations.answers(answer_id, question_id, question_version, user_id, answer) values(3, 0, 1, 1, 'Nothing');
insert into conversations.answers(answer_id, question_id, question_version, user_id, answer) values(4, 0, 2, 0, 'Worked a lot, you');

commit;
