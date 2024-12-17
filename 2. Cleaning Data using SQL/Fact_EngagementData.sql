SELECT 
  * 
FROM [PortfolioProject_MarketingAnalytics].[dbo].[engagement_data];

-- ******************************************************************************************************************************
-- ******************************************************************************************************************************

-- Query to clean and normalize the engagement_data table
SELECT 
  EngagementID, -- Selects the unique identifier for each engagement record
  ContentID, -- Selects the unique identifier for each piece of content
  CampaignID, -- Selects the unique identifier for each marketing campaign
  ProductID, -- Selects the unique identifier for each product
  UPPER(REPLACE(ContentType, 'Socialmedia', 'Social Media')) AS ContentType, -- Replaces "Socialmedia" with "Social Media" and converts all ContentType values to uppercase
  LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) -1) AS Views, -- Extracts the views part from the ViewsClicksCombined by taking substring before the '-' character
  RIGHT(ViewsClicksCombined, LEN(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined)) AS Clicks, -- Extracts the clicks part from the ViewsClicksCombined by taking the substring after the '-' character
  Likes, -- Selects the number of likes the content received
  -- Converts the EngagementDate to the dd.mm.yyyy format
  FORMAT(CONVERT(DATE, EngagementDate), 'dd.MM.yyyy') AS EngagementDate -- Converts and formats the date as dd.mm.yyyy
FROM 
  [PortfolioProject_MarketingAnalytics].[dbo].[engagement_data] -- Specifies the source table from which to select the data
WHERE 
  ContentType != 'Newsletter';
