# The Riddle That Seems Impossible Even If You Know The Answer


This is an application that demonstrates the results of the "100 prisoners problem", firstly introduced and published by Gál and Miltersen and explained by Muller at Veritasium YouTube channel.

You can find the video [here](https://www.youtube.com/watch?v=iSNsgj1OCLA), I recommend you watch it before you try the application.


You can see the problem actually defined in this text by Flajolet and Sedgewick which is slightly differnet to the published by Gal and Miltersen (Wikipedia):

"The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. The drawers are closed again afterwards. If, during this search, every prisoner finds his number in one of the drawers, all prisoners are pardoned. If just one prisoner does not find his number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the drawers. What is the prisoners' best strategy?"


We will use numbered boxes and numbered paper slips instead of cupboards and just numbers.

### Exercise 1: Demonstrate the favorable cases for prisoners

The video provides an excellent explanation about the problem and its solution. The solution is all about following a loop. In data structure terms, we could consider this as a Linked List. In simple termns, each prisoner opens the box with its prisoner number on it and then take the number on the slip inside of the box. Then, the prisoner check the number on the slip and opens that exact box with the same number on it. The prisoner repeats the process of box x -> slip n -> box n -> slip i -> box ... until the prisoner finds its own number in the slip of the last box (slip x). Of course, if a prisoner opens 50 boxes and does not find their number, then the prisoners are not to be safed.

In summary the solution to the problem is summarized in one sentence: In order to safe all prisoners, no loop with more than 50 boxes shall be generated when numbers are randomly distributed across boxes. 

Making the proper calculations, we can see that the favorable cases for prisoners are: 

random number distributions and favorable cases

1K   : 31.1%\
10K  : 31.259%\
100K : 31.352%\
1M   : 31,1083%

If tests are repeated for, let's say, 10K or 100K the probabilities change but the difference is not significant.
