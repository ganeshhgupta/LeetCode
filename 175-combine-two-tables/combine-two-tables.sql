# Write your MySQL query statement below
select firstName, lastName, city, state from PERSON LEFT JOIN ADDRESS ON PERSON.personid = ADDRESS.personid;