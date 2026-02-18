with purchase_orders_ranking as (
	select
		*
		,	row_number() over(
            partition by SupplierID, SupplierReference, OrderDate
            order by LastEditedWhen
        ) as rnk -- order ascending so we get the first entry of the duplicates (assuming the rest of them were a mistake and not intended modifications)
	from
		Purchasing.PurchaseOrders
)

select
	*
from purchase_orders_ranking
where rnk > 1 -- return duplicates (1st rank being the 'original')