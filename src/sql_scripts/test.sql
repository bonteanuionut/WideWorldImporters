with purchase_orders_rank as (
	select
		PurchaseOrderID
		,	OrderDate
		,	SupplierID
		,	row_number() over(partition by  SupplierId, SupplierReference order by OrderDate desc) as rnk
	from
		Purchasing.PurchaseOrders
)

, purchase_orders_dedup as (
	select *
	from
		purchase_orders_rank
	where rnk = 1
)

, filtered_supplier_transactions as (
	select
		SupplierID
		,	SupplierInvoiceNumber
		,	TransactionDate
		,	AmountExcludingTax
		,	isFinalized
	from
		Purchasing.SupplierTransactions
	where TransactionTypeID = 5 --Transaction type filter: 5
		and month(TransactionDate) = 11 --Transaction Month date filter: 11
		and year(TransactionDate) = 2015 --Transaction Year date filter: 2015
		
)

, cte_final as (
	select
		sup_trans.SupplierID
		,	sup.SupplierName
		,	sup_trans.SupplierInvoiceNumber
		,	cast(sup_trans.TransactionDate as date) as TransactionDate
		,	sup_trans.AmountExcludingTax
		,	sup_trans.isFinalized
		,	po.PurchaseOrderID
		,	cast(po.OrderDate as date) as OrderDate
		,	pol.PurchaseOrderLineID
		,	pol.StockItemID
		,	pol.Description
		,	pol.ReceivedOuters
		,	pol.ExpectedUnitPricePerOuter
	from
		Purchasing.Suppliers as sup
	join
		Purchasing.SupplierTransactions	as sup_trans
			on sup.SupplierID = sup_trans.SupplierID
	join
		purchase_orders_dedup as po
			on sup.SupplierID = po.SupplierID
	join
		Purchasing.PurchaseOrderLines as pol
			on po.PurchaseOrderID = pol.PurchaseOrderID
	where sup_trans.TransactionTypeID = 5 --Transaction type filter: 5
		and month(sup_trans.TransactionDate) = 11 --Transaction Month date filter: 11
		and year(sup_trans.TransactionDate) = 2015--Transaction Year date filter: 2015
)

select * from cte_final
