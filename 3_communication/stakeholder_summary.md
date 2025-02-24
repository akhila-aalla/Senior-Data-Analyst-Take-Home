#Stakeholder Summary - Fetch Data Analysis

**Subject:** Data Quality Insights & Key Trends for Fetch Analysis 

Hi [Stakeholder's Name],

During our analysis of Fetch's data, we identified several **data quality issues** and uncovered key trends that could impact business decisions.

---

### **Key Data Quality Issues & Open Questions**
1. **Missing Data:**  
   - `CATEGORY_4` in the product catalog is **92% missing**, making it unreliable.
   - **5,762 transactions (~11.5%)** are missing barcodes, making product linkage difficult.
   - **User birth dates:** Many entries show `1970-01-01`, likely a placeholder rather than real data.

2. **Duplicates & Data Integrity:**  
   - **215 duplicate product entries** and **171 duplicate transactions** detected.

3. **Outstanding Questions:**  
   - Should `CATEGORY_4` be removed or imputed?
   - Can we confirm whether missing `BARCODE` values are a system issue or expected behavior?
   - Do we have an alternative way to verify **user age** if `BIRTH_DATE` is unreliable?

---

### **Interesting Trend: Fetch’s Power Users Drive High Engagement**
- The **top 10% of users** (power users) contribute to **~45% of total sales**.
- These users engage frequently, scanning **5X more receipts** than the average user.
- A **loyalty-based rewards strategy** could further enhance engagement and retention.

---

### **New Insight: Health & Wellness Sales Are Growing Rapidly**
- The **Health & Wellness category accounts for ~18% of total sales** across all generations.
- **Gen Z & Millennials** contribute the most, making up **~65%** of category sales.
- A targeted **marketing campaign for Health & Wellness products** could drive further growth.

---

### **Action Needed**
To ensure more accurate analysis and business insights, we need your input on:
1. **Data Fixes:** Should we clean or discard unreliable fields like `CATEGORY_4` and missing barcodes?
2. **User Age Validation:** Can we cross-check **birth date inconsistencies** with alternative sources?
3. **Power User Strategy:** Would the team be interested in **exploring a retention program for top users**?

Let us know your thoughts, and we’d be happy to refine our approach.

Best,  
Akhila Aalla
aakhiladata@gmail.com
