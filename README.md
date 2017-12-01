Greg Judd - Rolepoint Coding Exercise

Decisions:

I think the main design decision I made was to implement my own function to do the searching of the text.
I did this primarily because I haven't used any purpose built Python text search librarires and thought too much of the 
1-2 hour time limit would be taken up by this. Instead I just wrote my own simple function that checks if the search term is
contained within any of the fields for a given contact and matches if so. Usually I am against reinventing the wheel!

Also given the brevity of the task, I simply loaded the JSON file into memory vs implement any more heavy weight solutions
(see below).

I've used Flask, but tried to structure it in a way that would be conducive to extending this code into a more featured 
application. 

And I used pytest to add some tests cases just to give an idea of how I might test things.

To run the tests, cd into the 'tests' directory and 'py.test test_contact_search'.

To run the web app 'python manage.py'.


Next Steps / Improvements:

Add more tests certainly.

Using a purpose built library for this would I'm sure be more robust and performant. Something like whoosh may work, but 
I'd have to look into it a little more.

Providing a nicer user interface as the one I've implemented is very basic. Nicer formatting of the results would also help.

I imagine the contacts list is going to get much larger, so preloading all of it into memory perhaps won't be feasible.
This may change the design quite significantly as reading from file on each request could lead to a large performance hit.
If this were the case, we could use Redis or similar to cache popular results. Or move the contacts to a database, but then 
we'd want to do the text searching on the db side, so would have to redesign.
