# Intro to Programming
#### Forest Hill High School > Mr. James
This is a very brief introduction to programming. We will spend 2 days on HTML, 1 day on CSS, and 2 days on Python. We'll use HTML and CSS to create a simple web page. We'll learn how to add links, images, header text, tables and forms to our page. Then we'll use CSS to improve the styling.  
Python is a general purpose programming language, and we'll learn very basic programming skills including math functions, for loops, if-else statements, lists, dictionaries and simple functions.  
The code is already written for you, so you only need to copy and paste it, then click Run. You will make minor changes to the code to complete the worksheets.  
### Resources
- Online HTML and CSS editor [jsfiddle](http://www.jsfiddle.net)   
In the HTML square type Hello World, then click the Run button.  
You should see the output in the bottom right box.  
Use jsfiddle for all our HTML and CSS exercises.  
- See detailed documentation on each HTML tag at [w3schools](https://www.w3schools.com/html/default.asp).  
W3schools has comprehensive explanations of all HTML tags.  
- HTML [standard colors](https://www.w3schools.com/cssref/css_colors.asp), HTML [custom hex colors](https://www.w3schools.com/colors/colors_picker.asp), and [color schemes](https://coolors.co/)  
- The [GitHub html](http://www.github.com/joeyajames/jps/html) folder, [GitHub css](https://github.com/joeyajames/jps/tree/master/css) folder, and [GitHub python](https://github.com/joeyajames/jps/tree/master/python) folder with a bunch of different starter code.  
You can copy and paste the HTML and CSS into the jsfiddle boxes one at a time, or retype them.  
You should get output in the bottom right box. You can run the Python code in a repl window. 
- Online python interpreter, [repl.it](https://repl.it). Click +New Repl button, then select Python. We'll use this window to type in our Python code, run it, and view the output.
### Instructions: HTML part 1
- Complete the HTML-1 worksheet as you go.  
- Open a jsfiddle window, the GitHub html folder, and w3schools in separate tabs in your browser.
- Copy and paste the HTML code from each of the HTML files into the jsfiddle and run it to see what it does.  
**Do files in order: 1. text, 2. images, 3. tables, 3. lists**  
Try modifying the code to see how the output changes. Add an extra block of text, or an extra form field. Put your own message in. Try making your own table.  
### Instructions: HTML part 2  
- Complete the HTML-2 worksheet as you go. 
- **Do files in order: 1. html forms, 2. menu bar, 3. page template, 4. homepage.**  
Try modifying the code to see how the output changes. Add an extra block of text, or an extra form field. Put your own message in. Try making your own form. 
- After you get familiar with each of the files in the html folder, try building up your own personal webpage, similar to mine (homepage_2.html).  
Add images you find on the web. You just need the image url to put the image into your webpage. You can do a google image search, then right-click the image and copy url. You may need to resize the images e.g. 
```html
<img src="my-url" width=300px height=200px>
```  
Put things you like on your homepage.  
- If you want to save your homepage so others can view it on the web you can create a free GitHub account and follow these [instructions](http://jmcglone.com/guides/github-pages/).  I can help you with this.  
### Instructions: CSS
- Open a jsfiddle window, the GitHub css folder, and w3schools in separate tabs in your browser.
- Go to the css folder. Copy and paste the HTML code from each of the HTML files and the CSS code from the corresponding CSS file into the jsfiddle and run it. 
- **Do files in this order: 1. text, 2. table, 3. forms.**    
- Try modifying the code to see how the output changes. Go to [w3schools](https://www.w3schools.com/cssref/css_colors.asp) color picker and pick colors you like. There's a big selection of named colors, and you can also enter a hex color code (eg. #a355c4). You can use an html color picker to find a hex code for any color you like.
- Experiment with different font sizes. Try bigger and smaller font sizes using 14px or 25px. You can also use % for font sizes, where 125% is 25% bigger than normal.
- Try the mouse-over styles by changing the a:hover css. What happens when you add a p:hover style or an h3:hover style?
- Copy and paste my table styles into the jsfiddle css window and run it. Then try editing it to make your own style for tables by setting different values for table, tr, td, and th tags. What happens when you add a td:hover style?
### Instructions: Python part 1
- Open two browser tabs: one tab with the GitHub python folder, and another go to [repl.it](http://www.repl.it)
- Copy and paste the python code in each of the files from GitHub into the repl, and run.  
**Do in this order: 1. simple_math, 2. for_loops, 3. if_else, 4. lists**  
- Complete the accompanying worksheet.
- What character indicates a comment?
- What types of data can a list hold? Try integers, floating point numbers (decimals), and strings (text). 
- How do you access individual items in a list?
- Try writing your own for loop to do an operation on each item in a list (eg. add 5 to each number).  
### Instructions: Python part 2  
- Open two browser tabs: one tab with the GitHub python folder, and another go to [repl.it](http://www.repl.it)
- Copy and paste the python code in each of the files from GitHub into the repl, and run.  
- **Do in this order: 1. dictionaries, 2. functions.**  
- Complete the accompanying worksheet.
- How are dictionaries different from lists?  
- What kinds of things could functions be used for?  
### Definitions
- **HTML** is hypertext markup language, which is a formatted text that web browsers can understand and decode to show you formatted content.
- **CSS** means cascading style sheets. This allows web developers to customize styles for different elements across a whole website. Even if you have 500 different webpages on your site, you can change the paragraph font size by only changing the CSS document in 1 place, so it saves a lot of time and makes the whole site consistent.
- **JavaScript** is the most widely used web programming language that can execute in the browser when you click on an element. Many browser-based games are written in Javascript.
  - **Form** is a web page where the user is required to enter data and click a submit button. There are a variety of different form fields for different types of data input (e.g. check boxes, text fields, drop-down lists). Normally the form itself is written in HTML, and when  you click the submit button a Javascript is executed to process the data.
- **Python** is one of the most popular programming language for web development, machine learning, data analysis, and a variety of other things.
  - **List** is a data structure in Python that stores an array of items. Most other programming languages call this an array. Python lists can store any type of objects: integers, decimal numbers, text strings, or other.
  - **Dictionary** is a data structure that uses key-value pairs to store data. For example, 1:Bob, 2:Jenny, 3:Frank. Or, Caylus:6135728097, Howard:6137892854.  
  - **Boolean** is an expression that evaluates to True or False (or 1/0, or On/Off). Examples of Boolean expressions: age == 16, height > 65, length < 36, direction == 'up'. Boolean expressions are used in if statements.
