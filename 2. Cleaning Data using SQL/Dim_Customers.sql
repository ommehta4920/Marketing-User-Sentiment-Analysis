SELECT 
  * 
FROM [PortfolioProject_MarketingAnalytics].dbo.customers;

SELECT
  *
FROM [PortfolioProject_MarketingAnalytics].dbo.geography;

-- *****************************************************************************************************************************
-- *****************************************************************************************************************************

-- Query to join Dim_Customers with Dim_Geography to enrich customer data with their geographic information
SELECT 
  c.CustomerID, -- Selects the unique indentifier for each customer
  c.CustomerName, -- Selects the name of each customer
  c.Email, -- Selects the email of each customer
  c.Gender, -- Selects the gender of each customer
  c.Age, -- Selects the age of each customer
  g.Country, -- Selects the country from geography table to enrich customer data
  g.city -- Selects the city from geography table to enrich customer data
FROM 
  [PortfolioProject_MarketingAnalytics].[dbo].[customers] AS c -- Specifies the alias 'c' for the dim_customers table
LEFT JOIN 
  [PortfolioProject_MarketingAnalytics].[dbo].[geography] AS g -- Specifies the alias 'g' for the dim_geography table
ON 
  c.GeographyID = g.GeographyID;

