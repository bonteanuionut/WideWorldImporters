with wide_world_importers_report as (
	select
		sup_trans.SupplierID
		,	sup.SupplierName
		,	sup_trans.SupplierInvoiceNumber
		,	cast(sup_trans.TransactionDate as date) as TransactionDate
		,	sup_trans.AmountExcludingTax
		,	case
				when sup_trans.isFinalized = 1 then 'YES'
				else 'NO'
			end as isFinalized
		,	po.PurchaseOrderID
		,	cast(po.OrderDate as date) as OrderDate
		,	pol.PurchaseOrderLineID
		,	pol.StockItemID
		,	replace(pol.Description, '"', '') as Description
		,	pol.ReceivedOuters
		,	pol.ExpectedUnitPricePerOuter
	from
		Purchasing.Suppliers as sup
	join
		Purchasing.SupplierTransactions	as sup_trans
			on sup.SupplierID = sup_trans.SupplierID
	join
		Purchasing.PurchaseOrders as po
			on sup.SupplierID = po.SupplierID
				and sup.SupplierReference = po.SupplierReference
				and sup_trans.PurchaseOrderID = po.PurchaseOrderID
	join
		Purchasing.PurchaseOrderLines as pol
			on po.PurchaseOrderID = pol.PurchaseOrderID
	where sup_trans.TransactionTypeID = ? --Transaction type filter: 5
		and month(sup_trans.TransactionDate) = ? --Transaction Month date filter: 11
		and year(sup_trans.TransactionDate) = ? --Transaction Year date filter: 2015

)

select *
from wide_world_importers_report