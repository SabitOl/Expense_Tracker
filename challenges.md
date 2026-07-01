# Here's what I encountered building this and some decisions I made

- Why have two while loops? It's to allow for restarting and continuity ofuser input. 

When the inner loops breaks as a result of wrong value entered, the inner loops only breaks. And then returns to the outer loop. This restarts the expense tracker automatically.

- I noticed without "break" and a user enters the wrong value type, it still gets added to the storage csv file.

So, I decided to include "break" at some points. This stops wrong value to be ever written in the csv file.

The while loops are working. But somehow, the file reader is sending an error message. Will definitely fix this next.