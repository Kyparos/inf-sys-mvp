CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "nickname" varchar,
  "age" int,
  "sex" bool
);

CREATE TABLE "heart_attack" (
  "id" SERIAL PRIMARY KEY,
  "user_id" int,
  "cp" int,
  "trtbps" int,
  "chol" int,
  "fbs" int,
  "restecg" int,
  "thalachh" int,
  "exng" int,
  "oldpeak" float,
  "slp" int,
  "caa" int
);

ALTER TABLE "heart_attack" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

