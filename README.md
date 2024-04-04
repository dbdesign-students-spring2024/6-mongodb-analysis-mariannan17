# AirBnB MongoDB Analysis

## Data Set Details
My data set represents the AirBnB listings in Naples, Campania, Italy. This data set comes from the website: [AirBnB listings data](http://insideairbnb.com/get-the-data.html). This website contains a lot of information for the many different regions where AirBnBs take place. The format to my original data file was in CSV format. 

#### Raw data
| id | listing_url|scrape_id|last_scraped|source,name|description|neighborhood_overview|picture_url|host_id|...|
|---|---|---|---|---|---|---|---|---|---|
|1036130317897450539| https://www.airbnb.com/rooms/1036130317897450539,20240324214356|2024-03-24| city scrape| Affitto camera in appartamento| Take a break and take a break at this peaceful oasis| My apartment is near the subway and all the amenities like pharmacy supermarkets shops bakeries bars|https://a0.muscache.com/pictures/7682be5f-d343-4e7b-b7ee-e950c2dcaccc.jpg| 548804637|
|1039263035915366113| https://www.airbnb.com/rooms/1039263035915366113,20240324214356| 2024-03-24| city scrape| Appartamento con terrazzo| Relax in this quiet space in a central location.| |https://a0.muscache.com/pictures/hosting/Hosting-1039263035915366113/original/aa6c7ba3-0314-4eee-9579-3a2dc6f67cf4.jpeg|516549962|
|...|

Link to the full original data set can be found [here](data/listings.csv)

#### Data Scrubbing
There weren't many problems present in the data set. Nevertheless, I decided to get rid of a few columns in order to make the data set slightly smaller and easier to understand. I decided to get rid of: `last_scraped`, `source`, `neighbourhood_group_cleansed`, `calendar_updated` and `calendar_last_scraped`. The reason being is that these columns are not necessary for the analysis that needs to be conducted on this dataset and I did not think that they were very relevant to the task at hand. The reason why I got rid of  `neighbourhood_group_cleansed`, even though in one of the analysis it could have been utilized is because there was no data for any of the rows/ids in the dataset. 


## Analysis 
1. For this query I am supposed to present two documents from the `listings` collection in any order. This code that I wrote made sure to do this for me.

Code:
```
db.listings.find().limit(2)
```
Output:
```
{ "_id" : ObjectId("660eeecec34b7fbd6a59f2c1"), "id" : NumberLong("1036130317897450539"), "listing_url" : "https://www.airbnb.com/rooms/1036130317897450539", "scrape_id" : NumberLong("20240324214356"), "name" : "Affitto camera in appartamento", "description" : "Take a break and take a break at this peaceful oasis. My apartment is near the subway and all the amenities like pharmacy supermarkets shops bakeries bars", "neighborhood_overview" : "", "picture_url" : "https://a0.muscache.com/pictures/7682be5f-d343-4e7b-b7ee-e950c2dcaccc.jpg", "host_id" : 548804637, "host_url" : "https://www.airbnb.com/users/show/548804637", "host_name" : "Anna", "host_since" : "2023-11-30", "host_location" : "Naples, Italy", "host_about" : "", "host_response_time" : "within a day", "host_response_rate" : "50%", "host_acceptance_rate" : "100%", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/User-548804637/original/115cc38e-8dcc-46e1-99f8-c5a569572998.jpeg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/pictures/user/User-548804637/original/115cc38e-8dcc-46e1-99f8-c5a569572998.jpeg?aki_policy=profile_x_medium", "host_neighbourhood" : "", "host_listings_count" : 2, "host_total_listings_count" : 2, "host_verifications" : "['email', 'phone']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "", "neighbourhood_cleansed" : "Scampia", "latitude" : 40.89460737372267, "longitude" : 14.246148101903206, "property_type" : "Private room in home", "room_type" : "Private room", "accommodates" : 2, "bathrooms" : 1, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"Free parking on premises\", \"TV\", \"Kitchen\", \"Washer\", \"Wifi\", \"Air conditioning\"]", "price" : "$28.00", "minimum_nights" : 1, "maximum_nights" : 365, "minimum_minimum_nights" : 1, "maximum_minimum_nights" : 1, "minimum_maximum_nights" : 365, "maximum_maximum_nights" : 365, "minimum_nights_avg_ntm" : 1, "maximum_nights_avg_ntm" : 365, "has_availability" : "t", "availability_30" : 29, "availability_60" : 59, "availability_90" : 89, "availability_365" : 269, "number_of_reviews" : 0, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "", "last_review" : "", "review_scores_rating" : "", "review_scores_accuracy" : "", "review_scores_cleanliness" : "", "review_scores_checkin" : "", "review_scores_communication" : "", "review_scores_location" : "", "review_scores_value" : "", "license" : "", "instant_bookable" : "f", "calculated_host_listings_count" : 2, "calculated_host_listings_count_entire_homes" : 0, "calculated_host_listings_count_private_rooms" : 2, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : "" }

{ "_id" : ObjectId("660eeecec34b7fbd6a59f2c2"), "id" : NumberLong("1039263035915366113"), "listing_url" : "https://www.airbnb.com/rooms/1039263035915366113", "scrape_id" : NumberLong("20240324214356"), "name" : "Appartamento con terrazzo", "description" : "Relax in this quiet space in a central location.", "neighborhood_overview" : "", "picture_url" : "https://a0.muscache.com/pictures/hosting/Hosting-1039263035915366113/original/aa6c7ba3-0314-4eee-9579-3a2dc6f67cf4.jpeg", "host_id" : 516549962, "host_url" : "https://www.airbnb.com/users/show/516549962", "host_name" : "Massimo", "host_since" : "2023-05-25", "host_location" : "", "host_about" : "", "host_response_time" : "N/A", "host_response_rate" : "N/A", "host_acceptance_rate" : "N/A", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/defaults/user_pic-50x50.png?v=3", "host_picture_url" : "https://a0.muscache.com/defaults/user_pic-225x225.png?v=3", "host_neighbourhood" : "", "host_listings_count" : 1, "host_total_listings_count" : 2, "host_verifications" : "['email', 'phone']", "host_has_profile_pic" : "f", "host_identity_verified" : "t", "neighbourhood" : "", "neighbourhood_cleansed" : "San Ferdinando", "latitude" : 40.833355, "longitude" : 14.2492488, "property_type" : "Entire rental unit", "room_type" : "Entire home/apt", "accommodates" : 4, "bathrooms" : 1, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"TV\", \"Paid parking on premises\", \"Kitchen\", \"Washer\", \"Wifi\", \"Air conditioning\"]", "price" : "$250.00", "minimum_nights" : 1, "maximum_nights" : 365, "minimum_minimum_nights" : 2, "maximum_minimum_nights" : 2, "minimum_maximum_nights" : 365, "maximum_maximum_nights" : 365, "minimum_nights_avg_ntm" : 2, "maximum_nights_avg_ntm" : 365, "has_availability" : "t", "availability_30" : 30, "availability_60" : 60, "availability_90" : 90, "availability_365" : 271, "number_of_reviews" : 0, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "", "last_review" : "", "review_scores_rating" : "", "review_scores_accuracy" : "", "review_scores_cleanliness" : "", "review_scores_checkin" : "", "review_scores_communication" : "", "review_scores_location" : "", "review_scores_value" : "", "license" : "", "instant_bookable" : "t", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 1, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : "" }
```
This just presents the user with two different documents, in this case, two different AirBnB listings and lists all their characteristics. 

2. For this query I must display 10 documents in any order but with the `pretty()` function

Code:
```
db.listings.find().limit(10).pretty()
```
Output:
```
{
	"_id" : ObjectId("660eeecec34b7fbd6a59f2c1"),
	"id" : NumberLong("1036130317897450539"),
	"listing_url" : "https://www.airbnb.com/rooms/1036130317897450539",
	"scrape_id" : NumberLong("20240324214356"),
	"name" : "Affitto camera in appartamento",
	"description" : "Take a break and take a break at this peaceful oasis. My apartment is near the subway and all the amenities like pharmacy supermarkets shops bakeries bars",
	"neighborhood_overview" : "",
	"picture_url" : "https://a0.muscache.com/pictures/7682be5f-d343-4e7b-b7ee-e950c2dcaccc.jpg",
	"host_id" : 548804637,
	"host_url" : "https://www.airbnb.com/users/show/548804637",
	"host_name" : "Anna",
	"host_since" : "2023-11-30",
	"host_location" : "Naples, Italy",
	"host_about" : "",
	"host_response_time" : "within a day",
	"host_response_rate" : "50%",
	"host_acceptance_rate" : "100%",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/User-548804637/original/115cc38e-8dcc-46e1-99f8-c5a569572998.jpeg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/pictures/user/User-548804637/original/115cc38e-8dcc-46e1-99f8-c5a569572998.jpeg?aki_policy=profile_x_medium",
	"host_neighbourhood" : "",
	"host_listings_count" : 2,
	"host_total_listings_count" : 2,
	"host_verifications" : "['email', 'phone']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "",
	"neighbourhood_cleansed" : "Scampia",
	"latitude" : 40.89460737372267,
	"longitude" : 14.246148101903206,
	"property_type" : "Private room in home",
	"room_type" : "Private room",
	"accommodates" : 2,
	"bathrooms" : 1,
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 1,
	"amenities" : "[\"Free parking on premises\", \"TV\", \"Kitchen\", \"Washer\", \"Wifi\", \"Air conditioning\"]",
	"price" : "$28.00",
	"minimum_nights" : 1,
	"maximum_nights" : 365,
	"minimum_minimum_nights" : 1,
	"maximum_minimum_nights" : 1,
	"minimum_maximum_nights" : 365,
	"maximum_maximum_nights" : 365,
	"minimum_nights_avg_ntm" : 1,
	"maximum_nights_avg_ntm" : 365,
	"has_availability" : "t",
	"availability_30" : 29,
	"availability_60" : 59,
	"availability_90" : 89,
	"availability_365" : 269,
	"number_of_reviews" : 0,
	"number_of_reviews_ltm" : 0,
	"number_of_reviews_l30d" : 0,
	"first_review" : "",
	"last_review" : "",
	"review_scores_rating" : "",
	"review_scores_accuracy" : "",
	"review_scores_cleanliness" : "",
	"review_scores_checkin" : "",
	"review_scores_communication" : "",
	"review_scores_location" : "",
	"review_scores_value" : "",
	"license" : "",
	"instant_bookable" : "f",
	"calculated_host_listings_count" : 2,
	"calculated_host_listings_count_entire_homes" : 0,
	"calculated_host_listings_count_private_rooms" : 2,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : ""
}
{
	"_id" : ObjectId("660eeecec34b7fbd6a59f2c2"),
	"id" : NumberLong("1039263035915366113"),
	"listing_url" : "https://www.airbnb.com/rooms/1039263035915366113",
	"scrape_id" : NumberLong("20240324214356"),
	"name" : "Appartamento con terrazzo",
	"description" : "Relax in this quiet space in a central location.",
	"neighborhood_overview" : "",
	"picture_url" : "https://a0.muscache.com/pictures/hosting/Hosting-1039263035915366113/original/aa6c7ba3-0314-4eee-9579-3a2dc6f67cf4.jpeg",
	"host_id" : 516549962,
	"host_url" : "https://www.airbnb.com/users/show/516549962",
	"host_name" : "Massimo",
	"host_since" : "2023-05-25",
	"host_location" : "",
	"host_about" : "",
	"host_response_time" : "N/A",
	"host_response_rate" : "N/A",
	"host_acceptance_rate" : "N/A",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/defaults/user_pic-50x50.png?v=3",
	"host_picture_url" : "https://a0.muscache.com/defaults/user_pic-225x225.png?v=3",
	"host_neighbourhood" : "",
	"host_listings_count" : 1,
	"host_total_listings_count" : 2,
	"host_verifications" : "['email', 'phone']",
	"host_has_profile_pic" : "f",
	"host_identity_verified" : "t",
	"neighbourhood" : "",
	"neighbourhood_cleansed" : "San Ferdinando",
	"latitude" : 40.833355,
	"longitude" : 14.2492488,
	"property_type" : "Entire rental unit",
	"room_type" : "Entire home/apt",
	"accommodates" : 4,
	"bathrooms" : 1,
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 1,
	"amenities" : "[\"TV\", \"Paid parking on premises\", \"Kitchen\", \"Washer\", \"Wifi\", \"Air conditioning\"]",
	"price" : "$250.00",
	"minimum_nights" : 1,
	"maximum_nights" : 365,
	"minimum_minimum_nights" : 2,
	"maximum_minimum_nights" : 2,
	"minimum_maximum_nights" : 365,
	"maximum_maximum_nights" : 365,
	"minimum_nights_avg_ntm" : 2,
	"maximum_nights_avg_ntm" : 365,
	"has_availability" : "t",
	"availability_30" : 30,
	"availability_60" : 60,
	"availability_90" : 90,
	"availability_365" : 271,
	"number_of_reviews" : 0,
	"number_of_reviews_ltm" : 0,
	"number_of_reviews_l30d" : 0,
	"first_review" : "",
	"last_review" : "",
	"review_scores_rating" : "",
	"review_scores_accuracy" : "",
	"review_scores_cleanliness" : "",
	"review_scores_checkin" : "",
	"review_scores_communication" : "",
	"review_scores_location" : "",
	"review_scores_value" : "",
	"license" : "",
	"instant_bookable" : "t",
	"calculated_host_listings_count" : 1,
	"calculated_host_listings_count_entire_homes" : 1,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : ""
}
{
	"_id" : ObjectId("660eeecec34b7fbd6a59f2c3"),
	"id" : 44165568,
	"listing_url" : "https://www.airbnb.com/rooms/44165568",
	"scrape_id" : NumberLong("20240324214356"),
	"name" : "Appartamento Sorrento",
	"description" : "The apartment is located on the ground floor in a courtyard inside the property.<br />The apartment includes a kitchen with an induction hob, a fridge, and all kitchen utensils. We provide linens.<br />Heating, air conditioning, TV and Wi-Fi",
	"neighborhood_overview" : "quartiere vicinissimo al centro di napoli siamo a 5 minuti dalla stazione di sangiovanni a teduccio e di barra in due fermate sarete a napoli centrale il centro di napoli ovvero piazza garibaldi .",
	"picture_url" : "https://a0.muscache.com/pictures/33152d19-09fb-4df6-ac41-fa27c4692c69.jpg",
	"host_id" : 248201660,
	"host_url" : "https://www.airbnb.com/users/show/248201660",
	"host_name" : "Immacolata",
	"host_since" : "2019-03-11",
	"host_location" : "Naples, Italy",
	"host_about" : "Ciao a tutti. Ho un gran piacere di conoscervi e di farmi conoscere, ma soprattutto sono lieta di ospitarvi nella mia struttura,comoda , e con tutti i confort che anche io vorrei quando mi sposto per visitare o per le vacanze. Estive o invernali. \nMi prendo cura del mio lavoro è tratto bene le persone che scelgono la mia casa per il loro soggiorno. ",
	"host_response_time" : "within an hour",
	"host_response_rate" : "90%",
	"host_acceptance_rate" : "97%",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/User-248201660/original/576bfea5-1bc9-49e7-a148-83747ab43689.jpeg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/pictures/user/User-248201660/original/576bfea5-1bc9-49e7-a148-83747ab43689.jpeg?aki_policy=profile_x_medium",
	"host_neighbourhood" : "",
	"host_listings_count" : 6,
	"host_total_listings_count" : 10,
	"host_verifications" : "['email', 'phone']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "Napoli, Campania, Italy",
	"neighbourhood_cleansed" : "San Giovanni a Teduccio",
	"latitude" : 40.83701,
	"longitude" : 14.31083,
	"property_type" : "Entire rental unit",
	"room_type" : "Entire home/apt",
	"accommodates" : 2,
	"bathrooms" : 1,
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 2,
	"amenities" : "[\"Bed linens\", \"Dining table\", \"TV\", \"Backyard\", \"Freezer\", \"Security cameras on property\", \"Bidet\", \"Iron\", \"Free street parking\", \"Outdoor dining area\", \"Ethernet connection\", \"Hot water kettle\", \"Baby safety gates\", \"Heating\", \"Refrigerator\", \"Lockbox\", \"Kitchen\", \"Crib\", \"Dedicated workspace\", \"Single level home\", \"Hangers\", \"Paid dryer \\u2013 In building\", \"Wifi\", \"Extra pillows and blankets\", \"Laundromat nearby\", \"Clothing storage: closet\", \"Paid washer \\u2013 In building\", \"Paid parking lot on premises\", \"Hot water\", \"Hair dryer\", \"Dishes and silverware\", \"Private entrance\", \"Stainless steel electric stove\", \"Courtyard view\", \"Fire extinguisher\", \"Essentials\", \"Cooking basics\", \"Long term stays allowed\", \"Drying rack for clothing\", \"Central air conditioning\", \"Self check-in\", \"Pack \\u2019n play/Travel crib\", \"Coffee maker: espresso machine\"]",
	"price" : "$51.00",
	"minimum_nights" : 2,
	"maximum_nights" : 365,
	"minimum_minimum_nights" : 2,
	"maximum_minimum_nights" : 2,
	"minimum_maximum_nights" : 1125,
	"maximum_maximum_nights" : 1125,
	"minimum_nights_avg_ntm" : 2,
	"maximum_nights_avg_ntm" : 1125,
	"has_availability" : "t",
	"availability_30" : 24,
	"availability_60" : 45,
	"availability_90" : 75,
	"availability_365" : 166,
	"number_of_reviews" : 37,
	"number_of_reviews_ltm" : 20,
	"number_of_reviews_l30d" : 0,
	"first_review" : "2021-07-31",
	"last_review" : "2024-01-12",
	"review_scores_rating" : 4.3,
	"review_scores_accuracy" : 4.41,
	"review_scores_cleanliness" : 4.62,
	"review_scores_checkin" : 4.41,
	"review_scores_communication" : 4.62,
	"review_scores_location" : 3.89,
	"review_scores_value" : 4.27,
	"license" : "",
	"instant_bookable" : "t",
	"calculated_host_listings_count" : 6,
	"calculated_host_listings_count_entire_homes" : 6,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 1.15
}
```

