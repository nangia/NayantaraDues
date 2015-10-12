# Nayantara Sahgal

[Nayantara Sahgal](https://en.wikipedia.org/wiki/Nayantara_Sahgal "Nayantara Sahgal") has recently been in news as she as returned the [Sahitya Academy Award](https://en.wikipedia.org/wiki/Sahitya_Akademi_Award). She got this award in 1986. While it has been [reported](http://www.thehindu.com/news/national/sahgal-returns-award-money/article7750688.ece?homepage=true) that she has returned the money as well, this page is an attempt to calculate the fair amount she actually owes. 

# Details of Calculations

This python program calculates the amounts due based upon different models. The assumptions used are:

* Rs. 50000 award money
* Interest rates models at 8%, 10% or 15% per annum

As reported in the Hindu article, she doesn't seem to remember well, what the award amount was, so I have just taken Rs. 50000. 

# TODO

A good thing would be to modify this program based on the varying interest rates as are reported [here](http://www.allbankingsolutions.com/Banking-Tutor/Chronology-Bank-Rate-India.shtml).  This should be fairly easy to do by writing another class modelling this varying rate of interest (just inherit from class BaseInterestModel).

# Summary

For those in hurry and don't want to run the program. Here's the current output of the program based on various possible models that might be used:

* Nayantara owes Sahitya Academy INR 465,863.74 (Interest of 8% per annum) 
* Nayantara owes Sahitya Academy INR 7,390,039.90 (Interest of 10% per annum) 
* Nayantara owes Sahitya Academy INR 425,484,901.22 (Interest of 15% per annum) 