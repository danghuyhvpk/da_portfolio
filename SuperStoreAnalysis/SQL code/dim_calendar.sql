create table dim_calendar as (
select 
	   orders.order_date as order_date, 
	   orders.years as years, 
       orders.months as months, 
       orders.days as days,
       mid(orders.months, 1 , 3) as mon_short,
	   month(order_date) as mon_no,
       CEILING( MONTH(order_date) / 3) as quater
from orders)