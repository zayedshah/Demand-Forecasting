I got your running stats from your github gist.

In the first approach, I used KMeans Clustering on Distance and Duration to group them into 3 routes. It gave me the length of the 3 routes and the average time to run each one as follows.

- Route 1 - 7297 meters, 50 mins
- Route 2 - 6330 meters, 40 mins
- Route 3 - 6858 meters, 51 mins

You seem to have run more often on Route 1 - 42 days out of the 100 days, so perhaps this is your favourite route. According to this approach of analysis, you ran 30 days on Route 2 and 28 days on Route 3.

> I observed that the time for Route 1 and Route 3 are very similar (50, 51 mins), even though Route 1 has longer distance (7297, 6858 meters). So I thought I should try to group them just using Distance. The time could vary, sometimes a runner could have taken it easy some days on the same route, but the distance covered ought to have been the same.

So, in the second approach, I grouped them just using Distance, and I got the 3 routes as follows (corresponding to the results from first approach). I had sorted the distance, divided them into 33, 33 and 34 days of data.

- Route 1 - 7336 meters, 48 mins
- Route 2 - 6356 meters, 41 mins
- Route 3 - 6947 meters, 52 mins

It looks like there is not much difference in the results from Approach 1 and 2. So Scikit-Learn's KMeans Clustering seems to have done a good job in grouping the 3 routes using Distance and Duration.
