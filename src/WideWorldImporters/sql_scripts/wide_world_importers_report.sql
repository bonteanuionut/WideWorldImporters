with wide_world_importers_report as (
    select
        sup_trans.SupplierID
        , sup.SupplierName
        , sup_trans.SupplierInvoiceNumber
        -- cast to date to avoid data type malfunction
        , cast(sup_trans.TransactionDate as date) as TransactionDate
        , sup_trans.AmountExcludingTax
        -- change from 1s and 0s to 'YES' and 'NO' to match the excel sample output
        , case
            when sup_trans.isFinalized = 1 then 'YES'
            else 'NO'
        end as isFinalized
        , po.PurchaseOrderID
        -- cast to date to avoid data type corruption
        , cast(po.OrderDate as date) as OrderDate
        , pol.PurchaseOrderLineID
        , pol.StockItemID
        -- remove double-quotes to match the excel sample output
        , replace(pol.Description, '"', '') as Description
        , pol.ReceivedOuters
        , pol.ExpectedUnitPricePerOuter
    from
        Purchasing.Suppliers as sup
        inner join Purchasing.SupplierTransactions as sup_trans
            on sup.SupplierID = sup_trans.SupplierID
        inner join Purchasing.PurchaseOrders as po
            on
                sup.SupplierID = po.SupplierID
                and sup.SupplierReference = po.SupplierReference
                and sup_trans.PurchaseOrderID = po.PurchaseOrderID
        inner join
            Purchasing.PurchaseOrderLines as pol
            on po.PurchaseOrderID = pol.PurchaseOrderID
    where
        1 = 1
        --Transaction type filter: 5
        {% if transaction_type %}
            and sup_trans.TransactionTypeID = {{ transaction_type }}
        {% endif %}
        --Transaction Month date filter: 11
        {% if transaction_month %}
            and month(sup_trans.TransactionDate) = {{ transaction_month }}
        {% endif %}
        --Transaction Year date filter: 2015
        {% if transaction_year %}
            and year(sup_trans.TransactionDate) = {{ transaction_year }}
        {% endif %}

)

select *
from wide_world_importers_report
