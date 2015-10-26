# Fresh Tomatoes

Using the Starter Code as the starting point, function was added to ```fresh_tomatoes.py```
```python
def create_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
```
This new function is identical to ```create_movies_page```, except for the exclusion of the  
lines
```python
    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
```
<hr>

```media.py``` was modified to remove the import and the method call ```show_trailer```

<hr>

```entertainment_center.py``` was modified to work with a single movie object and call the new function.
```python
movies = [kill_bill]

fresh_tomatoes.create_movies_page(movies)
```
<hr>

The execution was as follows:
1. python entertainment_center.py

This created a file the local directory named ```fresh_tomatoes.html```, containing the single movie object kill_bill.


<hr>
### reference to ud036_StarterCode
https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py

