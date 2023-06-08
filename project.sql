1.
Select COUNT(id),extract(year from  release_date) as year
from movie
where year != NULL
GROUP by year
order by year;


2.
select g.id, g.name,
  count(m.movie_id) as counter
from genre g full outer join movie_genres m
on m.genre_id = g.id
group by g.id, g.name

3.
select g.id, g.name,count(mv.id), extract(year from mv.release_date) as year, 
  count(m.movie_id) as counter 
  from movie mv
full outer join movie_genres m on mv.id = m.movie_id
full outer join genre g on m.genre_id = g.id
group by g.id, g.name,year
order by year

4.
SELECT max(budget), extract(year from  release_date) as year
from movie
GROUP by year
ORDER by year;

5.
select a.name,sum(m.revenue) as counter_rev,count(m.id) as counter_mov, extract(year from m.release_date) as year
from actor a full outer join movie_cast mc on mc.person_id = a.person_id
full outer join movie m on m.id = mc.movie_id
where a.name = 'Robert De Niro'
group by a.name,year
order by year;


6.
select avg(rating), user_id
from ratings
group by user_id;

7.
select count(rating), user_id
from ratings
group by user_id;

8.
SELECT r.user_id,avg(r.rating),count(r.user_id)
from ratings r
group by user_id;

9.
select g.name , avg(r.rating)
from genre g 
full outer join movie_genres m
on m.genre_id = g.id
full outer join movie mv
on mv.id= m.movie_id
full outer join ratings r
on mv.id= r.movie_id
group by g.name;



