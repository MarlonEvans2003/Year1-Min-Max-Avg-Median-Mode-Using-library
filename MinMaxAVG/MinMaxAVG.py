maxN = 0
minN = 999
averageN = 0
tot = 0
#
#manual code for min, mac, average 
#
print("This code will find the min, max and average of this list [3,6,9,12,21,62,1,1,1,7]")
for x in[3,6,9,12,21,62,1,1,1,7]:
   if x > maxN:
            maxN = x
   elif x < minN:
             minN = x
   tot2 = tot + x

#
#
#calculate average manually
#
averageN = tot2/10
print ("max value  = "+ str(maxN))
print ("min Value  = "+ str(minN))
print ("average value = "+ str(averageN))

#
#
#code using statistics package
#
#
from statistics import mean, median, mode
#
#
somelist = [3,6,9,12,21,62,1,1,1,7]
print("This code will find the min, max, median and mode of this list " + str(somelist))
avg_value = mean(somelist) # All added and then divided by total of numbers
median_value = median(somelist) # Middle value
mode_value = mode(somelist) # Most occuring
min_value = min(somelist)
max_value = max(somelist)
#
#
print ("avg value = " + str(avg_value))
print ("median value = " + str(median_value))
print ("mode value = " + str(mode_value))
print ("min value = " + str(min_value))
print("max value = " + str(max_value))
