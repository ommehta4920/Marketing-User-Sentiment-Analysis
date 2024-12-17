SELECT 
  * 
FROM [PortfolioProject_MarketingAnalytics].[dbo].[customer_reviews];

-- *************************************************************************************************************************************
-- *************************************************************************************************************************************

-- Query to clean whitespace issue in the Review Text column
SELECT 
  ReviewID, -- Selects the unique identifier for each review
  CustomerID, -- Selects the unique identifier for each customer
  ProductID, -- Selects the unique identifier for each product
  ReviewDate, -- Selects the date when review was written
  Rating, -- Selects the numerical rating given by the customer. (e.g., 1 to 5 stars)
  -- Cleans up the ReviewText by replacing the double space with single space to ensure the text is more readable and standardize
  REPLACE(ReviewText, '  ', ' ') AS ReviewText 
FROM 
  [PortfolioProject_MarketingAnalytics].[dbo].[customer_reviews] -- Specifies the source table from which to select the data
