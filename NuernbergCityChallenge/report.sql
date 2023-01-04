select UserData as "NüCC Gebiet", count(*) as Total, 
( select count(*)  from caches where found=1 and UserData = x.UserData) as Founded,
( select count(*)  from caches where found=0 and UserData = x.UserData) as NotFounded
FROM caches as x where UserData <> "" group by UserData;
