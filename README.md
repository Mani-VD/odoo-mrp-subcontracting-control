Odoo 18: Industrial Subcontracting & Wastage Control
📌 Overview
In industrial manufacturing hubs (like Coimbatore and Tiruppur), Job Work and Subcontracting are core operations. However, standard ERP flows often fail to account for material shrinkage (wastage) and lack real-time visibility of inventory residing at vendor sites.

This module provides an enterprise-grade solution to track, validate, and audit subcontracting operations, ensuring that material variances are approved by management before they affect the bottom line.

✨ Key Features
Wastage Tolerance Logic: Define "Allowed Wastage %" on the Bill of Materials (BoM).

Validation Gatekeeper: Automatically intercepts the "Receipt" process. If the returned quantity exceeds the allowed wastage, the system blocks validation until a Manufacturing Manager provides digital approval.

Subcontractor Stock Audit: A high-performance SQL-based reporting dashboard showing the real-time quantity and financial value of raw materials currently at vendor locations.

Odoo 18 Ready: Built using the latest framework standards, including list view architecture and invisible logic expressions (replacing deprecated attrs).

🛠 Technical Stack
Backend: Python 3.12, Odoo 18 Framework.

Database: PostgreSQL (Custom SQL Views for reporting performance).

Frontend: XML, QWeb (Optimized for Odoo 18 UI).

Security: Group-based access control (Manager vs. User approval levels).

🚀 Installation
Clone this repository into your Odoo custom_addons folder.

Install the mrp_subcontracting module (standard Odoo).

Update your App List and install "Industrial Job-Work & Wastage Tracker".

📊 Business Impact
Inventory Accuracy: Prevents "hidden" stock leaks by forcing manual reconciliation of missing items.

Financial Control: Gives management an immediate view of "Value at Risk" (total inventory value sitting in external vendor warehouses).

Process Automation: Reduces the need for manual spreadsheets to track "Challan" balances.
