SELECT * FROM retail_sales;

SELECT COUNT(*) AS Total_Orders
FROM retail_sales;

SELECT SUM(Final_Amount) AS Total_Revenue
FROM retail_sales;

SELECT ROUND(AVG(Final_Amount), 2) AS Average_Order_Value
FROM retail_sales;

SELECT SUM(Quantity) AS Total_Quantity_Sold
FROM retail_sales;

SELECT Product_Name,
       SUM(Quantity) AS Total_Quantity
FROM retail_sales
GROUP BY Product_Name
ORDER BY Total_Quantity DESC
LIMIT 10;

SELECT Customer_Name,
       SUM(Final_Amount) AS Revenue
FROM retail_sales
GROUP BY Customer_Name
ORDER BY Revenue DESC
LIMIT 10;

SELECT Category,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY Category
ORDER BY Revenue DESC;

SELECT Store_Name,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY Store_Name
ORDER BY Revenue DESC;

SELECT State,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY State
ORDER BY Revenue DESC;

SELECT City,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY City
ORDER BY Revenue DESC;

SELECT Order_Year,
       Order_Month,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;

SELECT Order_Year,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY Order_Year
ORDER BY Order_Year;

SELECT Gender,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY Gender;

SELECT ROUND(AVG(Discount), 2) AS Average_Discount
FROM retail_sales;

SELECT MAX(Discount) AS Highest_Discount
FROM retail_sales;

SELECT Order_ID,
       Customer_Name,
       Final_Amount
FROM retail_sales
ORDER BY Final_Amount DESC
LIMIT 10;

SELECT Category,
       ROUND(AVG(Price), 2) AS Average_Price
FROM retail_sales
GROUP BY Category;

SELECT State,
       COUNT(Customer_ID) AS Total_Customers
FROM retail_sales
GROUP BY State
ORDER BY Total_Customers DESC;

SELECT Order_Day,
       ROUND(SUM(Final_Amount), 2) AS Revenue
FROM retail_sales
GROUP BY Order_Day
ORDER BY Order_Day;