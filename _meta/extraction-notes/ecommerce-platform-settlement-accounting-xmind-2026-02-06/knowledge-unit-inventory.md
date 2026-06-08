# Knowledge Unit Inventory

| knowledge_unit_id | source_units | role | extracted knowledge |
| --- | --- | --- | --- |
| KU-XMF-001 | XMF-001 to XMF-014 | root decision | The XMind compares two income recognition methods and recommends using platform settlement time rather than shipment/ERP time. |
| KU-XMF-002 | method comparison nodes | accounting basis | Shipment-based recognition is ERP-centered and fast for month-start reporting, but creates accounts-receivable reconciliation and internal/external book mismatch. Settlement-time recognition is platform-backend-centered and aligns internal/external income, but requires order cost matching and in-transit goods checks. |
| KU-XMF-003 | recommendation nodes | system-risk evidence | The recommendation is driven by Kuaimai/ERP income capture risk: platform coupons and refund synchronization can overstate or understate income and profit. |
| KU-XMF-004 | refund/coupon example nodes | edge-case model | A 37.99 order with customer payment 24.99 and platform coupon 15 should be zero after refund, but an ERP refund amount of 24.99 can leave 15 falsely recognized as income. A non-refunded 37.99 order with 22.99 payment and 15 coupon can be understated if the system takes only actual shipped amount. |
| KU-XMF-005 | after-sale sync nodes | control point | New stores must enable after-sale order sync promptly; otherwise platform refunds may not synchronize into Kuaimai ERP, causing inflated income and profit. |
| KU-XMF-006 | platform bill nodes | shared workflow | Platform settlement accounting uses funds bills to classify cash movements and settlement bills to book income/service fees and build cost-matching workpapers. |
| KU-XMF-007 | cost matching nodes | cost workflow | Match platform settlement bill order numbers with Kuaimai order costs; export Kuaimai data, create pivots, pivot settlement data, and check missing cost or erroneous cost without payment. |
| KU-XMF-008 | Douyin nodes | platform procedure | Douyin uses funds bill, settlement bill, guarantee bill, and manager account bill; deposits and manager-account spending need separate treatment. |
| KU-XMF-009 | Pinduoduo nodes | platform procedure | Pinduoduo uses funds bill, guarantee bill, cost matching, and promotion expense bill; only recent three months of orders may be exportable for cost matching. |
| KU-XMF-010 | Xiaohongshu nodes | platform procedure | Xiaohongshu settlement bills have multiple sub-sheets; income and expense need classification by matching settlement order amounts with Kuaimai order amounts and by reading funds bill notes. |
| KU-XMF-011 | Video Account nodes | platform procedure | Video Account funds bill movement type is the main income/expense classification basis; service recharge account and guarantee account need balance checks and possible expense reversal. |
| KU-XMF-012 | Taobao nodes | platform procedure | Taobao funds bill fields must be configured and history refreshed to expose order numbers; aggregate account, guarantee account, and promotion fee need separate checks. |
| KU-XMF-013 | image nodes | unresolved evidence | 28 screenshot nodes preserve UI paths/configuration evidence. Exact screenshot text was not OCR-transcribed in this run and is tracked in `image-asset-inventory.md`. |
